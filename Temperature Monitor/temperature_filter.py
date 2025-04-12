#This module applies smoothing (moving average) to the raw data

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from collections import deque

class TemperatureFilter(Node):
    def __init__(self):
        super().__init__('temperature_filter')
        self.subscription = self.create_subscription(Float32, 'raw_temperature', self.callback, 10)
        self.publisher = self.create_publisher(Float32, 'filtered_temperature', 10)
        self.window = deque(maxlen=5)

    def callback(self, msg):
        self.window.append(msg.data)
        if len(self.window) == 0:
            return
        avg = sum(self.window) / len(self.window)
        self.publisher.publish(Float32(data=avg))
        self.get_logger().info(f'Filtered Temp: {avg:.2f}°C')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureFilter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
