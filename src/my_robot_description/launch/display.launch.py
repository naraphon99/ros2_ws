from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # ดึง path ของ package
    package_path = get_package_share_directory('my_robot_description')
    
    # path ของไฟล์ URDF
    urdf_path = os.path.join(package_path, 'urdf', 'my_robot.urdf.xacro')
    
    # Node สำหรับ robot_state_publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': False}],
        arguments=[urdf_path]
    )

    # Node สำหรับ RViz โดยไม่ใช้ config file
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
        # ไม่มี arguments เพื่อใช้ default RViz config
    )

    return LaunchDescription([
        robot_state_publisher_node,
        rviz_node
    ])

