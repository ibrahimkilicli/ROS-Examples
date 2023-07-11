# birfen-staj


#odom verileri

Odometri, bir robotun tekerleklerinin dönme hareketlerini ve mesafelerini kullanarak konum tahmini yapma yöntemidir. Bu tahminler, tekerlek dönüş sayıları ve tekerlek çapları gibi bilgilere dayanır. Odometri, robotun kısa mesafeli hareketlerde ve anlık pozisyon güncellemelerinde kullanılır.

Turtlebot3' ün odom verilerini çekebilmemiz için terminali öncelikle ikiye bölüp herhangi bir dünya başlatmamız gerekli. Örneğin roslaunch turtlebot3_gazebo turtlebot3_stage_4.launch başlatılabilir. Daha sonra diğer terminal ekranında rosrun uygulamalar odom_verileri.py komutunu yazarak python dosyasını başlatmalıyız. Bu işlemlerden sonra odom bilgileri terminalde listelenecektir.
