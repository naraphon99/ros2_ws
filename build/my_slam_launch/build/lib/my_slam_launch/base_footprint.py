#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster

class BaseFootprintTF(Node):
    def __init__(self):
        super().__init__('base_footprint_tf')
        self.br = TransformBroadcaster(self)
        self.timer = self.create_timer(0.05, self.broadcast)  # 20 Hz

    def broadcast(self):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'base_footprint'
        t.child_frame_id = 'base_link'

        # ปกติ base_link สูงจากพื้น
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0765

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self.br.sendTransform(t)

def main():
    rclpy.init()
    node = BaseFootprintTF()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main() 
