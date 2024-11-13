#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDrive
import numpy as np
from math import pi, atan2

class HybridController(Node):
    def __init__(self):
        super().__init__('hybrid_controller')
        
        # Controller parameters
        self.declare_parameters(
            namespace='',
            parameters=[
                # PID parameters
                ('kp', 0.8),
                ('ki', 0.1),
                ('kd', 0.2),
                # Follow Gap parameters
                ('bubble_radius', 0.5),
                ('min_gap_width', 0.5),
                ('safety_factor', 1.0),
                # Speed control
                ('max_speed', 2.0),
                ('min_speed', 0.5),
                ('threshold_distance', 2.0)
            ]
        )
        
        # Get parameters
        self.load_parameters()
        
        # PID control state
        self.error_sum = 0.0
        self.last_error = 0.0
        self.last_time = self.get_clock().now()
        
        # Create subscribers and publishers
        self.scan_sub = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback,
            10
        )
        
        self.drive_pub = self.create_publisher(
            AckermannDrive,
            'ackermann_cmd',
            10
        )
        
        self.get_logger().info('Hybrid Controller initialized')

    def load_parameters(self):
        """Load parameters from ROS parameter server"""
        # PID parameters
        self.kp = self.get_parameter('kp').value
        self.ki = self.get_parameter('ki').value
        self.kd = self.get_parameter('kd').value
        
        # Follow Gap parameters
        self.bubble_radius = self.get_parameter('bubble_radius').value
        self.min_gap_width = self.get_parameter('min_gap_width').value
        self.safety_factor = self.get_parameter('safety_factor').value
        
        # Speed control parameters
        self.max_speed = self.get_parameter('max_speed').value
        self.min_speed = self.get_parameter('min_speed').value
        self.threshold_distance = self.get_parameter('threshold_distance').value

    def calculate_pid(self, error, dt):
        """Calculate PID control output"""
        # Proportional term
        p_term = self.kp * error
        
        # Integral term
        self.error_sum += error * dt
        i_term = self.ki * self.error_sum
        
        # Derivative term
        d_term = self.kd * (error - self.last_error) / dt if dt > 0 else 0
        
        # Update state
        self.last_error = error
        
        return p_term + i_term + d_term[1]

    def find_best_gap(self, ranges):
        """Implement Follow the Gap algorithm"""
        proc_ranges = np.array(ranges)
        
        # Find closest point
        closest_idx = np.argmin(proc_ranges)
        
        # Create safety bubble
        bubble_radius_idx = int(self.bubble_radius / (2 * pi / len(ranges)))
        start_idx = max(0, closest_idx - bubble_radius_idx)
        end_idx = min(len(ranges), closest_idx + bubble_radius_idx)
        proc_ranges[start_idx:end_idx] = 0
        
        # Find gaps
        gaps = []
        start_idx = 0
        in_gap = False
        
        for idx in range(len(proc_ranges)):
            if proc_ranges[idx] > self.min_gap_width and not in_gap:
                start_idx = idx
                in_gap = True
            elif proc_ranges[idx] <= self.min_gap_width and in_gap:
                gaps.append((start_idx, idx))
                in_gap = False
        
        if not gaps:
            return None, None
            
        # Find largest gap
        largest_gap = max(gaps, key=lambda x: x[1] - x[0])
        gap_center = (largest_gap[0] + largest_gap[1]) // 2
        
        return gap_center, proc_ranges[gap_center]

    def combine_controllers(self, pid_output, gap_heading, closest_distance):
        """Combine PID and Follow Gap outputs"""
        # Weight factors for combining controllers
        pid_weight = np.clip(closest_distance / self.threshold_distance, 0, 1)
        gap_weight = 1 - pid_weight
        
        # Combine steering commands
        steering_angle = (pid_weight * pid_output + 
                         gap_weight * gap_heading)
        
        return np.clip(steering_angle, -pi/4, pi/4)

    def calculate_speed(self, distance):
        """Calculate speed based on distance to obstacles"""
        if distance < self.min_gap_width:
            return 0.0
        
        speed = np.interp(
            distance,
            [self.min_gap_width, self.threshold_distance],
            [self.min_speed, self.max_speed]
        )
        
        return speed

    def scan_callback(self, msg):
        try:
            # Calculate time step
            current_time = self.get_clock().now()
            dt = (current_time - self.last_time).nanoseconds / 1e9
            
            # Find best gap
            gap_center, gap_distance = self.find_best_gap(msg.ranges)
            
            if gap_center is not None:
                # Calculate gap heading
                gap_angle = (gap_center / len(msg.ranges)) * 2 * pi - pi
                
                # Calculate cross-track error for PID
                closest_idx = np.argmin(msg.ranges)
                cross_track_error = msg.ranges[closest_idx] * np.sin(
                    (closest_idx / len(msg.ranges)) * 2 * pi - pi
                )
                
                # Calculate PID output
                pid_output = self.calculate_pid(cross_track_error, dt)
                
                # Combine controllers
                steering_angle = self.combine_controllers(
                    pid_output, 
                    gap_angle,
                    gap_distance
                )
                
                # Calculate speed
                speed = self.calculate_speed(gap_distance)
                
                # Create and publish command
                cmd = AckermannDrive()
                cmd.steering_angle = float(steering_angle)
                cmd.speed = float(speed)
                
                self.drive_pub.publish(cmd)
                
                # Update time
                self.last_time = current_time
                
                self.get_logger().debug(
                    f'Steering: {steering_angle:.2f}, Speed: {speed:.2f}'
                )
            
        except Exception as e:
            self.get_logger().error(f'Error processing scan: {str(e)}')

def main(args=None):
    rclpy.init(args=args)
    controller = HybridController()
    
    try:
        rclpy.spin(controller)
    except KeyboardInterrupt:
        pass
    finally:
        controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
