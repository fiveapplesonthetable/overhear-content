# Authoring module for linden-courtyard-pt-s01e05-scene-05.
ID = 'linden-courtyard-pt-s01e05-scene-05'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 5
SCENE = 5
TITLE = 'Simple Words First  (Palavras simples primeiro)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = 'Vinte minutos antes do meio-dia, Caleb anda de um lado para o outro pelas pedras do pátio segurando um papel amassado enquanto Hannah se aproxima com um copo de água. Ouça primeiro.'
OPENER = 'Vamos repassar cada frase desta conversa.'
TRANSITION = 'Agora vamos escutar a cena inteira novamente.'
OUTRO = 'Nada de discurso de dezenove motivos: apenas obrigado por vir, senti sua falta, e sente-se para tomar chá e bolo de limão. Faltam dez minutos para o meio-dia! Até logo.'
CLOSING = ('caleb', 'Take care!')
STORY = [
    ('hannah', 'Here, drink a sip of cool water, Caleb. What is on that paper?', 'Tome, beba um gole de água fresca, Caleb. O que tem nesse papel?'),
    ('caleb', 'A five minute speech explaining nineteen reasons why we were both wrong in April.', 'Um discurso de cinco minutos explicando dezenove motivos pelos quais nós dois erramos em abril.'),
    ('hannah', 'Nineteen reasons?! Are you welcoming your brother or reading a train schedule?', 'Dezenove motivos?! Você está recebendo o seu irmão ou lendo uma tabela de horários de trem?'),
    ('caleb', 'When I get nervous, my sentences grow very long and formal!', 'Quando eu fico nervoso, minhas frases ficam muito compridas e formais!'),
    ('hannah', 'Fold that paper and put it in your pocket right now.', 'Dobre esse papel e guarde no bolso agora mesmo.'),
    ('caleb', 'Without my notes, what do I say when he walks through that gate?', 'Sem as minhas anotações, o que eu digo quando ele passar por aquele portão?'),
    ('hannah', "Start with three short sentences. First: 'Hello, Owen, thank you for coming.'", "Comece com três frases curtas. Primeira: 'Olá, Owen, obrigado por vir.'"),
    ('caleb', "'Hello, Owen, thank you for coming.' Okay, I can remember that.", "'Olá, Owen, obrigado por vir.' Certo, eu consigo lembrar disso."),
    ('hannah', "Second: 'I missed you these three years.'", "Segunda: 'Senti sua falta nestes três anos.'"),
    ('caleb', "'I missed you these three years.' Honest and clear. And third?", "'Senti sua falta nestes três anos.' Sincero e claro. E a terceira?"),
    ('hannah', "'Sit down, there is hot tea and Friday lemon cake.'", "'Sente-se, tem chá quente e bolo de limão de sexta-feira.'"),
    ('caleb', 'Tea and lemon cake! Hannah, you should open a school for nervous brothers.', 'Chá e bolo de limão! Hannah, você devia abrir uma escola para irmãos nervosos.'),
]
WALK = [
    (0, None, ["'Tome, beba um gole de água fresca, Caleb. O que tem nesse papel?' Para o que está escrito numa folha usamos sempre 'on':", (None, 'on that paper'), 'nesse papel.']),
    (1, None, ["'Um discurso de cinco minutos explicando dezenove motivos pelos quais nós dois erramos em abril.' Quando a medida vem antes do substantivo, ela fica no singular:", (None, 'five minute speech'), 'discurso de cinco minutos.']),
    (2, None, ["'Dezenove motivos?! Você está recebendo o seu irmão ou lendo uma tabela de horários de trem?' Um único auxiliar no começo,", (None, 'Are you welcoming'), "já vale também para o segundo verbo em '-ing'."]),
    (3, None, ["'Quando eu fico nervoso, minhas frases ficam muito compridas e formais!' Dois ótimos verbos para o nosso 'ficar':", (None, 'get nervous'), 'ficar nervoso, e', (None, 'grow very long'), 'ficar compridas aos poucos.']),
    (4, None, ["'Dobre esse papel e guarde no bolso agora mesmo.' Dois comandos simples e diretos abrindo com", (None, 'Fold that paper'), 'dobre esse papel.']),
    (5, None, ["'Sem as minhas anotações, o que eu digo quando ele passar por aquele portão?' Onde usamos futuro do subjuntivo, o inglês usa presente simples:", (None, 'when he walks through'), 'quando ele passar.']),
    (6, None, ["'Comece com três frases curtas. Primeira: Olá, Owen, obrigado por vir.' Agradecer a presença de alguém é simples assim:", (None, 'thank you for coming'), "com '-ing' após 'for'."]),
    (7, None, ["'Olá, Owen, obrigado por vir. Certo, eu consigo lembrar disso.' Depois de 'can' o verbo entra direto sem 'to':", (None, 'I can remember that'), 'consigo lembrar disso.']),
    (8, None, ["'Segunda: Senti sua falta nestes três anos.' Para dizer 'senti saudade de você', o inglês usa o verbo direto", (None, 'I missed you'), 'sem preposição.']),
    (9, None, ["'Senti sua falta nestes três anos. Sincero e claro. E a terceira?' Curto e prático,", (None, 'And third'), "pede o terceiro ponto sem repetir 'frase'."]),
    (10, None, ["'Sente-se, tem chá quente e bolo de limão de sexta-feira.' O convite acolhedor", (None, 'Sit down'), 'é indispensável para receber qualquer visita.']),
    (11, None, ["'Chá e bolo de limão! Hannah, você devia abrir uma escola para irmãos nervosos.' Para dar uma sugestão amigável ou bem-humorada, use", (None, 'you should open'), 'você deveria abrir.']),
]
