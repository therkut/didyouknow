# Twitter Bot

Bu Python kodu, Twitter üzerinde belirli bir hesap aracılığıyla otomatik tweetler paylaşan bir Twitter botunu oluşturmak için kullanılır. Bu bot, Türkçe Vikipedi'nin ana sayfasından alınan en son güncel bilgileri kullanarak tweetler oluşturur ve bu tweetleri belirli bir süre aralığıyla paylaşır.

## Hedef

Bu Python kodu, belirtilen Wikipedia sayfasından güncel bilgileri çekerek bu bilgileri bir dizi tweet olarak Twitter'a gönderen bir otomatik tweet botunu uygulamaktadır. Tweetler, belirli bir etiketle (#Bugün #Tarih #Spor #Sanat) birleştirilmiş şekilde paylaşılır.

## Gereksinimler

Kodun düzgün çalışabilmesi için aşağıdaki Python kütüphanelerinin kurulu olması gerekmektedir:
- requests
- time
- requests_oauthlib
- BeautifulSoup
- html

Ayrıca Twitter API'sine erişim sağlamak için Twitter API anahtarlarına (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET) ihtiyaç vardır. Bu anahtarlar çevresel değişkenlerde saklanmalıdır.

## Adımlar

Kod, aşağıdaki adımları takip eder:

1. Wikipedia verisi çekme:
   - Wikipedia'nın Türkçe ana sayfasına (https://tr.wikipedia.org/wiki/Anasayfa) HTTP isteği gönderilir ve sayfa verisi alınır.
   - BeautifulSoup kütüphanesi kullanılarak sayfa verisi işlenir.
   - 'td' etiketi ve 'mp-bm' özniteliğine sahip içerik bulunur.
   - 'td' etiketi içindeki 'ul' etiketi bulunur.
   - 'ul' etiketi içindeki tüm 'li' etiketleri bulunur ve ters sırayla sıralanır.
   - İlk 5 'li' öğesi alınır ve tweet_list adlı bir liste oluşturulur.

2. Tweet Oluşturma:
   - Her 'li' öğesi üzerinde strip_tags fonksiyonu kullanılarak HTML etiketleri temizlenir ve tweet_list listesine eklenir.
   - tweet_list öğeleri birleştirilerek tek bir tweet metni oluşturulur.

3. Twitter'a Tweet Gönderme:
   - OAuth1Session ile Twitter API'ye erişim sağlanır.
   - Her tweet için Twitter API'ye gönderilecek JSON verisi oluşturulur.
   - Her tweet gönderildikten sonra 30 saniyelik bir bekleme süresi eklenir.

4. Hata İşleme:
   - Herhangi bir hata durumunda, hata mesajı yazdırılır ve işlem devam eder.

## Kullanım

Bu kod, belirli bir Twitter hesabı üzerinden tweetler göndermek için tasarlanmıştır. Kullanıcı, Twitter API anahtarlarını çevresel değişkenlere atamalıdır. Ayrıca bu botun düzenli aralıklarla çalıştırılması gerekmektedir.

## Notlar

- Bu kod, belirli bir Wikipedia sayfasından veri çekmek ve Twitter üzerinden tweet göndermek için özelleştirilebilir. İlgili Wikipedia sayfasını ve tweet içeriğini değiştirebilirsiniz.

- Twitter API kullanımı için [Twitter API dokümantasyonuna](https://developer.twitter.com/en/docs) başvurun.

- Bu kod, herhangi bir özelleştirme veya geliştirme için temel bir çerçeve sağlar.

Umarız bu README belirli bir işlevi yerine getiren Python kodunun işleyişini daha iyi anlamanıza yardımcı olur.
