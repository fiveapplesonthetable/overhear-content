# Authoring module for linden-courtyard-pt-s01e06-scene-08.
ID = 'linden-courtyard-pt-s01e06-scene-08'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 6
SCENE = 8
TITLE = 'Room Nine  (O quarto nove)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = 'Já tarde na noite de sexta-feira, depois que o pátio esvazia, Hannah e Arthur fecham a recepção quando Graham sobe do porão dos fundos trazendo cadeiras extras e uma caixa de madeira empoeirada. Vamos ouvir.'
OPENER = 'Vamos repassar com calma a cena final da primeira temporada.'
TRANSITION = 'Agora ouça pela última vez toda a cena em velocidade natural.'
OUTRO = 'Uma nona chave de latão, um baú de cedro marcado Quarto Nove e uma planta mostrando uma porta escondida neste andar! Você concluiu a primeira temporada da pousada Linden Courtyard Inn. Até a segunda temporada!'
CLOSING = ('graham', 'Until tomorrow!')
STORY = [
    ('hannah', 'Did you find the three folding chairs behind the boiler room, Graham?', 'Você achou as três cadeiras dobráveis atrás da sala da caldeira, Graham?'),
    ('graham', 'Found the chairs, and behind an old brick wall, I found this.', 'Achei as cadeiras e, atrás de uma velha parede de tijolos, achei isto.'),
    ('arthur', 'A small cedar chest? I have never seen that box in fifteen years!', 'Um pequeno baú de cedro? Eu nunca vi essa caixa em quinze anos!'),
    ('hannah', 'Brush the dust off the brass plate on top... wait, read that number!', 'Limpe a poeira da plaquinha de latão em cima... espere, leia esse número!'),
    ('arthur', "Let me pull my glasses down from my forehead... 'Room Nine'?!", "Deixe eu puxar meus óculos da testa para baixo... 'Quarto Nove'?!"),
    ('hannah', 'Graham, look at the wooden key board behind us: one, two, three, four, five, six, seven, eight!', 'Graham, olhe para o quadro de madeira de chaves atrás de nós: um, dois, três, quatro, cinco, seis, sete, oito!'),
    ('arthur', 'This guesthouse has only ever had eight rooms! Where on earth is Room Nine?!', 'Esta pousada sempre teve apenas oito quartos! Onde neste mundo fica o Quarto Nove?!'),
    ('graham', 'Listen when I tilt the box. Something metal just slid inside.', 'Escutem quando eu inclino a caixa. Alguma coisa de metal acabou de deslizar lá dentro.'),
    ('hannah', 'There is a tiny keyhole on the front latch, and look taped underneath: an old brass key!', 'Tem um buraquinho de fechadura no fecho da frente, e olhem colada com fita embaixo: uma velha chave de latão!'),
    ('arthur', 'A ninth brass key?! Do we open it tonight or wait until morning?!', 'Uma nona chave de latão?! Nós abrimos hoje à noite ou esperamos até amanhã cedo?!'),
    ('graham', 'Look at the folded blueprint sticking out of the hinge. There is a hidden door drawn on this floor!', 'Olhem a planta dobrada saindo pela dobradiça. Tem uma porta escondida desenhada neste andar!'),
    ('hannah', 'Grab the flashlight, both of you. My second week starts right now!', 'Peguem a lanterna, vocês dois. Minha segunda semana começa agora mesmo!'),
]
WALK = [
    (0, None, ["'Você achou as três cadeiras dobráveis atrás da sala da caldeira, Graham?' Em", (None, 'folding chairs'), "o '-ing' indica a função do móvel: cadeiras dobráveis."]),
    (1, None, ["'Achei as cadeiras e, atrás de uma velha parede de tijolos, achei isto.' Na fala curta e prática de Graham, ele omite o 'I' inicial em", (None, 'Found the chairs'), 'achei as cadeiras.']),
    (2, None, ["'Um pequeno baú de cedro? Eu nunca vi essa caixa em quinze anos!' Para falar de toda a experiência até o presente, usamos", (None, 'I have never seen'), 'eu nunca vi.']),
    (3, None, ["'Limpe a poeira da plaquinha de latão em cima... espere, leia esse número!' A partícula 'off' em", (None, 'Brush the dust off'), 'mostra tirar a poeira de cima da superfície.']),
    (4, None, ["'Deixe eu puxar meus óculos da testa para baixo... Quarto Nove?!' Veja o movimento desenhado com clareza em", (None, 'pull my glasses down from'), 'puxar para baixo tirando da testa.']),
    (5, None, ["'Graham, olhe para o quadro de madeira de chaves atrás de nós: um, dois, três, quatro, cinco, seis, sete, oito!' Depois de preposição usamos o pronome oblíquo:", (None, 'behind us'), 'atrás de nós.']),
    (6, None, ["'Esta pousada sempre teve apenas oito quartos! Onde neste mundo fica o Quarto Nove?!' Para mostrar espanto total sem usar gíria pesada, pergunte", (None, 'Where on earth'), 'onde neste mundo?']),
    (7, None, ["'Escutem quando eu inclino a caixa. Alguma coisa de metal acabou de deslizar lá dentro.' Assim como os adjetivos, o material vem depois de 'something':", (None, 'Something metal'), 'algo metálico.']),
    (8, None, ["'Tem um buraquinho de fechadura no fecho da frente, e olhem colada com fita embaixo: uma velha chave de latão!' A palavra composta", (None, 'keyhole'), "junta 'chave' e 'buraco' para o buraco da fechadura."]),
    (9, None, ["'Uma nona chave de latão?! Nós abrimos hoje à noite ou esperamos até amanhã cedo?!' De 'nine' forma-se o ordinal", (None, 'ninth'), "perdendo a letra 'e' na grafia."]),
    (10, None, ["'Olhem a planta dobrada saindo pela dobradiça. Tem uma porta escondida desenhada neste andar!' O verbo com partícula", (None, 'sticking out of'), 'descreve uma ponta de papel escapando pela fresta.']),
    (11, None, ["'Peguem a lanterna, vocês dois. Minha segunda semana começa agora mesmo!' Cheio de energia de aventura,", (None, 'starts right now'), 'encerra a temporada deixando o mistério no ar!']),
]
