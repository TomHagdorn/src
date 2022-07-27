	

#!/usr/bin/env python3

from pickle import TRUE
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Teleop(Node):
    def __init__(self): # constructor
        super().__init__("auto") # parent class constructor
        self.pub = self.create_publisher(Twist, "/cmd_vel", 1)
        self.create_subscription(LaserScan, "/scan", self.callback, 10)


    def callback(self,msg):

        cmd = Twist() 
        speed_scale = 1.0
        turn_scale = 1.0
        mindata = min(msg.ranges)

       # if (mindata  < 0.10):
        #   self.estop()
        #
        #if (True):
         #   cmd.linear.x = speed_scale
          #  mindata = min(msg.ranges)
           # print(mindata)


        if (mindata >= 0.10 and mindata <= 0.50):
            cmd.angular.z = turn_scale *0.3
            cmd.linear.x = speed_scale *-0.2


        else:
            cmd.linear.x = turn_scale * 0.3

        
        self.pub.publish(cmd)



    def estop(self):
        cmd = Twist()
        cmd.linear.x = 0.0
        cmd.linear.y = 0.0
        cmd.linear.z = 0.0
        cmd.angular.x = 0.0
        cmd.angular.y = 0.0
        cmd.angular.z = 0.0
        self.pub.publish(cmd)

def main():
    rclpy.init()
    node = Teleop()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

