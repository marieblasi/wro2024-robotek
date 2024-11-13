#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from custom_interfaces.msg import ColoredObject, ColoredObjectArray

class ColorDetectorNode(Node):
    def _init_(self):
        super()._init_('color_detector')
        
        # Initialize CV bridge
        self.bridge = CvBridge()
        
        # Create subscribers and publishers
        self.image_subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10)
        
        self.processed_image_publisher = self.create_publisher(
            Image, 
            '/processed_image', 
            10)
            
        self.objects_publisher = self.create_publisher(
            ColoredObjectArray,
            '/detected_objects',
            10)
        
        # Color ranges in HSV
        self.color_ranges = {
            'red': [(np.array([0, 100, 100]), np.array([10, 255, 255])),
                   (np.array([160, 100, 100]), np.array([180, 255, 255]))],
            'green': [(np.array([40, 100, 100]), np.array([80, 255, 255]))]
        }
        
        self.min_area = 500
        self.get_logger().info('Color detector node initialized')

    def detect_color(self, hsv_image, color_name):
        mask = None
        for lower, upper in self.color_ranges[color_name]:
            current_mask = cv2.inRange(hsv_image, lower, upper)
            if mask is None:
                mask = current_mask
            else:
                mask = cv2.bitwise_or(mask, current_mask)
        return mask

    def process_contours(self, contours, color_name):
        objects = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > self.min_area:
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    
                    obj = ColoredObject()
                    obj.x = float(cx)
                    obj.y = float(cy)
                    obj.color = color_name
                    obj.area = float(area)
                    objects.append(obj)
        return objects

    def image_callback(self, msg):
        try:
            # Convert ROS Image to OpenCV format
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            output_image = cv_image.copy()
            
            # Convert to HSV color space
            hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
            
            # Initialize message for detected objects
            detected_objects = ColoredObjectArray()
            detected_objects.objects = []
            
            # Process each color
            for color_name in ['red', 'green']:
                # Get color mask
                mask = self.detect_color(hsv_image, color_name)
                
                # Clean up mask
                kernel = np.ones((5,5), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                
                # Find contours
                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, 
                                             cv2.CHAIN_APPROX_SIMPLE)
                
                # Process contours and get objects
                objects = self.process_contours(contours, color_name)
                detected_objects.objects.extend(objects)
                
                # Draw detections on output image
                for obj in objects:
                    color = (0, 255, 0) if color_name == 'green' else (0, 0, 255)
                    cv2.circle(output_image, (int(obj.x), int(obj.y)), 5, color, -1)
                    cv2.putText(output_image, 
                              f"{color_name}: ({int(obj.x)}, {int(obj.y)})",
                              (int(obj.x) - 20, int(obj.y) - 20),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            
            # Publish processed image
            self.processed_image_publisher.publish(
                self.bridge.cv2_to_imgmsg(output_image, "bgr8"))
            
            # Publish detected objects
            self.objects_publisher.publish(detected_objects)
            
        except Exception as e:
            self.get_logger().error(f'Error processing image: {str(e)}')

def main(args=None):
    rclpy.init(args=args)
    color_detector = ColorDetectorNode()
    rclpy.spin(color_detector)
    color_detector.destroy_node()
    rclpy.shutdown()

if _name_ == '_main_':
    main()
