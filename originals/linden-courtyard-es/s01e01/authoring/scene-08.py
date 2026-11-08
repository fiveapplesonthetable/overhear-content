# Authoring module for linden-courtyard-es-s01e01-scene-08.
ID = 'linden-courtyard-es-s01e01-scene-08'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = 'Left on the Step  (Dejada en el escalón)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Son casi las nueve de la noche y los faroles del patio brillan suavemente mientras Hannah termina su primera jornada con Graham. De pronto, la campana de la reja suena una vez en el silencio nocturno. Escucha primero.'
OPENER = 'Repasemos juntos cada línea de este cierre de episodio.'
TRANSITION = 'Escuchemos la escena completa una vez más.'
OUTRO = 'La maleta de Evelyn ha vuelto, pero el desconocido desapareció en la noche pidiendo que le guarden la suya hasta el viernes. ¡Así termina el episodio uno; te esperamos en el episodio dos!'
CLOSING = ('graham', 'Have a good night!')
STORY = [
    ('hannah', 'Did you hear that, Graham? Someone just rang the gate bell!', '¿Oíste eso, Graham? ¡Alguien acaba de tocar la campana de la entrada!'),
    ('graham', "At nine o'clock? Stay here, let us open the door together.", '¿A las nueve en punto? Quédate aquí, abramos la puerta juntos.'),
    ('hannah', 'Hello? Good evening! Nobody is standing in the courtyard!', '¿Hola? ¡Buenas noches! ¡No hay nadie parado en el patio!'),
    ('graham', 'Wait. Look down on the stone step.', 'Espera. Mira abajo en el escalón de piedra.'),
    ('hannah', "Another dark blue suitcase! Is this Miss Evelyn's bag?", '¡Otra maleta azul oscuro! ¿Es el equipaje de la señorita Evelyn?'),
    ('graham', 'Check the zipper... yes, her initials are right here!', 'Revisa la cremallera... ¡sí, sus iniciales están aquí mismo!'),
    ('hannah', 'Why did the person run away without taking his own suitcase back?', '¿Por qué salió corriendo esa persona sin llevarse su propia maleta?'),
    ('graham', 'Look, there is a folded white envelope taped to the handle.', 'Mira, hay un sobre blanco doblado pegado con cinta al asa.'),
    ('hannah', "Let me read it: 'Sorry for the mistake. Please keep my blue bag until Friday.'", 'Déjame leerlo: "Perdón por el error. Por favor, guarden mi bolso azul hasta el viernes."'),
    ('graham', 'Until Friday? No name, no signature!', '¿Hasta el viernes? ¡Sin nombre, sin firma!'),
    ('hannah', 'Why leave your own shoes and wooden train with strangers until Friday?', '¿Por qué dejar tus propios zapatos y un tren de madera con desconocidos hasta el viernes?'),
    ('graham', 'Welcome to the Linden Courtyard Inn, Hannah. Your second day will not be boring.', 'Bienvenida a Linden Courtyard Inn, Hannah. Tu segundo día no va a ser aburrido.'),
]
WALK = [
    (0, None, ["'¿Oíste eso, Graham? ¡Alguien acaba de tocar la campana de la entrada!' Otra pregunta limpia en pasado:", (None, 'Did you hear that'), 'pone el auxiliar delante y deja el verbo oír sin cambios.']),
    (1, None, ["'¿A las nueve en punto? Quédate aquí, abramos la puerta juntos.' La expresión clásica", (None, "nine o'clock"), 'marca siempre una hora exacta del reloj.']),
    (2, None, ["'¿Hola? ¡Buenas noches! ¡No hay nadie parado en el patio!' Atención a la diferencia vital: al llegar de noche saludas con", (None, 'Good evening'), 'mientras que la otra despedida nocturna se reserva para irte o acostarte.']),
    (3, None, ["'Espera. Mira abajo en el escalón de piedra.' Al juntar mirada y dirección,", (None, 'Look down'), 'indica enseguida que bajes la vista hacia el suelo.']),
    (4, None, ["'¡Otra maleta azul oscuro! ¿Es el equipaje de la señorita Evelyn?' Cuando quieres decir 'otro más' en singular, el inglés fusiona artículo y adjetivo en una sola palabra:", (None, 'Another'), 'otra maleta.']),
    (5, None, ["'Revisa la cremallera... ¡sí, sus iniciales están aquí mismo!' Como las iniciales pertenecen a una mujer, el posesivo es", (None, 'her initials'), "guiado por la dueña y no por la palabra 'iniciales'."]),
    (6, None, ["'¿Por qué salió corriendo esa persona sin llevarse su propia maleta?' Después de una preposición como 'sin' en", (None, 'without taking'), 'el verbo inglés adopta siempre su forma continua.']),
    (7, None, ["'Mira, hay un sobre blanco doblado pegado con cinta al asa.' De la palabra inglesa para cinta adhesiva sale directamente el participio", (None, 'taped'), 'pegado con cinta.']),
    (8, None, ['\'Déjame leerlo: "Perdón por el error. Por favor, guarden mi bolso azul hasta el viernes."\' Para pedir disculpas por un motivo concreto, el inglés enlaza', (None, 'Sorry for the mistake'), 'perdón por el error.']),
    (9, None, ["'¿Hasta el viernes? ¡Sin nombre, sin firma!' Los días de la semana como", (None, 'Friday'), 'se escriben siempre con mayúscula inicial en inglés, y', (None, 'until'), "marca el límite temporal 'hasta'."]),
    (10, None, ["'¿Por qué dejar tus propios zapatos y un tren de madera con desconocidos hasta el viernes?' Cuidado con", (None, 'strangers'), "que no significa 'extranjeros', sino personas desconocidas."]),
    (11, None, ["'Bienvenida a Linden Courtyard Inn, Hannah. Tu segundo día no va a ser aburrido.' Para predecir el futuro en negativo,", (None, 'will not be boring'), "significa que no resultará 'aburrido'."]),
]
