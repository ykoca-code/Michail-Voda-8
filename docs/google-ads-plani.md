# Google Ads Kurulum ve Kampanya Planı — Michail Voda 8

Meta reklam hesabındaki kısıtlama süreci belirsizken talebi ayakta tutacak ana kanal
Google Ads. Mantığı Meta'dan farklı: Meta'da talebi **siz yaratırsınız**, Google'da
zaten **arayan** kişiyi yakalarsınız. "Yunanistan golden visa" yazan biri niyetini
çoktan beyan etmiştir; bu yüzden lead maliyeti daha yüksek ama lead kalitesi daha iyidir.

---

## 1. Hesap açılışı (30 dakika)

1. **ads.google.com** → Start now → mevcut Google hesabınızla giriş.
2. Açılışta Google sizi "Smart Campaign" akışına sokmaya çalışır.
   Alt kısımdaki **"Switch to Expert Mode"** bağlantısına tıklayın; yoksa
   "Create an account without a campaign" seçeneğini kullanın. Smart mode'da
   anahtar kelime kontrolü yoktur, bu işte işe yaramaz.
3. Faturalandırma ülkesi **Türkiye**, para birimi **EUR**, saat dilimi **Europe/Istanbul**.
   *Para birimi ve saat dilimi sonradan değiştirilemez.* Bütçeyi euro düşündüğümüz için EUR.
4. Ödeme yöntemi: kredi kartı. Türkiye'de reklam harcamalarına **%20 dijital hizmet
   vergisi + KDV** yansır; 1.000 € bütçe kartınıza ~1.200 € olarak yansır, planlarken bunu ekleyin.

## 2. Dönüşüm ölçümü — KURULDU

**Durum: tamamlandı.** Aşağıdaki yapı canlıda çalışıyor.

| Bileşen | Değer |
|---|---|
| Google etiketi | `AW-18401005291` — `site/google.js` içinden dört sayfada da yükleniyor |
| Dönüşüm eylemi | `MV8 Ön Görüşme Talebi` |
| Yöntem | **URL kuralı** (kod yok) — "tesekkurler" içeren sayfa yüklenmesi |
| Hedef | Potansiyel müşteri formu gönderme |
| Değer | 250 € · sayım: bir kez · pencere: 30 gün |

### Neden kod (event snippet) yok

Kurulumda "Kod olmadan otomatik olarak" yöntemi seçildi. Sitede zaten canlı olan
AW etiketi her sayfa görüntülemeyi Google'a bildiriyor; Google `/tesekkurler`
yüklendiğinde dönüşümü kendi tarafında eşliyor. Teşekkür sayfasına form
doldurmadan ulaşmak mümkün değil ve sayfa `noindex`, dolayısıyla kural birebir
"form gönderildi" demek.

> ⚠️ `site/google.js` içindeki `LEAD_ETIKET` alanı **bilerek boş bırakıldı**.
> Oraya bir dönüşüm etiketi yazmak, URL kuralının üstüne ikinci bir sinyal
> ekleyeceği için aynı formu iki kez saydırır. Google Ads arayüzündeki
> `7727865543` numarası "dönüşüm türü kimliği"dir — conversion label değildir ve
> `AW-18401005291/7727865543` şeklinde birleştirilemez.

### Doğrulama

Siteden bir form doldurup `/tesekkurler` sayfasına düşün. Dönüşüm eyleminin
durumu 3–24 saat içinde "Dönüşümler bekleniyor"dan "Etkin"e döner. Kampanya
duraklatılmışken reklam tıklamasından gelen dönüşüm oluşmaz, ama etiketin
sayfayı görmesi durum göstergesini yine de besler.

### İsteğe bağlı: GA4

`analytics.google.com` → yeni mülk → `G-XXXXXXXXXX` kodunu `site/google.js`
içindeki `GA4_ID` alanına yazmak yeterli. Trafik davranışını (hangi bölümde
ne kadar kalınıyor, nerede terk ediliyor) görmek için faydalı; dönüşüm ölçümü
için gerekli değil.

> Not: Google'ın **Enhanced conversions** özelliği için formdaki e-posta/telefonun
> hash'lenip gönderilmesi gerekir. KVKK metnimiz bunu açıkça kapsamıyor; avukat
> onayı gelene kadar **kapalı** bırakıyoruz.

## 3. Kampanya mimarisi

Tek hesap, **üç kampanya**. Karıştırmayın — bütçeleri ve niyet seviyeleri farklı.

### K1 · Arama — Golden Visa niyeti (ana kampanya, bütçenin %60'ı)

- Kampanya türü: **Search**, "Website traffic" hedefi seçmeyin → **"Create a campaign
  without a goal's guidance"**. Hedef güdümlü akış sizi otomatik önerilere hapseder.
- Ağ: **Search Network yalnızca.** "Include Google Display Network" kutusunu **kaldırın**
  (yeni hesaplarda varsayılan açık gelir ve bütçeyi çöp trafiğe yakar).
- Konum: **Türkiye**. Ayrıca "Presence: People in or regularly in your targeted
  locations" seçin — varsayılan "interest" ayarı Türkiye'yi *arayan* yurt dışı
  trafiğini de alır.
- Dil: **Türkçe**.
- Teklif: İlk 3–4 hafta **Maximize clicks** + tıklama başı üst limit **1,20 €**.
  30 dönüşüm biriktikten sonra **Maximize conversions / tCPA**'ya geçin. Baştan tCPA
  koymak veri yokken algoritmayı boşa çalıştırır.
- Günlük bütçe: **20 €** (aylık ~600 €).

**Reklam grupları ve anahtar kelimeler** (tümü *phrase match*, yani `"..."` içinde):

| Reklam grubu | Anahtar kelimeler |
|---|---|
| Golden Visa — genel | "yunanistan golden visa", "yunanistan altın vize", "golden visa yunanistan şartları", "yunanistan oturum izni yatırım" |
| 250.000 € eşiği | "yunanistan golden visa 250 bin euro", "250000 euro golden visa", "yunanistan golden visa fiyat", "en ucuz golden visa" |
| Atina gayrimenkul | "atina daire fiyatları", "yunanistan ev alarak oturum", "atina yatırımlık daire", "yunanistan gayrimenkul yatırımı" |
| Avrupa oturumu — karşılaştırma | "avrupa oturum izni yatırım", "portekiz golden visa alternatifi", "hangi ülke golden visa veriyor" |

**Negatif anahtar kelimeler** (kampanya seviyesinde, ilk günden ekleyin — bunlar
bütçenin en hızlı kaçtığı yerdir):

```
ücretsiz, bedava, iş ilanı, iş bulma, çalışma izni, vize randevusu, schengen randevu,
turistik vize, öğrenci vizesi, kiralık, kiralik ev, iş kurma, şirket kurma,
vatandaşlık satın alma, pasaport satın alma, nasıl kaçak, sığınma, iltica,
dolandırıcılık, şikayet, forum, ekşi, wikipedia, memur, maaş
```

> `vatandaşlık` ve `pasaport` içeren aramaları **negatiflemek** hem bütçe hem uyum
> meselesi: o niyetle gelen kişiye satamayız ve o kelimelerle eşleşmek reklam
> onayını riske atar.

### K2 · Arama — Marka koruma (bütçenin %10'u)

- Anahtar kelimeler: `"michail voda 8"`, `"michailvoda8"`, `"michail voda atina"`
- Günlük bütçe **3 €**. Instagram/LinkedIn'den adı duyup Google'a yazan kişiyi
  rakip reklamına kaptırmamak için. Tıklama maliyeti kuruşlar mertebesinde olur.

### K3 · Yeniden pazarlama — Display (bütçenin %30'u, K1 veri ürettikten sonra)

- **Search kampanyası en az 100 tıklama getirdikten sonra** açın, önce değil.
- Kitle: siteyi ziyaret edip teşekkür sayfasına ulaşmamış kullanıcılar
  (Audience Manager → Website visitors → `michailvoda8.com` ziyaretçileri
  **eksi** `/tesekkurler` ziyaretçileri), 30 günlük pencere.
- Görseller: `mv8-design-paketi` içindeki render'lar. Boyutlar: 300×250, 336×280,
  728×90, 300×600, 320×100 + responsive için 1200×628 ve 1200×1200.
- Günlük bütçe **8 €**, frekans sınırı günde 3 gösterim.

## 4. Reklam metinleri (Responsive Search Ads)

Her reklam grubuna **bir** RSA yeterli. Google 15 başlık + 4 açıklama alır, kendisi
kombinler. Aşağıdakiler uyum diline uygun: "vatandaşlık" ve "garanti" geçmiyor.

**Başlıklar** (max 30 karakter):

```
Yunanistan Golden Visa
250.000 € ile Atina'da Ev
Atina'da 250.000 € Eşiği
AB'de 5 Yıllık Oturum İzni
Michail Voda 8 · Atina
Eşyalı Teslim · Aralık 2026
5 Yıl Kira Garantisi
Aylık 500 € Kira Geliri
Ofisten Konuta Dönüşüm
Aile Bireyleri de Dahil
Ücretsiz Ön Görüşme
Fiyat Listesi ve Kat Planı
12 Daire Müsait
Türkçe Süreç Desteği
Atina Merkezde Yatırım
```

**Açıklamalar** (max 90 karakter):

```
Atina merkezde ofisten konuta dönüşüm projesi. 250.000 € eşiğinden başvuru imkânı.
Eşyalı teslim, 5 yıl boyunca aylık 500 € kira garantisi. Aralık 2026 teslim.
Eş, 21 yaş altı çocuklar ve her iki tarafın ebeveynleri başvuruya dahil edilebilir.
Fiyat listesi ve süreç dosyası için formu bırakın; 24 saat içinde arayalım.
```

**Uzantılar** (Assets — hepsini ekleyin, tıklama oranını ciddi artırır):

- *Sitelinks:* `Golden Visa Nedir? → /#golden-visa` · `Yatırım Özeti → /#yatirim` ·
  `Daireler ve Kat Planları → /#daireler` · `Sık Sorulanlar → /#sss`
- *Callouts:* `Eşyalı teslim` · `5 yıl kira garantisi` · `Atina merkez` · `Türkçe destek`
- *Structured snippet* (Types → Amenities): `29–49 m²` · `Eşyalı` · `Asansörlü` · `Merkezi konum`
- *Call asset:* +90 536 569 68 96 (mesai saatleri 09:00–20:00 olarak ayarlayın)
- *Lead form asset:* **kullanmayın** — siteye trafik çekip pixel/GA verisi biriktirmek
  daha değerli, ayrıca Google'ın form lead'leri düşük kaliteli gelme eğiliminde.

**Final URL:** `https://michailvoda8.com/` — K1'in "250.000 € eşiği" grubunda
`https://michailvoda8.com/basvuru` de test edilebilir; A/B'yi 3. haftada kurarız.

## 5. Uyum — Google'ın kuralları Meta'dan farklı

Google, göçmenlik/vize reklamlarını **"Legal requirements"** başlığı altında
denetler. Reddi tetikleyen kalıplar:

- ❌ "vatandaşlık", "pasaport", "kesin oturum", "garantili vize", "%100 onay"
- ❌ Resmî kurum görünümü veren ifadeler ("Yunanistan Göç Bakanlığı onaylı" vb.)
- ✅ "oturum izni **başvurusu**", "yatırım yoluyla ikamet izni", "başvuru süreci"
- ✅ Site altındaki dipnot her sayfada duruyor:
  *"Başvuru sonucu resmi makamların takdirindedir."*

Reklam reddedilirse: reddin gerekçesi reklam satırının yanında yazar; metni düzeltip
yeniden gönderin. Google'da Meta'nın aksine tek bir red hesabı riske atmaz.

## 6. Bütçe ve beklenen sonuç

| Kalem | Aylık |
|---|---|
| K1 Arama — Golden Visa | 600 € |
| K2 Marka koruma | 90 € |
| K3 Yeniden pazarlama | 240 € |
| **Toplam medya** | **930 €** |
| Vergiler (~%20) | ~186 € |
| **Kart yansıması** | **~1.116 €** |

Türkiye pazarında bu anahtar kelimelerde gerçekçi aralık:

- Tıklama başı maliyet: **0,60 – 1,40 €**
- 930 € → yaklaşık **800–1.100 tıklama**
- Site form dönüşüm oranı %2–4 → **16–40 ham lead**
- Bunun %20–30'u gerçekten 250 k € bütçeye sahip → **4–10 nitelikli görüşme**
- Bu segmentte satışa dönüş %5–10 → **ayda 0,5–1 satış**

12 dairelik stok için bu tempo yeterli: kampanya ~12 ayda stoğu tüketir, Meta
geri açılırsa süre yarıya iner.

## 7. İlk 14 gün — kontrol listesi

- [x] Gün 1: Hesap açıldı (EUR · Europe/Istanbul) + faturalandırma
- [x] Gün 1: Google etiketi `AW-18401005291` sitede yayında
- [x] Gün 1: Dönüşüm eylemi URL kuralıyla kuruldu (kod gerekmedi)
- [ ] Gün 2: Kampanyayı duraklat, Görüntülü Reklam Ağı'nı kapat, konum
      ayarını "Presence" yap, negatif listesini yapıştır
- [ ] Gün 2: RSA başlık/açıklamalarını ve uzantıları tamamla
- [ ] Gün 3: K2 marka kampanyası (10 dakikalık iş)
- [ ] Gün 4–7: **Search terms report**'u her gün açın. Alakasız her sorguyu
      negatife ekleyin — ilk hafta bütçenin %30'u buradan kurtarılır.
- [ ] Gün 7: Tıklama oranı %3'ün altındaki başlıkları değiştirin
- [ ] Gün 10: 100 tıklamayı geçtiyse K3 yeniden pazarlamayı açın
- [ ] Gün 14: Dönüşüm başına maliyeti ölçün; 60 €'nun altındaysa bütçeyi %50 artırın

## 8. Meta geri açılırsa

Google Ads'i kapatmayın. İkisi farklı işi yapar: Google **niyeti hasat eder**,
Meta **niyeti üretir**. Meta açıldığında bütçe dağılımı 60 Meta / 40 Google olur;
Google'ın marka koruma ve yeniden pazarlama kampanyaları Meta trafiğini de
yakaladığı için birlikte daha verimli çalışırlar.
