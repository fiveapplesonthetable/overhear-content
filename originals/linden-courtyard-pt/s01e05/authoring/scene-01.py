# Authoring module for linden-courtyard-pt-s01e05-scene-01.
ID = 'linden-courtyard-pt-s01e05-scene-01'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Truth in the Courtyard  (A verdade no pátio)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'evelyn': 'Evelyn'}
INTRO = 'Ainda debaixo da árvore do pátio na pousada Linden Courtyard Inn, em Portland, Caleb se senta com Hannah e a senhorita Evelyn para explicar desde o começo o mistério de segunda-feira à noite. Ouça primeiro toda a cena.'
OPENER = 'Agora vamos repassar a conversa com calma, frase por frase.'
TRANSITION = 'Vamos ouvir toda a cena novamente em velocidade natural.'
OUTRO = 'Todas as peças de segunda e terça-feira finalmente se encaixaram! Na próxima cena, Caleb conta por que passou três anos sem falar com o irmão Owen. Até a próxima.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('evelyn', 'Let me look at you properly, Caleb! You grew taller than the piano!', 'Deixe eu olhar direito para você, Caleb! Você ficou mais alto que o piano!'),
    ('caleb', 'I cannot believe you are staying in the exact same guesthouse, Miss Evelyn.', 'Não consigo acreditar que a senhora está hospedada exatamente na mesma pousada, senhorita Evelyn.'),
    ('hannah', 'Wait, so you rode the same train on Monday and took her suitcase?', 'Espere, então você viajou no mesmo trem na segunda-feira, e levou a mala dela?'),
    ('caleb', "By complete accident! At my cousin's apartment I opened it and saw sheet music and a red ribbon.", 'Por puro acidente! No apartamento do meu primo eu abri a mala e vi partituras e uma fita vermelha.'),
    ('evelyn', 'Why did you leave my bag on the step at night and run away?', 'Por que você deixou a minha mala no degrau à noite e saiu correndo?'),
    ('caleb', 'Because when I walked here on Monday evening, I saw my older brother walking down this street!', 'Porque quando eu vim andando até aqui na segunda à noite, vi meu irmão mais velho descendo esta rua!'),
    ('hannah', 'Your older brother lives here in Portland?', 'O seu irmão mais velho mora aqui em Portland?'),
    ('caleb', 'Yes. I panicked, rang your bell, and slipped the Friday note onto the handle.', 'Sim. Entrei em pânico, toquei a campainha e encaixei o bilhete de sexta-feira na alça.'),
    ('evelyn', 'Wait, and Wednesday night you checked in here under your real name?', 'Espere, e na quarta-feira à noite você fez check-in aqui com o seu nome verdadeiro?'),
    ('caleb', 'I needed a quiet place nearby before Friday, and honestly felt too shy to ask for my bag!', 'Eu precisava de um lugar silencioso aqui perto antes de sexta, e sinceramente fiquei com vergonha de pedir minha mala!'),
    ('hannah', 'Even after you called us on Tuesday about the white package!', 'Mesmo depois de você nos ligar na terça sobre o pacote branco!'),
    ('caleb', 'Everything in that white paper belongs to my brother Owen, not me.', 'Tudo dentro daquele papel branco pertence ao meu irmão Owen, não a mim.'),
]
WALK = [
    (0, None, ["'Deixe eu olhar direito para você, Caleb! Você ficou mais alto que o piano!' Em adjetivos curtos, o comparativo ganha '-er' seguido de 'than':", (None, 'taller than the piano'), 'mais alto que o piano.']),
    (1, None, ["'Não consigo acreditar que a senhora está hospedada exatamente na mesma pousada, senhorita Evelyn.' Para mostrar surpresa feliz, o inglês emenda", (None, 'I cannot believe'), 'direto na frase seguinte.']),
    (2, None, ["'Espere, então você viajou no mesmo trem na segunda-feira, e levou a mala dela?' Para viagens de trem ou ônibus, o inglês americano usa muito", (None, 'rode the same train'), 'pegamos o mesmo trem.']),
    (3, None, ["'Por puro acidente! No apartamento do meu primo eu abri a mala e vi partituras e uma fita vermelha.' A expressão", (None, 'By complete accident'), 'deixa claro que foi totalmente sem querer.']),
    (4, None, ["'Por que você deixou a minha mala no degrau à noite e saiu correndo?' Como o auxiliar 'did' já marca o passado no começo, os dois verbos ficam na forma básica:", (None, 'leave'), 'e', (None, 'run away'), 'fugir correndo.']),
    (5, None, ["'Porque quando eu vim andando até aqui na segunda à noite, vi meu irmão mais velho descendo esta rua!' Depois de 'saw', usar '-ing' em", (None, 'walking down this street'), 'mostra a cena acontecendo em movimento.']),
    (6, None, ["'O seu irmão mais velho mora aqui em Portland?' Quando bate a surpresa, a pergunta pode manter a ordem normal,", (None, 'lives here in Portland'), 'mudando só a entonação.']),
    (7, None, ["'Sim. Entrei em pânico, toquei a campainha e encaixei o bilhete de sexta-feira na alça.' A preposição", (None, 'onto the handle'), 'indica movimento até ficar preso sobre a alça.']),
    (8, None, ["'Espere, e na quarta-feira à noite você fez check-in aqui com o seu nome verdadeiro?' Registrar-se num hotel é", (None, 'checked in'), 'e para o nome registrado usa-se', (None, 'under your real name'), 'sob seu nome verdadeiro.']),
    (9, None, ["'Eu precisava de um lugar silencioso aqui perto antes de sexta, e sinceramente fiquei com vergonha de pedir minha mala!' Para expressar timidez ou vergonha de fazer algo, o inglês usa", (None, 'felt too shy'), 'senti muita timidez.']),
    (10, None, ["'Mesmo depois de você nos ligar na terça sobre o pacote branco!' A preposição", (None, 'about'), "introduz o assunto da ligação, correspondendo a 'sobre'."]),
    (11, None, ["'Tudo dentro daquele papel branco pertence ao meu irmão Owen, não a mim.' O verbo pertencer pede sempre a preposição 'to':", (None, 'belongs to my brother'), 'pertence ao meu irmão.']),
]
