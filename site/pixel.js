/* Michail Voda 8 — olay takibi yardımcısı
   ------------------------------------------------------------------
   Meta Pixel'in kendisi her sayfanın <head> bölümüne satır içi (inline)
   gömülüdür; bu dosya yalnızca sayfalardan çağrılan mv8Track()
   yardımcısını tanımlar. Pixel kimliğini değiştirmek gerekirse dört
   HTML dosyasındaki fbq('init', ...) satırı güncellenir.          */

(function () {
  var STANDART = ['Lead','Contact','ViewContent','CompleteRegistration','Search','SubmitApplication'];
  window.mv8Track = function (olay, veri) {
    if (typeof window.fbq !== 'function') return;
    if (STANDART.indexOf(olay) > -1) window.fbq('track', olay, veri || {});
    else window.fbq('trackCustom', olay, veri || {});
  };
})();

/* Trafik kaynağı takibi
   ------------------------------------------------------------------
   Ziyaretçi reklamdan geldiyse URL'deki gclid / fbclid / utm_*
   parametreleri ilk sayfada yakalanır, oturum boyunca saklanır ve
   form gönderilirken gizli alan olarak eklenir. Böylece e-postaya
   düşen her talepte "bu kişi hangi reklamdan, hangi kelimeden geldi"
   bilgisi yer alır.                                                */

(function () {
  var ALANLAR = ['gclid', 'fbclid', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
  var ANAHTAR = 'mv8_kaynak';

  function oku() {
    try { return JSON.parse(sessionStorage.getItem(ANAHTAR)) || {}; }
    catch (e) { return {}; }
  }

  function yakala() {
    var kayit = oku();
    var yeni = false;
    try {
      var p = new URLSearchParams(location.search);
      ALANLAR.forEach(function (a) {
        var d = p.get(a);
        if (d && !kayit[a]) { kayit[a] = d.slice(0, 200); yeni = true; }
      });
    } catch (e) { return kayit; }

    if (!kayit.ilk_sayfa) { kayit.ilk_sayfa = location.pathname; yeni = true; }
    if (!kayit.yonlendiren && document.referrer && document.referrer.indexOf(location.hostname) === -1) {
      kayit.yonlendiren = document.referrer.slice(0, 200); yeni = true;
    }
    if (yeni) { try { sessionStorage.setItem(ANAHTAR, JSON.stringify(kayit)); } catch (e) {} }
    return kayit;
  }

  function formlaraEkle() {
    var kayit = yakala();
    var anahtarlar = Object.keys(kayit);
    if (!anahtarlar.length) return;
    document.querySelectorAll('form.lead-form').forEach(function (f) {
      anahtarlar.forEach(function (a) {
        if (f.querySelector('input[name="' + a + '"]')) return;
        var i = document.createElement('input');
        i.type = 'hidden'; i.name = a; i.value = kayit[a];
        f.appendChild(i);
      });
    });
  }

  yakala();
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', formlaraEkle);
  } else {
    formlaraEkle();
  }
  /* Popup formu sonradan açıldığında da alanlar dolu olsun */
  window.mv8KaynakEkle = formlaraEkle;
})();
