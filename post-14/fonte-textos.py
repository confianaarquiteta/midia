import sys
tpl='''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
@font-face{{font-family:'Fraunces';font-weight:600;src:url('fraunces-latin-600-normal.woff2') format('woff2');}}
body{{margin:0}}
.root{{width:1080px;height:1350px;box-sizing:border-box;padding:88px;position:relative;overflow:hidden;background:{bg};color:{fg};font-family:'Inter',Arial,sans-serif;display:flex;flex-direction:column}}
.arco{{position:absolute;left:520px;top:330px;width:700px;height:1100px;border-radius:350px 350px 0 0;background:{arco};opacity:.55}}
.selo{{position:relative;align-self:flex-start;background:#A55A41;color:#fff;font-weight:700;font-size:26px;letter-spacing:3px;padding:14px 28px;border-radius:999px}}
.mid{{position:relative;flex-grow:1;display:flex;flex-direction:column;justify-content:{just};gap:32px}}
.lab{{margin:0;font-size:28px;font-weight:700;letter-spacing:3px;color:{lab}}}
h1{{margin:0;font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:{hs}px;line-height:1.08}}
p{{margin:0;font-size:42px;line-height:1.4}}
.item{{display:flex;flex-direction:column;gap:6px;padding:26px 0;border-top:3px solid #D6BFA6}}
.item b{{font-family:'Fraunces',Georgia,serif;font-size:54px;color:#9A4F37}}
.item span{{font-size:36px;line-height:1.35}}
.handle{{position:relative;font-size:26px;font-weight:500;margin-top:40px}}
</style></head><body><div class="root"><div class="arco"></div>{selo}<div class="mid">{body}</div><span class="handle">@confianaarquiteta</span></div></body></html>'''
def w(name, **k): open(name,'w',encoding='utf-8').write(tpl.format(**k))
selo='<span class="selo">DICA DA ARQUI</span>'
w('mesa/02.html',bg='#F3EDE4',fg='#3B2A22',arco='#D6BFA6',lab='#9A4F37',just='center',hs=92,selo=selo,
  body='<p class="lab">A RESPOSTA DA ARQUI</p><p>Sei que a toalha é comum em muitas casas, sendo prática no dia a dia, durante as refeições.</p><h1>Mas, para decoração, a mesa fica à mostra.</h1>')
w('mesa/03.html',bg='#F3EDE4',fg='#3B2A22',arco='#D6BFA6',lab='#9A4F37',just='center',hs=84,selo=selo,
  body='<p class="lab">O QUE SE USA NO LUGAR</p><p>Como opção, pode-se usar jogo americano, caminho de mesa e sousplat.</p><div><div class="item"><b>Jogo americano</b><span>Um por lugar, no dia a dia.</span></div><div class="item"><b>Caminho de mesa</b><span>No centro, para receber.</span></div><div class="item"><b>Sousplat</b><span>Embaixo do prato, para ocasiões especiais.</span></div></div>')
w('mesa/10.html',bg='#A55A41',fg='#FFFFFF',arco='#B5654A',lab='#F3EDE4',just='flex-end',hs=108,selo='',
  body='<h1>Você ainda usa toalha de mesa?</h1><p>Conta pra Arqui nos comentários.</p><p><b>Envia para quem ainda esconde<br>a mesa embaixo da toalha.</b></p>')
