ID = 'paquita-salas-s01e02-scene-15'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 15
TITLE = 'A Macarena García no  (Not Macarena García)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'director': 'Director', 'fernando': 'Fernando'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Window 00:14:47,640–00:15:41,400 (cues 308–328).'
INTRO = (
    'Stopped in her tracks in the theatre aisle, Paquita insists Fernando must represent a different Macarena. '
    'Fernando admits onstage that Macarena García came to him herself, leaving Paquita stunned while the director tries to move on. '
    'Listen to the exchange first.'
)
OPENER = "Let's break down what Paquita, Fernando, and the director say in the aisle."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = (
    'You heard how Spanish fronts a person\'s name for emphasis, uses "in the air" for an unresolved rumour, and turns an adjective into "what matters". '
    'See you next time.'
)
CLOSING = ('paquita', '¡Buenas tardes!')

STORY = [
    ('paquita', 'Perdón, no. A Macarena García no la lleva él.',
     "Excuse me, no. He doesn't represent Macarena García.",
     [(309, 'Perdón, no'), (310, 'a Macarena García no la lleva él')],
     'Combined cues 309 and 310.'),
    ('director', 'Por favor, no es el momento.',
     "Please, this isn't the right moment.",
     [(312, 'Por favor, no es el momento')], ''),
    ('paquita', 'Si no, se queda en el aire esta cuestión y no es así.',
     "Otherwise this matter stays up in the air, and it isn't true.",
     [(313, 'Si no, se queda en el aire esta cuestión'), (314, 'y no es así')],
     'Trimmed middle clauses in cue 314.'),
    ('paquita', 'Fernando, ¿a qué Macarena llevas?',
     'Fernando, which Macarena do you represent?',
     [(318, 'Fernando'), (318, '¿A qué'), (318, 'Macarena'), (317, 'lleva')],
     'Completed interrupted question ¿A qué Maca...? in cue 318.'),
    ('fernando', 'A Macarena García, que la llevo yo ahora.',
     'Macarena García, because I represent her now.',
     [(321, 'A Macarena García, que la llevo yo ahora')], ''),
    ('paquita', '¿A mi Maqui?',
     'My Maqui?',
     [(322, '¿A mi Maqui?')], ''),
    ('fernando', 'Ha venido a que la represente.',
     'She came to me so I would represent her.',
     [(323, 'Ha venido a que la represente')], ''),
    ('director', 'No es el sitio.',
     "This isn't the place.",
     [(325, 'No es el sitio')], ''),
    ('paquita', 'Sigue, sigue, Fernando, por favor.',
     'Go on, go on, Fernando, please.',
     [(325, 'Sigue, sigue, Fernando, por favor')], ''),
    ('fernando', 'Bueno, perdonad este momento de locura entre representantes.',
     'Well, forgive this moment of madness between agents.',
     [(326, 'Bueno, perdonad'), (326, 'este momento de locura'), (327, 'entre representantes')],
     'Trimmed repeated perdonad de verdad.'),
    ('fernando', 'Vamos a lo importante.',
     "Let's get to what matters.",
     [(327, 'vamos a lo importante')], ''),
]

WALK = [
    (0, None, "'Excuse me, no. He doesn't represent Macarena García.' Putting \"Macarena García\" right at the front spotlights who is at stake, which triggers a matching \"her\" before \"represents\". Placing \"he\" at the very end contrasts Fernando sharply with Paquita herself."),
    (1, None, "'Please, this isn't the right moment.' Spanish needs no word for \"this\" or \"it\" before \"is not the moment\". It is a crisp, reusable way to cut off an awkward topic in public."),
    (2, None, "'Otherwise this matter stays up in the air, and it isn't true.' Opening with \"if not\" gives a punchy two-word equivalent of \"otherwise\". Just like English, Spanish says an unsettled issue \"stays in the air\", and closes with literally \"it is not thus\"."),
    (3, None, "'Fernando, which Macarena do you represent?' Even inside a question, Spanish keeps the personal marker \"a\" right at the front because Macarena is a person. Before a name or thing, the accented word for \"what\" means \"which\"."),
    (4, None, "'Macarena García, because I represent her now.' Casual Spanish often uses the short connector \"que\" to mean \"because\" or \"since\" when justifying an answer. Putting \"I\" after \"represent\" stresses that Fernando personally manages her now."),
    (5, None, "'My Maqui?' Alongside Maca, \"Maqui\" is Paquita's fond pet nickname for Macarena. Keeping \"a\" at the front echoes Fernando's phrasing, as if Paquita still cannot believe she is the object of his sentence."),
    (6, None, "'She came to me so I would represent her.' Literally \"she has come to that I represent her\", expressing purpose after a verb of motion. Notice how the ending on \"represent\" shifts to \"-e\" because it expresses what Macarena wanted him to do."),
    (7, None, "'This isn't the place.' Swap \"the moment\" from earlier for \"the site\" or \"spot\", and you get its twin rebuke. In Spain, this everyday noun covers everything from a seat in a theatre to a whole venue."),
    (8, None, "'Go on, go on, Fernando, please.' Repeating the casual command \"continue\" shows Paquita backing down in shock. It comes from the everyday action word for \"follow\" or \"carry on\"."),
    (9, None, "'Well, forgive this moment of madness between agents.' Addressing the whole auditorium, Fernando uses Spain's plural command ending \"-ad\" on \"forgive\". From \"loco\", meaning \"crazy\", Spanish builds the abstract noun for \"madness\" or \"craziness\"."),
    (10, None, "'Let's get to what matters.' That tiny neuter word \"lo\" in front of \"important\" turns a simple descriptive word into an abstract idea: \"the important thing\" or \"what matters\". You'll hear the same handy trick with \"good\", \"bad\", and \"best\"."),
]
