#!/usr/bin/env python3
"""Şantiye fotoğraflarını marka çerçevesine oturtur.

Ham şantiye fotoğrafı ikna etmez; tarihli ve markalı bir ilerleme karesi eder.
Reklam görselleriyle aynı dil: tam kanvas fotoğraf, alttan koyu degrade,
üstte marka + tarih rozeti, altta serif başlık ve italik vurgu satırı.

    python3 santiye-kare.py FOTOGRAF --tarih "26 Ağustos 2026" \
        --baslik "3. katta sıva tamamlandı" --vurgu "Teslime 4 ay" \
        --kirp "0,0.18,1,1"          # yüz/istenmeyen alanı kadrajdan çıkarmak için

4:5 ve 9:16 olmak üzere iki dosya üretir.
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFont

KOK = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(KOK, '..', '..', 'docs', 'rehber-kaynak', 'fonts')
SERIF   = os.path.join(FONT, 'FRAUNCES.ttf')
ITALIK  = os.path.join(FONT, 'FRAUNCES-ITALIC.ttf')
SANS    = os.path.join(FONT, 'INSTRUMENT.ttf')

ACCENT = (230, 174, 149)
BEYAZ  = (255, 255, 255)
SIS    = (214, 208, 202)

OLCU = {'45': (1080, 1350), '916': (1080, 1920)}


def yaz(f, p):
    return ImageFont.truetype(f, p)


def aralikli(d, xy, metin, font, renk, aralik):
    """Harf aralıklı yazı — küçük başlıklar için."""
    x, y = xy
    for ch in metin:
        d.text((x, y), ch, font=font, fill=renk)
        x += d.textlength(ch, font=font) + aralik
    return x


def kadraj(im, W, H, kirp=None):
    if kirp:
        l, t, r, b = kirp
        im = im.crop((int(l * im.width), int(t * im.height),
                      int(r * im.width), int(b * im.height)))
    olcek = max(W / im.width, H / im.height)
    yeni = im.resize((round(im.width * olcek), round(im.height * olcek)), Image.LANCZOS)
    return yeni.crop(((yeni.width - W) // 2, (yeni.height - H) // 2,
                      (yeni.width - W) // 2 + W, (yeni.height - H) // 2 + H))


def degrade(im, ust=0.30, alt=0.78):
    W, H = im.size
    kat = Image.new('L', (1, H), 0)
    px = kat.load()
    for y in range(H):
        o = y / H
        a = 235 * ((o - (1 - alt)) / alt) ** 1.5 if o > 1 - alt else 0
        u = 150 * ((ust - o) / ust) ** 1.4 if o < ust else 0
        px[0, y] = int(min(245, max(a, u)))
    maske = kat.resize((W, H))
    return Image.composite(Image.new('RGB', (W, H), (14, 12, 11)), im, maske)


def sar(d, metin, font, genislik):
    kelime, satir, hepsi = metin.split(), '', []
    for k in kelime:
        deneme = (satir + ' ' + k).strip()
        if d.textlength(deneme, font=font) <= genislik:
            satir = deneme
        else:
            if satir:
                hepsi.append(satir)
            satir = k
    if satir:
        hepsi.append(satir)
    return hepsi


def uret(kaynak, hedef, boy, tarih, baslik, vurgu, kirp):
    W, H = OLCU[boy]
    im = degrade(kadraj(Image.open(kaynak).convert('RGB'), W, H, kirp))
    d = ImageDraw.Draw(im)
    M = 62                                    # kenar boşluğu

    # --- üst: marka
    fm = yaz(SERIF, 54)
    fmi = yaz(ITALIK, 54)
    x = M
    d.text((x, M), 'Michail Voda ', font=fm, fill=BEYAZ)
    x += d.textlength('Michail Voda ', font=fm)
    d.text((x, M), '8', font=fmi, fill=ACCENT)
    aralikli(d, (M + 4, M + 68), 'ATHENS', yaz(SANS, 21), SIS, 7)

    # --- üst sağ: tarih rozeti
    fr = yaz(SANS, 21)
    rozet = 'ŞANTİYE · ' + tarih.upper()
    gen = sum(d.textlength(c, font=fr) + 5 for c in rozet) + 40
    d.rectangle([W - M - gen, M - 2, W - M, M + 44], outline=(235, 232, 228), width=2)
    aralikli(d, (W - M - gen + 20, M + 10), rozet, fr, (240, 238, 235), 5)

    # --- alt: başlık bloğu
    fb = yaz(SERIF, 76 if boy == '45' else 82)
    fv = yaz(ITALIK, 54 if boy == '45' else 58)
    satirlar = sar(d, baslik, fb, W - 2 * M)
    yuk = len(satirlar) * (fb.size + 14) + (fv.size + 22 if vurgu else 0)
    y = H - M - 58 - yuk

    aralikli(d, (M + 3, y - 40), 'İNŞAAT GÜNLÜĞÜ', yaz(SANS, 22), SIS, 8)
    for s in satirlar:
        d.text((M, y), s, font=fb, fill=BEYAZ)
        y += fb.size + 14
    if vurgu:
        d.text((M, y + 6), vurgu, font=fv, fill=ACCENT)

    d.text((M, H - M - 30), 'MICHAILVODA8.COM', font=yaz(SANS, 24), fill=(226, 222, 217))
    im.save(hedef, quality=92, optimize=True)
    return hedef


def main():
    p = argparse.ArgumentParser()
    p.add_argument('foto')
    p.add_argument('--tarih', required=True)
    p.add_argument('--baslik', required=True)
    p.add_argument('--vurgu', default='')
    p.add_argument('--kirp', default='', help='sol,ust,sag,alt oranları — ör. 0,0.18,1,1')
    p.add_argument('--cikti', default='.')
    p.add_argument('--ad', default='santiye')
    a = p.parse_args()
    kirp = [float(v) for v in a.kirp.split(',')] if a.kirp else None
    for boy in ('45', '916'):
        yol = os.path.join(a.cikti, f'{a.ad}-{boy}.jpg')
        print(uret(a.foto, yol, boy, a.tarih, a.baslik, a.vurgu, kirp))


if __name__ == '__main__':
    main()
