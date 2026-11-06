# Authoring module for posada-del-limonero-s01e02-scene-08.
ID = 'posada-del-limonero-s01e02-scene-08'
SHOW = 'posada-del-limonero'
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = 'Dos nombres, una habitación  (Two Names, One Room)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'ernesto': 'Ernesto', 'clara': 'Clara', 'mateo': 'Mateo'}
INTRO = "On Wednesday evening, as dusk settles over Valencia, Ernesto comes out of his office holding both the tablet and Mateo's paper ledger, looking pale. Clara and Mateo look up at once. Listen first."
OPENER = "Now let's walk through the scene line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Two guests booked into Room 7, pouring rain outside, and only forty minutes before the eight o'clock arrival! Episode 2 is done—join us in Episode 3 to see if the attic can save the night."
CLOSING = ('ernesto', '¡Hasta pronto!')
STORY = [
    ('ernesto', 'Mateo... Clara... por favor, decidme que la habitación seis está libre esta noche.', 'Mateo... Clara... please tell me room six is free tonight.'),
    ('clara', 'No, Ernesto, la pareja del sur entró en la seis hace una hora.', 'No, Ernesto, the couple from the south checked into room six an hour ago.'),
    ('mateo', 'Todas las llaves de la uno a la siete están ocupadas, y la ocho tiene pintura fresca.', 'Every key from one to seven is occupied, and room eight has wet paint.'),
    ('ernesto', '¡Qué desastre! ¡Ayer apunté una reserva por teléfono en la tableta sin mis gafas!', 'What a disaster! Yesterday I wrote down a phone booking on the tablet without my glasses!'),
    ('clara', 'Un momento, déjeme mirar la pantalla de la tableta y el cuaderno juntos.', 'Wait a moment, let me look at the tablet screen and the notebook together.'),
    ('mateo', 'Déjame adivinar. ¿Le prometiste a alguien una habitación que no tenemos?', 'Let me guess. Did you promise somebody a room we do not have?'),
    ('clara', '¡Ernesto! ¡La habitación siete ya está ocupada y apuntó a un segundo cliente en la siete!', 'Ernesto! Room seven is already occupied and you booked a second guest into seven!'),
    ('ernesto', '¡Y llega en el tren de las ocho de la tarde, dentro de cuarenta minutos!', "And he arrives on the eight o'clock evening train, in forty minutes!"),
    ('mateo', 'Te dije que esa tableta es una trampa.', 'I told you that tablet is a trap.'),
    ('ernesto', '¡Fuera llueve mucho y todos los hoteles de nuestra calle están llenos! ¿Qué hacemos?', 'Outside it is raining hard and every hotel on our street is full! What do we do?'),
    ('clara', 'Esperad... ¿qué hay en la tercera planta, arriba de la escalera?', 'Wait... what is on the third floor, at the top of the stairs?'),
    ('mateo', 'La vieja buhardilla soleada... ¡seguidme, rápido!', 'The old sunny attic room... follow me, quickly!'),
]
WALK = [
    (0, None, ["'Mateo... Clara... please tell me room six is free tonight.' Asking a hotel desk if a room is available uses", (None, 'está libre'), "literally 'is free'."]),
    (1, None, ["'No, Ernesto, the couple from the south checked into room six an hour ago.' Again 'ago' sits before the time span in", (None, 'hace una hora'), "literally 'it makes one hour'."]),
    (2, None, ["'Every key from one to seven is occupied, and room eight has wet paint.' Signs in Spain say", (None, 'pintura fresca'), "literally 'fresh paint' where English says 'wet paint'."]),
    (3, None, ["'What a disaster! Yesterday I wrote down a phone booking on the tablet without my glasses!'", (None, 'Qué desastre'), "is a dramatic favourite of Ernesto's whenever plans go sideways."]),
    (4, None, ["'Wait a moment, let me look at the tablet screen and the notebook together.' Clara stays polite with Ernesto using", (None, 'déjeme mirar'), "for 'let me look'."]),
    (5, None, ["'Let me guess. Did you promise somebody a room we do not have?' Hear how", (None, 'Déjame adivinar'), "mirrors Clara's line one beat earlier, except in Mateo's casual colleague voice."]),
    (6, None, ["'Ernesto! Room seven is already occupied and you booked a second guest into seven!' Notice the little human marker before", (None, 'a un segundo cliente'), 'because a guest is a person.']),
    (7, None, ["'And he arrives on the eight o'clock evening train, in forty minutes!' When 'in' means 'from now', Spanish says", (None, 'dentro de cuarenta minutos'), "literally 'inside of forty minutes'."]),
    (8, None, ["'I told you that tablet is a trap.' Short and dry:", (None, 'Te dije'), "means 'I told you'."]),
    (9, None, ["'Outside it is raining hard and every hotel on our street is full! What do we do?' Present-tense", (None, 'Qué hacemos'), "asks 'what do we do now?'."]),
    (10, None, ["'Wait... what is on the third floor, at the top of the stairs?' One small word,", (None, 'hay'), "asks 'what is there?' for singular and plural alike."]),
    (11, None, ["'The old sunny attic room... follow me, quickly!' A cosy top-floor room under the roof is", (None, 'buhardilla'), 'a charming word you will hear all through Episode 3.']),
]
