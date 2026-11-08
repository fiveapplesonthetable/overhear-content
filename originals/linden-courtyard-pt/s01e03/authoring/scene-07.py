# Authoring module for linden-courtyard-pt-s01e03-scene-07.
ID = 'linden-courtyard-pt-s01e03-scene-07'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 3
SCENE = 7
TITLE = 'Returning the Notebook  (Devolvendo o caderno)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb'}
INTRO = 'Hannah sobe até a porta do sótão para devolver o caderno de couro esquecido de Caleb, tentando agir normalmente mesmo achando que ele é um inspetor secreto de hotéis. Ouça primeiro.'
OPENER = 'Agora vamos passar por cada linha da conversa.'
TRANSITION = 'Vamos ouvir a cena inteira novamente na velocidade normal.'
OUTRO = 'Caleb recuperou o caderno sem desconfiar de nada, mas aquele radiador esfriando é um sinal de alerta. Última cena do episódio três a seguir: rumo ao porão! Até já.'
CLOSING = ('caleb', 'Have a good night!')
STORY = [
    ('hannah', 'Excuse me, Caleb? Sorry to disturb you.', 'Com licença, Caleb? Desculpe incomodar.'),
    ('caleb', 'Oh, my leather notebook! Thank you! I was just looking for it.', 'Ah, meu caderno de couro! Obrigado! Eu estava mesmo procurando por ele.'),
    ('hannah', 'You left it by the soup cup on the front counter.', 'O senhor o deixou perto da xícara de sopa no balcão da frente.'),
    ('caleb', 'All my street notes from this week are in here. You saved me.', 'Todas as minhas anotações de rua desta semana estão aqui dentro. Você me salvou.'),
    ('hannah', 'We are glad you find our courtyard peaceful for your... work.', 'Ficamos felizes que o senhor ache o nosso pátio tranquilo para o seu... trabalho.'),
    ('caleb', 'Very peaceful! Though did you hear a funny metal knock just now?', 'Muito tranquilo! Mas você ouviu uma batida metálica estranha agorinha?'),
    ('hannah', 'Yes! It sounded like it came from the heating pipe in the corner.', 'Sim! Pareceu vir do cano de aquecimento ali no canto.'),
    ('caleb', 'Feel the radiator. The bottom is warm, while the top is turning cool.', 'Toque no radiador. A parte de baixo está quente, enquanto a de cima está ficando fria.'),
    ('hannah', 'Oh! Sometimes old pipes have a little air bubble at night.', 'Ah! Às vezes canos antigos ficam com uma pequena bolha de ar à noite.'),
    ('caleb', 'I have a warm blanket, so I am quite comfortable tonight.', 'Eu tenho um cobertor quentinho, então estou bem confortável hoje à noite.'),
    ('hannah', 'Thank you for being so patient! Graham will check the basement right away.', 'Obrigada por ser tão paciente! O Graham vai verificar o porão agora mesmo.'),
    ('caleb', 'Good night, Hannah. See you at breakfast.', 'Boa noite, Hannah. Até o café da manhã.'),
]
WALK = [
    (0, None, ["'Com licença, Caleb? Desculpe incomodar.' Ao bater na porta de alguém,", (None, 'Sorry to disturb you'), 'é o jeito mais educado de pedir licença pela interrupção.']),
    (1, None, ["'Ah, meu caderno de couro! Obrigado! Eu estava mesmo procurando por ele.' Lembre-se de que procurar algo em inglês exige a preposição 'for':", (None, 'looking for it'), 'procurando por ele.']),
    (2, None, ["'O senhor o deixou perto da xícara de sopa no balcão da frente.' A preposição", (None, 'by the soup cup'), "indica proximidade: 'ao lado de' ou 'perto de'."]),
    (3, None, ["'Todas as minhas anotações de rua desta semana estão aqui dentro. Você me salvou.' O par", (None, 'in here'), "destaca 'aqui dentro deste caderno'."]),
    (4, None, ["'Ficamos felizes que o senhor ache o nosso pátio tranquilo para o seu... trabalho.' Em", (None, 'you find our courtyard peaceful'), "o verbo 'find' tem o sentido de achar ou considerar."]),
    (5, None, ["'Muito tranquilo! Mas você ouviu uma batida metálica estranha agorinha?' Além de engraçado,", (None, 'funny'), "significa muito frequentemente 'estranho' ou 'esquisito'."]),
    (6, None, ["'Sim! Pareceu vir do cano de aquecimento ali no canto.' Para dizer como um barulho soou usando uma frase inteira, diga", (None, 'It sounded like'), 'pareceu que.']),
    (7, None, ["'Toque no radiador. A parte de baixo está quente, enquanto a de cima está ficando fria.' Mudanças graduais de temperatura usam muito bem", (None, 'turning cool'), 'ficando frio.']),
    (8, None, ["'Ah! Às vezes canos antigos ficam com uma pequena bolha de ar à noite.' Diferente de manhã e tarde que usam 'in', com a noite dizemos", (None, 'at night'), 'sem artigo.']),
    (9, None, ["'Eu tenho um cobertor quentinho, então estou bem confortável hoje à noite.' No inglês americano,", (None, 'quite comfortable'), "reforça positivamente: 'bem confortável'."]),
    (10, None, ["'Obrigada por ser tão paciente! O Graham vai verificar o porão agora mesmo.' Para agradecer uma atitude usamos 'for' mais '-ing':", (None, 'for being so patient'), 'por ser tão paciente.']),
    (11, None, ["'Boa noite, Hannah. Até o café da manhã.' Para marcar encontro numa refeição usa-se a preposição pontual:", (None, 'at breakfast'), 'no café da manhã.']),
]
