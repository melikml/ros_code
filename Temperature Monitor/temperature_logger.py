import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TemperatureLogger(Node):
    def __init__(self):
        super().__init__('temperature_logger')
        self.sub = self.create_subscription(String, 'climate_action', self.log, 10)

    def log(self, msg):
        self.get_logger().info(f'[LOG] Climate action: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
