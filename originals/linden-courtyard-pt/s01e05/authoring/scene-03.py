# Authoring module for linden-courtyard-pt-s01e05-scene-03.
ID = 'linden-courtyard-pt-s01e05-scene-03'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 5
SCENE = 3
TITLE = 'Friday Lemon Cake  (O bolo de limão de sexta-feira)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'evelyn': 'Evelyn', 'caleb': 'Caleb', 'tessa': 'Tessa'}
INTRO = 'Às nove e meia, no cantinho do café, Tessa serve café fresco para a senhorita Evelyn e Caleb enquanto eles relembram as tardes de sexta-feira de vinte e cinco anos atrás. Ouça primeiro.'
OPENER = 'Vamos passar por cada frase desta conversa.'
TRANSITION = 'Agora ouça novamente a cena completa.'
OUTRO = 'Seis limões amarelos na cesta da cozinha e duas horas até o meio-dia: Tessa já está amarrando o avental! Na próxima cena saímos para o pátio. Até logo.'
CLOSING = ('tessa', 'Bye for now!')
STORY = [
    ('tessa', 'So, Caleb, you are really staying in the courtyard to greet Owen at noon?', 'Então, Caleb, você vai mesmo ficar no pátio para receber o Owen ao meio-dia?'),
    ('caleb', 'Yes, Tessa. Even if he turns around and walks straight back out the gate.', 'Sim, Tessa. Mesmo que ele dê meia-volta e saia direto pelo portão.'),
    ('evelyn', 'Owen will not walk out. He always acted tough for five seconds, then softened.', 'O Owen não vai embora. Ele sempre bancava o durão por cinco segundos e depois amolecia.'),
    ('caleb', 'You still remember that after all these years?', 'A senhora ainda lembra disso depois de todos esses anos?'),
    ('evelyn', 'Of course! Every Friday when he missed a piano note, he frowned at the wall.', 'Claro! Toda sexta-feira, quando ele errava uma nota no piano, fechava a cara para a parede.'),
    ('tessa', 'How did you get him smiling again, Miss Evelyn?', 'Como a senhora fazia ele voltar a sorrir, senhorita Evelyn?'),
    ('evelyn', 'His grandfather sliced warm lemon cake with powdered sugar on top!', 'O avô dele cortava fatias de bolo de limão morno com açúcar de confeiteiro por cima!'),
    ('caleb', 'Oh! Yellow lemon glaze! We fought over the corner piece every single Friday!', 'Ah! Cobertura amarela de limão! Nós disputávamos o pedaço da ponta toda santa sexta-feira!'),
    ('tessa', 'Hold everything! What time is it right now? Nine thirty-five!', 'Parem tudo! Que horas são agora mesmo? Nove e trinta e cinco!'),
    ('caleb', 'Tessa, please do not do extra work because of us.', 'Tessa, por favor não tenha trabalho extra por nossa causa.'),
    ('tessa', 'Six yellow lemons are sitting in my basket right now. This kitchen was waiting for today!', 'Seis limões amarelos estão ali na minha cesta agora mesmo. Esta cozinha estava esperando pelo dia de hoje!'),
    ('evelyn', 'Bake plenty of corner pieces, my dear!', 'Asse bastantes pedaços de canto, minha querida!'),
]
WALK = [
    (0, None, ["'Então, Caleb, você vai mesmo ficar no pátio para receber o Owen ao meio-dia?' De novo o contínuo", (None, 'you are really staying'), 'confirma uma decisão firme para hoje.']),
    (1, None, ["'Sim, Tessa. Mesmo que ele dê meia-volta e saia direto pelo portão.' Duas expressões essenciais:", (None, 'Even if'), "para 'mesmo que', e", (None, 'turns around'), 'para dar meia-volta.']),
    (2, None, ["'O Owen não vai embora. Ele sempre bancava o durão por cinco segundos e depois amolecia.' A combinação", (None, 'acted tough'), "retrata perfeitamente 'bancar o durão'."]),
    (3, None, ["'A senhora ainda lembra disso depois de todos esses anos?' Natural e muito comum,", (None, 'after all these years'), "equivale ao nosso 'depois de todos esses anos'."]),
    (4, None, ["'Claro! Toda sexta-feira, quando ele errava uma nota no piano, fechava a cara para a parede.' Em música ou esportes,", (None, 'missed a piano note'), 'é errar uma nota.']),
    (5, None, ["'Como a senhora fazia ele voltar a sorrir, senhorita Evelyn?' O giro", (None, 'get him smiling'), 'expressa conseguir fazer alguém começar a sorrir.']),
    (6, None, ["'O avô dele cortava fatias de bolo de limão morno com açúcar de confeiteiro por cima!' No fim de receitas e pratos,", (None, 'on top'), 'indica o que vai polvilhado por cima.']),
    (7, None, ["'Ah! Cobertura amarela de limão! Nós disputávamos o pedaço da ponta toda santa sexta-feira!' Colocar 'single' no meio de", (None, 'every single Friday'), 'dá ênfase: sem pular nenhuma sexta.']),
    (8, None, ["'Parem tudo! Que horas são agora mesmo? Nove e trinta e cinco!' Cheia de entusiasmo,", (None, 'Hold everything'), "equivale ao nosso 'parem tudo!' quando surge uma ideia brilhante."]),
    (9, None, ["'Tessa, por favor não tenha trabalho extra por nossa causa.' No final da frase,", (None, 'because of us'), "traduz direitinho 'por nossa causa'."]),
    (10, None, ["'Seis limões amarelos estão ali na minha cesta agora mesmo. Esta cozinha estava esperando pelo dia de hoje!' Objetos parados dentro de cestas ou mesas costumam usar 'sit':", (None, 'are sitting in my basket'), 'estão na minha cesta.']),
    (11, None, ["'Asse bastantes pedaços de canto, minha querida!' O tratamento carinhoso", (None, 'my dear'), 'soa afetuoso e gentil.']),
]
