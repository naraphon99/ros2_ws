from setuptools import setup
from setuptools import find_packages

package_name = 'my_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(where='src'),    # <- ใช้ find_packages จาก src
    package_dir={'': 'src'},                # <- map src เป็น root ของ package
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/display.launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/my_robot.urdf.xacro']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='naraphon9',
    maintainer_email='your_email@example.com',
    description='My robot description package',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [],
    },
)

