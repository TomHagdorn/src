#GUI interface zur benutzerfereundlicheren Bedienung 
#!/usr/bin/env python3

###################  import  ###########################
from curses import window
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from tkinter import*
from apriltag_msgs.msg import AprilTagDetectionArray
############# create a node class  #####################


class Apriltag_ID(Node):
    def __init__(self): 
        super().__init__("apriltag_id") 
        self.create_timer(0.1, self.callback)
        self.create_subscription(AprilTagDetectionArray, "/apriltag/detections", self.callback, 10) #TODO das ist kein string 

        self.window =    Tk(className=" Apriltag_ID")
        self.window.geometry('500x500+0+0')
        self.window.attributes('-topmost', True)


        global Apriltags
        global detect_Aptiltags     
        Apriltags =  ["Offene Apriltags", "1","2","3","4","5","6","7","8","9","10"]
        detect_Aptiltags=["Gefundene Apriltags","","","","","","","","","",""]


        height = 11
        width = 2
        
        for i in range(height): #Rows
            for j in range(width): #Columns
                Label(self.window, text= Apriltags[i] ,borderwidth=1 ).grid(row=i,column=1)
                Label(self.window, text= detect_Aptiltags[i] ,borderwidth=1 ).grid(row=i,column=2)

        

    def callback(self,msg):
        self.window.mainloop()
        try:
            tag_id = str(msg.detections[0].id)
        except:
            None

        for x in Apriltags:
            if tag_id in Apriltags:
                Apriltags.pop(x)
                detect_Aptiltags.pop(x)
                detect_Aptiltags.insert(x,tag_id)
        print("Detected:"+ detect_Aptiltags)

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