# ydlidar_slam_rviz_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        # ---- YDLidar Node ----
        Node(
            package='ydlidar',
            executable='ydlidar_node',
            name='ydlidar_node',
            output='screen',
            parameters=[{
                'port': '/dev/ttyUSB0',   # เปลี่ยนตาม LiDAR ของคุณ
                'frame_id': 'laser_frame',
                'inverted': False,
                'angle_compensate': True,
                'scan_mode': 'Standard',
                'baudrate': 128000
            }]
        ),

        # ---- SLAM Toolbox Node ----
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{
                'use_sim_time': False,
                'slam_params_file': '',
                'odom_frame': 'odom',
                'base_frame': 'base_link',
                'map_frame': 'map',
                'scan_topic': 'scan',
            }]
        ),

        # ---- Static transform from base_link to laser_frame ----
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_to_laser',
            arguments=['0','0','0','0','0','0','base_link','laser_frame']
        ),

        # ---- RViz2 Node ----
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '/home/naraphon9/ros2_ws/src/your_package/rviz/ydlidar_slam.rviz']
        )
    ])
