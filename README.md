# birfen-staj


#odom verileri

Odometri, bir robotun tekerleklerinin dönme hareketlerini ve mesafelerini kullanarak konum tahmini yapma yöntemidir. Bu tahminler, tekerlek dönüş sayıları ve tekerlek çapları gibi bilgilere dayanır. Odometri, robotun kısa mesafeli hareketlerde ve anlık pozisyon güncellemelerinde kullanılır.

Turtlebot3' ün odom verilerini çekebilmemiz için terminali öncelikle ikiye bölüp herhangi bir dünya başlatmamız gerekli. Örneğin roslaunch turtlebot3_gazebo turtlebot3_stage_4.launch başlatılabilir. Daha sonra diğer terminal ekranında rosrun uygulamalar odom_verileri.py komutunu yazarak python dosyasını başlatmalıyız. Bu işlemlerden sonra odom bilgileri terminalde listelenecektir.



#cmd_vel topic yayını

cmd_vel genelde robotlara hız ve yönlendirme komutlarını iletmek için kullanılır.
Öncelikle terminal ekranını üçe bölüyoruz. Ekranın birinde roscore yazarak ros çekirdiğini aktif ediyoruz. İkinci ekranda rosrun uygulamalar cmd_vel.py dosyasını başlatıyoruz. Üçüncü ekranda ise 
rostopic echo /cmd_vel yazarsak cmd_vel üzerinden yayınlanan hız mesajı görüntülenebilir.



#servis çalıştırma örneği

rosrun rospy_tutorials add_two_ints_server komutu, rospy_tutorials paketinde bulunan add_two_ints_server adlı bir Python düğümünü çalıştırır. Bu düğüm, iki tamsayıyı toplayan bir hizmet sunucusunu başlatır.
Terminal ekranını üçe bölüyoruz. Birinci ekranda roscore komutunu yazarak ros çekirdeğini başlatıyoruz. İkinci ekranda rosrun rospy_tutorials add_two_ints_server komutunu başlatıyoruz. Üçüncü ekranda rosservice list yaparak ros servislerine göz atıyoruz. Daha sonra rosservice info /add_two_ints yazarak / add_two_ints servisinin bilgilerine bakıyoruz. rosservice call /add_two_ints "a:5 b:7" yazarak enterlıyoruz. Servis bize yazdığımız iki sayının toplamı olan 12 sayısını veriyor.



#servis kullanarak asansör örneği

Öncelikle srv klasörüne asansor_komut.srv dosyası oluşturuyoruz. CMakeList.txt'e add_service_files(FILES asansor_komut.srv) dizini eklememiz gerekli. Daha sonra catkin_make ile derleme işlemi ve catkin_make install ile de oluşturulan servis dosyasının başlık dosyalarının yükleme işlemi tamamlanır. Uygulamalar klasöründeki scripts klasörüne servis.py ve istemci.py oluşturulur.  servis.py ve istemci.py kodlaması bittikten chmod +x ile iki dosya da derlenir. Terminal ekranı üçe bölünür. Birincisinde roscore başlatılır. Diğerinde servis düğümü çağırılır(rosrun uygulamalar servis.py). Üçüncü pencerede istemci düğümü çalıştırılır(rosrun uygulamalar istemci.py). Terminal ekranından çıkmak istenen kat aralığı girilir.

















