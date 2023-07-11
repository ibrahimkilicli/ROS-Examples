# birfen-staj


#odom verileri

Odometri, bir robotun tekerleklerinin dönme hareketlerini ve mesafelerini kullanarak konum tahmini yapma yöntemidir. Bu tahminler, tekerlek dönüş sayıları ve tekerlek çapları gibi bilgilere dayanır. Odometri, robotun kısa mesafeli hareketlerde ve anlık pozisyon güncellemelerinde kullanılır.

Turtlebot3' ün odom verilerini çekebilmemiz için terminali öncelikle ikiye bölüp herhangi bir dünya başlatmamız gerekli. Örneğin roslaunch turtlebot3_gazebo turtlebot3_stage_4.launch başlatılabilir. Daha sonra diğer terminal ekranında rosrun uygulamalar odom_verileri.py komutunu yazarak python dosyasını başlatmalıyız. Bu işlemlerden sonra odom bilgileri terminalde listelenecektir.

#cmd_vel topic yayını

cmd_vel genelde robotlara hız ve yönlendirme komutlarını iletmek için kullanılır.
Öncelikle terminal ekranını üçe bölüyoruz. Ekranın birinde roscore yazarak ros çekirdiğini aktif ediyoruz. İkinci ekranda rosrun uygulamalar cmd_vel.py dosyasını başlatıyoruz. Üçüncü ekranda ise 
rostopic echo /cmd_vel yazarsak cmd_vel üzerinden yayınlanan hız mesajı görüntülenebilir.

