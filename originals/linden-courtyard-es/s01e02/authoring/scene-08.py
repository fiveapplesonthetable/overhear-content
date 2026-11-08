# Authoring module for linden-courtyard-es-s01e02-scene-08.
ID = 'linden-courtyard-es-s01e02-scene-08'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = 'Two Names, One Room  (Dos nombres, una habitación)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'El miércoles por la tarde, mientras anochece sobre Portland, Arthur sale de su despacho pálido sosteniendo tanto la tableta como el libro de papel de Graham. Hannah y Graham levantan la vista al instante. Escucha primero.'
OPENER = 'Revisemos línea por línea qué ha descubierto Arthur.'
TRANSITION = 'Volvamos a oír toda la escena a velocidad natural.'
OUTRO = 'Dos huéspedes reservados en la habitación siete, lluvia afuera y solo cuarenta minutos antes del tren de las ocho. ¡Así concluye el episodio dos; acompáñanos en el episodio tres para ver si el ático logra salvar la noche!'
CLOSING = ('arthur', 'See you tomorrow!')
STORY = [
    ('arthur', 'Graham... Hannah... please tell me room six is free tonight.', 'Graham... Hannah... por favor díganme que la habitación seis está libre esta noche.'),
    ('hannah', 'No, Arthur, the couple from the south checked into room six an hour ago.', 'No, Arthur, la pareja del sur se registró en la habitación seis hace una hora.'),
    ('graham', 'Every key from one to seven is taken, and room eight has wet paint.', 'Todas las llaves de la uno a la siete están ocupadas, y la habitación ocho tiene pintura fresca.'),
    ('arthur', 'Oh, disaster! Yesterday I took a phone booking on the tablet without my glasses!', '¡Qué desastre! ¡Ayer anoté una reserva telefónica en la tableta sin mis gafas!'),
    ('hannah', 'Wait, let me look at the tablet screen and the paper book together.', 'Espera, déjame mirar juntos la pantalla de la tableta y el libro de papel.'),
    ('graham', 'Let me guess. You promised somebody a room we do not have?', 'Déjame adivinar. ¿Le prometiste a alguien una habitación que no tenemos?'),
    ('hannah', 'Arthur! Room seven is already occupied, and you booked a second guest into room seven!', '¡Arthur! ¡La habitación siete ya está ocupada y reservaste a un segundo huésped en la habitación siete!'),
    ('arthur', "And he arrives on the eight o'clock evening train, in forty minutes!", '¡Y llega en el tren de las ocho de la tarde, en cuarenta minutos!'),
    ('graham', 'Told you that tablet is a trap.', 'Te dije que esa tableta es una trampa.'),
    ('arthur', 'It is raining outside and every hotel on our street is full! What do we do?', '¡Está lloviendo afuera y todos los hoteles de nuestra calle están llenos! ¿Qué hacemos?'),
    ('hannah', 'Wait, what is on the third floor above the stairs?', 'Espera, ¿qué hay en el tercer piso arriba de las escaleras?'),
    ('graham', 'The old sunny attic study... follow me, quickly!', 'El viejo estudio soleado del ático... ¡sígueme, rápido!'),
]
WALK = [
    (0, None, ["'Graham... Hannah... por favor díganme que la habitación seis está libre esta noche.' Una habitación disponible y sin ocupar se describe sencillamente como", (None, 'is free tonight'), "'está libre esta noche'."]),
    (1, None, ["'No, Arthur, la pareja del sur se registró en la habitación seis hace una hora.' Registrarse al entrar en una habitación concreta pasa a", (None, 'checked into room six'), 'seguido del número.']),
    (2, None, ["'Todas las llaves de la uno a la siete están ocupadas, y la habitación ocho tiene pintura fresca.' Ojo al modismo de los carteles:", (None, 'wet paint'), "dice literalmente 'pintura mojada' donde nosotros decimos 'recién pintado'."]),
    (3, None, ["'¡Qué desastre! ¡Ayer anoté una reserva telefónica en la tableta sin mis gafas!' Con pantallas y dispositivos electrónicos el inglés emplea preposición de contacto:", (None, 'on the tablet'), 'en la tableta.']),
    (4, None, ["'Espera, déjame mirar juntos la pantalla de la tableta y el libro de papel.' Colocado al final,", (None, 'together'), 'indica comparar ambas cosas a la vez, una al lado de la otra.']),
    (5, None, ["'Déjame adivinar. ¿Le prometiste a alguien una habitación que no tenemos?' Antes de soltar una deducción irónica,", (None, 'Let me guess'), "funciona idéntico a nuestro 'déjame adivinar'."]),
    (6, None, ["'¡Arthur! ¡La habitación siete ya está ocupada y reservaste a un segundo huésped en la habitación siete!' La misma palabra que nombra un libro sirve como verbo para reservar en", (None, 'you booked'), "'hiciste una reserva'."]),
    (7, None, ["'¡Y llega en el tren de las ocho de la tarde, en cuarenta minutos!' Para horarios oficiales de trenes y vuelos, el presente simple", (None, 'he arrives'), 'es completamente natural en inglés.']),
    (8, None, ["'Te dije que esa tableta es una trampa.' En conversación informal es muy común omitir el sujeto inicial en", (None, 'Told you'), "el clásico 'te lo dije'."]),
    (9, None, ["'¡Está lloviendo afuera y todos los hoteles de nuestra calle están llenos! ¿Qué hacemos?' Para pedir un plan urgente en presente,", (None, 'What do we do'), "pregunta directamente '¿qué hacemos?'."]),
    (10, None, ["'Espera, ¿qué hay en el tercer piso arriba de las escaleras?' Recuerda que en Estados Unidos la planta baja cuenta como primer piso, así que", (None, 'on the third floor'), 'está dos plantas más arriba.']),
    (11, None, ["'El viejo estudio soleado del ático... ¡sígueme, rápido!' Dos palabras llenas de acción para cerrar el episodio:", (None, 'follow me'), 'sígueme.']),
]
