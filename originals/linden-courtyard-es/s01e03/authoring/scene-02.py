# Authoring module for linden-courtyard-es-s01e03-scene-02.
ID = 'linden-courtyard-es-s01e03-scene-02'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = 'The Sunny Attic  (El ático soleado)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = 'Arriba, bajo el tejado de madera del tercer piso, Graham abre el estudio del ático para Hannah mientras Tessa sube con toallas limpias. Escuchemos primero toda la escena.'
OPENER = 'Repasemos ahora cada intervención paso a paso.'
TRANSITION = 'Volvamos a escuchar la conversación completa de corrido.'
OUTRO = 'Con vigas de madera y lluvia sobre el tejado, al ático solo le faltan una lámpara, dos almohadas y una alfombra. Nos vemos en la próxima escena mientras corren contra el reloj.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('hannah', 'Oh, look at this room! Big wooden beams and a window over the courtyard!', '¡Oh, mira esta habitación! ¡Grandes vigas de madera y una ventana sobre el patio!'),
    ('tessa', 'Listen to the rain on the roof. It feels so cozy up here!', 'Escucha la lluvia en el tejado. ¡Se siente tan acogedor aquí arriba!'),
    ('graham', 'Dry, warm, and quiet. Now tell me what is missing.', 'Seco, cálido y tranquilo. Ahora dime qué falta.'),
    ('hannah', 'Okay: there is a bed, a table, and a chair, but no bedside lamp.', 'Vale: hay una cama, una mesa y una silla, pero ninguna lámpara de noche.'),
    ('tessa', 'And no mirror on the wall, and the floor feels bare without a rug.', 'Y ningún espejo en la pared, y el suelo se siente desnudo sin una alfombra.'),
    ('graham', 'There is a brass reading lamp in my workshop downstairs.', 'Hay una lámpara de lectura de latón en mi taller abajo.'),
    ('tessa', 'And I have two soft pillows and a woven blue rug in the closet!', '¡Y yo tengo dos almohadas suaves y una alfombra azul tejida en el armario!'),
    ('hannah', 'What about the small bathroom next door? Does the light work?', '¿Qué hay del baño pequeño de al lado? ¿Funciona la luz?'),
    ('graham', 'New bulb last week, clean soap, plenty of hot water.', 'Bombilla nueva la semana pasada, jabón limpio, mucha agua caliente.'),
    ('tessa', 'Give us fifteen minutes and this attic will beat room seven!', '¡Danos quince minutos y este ático superará a la habitación siete!'),
    ('hannah', 'Grab those cardboard boxes, Graham. Down the stairs we go!', 'Agarra esas cajas de cartón, Graham. ¡Escalera abajo vamos!'),
    ('graham', 'Careful on the turn, do not bump the wall!', '¡Cuidado en la curva, no golpees la pared!'),
]
WALK = [
    (0, None, ["'¡Oh, mira esta habitación! ¡Grandes vigas de madera y una ventana sobre el patio!' Para dirigir la mirada hacia algo concreto, el verbo va siempre acompañado de preposición en", (None, 'look at this room'), 'nunca solo.']),
    (1, None, ["'Escucha la lluvia en el tejado. ¡Se siente tan acogedor aquí arriba!' Igual pasa con escuchar:", (None, 'Listen to the rain'), 'exige esa pequeña preposición de dirección antes del sonido.']),
    (2, None, ["'Seco, cálido y tranquilo. Ahora dime qué falta.' En preguntas indirectas dentro de otra frase,", (None, 'what is missing'), 'mantiene el orden normal sin invertir el verbo.']),
    (3, None, ["'Vale: hay una cama, una mesa y una silla, pero ninguna lámpara de noche.' Para presentar lo que existe en un cuarto basta abrir con", (None, 'there is a bed'), 'en singular porque el primer objeto de la lista es singular.']),
    (4, None, ["'Y ningún espejo en la pared, y el suelo se siente desnudo sin una alfombra.' En cuadros y espejos colgados sobre superficies verticales, el inglés usa", (None, 'on the wall'), 'pensando en el contacto con la pared.']),
    (5, None, ["'Hay una lámpara de lectura de latón en mi taller abajo.' Una sola palabra,", (None, 'downstairs'), "resume 'en el piso de abajo' sin añadir preposiciones."]),
    (6, None, ["'¡Y yo tengo dos almohadas suaves y una alfombra azul tejida en el armario!' El participio", (None, 'woven'), 'actúa aquí como adjetivo delante del color para describir la textura artesanal.']),
    (7, None, ["'¿Qué hay del baño pequeño de al lado? ¿Funciona la luz?' Para cambiar de tema hacia otro detalle práctico,", (None, 'What about'), 'es el comodín conversacional más ágil del inglés.']),
    (8, None, ["'Bombilla nueva la semana pasada, jabón limpio, mucha agua caliente.' Con sustantivos incontables como el agua,", (None, 'plenty of hot water'), 'expresa abundancia con un tono muy positivo.']),
    (9, None, ["'¡Danos quince minutos y este ático superará a la habitación siete!' El verbo", (None, 'will beat'), 'no solo significa ganar un partido, sino también superar en calidad a otra opción.']),
    (10, None, ["'Agarra esas cajas de cartón, Graham. ¡Escalera abajo vamos!' Al adelantar la dirección en", (None, 'Down the stairs we go'), 'la frase gana ritmo y energía de equipo.']),
    (11, None, ["'¡Cuidado en la curva, no golpees la pared!' Para advertir que no ocurra algo por accidente, se abre con", (None, 'do not bump'), 'seguido del objeto directo.']),
]
