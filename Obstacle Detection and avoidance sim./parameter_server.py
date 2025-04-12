#this module dynamically sets detection range

import rclpy
from rclpy.node import Node

class ParameterServer(Node):
    def __init__(self):
        super().__init__('parameter_server')
        self.declare_parameter('detection_threshold', 1.0)
        self.timer = self.create_timer(2.0, self.print_params)

    def print_params(self):
        val = self.get_parameter('detection_threshold').value
        self.get_logger().info(f'Detection threshold: {val}')

def main(args=None):
    rclpy.init(args=args)
    node = ParameterServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
