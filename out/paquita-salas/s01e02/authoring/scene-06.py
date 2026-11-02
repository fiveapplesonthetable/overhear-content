ID = 'paquita-salas-s01e02-scene-06'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = "El videobook de mi prima  (My Cousin's Showreel)"
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'alex': 'Álex', 'magui': 'Magüi', 'paquita': 'Paquita'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Native Spanish captions from episode stream. Scene window 00:04:55,240–00:05:49,800.'
INTRO = ("Delivery courier Álex drops by the PS Management office with a parcel for a neighbour and quietly asks Magüi how Paquita is coping. "
         "Before leaving, he asks an exasperated Paquita whether she has watched his cousin's showreel yet. "
         "Listen to the Spanish first.")
OPENER = "Let's walk through Álex's visit to the office line by line."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard polite everyday greetings and parcel-delivery Spanish, Magüi's confession about hiding Paquita's snack cakes, "
         "and three casual ways to wrap up a visit at the door. See you next time.")
CLOSING = ('magui', '¡Hasta la próxima!')

STORY = [
    ('alex', 'Buenos días.',
     'Good morning.',
     [(99, 'Buenos días')], ''),
    ('magui', 'Hola.',
     'Hello.',
     [(99, 'Hola')], ''),
    ('alex', 'Traigo un paquete para Jorge Roelas. ¿Me firmas aquí?',
     'I have a parcel for Jorge Roelas. Will you sign here for me?',
     [(100, 'Traigo un paquete para Jorge Roelas. ¿Me firmas aquí?')], ''),
    ('paquita', 'Magüi, esto lo quito ya.',
     "Magüi, I'm turning this off now.",
     [(101, 'Magüi, esto lo quito ya')],
     'Removed tag question and second sentence.'),
    ('alex', '¿Qué tal está?',
     'How is she doing?',
     [(104, '¿Qué tal está?')], ''),
    ('magui', 'Está mejor. Le he escondido los Tigretones.',
     "She's better. I've hidden the Tigretones cakes from her.",
     [(104, 'Está mejor'), (105, 'Le he escondido los Tigretones')],
     'Combined answer and explanation, trimming trailing clause.'),
    ('magui', '¿Tú qué tal?',
     'How about you?',
     [(106, '¿Tú qué tal?')], ''),
    ('alex', 'Yo, bien.',
     "I'm good.",
     [(106, 'Yo, bien')], ''),
    ('alex', 'Oye, Paquita, ¿has visto el videobook de mi prima?',
     "Hey, Paquita, have you seen my cousin's showreel?",
     [(110, 'Oye, Paquita, ¿has visto el'), (110, 'videobook'), (110, 'de mi prima?')],
     'Removed subtitle quotation marks.'),
    ('alex', 'Lo mandé por correo.',
     'I sent it by post.',
     [(111, 'Lo mandé por correo')], ''),
    ('paquita', '¿Cómo me voy a poner a verlo?',
     'How am I supposed to sit down and watch it?',
     [(112, '¿Cómo me voy a poner a verlo?')], ''),
    ('alex', 'Pues nada.',
     'Oh well, never mind.',
     [(116, 'Pues nada')], ''),
    ('paquita', 'Chao, guapo.',
     'Bye, handsome.',
     [(117, 'Chao, guapo')], ''),
    ('alex', 'Adiós.',
     'Goodbye.',
     [(117, 'Adiós')], '')
]

WALK = [
    (0, None, "'Good morning.' Literally \"good days\" in the masculine plural, even though \"day\" ends in -a! In Spain people use this greeting all morning right up until lunchtime, often around two o'clock."),
    (1, None, "'Hello.' Notice that the opening letter h is completely silent in Spanish, so Magüi's greeting starts straight on the vowel sound."),
    (2, None, "'I have a parcel for Jorge Roelas. Will you sign here for me?' The first word has an irregular -go ending meaning \"I bring\". In the question, present-tense \"you sign\" with a little \"for me\" in front is the polite, natural way to make a quick request in Spain."),
    (3, None, "'Magüi, I'm turning this off now.' Earlier this same word meant taking a framed picture down; here it means \"switch off\" or \"turn off\" a video. Putting \"this\" first and echoing it with the tiny word for \"it\" plus \"right now\" shows Paquita's impatience."),
    (4, None, "'How is she doing?' Adding \"is\" onto that handy phrase for \"how are things\" asks specifically how someone is feeling right now, with no separate word for \"she\" needed."),
    (5, None, "'She's better. I've hidden the Tigretones cakes from her.' Where English says \"hidden from her\", Spanish puts a tiny word meaning \"to her\" before \"I have hidden\". Tigretones are famous Spanish chocolate-rolled sponge cakes that Paquita comfort-eats."),
    (6, None, "'How about you?' Returning a check-in is as easy as putting \"you\" right before that same two-word \"how's things\" chunk, with no action word needed at all."),
    (7, None, "'I'm good.' Mirroring Magüi's verbless question, Álex answers in just two words: \"I, well\", using the word for \"well\" where casual English says \"good\" or \"fine\"."),
    (8, None, "'Hey, Paquita, have you seen my cousin's showreel?' That attention-getting opener literally means \"hear!\" or \"listen!\". At the end, the -an ending on \"cousin\" tells you right away that Álex's cousin is a woman, unlike English \"cousin\"."),
    (9, None, "'I sent it by post.' Because Álex posted the package at a finished point in the past, \"I sent\" uses the crisp single-word past form ending in stressed -é rather than \"have sent\". Depending on context, the final word means either physical mail or email."),
    (10, None, "'How am I supposed to sit down and watch it?' Literally \"how am I going to put myself to watch it?\", using the handy expression \"put oneself to\" for settling down to start a task. Asking \"how am I going to...\" protests that she couldn't possibly have time."),
    (11, None, "'Oh well, never mind.' Literally \"well nothing\", an ultra-common two-word Spanish shrug for wrapping up a topic or accepting defeat gracefully before heading off."),
    (12, None, "'Bye, handsome.' Borrowed from Italian, this breezy farewell is used constantly across Spain, and calling someone \"handsome\" or \"gorgeous\" at the end is warm everyday friendliness rather than flirting."),
    (13, None, "'Goodbye.' This classic farewell comes from an old blessing literally meaning \"to God\", and you'll hear it everywhere from quick doorstep deliveries to formal goodbyes.")
]
