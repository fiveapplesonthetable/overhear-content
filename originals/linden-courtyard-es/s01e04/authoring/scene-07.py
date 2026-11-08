# Authoring module for linden-courtyard-es-s01e04-scene-07.
ID = 'linden-courtyard-es-s01e04-scene-07'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = 'Sunlight on the Tag  (Sol sobre la etiqueta)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = 'Al mediodía, Graham abre el armario del pasillo para ventilarlo tras la tormenta y deja la maleta azul sin reclamar junto a la recepción, justo cuando llega la señorita Evelyn a hablar con Hannah. Escucha primero.'
OPENER = 'Ahora repasemos cada línea de la escena.'
TRANSITION = 'Escuchemos otra vez toda la escena a velocidad natural.'
OUTRO = 'La luz del día sobre una vieja etiqueta de equipaje acaba de abrir veinticinco años de historia: dos hermanos en la calle Linden y el tren de madera de su abuelo. Queda una escena en el episodio cuatro.'
CLOSING = ('evelyn', 'Bye for now!')
STORY = [
    ('graham', 'Let me set this blue suitcase here for five minutes while I sweep the closet.', 'Déjame apoyar aquí esta maleta azul cinco minutos mientras barro el armario.'),
    ('hannah', 'Careful with it, Graham. Tomorrow at noon is Friday!', 'Con cuidado con ella, Graham. ¡Mañana al mediodía es viernes!'),
    ('evelyn', "Oh, is that the twin suitcase from Monday's train?", 'Oh, ¿esa es la maleta gemela del tren del lunes?'),
    ('hannah', "Yes, ma'am, still waiting for its owner.", 'Sí, señora, todavía esperando a su dueño.'),
    ('evelyn', 'May I look at the paper tag again here in the bright sunlight?', '¿Puedo mirar otra vez la etiqueta de papel aquí bajo la luz brillante del sol?'),
    ('graham', "Go right ahead, ma'am. Monday afternoon the lobby was dark.", 'Adelante, señora. El lunes por la tarde el vestíbulo estaba oscuro.'),
    ('evelyn', 'Wait a moment... Number twelve, Linden Street, and two childhood initials carved on the corner!', 'Un momento... ¡Número doce de la calle Linden, y dos iniciales de infancia talladas en la esquina!'),
    ('hannah', 'Miss Evelyn, you look amazed! Do you know Number twelve, Linden Street?', '¡Señorita Evelyn, se la ve asombrada! ¿Conoce el número doce de la calle Linden?'),
    ('evelyn', 'Know it? Every Friday for six years I climbed those wooden stairs to teach piano!', '¿Que si lo conozco? ¡Cada viernes durante seis años subí esa escalera de madera para enseñar piano!'),
    ('graham', 'Twenty-five years ago? In that same house?', '¿Hace veinticinco años? ¿En esa misma casa?'),
    ('evelyn', 'A carpenter lived there with his two grandsons. The older boy played piano, and the little one loved trains!', '¡Allí vivía un carpintero con sus dos nietos! El mayor tocaba el piano, ¡y al pequeño le encantaban los trenes!'),
    ('hannah', 'A carpenter... and a little wooden toy train inside the bag!', 'Un carpintero... ¡y un pequeño tren de juguete de madera dentro de la maleta!'),
]
WALK = [
    (0, None, ["'Déjame apoyar aquí esta maleta azul cinco minutos mientras barro el armario.' Para duraciones concretas de tiempo usamos la preposición", (None, 'for five minutes'), 'durante cinco minutos.']),
    (1, None, ["'Con cuidado con ella, Graham. ¡Mañana al mediodía es viernes!' Recuerda que mediodía lleva la misma preposición puntual que las horas:", (None, 'at noon'), 'al mediodía.']),
    (2, None, ["'Oh, ¿esa es la maleta gemela del tren del lunes?' En", (None, 'twin suitcase'), "la palabra para 'gemelo' describe dos objetos idénticos."]),
    (3, None, ["'Sí, señora, todavía esperando a su dueño.' Atención al posesivo neutro sin apóstrofo en", (None, 'waiting for its owner'), 'esperando a su dueño.']),
    (4, None, ["'¿Puedo mirar otra vez la etiqueta de papel aquí bajo la luz brillante del sol?' Cuando algo está iluminado por el sol, el inglés usa 'in':", (None, 'in the bright sunlight'), 'a plena luz del sol.']),
    (5, None, ["'Adelante, señora. El lunes por la tarde el vestíbulo estaba oscuro.' Para dar permiso con calidez inmediata, nada suena más natural que", (None, 'Go right ahead'), 'adelante, faltaría más.']),
    (6, None, ["'Un momento... ¡Número doce de la calle Linden, y dos iniciales de infancia talladas en la esquina!' El participio", (None, 'carved on the corner'), 'indica letras grabadas en madera o cuero.']),
    (7, None, ["'¡Señorita Evelyn, se la ve asombrada! ¿Conoce el número doce de la calle Linden?' Con verbos de aspecto como 'look', ponemos el adjetivo directo:", (None, 'you look amazed'), 'te ves asombrada.']),
    (8, None, ["'¿Que si lo conozco? ¡Cada viernes durante seis años subí esa escalera de madera para enseñar piano!' Después de 'teach', los instrumentos musicales van sin artículo en", (None, 'teach piano'), 'enseñar piano.']),
    (9, None, ["'¿Hace veinticinco años? ¿En esa misma casa?' Recuerda el orden temporal con", (None, 'Twenty-five years ago'), "donde 'ago' cierra siempre la expresión al final."]),
    (10, None, ["'¡Allí vivía un carpintero con sus dos nietos! El mayor tocaba el piano, ¡y al pequeño le encantaban los trenes!' Para no repetir 'boy', el inglés usa el comodín", (None, 'the little one'), 'el pequeño.']),
    (11, None, ["'Un carpintero... ¡y un pequeño tren de juguete de madera dentro de la maleta!' Tres pistas delante del sustantivo en", (None, 'little wooden toy train'), "tamaño, material y función antes de 'tren'."]),
]
