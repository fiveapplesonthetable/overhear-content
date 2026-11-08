# Authoring module for linden-courtyard-es-s01e01-scene-04.
ID = 'linden-courtyard-es-s01e01-scene-04'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'Room Four on the Second Floor  (La habitación cuatro en el segundo piso)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = 'En la recepción, Evelyn, profesora de piano jubilada, entra desde el taxi tirando de una gran maleta azul oscuro. Hannah recibe a su primera huésped real mientras Graham espera listo para ayudar con el equipaje. Escuchemos cómo les va.'
OPENER = 'Escuchemos de nuevo cada intervención con calma.'
TRANSITION = 'Ahora oigamos toda la escena seguida otra vez.'
OUTRO = 'Hannah resolvió su primer registro con soltura, aunque Graham notó que esa maleta azul pesaba de un modo extraño. Hasta la próxima para descubrir por qué.'
CLOSING = ('evelyn', 'Take care!')
STORY = [
    ('hannah', "Welcome! Good morning, ma'am.", '¡Bienvenida! Buenos días, señora.'),
    ('evelyn', 'Good morning, my dear. I have a booking for Evelyn.', 'Buenos días, querida. Tengo una reserva para Evelyn.'),
    ('hannah', 'Yes, room four on the second floor! How was your train trip?', '¡Sí, la habitación cuatro en el segundo piso! ¿Qué tal estuvo su viaje en tren?'),
    ('evelyn', 'Quiet and pleasant, thank you, though this suitcase feels very heavy today.', 'Tranquilo y agradable, gracias, aunque esta maleta se siente muy pesada hoy.'),
    ('graham', 'Allow me. Goodness, did you pack stones in here?', 'Permítame. ¡Madre mía, ¿metió piedras aquí dentro?!'),
    ('evelyn', 'Only dresses, sheet music, and my favorite teacup!', '¡Solo vestidos, partituras y mi taza de té favorita!'),
    ('hannah', 'Here is your key, number four. Breakfast is from seven thirty to ten.', 'Aquí tiene su llave, la número cuatro. El desayuno es de siete y media a diez.'),
    ('evelyn', 'Wonderful. Is the window facing the street or the courtyard?', 'Maravilloso. ¿La ventana da a la calle o al patio?'),
    ('hannah', 'The courtyard, right above the old tree. It is very quiet.', 'Al patio, justo encima del árbol viejo. Es muy tranquilo.'),
    ('evelyn', 'Just what I need. Where are the stairs?', 'Justo lo que necesito. ¿Dónde están las escaleras?'),
    ('graham', 'Right through this archway. I will carry the blue bag up for you.', 'Justo cruzando este arco. Yo le subo la maleta azul.'),
    ('evelyn', 'Thank you both very much.', 'Muchas gracias a los dos.'),
]
WALK = [
    (0, None, ["'¡Bienvenida! Buenos días, señora.' En Estados Unidos el trato cortés habitual hacia una clienta es", (None, "ma'am"), 'fórmula breve, cálida y muy respetuosa.']),
    (1, None, ["'Buenos días, querida. Tengo una reserva para Evelyn.' Para una reserva en un hotel o restaurante se suele usar el sustantivo", (None, 'booking'), "que viene del verbo 'book'."]),
    (2, None, ["'¡Sí, la habitación cuatro en el segundo piso! ¿Qué tal estuvo su viaje en tren?' Para preguntar cómo salió un trayecto ya terminado,", (None, 'How was your train trip'), 'es la fórmula más directa.']),
    (3, None, ["'Tranquilo y agradable, gracias, aunque esta maleta se siente muy pesada hoy.' El giro", (None, 'feels very heavy'), 'describe el peso que notas al levantar o arrastrar algo.']),
    (4, None, ["'Permítame. ¡Madre mía, ¿metió piedras aquí dentro?!' Al ofrecerte a cargar algo,", (None, 'Allow me'), 'suena caballeroso, y', (None, 'Goodness'), 'es una exclamación suave de sorpresa.']),
    (5, None, ["'¡Solo vestidos, partituras y mi taza de té favorita!' La música impresa en hojas se llama", (None, 'sheet music'), 'sin plural ni artículo cuando hablas de partituras en general.']),
    (6, None, ["'Aquí tiene su llave, la número cuatro. El desayuno es de siete y media a diez.' Mira qué sencillo es decir las horas hablando:", (None, 'seven thirty'), 'solo junta la hora y los minutos.']),
    (7, None, ["'Maravilloso. ¿La ventana da a la calle o al patio?' Donde nosotros decimos 'dar a', el inglés usa la imagen del rostro:", (None, 'facing the street'), 'como si la ventana mirara de frente a la calle.']),
    (8, None, ["'Al patio, justo encima del árbol viejo. Es muy tranquilo.' La combinación", (None, 'right above'), "añade precisión a 'encima de': exactamente arriba del viejo árbol."]),
    (9, None, ["'Justo lo que necesito. ¿Dónde están las escaleras?' Quédate con", (None, 'Just what I need'), 'una frase redonda para celebrar que algo te viene como anillo al dedo.']),
    (10, None, ["'Justo cruzando este arco. Yo le subo la maleta azul.' Para ofrecer ayuda en el acto, el inglés recurre a", (None, 'I will carry'), 'y añade', (None, 'up'), 'para dejar claro el movimiento escaleras arriba.']),
    (11, None, ["'Muchas gracias a los dos.' Colocar", (None, 'both'), 'en', (None, 'Thank you both'), 'agradece a dos personas a la vez con total naturalidad.']),
]
