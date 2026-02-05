from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # YDLidar node
        Node(
            package='ydlidar',
            executable='ydlidar_node',
            name='ydlidar_node',
            output='screen',
            parameters=[{
                'port': '/dev/ttyUSB0',   # เปลี่ยนตามพอร์ตของคุณ
                'frame_id': 'laser_frame',
                'inverted': False,
                'angle_compensate': True,
                'scan_mode': 'Standard',
                'baudrate': 128000
            }]
        ),
        # SLAM Toolbox
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{
                'use_sim_time': False,
                'map_frame': 'map',
                'odom_frame': 'odom',
                'base_frame': 'base_link',
                'scan_topic': 'scan'
            }]
        ),
        # RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '/home/naraphon9/ros2_ws/src/ydlidar/rviz/ydlidar_slam.rviz']  # สร้าง rviz config เอง
        )
    ])
