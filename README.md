# birfen-staj

**Odom Verileri**

Odometri, bir robotun tekerleklerinin dönme hareketlerini ve mesafelerini kullanarak konum tahmini yapma yöntemidir. Bu tahminler, tekerlek dönüş sayıları ve tekerlek çapları gibi bilgilere dayanır. Odometri, robotun kısa mesafeli hareketlerde ve anlık pozisyon güncellemelerinde kullanılır.

Turtlebot3'ün odom verilerini çekmek için öncelikle terminali ikiye bölmeliyiz ve bir dünya başlatmamız gerekmektedir. Örneğin, `roslaunch turtlebot3_gazebo turtlebot3_stage_4.launch` komutunu kullanarak bir dünya başlatabiliriz. Daha sonra diğer terminal ekranında `rosrun uygulamalar odom_verileri.py` komutunu yazarak Python dosyasını başlatmalıyız. Bu işlemlerden sonra odom bilgileri terminalde listelenecektir.

**cmd_vel Topic Yayını**

`cmd_vel` genellikle robotlara hız ve yönlendirme komutlarını iletmek için kullanılır. Bu komutlarla robotu hareket ettirebilir ve kontrol edebiliriz.

Öncelikle terminal ekranını üçe bölüyoruz. İlk terminalde `roscore` komutunu yazarak ROS çekirdeğini aktif ediyoruz. İkinci terminalde `rosrun uygulamalar cmd_vel.py` dosyasını başlatıyoruz. Üçüncü terminalde ise `rostopic echo /cmd_vel` komutunu yazarsak `cmd_vel` üzerinden yayınlanan hız mesajları görüntülenebilir.

Bu şekilde, `cmd_vel` konusu aracılığıyla robotun hız ve yönlendirme komutlarını görebilir ve robotun davranışını kontrol edebiliriz. Bu tür komutlar, Turtlebot3 gibi mobil robotlarla etkileşimde bulunmak ve onları yönlendirmek için kullanışlıdır.



**Servis Çalıştırma Örneği**

Terminal ekranını üçe bölüyoruz. Birinci ekranda `roscore` komutunu yazarak ROS çekirdeğini başlatıyoruz. İkinci ekranda `rosrun rospy_tutorials add_two_ints_server` komutunu çalıştırarak `rospy_tutorials` paketinde bulunan `add_two_ints_server` adlı bir Python düğümünü çalıştırıyoruz. Bu düğüm, iki tamsayıyı toplayan bir hizmet sunucusunu başlatır. Üçüncü ekranda `rosservice list` komutu ile ROS servislerine göz atıyoruz. Daha sonra `rosservice info /add_two_ints` komutunu kullanarak `/add_two_ints` servisinin bilgilerine bakıyoruz. `rosservice call /add_two_ints "a:5 b:7"` komutunu girerek servise iki sayı gönderiyoruz ve servis bize bu sayıların toplamı olan 12 sayısını döndürüyor.

**Servis Kullanarak Asansör Örneği**

Öncelikle `srv` klasörüne `asansor_komut.srv` dosyasını oluşturuyoruz. `CMakeLists.txt` dosyasına `add_service_files(FILES asansor_komut.srv)` satırını eklememiz gereklidir. Daha sonra `catkin_make` komutu ile derleme işlemini gerçekleştiriyoruz ve `catkin_make install` komutu ile de oluşturulan servis dosyasının başlık dosyalarını yüklüyoruz. Uygulamalar klasöründeki `scripts` klasörüne `servis.py` ve `istemci.py` dosyalarını oluşturuyoruz. `servis.py` ve `istemci.py` dosyalarının kodlaması tamamlandıktan sonra `chmod +x` komutu ile her iki dosyayı da derliyoruz. Terminal ekranını üçe bölerek: Birincisinde `roscore` başlatılır. Diğerinde servis düğümü çağrılır (`rosrun uygulamalar servis.py`). Üçüncü pencerede istemci düğümü çalıştırılır (`rosrun uygulamalar istemci.py`). Terminal ekranından çıkmak istenen kat aralığını girerek asansörü kullanabiliriz.

**Topic Örneği**

`scripts` klasörünün içerisine `topic_orneği.py` adında bir dosya oluşturuyoruz. Daha sonra bu dosyaya kodlarımızı yazıp terminalden `chmod +x` komutu ile derliyoruz. Terminali ikiye bölüyoruz. İlk ekranda `roscore` komutunu yazarak ROS çekirdeğini başlatıyoruz. İkinci ekranda `rosrun uygulamalar topic_orneği.py` komutunu girerek dosyamızı başlatıyoruz. Bu sayede, belirlediğimiz bir konu üzerinde ROS yayın ve dinleme işlemlerini gerçekleştirebiliriz.

**Turtlebot3 Düz Gitme Örneği**

`scripts` klasörünün içerisine `duz_git.py` adında bir dosya oluşturuyoruz. Daha sonra bu dosyaya kodlarımızı yazıp terminalden `chmod +x` komutu ile derliyoruz. Terminali ikiye bölüyoruz. İlk pencerede `roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch` komutunu çalıştırarak boş dünya ortamını Gazebo'da açmış oluyoruz. İkinci ekranda `rosrun uygulamalar duz_git.py` komutunu çalıştırarak Python dosyamızı başlatıyoruz. Bu sayede Turtlebot3 simülasyonunda, robotun 1 metre düz gitmesini sağlayabiliriz.

**Turtlesim Kare, Yuvarlak, Üçgen Örneği**

`scripts` klasörünün içerisine `turtlesim.py` adında bir dosya oluşturuyoruz. Daha sonra bu dosyaya kodlarımızı yazıp terminalden `chmod +x` komutu ile derliyoruz. Terminali üçe bölüyoruz. İlk ekrandan `roscore` komutu ile ROS'u aktif ediyoruz. İkinci ekrana `rosrun turtlesim turtlesim_node` komutunu yazarak turtlesimi başlatıyoruz. Son ekrandan `rosrun uygulamalar turtlesim.py` komutunu yazarak kodu çalıştırıyoruz. Turtle'a çizmesini istediğimiz şekli giriyoruz. Şekli çiziyor ve en sonunda ekranı temizleyip arka plan rengini değiştiriyoruz.



**Turtlesim Belirlenmiş Yol Örneği**

`scripts` klasörünün içerisine `turtlesim_yol.py` adında bir dosya oluşturuyoruz. Daha sonra bu dosyaya kodlarımızı yazıp terminalden `chmod +x` komutu ile derliyoruz. Terminali üçe bölüyoruz. İlk ekrandan `roscore` komutuyla ROS'u aktif ediyoruz. İkinci ekrana `rosrun turtlesim turtlesim_node` komutunu yazarak turtlesimi başlatıyoruz. Üçüncü ekranda `rosrun uygulamalar turtlesim_yol.py` komutunu yazarak Python dosyamızı çalıştırıyoruz. Dosyanın içerisinde belirlenmiş olan yolu turtle takip ederek tamamlıyor.

**Turtlesim Senkron Örneği**

`scripts` klasörünün içerisine `senkron_turtles.py` adında bir dosya oluşturuyoruz. Daha sonra bu dosyaya kodlarımızı yazıp terminalden `chmod +x` komutu ile derliyoruz. Terminali dörde bölüyoruz. İlk ekrandan `roscore` komutuyla ROS'u aktif ediyoruz. İkinci ekrana `rosrun turtlesim turtlesim_node` komutunu yazarak `turtlesim1`i başlatıyoruz. Üçüncü ekrana `rosrun turtlesim turtlesim_node __name:=turtle2` komutunu yazarak `turtlesim2`'yi başlatıyoruz. Dördüncü ekranda `rosrun uygulamalar senkron_turtle.py` komutunu çalıştırıyoruz. Turtle1 ve Turtle2 aynı anda daire çiziyor.

**Turtlebot ile Sanal Ortamda Haritalama ve Navigasyon**

Terminal ekranını dörde bölüyoruz. İlk ekranda `roslaunch turtlebot3_gazebo turtlebot3_house.launch` komutunu yazarak Gazebo'yu başlatıyoruz. İkinci ekrandan `roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping` komutunu girerek Rviz'i çalıştırıyoruz. Üçüncü ekranda `rosrun turtlebot3_teleop turtlebot3_teleop_key` komutunu girerek teleop'u başlatıyoruz. House'un tamamını `W`, `A`, `S`, `D`, `X` tuşları ile gezerek Rviz'de harita oluşturuyoruz. Oluşturduğumuz haritayı dördüncü ekranda `rosrun map_server map_saver -f ~/tb3_house_map` yazarak kaydediyoruz. Daha sonra Gazebo ve Rviz'i kapatıyoruz. Tekrardan `roslaunch turtlebot3_gazebo turtlebot3_house.launch` yazarak Gazebo ortamını başlatıyoruz. Daha sonra `roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/ibrahim/tb3_house_map.yaml` yazarak kaydettiğimiz haritayı Rviz'de açıyoruz. Turtlebot'un Gazebo ve Rviz'deki konumunu eşitleyip 2D nav goal çubuğunu kullanarak haritanın herhangi bir yerine robotu otonom yönlendirebiliyoruz.

**Turtlebot Düz Gidip Engel Gördüğünde Döndüğü Örnek**

`scripts` klasörünün içerisine `duz_git_don.py` adında bir dosya oluşturuyoruz. Daha sonra bu dosyaya kodlarımızı yazıp terminalden `chmod +x` komutu ile derliyoruz. Terminal ekranını ikiye bölüyoruz. İlk ekranda `roslaunch turtlebot3_gazebo turtlebot3_house.launch` komutunu çalıştırıyoruz. İkinci ekranda `rosrun uygulamalar duz_git_don.py` yazarak yazdığımız kodu çalıştırıyoruz. Turtlebot3 düz hareket ediyor ve bir metre kala duvar görürse dönüp düz devam ediyor.



























