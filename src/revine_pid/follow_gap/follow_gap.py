#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDrive
import numpy as np
from math import pi, atan2

class FollowGapNode(Node):
    def _init_(self):
        super()._init_('follow_gap_controller')
        
        # Algorithm parameters
        self.declare_parameters(
            namespace='',
            parameters=[
                ('bubble_radius', 0.5),    # Radius for bubble around closest point
                ('min_gap_width', 0.5),    # Minimum width to consider a gap
                ('safety_factor', 1.0),    # Alpha safety factor
                ('max_speed', 2.0),
                ('min_speed', 0.5),
                ('threshold_distance', 2.0)  # Distance threshold for speed control
            ]
        )
        
        # Get parameters
        self.bubble_radius = self.get_parameter('bubble_radius').value
        self.min_gap_width = self.get_parameter('min_gap_width').value
        self.safety_factor = self.get_parameter('safety_factor').value
        self.max_speed = self.get_parameter('max_speed').value
        self.min_speed = self.get_parameter('min_speed').value
        self.threshold_distance = self.get_parameter('threshold_distance').value
        
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
        
        self.get_logger().info('Follow Gap Controller initialized')

    def preprocess_lidar(self, ranges):
        """Preprocess LIDAR data"""
        # Remove inf values
        proc_ranges = np.array(ranges)
        proc_ranges[np.isinf(proc_ranges)] = 10.0  # Set inf to max range
        return proc_ranges

    def find_closest_point(self, ranges, angles):
        """Find the closest point to the robot"""
        min_idx = np.argmin(ranges)
        return min_idx, ranges[min_idx]

    def create_safety_bubble(self, ranges, center_idx):
        """Create safety bubble around closest point"""
        bubble_radius_idx = int(self.bubble_radius / (2 * pi / len(ranges)))
        
        start_idx = max(0, center_idx - bubble_radius_idx)
        end_idx = min(len(ranges), center_idx + bubble_radius_idx)
        
        ranges[start_idx:end_idx] = 0
        return ranges

    def find_max_gap(self, ranges):
        """Find the largest gap in the ranges array"""
        # Find gaps
        gaps = []
        start_idx = 0
        
        for idx in range(len(ranges)):
            if idx == 0:
                continue
            
            # Gap starts
            if ranges[idx] > self.min_gap_width and ranges[idx-1] <= self.min_gap_width:
                start_idx = idx
            
            # Gap ends
            if ranges[idx] <= self.min_gap_width and ranges[idx-1] > self.min_gap_width:
                gaps.append((start_idx, idx-1))
        
        # Find largest gap
        if not gaps:
            return None
            
        largest_gap = max(gaps, key=lambda x: x[1] - x[0])
        return largest_gap

    def find_best_gap_point(self, ranges, gap, goal_angle):
        """Find the best point in the gap considering goal direction"""
        if gap is None:
            return len(ranges) // 2  # Return middle point if no gap found
            
        start_idx, end_idx = gap
        gap_angles = np.linspace(-pi, pi, len(ranges))[start_idx:end_idx]
        
        # Find point in gap closest to goal direction
        goal_diff = np.abs(gap_angles - goal_angle)
        best_idx = start_idx + np.argmin(goal_diff)
        
        return best_idx

    def calculate_final_heading(self, best_point_idx, ranges, goal_angle):
        """Calculate final heading using Equation (1) from the paper"""
        d_min = min(ranges)  # Minimum distance to obstacles
        gap_angle = (best_point_idx / len(ranges)) * 2 * pi - pi
        
        # Implementation of Equation (1) from the paper
        final_angle = ((self.safety_factor * d_min * gap_angle) + goal_angle) / (self.safety_factor * d_min + 1)
        return final_angle

    def scan_callback(self, msg):
        try:
            # Preprocess LIDAR data
            proc_ranges = self.preprocess_lidar(msg.ranges)
            
            # Find closest point
            closest_idx, closest_dist
