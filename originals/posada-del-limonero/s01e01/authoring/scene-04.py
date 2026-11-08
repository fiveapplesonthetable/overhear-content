# Authoring module for posada-del-limonero-s01e01-scene-04.
ID = 'posada-del-limonero-s01e01-scene-04'
SHOW = 'posada-del-limonero'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'La habitación cuatro en la segunda planta  (Room Four on the Second Floor)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'clara': 'Clara', 'carmen': 'Carmen', 'mateo': 'Mateo'}
INTRO = "At the front desk, retired music teacher Carmen steps inside from her taxi pulling a large dark-blue suitcase. Clara greets her first real guest while Mateo stands ready to help with the bag. Let's hear how it goes."
OPENER = "Now let's unpack the conversation one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Clara handled her first check-in smoothly, though Mateo noticed that blue suitcase felt strangely heavy. See you next time to find out why.'
CLOSING = ('carmen', '¡Hasta pronto!')
STORY = [
    ('clara', '¡Bienvenida! Buenos días, señora.', 'Welcome! Good morning, madam.'),
    ('carmen', 'Buenos días, querida. Tengo una reserva para Isabel.', 'Good morning, my dear. I have a booking for Isabel.'),
    ('clara', '¡Sí, la habitación cuatro en la segunda planta! ¿Qué tal el viaje en tren?', 'Yes, room four on the second floor! How was your train trip?'),
    ('carmen', 'Tranquilo y agradable, gracias, aunque esta maleta pesa mucho hoy.', 'Quiet and pleasant, thank you, though this suitcase weighs a lot today.'),
    ('mateo', 'Con permiso. ¡Madre mía! ¿Lleva piedras aquí dentro?', 'Allow me. Goodness! Are you carrying stones inside here?'),
    ('carmen', '¡Solo vestidos, partituras y mi taza favorita!', 'Only dresses, sheet music, and my favourite cup!'),
    ('clara', 'Aquí tiene su llave, la número cuatro. El desayuno es de siete y media a diez.', 'Here is your key, number four. Breakfast is from seven thirty to ten.'),
    ('carmen', 'Estupendo. ¿La ventana da a la calle o al patio?', 'Wonderful. Does the window face the street or the courtyard?'),
    ('clara', 'Al patio, justo encima del viejo limonero. Es muy tranquilo.', 'The courtyard, right above the old lemon tree. It is very quiet.'),
    ('carmen', 'Justo lo que necesito. ¿Dónde está la escalera?', 'Just what I need. Where are the stairs?'),
    ('mateo', 'Por este arco. Yo subo la maleta azul por usted.', 'Through this archway. I will carry the blue suitcase up for you.'),
    ('carmen', 'Muchas gracias a los dos.', 'Thank you both very much.'),
]
WALK = [
    (0, None, ["'Welcome! Good morning, madam.' Adding", (None, 'señora'), 'sets a courteous hotel tone as soon as a guest walks in.']),
    (1, None, ["'Good morning, my dear. I have a booking for Isabel.' Carmen confidently walks in with", (None, 'Tengo una reserva'), "using the everyday verb for 'I have'."]),
    (2, None, ["'Yes, room four on the second floor! How was your train trip?' Drop any topic right after", (None, 'Qué tal'), 'to ask how something went without changing a single ending.']),
    (3, None, ["'Quiet and pleasant, thank you, though this suitcase weighs a lot today.' Instead of saying 'is heavy', Spanish naturally says", (None, 'pesa mucho'), "literally 'weighs much'."]),
    (4, None, ["'Allow me. Goodness! Are you carrying stones inside here?' First Mateo steps in politely with", (None, 'Con permiso'), "literally 'with permission', and then", (None, 'Madre mía'), "exclaims 'my mother!' for 'goodness!'."]),
    (5, None, "'Only dresses, sheet music, and my favourite cup!' One word here covers 'sheet music' in the plural: scores for the piano."),
    (6, None, ["'Here is your key, number four. Breakfast is from seven thirty to ten.' Handing anything to a guest,", (None, 'Aquí tiene'), "literally 'here you have', is the gold-standard polite phrase, and half past seven is 'seven and a half'."]),
    (7, None, ["'Wonderful. Does the window face the street or the courtyard?' For a window or balcony overlooking a place, Spanish says", (None, 'da a'), "literally 'gives onto'."]),
    (8, None, "'The courtyard, right above the old lemon tree. It is very quiet.' Notice how 'to' and 'the' merge at the start into one short word before masculine 'courtyard'."),
    (9, None, ["'Just what I need. Where are the stairs?' Even though a staircase has many steps, Spanish usually treats", (None, 'la escalera'), 'as a single thing.']),
    (10, None, ["'Through this archway. I will carry the blue suitcase up for you.' Notice Mateo's respectful", (None, 'por usted'), "using the formal 'you' on behalf of the guest."]),
    (11, None, ["'Thank you both very much.' Adding", (None, 'a los dos'), "literally 'to the two', thanks two people at once."]),
]
