#Setup file

from setuptools import setup
import os
from glob import glob

package_name = 'obstacle_avoidance_sim'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    description='A basic obstacle avoidance simulation with laser scan and reactive control.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'laser_simulator = obstacle_avoidance_sim.laser_simulator:main',
            'obstacle_detector = obstacle_avoidance_sim.obstacle_detector:main',
            'movement_controller = obstacle_avoidance_sim.movement_controller:main',
            'status_logger = obstacle_avoidance_sim.status_logger:main',
            'parameter_server = obstacle_avoidance_sim.parameter_server:main',
        ],
    },
)
