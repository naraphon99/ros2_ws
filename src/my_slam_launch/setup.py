from setuptools import setup
import os
from glob import glob

package_name = 'my_slam_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/scripts', glob('scripts/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='naraphon9',
    maintainer_email='example@example.com',
    description='My SLAM launch package (launch files only)',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'laser_tf_pub = my_slam_launch.laser_tf_pub:main',
            'base_footprint = my_slam_launch.base_footprint:main',
            #'fake_odom_tf = my_slam_launch.fake_odom_tf:main',
            #'odom_to_tf = my_slam_launch.odom_to_tf:main',
        ],
    },
)

 
