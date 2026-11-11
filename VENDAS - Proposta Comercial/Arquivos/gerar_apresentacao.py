from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'VENDAS - Proposta Comercial' / 'apresentacao-posicionamento-de-marca.pdf'
W, H = 960, 540
TOTAL = 13

# Rascunho interno: cases e condições comerciais ainda precisam de aprovação.

pdfmetrics.registerFont(TTFont('Arial', '/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', '/System/Library/Fonts/Supplemental/Arial Bold.ttf'))

INK = HexColor('#101114')
MUTED = HexColor('#535761')
FAINT = HexColor('#8c9199')
LINE = HexColor('#dedfe2')
WASH = HexColor('#f7f7f8')
WHITE = HexColor('#ffffff')

c = canvas.Canvas(str(OUTPUT), pagesize=(W, H), pageCompression=1)
c.setTitle('Brand Launch | Skave | Rascunho interno')
c.setAuthor('Skave')
c.setSubject('Apresentação comercial')


def text(x, top, value, size=16, color=INK, bold=False):
    font = 'Arial-Bold' if bold else 'Arial'
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawString(x, H - top - size, value)


def right_text(x, top, value, size=16, color=INK, bold=False):
    font = 'Arial-Bold' if bold else 'Arial'
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawRightString(x, H - top - size, value)


def wrap(value, font, size, width):
    result = []
    for source_line in value.split('\n'):
        if not source_line:
            result.append('')
            continue
        current = ''
        for word in source_line.split():
            trial = word if not current else current + ' ' + word
            if pdfmetrics.stringWidth(trial, font, size) <= width:
                current = trial
            else:
                if current:
                    result.append(current)
                current = word
                if pdfmetrics.stringWidth(current, font, size) > width:
                    raise ValueError(f'Word too wide: {word}')
        result.append(current)
    return result


def para(x, top, width, value, size=16, leading=None, color=INK, bold=False, max_height=None):
    font = 'Arial-Bold' if bold else 'Arial'
    leading = leading or size * 1.34
    rows = wrap(value, font, size, width)
    height = len(rows) * leading
    if max_height is not None and height > max_height:
        raise ValueError(f'Text overflow {height:.1f}>{max_height}: {value}')
    for i, row in enumerate(rows):
        text(x, top + i * leading, row, size, color, bold)
    return height


def box(x, top, width, height, fill=WHITE, stroke=LINE, radius=13):
    c.setLineWidth(1)
    c.setStrokeColor(stroke)
    c.setFillColor(fill)
    c.roundRect(x, H - top - height, width, height, radius, fill=1, stroke=1)


def rule(x1, x2, top, color=LINE, width=1):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x1, H - top, x2, H - top)


def header(label):
    text(56, 38, label.upper(), 10.5, MUTED, True)


def footer(page, reserve=False):
    rule(56, 904, 499)
    text(56, 509, 'SKAVE  /  BRAND LAUNCH  /  RASCUNHO INTERNO', 9, FAINT, True)
    text(869, 509, f'{page:02d} / {TOTAL:02d}', 9, FAINT, True)


def finish(page, reserve=False):
    footer(page, reserve)
    c.showPage()


def small_card(x, top, width, height, title, body, number=None):
    box(x, top, width, height)
    tx = x + 17
    if number:
        text(tx, top + 12, number, 10, FAINT, True)
        title_top = top + 30
        body_top = top + 54
    else:
        title_top = top + 13
        body_top = top + 39
    text(tx, title_top, title, 15, INK, True)
    para(tx, body_top, width - 34, body, 11.7, 15, MUTED, max_height=height - (body_top - top) - 9)



def title(label, value):
    header(label)
    para(56, 86, 848, value, 34, 41, INK, True, 92)


def cards(items, top=220):
    for i,(label,body) in enumerate(items):
        small_card(56+i*288, top, 272, 220, label, body, f'{i+1:02d}')


def table(headers, rows, widths, top=190, heights=None, size=13):
    x=56
    for label,width in zip(headers,widths):
        box(x,top,width,38,WASH,radius=0)
        text(x+12,top+10,label,12,INK,True); x+=width
    y=top+38
    for i,row in enumerate(rows):
        h=heights[i] if heights else 54
        x=56
        for j,(value,width) in enumerate(zip(row,widths)):
            box(x,y,width,h,WHITE,radius=0)
            para(x+12,y+10,width-24,value,size,size*1.3,INK if j==0 else MUTED,j==0,h-15)
            x+=width
        y+=h
    assert y<490,y

text(56,42,'SKAVE',21,INK,True)
rule(56,904,85)
para(56,150,848,'Posicionamento\nde Marca',58,68,INK,True,145)
text(58,312,'Brand Launch · Proposta para [cliente]',23,MUTED)
text(58,397,'Uma marca que comunica o valor do seu software.',18,INK)
text(58,451,'6 DE NOVEMBRO DE 2026',11,MUTED,True)
finish(1)

title('A Skave','Posicionamento e tecnologia,\nda criação à evolução.')
para(56,181,848,'Construímos marcas preparadas para ganhar vida no digital e evoluir com o negócio.',17,23,MUTED,max_height=50)
cards([('Estratégia','Entendemos negócio, público e mercado para definir uma direção clara.'),('Identidade','Transformamos a direção em expressão visual e verbal coerente.'),('Tecnologia','Ajudamos a aplicar e desenvolver a marca em experiências digitais.')],250)
finish(2)

title('Qualificação','O Brand Launch faz sentido para você?')
table(['É INDICADO QUANDO','AVALIAR OUTRO CAMINHO QUANDO'],[
('O negócio digital precisa do primeiro posicionamento, mesmo que já opere e venda.','A marca estabelecida precisa rever uma direção anterior. Avaliar Brand Evolution.'),
('Oferta, público inicial e problema atendido estão suficientemente compreendidos.','A prioridade ainda é descobrir a viabilidade da oferta ou do modelo de negócio.'),
('Lideranças podem participar da investigação e aprovar decisões.','A necessidade é apenas logo, peças avulsas ou gestão contínua de marketing.')],[424,424],185,[86,86,86],15)
finish(3)

title('Ponto de partida','O que entendemos sobre a sua marca')
para(56,177,848,'O produto já está no mercado. Como seu valor aparece na comunicação?',19,26,MUTED,max_height=55)
cards([('O que já existe','[Fato confirmado sobre produto, clientes e operação.]'),('O que observamos','[Exemplo concreto no site, nas redes ou nos materiais comerciais, com fonte.]'),('O que validar','[Hipótese sobre clareza, diferenciação ou coerência a confirmar com o cliente.]')],245)
finish(4)

title('O desafio','Ser entendido e escolhido\npelo valor certo')
para(56,181,848,'Seu comprador entende para quem o software é, que valor entrega e por que escolhê-lo?',19,26,MUTED,max_height=60)
cards([('Clareza','O benefício depende de uma explicação longa.'),('Diferenciação','A mensagem se parece com a das alternativas.'),('Coerência','Os canais e o comercial apresentam versões diferentes da empresa.')],250)
finish(5)

title('A proposta','Definir a direção e colocá-la em uso')
para(56,162,848,'Construiremos o primeiro posicionamento e o traduziremos em identidade, aplicações digitais e ferramentas para a equipe continuar.',19,26,MUTED,max_height=70)
cards([('Direção','Público prioritário, posicionamento, proposta de valor e diferenciais.'),('Expressão','Identidade visual e princípios de comunicação coerentes com a estratégia.'),('Aplicação','Primeiras peças nos canais escolhidos e recursos para manter consistência.')],245)
finish(6)

title('O caminho','11 semanas, da investigação à entrega')
table(['PERÍODO','TRABALHO E RESULTADO'],[
('Semanas 1–5','Imersão, mercado e estratégia. Posicionamento aprovado e Brand Strategy Book consolidado.'),
('Semanas 6–9','Alinhamento, desenvolvimento e aprovação da identidade visual.'),
('Semana 10','Manual e primeiras ativações digitais validados.'),
('Semana 11','Duas Skills, vídeo de treinamento e entrega final.'),
('Após a entrega','2 meses de orientação para aplicação da marca e uso das Skills.')],[170,678],166,[57,48,48,48,48],14)
text(56,467,'Calendário condicionado às devolutivas e à manutenção do escopo aprovado.',11,MUTED)
finish(7)

title('O que está incluído','Uma entrega integrada')
table(['FRENTE','ENTREGA AO CLIENTE'],[
('Estratégia','Apresentação de 13 slides + Brand Strategy Book de 22 páginas em PDF.'),
('Identidade visual','Sistema visual, aplicações demonstrativas, manual e arquivos finais.'),
('Ativação digital','Instagram + um canal escolhido; três posts estáticos de imagem única somente no Instagram, com texto da arte e sugestão de legenda.'),
('Continuidade','Duas Skills em Markdown: estratégia e conteúdo; vídeo de treinamento.'),
('Acompanhamento','2 meses de orientação após a entrega.')],[170,678],164,[49,49,72,49,45],14)
finish(8)

title('Evidência','Um trabalho real que mostre o método')
para(56,169,848,'[Case a selecionar: cliente, desafio documentado e escopo realmente executado.]',17,23,MUTED,max_height=55)
cards([('Desafio','[Situação inicial e evidência do problema de marca.]'),('Direção','[Definição estratégica e imagem da identidade desenvolvida.]'),('Aplicação','[Ponto de contato real e autorizado da marca.]')],244)
finish(9)

title('Como trabalharemos juntos','Decisões claras em cada etapa')
items=[('Skave','Investiga, recomenda a estratégia, cria a identidade e prepara as aplicações.'),('Cliente','Fornece informações, reúne decisores, consolida feedback e publica os conteúdos.'),('Aprovações','Uma rodada em estratégia, alinhamento visual, identidade e ativações. Retorno em até 3 dias úteis e aprovação expressa.'),('Acompanhamento','Uma reunião por mês, por 2 meses. WhatsApp em dias úteis, com resposta em até 1 dia útil.')]
for i,(label,body) in enumerate(items):
    small_card(56+(i%2)*433,167+(i//2)*136,415,123,label,body)
para(56,452,848,'Naming, site e landing page têm escopo próprio. Gestão de redes, conteúdo recorrente e novas peças não estão incluídos.',11,15,MUTED,max_height=32)
finish(10)

title('Investimento','Condição para este projeto')
text(56,183,'[VALOR APROVADO]',46,INK,True)
para(56,260,848,'[Pagamento: parcelas, vencimentos e total conferidos.]',20,27,MUTED,max_height=60)
box(56,350,848,104,WASH)
text(76,367,'11 semanas de execução + 2 meses de acompanhamento',20,INK,True)
text(76,409,'Condições comerciais ainda em definição. Preencher antes do envio.',13,MUTED)
finish(11)

title('Próximo passo','Vamos construir uma marca que\nmostre o valor de [cliente]?')
cards([('Confirmar','Alinhar escopo, segundo canal e condição comercial.'),('Formalizar','Aprovar a proposta e assinar o contrato.'),('Iniciar','Agendar kickoff e Escavação.')],235)
finish(12)

title('Comparativo final','Brand Launch × Start')
para(56,145,848,'Start é uma alternativa de escopo reduzido quando o projeto completo não for viável.',14,20,MUTED,max_height=28)
table(['ENTREGA','BRAND LAUNCH','START'],[
('Estratégia','Primeiro posicionamento; apresentação + Book.','Análise inicial, proposta de valor, personalidade e tom de voz.'),
('Posicionamento\ne diferenciais','Definições específicas incluídas.','Não previstos como entregas específicas.'),
('Identidade','Sistema, aplicações, manual e arquivos finais.','Identidade, aplicações de referência e manual.'),
('Ativação','Instagram + 1 canal; três posts somente no Instagram.','Não incluída.'),
('Skills','Duas Skills em Markdown + vídeo de treinamento.','Não incluídas.'),
('Prazo e apoio','11 semanas + 2 meses de acompanhamento.','Estratégia: 2 semanas; design: 30 dias; apoio: 60 dias.')],[154,347,347],174,[46,44,44,44,44,46],11)
finish(13)

c.save()
print(OUTPUT)
