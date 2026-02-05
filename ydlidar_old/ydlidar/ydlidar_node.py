#!/usr/bin/env python3

# ydlidar_node.py
import rclpy
from rclpy.node import Node

class YDLidarNode(Node):
    def __init__(self):
        super().__init__('ydlidar_node')
        self.get_logger().info("YDLidar node started")

def main():
    rclpy.init()
    node = YDLidarNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

