ID = 'paquita-salas-s01e02-scene-09'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 9
TITLE = 'Encima de las tablas  (On the Boards)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Window 00:07:59,600–00:09:02,600.'
INTRO = ("Paquita and Magüi arrive at the Primera Fila drama school in Madrid to scout young stage talent. "
         "Climbing the strange modern steps, Paquita mixes up playwright Henrik Ibsen with his character Hedda Gabler, then shares her theory of stage acting. "
         "Listen to the Spanish first.")
OPENER = "Let's walk through what Paquita and Magüi say in the theatre."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard the classic theatre idiom 'on top of the boards', how Spanish exclaims 'how strange!' with a single question word, and the film phrase for a 'close-up'. See you in the next scene.")
CLOSING = ('paquita', '¡Buenas tardes!')

STORY = [
    ('paquita', 'Estos escalones, qué raros.',
     'These steps, how strange.',
     [(169, 'Estos escalones, qué raros')],
     'Trimmed trailing interjection.'),
    ('magui', '¡Uy, qué moderno!',
     'Oh, how modern!',
     [(170, '¡Uy, qué moderno!')], ''),
    ('paquita', 'Una actriz se forma encima de las tablas.',
     'An actress trains on the stage.',
     [(172, 'una actriz se forma'), (173, 'encima de las tablas')],
     'Trimmed opening clause and joined across two cues.'),
    ('paquita', 'Por eso nos hemos venido a la escuela Primera Fila.',
     "That's why we've come to the Primera Fila school.",
     [(173, 'por eso nos hemos venido'), (174, 'la escuela Primera Fila')],
     'Condensed a la muestra de teatro de la escuela to a la escuela.'),
    ('paquita', 'Es la mejor de Madrid.',
     "It's the best in Madrid.",
     [(175, 'es la mejor de Madrid')],
     'Turned relative clause into a standalone sentence.'),
    ('paquita', 'Vamos a ver una obra de Henrik Ibsen.',
     "We're going to see a play by Henrik Ibsen.",
     [(175, 'a ver'), (178, 'Una obra'), (178, 'Henrik Ibsen')],
     'Adapted into a direct statement introducing the play.'),
    ('paquita', '¿La habrá adaptado una chiquita que se llama Hedda Gabler?',
     'Could a young girl called Hedda Gabler have adapted it?',
     [(179, 'la habrá adaptado una chiquita que se llama Hedda Gabler')],
     'Trimmed leading conjunction and trailing tag ¿no?.'),
    ('paquita', 'Calla, calla. Qué lío, ¿no?',
     'Hush, never mind. What a mix-up, right?',
     [(182, 'Calla, calla'), (182, 'Qué lío, ¿no?')],
     'Trimmed opening exclamation and third calla.'),
    ('paquita', 'Hedda Gabler es la obra de Henrik Ibsen.',
     'Hedda Gabler is the play by Henrik Ibsen.',
     [(184, '"Hedda Gabler" es la obra'), (185, 'de Henrik Ibsen')],
     'Joined across two cues and removed subtitle quotation marks.'),
    ('paquita', 'Qué bien. Será de acción.',
     "How great. It must be an action play.",
     [(187, 'Qué bien. Será de acción')], ''),
    ('paquita', 'El teatro lo debes ver de lejos, como un primer plano.',
     'You have to watch theatre from afar, like a close-up.',
     [(188, 'El teatro lo debes ver de lejos, como'), (188, 'un primer plano')],
     'Simplified como si fuera to como.'),
    ('magui', '¿De verdad?',
     'Really?',
     [(190, '¿De verdad?')], '')
]

WALK = [
    (0, None, """'These steps, how strange.' Each stair tread is masculine plural here, so both "these" and "strange" end in "-os". Putting the term "what" before a describing word is how Spanish exclaims "how strange!"."""),
    (1, None, """'Oh, how modern!' That little opening sound expresses sudden surprise — like "oh!" or "whoa!" when you nearly trip or spot something striking. Then the same "what" pattern turns "modern" into "how modern!"."""),
    (2, None, """'An actress trains on the stage.' Literally "forms herself on top of the boards", because traditional stages are built from wooden planks — just like English "treading the boards". Saying "forms herself" means getting real professional training."""),
    (3, None, """'That's why we've come to the Primera Fila school.' Opening with "for that" is the everyday Spanish chunk for "that's why". Adding "ourselves" to "have come" gives a lively, purposeful feel of coming all the way here together, and "Primera Fila" means "Front Row"."""),
    (4, None, """'It's the best in Madrid.' Where English says "the best in Madrid", Spanish uses "of Madrid" after "best". And "the" is feminine here because it points back to the feminine word "school"."""),
    (5, None, """'We're going to see a play by Henrik Ibsen.' The word "work" also means an artistic creation or a stage "play". After it, the tiny word "of" handles English "by" to name the author."""),
    (6, None, """'Could a young girl called Hedda Gabler have adapted it?' Spanish often uses the future form of "have" not for tomorrow, but to guess aloud: "will she have adapted it?". Notice the warm diminutive word a young girl, plus "calls herself" for "is called"."""),
    (7, None, """'Hush, never mind. What a mix-up, right?' Repeating the casual command for "be quiet" doesn't scold anyone here — it means "wait, scratch that!". Then a punchy two-syllable word "tangle" or "mess" captures her mix-up."""),
    (8, None, """'Hedda Gabler is the play by Henrik Ibsen.' Once corrected, Paquita repeats the title as if she knew it all along. Again, "the work of Henrik Ibsen" uses "of" where English says "by"."""),
    (9, None, """'How great. It must be an action play.' Again, a future form of "be" expresses a hunch right now — "it'll be an action one" — rather than a distant prediction. Literally "of action" turns "action" into a description of the play."""),
    (10, None, """'You have to watch theatre from afar, like a close-up.' Putting "the theatre" first makes Spanish echo it with "it" right before "you must see". At the end, literally "a first plane" is the standard Spanish cinema phrase for a camera close-up."""),
    (11, None, """'Really?' Literally "of truth?", this two-word question is one of the handiest reactions in Spanish. Use it anytime you want to ask "really?" or "seriously?".""")
]
