# Authoring module for linden-courtyard-es-s01e05-scene-02.
ID = 'linden-courtyard-es-s01e05-scene-02'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 5
SCENE = 2
TITLE = 'Three Years of Silence  (Tres años de silencio)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Dentro, en la recepción, Graham saca del armario la maleta azul oscuro para Caleb y Hannah. Ya es viernes por la mañana, tres horas antes del mediodía. Escuchemos primero.'
OPENER = 'Repasemos cada intervención del diálogo con calma.'
TRANSITION = 'Volvamos a escuchar toda la escena de corrido.'
OUTRO = 'En vez de esconderse al otro lado de la calle, Caleb tiene tres horas para reunir valor y quedarse aquí mismo en el patio. Nos vemos en la siguiente escena.'
CLOSING = ('graham', 'See you later!')
STORY = [
    ('graham', 'So our mystery Friday caller was sleeping upstairs under my attic roof all along.', 'Así que nuestro misterioso interlocutor del viernes estuvo durmiendo arriba bajo el techo de mi ático todo el tiempo.'),
    ('caleb', 'Sorry for the trouble, Graham. Thank you for guarding this bag all week.', 'Perdón por las molestias, Graham. Gracias por custodiar esta maleta toda la semana.'),
    ('hannah', 'Why could you not simply hand Owen the wooden train at his front door?', '¿Por qué no podías simplemente entregarle a Owen el tren de madera en la puerta de su casa?'),
    ('caleb', 'Three years ago, after our grandfather died, Owen and I argued bitterly over selling the old house.', 'Hace tres años, después de morir nuestro abuelo, Owen y yo discutimos amargamente por vender la casa vieja.'),
    ('graham', 'Family houses and old memories, those arguments cut deep.', 'Casas familiares y viejos recuerdos: esas discusiones dejan huella honda.'),
    ('caleb', 'We have not spoken since that day. Last week I sent him one short postcard.', 'No hemos hablado desde aquel día. La semana pasada le envié una postal corta.'),
    ('hannah', 'Asking him to meet you here on Friday at noon?', '¿Pidiéndole que se reuniera contigo aquí el viernes al mediodía?'),
    ('caleb', "Actually, I only wrote: 'Something from Grandfather is waiting at the Linden Courtyard Inn Friday at noon.'", "En realidad, solo escribí: 'Algo del abuelo te espera en la posada Linden Courtyard Inn el viernes al mediodía.'"),
    ('graham', 'Aha! You feared that if you signed your name, stubborn big brother would stay home!', '¡Ajá! ¡Temías que, si firmabas con tu nombre, el hermano mayor cabezota se quedara en casa!'),
    ('caleb', 'You know older brothers well, Graham.', 'Conoces bien a los hermanos mayores, Graham.'),
    ('hannah', 'Wait, were you planning to let the clerk hand him the bag and watch from across the street?!', 'Un momento, ¡¿planeabas dejar que el recepcionista le diera la bolsa y mirar desde la otra acera?!'),
    ('caleb', 'That was my cowardly Monday plan... before I met all of you.', 'Ese era mi plan cobarde del lunes... antes de conocerlos a todos ustedes.'),
]
WALK = [
    (0, None, ["'Así que nuestro misterioso interlocutor del viernes estuvo durmiendo arriba bajo el techo de mi ático todo el tiempo.' El cierre", (None, 'all along'), "significa 'desde el primer momento, todo este tiempo'."]),
    (1, None, ["'Perdón por las molestias, Graham. Gracias por custodiar esta maleta toda la semana.' Una disculpa cotidiana muy cortés es", (None, 'Sorry for the trouble'), 'perdón por las molestias.']),
    (2, None, ["'¿Por qué no podías simplemente entregarle a Owen el tren de madera en la puerta de su casa?' Aquí", (None, 'hand Owen'), "usa la palabra 'mano' como verbo: entregar en mano."]),
    (3, None, ["'Hace tres años, después de morir nuestro abuelo, Owen y yo discutimos amargamente por vender la casa vieja.' Para indicar el tema de una discusión se usa", (None, 'over selling'), "con '-ing' tras la preposición."]),
    (4, None, ["'Casas familiares y viejos recuerdos: esas discusiones dejan huella honda.' La metáfora", (None, 'cut deep'), "literalmente 'cortan profundo', describe heridas emocionales serias."]),
    (5, None, ["'No hemos hablado desde aquel día. La semana pasada le envié una postal corta.' Para marcar el punto exacto donde empezó un silencio se combina presente perfecto con", (None, 'since that day'), "desde aquel día."]),
    (6, None, ["'Pidiéndole que se reuniera contigo aquí el viernes al mediodía?' Observa la estructura limpia", (None, 'Asking him to meet you'), 'pedirle a alguien que quede contigo.']),
    (7, None, ["'En realidad, solo escribí: Algo del abuelo te espera en la posada Linden Courtyard Inn el viernes al mediodía.' Recordemos que 'esperar a alguien' es siempre 'wait for', y aquí", (None, 'is waiting at'), 'indica dónde aguarda el objeto.']),
    (8, None, ["'¡Ajá! ¡Temías que, si firmabas con tu nombre, el hermano mayor cabezota se quedara en casa!' Con la palabra 'home' tras verbos de estancia o movimiento no se pone preposición:", (None, 'would stay home'), 'se quedaría en casa.']),
    (9, None, ["'Conoces bien a los hermanos mayores, Graham.' El adverbio de modo va detrás del objeto en inglés:", (None, 'know older brothers well'), "nunca entre el verbo y 'hermanos'."]),
    (10, None, ["'Un momento, ¡¿planeabas dejar que el recepcionista le diera la bolsa y mirar desde la otra acera?!' Fíjate cómo la acción de mirar desde enfrente se describe con", (None, 'watch from across the street'), "literalmente 'a través de la calle'."]),
    (11, None, ["'Ese era mi plan cobarde del lunes... antes de conocerlos a todos ustedes.' Aunque termine en '-ly',", (None, 'cowardly'), "es un adjetivo que significa 'cobarde'."]),
]
