# Şantiye kareleri

Ham şantiye fotoğrafı ikna etmez — moloz ve iskele gören soğuk kitle
"bitmemiş, riskli" diye okur. Aynı fotoğraf tarihlenip markalanınca
**ilerleme kanıtına** dönüşür. Bizim leadlerimizin gerçek itirazı
"güzel mi" değil, "gerçek mi, teslim edilecek mi".

## Nerede kullanılır

| Yer | Neden |
|---|---|
| **WhatsApp takibi** | Susan leade "düşündünüz mü" yazmak zayıf; tarihli fotoğraf konuşmayı yeniden açar. En yüksek değerli kullanım. |
| **Sitede Güvence bölümü** | Astons'un güven vurgusuna verilecek en ucuz cevap. |
| **Instagram organik** | Reklamı görüp profile bakan kişi canlı bir hesap görmeli. |

**Reklamda kullanılmaz.** Soğuk kitlede şantiye görüntüsü teslim tarihini
daha da uzak hissettirir. Reklam kreatifleri `marka/reklam/` altında kalır.

## Üretim

```bash
python3 marka/santiye/santiye-kare.py FOTOGRAF \
  --tarih "26 Ağustos 2026" \
  --baslik "Dairelerde pencereler takıldı" \
  --vurgu "Sıra iç imalatta" \
  --ad daire-pencere --cikti marka/santiye
```

4:5 (akış) ve 9:16 (story/reels) olmak üzere iki dosya üretir.
Marka dili reklam kreatifleriyle aynı: tam kanvas fotoğraf, alttan koyu
degrade, üstte marka + tarih rozeti, altta serif başlık ve italik vurgu.

### `--kirp`

`sol,ust,sag,alt` oranlarıyla kadrajdan alan çıkarır.
**Yüz görünen karelerde zorunlu:** marka bilinçli olarak yüzsüz, ayrıca
çalışanın görüntüsü onun rızasına tabidir. `ornek-isci` `--kirp "0,0.47,1,1"`
ile üretildi; el ve mala kaldı, yüz çıktı.

## Fotoğraf seçimi

| İşe yarar | Yaramaz |
|---|---|
| İç mekân, yeni pencereler, korumalı zemin — "bitmiş eve giden iş" | Arka aydınlık, grafiti, moloz yığını — zarar veren tür |
| El/alet detayı (yüzsüz) — gerçek emek | Mavi filenin kadrajı yuttuğu geniş planlar (tek karelik istisna dışında) |

## Eksik olan, istenmesi gereken

- Bitmiş ya da bitmek üzere bir daire
- Giriş / lobi
- Fileler indikten sonra sokak cephesi
- **Her ay aynı açıdan çekim** — zaman içinde ilerleme en ikna edici kanıt

## Örnekler

`ornek-daire`, `ornek-isci`, `ornek-cephe` — 26 Ağustos 2026 fotoğraflarından.
