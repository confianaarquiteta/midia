# Stories do sofá Bonnie (28/11): montagem com imagens oficiais do anúncio, para postar depois do vídeo.
import asyncio, os
from playwright.async_api import async_playwright
os.chdir(os.path.dirname(os.path.abspath(__file__)))
CSS = """@font-face{font-family:Fraunces;src:url(fraunces-latin-600-normal.woff2);font-weight:600}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;font-family:Inter,sans-serif;background:#F3EDE4;color:#3B2A22;position:relative}
.h{font-family:Fraunces,serif;font-weight:600;line-height:1.08;letter-spacing:-0.5px}.abs{position:absolute}"""
def st(img, title, sub):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="abs" style="left:80px;top:200px;font-size:30px;font-weight:700">#publi</div>
<div class="abs h" style="left:80px;top:260px;font-size:80px;width:920px">{title}</div>
<div class="abs" style="left:80px;top:370px;font-size:34px;color:#5a4a42;width:920px">{sub}</div>
<div class="abs" style="left:40px;top:470px;width:1000px;height:1000px;background:#fff url({img}) center/contain no-repeat;border-radius:16px"></div>
<div class="abs" style="left:80px;top:1510px"><div style="font-size:30px;font-weight:600">Sofá retrátil Bonnie 2,00 m em bouclê</div>
<div class="h" style="font-size:64px;margin-top:10px">R$ 2.769</div>
<div style="font-size:26px;margin-top:6px">preço de hoje, pode mudar</div></div>
<div class="abs" style="right:80px;bottom:60px;font-size:24px;color:#6b5a52">Foto: anúncio da loja</div>
</body></html>'''
ARTS = {
 "sofa-story-1": st("s-aberto.jpg", "Assento retrátil", "puxa para a frente e o sofá fica mais fundo"),
 "sofa-story-2": st("s-multi.jpg", "Sofá, cama e baú", "vira cama de casal e guarda tudo embaixo"),
 "sofa-story-3": st("s-bau.jpg", "Baú embaixo do assento", "espaço extra para organizar a sala"),
}
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for n, h in ARTS.items():
            open(f"{n}.html","w").write(h); pg = await b.new_page(viewport={"width":1080,"height":1920})
            await pg.goto(f"file://{os.getcwd()}/{n}.html"); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f"../{n}.jpg", type="jpeg", quality=92); await pg.close(); os.remove(f"{n}.html")
        await b.close()
asyncio.run(main())
