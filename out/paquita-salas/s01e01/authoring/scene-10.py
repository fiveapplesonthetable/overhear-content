ID = 'paquita-salas-s01e01-scene-10'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 1
SCENE = 10
TITLE = 'No hay aeropuerto en Valladolid  (There\'s No Airport in Valladolid)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E01: Casada con esto'
SOURCE_FILE = 'sources/paquita-salas/s01/e01.es.srt'
SOURCE_NOTE = 'Window 00:10:23,200–00:11:41,720.'
INTRO = ("With Maca finishing too late for her evening train, Paquita orders Magüi to hunt for another way to get her to Valladolid. "
         "Every fast train is sold out, the night train takes eight hours, and the two argue over whether Valladolid even has an airport. "
         "Listen to the Spanish first.")
OPENER = "Let's unpack their frantic travel search."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how Spanish uses 'completo' for sold-out trains, 'tardar' for how long a journey takes, and 'en' for modes of transport. See you next time.")
CLOSING = ('magui', '¡Hasta luego!')

STORY = [
    ('paquita', 'Da igual el mail. Busca trenes porque no llega.',
     "Never mind the email. Search for trains because she won't make it.",
     [(235, 'Da igual el mail. Busca trenes porque no llega')], ''),
    ('magui', 'Nada. Completo, completo.',
     'Nothing. Sold out, sold out.',
     [(238, 'Nada. Completo, completo')], ''),
    ('magui', 'Busco en Rumbo, en Kayak.',
     "I'm searching on Rumbo, on Kayak.",
     [(241, 'en Rumbo'), (241, 'en Kayak')],
     'Added busco so the line forms a complete beginner clause.'),
    ('paquita', '¿Cómo ir en kayak a Valladolid?',
     'How could she go by kayak to Valladolid?',
     [(242, '¿Cómo ir en kayak a Valladolid?')], ''),
    ('magui', 'El tren cama tarda ocho horas.',
     'The sleeper train takes eight hours.',
     [(243, 'El tren-cama tarda ocho horas')],
     'Written as two words tren cama without hyphen.'),
    ('paquita', '¿Cómo va a ir en tren cama? ¡Busca aviones!',
     'How can she go by sleeper train? Search for planes!',
     [(244, '¿Cómo va a ir en tren-cama?'), (244, 'busca aviones!')], ''),
    ('magui', 'No hay aeropuerto en Valladolid.',
     "There's no airport in Valladolid.",
     [(245, 'No hay aeropuerto en Valladolid')], ''),
    ('paquita', 'Magüi, sí que hay aeropuerto.',
     'Magüi, there definitely is an airport.',
     [(246, 'Magüi'), (246, 'Sí que hay aeropuerto')], ''),
    ('magui', 'Nunca he ido a Valladolid en avión.',
     "I've never gone to Valladolid by plane.",
     [(248, 'Nunca he ido a Valladolid en avión')], ''),
    ('paquita', '¿Has estado alguna vez en Rusia?',
     'Have you ever been to Russia?',
     [(249, '¿Has estado alguna vez en Rusia?')], ''),
    ('paquita', '¿Y porque tú no has estado, no existe Rusia?',
     "And just because you haven't been there, Russia doesn't exist?",
     [(250, 'Y porque tú no has estado'), (251, '¿no existe Rusia?')], ''),
    ('magui', 'No hay aeropuerto en Valladolid, Paquita.',
     "There's no airport in Valladolid, Paquita.",
     [(254, 'No hay aeropuerto en Valladolid, Paquita')], ''),
    ('paquita', 'A lo mejor lo han cerrado ya. Busca en Wikipedia.',
     "Maybe they've closed it already. Look on Wikipedia.",
     [(256, 'A lo mejor lo han cerrado ya'), (258, 'Busca en Wikipedia')], ''),
    ('paquita', 'Cuando estudié mi carrera, no había mails ni Internet.',
     'When I did my degree, there were no emails or Internet.',
     [(264, 'Cuando estudié mi carrera'), (264, 'No había mails ni Internet')], '')
]

WALK = [
    (0, None, "'Never mind the email. Search for trains because she won't make it.' Literally it gives equal, Spain's go-to phrase for it doesn't matter or never mind. Notice too that search needs no separate word for before trains."),
    (1, None, "'Nothing. Sold out, sold out.' On Spanish train websites and hotel signs, the word for complete or full is the standard way to say sold out or fully booked."),
    (2, None, "'I'm searching on Rumbo, on Kayak.' Where English searches on a website, Spanish searches in Rumbo and in Kayak, two travel booking sites."),
    (3, None, "'How could she go by kayak to Valladolid?' Unfamiliar with the travel site Kayak, Paquita hears a literal paddle boat! Notice how Spanish uses in before a vehicle or boat where English says by kayak."),
    (4, None, "'The sleeper train takes eight hours.' Putting train and bed side by side builds sleeper train. Then a single dedicated word means takes time or lasts, related to the word for late."),
    (5, None, "'How can she go by sleeper train? Search for planes!' Asking how is she going to go expresses disbelief, before Paquita uses the command form of search with the plural word for aeroplanes."),
    (6, None, "'There's no airport in Valladolid.' Once again, negative there-is drops the word for an before masculine airport, keeping the refusal short and blunt."),
    (7, None, "'Magüi, there definitely is an airport.' Pairing yes with the little linking word right before there is adds lively insistence, just like saying there definitely is in English."),
    (8, None, "'I've never gone to Valladolid by plane.' Because the word for never sits at the very front of the sentence, Spanish puts no extra negative word before I have gone, and uses in plane rather than by plane."),
    (9, None, "'Have you ever been to Russia?' Literally have you been some time in Russia: Spanish says been in a country rather than been to a country, and uses some time to mean ever."),
    (10, None, "'And just because you haven't been there, Russia doesn't exist?' Notice how explicit casual you adds pointed sarcasm, while Spanish leaves out any word for there after haven't been."),
    (11, None, "'There's no airport in Valladolid, Paquita.' Magüi repeats her exact five-word sentence unchanged, adding Paquita's name at the end to stand her ground."),
    (12, None, "'Maybe they've closed it already. Look on Wikipedia.' That friendly three-word chunk at the start literally says to the best, and means maybe or perhaps in everyday speech."),
    (13, None, "'When I did my degree, there were no emails or Internet.' Watch out for a classic false friend: in Spain, studying your career means doing your university degree, and the little word before Internet means nor or.")
]
