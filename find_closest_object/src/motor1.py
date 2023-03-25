#!/usr/bin/python3

import rospy
from hw1.msg import motor_values

def callback(data):
    rospy.loginfo(data)

def listener():
    rospy.init_node('motor1', anonymous=True)
    rospy.Subscriber("motor1_values", motor_values, callback)
    rospy.spin()


listener()