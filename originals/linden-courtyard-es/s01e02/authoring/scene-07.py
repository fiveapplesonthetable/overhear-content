# Authoring module for linden-courtyard-es-s01e02-scene-07.
ID = 'linden-courtyard-es-s01e02-scene-07'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 2
SCENE = 7
TITLE = 'How Regulars Order  (Cómo piden los habituales)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Bajo el sol tranquilo de la tarde, Hannah se toma un descanso de diez minutos en el rincón del café mientras Tessa limpia la barra y Graham aprieta la pata floja de una silla de madera. Escucha primero.'
OPENER = 'Repasemos con calma cada frase de este respiro vespertino.'
TRANSITION = 'Escuchemos otra vez toda la escena de principio a fin.'
OUTRO = 'Una taza tranquila de café, una silla ajustada y tres compañeros que ya empiezan a sentirse un verdadero equipo. Queda una escena en el episodio dos, y Arthur está a punto de llevarse un susto. Hasta pronto.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('tessa', 'Sit down, Hannah! You ran half the city this morning, drink some coffee.', '¡Siéntate, Hannah! Esta mañana recorriste media ciudad corriendo; tómate un café.'),
    ('hannah', 'Gladly! With milk and a little sugar, please.', '¡Con mucho gusto! Con leche y un poquito de azúcar, por favor.'),
    ('graham', 'Watch that corner chair, wait ten seconds while I tighten this screw.', 'Cuidado con esa silla de la esquina; espera diez segundos mientras aprieto este tornillo.'),
    ('hannah', 'Done already? You carry a screwdriver everywhere, Graham!', '¿Ya está listo? ¡Llevas un destornillador a todas partes, Graham!'),
    ('graham', 'Old houses loosen one screw every Tuesday. Now sit.', 'Las casas viejas aflojan un tornillo cada martes. Ahora siéntate.'),
    ('tessa', 'Look, you survived the breakfast rush and the mystery phone call!', '¡Mira, sobreviviste al ajetreo del desayuno y a la llamada misteriosa!'),
    ('hannah', 'Honestly, I like it here much better than my old gray office.', 'Sinceramente, aquí estoy mucho más a gusto que en mi vieja oficina gris.'),
    ('tessa', 'Wait until Friday at noon, I want a front row seat when the suitcase man walks in!', 'Espera al viernes al mediodía; ¡quiero un asiento en primera fila cuando entre el hombre de la maleta!'),
    ('graham', 'Nobody stares at guests. We hand over the bag and mind our business.', 'Nadie se queda mirando fijo a los huéspedes. Entregamos la maleta y nos metemos en nuestros asuntos.'),
    ('tessa', 'Listen to him! Graham is twice as curious as we are!', '¡Escúchalo! ¡Graham tiene el doble de curiosidad que nosotras!'),
    ('graham', 'I am simply checking security. That is my job.', 'Simplemente estoy revisando la seguridad. Ese es mi trabajo.'),
    ('hannah', 'Sure, Graham, your secret is safe with us!', '¡Claro, Graham, tu secreto está a salvo con nosotras!'),
]
WALK = [
    (0, None, ["'¡Siéntate, Hannah! Esta mañana recorriste media ciudad corriendo; tómate un café.' Fíjate otra vez en cómo se coloca la mitad delante del artículo en", (None, 'half the city'), "'media ciudad', sin preposición intermedia."]),
    (1, None, ["'¡Con mucho gusto! Con leche y un poquito de azúcar, por favor.' Con sustantivos incontables como el azúcar, 'un poco de' se dice directo", (None, 'a little sugar'), 'sin preposición.']),
    (2, None, ["'Cuidado con esa silla de la esquina; espera diez segundos mientras aprieto este tornillo.' Del adjetivo 'apretado' nace el verbo", (None, 'tighten'), 'apretar un tornillo.']),
    (3, None, ["'¿Ya está listo? ¡Llevas un destornillador a todas partes, Graham!' La herramienta", (None, 'screwdriver'), 'explica su función a la perfección: lo que impulsa o gira un tornillo.']),
    (4, None, ["'Las casas viejas aflojan un tornillo cada martes. Ahora siéntate.' Aquí escuchas la pareja opuesta a la anterior:", (None, 'loosen'), 'aflojar, junto con', (None, 'every Tuesday'), "'todos los martes'."]),
    (5, None, ["'¡Mira, sobreviviste al ajetreo del desayuno y a la llamada misteriosa!' En inglés no 'sobrevives a algo', sino que el verbo va directo sin preposición:", (None, 'survived the breakfast rush'), 'la hora punta del desayuno.']),
    (6, None, ["'Sinceramente, aquí estoy mucho más a gusto que en mi vieja oficina gris.' Para reforzar el comparativo irregular, el inglés une", (None, 'much better than'), 'mucho mejor que.']),
    (7, None, ["'Espera al viernes al mediodía; ¡quiero un asiento en primera fila cuando entre el hombre de la maleta!' Aunque hable del futuro del viernes, en cláusulas temporales el inglés usa presente simple:", (None, 'when the suitcase man walks in'), "'cuando entre'."]),
    (8, None, ["'Nadie se queda mirando fijo a los huéspedes. Entregamos la maleta y nos metemos en nuestros asuntos.' Quedarse mirando fijamente es", (None, 'stares at'), 'y', (None, 'mind our business'), 'significa ocuparse de los propios asuntos.']),
    (9, None, ["'¡Escúchalo! ¡Graham tiene el doble de curiosidad que nosotras!' Las comparaciones de multiplicación se arman con", (None, 'twice as curious as'), "'el doble de curioso que'."]),
    (10, None, ["'Simplemente estoy revisando la seguridad. Ese es mi trabajo.' Cuando te refieres a tu puesto o responsabilidad concreta dices", (None, 'my job'), 'con sustantivo contable.']),
    (11, None, ["'¡Claro, Graham, tu secreto está a salvo con nosotras!' La frase hecha", (None, 'your secret is safe with us'), 'promete discreción con humor cómplice.']),
]
