*birfen-staj*

**Odom Verileri**

Odometri, bir robotun tekerleklerinin dönme hareketlerini ve mesafelerini kullanarak konum tahmini yapma yöntemidir. Bu tahminler, tekerlek dönüş sayıları ve tekerlek çapları gibi bilgilere dayanır. Odometri, robotun kısa mesafeli hareketlerde ve anlık pozisyon güncellemelerinde kullanılır.

Turtlebot3'ün odom verilerini çekmek için öncelikle terminali ikiye bölmeliyiz ve bir dünya başlatmamız gerekmektedir. Örneğin, `roslaunch turtlebot3_gazebo turtlebot3_stage_4.launch` komutunu kullanarak bir dünya başlatabiliriz. Daha sonra diğer terminal ekranında `rosrun uygulamalar odom_verileri.py` komutunu yazarak Python dosyasını başlatmalıyız. Bu işlemlerden sonra odom bilgileri terminalde listelenecektir.

**cmd_vel Topic Yayını**

`cmd_vel` genellikle robotlara hız ve yönlendirme komutlarını iletmek için kullanılır. Bu komutlarla robotu hareket ettirebilir ve kontrol edebiliriz.

Öncelikle terminal ekranını üçe bölüyoruz. İlk terminalde `roscore` komutunu yazarak ROS çekirdeğini aktif ediyoruz. İkinci terminalde `rosrun uygulamalar cmd_vel.py` dosyasını başlatıyoruz. Üçüncü terminalde ise `rostopic echo /cmd_vel` komutunu yazarsak `cmd_vel` üzerinden yayınlanan hız mesajları görüntülenebilir.

Bu şekilde, `cmd_vel` konusu aracılığıyla robotun hız ve yönlendirme komutlarını görebilir ve robotun davranışını kontrol edebiliriz. Bu tür komutlar, Turtlebot3 gibi mobil robotlarla etkileşimde bulunmak ve onları yönlendirmek için kullanışlıdır.



# servis çalıştırma örneği

rosrun rospy_tutorials add_two_ints_server komutu, rospy_tutorials paketinde bulunan add_two_ints_server adlı bir Python düğümünü çalıştırır. Bu düğüm, iki tamsayıyı toplayan bir hizmet sunucusunu başlatır.
Terminal ekranını üçe bölüyoruz. Birinci ekranda roscore komutunu yazarak ros çekirdeğini başlatıyoruz. İkinci ekranda rosrun rospy_tutorials add_two_ints_server komutunu başlatıyoruz. Üçüncü ekranda rosservice list yaparak ros servislerine göz atıyoruz. Daha sonra rosservice info /add_two_ints yazarak / add_two_ints servisinin bilgilerine bakıyoruz. rosservice call /add_two_ints "a:5 b:7" yazarak enterlıyoruz. Servis bize yazdığımız iki sayının toplamı olan 12 sayısını veriyor.



# servis kullanarak asansör örneği

Öncelikle srv klasörüne asansor_komut.srv dosyası oluşturuyoruz. CMakeList.txt'e add_service_files(FILES asansor_komut.srv) dizini eklememiz gerekli. Daha sonra catkin_make ile derleme işlemi ve catkin_make install ile de oluşturulan servis dosyasının başlık dosyalarının yükleme işlemi tamamlanır. Uygulamalar klasöründeki scripts klasörüne servis.py ve istemci.py oluşturulur.  servis.py ve istemci.py kodlaması bittikten chmod +x ile iki dosya da derlenir. Terminal ekranı üçe bölünür. Birincisinde roscore başlatılır. Diğerinde servis düğümü çağırılır(rosrun uygulamalar servis.py). Üçüncü pencerede istemci düğümü çalıştırılır(rosrun uygulamalar istemci.py). Terminal ekranından çıkmak istenen kat aralığı girilir.



# topic örneği

sctipts klasörünün içerisine topic_orneği.py adında bir dosya oluşturuyoruz. Daha sonra bu dosyaya kodlarımızı yazıp terminalden chmod +x le derliyoruz. Terminali ikiye bölüyoruz. İlk ekranda roscore komutunu yazarak ros çekirdeğini başlatıyoruz. İkinci ekranda rosrun uygulamalar topic_ornegi.py diyerek dosyamızı başlatıyoruz.



# turtlebot3 düz gitme örneği

sctipts klasörünün içerisine duz_git.py adında bir dosya oluşturuyoruz. Daha sonra bu dosyaya kodlarımızı yazıp terminalden chmod +x le derliyoruz. Terminali ikiye bölüyoruz. İlk pencerede roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch komutunu çalıştırıp boş dünya ortamını gazeboda açmış oluyoruz . ikinci ekranda rosrun uygulamalar duz_git.py komutunu çalıştırarak python dosyamızı başlatıyoruz. Simülasyon sonunda turtlebot3 1 metre düz gitmiş oluyor.



# turtlesim kare yuvarlak üçgen örneği

sctipts klasörünün içerisine turlesim.py adında bir dosya oluşturuyoruz. Daha sonra bu dosyaya kodlarımızı yazıp terminalden chmod +x le derliyoruz. Terminali üçe bölüyoruz. İlk ekrandan roscore komutuyla ros u aktif ediyoruz. İkinci ekrana rosrun turtlesim turtlesim_node komutunu yazarak turlesimi başlatıyoruz. Son ekrandan rosrun uygulamalar turtlesim.py komutunu yazıp kodu çalıştırıyoruz. Turle ın çizmesini istediğiniz şekli giriyorsunuz. Şekli çiziyor ve en sonunda ekranı temizleyip arka plan rengini değiştiriyor.



# turtlesim belirlenmiş yol örneği

sctipts klasörünün içerisine turlesim_yol.py adında bir dosya oluşturuyoruz. Daha sonra bu dosyaya kodlarımızı yazıp terminalden chmod +x le derliyoruz. Terminali üçe bölüyoruz.İlk ekrandan roscore komutuyla ros u aktif ediyoruz. İkinci ekrana rosrun turtlesim turtlesim_node komutunu yazarak turlesimi başlatıyoruz. Üçüncü ekranda rosrun uygulamalar turtlesim_yol.py komutunu yazarak python dosyamızı çalıştırıyoruz. Dosyanın içerisinde belirlenmiş olan yolu turtle izliyor ve tamamlıyor.



# turtlesim senkron örneği

sctipts klasörünün içerisine senkron_turtles.py adında bir dosya oluşturuyoruz. Daha sonra bu dosyaya kodlarımızı yazıp terminalden chmod +x le derliyoruz. Terminali dörde bölüyoruz.İlk ekrandan roscore komutuyla ros u aktif ediyoruz. İkinci ekrana rosrun turtlesim turtlesim_node komutunu yazarak turlesim1 i başlatıyoruz. Üçüncü ekrana rosrun turtlesim turtlesim_node __name:=turtle2 yazarak turlesim2 yi başlatıyoruz. Dördüncü ekranda rosrun uygulamalar senkron_turtle.py komutunu çalıştırıyoruz. Turtle1 ve turtle2 aynı anda daire çiziyor.



# Turtlebot ile sanal ortamda haritalama ve navigasyon

Terminal ekranını dörde bölüyoruz. İlk ekranda roslaunch turtlebot3_gazebo turtlebot3_house.launch komutunu yazarak gazeboyu başlatıyoruz. ikinci ekrandan roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping komutunu girerek Rvizi çalıştırıyoruz. Üçüncü ekranda teleopu başlatmak için rosrun turtlebot3_teleop turtlebot3_teleop_key komutunu giriyoruz.
House un tamamını W,A,S,D,X ile gezerek Rvizde harita oluşturuyoruz. Oluşturduğumuz haritayı dördüncü ekranda rosrun map_server map_saver -f ~/tb3_house_map yazarak kaydediyoruz. Daha sonra gazebo ve Rvizi kapatıyoruz. Tekrardan turtlebot3_gazebo turtlebot3_house.launch yazarak gazebo ortamını başlatıyoruz. Daha sonra roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/ibrahim/tb3_house_map.yaml yazarak kaydettiğimiz haritayı Rvizde açıyoruz. Turtlebot un gazebo ve Rvizde ki konumunu eşitleyip 2D nav goal çubuğunu kullanarak haritanın her hangi bir yerine robotu otonom yönlendirebiliyoruz.



# Turtlebot düz gidip engel gördüğünde döndüğü örnek

sctipts klasörünün içerisine duz_git_don.py adında bir dosya oluşturuyoruz. Daha sonra bu dosyaya kodlarımızı yazıp terminalden chmod +x le derliyoruz. Terminal ekranını ikiye bölüyoruz. İlk ekranda roslaunch turtlebot3_gazebo turtlebot3_house.launch komutunu çalıştırıyoruz. İkinci ekranda rosrun uygulamalar duz_git_don.py yazarak yazdığımız kodu çalıştırıyoruz. Turtlebot3 düz hareket ediyor bir metre kala duvar görürse dönüp düz devam ediyor. 


























