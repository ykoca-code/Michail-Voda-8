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

## 5a. Seçilen basit başlangıç: reklam hesabı kişi adına, reklamlar MV8 sayfasından

Reklamın halka görünen yüzü **sayfadır**; reklam hesabının sahibi dışarıdan görünmez.
Bu yüzden şu kurgu tamamen geçerli ve en hızlı başlangıçtır:

1. Business Portfolio'yu şahsi Facebook hesabıyla açın (işletme adı alanına
   "Michail Voda 8" yazılabilir; **işletme doğrulaması zorunlu değil**, evrak istenmez).
2. İçine MV8 sayfası + Instagram + yeni reklam hesabı; ödeme şahsi kredi kartı.
   Para birimi kuralı yine geçerli: **sonradan değişmez** (şahsi TR kartıyla Türkiye +
   TRY + %20 KDV en pratiği; %20'lik KDV maliyetini bütçeye ekleyin).
3. Reklamlar MV8 sayfası + @michailvoda8 kimliğiyle yayınlanır. İzleyici için hiçbir
   fark yok.

**Bilinmesi gereken 4 sınır:**
- **Fatura şahsa kesilir** → şirket gideri olarak gösterilemez. Vergisel olarak
  önemliyse muhasebeciye danışın; değilse sorun değil.
- **Yeni + doğrulamasız hesapların günlük harcama limiti başta düşüktür** ve otomatik
  sistemler yeni hesaplara karşı hassastır. İlk hafta düşük bütçeyle (50–100 €/gün)
  ısındırın, bilgileri (sayfa, site, domain doğrulaması) tutarlı tutun — domain
  doğrulaması ve Pixel kurulumu doğrulamasız da yapılabilir ve yapılmalı.
- **WhatsApp Business uygulaması** için de doğrulama gerekmez; yalnızca **WhatsApp API**
  (hafta 5+) işletme doğrulaması ister. O gün geldiğinde aynı portfolio'ya şirket
  evrakı yüklenir — sıfırdan kurulum gerekmez.
- İleride şirket faturası istenirse: aynı portfolio içinde şirkete bağlı **yeni bir
  reklam hesabı** açılır; sayfa, Instagram, takipçi ve Pixel verisi aynen kalır
  (asıl değer biriken bunlardır), sadece reklam hesabı değişir. Yani bu başlangıç
  geri döndürülebilir, riski düşük bir yoldur.

## 5b. Sitesiz çalışma opsiyonu

Web sitesi olmadan da huni kurulabilir; Meta bunun için iki reklam ürünü sunar:

1. **Instant Form (Potansiyel Müşteri reklamları):** form Facebook/Instagram'ın içinde
   açılır, site gerekmez. Ön eleme soruları sorulabilir; lead'ler CRM'e veya e-tabloya düşer.
2. **Click-to-WhatsApp reklamları:** reklama tıklayan doğrudan WhatsApp sohbetine gelir.
   Bilgi paketi PDF'i sohbetten gönderilir.

Instagram profili vitrin görevi görür; bio linki `wa.me/...` olur. Bu kurguda domain +
kurumsal e-posta yine alınmalıdır (ucuz, ve Meta hesap güvenilirliği için önemli).

**Sitesiz kaybedilenler:**
- **Google Search reklamları fiilen devre dışı** — "yunanistan golden visa" gibi en
  yüksek niyetli aramalar rakiplere kalır (bu kelimede arayan kişi zaten alıcıdır).
- **Pixel + site retargeting yok** (IG etkileşimi ve form açanlar üzerinden retargeting
  yine mümkün ama daha zayıf).
- **Güven sinyali eksilir:** ~270.000 €'luk kararda müşterinin Google'da sizi arayıp
  hiçbir şey bulamaması ciddi bir itiraz konusudur; dolandırıcılık algısı riski artar.
- **Meta işletme doğrulaması zorlaşır** (Meta, işletme bilgilerini web üzerinden çapraz
  kontrol eder) → WhatsApp API yolu da dolaylı olarak zorlaşır.

**Sonuç:** Sitesiz *başlanabilir*; ama site zaten hazır kodlanmış durumda (`site/`),
yayına alma maliyeti ~10 $/yıl domain + 15 dk Cloudflare Pages kurulumudur. Önerilen:
reklamlara Instant Form + Click-to-WhatsApp ile başla (site bloker değil), hazır siteyi
de aynı hafta yayına al — reklam metinlerinde link zorunlu değil, site yalnızca güven
ve Google araması için arkada dursun.

## 6a. Netleştirme — telefon numarası ve işletme doğrulaması, en basit yol

**Telefon: aslında 3 ayrı ihtiyaç var, tek numara sanılıyor.**

| İhtiyaç | En basit çözüm |
|---|---|
| Instagram/Facebook 2FA | Numara **gerekmez** — authenticator uygulaması (Google Authenticator/1Password) hem daha basit hem daha güvenli |
| WhatsApp Business uygulaması | Mevcut telefonunuza **1 ek eSIM/faturasız hat** (+90). Aktivasyonda bir kez SMS alması yeterli, sonrası internetten çalışır. Şahsi WhatsApp ile aynı telefonda yan yana durur (ayrı uygulama) |
| WhatsApp API (hafta 5+) | Uygulamadakinden **ayrı** ikinci bir numara — şimdi gerekmiyor, sırası gelince alınır |

İşletme doğrulama formundaki "işletme telefonu" için de telefon şart değil: onay adımını **alan adı e-postasıyla** (info@michailvoda8.com) geçebilirsiniz.

**İşletme doğrulaması: acele etmeyin, reklam için gerekmiyor.**

- Reklamlar doğrulamasız yayınlanır. Doğrulama yalnızca **WhatsApp API** (ve birkaç ileri özellik) için şart → hafta 4–5'te, API'den hemen önce yapın. Şimdilik sadece evrakları hazırlayın.
- **Hangi şirket:** reklam hesabını açtığınız tüzel kişilikle aynısı — binanın sahibi Yunan şirketi en temiz seçenek.
- **Evrak (2 belge):** (1) resmi kuruluş/vergi kaydı (yasal ad birebir aynı olmalı), (2) yasal ad + adresi birlikte gösteren belge (şirket banka ekstresi veya faturası). Şahsi belge/pasaport **kabul edilmez** — belgeler şirket adına olmalı.
- **Süreç:** Business Suite → Security Center → "Start verification" → bilgileri evraktaki yazımla birebir girin → belgeleri yükleyin → onay yöntemi olarak **e-posta (kendi domaininiz)** seçin → sonuç 1–14 iş günü.
- **Red yememenin sırrı tutarlılık:** web sitesi canlı olmalı ve şirketin yasal adı sitede (footer/iletişim sayfası) görünmeli; başvurudaki e-posta aynı domainde olmalı; adres evrakla aynı olmalı. Yani doğru sıra: önce site + kurumsal e-posta, sonra doğrulama başvurusu.

## 7. Bitiş kontrol listesi

- [ ] 3 domain Cloudflare'de, michailvoda8.com ana marka
- [ ] info@michailvoda8.com çalışıyor, MX/TXT doğrulandı
- [ ] FB sayfası + @michailvoda8 (işletme) bağlı, 2FA açık
- [ ] Business Portfolio: sayfa + IG + reklam hesabı + ödeme yöntemi + domain doğrulama + Pixel
- [ ] İşletme doğrulaması başvurusu gönderildi
- [ ] WhatsApp Business uygulaması ayrı hatta kurulu, katalog dolu
- [ ] Tüm hesaplarda 2FA + en az 2 yönetici + şifre yöneticisi (1Password/Bitwarden)

**Yaklaşık maliyet:** kurulum ~30 $/yıl (domainler) + 7 €/ay (e-posta) + telefon hattı; Meta/IG/WhatsApp uygulaması ücretsiz. Reklam bütçesi hariç.
