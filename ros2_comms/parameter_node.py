# This is the parameter node

import rclpy
from rclpy.node import Node

class ParameterNode(Node):
    def __init__(self):
        super().__init__('parameter_node')
        self.declare_parameter('update_rate', 1.0)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Parameter node started.')

    def timer_callback(self):
        update_rate = self.get_parameter('update_rate').value
        self.get_logger().info(f'Current update rate: {update_rate}')
        # You could dynamically change behavior based on update rate here

def main(args=None):
    rclpy.init(args=args)
    node = ParameterNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
