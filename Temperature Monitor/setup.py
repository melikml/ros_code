#setup code
from setuptools import setup
import os
from glob import glob

package_name = 'smart_temperature_monitor'

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
    maintainer='Meliksah Yorulmazlar',
    maintainer_email='yorulk@rpi.edu',
    description='A ROS2 project to simulate temperature monitoring and automated climate control.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_sensor = smart_temperature_monitor.temperature_sensor:main',
            'temperature_filter = smart_temperature_monitor.temperature_filter:main',
            'temperature_evaluator = smart_temperature_monitor.temperature_evaluator:main',
            'climate_controller = smart_temperature_monitor.climate_controller:main',
            'temperature_logger = smart_temperature_monitor.temperature_logger:main',
        ],
    },
)
