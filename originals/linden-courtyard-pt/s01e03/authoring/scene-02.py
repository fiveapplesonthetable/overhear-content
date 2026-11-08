# Authoring module for linden-courtyard-pt-s01e03-scene-02.
ID = 'linden-courtyard-pt-s01e03-scene-02'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = 'The Sunny Attic  (O sótão ensolarado)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = 'Lá em cima, sob o telhado de madeira do terceiro andar, Graham destranca o sótão para Hannah enquanto Tessa sobe trazendo toalhas limpas. Vamos ouvir a cena inteira primeiro.'
OPENER = 'Agora vamos passar por cada fala passo a passo.'
TRANSITION = 'Vamos escutar toda a conversa de novo sem pausas.'
OUTRO = 'Com vigas de madeira e chuva no telhado, o sótão só precisa de uma luminária, dois travesseiros e um tapete. Até a próxima cena nessa corrida contra o relógio.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('hannah', 'Oh, look at this room! Big wooden beams and a window over the courtyard!', 'Ah, olhe este quarto! Grandes vigas de madeira e uma janela voltada para o pátio!'),
    ('tessa', 'Listen to the rain on the roof. It feels so cozy up here!', 'Escute a chuva no telhado. Parece tão aconchegante aqui em cima!'),
    ('graham', 'Dry, warm, and quiet. Now tell me what is missing.', 'Seco, quentinho e silencioso. Agora me diga o que está faltando.'),
    ('hannah', 'Okay: there is a bed, a table, and a chair, but no bedside lamp.', 'Certo: tem uma cama, uma mesa e uma cadeira, mas nenhuma luminária de cabeceira.'),
    ('tessa', 'And no mirror on the wall, and the floor feels bare without a rug.', 'E nenhum espelho na parede, e o chão parece vazio sem um tapete.'),
    ('graham', 'There is a brass reading lamp in my workshop downstairs.', 'Tem uma luminária de leitura de latão na minha oficina lá embaixo.'),
    ('tessa', 'And I have two soft pillows and a woven blue rug in the closet!', 'E eu tenho dois travesseiros macios e um tapete azul tecido no armário!'),
    ('hannah', 'What about the small bathroom next door? Does the light work?', 'E quanto ao banheiro pequeno aqui ao lado? A luz funciona?'),
    ('graham', 'New bulb last week, clean soap, plenty of hot water.', 'Lâmpada nova na semana passada, sabonete limpo e bastante água quente.'),
    ('tessa', 'Give us fifteen minutes and this attic will beat room seven!', 'Dê quinze minutos para nós e este sótão vai ganhar do quarto sete!'),
    ('hannah', 'Grab those cardboard boxes, Graham. Down the stairs we go!', 'Pegue essas caixas de papelão, Graham. Descendo a escada!'),
    ('graham', 'Careful on the turn, do not bump the wall!', 'Cuidado na curva, não bata na parede!'),
]
WALK = [
    (0, None, ["'Ah, olhe este quarto! Grandes vigas de madeira e uma janela voltada para o pátio!' Para pedir que alguém olhe para algo específico, o verbo pede preposição:", (None, 'look at this room'), 'olhe para este quarto.']),
    (1, None, ["'Escute a chuva no telhado. Parece tão aconchegante aqui em cima!' O mesmo acontece ao ouvir com atenção:", (None, 'Listen to the rain'), "sempre leva 'to' antes do som."]),
    (2, None, ["'Seco, quentinho e silencioso. Agora me diga o que está faltando.' Em perguntas embutidas no meio da frase,", (None, 'what is missing'), 'segue na ordem normal de afirmação.']),
    (3, None, ["'Certo: tem uma cama, uma mesa e uma cadeira, mas nenhuma luminária de cabeceira.' Onde dizemos 'tem' para indicar existência, o inglês usa", (None, 'there is a bed'), 'no singular quando o primeiro item é singular.']),
    (4, None, ["'E nenhum espelho na parede, e o chão parece vazio sem um tapete.' Para objetos apoiados ou pendurados numa superfície como a parede, usa-se", (None, 'on the wall'), 'na parede.']),
    (5, None, ["'Tem uma luminária de leitura de latão na minha oficina lá embaixo.' Uma única palavra,", (None, 'downstairs'), "expressa 'no andar de baixo' sem precisar de preposição."]),
    (6, None, ["'E eu tenho dois travesseiros macios e um tapete azul tecido no armário!' A forma", (None, 'woven'), 'vem do verbo tecer e funciona como adjetivo para mostrar um tapete artesanal.']),
    (7, None, ["'E quanto ao banheiro pequeno aqui ao lado? A luz funciona?' Para puxar outro ponto prático na conversa,", (None, 'What about'), "equivale ao nosso 'e quanto a...?'."]),
    (8, None, ["'Lâmpada nova na semana passada, sabonete limpo e bastante água quente.' Para dizer que há mais do que suficiente de algo, use", (None, 'plenty of hot water'), 'bastante água quente.']),
    (9, None, ["'Dê quinze minutos para nós e este sótão vai ganhar do quarto sete!' Aqui", (None, 'will beat'), 'significa superar ou sair melhor do que o outro quarto.']),
    (10, None, ["'Pegue essas caixas de papelão, Graham. Descendo a escada!' Jogar a direção para o começo da frase em", (None, 'Down the stairs we go'), 'dá um ritmo animado de movimento.']),
    (11, None, ["'Cuidado na curva, não bata na parede!' Para avisos negativos rápidos usamos", (None, 'do not bump'), "seguido direto do objeto, sem preposição 'em'."]),
]
