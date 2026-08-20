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
