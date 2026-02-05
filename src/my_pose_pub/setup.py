from setuptools import setup

package_name = 'my_pose_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='naraphon9',
    maintainer_email='naraphon@example.com',
    description='Publish Pose2D for EKF',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pose2d_to_ekf = my_pose_pub.pose2d_to_ekf:main',
        ],
    },
)

