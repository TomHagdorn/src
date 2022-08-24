#!/usr/bin/env python3

import rclpy
import tf2_ros
from geometry_msgs.msg import TransformStamped
from apriltag_msgs.msg import AprilTagDetectionArray


def printer(trans: TransformStamped,april_id):
    print("----------------------------------------")
    print("Tag_id: " + str(april_id))
    print("Position: ")
    print("  X: " + str(trans.transform.translation.x))
    print("  Y: " + str(trans.transform.translation.y))
    print("  Z: " + str(trans.transform.translation.z))
    print("Orientation: ")
    print("  X: " + str(trans.transform.rotation.x))
    print("  Y: " + str(trans.transform.rotation.y))
    print("  Z: " + str(trans.transform.rotation.z))
    print("  W: " + str(trans.transform.rotation.w))

def timercallback():
    global tfBuffer
    global trans
    try:
        # do a lookup transform between 'base_link' and 'marker' frame
        trans = tfBuffer.lookup_transform(frame_id, "marker" + str(april_id), rclpy.duration.Duration())
        #trans = tfBuffer.lookup_transform(frame_id, "camera_lens_link", rclpy.duration.Duration())
        # returns TransformStamped() message
        #printer(trans,april_id)
        #tfBuffer.clear()
        april_transform_pub.publish(trans)
    except:
        # exception is raised on extrapolation, 
        # no connection between frames or when frames dont exist
        print("lookup failed")
    

def april_sub(msg):
    global april_id
    try: 
        april_id = msg.detections[0].id

    except: 
        april_id = "401 no tagt detected"
        # print(april_id)


def main():
    global tfBuffer
    global frame_id
    global april_transform_pub
    frame_id = 'camera_lens_link'
    rclpy.init() # init ros client library
    nh = rclpy.create_node('tf2_listener') # create a node with name 'tf2_listener'
    tfBuffer = tf2_ros.Buffer(cache_time=rclpy.duration.Duration(nanoseconds=100000000)) # create a TF2 buffer which saves the TFs for given cache_time
    tf2_ros.TransformListener(tfBuffer, nh) # create TF2 listener which connects buffer with node
    nh.create_timer(0.1, timercallback) # call timercallback every 100ms
    nh.create_subscription(AprilTagDetectionArray, '/apriltag/detections', april_sub, 10)
    april_transform_pub = nh.create_publisher(TransformStamped, '/apriltag_map_stamped',1 )
    try:
        rclpy.spin(nh) # spin node until exception
    except KeyboardInterrupt:
        nh.destroy_node() # destroy node
        rclpy.shutdown() # shutdown ros client library

if __name__ == '__main__':
    main()