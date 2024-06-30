#! /usr/bin/env python3

import rospy
from std_msgs.msg import String, Float32
from sensor_msgs.msg import Imu, NavSatFix
from tf import transformations
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from math import radians, cos, sin, asin, sqrt, atan2, degrees
from time import sleep
from sbg_driver.msg import SbgGpsPos, SbgEkfEuler
import numpy as np

rospy.init_node("aruco_follow")
status = rospy.Publisher("/status", String, queue_size=10)

yaw = 0.0
lat = 0.0
lon = 0.0

lin_vel = 60
ang_vel = 10

forward = Twist()
left = Twist()
right = Twist()
backward = Twist()
stop = Twist()

forward.linear.x = lin_vel
left.angular.z = ang_vel
right.angular.z = -ang_vel
backward.linear.x = -lin_vel

class Callbacks:
    def status_stuff(self, status_string):
        print(status_string)
        status.publish(status_string)

    def aruco_tag_info_callback(self, msg):
        data = msg.data.split()
        aruco_state = int(data[0])

        if aruco_state:

            distance = float(data[1])
            x = int(data[2])
            y = int(data[3])
            id = data[4]

            if x > ((aruco.img_res[0]/2) + 50):
                rover.publish(right)
                callbacks.status_stuff("turning right")
                print("turning right")
                # aruco_reached_pub.publish(0.0)

            elif x < ((aruco.img_res[0]/2) - 50):
                rover.publish(left)
                callbacks.status_stuff("turning left")
                print("turning left")
                # aruco_reached_pub.publish(0.0)

            elif x < ((aruco.img_res[0]/2) + 50) and x > ((aruco.img_res[0]/2) - 50):
                if distance == None:
                    print(distance)
                    # aruco_reached_pub.publish(0.0)
                elif distance > 500.0:    
                    rover.publish(forward)
                    callbacks.status_stuff("going forward")
                    print("going forward")
                    # aruco_reached_pub.publish(0.0)
                else:
                    if distance == 0.0:
                        pass
                    else:
                        post_state = True
                        status_led.publish("g")
                        # sleep(2)
                        status_led.publish("g")
                        print("Reached")

                        # aruco_reached_pub.publish(1.0)

        # callbacks.status_stuff("Reached Target Coords")
        # rover.publish(stop)


class Aruco:
    img_res = (640, 480)
    

if __name__ == "__main__":
    callbacks = Callbacks()
    aruco = Aruco()

    rover = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    status_led = rospy.Publisher("/status_indicator", String, queue_size=10)
    # aruco_reached_pub = rospy.Publisher("/aruco_reached", Float32, queue_size=10)
    aruco_tag_info_sub = rospy.Subscriber("/aruco_tag_info", String, callbacks.aruco_tag_info_callback)

    rospy.spin()
