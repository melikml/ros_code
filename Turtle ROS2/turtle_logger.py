import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class TurtleLogger(Node):
    def __init__(self):
        super().__init__('turtle_logger')
        self.create_subscription(Pose, 'turtle1/pose', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'Pose -> x: {msg.x:.2f}, y: {msg.y:.2f}, θ: {msg.theta:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = TurtleLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
