import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty

class ResetTurtle(Node):
    def __init__(self):
        super().__init__('reset_turtle')
        self.client = self.create_client(Empty, 'reset')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for reset service...')
        self.future = self.client.call_async(Empty.Request())

def main(args=None):
    rclpy.init(args=args)
    node = ResetTurtle()
    rclpy.spin_until_future_complete(node, node.future)
    node.get_logger().info('Turtle has been reset.')
    node.destroy_node()
    rclpy.shutdown()
