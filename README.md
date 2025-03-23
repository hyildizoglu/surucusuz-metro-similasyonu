Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)

📌 Proje Tanımı

Bu proje, sürücüsüz metro sistemlerinin daha verimli çalışmasını sağlamak amacıyla geliştirilmiştir. Metro ağı içerisindeki istasyonlar arası en kısa ve en az aktarmalı rotaların belirlenmesi, toplu taşımadaki yolculuk sürelerini kısaltmak, yolcu memnuniyetini artırmak ve algoritmik düşünceyle gerçek dünya problemlerini çözmek açısından oldukça önemlidir. Bu doğrultuda, Python programlama dili ile geliştirilen bu projede, BFS (Breadth-First Search) algoritması ile en az aktarmalı rotalar, A* algoritması ile ise en hızlı (en kısa süreli) rotalar hesaplanmaktadır. Ayrıca tkinter kütüphanesi ile görsel arayüz tasarlanmış, networkx ve matplotlib kütüphaneleri ile metro ağ yapısı grafiksel olarak kullanıcıya sunulmuştur.

-------Proje Amaçları-----

* Metro istasyonlarının ve hatlarının grafik veri yapısı ile modellenmesi

* BFS algoritması ile istasyonlar arası en az aktarma yapılan rotayı bulmak

* A* algoritması ile istasyonlar arası en kısa süreli rotayı bulmak

* Gerçek bir metro ağını temsil eden örnek bir sistem üzerinde algoritmaları test etmek

* Kullanıcı dostu bir arayüz ile başlangıç ve hedef istasyonların seçimini sağlamak

* Kullanıcıya hem metinsel hem de görsel olarak rotayı göstermek

* Kodun modüler ve anlaşılır bir yapıda yazılması

----- Kullanılan Teknolojiler & Kütüphaneler -------


---tkinter

Python'un yerleşik GUI kütüphanesidir. Başlangıç ve hedef istasyon seçimleri ile butonlar bu kütüphane ile yapılmıştır.

---networkx

Grafik veri yapıları ve görselleştirme için kullanılmıştır. Metro ağının bağlantıları bu yapı ile oluşturulmuştur.

---matplotlib

NetworkX ile birlikte kullanılarak metro ağı görselleştirilmiştir. İstasyonlar ve bağlantılar çizilmiştir.

---heapq

A* algoritmasında öncelikli kuyruk yapısı için kullanılmıştır.

---collections

BFS algoritmasında çift uçlu kuyruk (deque) kullanımı için tercih edilmiştir.

---typing

Kodun okunabilirliğini ve güvenliğini artırmak için tip ipuçları verilmiştir.
----------------------------------------------------------------------------------------------------
 Algoritmaların Çalışma Mantığı

**** BFS (Breadth-First Search) *****

BFS algoritması grafın katman katman gezilmesini sağlar. Bu projede BFS algoritması ile en az aktarmalı rota bulunmuştur. Yani, istasyonlar arası geçen sürelerden bağımsız olarak, başlangıç noktasından hedefe en az sayıda durakla ulaşılacak yol tercih edilmiştir. BFS algoritması sırasında:

Ziyaret edilen istasyonlar takip edilmiştir

Kuyruk yapısı kullanılarak (deque) istasyonlar sırayla ziyaret edilmiştir

Hedef istasyona ilk ulaşıldığında algoritma durdurulmuş ve o ana kadar izlenen yol döndürülmüştür

***** A* (A Star Search Algorithm) *****

A* algoritması, graf üzerinde hedefe giden en kısa (süre bakımından) yolu bulmak için kullanılan bir yol bulma algoritmasıdır. Projede, her istasyon arası bağlantıya bir süre değeri atanmıştır (örneğin Kızılay -> Ulus: 4 dk gibi). A* algoritması:

Öncelik kuyruğu (priority queue) kullanılarak her adımda en düşük maliyetli istasyonu seçmiştir

Gidilen yolun toplam süresi her adımda hesaplanmıştır

Hedefe ulaşıldığında o ana kadarki en kısa süreli rota döndürülmüştür

Bu projede heuristic (tahmini uzaklık) değeri kullanılmamıştır; sadece gerçek süreler baz alınmıştır (Dijkstra benzeri)

**** Arayüz Özellikleri *****

Kullanıcı arayüzü tkinter kütüphanesi ile tasarlanmıştır. Arayüzün amacı, algoritmaları kullanıcıya kolay bir şekilde test ettirebilmek ve algoritmaların sonuçlarını görselleştirmektir.

Başlangıç ve hedef istasyonlar için açılır kutular

"En Az Aktarma (BFS)" butonu

"En Hızlı Rota (A*)" butonu

"Metro Ağı Grafiğini Göster" butonu

Rota metinsel olarak ekranda gösterilmektedir

Metro ağı networkx ve matplotlib ile çizilmektedir

Bulunan rotalar yeşil çizgiyle vurgulanırken diğer bağlantılar gri olarak kalmaktadır

Grafikler tkinter içine gömülmekte, ayrı bir pencere açılmamaktadır

!!!!! Örnek Kullanım Adımları !!!!!

Proje dosyalarını aynı klasörde bulundurunuz:

HayriyeNurYildizoglu_MetroSimulation.py

metro_gui.py

Terminal veya IDE üzerinden metro_gui.py dosyasını çalıştırınız:

Açılan pencerede başlangıç ve hedef istasyonu seçiniz

"En Az Aktarma (BFS)" veya "En Hızlı Rota (A*)" butonuna tıklayınız

Rota metinsel olarak aşağıda gösterilecektir

Aynı zamanda metro ağı grafiği de çizilecek, rota yeşil ile vurgulanacaktır

***Örnek Test Senaryoları

AŞTİ -> OSB

Batıkent -> Keçiören

Keçiören -> AŞTİ

Bu testler algoritmaların doğru çalıştığını test etmek amacıyla eklenmiştir.

***** Geliştirme Fikirleri *****

Metro ağı haritasının coğrafi koordinatlarla eşlenmesi

Hatlara özel renkler atanması (örneğin kırmızı hat kırmızı renkte çizilsin)

Kullanıcıdan metro hattı ve süre bilgisi girişi alınarak dinamik ağ oluşturulması

Rota boyunca toplam durak sayısı, toplam aktarma sayısı gibi istatistiklerin verilmesi

A* algoritmasına heuristic (tahmini uzaklık) fonksiyonu eklenmesi

İstasyonlar arası bekleme süresi gibi gerçek zamanlı parametrelerin eklenmesi

*** Geliştirici Notu ****

Bu proje tarafımdan eğitim amacıyla gerçekleştirilmiştir. Sadece algoritmaların ve grafiksel arayüzlerin çalışmasını test etmeye yönelik örnek bir metro ağı modeli oluşturulmuştur. Gerçek hayattaki metro hatları ve süreleri birebir yansıtılmamaktadır.

Kod yapısının modüler ve sade olmasına özellikle dikkat edilmiştir. Her algoritma ayrı ayrı tanımlanmış, tüm işlemler fonksiyonlar aracılığıyla yürütülmüştür. Bu sayede hem anlaşılır hem de geliştirilebilir bir yapı oluşturulmuştur.

---- Gereksinimler !!!!

Bu projeyi çalıştırmak için Python 3.8 veya üzeri bir sürüm gereklidir. Aşağıdaki kütüphanelerin sisteminizde yüklü olması gerekir:
networkx , matplotlib

Diğer kutuphaneler python ile birlikte gelir.
