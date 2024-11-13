#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDrive
import numpy as np
from math import pi

class LidarPIDController(Node):
    def __init__(self):
        super().__init__('lidar_pid_controller')
        
        # PID parameters
        self.declare_parameters(
            namespace='',
            parameters=[
                ('kp', 0.8),
                ('ki', 0.1),
                ('kd', 0.2),
                ('target_distance', 1.0),
                ('max_steering_angle', 0.7),
                ('min_safe_distance', 0.5),
                ('scan_angle_front', 30),  # degrees
                ('scan_angle_side', 45)    # degrees
            ]
        )
        
        # Get parameters
        self.kp = self.get_parameter('kp').value
        self.ki = self.get_parameter('ki').value
        self.kd = self.get_parameter('kd').value
        self.target_distance = self.get_parameter('target_distance').value
        self.max_steering_angle = self.get_parameter('max_steering_angle').value
        self.min_safe_distance = self.get_parameter('min_safe_distance').value
        self.scan_angle_front = self.get_parameter('scan_angle_front').value
        self.scan_angle_side = self.get_parameter('scan_angle_side').value
        
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
        
        self.get_logger().info('LiDAR PID Controller initialized')

    def get_sector_distance(self, ranges, angle_min, angle_max):
        """Calculate minimum distance in a sector of the scan"""
        if len(ranges) == 0:
            return float('inf')
            
        angle_increment = 2 * pi / len(ranges)
        start_idx = int((angle_min * pi / 180) / angle_increment)
        end_idx = int((angle_max * pi / 180) / angle_increment)
        
        if start_idx < 0:
            start_idx += len(ranges)
        if end_idx < 0:
            end_idx += len(ranges)
            
        sector = ranges[start_idx:end_idx]
        valid_ranges = [r for r in sector if r >= self.min_safe_distance]
        
        return min(valid_ranges) if valid_ranges else float('inf')

    def calculate_pid(self, error, dt):
        """Calculate PID control value"""
        # Proportional term
        p_term = self.kp * error
        
        # Integral term
        self.error_sum += error * dt
        i_term = self.ki * self.error_sum
        
        # Derivative term
        d_term = self.kd * (error - self.last_error) / dt if dt > 0 else 0
        
        # Update state
        self.last_error = error
        
        # Calculate total control output
        control = p_term + i_term + d_term
        
        return np.clip(control, -self.max_steering_angle, self.max_steering_angle)

    def scan_callback(self, msg):
        try:
            # Get current time for dt calculation
            current_time = self.get_clock().now()
            dt = (current_time - self.last_time).nanoseconds / 1e9
            
            # Get distances in different sectors
            front_dist = self.get_sector_distance(
                msg.ranges, 
                -self.scan_angle_front/2, 
                self.scan_angle_front/2
            )
            
            left_dist = self.get_sector_distance(
                msg.ranges,
                self.scan_angle_side,
                self.scan_angle_side + 30
            )
            
            right_dist = self.get_sector_distance(
                msg.ranges,
                -self.scan_angle_side - 30,
                -self.scan_angle_side
            )
            
            # Calculate error (difference between left and right distances)
            error = left_dist - right_dist
            
            # Calculate steering angle using PID
            steering_angle = self.calculate_pid(error, dt)
            
            # Calculate speed based on front distance
            speed = self.calculate_speed(front_dist)
            
            # Create and publish Ackermann command
            cmd = AckermannDrive()
            cmd.steering_angle = float(steering_angle)
            cmd.speed = float(speed)
            
            self.drive_pub.publish(cmd)
            
            # Update time
            self.last_time = current_time
            
            # Log data
            self.get_logger().debug(
                f'Distances - Front: {front_dist:.2f}, '
                f'Left: {left_dist:.2f}, Right: {right_dist:.2f}, '
                f'Steering: {steering_angle:.2f}, Speed: {speed:.2f}'
            )
            
        except Exception as e:
            self.get_logger().error(f'Error processing scan: {str(e)}')

    def calculate_speed(self, front_distance):
        """Calculate speed based on front distance"""
        if front_distance < self.min_safe_distance:
            return 0.0
        
        # Linear speed scaling
        max_speed = 2.0
        min_speed = 0.5
        
        speed = np.interp(
            front_distance,
            [self.min_safe_distance, self.target_distance * 2],
            [min_speed, max_speed]
        )
        
        return speed

def main(args=None):
    rclpy.init(args=args)
    controller = LidarPIDController()
    
    try:
        rclpy.spin(controller)
    except KeyboardInterrupt:
        pass
    finally:
        controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
