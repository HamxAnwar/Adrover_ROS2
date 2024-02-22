import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidarNode_composition',
            output='screen',
            parameters=[{
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'serial_port': '/dev/ttyUSB0',
                'scan_mode': 'Standard',
            }]
        )
    ])