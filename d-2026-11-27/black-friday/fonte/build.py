import asyncio, os
from playwright.async_api import async_playwright
os.chdir(os.path.dirname(os.path.abspath(__file__)))

CSS = """@font-face{font-family:Fraunces;src:url(fraunces-latin-600-normal.woff2);font-weight:600}
*{margin:0;padding:0;box-sizing:border-box}
body{width:%dpx;height:%dpx;overflow:hidden;font-family:Inter,sans-serif;background:#F3EDE4;color:#3B2A22;position:relative}
.bg{position:absolute;inset:0;background-size:cover}
.h{font-family:Fraunces,serif;font-weight:600;line-height:1.08;letter-spacing:-0.5px}
.abs{position:absolute}
.pill{display:inline-block;background:#A55A41;color:#F3EDE4;border-radius:40px;padding:12px 28px;font-weight:700;letter-spacing:4px;font-size:24px}
.off{display:inline-block;background:#A55A41;color:#fff;border-radius:10px;padding:8px 16px;font-weight:700;font-size:28px;vertical-align:middle;margin-left:14px}
.st{position:absolute;left:0;right:0;top:0;background:linear-gradient(rgba(30,20,15,.66),rgba(30,20,15,0))}
.sb{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(rgba(30,20,15,0),rgba(30,20,15,.7))}
"""

def doc(w, h, body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS % (w, h)}</style></head><body>{body}</body></html>'

# itens (dados conferidos no anúncio em 27/11/2026)
I = {
 "a": dict(name="Árvore de Natal de 1,50 m", sub="pinheiro canadense com 450 galhos", price="R$ 89,91", off="55% OFF", pnote="no Pix · preço de hoje, pode mudar", pos="center", dark=False),
 "b": dict(name="Aparelho de jantar e chá", sub="20 peças em porcelana, linha Ryo Maresia", price="R$ 280,20", off="53% OFF", pnote="preço de hoje, pode mudar", pos="center", dark=False),
 "c": dict(name="Câmera inteligente 360°", sub="Wi-Fi, visão noturna e áudio nos dois sentidos", price="R$ 169,91", off="47% OFF", pnote="no Pix · preço de hoje, pode mudar", pos="center", dark=True),
 "d": dict(name="Aparelho de jantar 30 peças", sub="grés off-white com acabamento manual", price="R$ 499,90", off="", pnote="em 9x sem juros · preço de hoje, pode mudar", pos="center", dark=False),
 "e": dict(name="Sofá retrátil de 2 m em bouclê", sub="vira cama de casal e tem baú", price="R$ 2.571", off="", pnote="ou R$ 2.511,89 com cupom · preço de hoje, pode mudar", pos="center", dark=True),
}
COVER = {
 "a": "A árvore cheia<br>por menos de R$ 90",
 "b": "Mesa posta com cara<br>de loja de decoração",
 "c": "A casa de olho,<br>mesmo de longe",
 "d": "Louça com<br>cara de ateliê",
 "e": "O sofá bouclê<br>que vira cama",
}
ORDER = "abcde"

def price_block(it, size=76):
    off = f'<span class="off">{it["off"]}</span>' if it["off"] else ""
    return f'''<div class="h" style="font-size:{size}px;color:#fff">{it["price"]}{off}</div>
<div style="font-size:24px;color:#fff;opacity:.92;margin-top:8px">{it["pnote"]}</div>'''

def cover(k, w=1080, h=1350, story=False):
    it = I[k]; col = "#3B2A22" if it["dark"] else "#fff"
    st = "" if it["dark"] else '<div class="st" style="height:620px"></div>'
    top = 230 if story else 72
    foot = '' if story else '<div class="abs" style="right:64px;bottom:40px;font-size:22px;color:#fff;opacity:.9">#publi · Foto: anúncio da loja</div>'
    more = '' if story else '<div style="font-size:26px;color:#fff;margin-top:18px;font-weight:600">+ 4 escolhas da Arqui com desconto · arrasta →</div>'
    bottom = 340 if story else 90
    pubstory = '<div class="abs" style="left:64px;top:170px;font-size:28px;font-weight:700;color:%s">#publi</div>' % col if story else ''
    credit = '<div class="abs" style="right:64px;bottom:300px;font-size:22px;color:#fff;opacity:.9">Foto: anúncio da loja</div>' if story else ''
    return doc(w, h, f'''<div class="bg" style="background-image:url({k}.jpg);background-position:{it["pos"]}"></div>
{st}<div class="sb" style="height:{760 if story else 600}px"></div>{pubstory}
<div class="abs" style="left:64px;top:{top}px"><span class="pill">BLACK FRIDAY DA ARQUI</span></div>
<div class="abs h" style="left:64px;top:{top+90}px;font-size:{80 if story else 78}px;width:{w-120}px;color:{col}">{COVER[k]}</div>
<div class="abs" style="left:64px;bottom:{bottom}px;width:{w-128}px">
<div style="font-size:32px;color:#fff;font-weight:600;margin-bottom:10px">{it["name"]}</div>
{price_block(it)}{more}</div>{foot}{credit}''')

def item_slide(k):
    it = I[k]; col = "#3B2A22" if it["dark"] else "#fff"
    st = "" if it["dark"] else '<div class="st" style="height:420px"></div>'
    return doc(1080, 1350, f'''<div class="bg" style="background-image:url({k}.jpg);background-position:{it["pos"]}"></div>
{st}<div class="sb" style="height:520px"></div>
<div class="abs h" style="left:64px;top:64px;font-size:62px;width:950px;color:{col}">{it["name"]}</div>
<div class="abs" style="left:64px;top:{64+80}px;font-size:28px;font-weight:500;width:900px;color:{col}">{it["sub"]}</div>
<div class="abs" style="left:64px;bottom:90px">{price_block(it)}</div>
<div class="abs" style="right:64px;bottom:40px;font-size:22px;color:#fff;opacity:.9">#publi · Foto: anúncio da loja</div>''')

CTA = doc(1080, 1350, '''<div class="abs" style="inset:0;background:#A55A41"></div>
<div class="abs h" style="left:90px;top:420px;font-size:96px;color:#F3EDE4;width:900px">Gostou de<br>alguma peça?</div>
<div class="abs" style="left:90px;top:680px;font-size:44px;color:#F3EDE4;width:880px;line-height:1.3">Comenta QUERO e o nome da peça que eu te mando o link 🤎</div>
<div class="abs" style="left:90px;top:880px;font-size:28px;color:#F3EDE4;opacity:.85;width:880px;line-height:1.4">Preços conferidos hoje no anúncio.<br>Podem mudar a qualquer momento.</div>
<div class="abs" style="left:90px;bottom:60px;font-size:24px;color:#F3EDE4;opacity:.8">@confianaarquiteta</div>
<div class="abs" style="right:90px;bottom:60px;font-size:24px;color:#F3EDE4;opacity:.8">#publi</div>''')

ARTS = {}
for n, k in enumerate(ORDER, 1):
    ARTS[f"post{n}-01"] = (cover(k), 1080, 1350)
    others = [o for o in ORDER if o != k]
    for j, o in enumerate(others, 2):
        ARTS[f"post{n}-{j:02d}"] = (item_slide(o), 1080, 1350)
    ARTS[f"post{n}-06"] = (CTA, 1080, 1350)
    ARTS[f"post{n}-story"] = (cover(k, 1080, 1920, story=True), 1080, 1920)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        done = {}
        for name, (html, w, h) in ARTS.items():
            open(f"{name}.html", "w").write(html)
            pg = await b.new_page(viewport={"width": w, "height": h})
            await pg.goto(f"file://{os.getcwd()}/{name}.html")
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"{name}.jpg", type="jpeg", quality=92)
            await pg.close()
        await b.close()
asyncio.run(main())
