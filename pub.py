

import rclpy
from rclpy.node import Node


import rclpy.qos

#! Our interface definition, which is a class in Python
from ros2_examples_interfaces.msg import String



class Pub(Node):
    """Example ROS 2 node with a subscriber to a custom topic."""

    def __init__(self) -> None:

        # We need to call the base Node constructor
        super().__init__('publisher_node')

        # Create a custom, best-effort QoS profile
        qos_profile = rclpy.qos.QoSProfile(
            depth=1,
            history=rclpy.qos.HistoryPolicy.KEEP_LAST,
            reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT,
            durability=rclpy.qos.DurabilityPolicy.VOLATILE)

        # Create a publisher to the custom topic
        self._pub = self.create_publisher(
            String,
            '~/examples/test_topic',
            qos_profile)

        # Create a timer to publish a message every second
        self._timer = self.create_timer(
            0.5,
            self.timer_callback)

        self._cnt = 0

        self.get_logger().info('Node initialized')

    # Callback functions are methods here too, and are passed message objects
    def timer_callback(self) -> None:
        #! Create a message object, fill it, and publish it
        msg = String()
        msg.data = 'Hello %d' % self._cnt
        self._pub.publish(msg)
        self._cnt += 1

        self.get_logger().info('Published message: %s' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node = Pub()

    try:
        rclpy.spin(node)
    except:
      pass
    node.destroy_node()

    print('Publisher terminated')
if __name__ == '__main__':
    main()
