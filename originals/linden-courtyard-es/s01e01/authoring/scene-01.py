# Authoring module for linden-courtyard-es-s01e01-scene-01.
ID = 'linden-courtyard-es-s01e01-scene-01'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Lift the Handle  (Levanta el picaporte)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Hannah llega temprano en su primera mañana en la posada Linden Courtyard Inn, en Portland. Detrás de la recepción, el veterano encargado de mantenimiento, Graham, ya se sirve un té bien cargado. Escucha primero toda la escena en inglés sin preocuparte por entender cada palabra.'
OPENER = 'Ahora repasemos la conversación con calma, frase por frase.'
TRANSITION = 'Escuchemos otra vez toda la escena a velocidad natural.'
OUTRO = 'Hannah ya está dentro, las ocho llaves de latón cuelgan del tablero y su primera mañana acaba de empezar. No pasa nada si alguna palabra pasó rápido; volverán a salir toda la semana. Hasta la próxima.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Good morning! Excuse me, is the door locked?', '¡Buenos días! Disculpe, ¿está cerrada con llave la puerta?'),
    ('graham', 'Good morning. No, lift the handle first, then push.', 'Buenos días. No, primero levanta el picaporte y luego empuja.'),
    ('hannah', 'Oh, it opens! Thank you. I am Hannah, the new receptionist.', '¡Ah, ya abre! Gracias. Soy Hannah, la nueva recepcionista.'),
    ('graham', 'I am Graham. You are ten minutes early.', 'Soy Graham. Llegas diez minutos temprano.'),
    ('hannah', 'I always walk fast on my first day. Where is the computer?', 'Siempre camino rápido en mi primer día. ¿Dónde está la computadora?'),
    ('graham', 'In the drawer. Here we use this big paper book and a pencil.', 'En el cajón. Aquí usamos este gran libro de papel y un lápiz.'),
    ('hannah', 'A paper book? Really?', '¿Un libro de papel? ¿En serio?'),
    ('graham', 'Paper never loses the room list when it rains.', 'El papel nunca pierde la lista de habitaciones cuando llueve.'),
    ('hannah', 'Fair enough! And these are the keys?', '¡Tiene sentido! ¿Y estas son las llaves?'),
    ('graham', 'Yes, eight rooms, eight brass keys. Room four is arriving today.', 'Sí, ocho habitaciones, ocho llaves de latón. La habitación cuatro llega hoy.'),
    ('hannah', 'Great. Tell me everything I need to know.', 'Genial. Dime todo lo que necesito saber.'),
    ('graham', 'Rule one: drink hot tea first, then answer the bell.', 'Regla uno: primero bebe té caliente y luego contesta el timbre.'),
]
WALK = [
    (0, None, ["'¡Buenos días! Disculpe, ¿está cerrada con llave la puerta?' En inglés el saludo matutino va en singular,", (None, 'Good morning'), 'y para preguntar se adelanta', (None, 'is'), 'delante de la puerta.']),
    (1, None, ["'Buenos días. No, primero levanta el picaporte y luego empuja.' Para dar instrucciones directas basta el verbo tal cual:", (None, 'lift'), 'y', (None, 'push'), 'sin añadir ningún pronombre delante.']),
    (2, None, ["'¡Ah, ya abre! Gracias. Soy Hannah, la nueva recepcionista.' Fíjate en", (None, 'it opens'), 'porque el inglés nunca deja el verbo solo: necesita ese pequeño sujeto neutro para referirse a la puerta.']),
    (3, None, ["'Soy Graham. Llegas diez minutos temprano.' Donde en español decimos 'llegas diez minutos antes', el inglés usa el verbo ser o estar:", (None, 'You are ten minutes early'), "literalmente 'estás diez minutos temprano'."]),
    (4, None, ["'Siempre camino rápido en mi primer día. ¿Dónde está la computadora?' Con días concretos el inglés elige la preposición", (None, 'on my first day'), 'como si te apoyaras sobre esa fecha del calendario.']),
    (5, None, ["'En el cajón. Aquí usamos este gran libro de papel y un lápiz.' Observa el orden delante del sustantivo en", (None, 'big paper book'), "donde tamaño y material van antes de 'libro', sin usar ninguna preposición."]),
    (6, None, ["'¿Un libro de papel? ¿En serio?' Esa reacción corta,", (None, 'Really'), "sirve igual que nuestro '¿de verdad?' o '¿en serio?' con solo subir la entonación al final."]),
    (7, None, ["'El papel nunca pierde la lista de habitaciones cuando llueve.' Mira el cierre", (None, 'when it rains'), 'donde otra vez aparece un sujeto neutro obligatorio con los verbos de clima.']),
    (8, None, ["'¡Tiene sentido! ¿Y estas son las llaves?' Cuando alguien te convence con un buen argumento,", (None, 'Fair enough'), "suena muy natural para decir 'justo es' o 'me parece razonable'."]),
    (9, None, ["'Sí, ocho habitaciones, ocho llaves de latón. La habitación cuatro llega hoy.' La forma continua", (None, 'is arriving today'), 'se usa muchísimo en inglés para planes ya previstos hoy mismo.']),
    (10, None, ["'Genial. Dime todo lo que necesito saber.' Después de", (None, 'everything'), "el inglés omite el equivalente a 'que' y enlaza directo con", (None, 'I need to know'), 'de forma muy ágil.']),
    (11, None, ["'Regla uno: primero bebe té caliente y luego contesta el timbre.' En inglés no solo contestas el teléfono: también dices", (None, 'answer the bell'), 'para acudir cuando suena la campanilla del mostrador.']),
]
