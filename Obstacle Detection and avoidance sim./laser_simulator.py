# This code publishes fake laser scan data
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import random

class LaserSimulator(Node):
    def __init__(self):
        super().__init__('laser_simulator')
        self.pub = self.create_publisher(Float32MultiArray, 'laser_scan', 10)
        self.timer = self.create_timer(0.5, self.publish_scan)

    def publish_scan(self):
        scan = Float32MultiArray()
        scan.data = [random.uniform(0.1, 5.0) for _ in range(8)]
        self.pub.publish(scan)
        self.get_logger().info(f'Published scan: {scan.data}')

def main(args=None):
    rclpy.init(args=args)
    node = LaserSimulator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
