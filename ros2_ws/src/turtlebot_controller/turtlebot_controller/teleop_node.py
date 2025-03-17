# Turtle bot teleop file

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, select, termios, tty

#key  dictionary
KEY_MAPPINGS = {
    'w': (0.2, 0),  #Moves forward
    's': (-0.2, 0), #Moves backward
    'a': (0, 0.5),  #Turns left
    'd': (0, -0.5), #Turns right
    'x': (0, 0)     #this makes it stop
}

# Basically W makes the turtlebot go forward,S makes the turtlebot go backwards,A makes it turn left,D makes it turn right,X makes the bot sopt moving


#  This is the turtlebot class i built up
class TurtleBotTeleop(Node):
    # The initiation of the class
    def __init__(self):
        super().__init__('turtlebot_teleop')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info("TurtleBot Teleop Node Started. Use W/A/S/D to move, X to stop.")

    #this method reads a single key from the terminal
    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, termios.tcgetattr(sys.stdin))
        return key

    # This method makes it loop and read from the keyboard input and publish velocity commands
    def run(self):
        #Main loop to read keyboard input and publish velocity commands.
        while rclpy.ok():
            key = self.get_key()
            if key in KEY_MAPPINGS:
                linear, angular = KEY_MAPPINGS[key]
                twist = Twist()
                twist.linear.x = linear
                twist.angular.z = angular
                self.publisher.publish(twist)
                self.get_logger().info(f"Moving: linear={linear}, angular={angular}")

            elif key == '\x03':  # Ctrl+C
                self.get_logger().info("Shutting down teleop node...")
                break

def main():
    rclpy.init()
    node = TurtleBotTeleop()
    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
