#!/usr/bin/python3

import rospy
from hw1.msg import proximity 
import random

def rand():
    return random.randint(10, 200)

def talker():
    pub = rospy.Publisher("distance",proximity,queue_size=10)
    rospy.init_node("sensor",anonymous=True)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown(): 
        msg = proximity()
        msg.front = rand()
        msg.right = rand()
        msg.back = rand()
        msg.left = rand()
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

talker()