# Authoring module for linden-courtyard-pt-s01e06-scene-06.
ID = 'linden-courtyard-pt-s01e06-scene-06'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 6
SCENE = 6
TITLE = 'Permanent Keys  (Chaves permanentes)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'arthur': 'Arthur', 'tessa': 'Tessa', 'hannah': 'Hannah'}
INTRO = 'No cantinho ensolarado do café, Arthur fica de pé todo orgulhoso diante de Tessa e Hannah, ainda segurando a página dois da carta com um sorriso de orelha a orelha. Vamos ouvir.'
OPENER = 'Vamos conferir frase por frase estas ótimas notícias.'
TRANSITION = 'Ouça novamente a cena inteira no ritmo normal.'
OUTRO = 'Um café aberto à vizinhança no pátio para Tessa e a vaga efetiva na recepção para Hannah! Na próxima cena cai o entardecer e as lanternas do pátio se acendem para todos.'
CLOSING = ('arthur', 'See you later!')
STORY = [
    ('arthur', 'Tessa, how many cinnamon rolls and lemon cakes can your oven bake each morning?', 'Tessa, quantos rolinhos de canela e bolos de limão o seu forno consegue assar a cada manhã?'),
    ('tessa', 'Double what I make now! Are we really opening the courtyard cafe to our street?', 'O dobro do que eu faço hoje! Nós vamos mesmo abrir o café do pátio para a nossa rua?'),
    ('arthur', 'Starting tomorrow at eight! Four tables inside, three tables under the tree!', 'Começando amanhã às oito! Quatro mesas lá dentro, três mesas debaixo da árvore!'),
    ('tessa', "My dream cafe, right here in our own courtyard! Wait until I tell the baker's market!", 'O café dos meus sonhos, bem aqui no nosso próprio pátio! Esperem só até eu contar na feira dos padeiros!'),
    ('arthur', 'And now, Hannah, today is Friday, the last day of your five day trial week.', 'E agora, Hannah, hoje é sexta-feira, o último dia da sua semana de experiência de cinco dias.'),
    ('hannah', 'Oh! With the suitcases, the boiler, and the letter, I completely forgot!', 'Ah! Com as malas, a caldeira e a carta, eu esqueci completamente!'),
    ('arthur', 'On Monday you opened our tricky door; since then you saved rooms, pipes, breakfast, and our lease.', 'Na segunda você abriu nossa porta manhosa; desde então salvou quartos, canos, o café da manhã e o nosso contrato.'),
    ('tessa', 'If you do not hire her full time, Arthur, I am hiring her in my kitchen!', 'Se você não contratar ela em período integral, Arthur, eu contrato na minha cozinha!'),
    ('arthur', 'Hands off, Tessa! Hannah, would you stay as our permanent front desk manager?', 'Tire o olho, Tessa! Hannah, você aceitaria ficar como nossa gerente efetiva da recepção?'),
    ('hannah', 'Stay here with all of you? Yes, a hundred times yes!', 'Ficar aqui com todos vocês? Sim, cem vezes sim!'),
    ('arthur', "Wonderful! Your name goes in Graham's big paper book in permanent ink!", 'Maravilha! Seu nome vai entrar no grande livro de papel do Graham com tinta permanente!'),
    ('hannah', 'Best first week of my life!', 'A melhor primeira semana da minha vida!'),
]
WALK = [
    (0, None, ["'Tessa, quantos rolinhos de canela e bolos de limão o seu forno consegue assar a cada manhã?' Para perguntar quantidades contáveis no plural, abra sempre com", (None, 'how many'), 'quantos.']),
    (1, None, ["'O dobro do que eu faço hoje! Nós vamos mesmo abrir o café do pátio para a nossa rua?' Curto e cheio de energia,", (None, 'Double what I make now'), 'significa o dobro do que preparo agora.']),
    (2, None, ["'Começando amanhã às oito! Quatro mesas lá dentro, três mesas debaixo da árvore!' Para marcar quando uma novidade começa a valer, use", (None, 'Starting tomorrow'), 'a partir de amanhã.']),
    (3, None, ["'O café dos meus sonhos, bem aqui no nosso próprio pátio! Esperem só até eu contar na feira dos padeiros!' Colocar 'dream' antes do substantivo cria", (None, 'My dream cafe'), 'o café dos meus sonhos.']),
    (4, None, ["'E agora, Hannah, hoje é sexta-feira, o último dia da sua semana de experiência de cinco dias.' No trabalho, período de experiência é 'trial', formando", (None, 'five day trial week'), "com 'day' no singular."]),
    (5, None, ["'Ah! Com as malas, a caldeira e a carta, eu esqueci completamente!' Natural e muito comum,", (None, 'I completely forgot'), 'coloca o advérbio logo antes do verbo no passado.']),
    (6, None, ["'Na segunda você abriu nossa porta manhosa; desde então salvou quartos, canos, o café da manhã e o nosso contrato.' O par temporal", (None, 'since then'), "significa 'desde então'."]),
    (7, None, ["'Se você não contratar ela em período integral, Arthur, eu contrato na minha cozinha!' No vocabulário de emprego,", (None, 'hire her full time'), 'é contratar em período integral.']),
    (8, None, ["'Tire o olho, Tessa! Hannah, você aceitaria ficar como nossa gerente efetiva da recepção?' Duas expressões ótimas:", (None, 'Hands off'), "literalmente 'tire as mãos!', e o convite", (None, 'would you stay'), 'você ficaria?']),
    (9, None, ["'Ficar aqui com todos vocês? Sim, cem vezes sim!' Em inglês 'cem' pede artigo indefinido na frente:", (None, 'a hundred times yes'), 'cem vezes sim!']),
    (10, None, ["'Maravilha! Seu nome vai entrar no grande livro de papel do Graham com tinta permanente!' Para dizer se algo foi escrito a tinta ou a lápis usa-se 'in':", (None, 'in permanent ink'), 'com tinta permanente.']),
    (11, None, ["'A melhor primeira semana da minha vida!' Na fala empolgada,", (None, 'Best first week of my life'), "dispensa o 'the' inicial e soa super espontâneo."]),
]
