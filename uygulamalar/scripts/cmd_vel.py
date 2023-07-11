#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node("cmd_vel_ornegi") 
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)  # rospy.Publisher ile bir yayıncı oluşturuluyor hız mesajı yayınlamak için

    hiz_mesaji = Twist()           # hız mesajı yayınlayacağın tipi ayarlıyorsun.
    hiz_mesaji.linear.x = 0.5

    rate = rospy.Rate(10)  # Yayın hızını belirlemek için bir hız nesnesi oluşturuyoruz (10 Hz)
    while not rospy.is_shutdown():
        pub.publish(hiz_mesaji)  # pub.publish diyerek hız mesajını yayınlıyoruz
        rate.sleep()


