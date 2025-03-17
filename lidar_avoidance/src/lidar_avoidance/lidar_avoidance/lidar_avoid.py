import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


# Lidar Avoidance class
class LidarAvoidance(Node):
    def __init__(self):
        super().__init__('lidar_avoidance')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',  # LiDAR topic
            self.lidar_callback,
            10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info("LiDAR Avoidance Node Started!")

    #Process LiDAR data to detect obstacles and avoid them
    def lidar_callback(self, msg):
        min_distance = min(msg.ranges)  # Closest obstacle distance
        threshold = 0.5  # Minimum safe distance (meters)

        twist_msg = Twist()

        if min_distance < threshold:
            # If the code detects an obstacle, it turns left
            twist_msg.angular.z = 0.5
            self.get_logger().info("Obstacle detected! Turning left")
        else:
            #if there was no obstacle it continues moving forward
            twist_msg.linear.x = 0.2
            self.get_logger().info("Path is clear. Moving forward")
        self.publisher.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)
    node = LidarAvoidance()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
