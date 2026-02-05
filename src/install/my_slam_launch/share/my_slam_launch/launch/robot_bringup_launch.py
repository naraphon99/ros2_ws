from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    ekf_config_path = '/home/naraphon9/ros2_ws/src/my_slam_launch/config/ekf_odom.yaml'

    return LaunchDescription([

        # EKF node (robot_localization)
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[ekf_config_path],
            remappings=[
                ('/odometry/filtered', '/odom')  # ให้ topic odom ออกมาตรงมาตรฐาน
            ]
        ),

        # Static TF: base_footprint → base_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='basefootprint_to_baselink',
            arguments=['0', '0', '0.05', '0', '0', '0', 'base_footprint', 'base_link']
        ),

        # Static TF: base_link → laser_frame
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='baselink_to_laser',
            arguments=['0.08', '0.0', '0.1', '0', '0', '0', 'base_link', 'laser_frame']
        ),

        # Wheel odometry node (จาก ESP32 / micro-ROS)
        Node(
            package='my_slam_launch',
            executable='esp32_odom',
            name='wheel_odom',
            output='screen'
        )

    ])

