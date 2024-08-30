import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
    Node(package='rover_controller', 
         executable='robot_controller',
         output='screen'),
    Node(package='rover_controller', 
         executable='robot_estimator',
         output='screen'),
    ])