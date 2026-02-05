from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ydlidar',            # แพ็กเกจ LiDAR
            executable='ydlidar_node',    # Node executable ของ LiDAR
            name='lidar_node',
            output='screen',
            parameters=[{
                'frame_id': 'laser_frame',      # ชื่อ frame ของ LiDAR
                'serial_port': '/dev/ttyUSB0',  # พอร์ตที่เชื่อม LiDAR
                'serial_baudrate': 128000,      # Baudrate ของ LiDAR
                'inverted': False,              # พลิกสัญญาณหรือไม่
                'angle_compensate': True,       # เปิดใช้งาน angle compensation
                'scan_mode': 'Standard',        # โหมดสแกน
                'range_max': 10.0,              # ระยะสูงสุด (เมตร)
                'range_min': 0.15               # ระยะต่ำสุด (เมตร)
            }]
        )
    ])

