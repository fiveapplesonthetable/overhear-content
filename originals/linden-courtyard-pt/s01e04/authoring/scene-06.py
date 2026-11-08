# Authoring module for linden-courtyard-pt-s01e04-scene-06.
ID = 'linden-courtyard-pt-s01e04-scene-06'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 4
SCENE = 6
TITLE = 'The Acoustic Architect  (O arquiteto acústico)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = 'Lá fora, à sombra da velha árvore do pátio, Caleb abre seu caderno de couro marrom para Hannah e Tessa enquanto os pássaros cantam pela manhã. Vamos ouvir primeiro.'
OPENER = 'Agora vamos repassar cada linha com tranquilidade.'
TRANSITION = 'Vamos escutar toda a cena novamente em ritmo normal.'
OUTRO = "Caleb é arquiteto acústico, e aquela menção discreta a 'duas ruas daqui' e 'sexta-feira' fez Hannah e Tessa arregalarem os olhos! Até a próxima cena."
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('caleb', 'Look closely at this page. It measures decibels and quietness, not hotel stars!', 'Olhem bem de perto esta página. Ela mede decibéis e silêncio, não estrelas de hotel!'),
    ('hannah', "Decibels? So 'nine out of ten' was not a review of my front desk?", "Decibéis? Então 'nove de dez' não era uma avaliação da minha recepção?"),
    ('caleb', 'Well, your front desk deserves ten! Honestly, though, I am an acoustic architect.', 'Bem, a sua recepção merece dez! Sinceramente, porém, eu sou arquiteto acústico.'),
    ('tessa', 'An acoustic architect! Do you design concert halls?', 'Um arquiteto acústico! Você projeta salas de concerto?'),
    ('caleb', 'Small libraries and courtyards, mostly. I measure how old stone walls block street noise.', 'Pequenas bibliotecas e pátios, na maior parte. Eu meço como velhos muros de pedra bloqueiam o barulho da rua.'),
    ('hannah', 'That is why you listened for cars up in the attic last night!', 'É por isso que você ficou escutando se passavam carros lá no sótão ontem à noite!'),
    ('caleb', 'Exactly. Outside on the avenue it is loud, yet inside this courtyard you hear leaves and birds.', 'Exatamente. Lá fora na avenida é barulhento, mas dentro deste pátio você ouve folhas e pássaros.'),
    ('tessa', 'Wait until Arthur hears he panicked all night over decibels!', 'Espere até o Arthur saber que entrou em pânico a noite toda por causa de decibéis!'),
    ('caleb', 'Truthfully, I also chose this neighborhood for an old family reason.', 'Para ser sincero, também escolhi este bairro por um antigo motivo de família.'),
    ('hannah', 'Oh? Did your family live near here once?', 'Ah, é? Sua família já morou perto daqui no passado?'),
    ('caleb', 'Two streets away, when I was small. Friday is... an important day for me.', 'A duas ruas daqui, quando eu era pequeno. Sexta-feira é... um dia importante para mim.'),
    ('tessa', 'Wait, did he just say Friday?!', 'Espere, ele acabou de dizer sexta-feira?!'),
]
WALK = [
    (0, None, ["'Olhem bem de perto esta página. Ela mede decibéis e silêncio, não estrelas de hotel!' A combinação", (None, 'Look closely'), 'pede para observar os detalhes de pertinho.']),
    (1, None, ["'Decibéis? Então nove de dez não era uma avaliação da minha recepção?' Para checar algo que parecia verdade antes, usa-se o passado simples em", (None, 'was not a review'), 'não era uma avaliação.']),
    (2, None, ["'Bem, a sua recepção merece dez! Sinceramente, porém, eu sou arquiteto acústico.' Solto entre vírgulas,", (None, 'though'), "funciona como um 'porém' leve e muito natural na conversa."]),
    (3, None, ["'Um arquiteto acústico! Você projeta salas de concerto?' Em", (None, 'concert halls'), "a primeira palavra fica no singular porque qualifica 'salas'."]),
    (4, None, ["'Pequenas bibliotecas e pátios, na maior parte. Eu meço como velhos muros de pedra bloqueiam o barulho da rua.' No fim da frase,", (None, 'mostly'), "resume 'principalmente' ou 'na maioria das vezes'."]),
    (5, None, ["'É por isso que você ficou escutando se passavam carros lá no sótão ontem à noite!' Note a diferença: 'listen to' é ouvir algo presente, já", (None, 'listened for cars'), 'é apurar o ouvido procurando um som.']),
    (6, None, ["'Exatamente. Lá fora na avenida é barulhento, mas dentro deste pátio você ouve folhas e pássaros.' Ligando duas ideias opostas,", (None, 'yet'), "significa 'mas ainda assim'."]),
    (7, None, ["'Espere até o Arthur saber que entrou em pânico a noite toda por causa de decibéis!' Depois de 'until' falando do futuro, o inglês usa presente simples:", (None, 'until Arthur hears'), 'até ele ouvir.']),
    (8, None, ["'Para ser sincero, também escolhi este bairro por um antigo motivo de família.' O passado irregular", (None, 'chose'), "vem do verbo escolher, 'choose'."]),
    (9, None, ["'Ah, é? Sua família já morou perto daqui no passado?' No fim da pergunta sobre o passado,", (None, 'once'), "significa 'em outra época' ou 'alguma vez'."]),
    (10, None, ["'A duas ruas daqui, quando eu era pequeno. Sexta-feira é... um dia importante para mim.' Para falar da infância usa-se naturalmente", (None, 'when I was small'), 'quando eu era pequeno.']),
    (11, None, ["'Espere, ele acabou de dizer sexta-feira?!' Veja de novo a pergunta rápida no passado com 'just':", (None, 'did he just say'), 'ele acabou de dizer?']),
]
