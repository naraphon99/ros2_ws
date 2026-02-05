from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nav2_controller',
            executable='controller_server',
            parameters=['/home/naraphon9/ros2_ws/src/my_slam_launch/nav2_params.yaml'],
            output='screen'
        ),
        Node(
            package='nav2_planner',
            executable='planner_server',
            parameters=['/home/naraphon9/ros2_ws/src/my_slam_launch/nav2_params.yaml'],
            output='screen'
        ),
        Node(
            package='nav2_bt_navigator',
            executable='bt_navigator',
            parameters=['/home/naraphon9/ros2_ws/src/my_slam_launch/nav2_params.yaml'],
            output='screen'
        ),
        Node(
            package='nav2_recoveries',
            executable='recoveries_server',
            parameters=['/home/naraphon9/ros2_ws/src/my_slam_launch/nav2_params.yaml'],
            output='screen'
        ),
        Node(
    package='nav2_costmap_2d',
    executable='nav2_costmap_2d',
    name='global_costmap',
    output='screen',
    parameters=['/home/naraphon9/ros2_ws/src/my_slam_launch/nav2_params.yaml']
),

Node(
    package='nav2_costmap_2d',
    executable='nav2_costmap_2d',
    name='local_costmap',
    output='screen',
    parameters=['/home/naraphon9/ros2_ws/src/my_slam_launch/nav2_params.yaml']
),


        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager',
            parameters=[{
                'autostart': True,
                'use_sim_time': False,
                'node_names': [
    'controller_server',
    'nav2_planner',
    'recoveries_server',
    'bt_navigator',
    'global_costmap',
    'local_costmap'
]

            }],
            output='screen'
        ),
    ])

