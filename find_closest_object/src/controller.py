#!/usr/bin/python3

import rospy
from hw1.msg import proximity
from hw1.msg import motor_values

pub_1 = rospy.Publisher('motor1_values', motor_values, queue_size=1000) 
pub_2 = rospy.Publisher('motor2_values', motor_values, queue_size=1000) 
sensor_data = proximity()

def callback(data):
    global sensor_data
    sensor_data = data
    rospy.loginfo(sensor_data)
    motor_decision()
    rospy.loginfo("------------------------------------------------------------------------")

def find_min_value():
    global sensor_data
    min_value = sensor_data.back
    min_direction = "back"

    if(sensor_data.front < min_value):
        min_value=sensor_data.front
        min_direction="front"

    if(sensor_data.right < min_value):
        min_value=sensor_data.right
        min_direction="right"

    if(sensor_data.left < min_value):
        min_value=sensor_data.left
        min_direction="left"

    return min_direction


def motor_decision():
    global sensor_data , pub_1,pub_2

    m1 = motor_values()
    m2 = motor_values()
    min_direction = find_min_value()


    if min_direction == 'front' :
        m1.degree = 180
        m1.isClockwise = True

        m2.degree = 180
        m2.isClockwise = True
    elif  min_direction == 'right' :

        m1.degree = 90
        m1.isClockwise = False

        m2.degree = 90
        m2.isClockwise = False

    elif  min_direction == 'left' :

        m1.degree = 90
        m1.isClockwise = True

        m2.degree = 90
        m2.isClockwise = True

    else:

        m1.degree = 0
        m1.isClockwise = False

        m2.degree = 0
        m2.isClockwise = False

    rospy.loginfo(m1)
    rospy.loginfo(m2)
    pub_1.publish(m1)
    pub_2.publish(m2)

def controller():
    rospy.init_node('controller', anonymous=True)
    rospy.Subscriber('distance', proximity, callback)
    rospy.spin()

controller()