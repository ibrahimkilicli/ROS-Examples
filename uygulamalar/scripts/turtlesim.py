#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
import random

def sekil_ciz(sekil):
    rospy.init_node('turtle_shapes', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  

    vel_msg = Twist()

    

    # Çizim şekline göre hareket komutlarını belirle
    if sekil == 'kare':
        for _ in range(4):
            rospy.sleep(0.5)
            vel_msg.linear.x = 3
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            rospy.sleep(1)

            vel_msg.linear.x = 0
            vel_msg.angular.z = 1.570796  #90 derece
            velocity_publisher.publish(vel_msg)
            rospy.sleep(1)
    elif sekil == 'yuvarlak':
        rospy.sleep(0.5)
        vel_msg.linear.x = 1
        vel_msg.angular.z = 0.523598  #30 derece
        for _ in range(12):
            velocity_publisher.publish(vel_msg)
            rospy.sleep(1)

    elif sekil == 'üçgen':
        for _ in range(3):
            rospy.sleep(0.5)
            vel_msg.linear.x = 2
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            rospy.sleep(1)

            vel_msg.linear.x = 0
            vel_msg.angular.z = 2.094395   #120 derece
            velocity_publisher.publish(vel_msg)
            rospy.sleep(1)
    #rospy.spin()
def change_background_color_client():


          rospy.wait_for_service('/clear')

          try: 

            rospy.set_param('/turtlesim/background_r', random.randint(0, 255))
            rospy.set_param('/turtlesim/background_g', random.randint(0, 255))
            rospy.set_param('/turtlesim/background_b', random.randint(0, 255))

            change_background_color = rospy.ServiceProxy('/clear', Empty)

            resp = change_background_color()

            return resp

          except rospy.ServiceException as e:   #yakalanan hatayı e değişkenine atayıp str(e) ile yazdırıyoruz.
           
           rospy.loginfo("Arka plan rengini değiştirme hatası:", str(e))



if __name__ == '__main__':
    sekil = input("Çizilecek şekli girin (kare/yuvarlak/üçgen): ")
    sekil_ciz(sekil)
    change_background_color_client()







