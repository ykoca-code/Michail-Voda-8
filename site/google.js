/* Google Ads / GA4 ölçümü.

   LEAD_ETIKET BİLEREK BOŞ — DOLDURMAYIN.
   Lead dönüşümü Google Ads tarafında URL kuralıyla tanımlı:
   "tesekkurler" içeren sayfa yüklendiğinde Google, sitedeki AW etiketinin
   sayfa görüntüleme sinyalinden dönüşümü kendisi eşliyor. Buraya bir
   dönüşüm etiketi yazmak aynı formu İKİ KEZ saydırır.
   (Google Ads'teki 7727865543 numarası "dönüşüm türü kimliği"dir,
   conversion label değildir; AW-.../7727865543 şeklinde birleştirilemez.)

   GA4_ID isteğe bağlı; doldurulursa GA4 ölçümü de devreye girer. */
(function () {
  var ETIKET_ID   = 'AW-18401005291';            // Google Ads etiketi
  var GA4_ID      = '';            // Örn. 'G-XXXXXXXXXX'   (isteğe bağlı)
  var LEAD_ETIKET = '';            // Boş kalacak — yukarıdaki nota bakın

  var idler = [ETIKET_ID, GA4_ID].filter(Boolean);
  if (!idler.length) { window.mv8Google = function () {}; return; }

  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + idler[0];
  document.head.appendChild(s);

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('js', new Date());
  idler.forEach(function (id) { gtag('config', id); });

  /* Dönüşüm: yalnızca teşekkür sayfasında çağrılır. */
  window.mv8Google = function (olay) {
    if (olay === 'Lead' && LEAD_ETIKET) {
      gtag('event', 'conversion', { send_to: LEAD_ETIKET });
    }
    if (GA4_ID) {
      gtag('event', olay === 'Lead' ? 'generate_lead' : olay);
    }
  };
})();
