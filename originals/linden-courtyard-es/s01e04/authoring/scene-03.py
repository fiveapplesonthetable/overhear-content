# Authoring module for linden-courtyard-es-s01e04-scene-03.
ID = 'linden-courtyard-es-s01e04-scene-03'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 4
SCENE = 3
TITLE = 'Hot Cinnamon Rolls  (Rollos de canela calientes)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'tessa': 'Tessa', 'evelyn': 'Evelyn', 'arthur': 'Arthur'}
INTRO = 'Back at the inn, Evelyn walks down at seven ten in her dressing gown, hoping for tea before her morning wash. Tessa and Arthur exchange a quick look and launch their distraction plan. Listen first.'
OPENER = 'Ahora recorramos la escena paso a paso.'
TRANSITION = 'Escuchemos de nuevo toda la conversación seguida.'
OUTRO = 'Los rollos de canela calientes les dieron exactamente los diez minutos que necesitaban mientras Hannah entraba corriendo por el patio. En la próxima escena bajamos a la sala de calderas.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('evelyn', 'Good morning! Something smells like warm cinnamon all the way upstairs!', '¡Buenos días! ¡Algo huele a canela tibia hasta arriba del todo!'),
    ('tessa', 'Good morning, Miss Evelyn! My cinnamon rolls just came out of the oven.', '¡Buenos días, señorita Evelyn! Mis rollos de canela acaban de salir del horno.'),
    ('arthur', "Sit right down by the sunny window, ma'am! No rush to go upstairs yet!", '¡Siéntese aquí mismo junto a la ventana soleada, señora! ¡Sin prisa por subir todavía!'),
    ('evelyn', 'Actually, I only came down to ask why the bathroom tap felt so chilly.', 'En realidad, solo bajé a preguntar por qué el grifo del baño se sentía tan frío.'),
    ('arthur', 'Chilly? Ah, yes! Our neighborhood water pipes take a gentle morning stretch!', '¿Frío? ¡Ah, sí! ¡Las tuberías de agua de nuestro barrio hacen un suave estiramiento matutino!'),
    ('tessa', 'Have a hot cup of tea and a cinnamon roll for ten minutes first!', '¡Tómese primero una taza de té caliente y un rollo de canela durante diez minutos!'),
    ('evelyn', 'Well, nobody wise says no to warm cinnamon bread at seven in the morning.', 'Bueno, nadie sensato le dice que no al pan tibio de canela a las siete de la mañana.'),
    ('arthur', 'Wonderful choice! Would you like honey or apple jam beside it?', '¡Excelente elección! ¿Le gustaría miel o mermelada de manzana al lado?'),
    ('evelyn', 'Just a little butter, thank you. Why are you looking at your watch, sir?', 'Solo un poco de mantequilla, gracias. ¿Por qué está mirando su reloj, señor?'),
    ('arthur', 'Me? Oh, I simply love being on time! Seven fourteen is a beautiful minute!', '¿Yo? ¡Oh, simplemente me encanta ser puntual! ¡Las siete y catorce es un minuto precioso!'),
    ('tessa', 'Look through the courtyard window, Arthur. Someone just ran through the gate!', 'Mira por la ventana del patio, Arthur. ¡Alguien acaba de entrar corriendo por la verja!'),
    ('arthur', "Saved! Excuse me one moment, ma'am, enjoy your hot tea!", '¡Salvados! Disculpe un momento, señora, ¡disfrute de su té caliente!'),
]
WALK = [
    (0, None, ["'¡Buenos días! ¡Algo huele a canela tibia hasta arriba del todo!' Cuando comparas un olor con un ingrediente concreto añades 'like':", (None, 'smells like warm cinnamon'), 'huele a canela tibia.']),
    (1, None, ["'¡Buenos días, señorita Evelyn! Mis rollos de canela acaban de salir del horno.' Otra vez el pasado con 'just',", (None, 'just came out'), "expresa 'acaban de salir' de manera muy ágil."]),
    (2, None, ["'¡Siéntese aquí mismo junto a la ventana soleada, señora! ¡Sin prisa por subir todavía!' Intercalar 'right' dentro de", (None, 'Sit right down'), 'hace la invitación mucho más cálida e inmediata.']),
    (3, None, ["'En realidad, solo bajé a preguntar por qué el grifo del baño se sentía tan frío.' Cuidado con el falso amigo", (None, 'Actually'), "que no significa 'actualmente', sino 'en realidad' o 'la verdad es que'."]),
    (4, None, ["'¿Frío? ¡Ah, sí! ¡Las tuberías de agua de nuestro barrio hacen un suave estiramiento matutino!' El adjetivo", (None, 'Chilly'), 'describe un fresco incómodo sin llegar a helar.']),
    (5, None, ["'¡Tómese primero una taza de té caliente y un rollo de canela durante diez minutos!' Para ofrecer comida o bebida en mesa, el inglés prefiere", (None, 'Have a hot cup'), "en lugar de usar 'take'."]),
    (6, None, ["'Bueno, nadie sensato le dice que no al pan tibio de canela a las siete de la mañana.' Con pronombres indefinidos como 'nobody', el adjetivo va detrás:", (None, 'nobody wise'), 'nadie sabio o sensato.']),
    (7, None, ["'¡Excelente elección! ¿Le gustaría miel o mermelada de manzana al lado?' Para ofrecer algo con cortesía en cafetería o restaurante, la llave maestra es", (None, 'Would you like'), '¿le gustaría?']),
    (8, None, ["'Solo un poco de mantequilla, gracias. ¿Por qué está mirando su reloj, señor?' Con cantidades incontables pequeñas se dice", (None, 'Just a little butter'), 'solo un poco de mantequilla.']),
    (9, None, ["'¿Yo? ¡Oh, simplemente me encanta ser puntual! ¡Las siete y catorce es un minuto precioso!' Tras 'love' usamos '-ing' para hablar de gustos generales:", (None, 'love being on time'), 'encantar llegar puntual.']),
    (10, None, ["'Mira por la ventana del patio, Arthur. ¡Alguien acaba de entrar corriendo por la verja!' Para mirar a través de un cristal se usa", (None, 'through the courtyard window'), 'atravesando con la vista la ventana.']),
    (11, None, ["'¡Salvados! Disculpe un momento, señora, ¡disfrute de su té caliente!' El verbo", (None, 'enjoy your hot tea'), 'va directo al objeto sin ninguna preposición en medio.']),
]
