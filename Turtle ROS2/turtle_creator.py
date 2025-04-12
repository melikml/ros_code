import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class TurtleSpawner(Node):
    def __init__(self):
        super().__init__('turtle_spawner')
        self.client = self.create_client(Spawn, 'spawn')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for spawn service...')
        req = Spawn.Request()
        req.x = 5.0
        req.y = 5.0
        req.theta = 0.0
        req.name = 'turtle2'
        self.future = self.client.call_async(req)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawner()
    rclpy.spin_until_future_complete(node, node.future)
    node.get_logger().info(f'Spawned turtle: {node.future.result().name}')
    node.destroy_node()
    rclpy.shutdown()
