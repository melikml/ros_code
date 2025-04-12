# launch file to run all the files
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='smart_temperature_monitor',
            executable='temperature_sensor',
            name='temperature_sensor'
        ),
        Node(
            package='smart_temperature_monitor',
            executable='temperature_filter',
            name='temperature_filter'
        ),
        Node(
            package='smart_temperature_monitor',
            executable='temperature_evaluator',
            name='temperature_evaluator',
            parameters=[{'hot_threshold': 30.0, 'cold_threshold': 18.0}]
        ),
        Node(
            package='smart_temperature_monitor',
            executable='climate_controller',
            name='climate_controller'
        ),
        Node(
            package='smart_temperature_monitor',
            executable='temperature_logger',
            name='temperature_logger'
        ),
    ])
