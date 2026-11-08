# Authoring module for linden-courtyard-pt-s01e02-scene-04.
ID = 'linden-courtyard-pt-s01e02-scene-04'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 2
SCENE = 4
TITLE = 'Herbs from the Courtyard  (Ervas do pátio)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'graham': 'Graham', 'tessa': 'Tessa', 'hannah': 'Hannah'}
INTRO = 'Na cozinha, Tessa bate os ovos enquanto Graham entra trazendo um punhado de ervas frescas do vaso do pátio e Hannah arruma as quatro mesas. Ouça primeiro.'
OPENER = 'Vamos observar as expressões mais úteis desta cena.'
TRANSITION = 'Agora vamos ouvir toda a cena seguida mais uma vez.'
OUTRO = 'Com um minuto de sobra, as quatro mesas do café estão postas e perfumadas com pão quentinho e ervas frescas. Na próxima cena, os hóspedes descem para comer.'
CLOSING = ('graham', 'See you soon!')
STORY = [
    ('graham', 'I heard shouting about butter from all the way out in the courtyard.', 'Ouvi gritos sobre manteiga lá de fora, do outro lado do pátio.'),
    ('tessa', 'Hannah bought sea salt butter, so today we are making French style eggs!', 'A Hannah comprou manteiga com flor de sal, então hoje vamos fazer ovos ao estilo francês!'),
    ('graham', 'Good. Put these fresh green herbs on top before you serve them.', 'Ótimo. Coloque estas ervas verdes frescas por cima antes de servir.'),
    ('hannah', 'Did you grow those herbs yourself, Graham?', 'Foi você mesmo quem plantou essas ervas, Graham?'),
    ('graham', 'Somebody has to take care of the courtyard plants.', 'Alguém tem que cuidar das plantas do pátio.'),
    ('tessa', 'Smell that! Warm bread, hot eggs, and fresh herbs.', 'Sinta esse cheiro! Pão quentinho, ovos bem quentes e ervas frescas.'),
    ('hannah', 'Where do the small spoons and napkins go?', 'Onde ficam as colherzinhas e os guardanapos?'),
    ('tessa', 'Put one napkin and one small spoon beside every blue cup.', 'Coloque um guardanapo e uma colherzinha ao lado de cada xícara azul.'),
    ('graham', 'Seven twenty-nine on my watch. Guests are coming down the stairs.', 'Sete e vinte e nove no meu relógio. Os hóspedes estão descendo as escadas.'),
    ('hannah', 'Four tables, eight chairs, everything in place!', 'Quatro mesas, oito cadeiras, tudo no lugar!'),
    ('tessa', 'Pour the hot water into the teapot, Hannah, here they come!', 'Despeje a água quente no bule, Hannah, lá vêm eles!'),
    ('graham', 'Not bad for day two, rookie.', 'Nada mal para o segundo dia, novata.'),
]
WALK = [
    (0, None, ["'Ouvi gritos sobre manteiga lá de fora, do outro lado do pátio.' Depois do verbo ouvir, a forma contínua captura o barulho em andamento:", (None, 'I heard shouting'), 'ouvi gritaria.']),
    (1, None, ["'A Hannah comprou manteiga com flor de sal, então hoje vamos fazer ovos ao estilo francês!' Repare no passado irregular", (None, 'bought'), 'do verbo comprar, em que as consoantes do meio não são pronunciadas.']),
    (2, None, ["'Ótimo. Coloque estas ervas verdes frescas por cima antes de servir.' No inglês americano, o agá inicial de", (None, 'herbs'), 'costuma ser mudo, e', (None, 'on top'), "indica 'por cima'."]),
    (3, None, ["'Foi você mesmo quem plantou essas ervas, Graham?' Para enfatizar que a própria pessoa fez algo com as próprias mãos, fecha-se a frase com", (None, 'yourself'), 'você mesmo.']),
    (4, None, ["'Alguém tem que cuidar das plantas do pátio.' Uma locução indispensável para a vida inteira:", (None, 'take care of'), 'cuidar de alguma coisa ou alguém.']),
    (5, None, ["'Sinta esse cheiro! Pão quentinho, ovos bem quentes e ervas frescas.' Veja a diferença sutil de temperatura entre", (None, 'Warm bread'), 'agradavelmente morno, e', (None, 'hot eggs'), 'bem quentes saindo da panela.']),
    (6, None, ["'Onde ficam as colherzinhas e os guardanapos?' Ao arrumar a mesa, perguntar o lugar certo de cada item usa o verbo ir:", (None, 'Where do the small spoons and napkins go'), 'onde vão os talheres.']),
    (7, None, ["'Coloque um guardanapo e uma colherzinha ao lado de cada xícara azul.' A preposição", (None, 'beside'), "significa 'ao lado de', bem prática para descrever posições na mesa."]),
    (8, None, ["'Sete e vinte e nove no meu relógio. Os hóspedes estão descendo as escadas.' Para horas vistas no relógio de pulso usamos", (None, 'on my watch'), 'no meu relógio.']),
    (9, None, ["'Quatro mesas, oito cadeiras, tudo no lugar!' Duas palavras curtas bastam para dizer que tudo está arrumado onde deve:", (None, 'in place'), 'no devido lugar.']),
    (10, None, ["'Despeje a água quente no bule, Hannah, lá vêm eles!' Para servir líquidos dentro de um bule ou copo, o verbo certo é", (None, 'Pour'), 'seguido de', (None, 'into'), 'indicando entrada no recipiente.']),
    (11, None, ["'Nada mal para o segundo dia, novata.' Um elogio bem típico do jeito seco do Graham:", (None, 'Not bad'), 'nada mal, completado por', (None, 'rookie'), 'novata ou estreante.']),
]
