import asyncio, os
from playwright.async_api import async_playwright

os.chdir(os.path.dirname(os.path.abspath(__file__)))

BASE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Fraunces;src:url(fraunces-latin-600-normal.woff2);font-weight:600}
*{margin:0;padding:0;box-sizing:border-box}
body{width:%(w)dpx;height:%(h)dpx;overflow:hidden;font-family:Inter,sans-serif;background:%(bgc)s;color:#3B2A22;position:relative}
.bg{position:absolute;inset:0;background-size:cover;background-position:%(pos)s}
.h{font-family:Fraunces,serif;font-weight:600;line-height:1.08;letter-spacing:-0.5px}
.pill{display:inline-block;background:#6F7C5E;color:#F3EDE4;border-radius:40px;padding:14px 32px;font-weight:600;letter-spacing:6px;font-size:26px}
.tag{display:inline-block;background:rgba(243,237,228,.93);color:#3B2A22;border-radius:12px;padding:14px 24px;font-weight:600;font-size:30px}
.abs{position:absolute}
.shadowtop{position:absolute;left:0;right:0;top:0;height:%(st)dpx;background:linear-gradient(rgba(30,20,15,.62),rgba(30,20,15,0))}
.shadowbot{position:absolute;left:0;right:0;bottom:0;height:%(sb)dpx;background:linear-gradient(rgba(30,20,15,0),rgba(30,20,15,.62))}
.w{color:#fff}
.small{font-size:26px;opacity:.95}
</style></head><body>%(body)s</body></html>"""

def page(w, h, body, pos="center", st=0, sb=0, bgc="#F3EDE4"):
    return BASE % dict(w=w, h=h, body=body, pos=pos, st=st, sb=sb, bgc=bgc)

ARTS = {}

# ---------- ITEM 1: bandeja, carrossel 1080x1350 ----------
ARTS["item1-feed-1"] = page(1080, 1350, """
<div class="bg" style="background-image:url(i1-a.jpg)"></div>
<div class="shadowtop"></div><div class="shadowbot"></div>
<div class="abs" style="left:72px;top:72px"><span class="pill">APROVADO PELA ARQUI</span></div>
<div class="abs h w" style="left:72px;top:170px;font-size:88px;width:940px">Café na cama,<br>com cara de hotel</div>
<div class="abs w" style="left:72px;bottom:72px;font-size:30px;font-weight:500;width:420px">Bandeja de bambu<br>com pés dobráveis</div>
<div class="abs w" style="right:72px;bottom:72px;text-align:right">
<div style="font-size:42px;font-weight:600;line-height:1.2">Comenta QUERO<br>e receba o link 🤎</div>
<div class="small" style="margin-top:14px">#publi · Foto: anúncio da loja</div></div>
""", pos="center 60%", st=520, sb=440)

ARTS["item1-feed-2"] = page(1080, 1350, """
<div class="bg" style="background-image:url(i1-b.jpg)"></div>
<div class="abs" style="left:72px;top:72px"><span class="tag">Do quarto ao sofá</span></div>
<div class="abs" style="left:72px;bottom:72px"><span class="tag">Pés dobráveis</span></div>
<div class="abs" style="right:40px;bottom:30px;font-size:22px;color:#fff;opacity:.9">#publi · Foto: anúncio da loja</div>
""", pos="center")

ARTS["item1-feed-3"] = page(1080, 1350, """
<div class="abs" style="left:0;top:270px;width:1080px;height:1080px;background:url(i1-c.jpg) center/cover"></div>
<div class="abs" style="left:0;top:250px;width:1080px;height:40px;background:linear-gradient(#ebe6e0,rgba(235,230,224,0))"></div>
<div class="abs h" style="left:72px;top:80px;font-size:66px;width:940px">50 x 30 cm de bambu,<br>com pés dobráveis</div>
<div class="abs" style="left:72px;bottom:150px"><span class="tag">Comenta QUERO e receba o link 🤎</span></div>
<div class="abs" style="right:40px;bottom:30px;font-size:22px;color:#3B2A22;opacity:.8">#publi · Foto: anúncio da loja</div>
""", bgc="#EBE6E0")

# ---------- STORY base (1080x1920) ----------
def story(img, title, sub, price=None, price_sub=None, link_bio=False, photo_pos="center"):
    p = ""
    if price:
        p = f"""<div class="abs" style="left:80px;top:1440px"><div class="h" style="font-size:72px;color:#3B2A22">{price}</div>
<div style="font-size:30px;margin-top:6px">{price_sub}</div></div>"""
    lb = ""
    if link_bio:
        lb = """<div class="abs" style="left:80px;top:1640px"><span style="display:inline-block;background:#A55A41;color:#F3EDE4;border-radius:40px;padding:18px 40px;font-size:34px;font-weight:600">Link na bio 🤎</span></div>"""
    return page(1080, 1920, f"""
<div class="abs" style="left:80px;top:220px;font-size:30px;font-weight:700">#publi</div>
<div class="abs h" style="left:80px;top:280px;font-size:84px;width:920px">{title}</div>
<div class="abs" style="left:80px;top:480px;font-size:32px;color:#5a4a42;width:920px">{sub}</div>
<div class="abs" style="left:0;right:0;top:620px;height:780px;background:url({img}) {photo_pos}/cover"></div>
{p}{lb}
<div class="abs" style="left:80px;bottom:60px;font-size:26px;color:#6b5a52">@confianaarquiteta</div>
<div class="abs" style="right:80px;bottom:60px;font-size:26px;color:#6b5a52">Foto: anúncio da loja</div>
""")

T3, S3 = "Ao lado do sofá,<br>só o essencial", "Mesa lateral de um pé só, com 34 cm de diâmetro e 52 cm de altura"
ARTS["item3-story"] = story("i3-a.jpg", T3, S3, price="R$ 106,74", price_sub="na Black Friday · preço de hoje, pode mudar", link_bio=True, photo_pos="center 62%")
ARTS["item3-story-link"] = story("i3-a.jpg", T3, S3, price="R$ 106,74", price_sub="na Black Friday · preço de hoje, pode mudar", photo_pos="center 62%")
ARTS["item1-story-link"] = story("i1-a.jpg", "Café na cama,<br>com cara de hotel", "Bandeja de bambu de 50 x 30 cm, com pés dobráveis",
                                 price="R$ 56,99", price_sub="no Pix · preço de hoje, pode mudar", photo_pos="center 55%")
ARTS["item2-story-link"] = story("i2-a-sq.jpg", "Lavabo arrumado<br>com charme", "Cesto de algodão trançado, feito artesanalmente, 33 x 15 x 10 cm",
                                 price="R$ 29,98", price_sub="preço de hoje, pode mudar", photo_pos="center 55%")

# ---------- Reels: cenas (fundo off-white, foto 1080x1080 em y=440, inserida no vídeo) ----------
def scene(title, bottom, pill=False):
    pl = '<div class="abs" style="left:80px;top:170px"><span class="pill">APROVADO PELA ARQUI</span></div>' if pill else ''
    return page(1080, 1920, f"""{pl}
<div class="abs h" style="left:80px;top:{260 if pill else 220}px;font-size:76px;width:920px">{title}</div>
<div class="abs" style="left:0;top:440px;width:1080px;height:1080px;background:#ddd"></div>
<div class="abs" style="left:80px;top:1590px;font-size:40px;font-weight:500;width:920px">{bottom}</div>
<div class="abs" style="right:80px;bottom:70px;font-size:24px;color:#6b5a52">#publi · Foto: anúncio da loja</div>""")
ARTS["sc1"] = scene("Lavabo arrumado<br>com charme", "Cesto de algodão trançado", pill=True)
ARTS["sc2"] = scene("Feito<br>artesanalmente", "Corda de algodão, com alças")
ARTS["sc3"] = scene("Na bancada,<br>na cômoda, no lavabo", "Comenta QUERO e receba o link 🤎")
ARTS["item2-reels-capa"] = page(1080, 1920, """
<div class="abs" style="left:80px;top:250px"><span class="pill">APROVADO PELA ARQUI</span></div>
<div class="abs h" style="left:80px;top:350px;font-size:100px;width:920px">Lavabo arrumado<br>com charme</div>
<div class="abs" style="left:0;top:700px;width:1080px;height:1080px;background:url(i2-a-sq.jpg) center/cover"></div>
<div class="abs" style="left:80px;bottom:50px;font-size:26px;color:#6b5a52">#publi · Foto: anúncio da loja</div>""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html in ARTS.items():
            w, h = (1080, 1350) if name.startswith("item1-feed") else (1080, 1920)
            open(f"{name}.html", "w").write(html)
            pg = await b.new_page(viewport={"width": w, "height": h})
            await pg.goto(f"file://{os.getcwd()}/{name}.html")
            await pg.wait_for_timeout(400)
            await pg.screenshot(path=f"{name}.jpg", type="jpeg", quality=92)
            await pg.close()
        await b.close()
asyncio.run(main())
