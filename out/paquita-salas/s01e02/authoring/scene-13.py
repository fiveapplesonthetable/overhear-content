ID = 'paquita-salas-s01e02-scene-13'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 13
TITLE = '¿Puedo coger el micro?  (Can I Borrow the Mic?)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'fernando': 'Fernando', 'paquita': 'Paquita'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Window 00:12:42,160–00:13:37,080 (cues 263–281).'
INTRO = (
    'Up on the Primera Fila stage, rival agent Fernando Canelón praises the drama students and quietly slips his business card to Mariona. '
    'Refusing to be outdone, Paquita climbs up, borrows the microphone, and congratulates the cast on behalf of PS Management. '
    "Listen to the Spanish first, then we'll walk through each line."
)
OPENER = "Let's hear how Fernando praises the cast and how Paquita steps in."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = (
    'You heard warm Spanish congratulations, two ways to say "be" side by side, and Spain\'s everyday slang word for hard work. '
    'See you next time.'
)
CLOSING = ('paquita', '¡Hasta luego!')

STORY = [
    ('fernando', 'Muchas gracias. Enhorabuena a todos.',
     'Thank you very much. Congratulations to everyone.',
     [(263, 'Muchas gracias'), (263, 'Enhorabuena a todos')],
     'Trimmed repeated gracias and trailing tag.'),
    ('fernando', 'Habéis estado fantásticos.',
     "You've been fantastic.",
     [(264, 'Habéis estado fantásticos')],
     'Omitted trailing Genial.'),
    ('fernando', 'Te doy mi tarjeta por si te escapas.',
     "I'm giving you my card in case you slip away.",
     [(265, 'Te doy mi tarjeta por si te escapas')], ''),
    ('fernando', 'Todos están muy bien, pero tú estás brillante.',
     "Everyone is very good, but you're brilliant.",
     [(266, 'Todos están muy bien, pero tú estás brillante')],
     'Omitted trailing de verdad.'),
    ('fernando', 'Uno sale al escenario y ve lo difícil que es ser actor.',
     'You step out onto the stage and see how hard it is to be an actor.',
     [(272, 'Uno sale al escenario'), (273, 'y ve lo difícil que es ser actor')],
     'Joined sentence across cues 272 and 273.'),
    ('paquita', 'Perdón, una cosita. ¿Puedo coger el micro un momento?',
     'Excuse me, just one little thing. Can I borrow the mic for a moment?',
     [(275, 'Perdón, una cosita. ¿Puedo coger el micro un momento?')], ''),
    ('paquita', 'Gracias. Perdón por la intrusión.',
     'Thank you. Sorry for the intrusion.',
     [(276, 'Gracias'), (276, 'perdón'), (276, 'la intrusión')],
     'Added por before la intrusión and trimmed spoken fillers.'),
    ('paquita', 'Yo soy Paquita Salas, de PS Management.',
     "I'm Paquita Salas, from PS Management.",
     [(277, 'Yo soy Paquita Salas, de PS Management')], ''),
    ('paquita', 'También soy representante de actores.',
     "I'm also a talent agent for actors.",
     [(278, 'También soy representante de actores')],
     'Trimmed opening hesitation.'),
    ('paquita', 'Chicos, enhorabuena por el curro.',
     'Kids, congratulations on the hard work.',
     [(279, 'chicos'), (280, 'enhorabuena por el curro')],
     'Selected vocative and praise across cues 279 and 280.'),
    ('paquita', 'Pido un aplauso para ellos otra vez, por favor.',
     'I ask for another round of applause for them, please.',
     [(281, 'Pido un aplauso para ellos otra vez, por favor')],
     'Omitted trailing De verdad.'),
]

WALK = [
    (0, None, "'Thank you very much. Congratulations to everyone.' Spain's favourite single word for \"congratulations\" is built from three pieces that literally mean \"in a good hour\". Adding \"to all\" directs the praise to the whole group onstage."),
    (1, None, "'You've been fantastic.' Addressing the students as a group in Spain uses the informal plural form of \"you have\". Notice the masculine plural ending on \"fantastic\", which covers a mixed group of men and women."),
    (2, None, "'I'm giving you my card in case you slip away.' That neat two-word link in the middle literally says \"for if\" and works just like English \"just in case\". At the end, \"you escape\" playfully imagines Mariona sneaking off before they talk."),
    (3, None, "'Everyone is very good, but you're brilliant.' Rather than the permanent \"be\", Fernando chooses the state form here because he means how they performed tonight, not their personalities in general. He includes the explicit word for \"you\" to single Mariona out from the rest."),
    (4, None, "'You step out onto the stage and see how hard it is to be an actor.' Where casual English says \"you step out\", Spanish often uses \"one goes out\" for people in general. Before \"stage\", \"to\" and \"the\" fuse into one short word, and a neuter article before \"difficult\" builds \"how hard it is\"."),
    (5, None, "'Excuse me, just one little thing. Can I borrow the mic for a moment?' Softening \"thing\" with a diminutive ending makes Paquita's interruption sound harmless and polite. In Peninsular Spanish, the everyday word for \"take\" or \"grab\" is completely normal here, and \"microphone\" clips down to two syllables."),
    (6, None, "'Thank you. Sorry for the intrusion.' After \"pardon\", Spanish links the reason with \"for\", matching English \"sorry for\" word for word. \"Intrusion\" sounds almost like its English cousin, just stressed right on the final syllable."),
    (7, None, "'I'm Paquita Salas, from PS Management.' Usually, Spaniards drop the word for \"I\", since \"am\" already reveals who is speaking. Keeping it right at the start puts extra spotlight on Paquita as she introduces herself after Fernando."),
    (8, None, "'I'm also a talent agent for actors.' Opening with \"also\" reminds the hall that Fernando is not the only agent in the room. Once again, Spanish skips \"a\" before the job title and links \"actors\" with \"of\" rather than \"for\"."),
    (9, None, "'Kids, congratulations on the hard work.' Addressing young adults affectionately as \"boys and girls\" is standard across Spain. At the end, Paquita reaches for a lively Madrid slang noun meaning \"work\" or \"graft\" instead of the textbook word."),
    (10, None, "'I ask for another round of applause for them, please.' The opening action word packs \"ask for\" into one piece, so you never add a separate \"for\" right after it; \"for them\" introduces the recipients instead. At the close, \"other time\" is the natural Spanish chunk for \"again\"."),
]
