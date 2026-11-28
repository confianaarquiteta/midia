# Stories do sofá Bonnie em montagem de 2 fotos (28/11), imagens oficiais do anúncio.
import asyncio, os
from playwright.async_api import async_playwright
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def st(a, pa, b, pb, ca, cb):
    chip = lambda t: f'<span style="position:absolute;left:24px;bottom:24px;background:rgba(243,237,228,.94);border-radius:10px;padding:10px 18px;font:600 28px Inter,sans-serif;color:#3B2A22">{t}</span>' if t else ''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;overflow:hidden;background:#F3EDE4;position:relative;font-family:Inter,sans-serif;color:#3B2A22}}
.p{{position:absolute;left:40px;width:1000px;height:790px;border-radius:22px;background-size:cover;overflow:hidden}}</style></head><body>
<div style="position:absolute;left:44px;top:96px;font-size:28px;font-weight:700">#publi</div>
<div class="p" style="top:150px;background-image:url({a});background-position:{pa}">{chip(ca)}</div>
<div class="p" style="top:960px;background-image:url({b});background-position:{pb}">{chip(cb)}</div>
<div style="position:absolute;right:44px;bottom:40px;font-size:22px;color:#6b5a52">Fotos: anúncio da loja</div>
</body></html>'''
ARTS = {
 "sofa-collage-1": st("s-sala-fechado.jpg", "center 72%", "s-sala-aberto.jpg", "center 60%", "Fechado", "Aberto"),
 "sofa-collage-2": st("s-aberto.jpg", "center 55%", "s-bau-crop.jpg", "center center", "Assento retrátil", "Baú embaixo"),
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
