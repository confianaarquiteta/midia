import asyncio, sys
from playwright.async_api import async_playwright

BASE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Fraunces;src:url(fraunces-latin-600-normal.woff2);font-weight:600}
*{margin:0;padding:0;box-sizing:border-box}
body{width:%(w)dpx;height:%(h)dpx;overflow:hidden;font-family:Inter,sans-serif;background:#F3EDE4;color:#3B2A22;position:relative}
.bg{position:absolute;inset:0;background-size:cover;background-position:%(pos)s}
.h{font-family:Fraunces,serif;font-weight:600;line-height:1.08;letter-spacing:-0.5px}
.pill{display:inline-block;background:#6F7C5E;color:#F3EDE4;border-radius:40px;padding:14px 32px;font-weight:600;letter-spacing:6px;font-size:26px}
.tag{display:inline-block;background:rgba(243,237,228,.92);color:#3B2A22;border-radius:12px;padding:14px 24px;font-weight:600;font-size:30px}
.abs{position:absolute}
.shadowtop{position:absolute;left:0;right:0;top:0;height:%(st)dpx;background:linear-gradient(rgba(30,20,15,.62),rgba(30,20,15,0))}
.shadowbot{position:absolute;left:0;right:0;bottom:0;height:%(sb)dpx;background:linear-gradient(rgba(30,20,15,0),rgba(30,20,15,.62))}
.w{color:#fff}
.small{font-size:26px;opacity:.95}
</style></head><body>%(body)s</body></html>"""

def page(w, h, body, pos="center", st=0, sb=0):
    return BASE % dict(w=w, h=h, body=body, pos=pos, st=st, sb=sb)

ARTS = {}

# ---------- ITEM 1: feed carrossel 1080x1350 ----------
ARTS["item1-feed-1"] = page(1080, 1350, """
<div class="bg" style="background-image:url(i1-a.jpg)"></div>
<div class="shadowtop"></div><div class="shadowbot"></div>
<div class="abs" style="left:72px;top:72px"><span class="pill">APROVADO PELA ARQUI</span></div>
<div class="abs h w" style="left:72px;top:170px;font-size:84px;width:900px">Mesa de Natal<br>pronta para 4</div>
<div class="abs w" style="left:72px;bottom:72px;font-size:30px;font-weight:500;width:440px">Jogo americano, guardanapo<br>e argola dourada</div>
<div class="abs w" style="right:72px;bottom:72px;text-align:right">
<div style="font-size:42px;font-weight:600;line-height:1.2">Comenta QUERO<br>e receba o link 🤎</div>
<div class="small" style="margin-top:14px">#publi · Foto: anúncio da loja</div></div>
""", pos="center", st=520, sb=420)

ARTS["item1-feed-2"] = page(1080, 1350, """
<div class="bg" style="background-image:url(i1-b.jpg)"></div>
<div class="abs" style="left:72px;top:72px"><span class="tag">Jogo americano redondo de 38 cm</span></div>
<div class="abs" style="left:72px;bottom:150px"><span class="tag">Guardanapo de tecido 35 x 35 cm</span></div>
<div class="abs" style="left:72px;bottom:72px"><span class="tag">Argola dourada</span></div>
<div class="abs" style="right:40px;bottom:30px;font-size:22px;color:#3B2A22;opacity:.8">#publi · Foto: anúncio da loja</div>
""", pos="center")

ARTS["item1-feed-3"] = page(1080, 1350, """
<div class="bg" style="background-image:url(i1-c.jpg)"></div>
<div class="shadowbot"></div>
<div class="abs w" style="left:72px;bottom:150px;width:940px">
<div class="h" style="font-size:66px">Kit para 4 lugares</div>
<div style="font-size:30px;margin-top:14px;font-weight:500">Prato, taça e talheres não acompanham</div></div>
<div class="abs w" style="left:72px;bottom:60px;font-size:34px;font-weight:600">Comenta QUERO e receba o link 🤎</div>
<div class="abs w small" style="right:40px;bottom:24px;font-size:22px">#publi · Foto: anúncio da loja</div>
""", pos="center", sb=560)

# ---------- STORY base (1080x1920) ----------
def story(img, title, sub, price=None, price_sub=None, link_bio=False, photo_pos="center", photo_h=760):
    p = ""
    if price:
        p = f"""<div class="abs" style="left:80px;top:1480px"><div class="h" style="font-size:72px;color:#3B2A22">{price}</div>
<div style="font-size:30px;margin-top:6px">{price_sub}</div></div>"""
    lb = ""
    if link_bio:
        lb = """<div class="abs" style="left:80px;top:1660px"><span style="display:inline-block;background:#A55A41;color:#F3EDE4;border-radius:40px;padding:18px 40px;font-size:34px;font-weight:600">Link na bio 🤎</span></div>"""
    else:
        lb = ""
    return page(1080, 1920, f"""
<div class="abs" style="left:80px;top:240px;font-size:30px;font-weight:700">#publi</div>
<div class="abs h" style="left:80px;top:300px;font-size:84px;width:920px">{title}</div>
<div class="abs" style="left:80px;top:{300+190}px;font-size:32px;color:#5a4a42;width:920px">{sub}</div>
<div class="abs" style="left:0;right:0;top:640px;height:{photo_h}px;background:url({img}) {photo_pos}/cover"></div>
{p}{lb}
<div class="abs" style="left:80px;bottom:60px;font-size:26px;color:#6b5a52">@confianaarquiteta</div>
<div class="abs" style="right:80px;bottom:60px;font-size:26px;color:#6b5a52">Foto: anúncio da loja</div>
""")

# item 3 story de venda (21h) com preço e Link na bio
ARTS["item3-story"] = story("i3-quarto.jpg", "Cara de loja de<br>decoração cara", "Abajur de mesa com 40 cm de altura e cúpula de linho",
                            price="R$ 65,22", price_sub="preço de hoje, pode mudar", link_bio=True, photo_pos="center 40%")
# stories com espaço para figurinha (sem Link na bio)
ARTS["item3-story-link"] = story("i3-quarto.jpg", "Cara de loja de<br>decoração cara", "Abajur de mesa com 40 cm de altura e cúpula de linho",
                                 price="R$ 65,22", price_sub="preço de hoje, pode mudar", photo_pos="center 40%")
ARTS["item1-story-link"] = story("i1-c.jpg", "Mesa de Natal<br>pronta para 4", "Jogo americano de 38 cm, guardanapo e argola dourada",
                                 price="R$ 61,50", price_sub="kit para 4 lugares · preço de hoje, pode mudar", photo_pos="center 45%")
ARTS["item2-story-link"] = story("i2-sala.jpg", "Verde que não<br>precisa regar", "6 vasinhos de gesso feitos à mão, com planta artificial",
                                 price="R$ 39,99", price_sub="kit com 6 · preço de hoje, pode mudar", photo_pos="center 70%")

# ---------- Reels: cenas (fundo off-white, foto no meio 1080x1080 em y=440) ----------
def scene(title, bottom, pill=False):
    pl = '<div class="abs" style="left:80px;top:170px"><span class="pill">APROVADO PELA ARQUI</span></div>' if pill else ''
    return page(1080, 1920, f"""{pl}
<div class="abs h" style="left:80px;top:{260 if pill else 220}px;font-size:76px;width:920px">{title}</div>
<div class="abs" style="left:0;top:440px;width:1080px;height:1080px;background:#ddd"></div>
<div class="abs" style="left:80px;top:1590px;font-size:40px;font-weight:500;width:920px">{bottom}</div>
<div class="abs" style="right:80px;bottom:70px;font-size:24px;color:#6b5a52">#publi · Foto: anúncio da loja</div>""")
ARTS["sc1"] = scene("Verde que não<br>precisa regar", "Kit com 6 vasinhos de gesso", pill=True)
ARTS["sc2"] = scene("Na mesa, no aparador<br>ou na varanda", "Já vêm com as plantinhas artificiais")
ARTS["sc3"] = scene("Feitos à mão,<br>em gesso", "Comenta QUERO e receba o link 🤎")
ARTS["item2-reels-capa"] = page(1080, 1920, """
<div class="bg" style="background-image:url(i2-sala.jpg);background-position:center 70%"></div>
<div class="shadowtop" style="height:760px"></div>
<div class="abs" style="left:80px;top:250px"><span class="pill">APROVADO PELA ARQUI</span></div>
<div class="abs h w" style="left:80px;top:350px;font-size:100px;width:920px">Verde que não<br>precisa regar</div>
<div class="abs w" style="left:80px;bottom:80px;font-size:26px">#publi · Foto: anúncio da loja</div>""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html in ARTS.items():
            w, h = (1080, 1350) if name.startswith("item1-feed") else (1080, 1920)
            open(f"{name}.html", "w").write(html)
            pg = await b.new_page(viewport={"width": w, "height": h})
            await pg.goto(f"file:///home/claude/work/art/{name}.html")
            await pg.wait_for_timeout(300)
            if name.startswith("ov"):
                await pg.screenshot(path=f"{name}.png", omit_background=True)
            else:
                await pg.screenshot(path=f"{name}.jpg", type="jpeg", quality=92)
            await pg.close()
        await b.close()
asyncio.run(main())
