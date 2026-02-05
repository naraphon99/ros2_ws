from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction

def generate_launch_description():
    return LaunchDescription([


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
   
    
        Node(
            package='ydlidar',
            executable='ydlidar_node',
            name='ydlidar_node',
            output='screen',
            parameters=[
                '/home/naraphon9/ros2_ws/src/ydlidar_ros2/params/ydlidar.yaml',
                {'use_sim_time': False},
                {'scan_qos_profile': 'sensor_data_qos'}
            ]
        ),

    
        TimerAction(
            period=1.0,
            actions=[
                Node(
                    package='robot_localization',
                    executable='ekf_node',
                    name='ekf_filter_node',
                    output='screen',
                    parameters=[{
                        'use_sim_time': False,
                        'frequency': 50.0,
                        'sensor_timeout': 0.1,
                        'two_d_mode': True,

                        'odom_frame': 'odom',
                        'base_link_frame': 'base_footprint',
                        'world_frame': 'odom',

                        'odom0': '/odom',
                        'odom0_config': [
                            True,  True,  False,   # x, y, z
                            False, False, True,    # roll, pitch, yaw
                            True,  True,  False,   # vx, vy, vz
                            False, False, True     # yaw_rate 
                        ],

                        'odom0_queue_size': 10,
                        'publish_tf': True,
                        'publish_acceleration': False,
                        'reset_on_time_jump': True
                    }]
                )
            ]
        ),

     
        TimerAction(
            period=5.0,
            actions=[
                Node(
                    package='slam_toolbox',
                    executable='async_slam_toolbox_node',
                    name='slam_toolbox',
                    output='screen',
                    parameters=[{
                        'use_sim_time': False,

                        'base_frame': 'base_footprint',
                        'odom_frame': 'odom',
                        'map_frame': 'map',

                      
                        'use_pose_topic': False,
                        'publish_pose': False,

                        'scan_topic': '/scan',
                        'max_laser_range': 4.0,
                        'min_laser_range': 0.15,

                       
                        'minimum_travel_distance': 0.25,
                        'minimum_travel_heading': 0.25,

                        'scan_buffer_size': 50,
                        'scan_duration': 0.1,

                        'correlation_search_space_dimension': 0.15,
                        'correlation_search_space_resolution': 0.02,

                        'use_scan_matching': True,
                        'do_loop_closing': False,

                        'transform_timeout': 0.5,
                        'tf_buffer_duration': 120.0
                    }],
                    arguments=['--ros-args', '--log-level', 'info']
                )
            ]
        ),
    ])


