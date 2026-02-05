from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        
        # static transform สำหรับ LiDAR (แกน x,y,z ตามจริงของ sensor)
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_lidar',
            arguments=['0.0', '0.0', '0.35', '0.0', '0.0', '0.0', 'base_link', 'laser_frame']
        ),
    ])
