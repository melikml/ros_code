import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ClimateController(Node):
    def __init__(self):
        super().__init__('climate_controller')
        self.subscription = self.create_subscription(String, 'temp_alert', self.act, 10)
        self.action_pub = self.create_publisher(String, 'climate_action', 10)

    def act(self, msg):
        action = "idle"
        if msg.data == "too_hot":
            action = "turn_on_ac"
        elif msg.data == "too_cold":
            action = "turn_on_heater"
        self.action_pub.publish(String(data=action))
        self.get_logger().info(f'Action: {action}')

def main(args=None):
    rclpy.init(args=args)
    node = ClimateController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
