# This code reacts to obstacle status (move/turn)

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MovementController(Node):
    def __init__(self):
        super().__init__('movement_controller')
        self.sub = self.create_subscription(String, 'obstacle_status', self.decision_callback, 10)
        self.pub = self.create_publisher(String, 'robot_action', 10)

    def decision_callback(self, msg):
        if msg.data == 'obstacle':
            action = 'turn_left'
        else:
            action = 'move_forward'
        self.pub.publish(String(data=action))
        self.get_logger().info(f'Action taken: {action}')

def main(args=None):
    rclpy.init(args=args)
    node = MovementController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
