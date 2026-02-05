#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose2D
from geometry_msgs.msg import PoseWithCovarianceStamped
import math


class Pose2DToEKF(Node):
    def __init__(self):
        super().__init__('pose2d_to_ekf')

        # รับ Pose2D จาก topic ที่คุณสร้างเอง
        self.sub = self.create_subscription(
            Pose2D,
            '/my_slam_pose2d',
            self.cb,
            10)

        # ส่งออกเป็น PoseWithCovarianceStamped ให้ EKF ใช้
        self.pub = self.create_publisher(
            PoseWithCovarianceStamped,
            '/slam_pose',
            10)

    def cb(self, msg: Pose2D):
        out = PoseWithCovarianceStamped()
        out.header.stamp = self.get_clock().now().to_msg()
        out.header.frame_id = 'map'   # world frame ของ EKF

        # position
        out.pose.pose.position.x = msg.x
        out.pose.pose.position.y = msg.y
        out.pose.pose.position.z = 0.0

        # theta → quaternion
        qz = math.sin(msg.theta / 2.0)
        qw = math.cos(msg.theta / 2.0)
        out.pose.pose.orientation.z = qz
        out.pose.pose.orientation.w = qw

        # covariance (ต้องมี ไม่งั้น EKF ไม่รับ)
        cov = [0.0] * 36
        cov[0] = 0.02
        cov[7] = 0.02
        cov[35] = 0.05
        out.pose.covariance = cov

        self.pub.publish(out)
def main(args=None):
    rclpy.init(args=args)
    node = Pose2DToEKF()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
