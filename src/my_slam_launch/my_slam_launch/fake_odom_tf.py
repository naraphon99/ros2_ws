#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
import math

class FakeOdomPublisher(Node):
    def __init__(self):
        super().__init__('fake_odom_tf_publisher')
        self.br = TransformBroadcaster(self)
        self.theta = 0.0
        self.timer = self.create_timer(0.1, self.publish_tf)  # 10 Hz

    def publish_tf(self):
        # อัพเดทมุม
        self.theta = (self.theta + 0.05) % (2 * math.pi)

        # ให้หุ่นวิ่งเป็นวงกลมรัศมี 1 เมตร
        x = math.cos(self.theta) * 1.0
        y = math.sin(self.theta) * 1.0

        # สร้าง TF message
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'

        t.transform.translation.x = x
        t.transform.translation.y = y
        t.transform.translation.z = 0.0

        # quaternion จาก yaw (theta)
        qz = math.sin(self.theta / 2.0)
        qw = math.cos(self.theta / 2.0)

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = qz
        t.transform.rotation.w = qw

        # ส่ง TF
        self.br.sendTransform(t)

        # log เป็น debug mode (จะไม่ spam จนเกินไป)
        self.get_logger().debug(f"Publishing TF: x={x:.2f}, y={y:.2f}, theta={self.theta:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = FakeOdomPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

