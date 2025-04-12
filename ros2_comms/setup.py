# This is the setup file
from setuptools import setup
import os
from glob import glob

package_name = 'ros2_comms_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include launch files if any
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Meliksah Yorulmazlar',
    maintainer_email='yorulk@rpi.edu',
    description='A ROS2 demo package with publisher, subscriber, service, client, and parameter nodes.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker_node = ros2_comms_demo.talker_node:main',
            'listener_node = ros2_comms_demo.listener_node:main',
            'add_two_ints_server = ros2_comms_demo.add_two_ints_server:main',
            'add_two_ints_client = ros2_comms_demo.add_two_ints_client:main',
            'parameter_node = ros2_comms_demo.parameter_node:main',
        ],
    },
)
