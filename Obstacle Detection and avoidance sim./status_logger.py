# this logs current robot action -this code is helpful for debugging

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StatusLogger(Node):
    def __init__(self):
        super().__init__('status_logger')
        self.sub = self.create_subscription(String, 'robot_action', self.log_status, 10)

    def log_status(self, msg):
        self.get_logger().info(f'Robot is: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = StatusLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
