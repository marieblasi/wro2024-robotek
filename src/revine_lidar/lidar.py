#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rplidar import RPLidar
import numpy as np
from math import pi
import time

class LidarNode(Node):
    def __init__(self):
        super().__init__('lidar_publisher')
        
        # LiDAR parameters
        self.port = '/dev/ttyUSB0'  # Default port for RPLidar
        self.scan_period = 0.1  # 10Hz scan rate
        
        # Initialize parameters
        self.declare_parameters(
            namespace='',
            parameters=[
                ('port', self.port),
                ('scan_period', self.scan_period),
                ('angle_min', -pi),
                ('angle_max', pi),
                ('range_min', 0.15),
                ('range_max', 12.0),
                ('angle_increment', pi/180.0)  # 1 degree resolution
            ]
        )
        
        # Get parameters
        self.port = self.get_parameter('port').value
        self.scan_period = self.get_parameter('scan_period').value
        self.angle_min = self.get_parameter('angle_min').value
        self.angle_max = self.get_parameter('angle_max').value
        self.range_min = self.get_parameter('range_min').value
        self.range_max = self.get_parameter('range_max').value
        self.angle_increment = self.get_parameter('angle_increment').value
        
        # Create publisher
        self.scan_publisher = self.create_publisher(
            LaserScan,
            'scan',
            10
        )
        
        # Initialize LiDAR
        try:
            self.lidar = RPLidar(self.port)
            self.get_logger().info(f'Connected to LiDAR on port {self.port}')
            
            # Reset LiDAR
            self.lidar.clean_input()
            self.lidar.stop()
            self.lidar.stop_motor()
            self.lidar.start_motor()
            
        except Exception as e:
            self.get_logger().error(f'Failed to initialize LiDAR: {str(e)}')
            return
        
        # Create timer for scanning
        self.create_timer(self.scan_period, self.scan_callback)
        
        # Initialize scan data storage
        self.angles = []
        self.distances = []
        self.qualities = []
        
        self.get_logger().info('LiDAR node initialized')

    def process_scan(self, scan_data):
        """Process raw scan data into LaserScan message"""
        # Initialize arrays for valid measurements
        angles = []
        distances = []
        
        # Process each measurement
        for measurement in scan_data:
            angle = measurement[1]  # Angle in degrees
            distance = measurement[2] / 1000.0  # Convert mm to meters
            
            # Filter valid measurements
            if (distance >= self.range_min and 
                distance <= self.range_max):
                angles.append(np.deg2rad(angle))  # Convert to radians
                distances.append(distance)
        
        # Sort measurements by angle
        sorted_indices = np.argsort(angles)
        angles = np.array(angles)[sorted_indices]
        distances = np.array(distances)[sorted_indices]
        
        return angles, distances

    def create_laser_scan_msg(self, angles, distances):
        """Create LaserScan message from processed data"""
        scan_msg = LaserScan()
        
        # Set header
        scan_msg.header.stamp = self.get_clock().now().to_msg()
        scan_msg.header.frame_id = 'laser_frame'
        
        # Set scan parameters
        scan_msg.angle_min = self.angle_min
        scan_msg.angle_max = self.angle_max
        scan_msg.angle_increment = self.angle_increment
        scan_msg.time_increment = self.scan_period / len(distances)
        scan_msg.scan_time = self.scan_period
        scan_msg.range_min = self.range_min
        scan_msg.range_max = self.range_max
        
        # Initialize ranges array
        num_readings = int((self.angle_max - self.angle_min) / self.angle_increment)
        ranges = [float('inf')] * num_readings
        
        # Fill in the actual readings
        for angle, distance in zip(angles, distances):
            index = int((angle - self.angle_min) / self.angle_increment)
            if 0 <= index < num_readings:
                ranges[index] = distance
        
        scan_msg.ranges = ranges
        return scan_msg

    def scan_callback(self):
        """Timer callback to publish scan data"""
        try:
            # Get scan data
            scan_data = next(self.lidar.iter_scans())
            
            # Process scan data
            angles, distances = self.process_scan(scan_data)
            
            # Create and publish LaserScan message
            if len(angles) > 0:
                scan_msg = self.create_laser_scan_msg(angles, distances)
                self.scan_publisher.publish(scan_msg)
                
        except Exception as e:
            self.get_logger().error(f'Error during scan: {str(e)}')

    def cleanup(self):
        """Cleanup when node is shutting down"""
        if hasattr(self, 'lidar'):
            self.lidar.stop()
            self.lidar.stop_motor()
            self.lidar.disconnect()
            self.get_logger().info('LiDAR disconnected')

def main(args=None):
    rclpy.init(args=args)
    lidar_node = LidarNode()
    
    try:
        rclpy.spin(lidar_node)
    except KeyboardInterrupt:
        pass
    finally:
        lidar_node.cleanup()
        lidar_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
