# Story do Ryo Maresia com foto que mostra mais as peças (28/11)
import asyncio, os
from playwright.async_api import async_playwright
os.chdir(os.path.dirname(os.path.abspath(__file__)))
CSS = open('build.py').read().split('CSS = """')[1].split('"""')[0]
def doc(body): return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS % (1080,1920)}</style></head><body>{body}</body></html>'
def st(img): return doc(f'''
<div class="abs" style="left:80px;top:200px;font-size:30px;font-weight:700">#publi</div>
<div class="abs h" style="left:80px;top:260px;font-size:72px;width:920px">Aparelho de jantar e chá<br>Ryo Maresia</div>
<div class="abs" style="left:80px;top:440px;font-size:32px;color:#5a4a42">20 peças em porcelana · vai na lava-louças</div>
<div class="abs" style="left:0;top:530px;width:1080px;height:1080px;background:url({img}) center/cover"></div>
<div class="abs" style="left:80px;top:1640px"><div class="h" style="font-size:72px">R$ 280,20</div>
<div style="font-size:28px;margin-top:6px">preço de hoje, pode mudar</div></div>
<div class="abs" style="right:80px;bottom:60px;font-size:24px;color:#6b5a52">Foto: anúncio da loja</div>''')
ARTS={"post2-story-v3a":st("b2.jpg"),"post2-story-v3b":st("b3.jpg")}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for n,h in ARTS.items():
            open(f"{n}.html","w").write(h); pg=await b.new_page(viewport={"width":1080,"height":1920})
            await pg.goto(f"file://{os.getcwd()}/{n}.html"); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f"../{n}.jpg",type="jpeg",quality=92); await pg.close(); os.remove(f"{n}.html")
        await b.close()
asyncio.run(main())
