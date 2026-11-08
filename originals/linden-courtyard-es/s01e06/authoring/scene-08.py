# Authoring module for linden-courtyard-es-s01e06-scene-08.
ID = 'linden-courtyard-es-s01e06-scene-08'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 6
SCENE = 8
TITLE = 'Room Nine  (La habitación nueve)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = 'Ya entrada la noche del viernes, cuando el patio queda en silencio, Hannah y Arthur cierran la recepción mientras Graham sube del sótano trasero cargando sillas extra y un cofre de madera cubierto de polvo. Escucha primero.'
OPENER = 'Repasemos con calma la escena final de la primera temporada.'
TRANSITION = 'Escuchemos una última vez toda la escena a velocidad natural.'
OUTRO = '¡Una novena llave de latón, un cofre de cedro marcado con Habitación Nueve y un plano que muestra una puerta oculta en esta planta! Has completado la primera temporada de la posada Linden Courtyard Inn. ¡Nos vemos en la segunda temporada!'
CLOSING = ('graham', 'Until tomorrow!')
STORY = [
    ('hannah', 'Did you find the three folding chairs behind the boiler room, Graham?', '¿Encontraste las tres sillas plegables detrás de la sala de calderas, Graham?'),
    ('graham', 'Found the chairs, and behind an old brick wall, I found this.', 'Encontré las sillas y, detrás de un viejo muro de ladrillo, encontré esto.'),
    ('arthur', 'A small cedar chest? I have never seen that box in fifteen years!', '¿Un pequeño cofre de cedro? ¡Jamás he visto esa caja en quince años!'),
    ('hannah', 'Brush the dust off the brass plate on top... wait, read that number!', 'Quita con la mano el polvo de la placa de latón de arriba... ¡espera, lee ese número!'),
    ('arthur', "Let me pull my glasses down from my forehead... 'Room Nine'?!", "Déjenme bajar mis gafas de la frente... ¡¿'Habitación Nueve'?!"),
    ('hannah', 'Graham, look at the wooden key board behind us: one, two, three, four, five, six, seven, eight!', 'Graham, mira el tablero de madera de las llaves detrás de nosotros: ¡uno, dos, tres, cuatro, cinco, seis, siete, ocho!'),
    ('arthur', 'This guesthouse has only ever had eight rooms! Where on earth is Room Nine?!', '¡Esta posada jamás en su historia ha tenido más de ocho habitaciones! ¡¿Dónde diablos está la Habitación Nueve?!'),
    ('graham', 'Listen when I tilt the box. Something metal just slid inside.', 'Escuchen cuando inclino la caja. Algo de metal acaba de deslizarse dentro.'),
    ('hannah', 'There is a tiny keyhole on the front latch, and look taped underneath: an old brass key!', '¡Hay una cerradura diminuta en el cierre delantero, y miren pegada debajo con cinta: una vieja llave de latón!'),
    ('arthur', 'A ninth brass key?! Do we open it tonight or wait until morning?!', '¡¿Una novena llave de latón?! ¡¿La abrimos esta noche o esperamos hasta la mañana?!'),
    ('graham', 'Look at the folded blueprint sticking out of the hinge. There is a hidden door drawn on this floor!', 'Miren el plano doblado que asoma por la bisagra. ¡Hay una puerta oculta dibujada en esta planta!'),
    ('hannah', 'Grab the flashlight, both of you. My second week starts right now!', 'Agarren la linterna los dos. ¡Mi segunda semana empieza ahora mismo!'),
]
WALK = [
    (0, None, ["'¿Encontraste las tres sillas plegables detrás de la sala de calderas, Graham?' En", (None, 'folding chairs'), "la forma en '-ing' describe para qué están hechas: sillas plegables."]),
    (1, None, ["'Encontré las sillas y, detrás de un viejo muro de ladrillo, encontré esto.' En conversación informal Graham omite el sujeto inicial en", (None, 'Found the chairs'), 'dando su tono seco habitual.']),
    (2, None, ["'¿Un pequeño cofre de cedro? ¡Jamás he visto esa caja en quince años!' La experiencia acumulada hasta hoy se expresa con", (None, 'I have never seen'), 'nunca he visto.']),
    (3, None, ["'Quita con la mano el polvo de la placa de latón de arriba... ¡espera, lee ese número!' El verbo", (None, 'Brush the dust off'), "usa 'off' para apartar el polvo de una superficie."]),
    (4, None, ["'Déjenme bajar mis gafas de la frente... ¡¿Habitación Nueve?!' Mira el recorrido físico completo en", (None, 'pull my glasses down from'), 'bajar tirando suavemente desde la frente.']),
    (5, None, ["'Graham, mira el tablero de madera de las llaves detrás de nosotros: ¡uno, dos, tres, cuatro, cinco, seis, siete, ocho!' Detrás de una preposición usamos el pronombre objeto:", (None, 'behind us'), 'detrás de nosotros.']),
    (6, None, ["'¡Esta posada jamás en su historia ha tenido más de ocho habitaciones! ¡¿Dónde diablos está la Habitación Nueve?!' Para expresar perplejidad limpia y muy natural, añade", (None, 'Where on earth'), "literalmente '¿dónde en la tierra?'."]),
    (7, None, ["'Escuchen cuando inclino la caja. Algo de metal acaba de deslizarse dentro.' Con 'something', el material o adjetivo también va detrás:", (None, 'Something metal'), 'algo metálico.']),
    (8, None, ["'¡Hay una cerradura diminuta en el cierre delantero, y miren pegada debajo con cinta: una vieja llave de latón!' El compuesto transparente", (None, 'keyhole'), "une 'llave' y 'agujero' para el ojo de la cerradura."]),
    (9, None, ["'¡¿Una novena llave de latón?! ¡¿La abrimos esta noche o esperamos hasta la mañana?!' De 'nine' sale el ordinal", (None, 'ninth'), "escritura sin la 'e' final."]),
    (10, None, ["'Miren el plano doblado que asoma por la bisagra. ¡Hay una puerta oculta dibujada en esta planta!' El giro", (None, 'sticking out of'), 'describe algo que sobresale o asoma por una rendija.']),
    (11, None, ["'Agarren la linterna los dos. ¡Mi segunda semana empieza ahora mismo!' Con presente simple y energía de aventura,", (None, 'starts right now'), 'cierra la temporada por todo lo alto.']),
]
