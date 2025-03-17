import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, select, termios, tty

#key  dictionary
KEY_MAPPINGS = {
    'w': (0.2, 0),  #Moves forward
    's': (-0.2, 0), #Moves backward
    'a': (0, 0.5),  #Turns left
    'd': (0, -0.5), #Turns right
    'x': (0, 0)     #this makes it stop
}
