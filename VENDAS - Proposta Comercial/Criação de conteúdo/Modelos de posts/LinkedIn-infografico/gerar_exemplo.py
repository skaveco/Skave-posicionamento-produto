import sys
mode=sys.argv[1]
dark=mode=='dark'
c=dict(bg='#252F25',txt='#F8F8F6',sup='#ABB9AB',line='#445644',pill='#F8F8F6',pillt='#252F25') if dark else dict(bg='#F8F8F6',txt='#252F25',sup='#667266',line='#D7D7C9',pill='#252F25',pillt='#F8F8F6')
items=[("Hoje","No CRM: “perdemos no preço”.",True),
("1 semana antes","O cliente comparou três propostas que diziam a mesma coisa.",True),
("3 semanas antes","Na apresentação, o vendedor mostrou tudo que o produto faz.",True),
None,
("1 mês antes","“O que vocês fazem de diferente?” A resposta foi uma lista.",False),
("2 meses antes","O site dizia o mesmo que os concorrentes.",False)]
rows=""
for it in items:
    if it is None:
        rows+=f'<div class="cut"><span class="pill">Aqui a venda começou a ir pro preço</span></div>'
        continue
    w,t,f=it
    rows+=f'<div class="row{"" if f else " early"}"><span class="dot"></span><div><div class="when">{w}</div><div class="what">{t}</div></div></div>'
html=f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
body{{margin:0}}
.p{{width:1080px;height:1350px;background:{c['bg']};color:{c['txt']};font-family:'Instrument Sans',sans-serif;display:flex;align-items:center;justify-content:center}}
.in{{width:864px;display:flex;flex-direction:column;gap:56px}}
.hd{{display:flex;align-items:center;gap:22px}}
.hd img{{width:92px;height:92px;border-radius:50%;object-fit:cover}}
.nm{{display:flex;align-items:center;gap:10px;font-weight:600;font-size:32px}}
.sb{{font-size:26px;color:{c['sup']};margin-top:4px}}
h1{{margin:0;font-weight:600;font-size:52px;line-height:1.2;letter-spacing:-.01em}}
.tl{{position:relative;display:flex;flex-direction:column;gap:34px;padding-left:4px}}
.tl:before{{content:"";position:absolute;left:12px;top:14px;bottom:14px;width:2px;background:{c['line']}}}
.row{{display:flex;gap:34px;align-items:flex-start;position:relative}}
.dot{{width:18px;height:18px;border-radius:50%;background:{c['txt']};flex:none;margin-top:8px;margin-left:-1px;box-shadow:0 0 0 8px {c['bg']}}}
.early .dot{{background:{c['bg']};border:2px solid {c['sup']};width:14px;height:14px}}
.when{{font-size:22px;color:{c['sup']};letter-spacing:.02em}}
.what{{font-size:34px;line-height:1.3;margin-top:4px}}
.cut{{position:relative;padding-left:52px}}
.pill{{display:inline-block;background:{c['pill']};color:{c['pillt']};font-weight:500;font-size:24px;padding:10px 20px;border-radius:999px}}
.end{{font-size:34px;line-height:1.35;font-weight:500;color:{c['txt']}}}
</style></head><body><div class="p"><div class="in">
<div class="hd"><img src="avatar.jpg"><div><div class="nm">Mateus Ritter<svg width="28" height="28" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#4193EF"/><path d="M7 12.5l3.2 3.2L17 9" stroke="#FFF" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div><div class="sb">Posicionamento para SaaS B2B</div></div></div>
<h1>Rebobinando uma venda perdida “no preço”</h1>
<div class="tl">{rows}</div>
<div class="end">O CRM registra o fim da venda. O motivo quase sempre aparece no começo.</div>
</div></div></body></html>'''
open(f'v2-{mode}.html','w').write(html)
