from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # เรียกใช้ slam_toolbox
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[
                {'use_sim_time': False},
                {'base_frame': 'base_link'},
                {'odom_frame': 'odom'},
                {'map_frame': 'map'},
                {'scan_topic': '/scan'}
            ]
        ),

        # TF: base_link -> laser_frame (static)
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_base_laser',
            arguments=['0.1', '0.0', '0.2', '0', '0', '0', 'base_link', 'laser_frame']
        ),

        # TF: base_link -> base_footprint (static)
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_base_basefootprint',
            arguments=['0', '0', '0.1', '0', '0', '0', 'base_footprint', 'base_link']
        ),
    ])

