#!/usr/bin/env python3
"""Golden Visa reklam kreatifi üretir.

Instagram'daki organik gönderiyle aynı dil: tam kanvas görsel, alttan koyu
degrade, üstte marka + teslim rozeti, altta serif başlık ve italik vurgu.
Her başlık konuyu bilmeyen birine kendini anlatmalı — Atina, 250.000 € ve
oturum izni başvurusu birlikte geçmeli.

    python3 reklam-kare.py GORSEL --ad gv-kira \
      --kicker "YUNANİSTAN GOLDEN VISA · ATİNA" \
      --baslik "Ayda 500 € kira garantili|250.000 €'luk Atina dairesi" \
      --vurgu "+ ailenizle oturum izni başvurusu"

4:5 ve 9:16 üretir. Başlık satırları | ile ayrılır.
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFont

KOK  = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(KOK, '..', '..', 'docs', 'rehber-kaynak', 'fonts')
SERIF  = os.path.join(FONT, 'FRAUNCES.ttf')
ITALIK = os.path.join(FONT, 'FRAUNCES-ITALIC.ttf')
SANS   = os.path.join(FONT, 'INSTRUMENT.ttf')

ACCENT = (230, 174, 149)
BEYAZ  = (255, 255, 255)
SIS    = (206, 200, 194)
UYARI  = 'Başvuru sonucu resmi\nmakamların takdirindedir.'

OLCU = {'45': (1080, 1350), '916': (1080, 1920)}


def f(yol, punto):
    return ImageFont.truetype(yol, punto)


def aralikli(d, xy, metin, font, renk, aralik):
    x, y = xy
    for ch in metin:
        d.text((x, y), ch, font=font, fill=renk)
        x += d.textlength(ch, font=font) + aralik
    return x - aralik


def kadraj(im, W, H):
    olcek = max(W / im.width, H / im.height)
    yeni = im.resize((round(im.width * olcek), round(im.height * olcek)), Image.LANCZOS)
    sx, sy = (yeni.width - W) // 2, (yeni.height - H) // 2
    return yeni.crop((sx, sy, sx + W, sy + H))


def degrade(im, ust=0.26, alt=0.62):
    W, H = im.size
    kat = Image.new('L', (1, H))
    px = kat.load()
    for y in range(H):
        o = y / H
        a = 232 * ((o - (1 - alt)) / alt) ** 1.6 if o > 1 - alt else 0
        u = 120 * ((ust - o) / ust) ** 1.5 if o < ust else 0
        px[0, y] = int(min(242, max(a, u)))
    return Image.composite(Image.new('RGB', (W, H), (16, 13, 12)), im, kat.resize((W, H)))


def uret(kaynak, hedef, boy, kicker, satirlar, vurgu, alt):
    W, H = OLCU[boy]
    im = degrade(kadraj(Image.open(kaynak).convert('RGB'), W, H), alt=alt)
    d = ImageDraw.Draw(im)
    M = 62

    fm, fmi = f(SERIF, 54), f(ITALIK, 54)
    x = M
    d.text((x, M), 'Michail Voda ', font=fm, fill=BEYAZ)
    x += d.textlength('Michail Voda ', font=fm)
    d.text((x, M), '8', font=fmi, fill=ACCENT)
    aralikli(d, (M + 4, M + 68), 'ATHENS', f(SANS, 21), SIS, 7)

    fr = f(SANS, 21)
    rozet = 'TESLİM · ARALIK 2026'
    gen = sum(d.textlength(c, font=fr) + 5 for c in rozet) + 40
    d.rectangle([W - M - gen, M - 2, W - M, M + 44], outline=(232, 229, 225), width=2)
    aralikli(d, (W - M - gen + 20, M + 10), rozet, fr, (240, 238, 235), 5)

    # başlık, kutuya sığana kadar küçülür
    punto = 74 if boy == '45' else 80
    while punto > 44:
        fb = f(SERIF, punto)
        if max(d.textlength(s, font=fb) for s in satirlar) <= W - 2 * M:
            break
        punto -= 2
    fb = f(SERIF, punto)
    fv = f(ITALIK, max(40, punto - 20))

    yuk = len(satirlar) * (punto + 12) + fv.size + 20
    y = H - M - 96 - yuk
    aralikli(d, (M + 3, y - 42), kicker, f(SANS, 22), SIS, 8)
    for s in satirlar:
        d.text((M, y), s, font=fb, fill=BEYAZ)
        y += punto + 12
    d.text((M, y + 4), vurgu, font=fv, fill=ACCENT)

    d.text((M, H - M - 34), 'MICHAILVODA8.COM', font=f(SANS, 24), fill=(226, 222, 217))
    fu = f(SANS, 20)
    for i, s in enumerate(UYARI.split('\n')):
        d.text((W - M - d.textlength(s, font=fu), H - M - 46 + i * 26), s, font=fu, fill=(178, 172, 166))

    im.save(hedef, quality=92, optimize=True)
    return hedef


def main():
    p = argparse.ArgumentParser()
    p.add_argument('gorsel')
    p.add_argument('--ad', required=True)
    p.add_argument('--kicker', required=True)
    p.add_argument('--baslik', required=True, help='satırlar | ile ayrılır')
    p.add_argument('--vurgu', required=True)
    p.add_argument('--cikti', default='.')
    p.add_argument('--karart', type=float, default=0.62,
                   help='alt degradenin kapladığı oran; açık zeminli görsellerde yükseltin')
    a = p.parse_args()
    satirlar = [s.strip() for s in a.baslik.split('|')]
    for boy in ('45', '916'):
        print(uret(a.gorsel, os.path.join(a.cikti, f'{a.ad}-{boy}.jpg'),
                   boy, a.kicker, satirlar, a.vurgu, a.karart))


if __name__ == '__main__':
    main()
