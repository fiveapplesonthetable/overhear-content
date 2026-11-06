# Authoring module for posada-del-limonero-s01e01-scene-03.
ID = 'posada-del-limonero-s01e01-scene-03'
SHOW = 'posada-del-limonero'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = '¿Dónde están mis gafas?  (Where Are My Glasses?)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'ernesto': 'Ernesto', 'clara': 'Clara', 'mateo': 'Mateo'}
INTRO = 'Before the first guest arrives, guesthouse owner Ernesto hurries in from the courtyard looking flustered. Clara and Mateo watch as Ernesto searches his pockets in a panic. Listen to the whole scene first.'
OPENER = "Let's go through those lines together, step by step."
TRANSITION = "Now let's hear all twelve lines together from the top."
OUTRO = 'Ernesto found his glasses on his own forehead just as the taxi pulled up outside. Relax and let the rhythm of the words sink in; see you next time.'
CLOSING = ('ernesto', '¡Hasta luego!')
STORY = [
    ('ernesto', '¡Buenos días a todos! Bienvenida, Clara. ¿Está todo listo?', 'Good morning, everyone! Welcome, Clara. Is everything ready?'),
    ('clara', '¡Buenos días! Sí, el mostrador está limpio y las llaves están listas.', 'Good morning! Yes, the counter is clean and the keys are ready.'),
    ('ernesto', 'La clienta de la habitación cuatro se queda toda la semana. ¡Todo debe estar perfecto!', 'The guest in room four is staying all week. Everything must be perfect!'),
    ('mateo', 'Tranquilo, Ernesto. La habitación está limpia y las toallas están secas.', 'Relax, Ernesto. The room is clean and the towels are dry.'),
    ('ernesto', 'Necesito leer el libro de reservas, ¡pero no encuentro mis gafas!', 'I need to read the reservation book, yet I cannot find my glasses!'),
    ('clara', '¿Están en el bolsillo del abrigo?', 'Are they in your coat pocket?'),
    ('ernesto', '¡No, solo tengo mi bolígrafo y tres recibos viejos!', 'No, I only have my pen and three old receipts!'),
    ('mateo', 'Mira en el espejo detrás del mostrador, jefe.', 'Look in the mirror behind the counter, boss.'),
    ('ernesto', '¿Por qué van a estar mis gafas en el... ¡ah! ¡Están en mi cabeza!', 'Why would my glasses be in the... oh! They are on my head!'),
    ('clara', 'Ahí mismo, en la frente, sanas y salvas.', 'Right there on your forehead, safe and sound.'),
    ('ernesto', '¡Ni una palabra a nadie! Ahora sonreíd cuando suene el timbre.', 'Not a word to anyone! Now smile when the bell rings.'),
    ('mateo', 'Ahora mismo llega un taxi a la puerta.', 'Right now a taxi is pulling up at the gate.'),
]
WALK = [
    (0, None, ["'Good morning, everyone! Welcome, Clara. Is everything ready?' Greeting a woman,", (None, 'Bienvenida'), 'ends in a; when greeting a man it ends in o.']),
    (1, None, ["'Good morning! Yes, the counter is clean and the keys are ready.' Clean and ready describe current condition rather than permanent identity, so Clara pairs them with", (None, 'está'), 'and its plural form.']),
    (2, None, ["'The guest in room four is staying all week. Everything must be perfect!'", (None, 'La clienta'), "signals immediately that Room 4's guest is female."]),
    (3, None, ["'Relax, Ernesto. The room is clean and the towels are dry.' Mateo calms him down with", (None, 'Tranquilo'), "literally 'calm', Spain's favourite one-word way to say 'take it easy'."]),
    (4, None, ["'I need to read the reservation book, yet I cannot find my glasses!' Reading glasses in Spain are called", (None, 'gafas'), 'always plural just like in English.']),
    (5, None, ["'Are they in your coat pocket?' For pockets and clothes you are wearing, Spanish prefers 'the' over 'your', saying", (None, 'el bolsillo del abrigo'), "where 'of' and 'the' contract into one short word."]),
    (6, None, "'No, I only have my pen and three old receipts!' Notice how 'old receipts' flips the English order to put the describing word last."),
    (7, None, ["'Look in the mirror behind the counter, boss.' Mateo calls Ernesto", (None, 'jefe'), 'the warm everyday word for boss or chief.']),
    (8, None, ["'Why would my glasses be in the... oh! They are on my head!' Written as two words,", (None, 'Por qué'), "asks 'why?'; written together without a space, it means 'because'."]),
    (9, None, ["'Right there on your forehead, safe and sound.' The pair", (None, 'sanas y salvas'), "literally 'healthy and safe', takes feminine plural endings to match the glasses."]),
    (10, None, ["'Not a word to anyone! Now smile when the bell rings.' Speaking to Clara and Mateo together, Ernesto uses Spain's plural group command", (None, 'sonreíd'), 'to tell both colleagues to smile.']),
    (11, None, ["'Right now a taxi is pulling up at the gate.' Pairing 'now' with 'same' in", (None, 'Ahora mismo'), "means 'this very instant'."]),
]
