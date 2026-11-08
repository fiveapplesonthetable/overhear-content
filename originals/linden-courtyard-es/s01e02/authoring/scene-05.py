# Authoring module for linden-courtyard-es-s01e02-scene-05.
ID = 'linden-courtyard-es-s01e02-scene-05'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = 'Juice on the Tie  (Zumo en la corbata)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'arthur': 'Arthur', 'evelyn': 'Evelyn', 'hannah': 'Hannah'}
INTRO = 'El desayuno está en pleno apogeo en el soleado rincón del café. Evelyn se sienta junto a la ventana mientras Arthur insiste en ayudar a Hannah a servir las bebidas como anfitrión de gran hotel. Escucha primero.'
OPENER = 'Repasemos cada línea de esta escena en el comedor.'
TRANSITION = 'Escuchemos otra vez toda la escena sin interrupciones.'
OUTRO = 'A Evelyn le encantó el desayuno, aunque la corbata de Arthur se bebió casi todo el zumo de naranja. Muy pronto el teléfono de recepción traerá noticias sobre la maleta misteriosa. Hasta la próxima.'
CLOSING = ('evelyn', 'Take care!')
STORY = [
    ('hannah', 'Good morning again, Miss Evelyn! Would you like coffee or black tea?', '¡Buenos días de nuevo, señorita Evelyn! ¿Le gustaría café o té negro?'),
    ('evelyn', 'Black tea without sugar, please, and one slice of warm bread.', 'Té negro sin azúcar, por favor, y una rebanada de pan tibio.'),
    ('arthur', "Allow me to pour the fresh orange juice, ma'am!", '¡Permítame servirle el zumo de naranja recién exprimido, señora!'),
    ('evelyn', 'Oh, how kind of you, sir. Just half a glass.', '¡Oh, qué amable de su parte, caballero! Solo medio vaso.'),
    ('arthur', 'At our guesthouse, five-star service comes naturally... whoops!', 'En nuestra posada, el servicio de cinco estrellas sale solo... ¡ups!'),
    ('hannah', 'Careful, Arthur, the pitcher spout is wide!', '¡Cuidado, Arthur, que el pico de la jarra es ancho!'),
    ('arthur', 'Oh dear! Not a drop on the table, thank goodness... all of it is on my tie!', '¡Ay, madre! Ni una gota en la mesa, menos mal... ¡está todo en mi corbata!'),
    ('evelyn', 'Do not worry! Cold sparkling water takes orange juice right out.', '¡No se preocupe! El agua fría con gas quita el zumo de naranja enseguida.'),
    ('hannah', 'Here is a clean cloth and cold water, Arthur.', 'Aquí tiene un paño limpio y agua fría, Arthur.'),
    ('arthur', "Excuse me, ma'am, I shall retreat to my office with dignity!", '¡Disculpe, señora, me retiraré a mi despacho con dignidad!'),
    ('evelyn', 'The scrambled eggs are delicious, Hannah. Tell Tessa my compliments!', 'Los huevos revueltos están deliciosos, Hannah. ¡Felicite a Tessa de mi parte!'),
    ('hannah', 'I will! Enjoy your morning.', '¡De su parte! Que disfrute la mañana.'),
]
WALK = [
    (0, None, ["'¡Buenos días de nuevo, señorita Evelyn! ¿Le gustaría café o té negro?' Al ofrecer algo en mesa o recepción,", (None, 'Would you like'), 'suena mucho más amable y educado que preguntar si quiere a secas.']),
    (1, None, ["'Té negro sin azúcar, por favor, y una rebanada de pan tibio.' Como el pan es incontable en inglés, para pedir una unidad concreta decimos", (None, 'one slice of warm bread'), 'una rebanada.']),
    (2, None, ["'¡Permítame servirle el zumo de naranja recién exprimido, señora!' En registro muy cortés,", (None, 'Allow me to pour'), 'une el permiso formal con la acción de servir líquidos.']),
    (3, None, ["'¡Oh, qué amable de su parte, caballero! Solo medio vaso.' Agradecer un gesto cortés con", (None, 'how kind of you'), 'es elegancia pura, y fíjate en el orden de', (None, 'half a glass'), 'donde la mitad va delante del artículo.']),
    (4, None, ["'En nuestra posada, el servicio de cinco estrellas sale solo... ¡ups!' Cuando un número acompaña a un sustantivo como adjetivo en", (None, 'five-star service'), 'estrella va en singular, y', (None, 'whoops'), "es el '¡uy!' de un tropiezo."]),
    (5, None, ["'¡Cuidado, Arthur, que el pico de la jarra es ancho!' Para avisar rápido de un peligro inmediato basta una sola palabra:", (None, 'Careful'), 'sin verbo ninguno.']),
    (6, None, ["'¡Ay, madre! Ni una gota en la mesa, menos mal... ¡está todo en mi corbata!' La exclamación de alivio", (None, 'thank goodness'), "funciona igual que 'menos mal' o 'gracias a Dios'."]),
    (7, None, ["'¡No se preocupe! El agua fría con gas quita el zumo de naranja enseguida.' El agua con gas se pide como", (None, 'sparkling water'), 'agua chispeante, y', (None, 'takes orange juice right out'), 'significa quitar una mancha por completo.']),
    (8, None, ["'Aquí tiene un paño limpio y agua fría, Arthur.' La palabra", (None, 'cloth'), 'designa un trapo o paño de tela limpia para secar la mesa.']),
    (9, None, ["'¡Disculpe, señora, me retiraré a mi despacho con dignidad!' Arthur exagera su tono solemne usando", (None, 'I shall retreat'), 'que hoy suena teatral y humorísticamente formal.']),
    (10, None, ["'Los huevos revueltos están deliciosos, Hannah. ¡Felicite a Tessa de mi parte!' Para transmitir saludos o felicitaciones se dice literalmente 'dile mis cumplidos':", (None, 'Tell Tessa my compliments'), "."]),
    (11, None, ["'¡De su parte! Que disfrute la mañana.' Prometer que harás un recado se resume en dos palabras:", (None, 'I will'), "literalmente 'lo haré'."]),
]
