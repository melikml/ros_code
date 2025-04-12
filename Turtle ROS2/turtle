import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

class TurtleSquare(Node):
    def __init__(self):
        super().__init__('turtle_square')
        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.sub = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)
        self.pose = None
        self.state = 'MOVE'
        self.edge_count = 0
        self.start_time = time.time()
        self.get_logger().info('Drawing square...')

    def pose_callback(self, msg):
        self.pose = msg
        self.move_square()

    def move_square(self):
        if self.edge_count >= 4:
            self.pub.publish(Twist())  # stop
            return

        twist = Twist()
        now = time.time()
        if self.state == 'MOVE':
            if now - self.start_time < 2.0:
                twist.linear.x = 2.0
            else:
                self.state = 'TURN'
                self.start_time = now
        elif self.state == 'TURN':
            if now - self.start_time < 1.0:
                twist.angular.z = math.pi / 2
            else:
                self.state = 'MOVE'
                self.start_time = now
                self.edge_count += 1

        self.pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSquare()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
