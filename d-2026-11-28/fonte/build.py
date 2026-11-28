import asyncio, os
from playwright.async_api import async_playwright

os.chdir(os.path.dirname(os.path.abspath(__file__)))

BASE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Fraunces;src:url(fraunces-latin-600-normal.woff2);font-weight:600}
*{margin:0;padding:0;box-sizing:border-box}
body{width:%(w)dpx;height:%(h)dpx;overflow:hidden;font-family:Inter,sans-serif;background:%(bgc)s;color:#3B2A22;position:relative}
.h{font-family:Fraunces,serif;font-weight:600;line-height:1.08;letter-spacing:-0.5px}
.pill{display:inline-block;background:#6F7C5E;color:#F3EDE4;border-radius:40px;padding:14px 32px;font-weight:600;letter-spacing:6px;font-size:26px}
.tag{display:inline-block;background:rgba(243,237,228,.94);color:#3B2A22;border-radius:12px;padding:14px 24px;font-weight:600;font-size:30px}
.abs{position:absolute}
.w{color:#fff}
.ts{text-shadow:0 2px 14px rgba(0,0,0,.35)}
</style></head><body>%(body)s</body></html>"""

def page(w, h, body, bgc="#F3EDE4"):
    return BASE % dict(w=w, h=h, body=body, bgc=bgc)

ARTS = {}

# ---------- ITEM 1: guirlanda, foto unica 1080x1350 (12h) ----------
# fundo: a propria foto ampliada e desfocada (continua a cena), foto nitida 1080x1080 embaixo
ARTS["item1-feed"] = page(1080, 1350, """
<div class="abs" style="inset:-40px;background:url(i1-a.jpg) center 20%/cover;filter:blur(26px) brightness(.62)"></div>
<div class="abs" style="left:0;top:270px;width:1080px;height:1080px;background:url(i1-a.jpg) center/cover"></div>
<div class="abs" style="left:0;top:262px;width:1080px;height:70px;background:linear-gradient(rgba(60,38,26,.55),rgba(60,38,26,0))"></div>
<div class="abs" style="left:72px;top:40px"><span class="pill">APROVADO PELA ARQUI</span></div>
<div class="abs h w ts" style="left:72px;top:112px;font-size:66px;width:980px;white-space:nowrap">Sua porta já está pronta<br>para o Natal?</div>
<div class="abs ts" style="right:36px;bottom:14px;font-size:21px;color:#fff;opacity:.92">#publi · Foto: anúncio da loja</div>
""")

# ---------- ITEM 3: rede, carrossel 2 slides 1080x1350 (21h) ----------
ARTS["item3-feed-1"] = page(1080, 1350, """
<div class="abs" style="inset:0;background:url(i3-a.jpg) center/cover"></div>
<div class="abs" style="left:0;right:0;top:0;height:470px;background:linear-gradient(rgba(30,20,15,.62),rgba(30,20,15,0))"></div>
<div class="abs" style="left:0;right:0;bottom:0;height:300px;background:linear-gradient(rgba(30,20,15,0),rgba(30,20,15,.55))"></div>
<div class="abs" style="left:72px;top:64px"><span class="pill">APROVADO PELA ARQUI</span></div>
<div class="abs h w" style="left:72px;top:150px;font-size:88px;width:940px">Repara no babado<br>de macramê</div>
<div class="abs w" style="left:72px;bottom:64px;font-size:40px;font-weight:600;line-height:1.2">Comenta QUERO<br>e receba o link 🤎</div>
<div class="abs" style="right:40px;bottom:28px;font-size:22px;color:#fff;opacity:.92">#publi · Foto: anúncio da loja</div>
""")

ARTS["item3-feed-2"] = page(1080, 1350, """
<div class="abs" style="left:0;top:270px;width:1080px;height:1080px;background:url(i3-b.jpg) center/cover"></div>
<div class="abs" style="left:0;top:250px;width:1080px;height:40px;background:linear-gradient(#fff,rgba(255,255,255,0))"></div>
<div class="abs h" style="left:72px;top:78px;font-size:66px;width:940px">Tecido de 2,80 x 1,50 m,<br>em algodão</div>
<div class="abs" style="left:72px;bottom:110px"><span class="tag" style="background:#F3EDE4">Suporta até 400 kg</span></div>
<div class="abs" style="right:40px;bottom:30px;font-size:22px;color:#3B2A22;opacity:.8">#publi · Foto: anúncio da loja</div>
""", bgc="#fff")

# ---------- STORIES 1080x1920 (sem "Link na bio", espaço livre para a figurinha de link) ----------
def story(img, title, sub, price, price_sub, photo_pos="center"):
    return page(1080, 1920, f"""
<div class="abs" style="left:80px;top:200px;font-size:30px;font-weight:700">#publi</div>
<div class="abs h" style="left:80px;top:260px;font-size:84px;width:920px">{title}</div>
<div class="abs" style="left:80px;top:465px;font-size:32px;color:#5a4a42;width:920px;line-height:1.3">{sub}</div>
<div class="abs" style="left:0;right:0;top:610px;height:800px;background:url({img}) {photo_pos}/cover"></div>
<div class="abs" style="left:80px;top:1450px"><div class="h" style="font-size:72px">{price}</div>
<div style="font-size:30px;margin-top:6px">{price_sub}</div></div>
<div class="abs" style="left:80px;bottom:60px;font-size:26px;color:#6b5a52">@confianaarquiteta</div>
<div class="abs" style="right:80px;bottom:60px;font-size:26px;color:#6b5a52">Foto: anúncio da loja</div>
""")

ARTS["item1-story-link"] = story("i1-a.jpg", "Sua porta já está<br>pronta para o Natal?", "Guirlanda de 30 cm, com laço dourado e luz de LED",
                                 "R$ 113,59", "preço de hoje, pode mudar", "center 50%")
ARTS["item2-story-link"] = story("i2-c.jpg", "Para o brinde<br>de fim de ano", "6 taças de cristal Bohemia, de 220 ml cada",
                                 "R$ 78,90", "preço de hoje, pode mudar", "center 60%")
ARTS["item3-story-link"] = story("i3-a.jpg", "Repara no babado<br>de macramê", "Rede de algodão, tecido de 2,80 x 1,50 m",
                                 "R$ 224,91", "preço de hoje, pode mudar", "center 55%")

# ---------- ITEM 2: Reels das taças (18h30) — cenas com área da foto em y=440 (1080x1080) ----------
def scene(title, bottom, pill=False):
    pl = '<div class="abs" style="left:80px;top:170px"><span class="pill">APROVADO PELA ARQUI</span></div>' if pill else ''
    return page(1080, 1920, f"""{pl}
<div class="abs h" style="left:80px;top:{262 if pill else 220}px;font-size:76px;width:920px">{title}</div>
<div class="abs" style="left:0;top:440px;width:1080px;height:1080px;background:#ddd"></div>
<div class="abs" style="left:80px;top:1590px;font-size:40px;font-weight:500;width:920px;line-height:1.25">{bottom}</div>
<div class="abs" style="right:80px;bottom:70px;font-size:24px;color:#6b5a52">#publi · Foto: anúncio da loja</div>""")
ARTS["sc1"] = scene("Para o brinde<br>de fim de ano", "6 taças de cristal Bohemia", pill=True)
ARTS["sc2"] = scene("Finas, com brilho<br>de cristal", "220 ml e 24,5 cm de altura")
ARTS["sc3"] = scene("Da ceia de Natal<br>à virada do ano", "Comenta QUERO e receba o link 🤎")
ARTS["item2-reels-capa"] = page(1080, 1920, """
<div class="abs" style="left:80px;top:250px"><span class="pill">APROVADO PELA ARQUI</span></div>
<div class="abs h" style="left:80px;top:350px;font-size:100px;width:920px">Para o brinde<br>de fim de ano</div>
<div class="abs" style="left:0;top:700px;width:1080px;height:1080px;background:url(i2-c.jpg) center/cover"></div>
<div class="abs" style="left:80px;bottom:50px;font-size:26px;color:#6b5a52">#publi · Foto: anúncio da loja</div>""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html in ARTS.items():
            w, h = (1080, 1350) if "-feed" in name else (1080, 1920)
            open(f"{name}.html", "w").write(html)
            pg = await b.new_page(viewport={"width": w, "height": h})
            await pg.goto(f"file://{os.getcwd()}/{name}.html")
            await pg.wait_for_timeout(500)
            ext = "png" if name.startswith("sc") else "jpg"
            if ext == "png":
                await pg.screenshot(path=f"{name}.png")
            else:
                await pg.screenshot(path=f"{name}.jpg", type="jpeg", quality=92)
            await pg.close()
        await b.close()
asyncio.run(main())
