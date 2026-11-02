ID = 'paquita-salas-s01e02-scene-17'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 17
TITLE = 'Quitarme la peluca  (Taking Off the Wig)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'mariona': 'Mariona', 'director': 'Director'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Window 00:16:30,760–00:18:01,120 (cues 351–379).'
INTRO = (
    'Moved by Paquita and Magüi, student actress Mariona pulls off her stage wig right onstage, calls out Fernando\'s heartlessness, and tells the director she is tired of playing maids. '
    'She urges her classmates to fight for their dreams and declares she is made for hit television like Velvet. '
    'Listen to the Spanish first.'
)
OPENER = "Now we walk through Mariona's big moment."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = (
    'You heard how Spanish expresses "fed up", cheers friends on to fight for their dreams, and declares "just so you know". '
    'See you next time.'
)
CLOSING = ('mariona', '¡Hasta la próxima!')

STORY = [
    ('director', 'Mariola, por favor.',
     'Mariola, please.',
     [(351, 'Mariola, por favor')], ''),
    ('mariona', '¡Déjame hablar!',
     'Let me speak!',
     [(351, '¡Déjame hablar!')], ''),
    ('mariona', 'Qué gusto quitarme la peluca.',
     'What a relief to take off the wig.',
     [(353, 'Qué gusto quitarme la peluca')], ''),
    ('mariona', 'Solo me pones de criada.',
     'You only ever cast me as a maid.',
     [(355, 'solo me pones de criada')],
     'Omitted coarse tag and side remark.'),
    ('mariona', 'No tienes corazón con lo que acabas de hacer con estas dos personas.',
     "You have no heart after what you've just done to these two people.",
     [(358, 'no tienes corazón'), (359, 'con lo que acabas de hacer con estas dos personas')],
     'Omitted coarse opening in cue 358.'),
    ('mariona', '¡Es inhumano!',
     "It's inhumane!",
     [(360, 'Es inhumano')], ''),
    ('mariona', 'Estoy harta de que no me escuchéis y de que no me veáis.',
     "I'm fed up with you all not listening to me and not seeing me.",
     [(361, 'estoy harta'), (362, 'de que no me escuchéis'), (362, 'de que no me veáis')],
     'Omitted coarse interjection in cue 361 and joined cleanly.'),
    ('mariona', 'Estoy cansada.',
     "I'm tired.",
     [(363, 'Estoy cansada')], ''),
    ('mariona', 'Chicos, valéis mucho. De verdad, luchad por vuestros sueños.',
     "Guys, you're worth so much. Truly, fight for your dreams.",
     [(364, 'chicos'), (364, 'valéis mucho'), (365, 'De verdad, luchad por vuestros sueños')],
     'Trimmed surrounding fillers in cue 364.'),
    ('mariona', 'Pasa de ellos y date tiempo.',
     'Ignore them and give yourself time.',
     [(371, 'pasa de ellos y date tiempo')],
     'Trimmed framing clause and trailing tag.'),
    ('director', 'Hasta aquí hemos llegado.',
     'That is quite enough.',
     [(376, 'Hasta aquí hemos llegado')], ''),
    ('mariona', 'Lo que yo iba a hacer es Velvet.',
     'What I was meant to do is Velvet.',
     [(376, 'Lo que yo iba a hacer es Velvet')],
     'Removed subtitle quotation marks.'),
    ('mariona', 'Que sepas que soy una estrella, ¿vale?',
     "Just so you know, I'm a star, okay?",
     [(379, 'Que sepas que'), (379, 'es una estrella, ¿vale?')],
     'Adapted coarse third-person self-reference into clean first-person soy.'),
]

WALK = [
    (0, None, "'Mariola, please.' Even while scolding her onstage, the director gets Mariona's name wrong, calling her \"Mariola\". That tiny detail shows why she feels overlooked at the school."),
    (1, None, "'Let me speak!' Attaching \"me\" straight onto the command \"leave\" or \"let\" builds a punchy one-word plea, written with an accent to hold the stress on the opening syllable. Follow it with any basic action word to say \"let me do something\"."),
    (2, None, "'What a relief to take off the wig.' Exclaiming \"what pleasure!\" expresses pure physical relief here. For clothing, glasses, or a stage wig, Spanish says \"remove from myself the wig\" rather than \"take off my wig\"."),
    (3, None, "'You only ever cast me as a maid.' Literally \"you only put me of maid\", using \"put of\" as theatre shorthand for casting someone in a stock role. Notice there is no \"a\" before \"maid\" after \"of\"."),
    (4, None, "'You have no heart after what you've just done to these two people.' Turning right on Fernando, Mariona says \"you don't have heart\" without any article before \"heart\". She reuses Magüi's \"what you've just done\" chunk to defend Paquita and Magüi."),
    (5, None, "'It's inhumane!' Adding the negative prefix \"in-\" to \"human\" works exactly like English \"inhumane\", though the initial \"h\" is completely silent in Spanish. No separate word for \"it\" is needed before \"is\"."),
    (6, None, "'I'm fed up with you all not listening to me and not seeing me.' Originally meaning \"stuffed full\", \"harta\" with \"estoy\" is Spain's everyday way to say \"I'm fed up\", ending in \"-a\" for Mariona. Both \"listen\" and \"see\" take plural \"vosotros\" endings addressed to the teachers."),
    (7, None, "'I'm tired.' Pairing \"estoy\" with \"cansada\" expresses how worn out she feels right now. Swap \"estoy\" for \"soy\" and you would accidentally call yourself a tiring, exhausting person instead!"),
    (8, None, "'Guys, you're worth so much. Truly, fight for your dreams.' Telling someone \"you are worth a lot\" is a warm Spanish way to praise their talent and value. \"Of truth\" means \"truly\", followed by the plural command \"fight\" and \"dreams\", the same word used for \"sleep\"."),
    (9, None, "'Ignore them and give yourself time.' Encouraging a nervous classmate, Mariona uses \"pass of them\", colloquial Spain Spanish for \"brush them off\" or \"don't care about them\". Then \"give\" plus \"yourself\" fuses smoothly into one two-syllable word."),
    (10, None, "'That is quite enough.' Word for word, the director says \"until here we have arrived\". Spaniards reach for this set expression whenever their patience runs out and they are drawing a firm line."),
    (11, None, "'What I was meant to do is Velvet.' Opening with \"that which I was going to do\" frames her true calling before naming Spain's hit glamour drama Velvet. Rather than classical Norwegian tragedy, she wants prime-time television."),
    (12, None, "'Just so you know, I'm a star, okay?' Starting a sentence with \"that you know that\" is a bold, idiomatic Spanish way to say \"let me tell you\" or \"just so you know\". Tagging \"vale?\" onto the end challenges the room to argue."),
]
