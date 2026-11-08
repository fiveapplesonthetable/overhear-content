# Authoring module for linden-courtyard-es-s01e03-scene-04.
ID = 'linden-courtyard-es-s01e03-scene-04'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = 'In from the Rain  (Entrando de la lluvia)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb', 'tessa': 'Tessa'}
INTRO = 'Abajo en el vestíbulo, Caleb, un viajero tranquilo de unos treinta y pocos años, entra sacudiendo su paraguas mojado. Hannah lo recibe en el mostrador mientras Tessa le acerca una toalla seca. Escuchemos primero.'
OPENER = 'Vamos a repasar el diálogo frase por frase.'
TRANSITION = 'Escuchemos otra vez toda la escena a ritmo normal.'
OUTRO = 'La sinceridad, una toalla seca y una taza de sopa caliente mantuvieron la conversación serena. En la próxima escena, Caleb sube la escalera para juzgar el ático por sí mismo. Hasta la próxima.'
CLOSING = ('caleb', 'See you soon!')
STORY = [
    ('hannah', 'Good evening! Come inside out of the rain, sir.', '¡Buenas noches! Pase adentro y resguárdese de la lluvia, señor.'),
    ('caleb', 'Good evening. Sorry for dripping water on your clean floor.', 'Buenas noches. Perdón por gotear agua sobre su suelo limpio.'),
    ('hannah', 'Do not worry at all! You must be Caleb.', '¡No se preocupe en absoluto! Usted debe de ser Caleb.'),
    ('caleb', 'Yes, Caleb. I booked room seven by phone yesterday.', 'Sí, Caleb. Reservé la habitación siete por teléfono ayer.'),
    ('tessa', 'Here is a dry towel for your coat and a cup of hot soup, sir.', 'Aquí tiene una toalla seca para su abrigo y una taza de sopa caliente, señor.'),
    ('caleb', 'Hot soup? After that cold walk in the rain, that sounds wonderful.', '¿Sopa caliente? Después de ese paseo frío bajo la lluvia, eso suena de maravilla.'),
    ('hannah', 'Sir, before we go upstairs, I owe you an honest apology.', 'Señor, antes de subir, le debo una disculpa sincera.'),
    ('caleb', 'Oh? Is there a problem with my booking?', '¿Ah, sí? ¿Hay algún problema con mi reserva?'),
    ('hannah', 'We accidentally booked two guests into room seven tonight.', 'Por accidente registramos a dos huéspedes en la habitación siete esta noche.'),
    ('caleb', 'Ah... in this rain? Every hotel near the station looked full.', 'Ah... ¿con esta lluvia? Todos los hoteles cerca de la estación parecían llenos.'),
    ('hannah', 'Please do not worry! We prepared our quiet third floor attic study just for you.', '¡Por favor, no se preocupe! Preparamos nuestro tranquilo estudio del ático del tercer piso solo para usted.'),
    ('caleb', 'An attic study? May I see it first?', '¿Un estudio en el ático? ¿Puedo verlo primero?'),
]
WALK = [
    (0, None, ["'¡Buenas noches! Pase adentro y resguárdese de la lluvia, señor.' Fíjate cómo el inglés dibuja el recorrido con dos palabras seguidas:", (None, 'inside out of the rain'), 'adentro y fuera de la lluvia.']),
    (1, None, ["'Buenas noches. Perdón por gotear agua sobre su suelo limpio.' Para disculparse por algo que estás haciendo, se une", (None, 'Sorry for dripping'), "con la forma en '-ing'."]),
    (2, None, ["'¡No se preocupe en absoluto! Usted debe de ser Caleb.' El cierre enfático", (None, 'at all'), "convierte un simple 'no se preocupe' en un cálido 'para nada, en absoluto'."]),
    (3, None, ["'Sí, Caleb. Reservé la habitación siete por teléfono ayer.' Para indicar el medio de comunicación se dice", (None, 'by phone'), "sin artículo en medio, igual que 'por teléfono'."]),
    (4, None, ["'Aquí tiene una toalla seca para su abrigo y una taza de sopa caliente, señor.' Al entregar algo en mano,", (None, 'Here is a dry towel'), "equivale a nuestro amable 'aquí tiene'."]),
    (5, None, ["'¿Sopa caliente? Después de ese paseo frío bajo la lluvia, eso suena de maravilla.' Cuando un plan te apetece mucho al oírlo, responde con", (None, 'that sounds wonderful'), "con adjetivo detrás del verbo."]),
    (6, None, ["'Señor, antes de subir, le debo una disculpa sincera.' El verbo", (None, 'I owe you'), 'sirve tanto para dinero como para favores, explicaciones o disculpas.']),
    (7, None, ["'¿Ah, sí? ¿Hay algún problema con mi reserva?' Al invertir", (None, 'Is there a problem'), "pasamos de 'hay' afirmativo a la pregunta directa '¿hay algún problema?'."]),
    (8, None, ["'Por accidente registramos a dos huéspedes en la habitación siete esta noche.' Fíjate en cómo", (None, 'booked two guests'), "resume toda la acción de aceptar reservas para esos clientes."]),
    (9, None, ["'Ah... ¿con esta lluvia? Todos los hoteles cerca de la estación parecían llenos.' Donde decimos 'todos los hoteles' en plural, el inglés usa singular con", (None, 'Every hotel'), 'pensando en cada uno.']),
    (10, None, ["'¡Por favor, no se preocupe! Preparamos nuestro tranquilo estudio del ático del tercer piso solo para usted.' El cierre", (None, 'just for you'), 'aporta un toque de atención personalizada y amable.']),
    (11, None, ["'¿Un estudio en el ático? ¿Puedo verlo primero?' Para pedir permiso con mucha educación,", (None, 'May I see it'), "suena más cortés y cuidado que usar 'can'."]),
]
