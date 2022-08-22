#GUI interface zur benutzerfereundlicheren Bedienung 
#!/usr/bin/env python3

###################  import  ###########################
from curses import window
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from tkinter import*
from geometry_msgs.msg import TransformStamped
############# create a node class  #####################


class Apriltag_ID(Node):
    def __init__(self): 
        super().__init__("apriltag_id") 
        self.create_subscription(TransformStamped, "/apriltag_map_stamped", self.callback, 10) 




        global Apriltags
        global detect_Aptiltags     
        Apriltags =  [1,2,3,4,5,6,7,8,9,10]
        detect_Aptiltags=["","","","","","","","","",""]


    def callback(self,msg):
        
        try:
            tag_id_str = msg.child_frame_id
            tag_id = int(tag_id_str[6:])
            tag_tranform = msg.transform
        except:
            None

        for x in Apriltags:
            if tag_id in Apriltags:
                Apriltags.pop(x)
                detect_Aptiltags.pop(x)
                detect_Aptiltags.insert(x,tag_id_str)
                #Print message to terminal 
                printer(msg,tag_id)
                #Write ID and Transform to a textfile for later 
                with open('/home/tom/robotik3_ws/src/tb3_teleop/apriltag_positions.txt', 'w') as f:
                    f.write(tag_id_str +  str(tag_tranform))

                    
def printer(trans: TransformStamped,april_id):
    print("----------------------------------------")
    print("Tag_frame: " + str(april_id))
    print("Position: ")
    print("  X: " + str(trans.transform.translation.x))
    print("  Y: " + str(trans.transform.translation.y))
    print("  Z: " + str(trans.transform.translation.z))
    print("Orientation: ")
    print("  X: " + str(trans.transform.rotation.x))
    print("  Y: " + str(trans.transform.rotation.y))
    print("  Z: " + str(trans.transform.rotation.z))
    print("  W: " + str(trans.transform.rotation.w))            


def main():
    rclpy.init()
    node = Apriltag_ID()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()