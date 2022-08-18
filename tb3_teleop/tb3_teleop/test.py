	

#!/usr/bin/env python3

###################  import  ###########################
from tokenize import String
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
############# create a node class  #####################
class Test(Node):
    def __init__(self): # constructor
        super().__init__("test_id") # parent class constructor
        self.pub = self.create_publisher(String, "/apriltag/detections", 1)
        



    def callback(self,msg):
        
        test_id = "test"
        self.pub.publish(test_id)




###################  main method  ######################
def main():
    rclpy.init()
    node = Test()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()


