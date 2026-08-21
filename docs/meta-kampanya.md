# Meta reklam yapısı — kimlikler ve yönetim

Meta reklamları bu oturumdan Graph API ile yönetiliyor. Panele girmeden
kampanya kurulabiliyor, bütçe değiştirilebiliyor, rapor alınabiliyor.

## Erişim

| | |
|---|---|
| System user | `MV8-Claude` (ID 122101408239446761) |
| Token | ortam değişkeni `MV8_META_ACCESS_TOKEN` — süresiz |
| Hesap ID | ortam değişkeni `MV8_META_AD_ACCOUNT_ID` = `act_1062491723404445` |
| İzin kuralı | `.claude/settings.json` → yalnızca `graph.facebook.com` |

> ⚠️ Aynı ortamda Bow Collect'e ait `META_ACCESS_TOKEN` / `META_AD_ACCOUNT_ID`
> değişkenleri de var. **Komutlarda yalnızca `MV8_` önekli değişkenler kullanılır.**
> Her yazma işleminden önce hedef hesabın `1062491723404445` olduğu doğrulanır.

## Varlıklar

| Varlık | ID |
|---|---|
| Business portfolio | 1435580968467788 (michailvoda8goldenvisa) |
| Reklam hesabı | 1062491723404445 · MV8-AdAcc · **TRY** · Europe/Istanbul |
| Ödeme | Mastercard *0915 · sonradan ödeme · harcama limiti yok |
| Facebook sayfası | 1346122758575388 · "Michail Voda 8 Atina" · kategori Emlak |
| Instagram | 17841432238241265 · @michailvoda8 |
| Piksel | 1564731061789182 · MV8 Web Pixel |
| Minimum günlük bütçe | TL 47,88 (hesap tarafından dayatılan taban) |

## İlk kampanya

| Katman | ID | Ayar |
|---|---|---|
| Kampanya | 120253029646810721 | `MV8 \| Lead \| Eşik \| TR` · OUTCOME_LEADS · özel kategori beyan edilmedi |
| Reklam seti | 120253029682550721 | `TR \| 33-65 \| Yatırım-Gayrimenkul` · günlük TL 800 |
| Reklam · Esik-1 | 120253029835820721 | kreatif 1620816276360661 |
| Reklam · Kira-1 | 120253029836600721 | kreatif 1049320634579458 |
| Reklam · Proje-1 | 120253029836870721 | kreatif 2518671931982727 |

Reklam seti ayarları: dönüşüm konumu **web sitesi**, optimizasyon
`OFFSITE_CONVERSIONS` → piksel `Lead` olayı, faturalama gösterim başına,
teklif `LOWEST_COST_WITHOUT_CAP`. Hedefleme: Türkiye (yalnızca burada
yaşayanlar), 33–65, Türkçe (locale 19), ilgi alanları — Gayrimenkul
yatırımı `6003446239080`, Varlık yönetimi `6003484864669`, Yatırım
bankacılığı `6003063638807`, Investment company `6003392721577`.
Advantage+ kitle genişletme **kapalı** (`advantage_audience: 0`).
Kreatiflerde metin ve görsel iyileştirmeleri **kapalı**.

Bağlantılar UTM ile etiketli (`utm_source=facebook`, `utm_content=esik-1`
vb.); `site/pixel.js` bu parametreleri yakalayıp forma gizli alan olarak
eklediği için her talepte hangi reklamdan geldiği görünüyor.

## API notları (tekrar takılmamak için)

- Kampanya oluştururken `is_adset_budget_sharing_enabled` **zorunlu**.
- Reklam setinde `bid_strategy` açıkça verilmeli, yoksa "teklif tutarı
  gerekiyor" hatası döner.
- Kreatiflerde `standard_enhancements` alanı **kaldırıldı**; özellikler
  tek tek kapatılıyor (`text_optimizations`, `image_touchups`,
  `image_brightness_and_contrast`).
- Uygulama **Live** modda olmalı; geliştirme modunda kreatif oluşturulamıyor.
- Token'da `instagram_basic` izni yok — sayfanın Instagram alanı okunamıyor.
  Bağlantının varlığı kreatifteki `instagram_user_id` alanından doğrulanır.

## Çalışma kuralları

- Yeni kampanya **daima duraklatılmış** oluşturulur, önizleme gösterilir,
  yayına alma kararı kullanıcıya aittir.
- Günlük bütçe **sorulmadan artırılmaz**; düşürmek serbest.
- Hesap ayarlarına (ödeme, işletme bilgisi, doğrulama) dokunulmaz.
- Yapılan her değişiklik kullanıcıya yazılır.
