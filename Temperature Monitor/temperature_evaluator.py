import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class TemperatureEvaluator(Node):
    def __init__(self):
        super().__init__('temperature_evaluator')
        self.subscription = self.create_subscription(Float32, 'filtered_temperature', self.eval_temp, 10)
        self.alert_pub = self.create_publisher(String, 'temp_alert', 10)
        self.declare_parameter('hot_threshold', 30.0)
        self.declare_parameter('cold_threshold', 18.0)

    def eval_temp(self, msg):
        temp = msg.data
        hot = self.get_parameter('hot_threshold').value
        cold = self.get_parameter('cold_threshold').value
        status = "normal"
        if temp >= hot:
            status = "too_hot"
        elif temp <= cold:
            status = "too_cold"
        self.alert_pub.publish(String(data=status))
        self.get_logger().info(f'Status: {status}')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureEvaluator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
