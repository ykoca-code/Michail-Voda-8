# Meta anlık form (instant form) geçişi

Reklamlar siteye yönlendirmek yerine Meta'nın içinde açılan anlık forma
geçiriliyor. Bu klasördeki JSON dosyaları oluşturulacak formun içeriğidir.

## Neden

Site formuna 103 ziyaretçide 0 gönderim geldi; dönüşen herkes WhatsApp'a
yöneldi. Anlık form mobilde sürtünmeyi kaldırır: ad, telefon ve e-posta
Meta profilinden ön-doldurulur, kullanıcı siteye hiç gitmez.

## Bedeli — bilerek kabul ediliyor

| Kaybedilen | Sonuç |
|---|---|
| Site ziyareti | Ziyaretçi projeyi sitede incelemez; ikna tamamen reklam metnine ve forma kalır |
| Formspree e-postası | Lead'ler Meta'nın içinde birikir, e-posta düşmez |
| `Lead` pixel olayı | Site tarafı ölçüm devre dışı; dönüşüm Meta'nın kendi kaydından okunur |
| UTM kaynak takibi | `site/pixel.js` ile forma yazılan kaynak alanları dolmaz |

Buna karşılık dönüşüm oranının belirgin artması beklenir; mobilde anlık
form tipik olarak site formunun birkaç katı doldurulur.

## Lead'lere nasıl ulaşılacak

Üç yol var, ilk ikisi kurulmalı:

1. **Sayfa bildirimleri** — yeni lead geldiğinde Meta bildirim/e-posta
   gönderir. Sayfa ayarlarından açılır.
2. **API ile çekme** — `leads_retrieval` izniyle lead'ler bu oturumdan
   okunabilir; günlük rapora eklenir. Asıl çözüm budur.
3. Leads Center'dan elle CSV indirme — yedek yöntem.

Lead'e **2 saat içinde** dönülmezse anlık formun avantajı kaybolur;
düşük sürtünmeyle gelen kişi aynı hızla soğur.

## Form içeriği

| Dosya | İçerik |
|---|---|
| `lf-sorular.json` | Ad soyad, telefon, e-posta (ön-doldurulur) + iki niteleme sorusu: kaç kişi, ne zaman |
| `lf-context.json` | Form açılışındaki tanıtım kartı — dört madde |
| `lf-ty.json` | Teşekkür ekranı; düğme rehber PDF'ine gider |
| `lf-privacy.json` | KVKK aydınlatma metni bağlantısı |

İki niteleme sorusu bilinçli: sürtünmeyi bir miktar artırır ama 250.000 €
ürününde niteliksiz lead'i elemek daha değerlidir. Sorular site formundaki
alanlarla birebir aynı, böylece iki kanaldan gelen kayıtlar karşılaştırılabilir.

## Kurulum (izin geldikten sonra)

```bash
PT=<sayfa token>
curl -s -X POST "https://graph.facebook.com/v21.0/1346122758575388/leadgen_forms" \
  -d "name=MV8 Yatirimci Rehberi" -d "locale=tr_TR" \
  -d "block_display_for_non_targeted_viewer=true" \
  --data-urlencode "questions@lf-sorular.json" \
  --data-urlencode "context_card@lf-context.json" \
  --data-urlencode "thank_you_page@lf-ty.json" \
  --data-urlencode "privacy_policy@lf-privacy.json" \
  --data-urlencode "access_token=$PT"
```

Ardından reklam seti `destination_type=ON_AD`,
`optimization_goal=LEAD_GENERATION`, `promoted_object={"page_id":...}`
olarak güncellenir; kreatiflerin eylem düğmesi
`{"type":"SIGN_UP","value":{"lead_gen_form_id":...}}` ile forma bağlanır.

## Durum — 24 Ağustos 2026

İki kampanya paralel yürüyecek, aynı kreatiflerle, farklı hedefle:

| Kampanya | ID | Hedef | Günlük bütçe | Durum |
|---|---|---|---|---|
| `MV8 \| Lead \| Eşik \| TR` | 120253029646810721 | Web sitesi | TL 1.040 | ACTIVE |
| `MV8 \| Lead \| Anlık Form \| TR` | 120253082188570721 | Anlık form | TL 1.040 | PAUSED — kurulum yarım |

Kampanya kabuğu oluşturuldu; reklam seti ve kreatifler aşağıdaki iki
engel kalkmadan kurulamıyor.

## Engeller — ikisi de kullanıcı tarafında

**1. Lead Ads Şartları kabul edilmemiş.** Reklam seti oluşturulurken
Meta şunu döndürüyor:

> Facebook Sayfanız Facebook'un Potansiyel Müşteri Bulma Hizmet
> Koşulları'nı kabul edene dek potansiyel müşteri reklamları
> yayınlayamazsınız.

Kabul yeri: Sayfa → Yayınlama araçları → Anlık Formlar (ya da Ads
Manager'da potansiyel müşteri reklamı kurarken çıkan bağlantı).
Bir kez kabul edilir.

**2. Token izinleri eksik.** Anlık form oluşturmak `pages_manage_ads`
istiyor; mevcut token'da yok.

## Gereken izinler

Mevcut system user token'ında yok:

- `pages_manage_ads` — anlık form oluşturmak için **zorunlu**
- `leads_retrieval` — lead'leri API'den çekmek için (raporlama)
- `pages_show_list` — sayfa listesine erişim

Ayrıca Ads Manager'da **Lead Ads Şartları** bir kez kabul edilmeli.
