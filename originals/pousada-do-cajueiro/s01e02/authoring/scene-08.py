ID = 'pousada-do-cajueiro-s01e02-scene-08'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 2, 8
TITLE = 'Dois nomes, um quarto  (Two Names, One Room)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'otavio': 'Otávio', 'camila': 'Camila', 'jorge': 'Jorge'}

INTRO = ('On Wednesday evening, as rain clouds gather over Recife, Otavio steps out of his office holding both the '
 "tablet and Jorge's paper ledger, looking pale. Camila and Jorge look up at once. Listen first.")
OPENER = "Let's go back through the Wednesday evening cliffhanger line by line."
TRANSITION = "Now let's hear the whole scene again from start to finish."
OUTRO = ("Two guests booked into Room 7, rain pouring outside, and only forty minutes until the eight o'clock "
 'arrival! Episode 2 is complete—join us in Episode 3 to see if the third-floor attic can save the night. '
 'See you next time.')
CLOSING = ('otavio', 'Boa noite!')

STORY = [
    ('otavio', 'Jorge... Camila... por favor, me digam que o quarto seis está livre hoje à noite.', 'Jorge... Camila... please tell me that room six is free tonight.'),
    ('camila', 'Não, Seu Otávio, o casal do sul entrou no quarto seis faz uma hora.', 'No, Mr Otavio, the couple from the south checked into room six an hour ago.'),
    ('jorge', 'Todas as chaves de um a sete estão ocupadas, e o quarto oito está com tinta fresca.', 'Every key from one to seven is taken, and room eight has wet paint.'),
    ('otavio', 'Ai, que desastre! Ontem anotei uma reserva no tablet sem os meus óculos!', 'Oh, what a disaster! Yesterday I wrote a booking on the tablet without my glasses!'),
    ('camila', 'Espere, deixe eu olhar a tela do tablet e o caderno de papel juntos.', 'Wait, let me look at the tablet screen and the paper notebook together.'),
    ('jorge', 'Deixe eu adivinhar. O senhor prometeu um quarto que a gente não tem?', 'Let me guess. Did you promise a room that we do not have?'),
    ('camila', 'Seu Otávio! O quarto sete já está ocupado, e o senhor colocou outro hóspede no sete!', 'Mr Otavio! Room seven is already occupied, and you put another guest in seven!'),
    ('otavio', 'E ele chega aqui às oito da noite, daqui a quarenta minutos!', "And he arrives here at eight o'clock this evening—in forty minutes!"),
    ('jorge', 'Eu avisei que esse tablet é uma armadilha.', 'I warned you that this tablet is a trap.'),
    ('otavio', 'Está chovendo lá fora e todos os hotéis da rua estão cheios! O que vamos fazer?', 'It is raining outside and every hotel on the street is full! What are we going to do?'),
    ('camila', 'Espere, o que tem lá no terceiro andar, em cima da escada?', 'Wait, what is up on the third floor, above the stairs?'),
    ('jorge', 'O antigo estúdio do sótão... venham comigo, rápido!', 'The old attic study... come with me, fast!'),
]

WALK = [
    (0, None, ["'Jorge... Camila... please tell me that room six is free tonight.' For an available room or seat, ", (None, 'está livre'), " means 'is free'."]),
    (1, None, ["'No, Mr Otavio, the couple from the south checked into room six an hour ago.' Spoken Portuguese loves ", (None, 'faz uma hora.'), " literally 'it makes one hour', for 'an hour ago'."]),
    (2, None, ["'Every key from one to seven is taken, and room eight has wet paint.' Signs on newly painted benches and doors read ", (None, 'tinta fresca.'), " literally 'fresh paint' where English says 'wet paint'."]),
    (5, None, ["'Let me guess. Did you promise a room that we do not have?' Playful ", (None, 'Deixe eu adivinhar.'), " means 'let me guess' right before Jorge delivers the bad news."]),
    (7, None, ["'And he arrives here at eight o'clock this evening—in forty minutes!'clock evening bus, in forty minutes!' To say 'in forty minutes from now', Portuguese uses ", (None, 'daqui a quarenta minutos!'), " literally 'from here to forty minutes'."]),
    (8, None, ["'I warned you that this tablet is a trap.' Vivid ", (None, 'uma armadilha.'), " means 'a trap', Jorge's verdict on modern screens."]),
    (9, None, ["'It is raining outside and every hotel on the street is full! What are we going to do?' Rain happening right now uses ", (None, 'Está chovendo'), ' alongside ', (None, 'lá fora'), " for 'out there' or 'outside'."]),
    (11, None, ["'The old attic study... come with me, fast!' Just like 'with me' in Scene 2, ", (None, 'comigo,'), " fuses 'with' and 'me' as Jorge leads the charge upstairs."]),
]
