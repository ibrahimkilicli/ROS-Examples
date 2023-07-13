#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def control_robots():
    rospy.init_node('dual_turtle_control', anonymous=True)
    turtle_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) 
    #iki turlesim de aynı topice bağlı

    while not rospy.is_shutdown():
    
        vel_msg = Twist()

        vel_msg.linear.x = 1.0
        vel_msg.angular.z = 0.5

        turtle_publisher.publish(vel_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        control_robots()
    except rospy.ROSInterruptException:
        pass









