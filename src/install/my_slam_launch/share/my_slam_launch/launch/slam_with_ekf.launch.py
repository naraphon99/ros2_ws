# my_robot_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        # -------------------- EKF Node --------------------
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[{
                'frequency': 20.0,
                'two_d_mode': True,
                'publish_tf': True,
                'map_frame': 'map',
                'odom_frame': 'odom',
                'base_link_frame': 'base_link',

                # Wheel odometry topic
                'odom0': '/wheel/odom',
                'odom0_config': [True, True, False,
                                 False, False, True,
                                 False, False, False,
                                 False, False, False,
                                 False, False, False],
                'odom0_differential': False,
                'odom0_relative': False
            }]
        ),

        # -------------------- Static TF: base_footprint -> base_link --------------------
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_footprint_to_base_link',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', '1', 'base_footprint', 'base_link']
        ),

        # -------------------- Static TF: base_link -> laser_frame --------------------
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_link_to_laser',
            output='screen',
            arguments=['0.0', '0.0', '0.1', '0', '0', '0', '1', 'base_link', 'laser_frame']
            # ปรับ 0.1 เป็นความสูงเลเซอร์จริง
        ),

        # -------------------- Micro-ROS Odometry Publisher --------------------
        Node(
            package='my_micro_ros_pkg',
            executable='wheel_odom_node',
            name='wheel_odom',
            output='screen'
        ),

    ])

