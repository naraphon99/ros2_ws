from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction

def generate_launch_description():
    return LaunchDescription([

       

        # base_link -> laser_frame
           Node(
            package='my_slam_launch',
            executable='laser_tf_pub',
            name='laser_tf_pub',
            output='screen'
        ),
        Node(
            package='my_slam_launch',
            executable='base_footprint',
            name='base_footprint',
            output='screen'
        ),

        # YDLIDAR
        Node(
            package='ydlidar',
            executable='ydlidar_node',
            output='screen',
            parameters=[
                '/home/naraphon9/ros2_ws/src/ydlidar_ros2/params/ydlidar.yaml',
                {'use_sim_time': False},
                {'scan_qos_profile': 'sensor_data_qos'}
            ]
        ),

        # EKF
        TimerAction(
            period=1.0,
            actions=[
                Node(
                    package='robot_localization',
                    executable='ekf_node',
                    output='screen',
                    parameters=[{
                        'use_sim_time': False,
                        'frequency': 50.0,
                        'two_d_mode': True,

                        'odom_frame': 'odom',
                        'base_link_frame': 'base_footprint',
                        'world_frame': 'odom',

                        'odom0': '/odom',
                        'odom0_config': [
                            True, True, False,
                            False, False, True,
                            True, True, False,
                            False, False, True
                        ],
                        'publish_tf': True
                    }]
                )
            ]
        ),

      
    ])

