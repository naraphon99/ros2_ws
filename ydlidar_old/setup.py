from setuptools import setup

package_name = 'ydlidar'

setup(
    name=package_name,
    version='0.0.1',
    packages=['ydlidar'],  # โฟลเดอร์ย่อยที่มี __init__.py
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='YDLidar ROS2 package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ydlidar_node = ydlidar.ydlidar_node:main',
        ],
    },
    data_files=[
        ('share/ydlidar/launch', ['launch/ydlidar_slam_rviz_launch.py']),
        ('share/ament_index/resource_index/packages',
         ['package.xml']),
    ],
)

