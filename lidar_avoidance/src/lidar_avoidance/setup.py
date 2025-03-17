#Setup file
from setuptools import setup

package_name = 'lidar_avoidance'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='LiDAR-based obstacle avoidance for robots',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lidar_avoid = lidar_avoidance.lidar_avoid:main',
        ],
    },
)
