import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty

class TurtleCleaner(Node):
    def __init__(self):
        super().__init__('turtle_cleaner')
        self.client = self.create_client(Empty, 'clear')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for clear service...')
        self.future = self.client.call_async(Empty.Request())

def main(args=None):
    rclpy.init(args=args)
    node = TurtleCleaner()
    rclpy.spin_until_future_complete(node, node.future)
    node.get_logger().info('Screen cleared.')
    node.destroy_node()
    rclpy.shutdown()
