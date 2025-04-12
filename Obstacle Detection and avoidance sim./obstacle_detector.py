# this code subscribes to scan data and detects obstacles
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, String

class ObstacleDetector(Node):
    def __init__(self):
        super().__init__('obstacle_detector')
        self.create_subscription(Float32MultiArray, 'laser_scan', self.scan_callback, 10)
        self.alert_pub = self.create_publisher(String, 'obstacle_status', 10)
        self.threshold = 1.0

    def scan_callback(self, msg):
        if any(d < self.threshold for d in msg.data):
            status = 'obstacle'
        else:
            status = 'clear'
        self.alert_pub.publish(String(data=status))
        self.get_logger().info(f'Obstacle status: {status}')

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
