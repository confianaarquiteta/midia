import asyncio, os
from playwright.async_api import async_playwright

os.chdir(os.path.dirname(os.path.abspath(__file__)))

BASE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Fraunces;src:url(fraunces-latin-600-normal.woff2);font-weight:600}
*{margin:0;padding:0;box-sizing:border-box}
body{width:%(w)dpx;height:%(h)dpx;overflow:hidden;font-family:Inter,sans-serif;background:#F3EDE4;color:#3B2A22;position:relative}
.h{font-family:Fraunces,serif;font-weight:600;line-height:1.08;letter-spacing:-0.5px}
.pill{display:inline-block;background:#6F7C5E;color:#F3EDE4;border-radius:40px;padding:12px 28px;font-weight:600;letter-spacing:6px;font-size:24px}
.abs{position:absolute}
</style></head><body>%(body)s</body></html>"""

def page(w, h, body):
    return BASE % dict(w=w, h=h, body=body)

# name, details, price, photo
G = [
    ("Dourada, com luz", "30 cm · laço dourado, flores claras e luz de LED", "R$ 113,59", "g1.jpg", "https://meli.la/1GkEVZZ"),
    ("Clássica vermelha", "30 cm · laço vermelho, bolas e fio de luz de LED", "R$ 66,78 no Pix", "g2.jpg", "https://meli.la/1oEnts6"),
    ("Nevada, com pinhas", "60 cm · pontas nevadas, pinhas e frutinhas", "R$ 98,37", "g3.jpg", "https://meli.la/1zfBkxn"),
    ("Flores e “Feliz Natal”", "38 cm · laço, flores vermelhas e bolas", "R$ 59,90", "g5.jpg", "https://meli.la/13dNELo"),
    ("Verde, para enfeitar", "60 cm · base lisa para decorar do seu jeito", "R$ 74,73", "g4.jpg", "https://meli.la/2Ktrkhf"),
]

ARTS = {}

ARTS["feed-1"] = page(1080, 1350, """
<div class="abs" style="inset:-40px;background:url(g3.jpg) center 30%/cover;filter:blur(28px) brightness(1.02)"></div>
<div class="abs" style="inset:0;background:rgba(243,237,228,.55)"></div>
<div class="abs" style="left:0;top:270px;width:1080px;height:1080px;background:url(g3.jpg) center/cover"></div>
<div class="abs" style="left:72px;top:44px"><span class="pill">SELEÇÃO DA ARQUI</span></div>
<div class="abs h" style="left:72px;top:112px;font-size:66px;width:960px">Qual guirlanda combina<br>com a sua porta?</div>
<div class="abs" style="left:72px;bottom:44px;background:rgba(243,237,228,.94);border-radius:12px;padding:14px 24px;font-weight:600;font-size:28px">5 opções com envio nacional · arrasta 👉</div>
<div class="abs" style="right:36px;bottom:14px;font-size:20px;color:#3B2A22;opacity:.8">#publi · Fotos: anúncios das lojas</div>
""")

for i, (name, det, price, img, _) in enumerate(G, start=2):
    ARTS[f"feed-{i}"] = page(1080, 1350, f"""
<div class="abs" style="inset:-40px;background:url({img}) center 80%/cover;filter:blur(28px) brightness(.55)"></div>
<div class="abs" style="left:0;top:0;width:1080px;height:1080px;background:url({img}) center/cover"></div>
<div class="abs" style="left:0;top:1060px;width:1080px;height:40px;background:linear-gradient(rgba(40,28,20,0),rgba(40,28,20,.35))"></div>
<div class="abs h" style="left:72px;top:1112px;font-size:58px;color:#fff;width:640px">{name}</div>
<div class="abs" style="left:72px;top:1190px;font-size:28px;color:#F3EDE4;width:700px;line-height:1.3">{det}</div>
<div class="abs" style="right:72px;top:1118px;text-align:right"><div class="h" style="font-size:46px;color:#fff;white-space:nowrap">{price}</div>
<div style="font-size:22px;color:#F3EDE4;margin-top:6px">preço de hoje, pode mudar</div></div>
<div class="abs" style="right:36px;bottom:14px;font-size:20px;color:#fff;opacity:.85">#publi · Foto: anúncio da loja</div>
""")

ARTS["feed-7"] = page(1080, 1350, """
<div class="abs" style="left:0;top:0;width:1080px;height:640px;display:grid;grid-template-columns:repeat(5,1fr);gap:6px">
""" + "".join(f'<div style="background:url({g[3]}) center/cover"></div>' for g in G) + """</div>
<div class="abs h" style="left:72px;top:720px;font-size:72px;width:940px">Gostou de uma?</div>
<div class="abs" style="left:72px;top:830px;font-size:38px;width:900px;line-height:1.35">Comenta <b>QUERO</b> e o nome da sua favorita que eu te mando o link 🤎</div>
<div class="abs" style="left:72px;top:1030px;font-size:28px;color:#5a4a42;width:900px;line-height:1.4">Todas com envio nacional. Preços conferidos hoje; podem mudar.</div>
<div class="abs" style="left:72px;bottom:60px;font-size:26px;color:#6b5a52">Beijo da Arqui 🤎</div>
<div class="abs" style="right:36px;bottom:14px;font-size:20px;color:#3B2A22;opacity:.8">#publi · Fotos: anúncios das lojas</div>
""")

def story(img, title, sub, price):
    return page(1080, 1920, f"""
<div class="abs" style="left:80px;top:200px;font-size:30px;font-weight:700">#publi</div>
<div class="abs h" style="left:80px;top:260px;font-size:84px;width:920px">{title}</div>
<div class="abs" style="left:80px;top:370px;font-size:32px;color:#5a4a42;width:920px;line-height:1.3">{sub}</div>
<div class="abs" style="left:90px;top:470px;width:900px;height:900px;background:url({img}) center/cover;border-radius:8px"></div>
<div class="abs" style="left:80px;top:1410px"><div class="h" style="font-size:72px">{price}</div>
<div style="font-size:30px;margin-top:6px">preço de hoje, pode mudar</div></div>
<div class="abs" style="left:80px;bottom:60px;font-size:26px;color:#6b5a52">@confianaarquiteta</div>
<div class="abs" style="right:80px;bottom:60px;font-size:26px;color:#6b5a52">Foto: anúncio da loja</div>
""")

for i, (name, det, price, img, _) in enumerate(G, start=1):
    ARTS[f"story-{i}"] = story(img, name, det, price)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html in ARTS.items():
            w, h = (1080, 1350) if name.startswith("feed") else (1080, 1920)
            open(f"{name}.html", "w").write(html)
            pg = await b.new_page(viewport={"width": w, "height": h})
            await pg.goto(f"file://{os.getcwd()}/{name}.html")
            await pg.wait_for_timeout(500)
            await pg.screenshot(path=f"../guirlandas-{name}.jpg", type="jpeg", quality=92)
            await pg.close()
            os.remove(f"{name}.html")
        await b.close()
asyncio.run(main())
