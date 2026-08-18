/* Michail Voda 8 — Meta Pixel ve olay takibi
   ------------------------------------------------------------------
   KURULUM: Events Manager > Veri Kaynakları > Pixel'inizi seçin,
   "Pixel Kimliği" (15–16 haneli sayı) aşağıya yazın. Boş bırakıldığı
   sürece hiçbir izleme kodu çalışmaz (site normal şekilde açılır).   */

var MV8_PIXEL_ID = ''; // örn: '1234567890123456'

(function () {
  if (!MV8_PIXEL_ID) { window.mv8Track = function () {}; return; }

  // Meta Pixel standart kodu
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
  n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}
  (window,document,'script','https://connect.facebook.net/en_US/fbevents.js');

  fbq('init', MV8_PIXEL_ID);
  fbq('track', 'PageView');

  // Sayfalardan çağrılan yardımcı: standart olay değilse özel olay gönderir
  var STANDART = ['Lead','Contact','ViewContent','CompleteRegistration','Search','SubmitApplication'];
  window.mv8Track = function (olay, veri) {
    if (typeof fbq !== 'function') return;
    if (STANDART.indexOf(olay) > -1) fbq('track', olay, veri || {});
    else fbq('trackCustom', olay, veri || {});
  };
})();

if (!window.mv8Track) window.mv8Track = function () {};
