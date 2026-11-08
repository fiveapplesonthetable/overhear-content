# Authoring module for linden-courtyard-es-s01e05-scene-04.
ID = 'linden-courtyard-es-s01e05-scene-04'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 5
SCENE = 4
TITLE = 'Two Chairs Under the Tree  (Dos sillas bajo el árbol)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'A las once en punto, el aroma dulce del pastel de limón llega hasta el patio mientras Hannah, Tessa y Graham preparan una mesita redonda bajo la sombra del árbol. Escuchemos primero.'
OPENER = 'Vamos a repasar el diálogo frase por frase.'
TRANSITION = 'Escuchemos otra vez toda la escena a ritmo normal.'
OUTRO = 'Dos sillas bajo el árbol, pastel tibio enfriándose en la rejilla y cuarenta minutos en el reloj. En la próxima escena, Hannah ayuda a Caleb a elegir sus primeras palabras. Hasta pronto.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Let us put the small wooden table right here under the tree, away from the door.', 'Pongamos la mesita de madera justo aquí bajo el árbol, lejos de la puerta.'),
    ('graham', 'Good spot. Two solid chairs, facing the garden herbs instead of the lobby window.', 'Buen sitio. Dos sillas firmes, mirando hacia las hierbas del jardín en vez de a la ventana del vestíbulo.'),
    ('tessa', 'Here is a clean white cloth and two blue teacups.', 'Aquí hay un mantel blanco limpio y dos tazas de té azules.'),
    ('hannah', 'Graham, are you hanging those paper lanterns for noon?', 'Graham, ¿estás colgando esos faroles de papel para el mediodía?'),
    ('graham', 'The wire needed straightening anyway. Nothing sentimental about good maintenance.', 'El cable necesitaba enderezarse de todos modos. No hay nada sentimental en un buen mantenimiento.'),
    ('tessa', 'Oh, listen to Mister Maintenance! Yesterday you fixed the boiler, today you fix two brothers!', '¡Oh, escuchen al Señor Mantenimiento! ¡Ayer arreglaste la caldera y hoy arreglas a dos hermanos!'),
    ('graham', 'I fix pipes and chairs. People have to fix their own words.', 'Yo arreglo tuberías y sillas. La gente tiene que arreglar sus propias palabras.'),
    ('hannah', 'What time does your watch say now, Graham?', '¿Qué hora marca tu reloj ahora, Graham?'),
    ('graham', 'Eleven twenty. Cake ready, Tessa?', 'Las once y veinte. ¿Listo el pastel, Tessa?'),
    ('tessa', 'Cooling on the rack right now, golden crust and sweet lemon sugar!', '¡Enfriándose en la rejilla ahora mismo, corteza dorada y azúcar dulce de limón!'),
    ('hannah', 'Look upstairs at the attic window: Caleb has changed his shirt three times!', 'Miren arriba a la ventana del ático: ¡Caleb se ha cambiado de camisa tres veces!'),
    ('tessa', 'Go talk to him, Hannah, before he wears out the wooden floor!', '¡Ve a hablar con él, Hannah, antes de que desgaste el suelo de madera!'),
]
WALK = [
    (0, None, ["'Pongamos la mesita de madera justo aquí bajo el árbol, lejos de la puerta.' Para indicar distancia respecto a un punto de paso se usa", (None, 'away from the door'), 'apartada de la puerta.']),
    (1, None, ["'Buen sitio. Dos sillas firmes, mirando hacia las hierbas del jardín en vez de a la ventana del vestíbulo.' El participio", (None, 'facing'), "viene de 'cara' y significa 'orientadas hacia'."]),
    (2, None, ["'Aquí hay un mantel blanco limpio y dos tazas de té azules.' La misma palabra", (None, 'cloth'), 'sirve tanto para un paño de limpieza como para un mantel de mesa.']),
    (3, None, ["'Graham, ¿estás colgando esos faroles de papel para el mediodía?' Al hacer una pregunta en presente continuo, el verbo auxiliar 'are' salta delante del sujeto:", (None, 'are you hanging'), "¿estás tú colgando?"]),
    (4, None, ["'El cable necesitaba enderezarse de todos modos. No hay nada sentimental en un buen mantenimiento.' Tras 'need', el inglés permite usar '-ing' con sentido pasivo:", (None, 'needed straightening'), 'necesitaba ser enderezado.']),
    (5, None, ["'¡Oh, escuchen al Señor Mantenimiento! ¡Ayer arreglaste la caldera y hoy arreglas a dos hermanos!' El apodo juguetón", (None, 'Mister Maintenance'), 'personifica el oficio con humor cariñoso.']),
    (6, None, ["'Yo arreglo tuberías y sillas. La gente tiene que arreglar sus propias palabras.' Con 'people' en plural, su posesivo correspondiente es", (None, 'their own words'), 'sus propias palabras.']),
    (7, None, ["'¿Qué hora marca tu reloj ahora, Graham?' En inglés los relojes literalmente 'dicen' la hora:", (None, 'What time does your watch say'), '¿qué hora marca tu reloj?']),
    (8, None, ["'Las once y veinte. ¿Listo el pastel, Tessa?' En conversación ágil entre compañeros basta unir sustantivo y adjetivo:", (None, 'Cake ready'), '¿listo el pastel?']),
    (9, None, ["'¡Enfriándose en la rejilla ahora mismo, corteza dorada y azúcar dulce de limón!' Para bandejas o rejillas de repostería usamos", (None, 'on the rack'), 'sobre la rejilla.']),
    (10, None, ["'Miren arriba a la ventana del ático: ¡Caleb se ha cambiado de camisa tres veces!' Mientras que una vez es 'once' y dos es 'twice', a partir de tres se dice", (None, 'three times'), 'tres veces.']),
    (11, None, ["'¡Ve a hablar con él, Hannah, antes de que desgaste el suelo de madera!' El verbo con partícula", (None, 'wears out'), 'significa gastar algo de tanto usarlo o pisarlo.']),
]
