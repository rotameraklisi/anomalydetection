# anomalydetection

ANOMALY TESPİTİ

Bu çalışmanın amacı, büyük veri madenciliği tekniklerinden biri olan makine öğrenmesinin sınıflandırma algoritmalarından k-NN algoritması algoritması ile KDDCup99 veri seti üzerinde analizler yapılarak olası anomalilerin tespitinin analizi gerçekleştirilmiştir.

Kullanılan Ortam - Jupyter Notebook
Jupyter Notebook aldığımız notları ve hesaplamaları beraber tutmak için , Python kodları yazma olanağı sağlayan, görselleştirme özelliği bulunan yararlı bir araçtır.

Kullanılan Dil - Python
Python, nesne yönelimli, yorumlamalı, birimsel ve etikileşimli yüksek seviyeli bir programlama dilidir.

Kullanılan Algoritma- K-NN
Makine öğrenmesi algoritmaları arasında en basiti olarak belirtilmektedir. Modeli oluşturmak, yalnızca eğitim datasetinin saklanmasından oluşur. Yeni bir veri noktası için bir tahmin yapmak için algoritma, eğitim verisetindeki ‘’en yakın komşuları’’ içindeki en yakın veri noktalarını bulur. Çoğunluk olan taraf seçilir. Öngörüde bulunmak istediğimiz noktaya en yakın eğitim verilerini dikkate alır. Bütün eğiitim seti içindekiler ile arasındaki uzaklık bulunur. En yakın k örnek seçilir. Hem classifivation hem regression için kullanıılr.

Dataset - KDD Cup'99 (http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html -kddcup.data_10_ percent_corrected)
Dataset, 41 featuredan, yaklaşık 75Mb boyutunda 494021 kayıttan oluşmaktadır. 

Verisetinin daha anlamlı hale gelmesi için özellik seçmesi yapılmasına karar verilmiştir ve özellik seçimi yaparken literatür taramasında ulduğum “Lojistik Regresyon ile Bilgisayar Ağlarında Anomali Tespiti” adlı makale göz önüne alınmıştır. Makaleye göre aşağıdaki prensiplere uyarak bu sayıyı 9’a indirilmiştir:

-Parametrelerin birbirlerinden bağımsız olanları seçilmiştir. Örneğin root_shell, su_attempted, num_root alanlarının tümü birden alınmak yerine su_attempted alanı alınmıştır.
-Parametrelerin bağımlı değişkeni etkilemeyecek olanları seçilmemiştir.
-Veriler daha kolay işlenebilmek için binary hale getirilmiştir.

Bu prensiplere uyarak özellik olarak aşağıda sıralanan özellikleri kullanılmıştır.
 protocol_type
 service
 flag
 land
 wrong_fragment
 hot
 um_failed_logins
 nsu_attempted
 num_access_files

Özellik seçiminden sonra verisetinden eksik veri olup olmadığı kontrol edilmiş ve eksik veri bulunmamaktadır. Verinin önişleme aşamasında verisetinin ölçeklenmesi de önemlidir. Veri ölçekleme, mevcut konumu ve yönü bozulamadan büyütüp küçültmek, veriyi algoritmanın daha iyi anlayabileceği şekle getirmek, veriyi daha iyi ifade etmeyi sağlamaktadır. Bu çalışmada ölçekleme olarak pratikte fazlasıyla kullanılan standardizasyon yöntemi tercih edilmiştir. Böylece, verisetindeki her feature için ortalaması 0, varyansı 1 yapar ve tüm özelliklerin aynı büyüklüte olmasını sağlar, veriyi sıkıştırır.

Verisetimizi modele uygun hale getirmek için projenin ilk aşamasında eğitim verisi %70, test verisi %30 olarak parçalanmıştır ve eğitim verileri ile eğitim aşaması tamamlanıp model oluşturulmuştur. İkinci aşamasında, k-fold Cross Validation yöntemi ile tüm veri 3 ile 10 parçaya bölünerek teker teker her parça üzerinden eğitim ve test verisi olarak kullanılarak değerlendirilmiştir.

Modelin başarısını ölçerken confusion matrix diye adlandırılan karışıklık matrisinden yararlanılır. Confusion matrix, gerçek değerlerin bilindiği test verisi üzerinde bir sınıflandırma modelinin doğruluğunu, performansını ölçmek için kullanılmaktadır.
k-NN algoritmasında parametre olarak en yakın komşu sayısı “k” değeri belirleniyor. Bu çalışmada k değerine 1’den 30’ a kadar değerler verilmiştir. Çalışma sonucundaki modelin doğruluk ya da başarı oranı şekil 2.2’ de görülmektedir. Şekilden de anlaşılacağı üzere k parametresinin değeri arttıkça modelimizin başarısı ufak tefek artıp azalma göstermektedir. En yüksek başarı oranı k= 3 iken %0.994473 olarak sonuçlanmıştır ve son olarak k=26 değerinde %0.993993’ te sabitlenmiştir.

Ayrıntılar için -> raporr.pdf

