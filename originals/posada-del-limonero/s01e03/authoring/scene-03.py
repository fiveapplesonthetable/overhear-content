# Authoring module for posada-del-limonero-s01e03-scene-03.
ID = 'posada-del-limonero-s01e03-scene-03'
SHOW = 'posada-del-limonero'
SEASON = 1
EPISODE = 3
SCENE = 3
TITLE = 'A la izquierda en el rellano  (Left at the Landing)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'clara': 'Clara', 'rocio': 'Rocío', 'ernesto': 'Ernesto'}
INTRO = 'Ten minutes before eight, Clara, Rocio, and Ernesto put the finishing touches on the third-floor room. Every detail matters before the soaked traveller arrives. Listen first.'
OPENER = "Let's go through those lines together, step by step."
TRANSITION = "Now let's hear all twelve lines together from the top."
OUTRO = "The warm brass lamp is glowing just as the eight o'clock guest rings the downstairs bell. Next time, Javier steps out of the rain."
CLOSING = ('clara', '¡Nos vemos!')
STORY = [
    ('rocio', '¡Mete bien esa esquina de la sábana, Clara! Aquí van las dos almohadas blandas.', 'Tuck that corner of the sheet in tight, Clara! Here go the two soft pillows.'),
    ('clara', '¡Listo! Y la alfombra azul cabe justo al lado de la cama.', 'Done! And the blue rug fits right beside the bed.'),
    ('ernesto', '¿Dónde cuelgo este espejo redondo? ¿A la izquierda de la ventana o a la derecha?', 'Where do I hang this round mirror? Left of the window or right?'),
    ('clara', 'Justo al lado del escritorio, donde hay buena luz.', 'Right beside the desk, where there is good light.'),
    ('rocio', 'Enchufa la lámpara de latón de Mateo... ¡ay, mira qué luz amarilla tan cálida!', "Plug in Mateo's brass lamp... oh, look how warm that yellow light is!"),
    ('ernesto', 'Sinceramente, ¡casi quiero dormir yo mismo aquí arriba esta noche!', 'Honestly, I almost want to sleep up here myself tonight!'),
    ('clara', 'Un momento: ¿qué descuento le ofrecemos por cambiar de habitación?', 'Wait a moment: what discount do we offer him for changing rooms?'),
    ('ernesto', '¡A mitad de precio esta noche, y desayuno gratis toda la semana!', 'Half price tonight, and free breakfast all week!'),
    ('rocio', '¡Qué generoso! ¿Habéis oído el timbre de la puerta del patio abajo?', 'How generous! Did you two hear the courtyard gate bell downstairs?'),
    ('clara', '¡Las ocho en punto! ¡Nuestro cliente ya está aquí!', "Eight o'clock on the dot! Our guest is already here!"),
    ('ernesto', '¡Me late el corazón a mil! Clara, explíquelo usted: ¡suena tranquila y sincera!', 'My heart is racing! Clara, you explain it: you sound calm and honest!'),
    ('clara', 'Déjemelo a mí. Vamos abajo a darle la bienvenida.', 'Leave it to me. Let us go down and welcome him.'),
]
WALK = [
    (0, None, ["'Tuck that corner of the sheet in tight, Clara! Here go the two soft pillows.'", (None, 'Mete bien'), "literally says 'put in well' for tucking bedsheets neatly."]),
    (1, None, ["'Done! And the blue rug fits right beside the bed.' When an object fits into a space, Spanish uses", (None, 'cabe'), 'rather than the clothing-fit word we heard in Episode 1.']),
    (2, None, ["'Where do I hang this round mirror? Left of the window or right?' Pair", (None, 'A la izquierda'), 'and', (None, 'a la derecha'), "for 'on the left' and 'on the right'—crucial direction chunks."]),
    (3, None, ["'Right beside the desk, where there is good light.' Putting", (None, 'Justo al lado'), "together sharpens 'beside' into 'right beside'."]),
    (4, None, ["'Plug in Mateo's brass lamp... oh, look how warm that yellow light is!' Because Spanish has no apostrophe-s,", (None, 'la lámpara de latón de Mateo'), "chains 'of brass of Mateo'."]),
    (5, None, ["'Honestly, I almost want to sleep up here myself tonight!'", (None, 'aquí arriba'), "puts 'here' before 'up' where English says 'up here'."]),
    (6, None, ["'Wait a moment: what discount do we offer him for changing rooms?' Look at", (None, 'cambiar de habitación'), "literally 'change of room', the pattern Spanish uses for switching trains, jobs, or rooms."]),
    (7, None, ["'Half price tonight, and free breakfast all week!' Two travel favourites in one line:", (None, 'A mitad de precio'), 'for half price, and', (None, 'gratis'), 'unchanged whether singular or plural.']),
    (8, None, ["'How generous! Did you two hear the courtyard gate bell downstairs?' Asking Clara and Ernesto together, Rocio uses Spain's plural", (None, 'Habéis oído'), "for 'have you two heard?'."]),
    (9, None, ["'Eight o'clock on the dot! Our guest is already here!' Add", (None, 'en punto'), "literally 'on point', after any hour to mean 'on the dot' or 'sharp'."]),
    (10, None, ["'My heart is racing! Clara, you explain it: you sound calm and honest!' Saying one's heart beats", (None, 'a mil'), "literally 'at a thousand', captures a racing pulse."]),
    (11, None, ["'Leave it to me. Let us go down and welcome him.'", (None, 'Déjemelo a mí'), "stacks 'leave-me-it' smoothly into a single reassuring word."]),
]
