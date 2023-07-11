#!/usr/bin/env python3

import rospy
from uygulamalar.srv import asansor_komut


def istekteBulun(x):
    rospy.wait_for_service("hedef_kat")
    try:
        servis = rospy.ServiceProxy("hedef_kat", asansor_komut)
        cevap = servis(x)
        return cevap.kaldirildi
        
    except rospy.ServiceException:
        print("Servisle ilgili hata!")
    
hedef = float(input("Hedef katı giriniz: "))
t = istekteBulun(hedef)
print(t)

