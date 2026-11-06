# Authoring module for posada-del-limonero-s01e01-scene-01.
ID = 'posada-del-limonero-s01e01-scene-01'
SHOW = 'posada-del-limonero'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Levanta el picaporte  (Lift the Handle)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'clara': 'Clara', 'mateo': 'Mateo'}
INTRO = 'Clara arrives early for her very first morning at the Lemon Tree Inn guesthouse in Valencia. Behind the front desk, veteran handyman Mateo is already pouring strong tea. Listen to the Spanish first without worrying about catching every word.'
OPENER = "Let's go back through the conversation slowly, one line at a time."
TRANSITION = "Now let's hear the entire scene again at natural speed."
OUTRO = "Clara is inside, the eight brass keys are on the board, and her first morning has begun. Don't worry if a few words went past quickly; they come back all week. See you next time."
CLOSING = ('clara', '¡Hasta luego!')
STORY = [
    ('clara', '¡Buenos días! Disculpe, ¿está cerrada la puerta?', 'Good morning! Excuse me, is the door locked?'),
    ('mateo', 'Buenos días. No, primero levanta el picaporte y luego empuja.', 'Good morning. No, lift the handle first, then push.'),
    ('clara', '¡Ah, se abre! Gracias. Soy Clara, la nueva recepcionista.', 'Oh, it opens! Thank you. I am Clara, the new receptionist.'),
    ('mateo', 'Yo soy Mateo. Llegas diez minutos antes.', 'I am Mateo. You are ten minutes early.'),
    ('clara', 'Mi primer día siempre camino rápido. ¿Dónde está el ordenador?', 'On my first day I always walk fast. Where is the computer?'),
    ('mateo', 'En el cajón. Aquí usamos este cuaderno grande de papel y un lápiz.', 'In the drawer. Here we use this big paper notebook and a pencil.'),
    ('clara', '¿Un cuaderno de papel? ¿De verdad?', 'A paper notebook? Really?'),
    ('mateo', 'El papel nunca pierde la lista de habitaciones cuando llueve.', 'Paper never loses the room list when it rains.'),
    ('clara', '¡Tiene razón! ¿Y estas son las llaves?', 'Fair point! And these are the keys?'),
    ('mateo', 'Sí, ocho habitaciones y ocho llaves de latón. Hoy llega la cuatro.', 'Yes, eight rooms and eight brass keys. Number four arrives today.'),
    ('clara', 'Genial. Dime todo lo que necesito saber.', 'Great. Tell me everything I need to know.'),
    ('mateo', 'Primera regla: primero bebe té caliente y después abre la puerta.', 'Rule one: drink hot tea first, then answer the door.'),
]
WALK = [
    (0, None, ["'Good morning! Excuse me, is the door locked?' Spanish greets the morning in the plural, literally wishing good days, and", (None, 'Disculpe'), "politely gets a stranger's attention through a closed door."]),
    (1, None, ["'Good morning. No, lift the handle first, then push.' Mateo switches straight to friendly colleague speech with", (None, 'levanta'), 'and links his two steps using words for first and then.']),
    (2, None, ["'Oh, it opens! Thank you. I am Clara, the new receptionist.' Listen to", (None, 'se abre'), 'which literally says the door opens itself, a turn of phrase Spanish loves for doors and shops.']),
    (3, None, ["'I am Mateo. You are ten minutes early.' Mateo adds", (None, 'Yo'), 'for contrast—meaning I, for my part, am Mateo—while Spanish expresses early as ten minutes before.']),
    (4, None, ["'On my first day I always walk fast. Where is the computer?' Across Spain, people call a computer", (None, 'el ordenador'), 'built from the idea of putting data in order.']),
    (5, None, ["'In the drawer. Here we use this big paper notebook and a pencil.' Describing words sit after the item in Spanish, so", (None, 'cuaderno grande de papel'), 'runs notebook big of paper.']),
    (6, None, ["'A paper notebook? Really?' That crisp two-word reaction,", (None, 'De verdad'), "literally asks 'of truth?' and fits anywhere English says 'really?'."]),
    (7, None, "'Paper never loses the room list when it rains.' Notice how Spanish needs just a single word at the end for 'it rains', with no separate word for 'it'."),
    (8, None, ["'Fair point! And these are the keys?' Clara agrees using", (None, 'Tiene razón'), "literally 'you have reason', the natural Spanish way to tell someone they are right."]),
    (9, None, ["'Yes, eight rooms and eight brass keys. Number four arrives today.' At the end,", (None, 'la cuatro'), "keeps the feminine word for 'the' because the unspoken word for room is feminine."]),
    (10, None, ["'Great. Tell me everything I need to know.' Now Clara matches Mateo's casual colleague tone:", (None, 'Dime'), "packs 'tell' and 'me' into one punchy word."]),
    (11, None, "'Rule one: drink hot tea first, then answer the door.' Mateo's house rule puts hot tea ahead of work, ordering the words as 'tea hot'."),
]
