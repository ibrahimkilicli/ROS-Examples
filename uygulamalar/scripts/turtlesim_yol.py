#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def yol_uzerinde_hareket(yol):
    rospy.init_node('turtle_yol', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  

    vel_msg = Twist()

    # Yol boyunca hareket et
    for point in yol:
        rospy.sleep(0.5)
        vel_msg.linear.x = point[0]
        vel_msg.angular.z = point[1]
        velocity_publisher.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    # Önceden belirlenmiş yol
    yol = [(1.0, 0.0), (0.0, 1.570796), (2.0, 0,0), (0.0, -1.047119), (1.0, 0.0),(0.0, 2.094395), (3.5, 0.0)]

    try:
        yol_uzerinde_hareket(yol)
    except rospy.ROSInterruptException:
        pass








