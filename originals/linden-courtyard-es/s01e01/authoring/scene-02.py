# Authoring module for linden-courtyard-es-s01e01-scene-02.
ID = 'linden-courtyard-es-s01e01-scene-02'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = 'Warm Rolls and Two Rings  (Panecillos calientes y dos timbrazos)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'tessa': 'Tessa', 'graham': 'Graham'}
INTRO = 'Cinco minutos después, un aroma tibio a pan recién horneado llena el vestíbulo desde el rincón del desayuno. Tessa sale con una cesta de panecillos calientes para conocer a Hannah y a Graham. Escuchemos primero.'
OPENER = 'Vamos a recorrer la escena despacio, línea por línea.'
TRANSITION = 'Ahora volvamos a escuchar toda la escena de corrido.'
OUTRO = 'Hannah ya tiene un panecillo tibio en la mano y una aliada simpática en la cafetería. Oirás este contraste entre trato cercano y trato formal en cada episodio. Hasta pronto.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('tessa', 'Hello! You must be Hannah. I am Tessa from the kitchen.', '¡Hola! Tú debes de ser Hannah. Yo soy Tessa, de la cocina.'),
    ('hannah', 'Nice to meet you, Tessa. Something smells wonderful!', 'Mucho gusto, Tessa. ¡Algo huele de maravilla!'),
    ('tessa', 'Fresh morning rolls! Take one while it is still warm.', '¡Panecillos recién hechos de la mañana! Toma uno mientras sigue caliente.'),
    ('hannah', 'Thank you! Do we use first names here?', '¡Gracias! ¿Aquí nos tratamos por el nombre de pila?'),
    ('tessa', 'With me, always! Leave the stiff polite talk for the guests.', '¡Conmigo, siempre! Deja el trato tieso y formal para los huéspedes.'),
    ('graham', 'Tessa talks to everyone on our street like old friends.', 'Tessa habla con todo el mundo en nuestra calle como viejos amigos.'),
    ('tessa', 'Because good coffee and warm bread make people friendly!', '¡Porque el buen café y el pan caliente vuelven amable a la gente!'),
    ('hannah', 'What was that bell? Somebody rang twice!', '¿Qué fue ese timbre? ¡Alguien tocó dos veces!'),
    ('graham', 'Nobody is there. That is the buzzer from room four.', 'No hay nadie ahí. Ese es el zumbador de la habitación cuatro.'),
    ('tessa', 'Even when room four is empty, the old wire rings twice.', 'Incluso cuando la habitación cuatro está vacía, el cable viejo suena dos veces.'),
    ('hannah', 'So the house says hello on its own?', '¿Así que la casa saluda por su cuenta?'),
    ('tessa', 'Exactly! You already fit right in.', '¡Exacto! Ya encajas aquí perfectamente.'),
]
WALK = [
    (0, None, ["'¡Hola! Tú debes de ser Hannah. Yo soy Tessa, de la cocina.' Para deducir quién es alguien al verlo,", (None, 'You must be'), "expresa esa suposición amable igual que 'debes de ser'."]),
    (1, None, ["'Mucho gusto, Tessa. ¡Algo huele de maravilla!' Tras verbos de los sentidos como", (None, 'smells'), 'el inglés pone un adjetivo directo,', (None, 'wonderful'), 'en vez de un adverbio.']),
    (2, None, ["'¡Panecillos recién hechos de la mañana! Toma uno mientras sigue caliente.' La combinación", (None, 'still warm'), "une 'todavía' con 'tibio', un par muy práctico en mesa y cocina."]),
    (3, None, ["'¡Gracias! ¿Aquí nos tratamos por el nombre de pila?' Como el inglés usa un único pronombre tanto para 'tú' como para 'usted', pregunta por la confianza diciendo", (None, 'Do we use first names'), 'con el auxiliar al principio.']),
    (4, None, ["'¡Conmigo, siempre! Deja el trato tieso y formal para los huéspedes.' Escucha", (None, 'polite talk'), 'donde el verbo hablar funciona como sustantivo para referirse a la manera de conversar.']),
    (5, None, ["'Tessa habla con todo el mundo en nuestra calle como viejos amigos.' En tercera persona singular el presente añade ese al final, como oyes en", (None, 'talks to everyone'), 'habla con todo el mundo.']),
    (6, None, ["'¡Porque el buen café y el pan caliente vuelven amable a la gente!' Atención a", (None, 'people'), 'que en inglés siempre es plural, por eso lleva el verbo', (None, 'make'), 'sin ese final.']),
    (7, None, ["'¿Qué fue ese timbre? ¡Alguien tocó dos veces!' En lugar de decir 'dos veces' con dos palabras, el inglés concentra toda la idea en una sola:", (None, 'twice'), 'corta y muy frecuente.']),
    (8, None, ["'No hay nadie ahí. Ese es el zumbador de la habitación cuatro.' Como el inglés evita la doble negación, empieza directo con", (None, 'Nobody is there'), 'y deja el verbo en afirmativo.']),
    (9, None, ["'Incluso cuando la habitación cuatro está vacía, el cable viejo suena dos veces.' La pareja", (None, 'Even when'), "abre la frase con el sentido exacto de 'incluso cuando'."]),
    (10, None, ["'¿Así que la casa saluda por su cuenta?' Guarda dos bloques muy idiomáticos aquí:", (None, 'says hello'), "para 'saluda' y", (None, 'on its own'), "para 'por sí sola'."]),
    (11, None, ["'¡Exacto! Ya encajas aquí perfectamente.' La expresión coloquial", (None, 'fit right in'), 'significa integrarse de maravilla en un grupo nuevo desde el primer momento.']),
]
