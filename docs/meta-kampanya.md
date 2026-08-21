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

## Yayındaki kampanya

| Katman | ID | Ayar |
|---|---|---|
| Kampanya | 120253029646810721 | `MV8 \| Lead \| Eşik \| TR` · OUTCOME_LEADS · özel kategori beyan edilmedi |
| Reklam seti | 120253029682550721 | `TR \| 33-65 \| Yatırım-Gayrimenkul` · **günlük TL 800** |
| Reklam · GV-Esik-v2 | 120253030488610721 | kreatif 1610829687225588 |
| Reklam · GV-Aile-v3 | 120253030620170721 | kreatif 1079343091275876 |
| Reklam · GV-Sure-v3 | 120253030621160721 | kreatif 1370897995256181 |

**Yalnızca Instagram.** `publisher_platforms: ["instagram"]`,
yerleşimler: `stream`, `story`, `reels`, `explore_home`, `profile_feed`.
Facebook yerleşimi kapalı.

Dönüşüm konumu web sitesi, optimizasyon `OFFSITE_CONVERSIONS` → piksel
`Lead` olayı, faturalama gösterim başına, teklif `LOWEST_COST_WITHOUT_CAP`.
Hedefleme: Türkiye (yalnızca burada yaşayanlar), 33–65, Türkçe (locale 19),
ilgi alanları — Gayrimenkul yatırımı `6003446239080`, Varlık yönetimi
`6003484864669`, Yatırım bankacılığı `6003063638807`, Investment company
`6003392721577`. Advantage+ kitle genişletme kapalı, kreatif iyileştirmeleri kapalı.

Kreatifler `asset_feed_spec` + `asset_customization_rules` kullanıyor:
akış/keşfet/profil → 4:5, story/reels → 9:16. Görseller
`marka/reklam/golden-visa/` altında.

Bağlantılar UTM etiketli (`utm_source=instagram`, `utm_campaign=mv8-goldenvisa`,
`utm_content=esik|aile|sure`); `site/pixel.js` bunları forma gizli alan olarak
eklediği için her talepte hangi reklamdan geldiği görünüyor.

### Mesaj yaklaşımı

Reklamlar daireyi değil **oturum iznini** öne çıkarıyor: 250.000 € eşiği,
ailenin başvuruya dahil edilmesi, iznin süresi ve Schengen seyahati. Proje
ikinci planda, kanıt olarak anlatılıyor. Yasak kelimeler ("vatandaşlık",
"pasaport", "garanti", "kesin onay") hiçbir metinde geçmiyor; her metin
"Başvuru sonucu resmi makamların takdirindedir." ile bitiyor.

Daire odaklı ilk üç reklam (Esik-1, Kira-1, Proje-1) ve bölünmüş-panel görsele sahip ilk GV seti yayınlanmadan silindi.

Görsel dili v2 ile değişti: tam kanvas fotoğraf, alttan koyu degrade, üstte marka + "TESLİM · ARALIK 2026" rozeti, fotoğraf üzerinde büyük serif başlık + italik vurgu satırı (Instagram'daki organik gönderiyle aynı dil). Başlıklar konuyu bilmeyen birine kendini anlatacak şekilde kuruldu: her başlıkta Atina/Yunanistan + 250.000 € + oturum izni birlikte geçiyor; izin daima "başvuru" olarak ifade ediliyor, alıcıya verilen bir şey olarak değil.

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
