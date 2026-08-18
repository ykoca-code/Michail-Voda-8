# Meta Pixel Kurulumu — MV8

Site tarafı hazır: `site/pixel.js` içindeki `MV8_PIXEL_ID` doldurulduğu anda izleme
başlar. Boş kaldığı sürece hiçbir izleme kodu yüklenmez (ziyaretçi verisi toplanmaz).

## 1. Ön koşul: Business Portfolio ve reklam hesabı

Pixel bir Meta Business Portfolio içinde oluşturulur. Sırasıyla:

1. [business.facebook.com](https://business.facebook.com) → şahsi Facebook hesabınızla giriş
2. **Create a business portfolio** → işletme adı: "Michail Voda 8", kurumsal e-posta: info@michailvoda8.com
3. Portfolio içine ekleyin:
   - **Sayfa:** Facebook sayfası (yoksa bu adımda oluşturun)
   - **Instagram:** @michailvoda8goldenvisa hesabını bağlayın
   - **Reklam hesabı:** yeni hesap · ülke/para birimi **sonradan değişmez** (şahsi kartla Türkiye + TRY en pratiği, %20 KDV bütçeye eklenir)

## 2. Pixel oluşturma (5 dk)

1. Business Manager → **All tools → Events Manager** (Etkinlik Yöneticisi)
2. **Connect data sources → Web → Connect**
3. Ad: `MV8 Web Pixel` · URL: `https://michailvoda8.com`
4. Kurulum yöntemi sorulduğunda **"Install code manually"** seçin (kod bizde hazır, Meta'nın verdiği snippet'i kopyalamanıza gerek yok)
5. Ekranda görünen **Pixel Kimliği**'ni (15–16 haneli sayı) not alın → bana iletin

## 3. Domain doğrulama (aynı ekranda, atlanmamalı)

Business Manager → **Brand Safety → Domains** → `michailvoda8.com` ekleyin →
**DNS TXT** yöntemini seçin → verilen TXT kaydını Cloudflare DNS'e ekleyin (Type: TXT,
Name: `@`, Content: Meta'nın verdiği değer) → **Verify**.

Doğrulama olmadan iOS kullanıcılarında dönüşüm ölçümü ciddi şekilde eksik kalır.

## 4. Toplanan olaylar

| Olay | Nerede tetiklenir | Kullanımı |
|---|---|---|
| `PageView` | Tüm sayfalar | Trafik, retargeting kitlesi |
| `FormAcildi` (özel) | Formu açan / başvuru sayfasına gelen | Niyet sinyali; "formu açıp bırakanlar" retargeting kitlesi |
| `FilmIzlendi` (özel) | Tanıtım filminin yarısını izleyenler | İlgili kitle; sıcak retargeting |
| **`Lead`** (standart) | Form gönderildikten sonra teşekkür sayfası | **Ana dönüşüm** — kampanya optimizasyonu buna göre yapılır |

`Lead` olayı bilerek teşekkür sayfasında tetikleniyor: form gönderimi başarısız olursa
sayılmaz, yani veri gerçek başvuruları yansıtır.

## 5. Pixel ID geldikten sonra (bende)

1. `site/pixel.js` içindeki `MV8_PIXEL_ID` doldurulur, yayına alınır
2. Test: Chrome'a **Meta Pixel Helper** eklentisini kurup siteyi açın — PageView görünmeli;
   formu doldurup teşekkür sayfasına düşün, `Lead` olayı düşmeli
3. Events Manager → **Test Events** sekmesinden de canlı doğrulama yapılabilir

## 6. Sonraki adım: Toplu Etkinlik Ölçümü (iOS)

Events Manager → **Aggregated Event Measurement** → michailvoda8.com için olay
önceliklendirme: **1) Lead, 2) FormAcildi, 3) FilmIzlendi, 4) PageView**.
Reklamlar başlamadan önce yapılmalı.

## 7. İleri seviye (şimdilik gerekmez)

**Conversions API (CAPI):** tarayıcı engelleyicilerin kaçırdığı dönüşümleri sunucu
tarafından gönderir; ölçüm doğruluğunu %10–30 artırabilir. Statik sitede doğrudan
mümkün değil, ancak sitemiz Cloudflare Worker üzerinde çalıştığı için ileride
Worker'a küçük bir uç nokta eklenerek kurulabilir. Reklam bütçesi 5.000 €/ay'ı
aştığında değerlendirilmeli.
