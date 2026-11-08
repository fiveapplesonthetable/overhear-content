# Authoring module for linden-courtyard-es-s01e06-scene-03.
ID = 'linden-courtyard-es-s01e06-scene-03'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = 'Thirty Days on Paper  (Treinta días en papel)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'De vuelta detrás de la recepción, Arthur está hundido junto al tablero de llaves mientras Graham y Hannah se inclinan sobre el mostrador hablando en voz baja. Escucha primero.'
OPENER = 'Vamos a repasar cada frase de esta conversación.'
TRANSITION = 'Escuchemos de nuevo la escena entera a ritmo normal.'
OUTRO = 'Hannah recordó que tienen a un experto en edificios históricos con patio sentado justo bajo su propio árbol. En la próxima escena, Tessa sirve el pastel y Owen nota que algo ocurre dentro.'
CLOSING = ('graham', 'Bye for now!')
STORY = [
    ('arthur', 'Fifteen years of polishing brass keys and straightening ties... gone in thirty days!', 'Quince años sacando brillo a llaves de latón y enderezando corbatas... ¡perdidos en treinta días!'),
    ('graham', 'Stop burying us before we read the whole document, Arthur.', 'Deja de darnos por muertos antes de leer el documento entero, Arthur.'),
    ('hannah', 'Yes! Earlier I noticed a second page clipped behind the cover letter.', '¡Sí! Antes me fijé en una segunda página sujeta con clip detrás de la carta de presentación.'),
    ('arthur', 'Legal paragraphs give me a headache even with two pairs of glasses!', '¡Los párrafos legales me dan dolor de cabeza incluso con dos pares de gafas!'),
    ('graham', 'This house survived eighty winters and one broken boiler valve yesterday.', 'Esta casa sobrevivió a ochenta inviernos y a una válvula de caldera rota ayer.'),
    ('hannah', 'Wait, who is sitting ten meters away in our courtyard right now?', 'Esperen, ¿quién está sentado a diez metros en nuestro patio ahora mismo?'),
    ('arthur', 'Two brothers eating lemon cake?', '¿Dos hermanos comiendo pastel de limón?'),
    ('hannah', 'An architect who works with historic courtyard buildings all over Portland!', '¡Un arquitecto que trabaja con edificios históricos con patio por todo Portland!'),
    ('graham', 'Smart thinking, Hannah. Caleb reads city building rules every single week.', 'Bien pensado, Hannah. Caleb lee normativas municipales de edificación todas las semanas.'),
    ('arthur', 'Oh, I could never bother a paying guest with our landlord troubles!', '¡Oh, jamás podría molestar a un huésped de pago con nuestros problemas de alquiler!'),
    ('hannah', 'After we guarded his blue suitcase all week? He will want to help!', '¿Después de que custodiamos su maleta azul toda la semana? ¡Querrá ayudar!'),
    ('graham', 'Wait, here comes Tessa back from their table right now.', 'Esperen, ahí vuelve Tessa de la mesa de ellos ahora mismo.'),
]
WALK = [
    (0, None, ["'Quince años sacando brillo a llaves de latón y enderezando corbatas... ¡perdidos en treinta días!' Tras 'of', ambos verbos van en '-ing', y el participio", (None, 'gone in thirty days'), "resume 'desaparecidos en treinta días'."]),
    (1, None, ["'Deja de darnos por muertos antes de leer el documento entero, Arthur.' Cuando 'stop' va seguido de '-ing',", (None, 'Stop burying us'), 'significa dejar por completo de hacer algo.']),
    (2, None, ["'¡Sí! Antes me fijé en una segunda página sujeta con clip detrás de la carta de presentación.' En correspondencia oficial,", (None, 'cover letter'), 'es la primera hoja o carta principal.']),
    (3, None, ["'¡Los párrafos legales me dan dolor de cabeza incluso con dos pares de gafas!' En inglés el dolor de cabeza lleva artículo indefinido:", (None, 'give me a headache'), 'me dan dolor de cabeza.']),
    (4, None, ["'Esta casa sobrevivió a ochenta inviernos y a una válvula de caldera rota ayer.' Fíjate en que", (None, 'survived eighty winters'), "no usa la preposición 'a' que ponemos en español."]),
    (5, None, ["'Esperen, ¿quién está sentado a diez metros en nuestro patio ahora mismo?' La distancia se marca añadiendo 'away' detrás de la medida:", (None, 'ten meters away'), 'a diez metros de aquí.']),
    (6, None, ["'¿Dos hermanos comiendo pastel de limón?' La forma en '-ing' reduce toda una oración relativa en", (None, 'Two brothers eating'), 'dos hermanos que están comiendo.']),
    (7, None, ["'¡Un arquitecto que trabaja con edificios históricos con patio por todo Portland!' Para abarcar una ciudad entera de punta a punta usa", (None, 'all over Portland'), 'por todo Portland.']),
    (8, None, ["'Bien pensado, Hannah. Caleb lee normativas municipales de edificación todas las semanas.' El elogio rápido", (None, 'Smart thinking'), 'celebra una buena idea al instante.']),
    (9, None, ["'Oh, jamás podría molestar a un huésped de pago con nuestros problemas de alquiler!' Combinar 'could' con 'never' en", (None, 'I could never bother'), 'expresa un escrúpulo de cortesía muy fuerte.']),
    (10, None, ["'¿Después de que custodiamos su maleta azul toda la semana? ¡Querrá ayudar!' Con total seguridad amable,", (None, 'He will want to help'), 'anticipa su buena disposición.']),
    (11, None, ["'Esperen, ahí vuelve Tessa de la mesa de ellos ahora mismo.' Con nombres propios en", (None, 'here comes Tessa'), 'el verbo va delante del nombre para anunciar a quien se acerca.']),
]
