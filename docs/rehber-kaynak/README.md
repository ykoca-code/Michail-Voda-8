# Yatırımcı rehberi — kaynak

`rehber.html` bu klasördeki fontlar ve görsellerle birlikte Chromium'un
"yazdır → PDF" motoruyla basılıyor. Çıktı: `site/rehber/michail-voda-8-golden-visa-rehberi.pdf`

## Yeniden üretmek

```bash
cd docs/rehber-kaynak && python3 -m http.server 8894 &
python3 - <<'PY'
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg = b.new_page()
    pg.goto('http://localhost:8894/rehber.html', wait_until='networkidle')
    pg.pdf(path='../../site/rehber/michail-voda-8-golden-visa-rehberi.pdf',
           format='A4', print_background=True,
           margin={'top':'0','bottom':'0','left':'0','right':'0'})
    b.close()
PY
```

Fiyat, daire sayısı veya teslim tarihi değişirse `rehber.html` güncellenip
PDF yeniden basılmalı. Rakamların geçerlilik tarihi son sayfada yazıyor.

## Uyum

Metinlerde "vatandaşlık", "garanti", "pasaport" ifadeleri geçmiyor; izin
her yerde "başvuru" olarak ifade ediliyor. Son sayfadaki yasal uyarı
başvuru sonucunun resmi makamların takdirinde olduğunu belirtiyor.
