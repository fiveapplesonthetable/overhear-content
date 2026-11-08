# Authoring module for linden-courtyard-es-s01e04-scene-06.
ID = 'linden-courtyard-es-s01e04-scene-06'
SHOW = 'linden-courtyard-es'
SEASON = 1
EPISODE = 4
SCENE = 6
TITLE = 'The Acoustic Architect  (El arquitecto acústico)'
LEVEL = 'A1 — principiante'
PAIR = 'en-es'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = 'Afuera, bajo la sombra del viejo árbol del patio, Caleb abre su cuaderno de cuero marrón para Hannah y Tessa mientras cantan los pájaros de la mañana. Escuchemos primero.'
OPENER = 'Vamos a recorrer la explicación frase por frase.'
TRANSITION = 'Escuchemos otra vez toda la escena seguida.'
OUTRO = "Caleb es arquitecto acústico, y esa mención tranquila de 'a dos calles de aquí' y 'el viernes' acaba de hacer que Hannah y Tessa se miren con los ojos muy abiertos. Hasta la próxima."
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('caleb', 'Look closely at this page. It measures decibels and quietness, not hotel stars!', 'Miren de cerca esta página. ¡Mide decibelios y silencio, no estrellas de hotel!'),
    ('hannah', "Decibels? So 'nine out of ten' was not a review of my front desk?", "¿Decibelios? ¿Así que 'nueve de diez' no era una reseña de mi recepción?"),
    ('caleb', 'Well, your front desk deserves ten! Honestly, though, I am an acoustic architect.', '¡Bueno, tu recepción merece un diez! Aunque, sinceramente, soy arquitecto acústico.'),
    ('tessa', 'An acoustic architect! Do you design concert halls?', '¡Un arquitecto acústico! ¿Diseña salas de conciertos?'),
    ('caleb', 'Small libraries and courtyards, mostly. I measure how old stone walls block street noise.', 'Pequeñas bibliotecas y patios, sobre todo. Mido cómo los viejos muros de piedra frenan el ruido de la calle.'),
    ('hannah', 'That is why you listened for cars up in the attic last night!', '¡Por eso prestó oído a los coches arriba en el ático anoche!'),
    ('caleb', 'Exactly. Outside on the avenue it is loud, yet inside this courtyard you hear leaves and birds.', 'Exacto. Afuera en la avenida hay mucho ruido; sin embargo, dentro de este patio oyes hojas y pájaros.'),
    ('tessa', 'Wait until Arthur hears he panicked all night over decibels!', '¡Espera a que Arthur se entere de que entró en pánico toda la noche por unos decibelios!'),
    ('caleb', 'Truthfully, I also chose this neighborhood for an old family reason.', 'A decir verdad, también elegí este barrio por un viejo motivo familiar.'),
    ('hannah', 'Oh? Did your family live near here once?', '¿Ah, sí? ¿Vivió su familia cerca de aquí alguna vez?'),
    ('caleb', 'Two streets away, when I was small. Friday is... an important day for me.', 'A dos calles de distancia, cuando yo era pequeño. El viernes es... un día importante para mí.'),
    ('tessa', 'Wait, did he just say Friday?!', '¡Espera, ¿acaba de decir el viernes?!'),
]
WALK = [
    (0, None, ["'Miren de cerca esta página. ¡Mide decibelios y silencio, no estrellas de hotel!' El adverbio", (None, 'Look closely'), 'pide fijarse con atención en los detalles pequeños.']),
    (1, None, ["'¿Decibelios? ¿Así que nueve de diez no era una reseña de mi recepción?' Para comprobar una conclusión lógica en pasado basta usar", (None, 'was not a review'), 'no era una reseña.']),
    (2, None, ["'¡Bueno, tu recepción merece un diez! Aunque, sinceramente, soy arquitecto acústico.' Colocado entre comas,", (None, 'though'), "funciona como un 'aunque' o 'sin embargo' muy suave y conversacional."]),
    (3, None, ["'¡Un arquitecto acústico! ¿Diseña salas de conciertos?' En", (None, 'concert halls'), "el sustantivo 'concert' va en singular porque actúa como adjetivo de 'salas'."]),
    (4, None, ["'Pequeñas bibliotecas y patios, sobre todo. Mido cómo los viejos muros de piedra frenan el ruido de la calle.' Al final de una frase,", (None, 'mostly'), "resume 'en su mayoría' o 'sobre todo'."]),
    (5, None, ["'¡Por eso prestó oído a los coches arriba en el ático anoche!' Guarda dos piezas clave: la apertura", (None, 'That is why'), "para 'por eso', y", (None, 'listened for cars'), 'escuchar intentando detectar algo.']),
    (6, None, ["'Exacto. Afuera en la avenida hay mucho ruido; sin embargo, dentro de este patio oyes hojas y pájaros.' Como conector entre dos frases,", (None, 'yet'), "significa 'sin embargo' de forma breve y elegante."]),
    (7, None, ["'¡Espera a que Arthur se entere de que entró en pánico toda la noche por unos decibelios!' Después de", (None, 'Wait until Arthur hears'), 'el inglés usa presente simple aunque hable de algo futuro.']),
    (8, None, ["'A decir verdad, también elegí este barrio por un viejo motivo familiar.' El pasado irregular", (None, 'chose'), "viene de 'choose' con una sola 'o' en la escritura."]),
    (9, None, ["'¿Ah, sí? ¿Vivió su familia cerca de aquí alguna vez?' Al final de una pregunta sobre el pasado,", (None, 'once'), "significa 'en algún tiempo anterior' o 'alguna vez'."]),
    (10, None, ["'A dos calles de distancia, cuando yo era pequeño. El viernes es... un día importante para mí.' Para hablar de la infancia en inglés es muy natural decir", (None, 'when I was small'), 'cuando era pequeño.']),
    (11, None, ["'¡Espera, ¿acaba de decir el viernes?!' De nuevo la combinación", (None, 'did he just say'), 'captura al vuelo las palabras que alguien acaba de pronunciar.']),
]
