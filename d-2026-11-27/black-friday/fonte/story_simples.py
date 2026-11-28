# Stories simples (28/11): só o produto, uma linha de informação e o preço do dia.
import asyncio, os, importlib.util
from playwright.async_api import async_playwright
os.chdir(os.path.dirname(os.path.abspath(__file__)))
CSS = open('build.py').read().split('CSS = """')[1].split('"""')[0]
def doc(w,h,body): return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS % (w,h)}</style></head><body>{body}</body></html>'
S = {
 "post2-story-v2": ("b", "Aparelho de jantar e chá<br>Ryo Maresia", "20 peças em porcelana · vai na lava-louças", "R$ 280,20", "preço de hoje, pode mudar"),
 "post4-story-v2": ("d", "Aparelho de jantar<br>Porto Brasil Bio Latte", "30 peças em grés · vai no micro-ondas e na lava-louças", "R$ 569,90", "no Pix · preço de hoje, pode mudar"),
}
ARTS = {}
for name,(k,t,sub,price,note) in S.items():
    ARTS[name] = doc(1080,1920,f'''<div class="bg" style="background-image:url({k}.jpg);background-position:center"></div>
<div class="st" style="height:900px"></div>
<div class="abs" style="left:64px;top:170px;font-size:28px;font-weight:700;color:#fff;text-shadow:0 1px 8px rgba(0,0,0,.4)">#publi</div>
<div class="abs" style="left:64px;top:240px;width:950px;color:#fff">
<div class="h" style="font-size:58px">{t}</div>
<div style="font-size:30px;margin-top:14px;opacity:.95">{sub}</div>
<div class="h" style="font-size:76px;margin-top:28px">{price}</div>
<div style="font-size:24px;opacity:.92;margin-top:8px">{note}</div></div>
<div class="abs" style="right:64px;bottom:60px;font-size:22px;color:#fff;opacity:.9">Foto: anúncio da loja</div>''')
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for n,html in ARTS.items():
            open(f"{n}.html","w").write(html)
            pg = await b.new_page(viewport={"width":1080,"height":1920})
            await pg.goto(f"file://{os.getcwd()}/{n}.html"); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f"../{n}.jpg", type="jpeg", quality=92); await pg.close(); os.remove(f"{n}.html")
        await b.close()
asyncio.run(main())
