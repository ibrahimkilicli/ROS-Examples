#!/usr/bin/env python3

import rospy
from uygulamalar.srv import asansor_komut


def Yukari_Asagi_Fonksiyonu(istek):
    if (istek.hedef_kat < 6) and (istek.hedef_kat > 0):
        cevap = "Asansör {} birim yukarı kaldırıldı".format(istek.hedef_kat)
        return cevap

def cevap_gonder():
    rospy.init_node("server_dugumu")
    rospy.Service("hedef_kat", asansor_komut, Yukari_Asagi_Fonksiyonu)
    rospy.spin()

cevap_gonder()

    
