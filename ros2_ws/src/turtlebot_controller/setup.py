# This code sets it up

from setuptools import setup

package_name = 'turtlebot_controller'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='TurtleBot3 Teleop Node',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'teleop = turtlebot_controller.teleop_node:main',
        ],
    },
)
