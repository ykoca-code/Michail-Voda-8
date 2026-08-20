/* Google Ads / GA4 ölçümü.
   Kurulum: Google Ads → Araçlar → Dönüşümler ekranından aldığınız değerleri
   aşağıdaki üç satıra yazın. Boş bırakıldığı sürece bu dosya hiçbir şey yapmaz. */
(function () {
  var ETIKET_ID   = '';            // Örn. 'AW-1234567890'  (Google Ads etiketi)
  var GA4_ID      = '';            // Örn. 'G-XXXXXXXXXX'   (isteğe bağlı)
  var LEAD_ETIKET = '';            // Örn. 'AW-1234567890/AbC-D_efG'  (dönüşüm etiketi)

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
