# MV8 — Hesap ve Altyapı Kurulum Rehberi

Başlangıç noktası: elde yalnızca şahsi bir Facebook hesabı var. Aşağıdaki sıra önemli;
her adım bir sonrakinin ön şartı. Tamamı ilk hafta içinde bitirilebilir.

## 0. Başlamadan hazırda olması gerekenler

| Gereksinim | Not |
|---|---|
| Şahsi Facebook hesabı | ✅ Var — Business Portfolio bununla açılacak. **Hemen 2FA açın**; bu hesap kapanırsa her şey gider |
| Kredi kartı (şirket kartı tercihen) | Domain, e-posta ve reklam ödemeleri |
| Şirket evrakları | Ticaret sicil/faaliyet belgesi, vergi levhası, şirket adına adres+telefon — Meta işletme doğrulaması ve WhatsApp API için |
| Ayrı telefon hattı (yeni numara/eSIM) | Instagram + WhatsApp Business için; şahsi numara kullanmayın |
| **Karar:** faturalama hangi şirketten? | Reklam hesabının ülke/para birimi **sonradan değiştirilemez**. Yunan şirketi → Yunanistan + EUR; Türk şirketi → Türkiye + TRY (+KDV). Yunan şirketi genelde daha temiz |

## 1. Domain — Cloudflare Registrar (≈10 $/yıl/domain)

- `michailvoda8.com`, `mv8athens.com`, `michailvoda8athens.com` üçü de şu an **boşta** (RDAP kontrolü, 18.08.2026).
- **Nereden:** [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/) — maliyetine satar, DNS + ileride site barındırma (Pages) aynı panelde. Alternatif: Namecheap.
- **Ne yapılacak:** Cloudflare hesabı aç → üç domaini de al (yıllık toplam ~30 $; ana marka `michailvoda8.com`, diğerleri yönlendirme) → WHOIS gizliliği otomatik açık.

## 2. Kurumsal e-posta — Google Workspace (≈7 €/kullanıcı/ay)

- **Nereden:** [workspace.google.com](https://workspace.google.com) → Business Starter.
- **Ne yapılacak:** `info@michailvoda8.com` ile başlayın (ilerde `satis@`, `destek@` takma ad olarak ücretsiz eklenir). Kurulum sihirbazı domain doğrulaması için TXT/MX kayıtlarını verir → Cloudflare DNS'e yapıştırın (5 dk).
- Bundan sonraki **tüm** hesaplar (Meta, Instagram, CRM…) bu kurumsal adresle açılır — şahsi Gmail kullanmayın.

## 3. Facebook Sayfası (ücretsiz, 10 dk)

- Şahsi hesabınızla [facebook.com/pages/create](https://www.facebook.com/pages/create) → Ad: **Michail Voda 8, Athens** · Kategori: *Real Estate Developer / Gayrimenkul*.
- Şahsi profiliniz yalnızca "yönetici" olur; reklamlarda ve sayfada görünmez.
- Profil/kapak görseli: bina renderı; hakkında kısmına TR+EN kısa metin + site linki.
- **İkinci bir yönetici ekleyin** (ortak/çalışan) — tek kişiye bağlı kalmasın.

## 4. Instagram hesabı (ücretsiz, 15 dk)

- Uygulamadan yeni hesap: **@michailvoda8** (doluysa @mv8athens). Kayıtta kurumsal e-posta + yeni telefon hattı.
- Ayarlar → Hesap türü → **Profesyonel (İşletme)** yap → **Facebook sayfasına bağla** (reklam ve DM otomasyonunun ön şartı).
- Profil adı alanı: "Michail Voda 8 | Atina Golden Visa" · bio pazarlama planındaki metin · 2FA açık.

## 5. Meta Business Manager / Business Portfolio (ücretsiz, 1–2 gün doğrulama)

- **Nereden:** [business.facebook.com](https://business.facebook.com) → şahsi FB hesabıyla giriş → "Create a business portfolio". İşletme adı + kurumsal e-posta.
- İçine sırasıyla ekleyin:
  1. **Sayfa** (3. adımdaki) ve **Instagram hesabı** (4. adımdaki),
  2. **Yeni reklam hesabı** — ülke/para birimi kararına göre (EUR önerilir; sonradan değişmez), ödeme yöntemi olarak şirket kartı,
  3. **Domain doğrulaması:** Brand Safety → Domains → `michailvoda8.com` → DNS TXT kaydını Cloudflare'e ekleyin,
  4. **Pixel/Dataset:** Events Manager → yeni veri kaynağı → Pixel kodu siteye (site yayına girerken CAPI de eklenecek),
  5. **İşletme doğrulaması (Business Verification):** Security Center → şirket evrakları + şirket telefonu. WhatsApp API'nin ön şartı; reklam limitlerini de rahatlatır.
- Güvenlik: Portfolio'ya ikinci admin, herkese 2FA zorunluluğu (ayarlardan açılabilir).

## 6. WhatsApp — iki aşamalı

**Aşama 1 (bugün): WhatsApp Business uygulaması (ücretsiz).**
Ayrı hatla kurun (+30 Yunan veya +90 Türk numarası; hedef kitle TR olduğu için +90 güven verir, Atina ofisi vurgusu için +30 ikinci hat olabilir). İşletme profili (ad, adres, site), katalog (daireler), hızlı yanıtlar, etiketler. Bio ve reklam butonları için bu yeterli.

**Aşama 2 (hafta 5+, otomasyon/çoklu temsilci gerekince): WhatsApp Business Platform (Cloud API).**
- Ön şartlar: doğrulanmış Business Portfolio (adım 5) + **uygulamada kullanılmayan** bir numara (bir numara ya uygulamada ya API'de olur; taşırsanız uygulamadan çıkar — bu yüzden API'ye ayrı numara ayırın).
- **Nereden:** doğrudan Meta ([business.whatsapp.com](https://business.whatsapp.com) → Cloud API, aracısız) veya bir BSP/arayüz: 360dialog, respond.io, Twilio; ManyChat DM otomasyonu da aynı API'ye bağlanır. Ücretlendirme konuşma başına; müşteri size yazdığında açılan servis konuşmaları ücretsiz, sizin başlattığınız şablon mesajlar ücretli.

## 7. Bitiş kontrol listesi

- [ ] 3 domain Cloudflare'de, michailvoda8.com ana marka
- [ ] info@michailvoda8.com çalışıyor, MX/TXT doğrulandı
- [ ] FB sayfası + @michailvoda8 (işletme) bağlı, 2FA açık
- [ ] Business Portfolio: sayfa + IG + reklam hesabı + ödeme yöntemi + domain doğrulama + Pixel
- [ ] İşletme doğrulaması başvurusu gönderildi
- [ ] WhatsApp Business uygulaması ayrı hatta kurulu, katalog dolu
- [ ] Tüm hesaplarda 2FA + en az 2 yönetici + şifre yöneticisi (1Password/Bitwarden)

**Yaklaşık maliyet:** kurulum ~30 $/yıl (domainler) + 7 €/ay (e-posta) + telefon hattı; Meta/IG/WhatsApp uygulaması ücretsiz. Reklam bütçesi hariç.
