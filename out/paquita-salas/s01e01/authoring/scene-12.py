ID = 'paquita-salas-s01e01-scene-12'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 1
SCENE = 12
TITLE = 'Hace cinco días  (Five Days Ago)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'alex': 'Álex', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E01: Casada con esto'
SOURCE_FILE = 'sources/paquita-salas/s01/e01.es.srt'
SOURCE_NOTE = 'Window 00:13:49,280–00:14:48,280.'
INTRO = ("After Paquita rushes out to drive Macarena to Valladolid, Magüi stays at her desk with Álex to sort through the unread spam folder. "
         "There she spots an email from Macarena sent five days earlier leaving Paquita's agency, and frantically leaves Paquita a voicemail. "
         "Listen to the Spanish first.")
OPENER = "Let's go through what Magüi and Álex uncover."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how 'hace cinco días' expresses 'five days ago', and how 'por' introduces the channel a message was sent through. See you in the next scene.")
CLOSING = ('magui', '¡Hasta pronto!')

STORY = [
    ('alex', '¿Y ese era importante?',
     'And was that one important?',
     [(311, '¿Y ese era importante?')], ''),
    ('magui', 'Qué barbaridad. Todo esto es trabajo.',
     'Unbelievable. All of this is work.',
     [(311, 'Qué barbaridad. Todo esto es trabajo')], ''),
    ('alex', 'Bueno, no te preocupes.',
     "Well, don't worry.",
     [(313, 'Bueno, no te preocupes')], ''),
    ('magui', 'Macarena García. ¿Este de cuándo es?',
     'Macarena García. When is this one from?',
     [(314, 'Macarena García'), (315, '¿Este de cuándo es?')], ''),
    ('alex', 'Hace cinco días.',
     'Five days ago.',
     [(315, 'Hace cinco días')], ''),
    ('magui', '¡Ay, Dios mío! ¡Ay, Macarena!',
     'Oh, my goodness! Oh, Macarena!',
     [(316, 'Ay, Dios mío. ¡Ay, Macarena!')], ''),
    ('alex', '¿Pero qué pasa, Magüi?',
     "Wait, what's wrong, Magüi?",
     [(319, '¿Pero qué pasa, Magüi?')], ''),
    ('magui', 'El correo es de hace cinco días.',
     'The email is from five days ago.',
     [(321, 'de hace cinco días'), (321, 'el correo')],
     'Normalised spoken word order.'),
    ('magui', 'Macarena García ha dejado a Paquita hace cinco días.',
     'Macarena García left Paquita five days ago.',
     [(322, 'Ha dejado a Paquita'), (322, 'Macarena García hace cinco días')], ''),
    ('magui', 'Paquita, soy Magüi. Llámame cuando puedas, urgente.',
     "Paquita, it's Magüi. Call me when you can, urgent.",
     [(325, 'Paquita, soy Magüi. Llámame cuando puedas'), (325, 'urgente')], ''),
    ('magui', 'Un beso.',
     'A kiss.',
     [(326, 'Un beso')], ''),
    ('magui', '¿Cómo ha hecho eso por mail?',
     'How did she do that by email?',
     [(327, '¿cómo ha hecho eso por mail?')], ''),
    ('alex', 'Tranquilízate.',
     'Calm down.',
     [(327, 'Tranquilízate')], ''),
    ('magui', '¿Cómo ha hecho esto por spam?',
     'How did she do this by spam?',
     [(330, '¿cómo ha hecho esto por'), (330, 'spam')], '')
]

WALK = [
    (0, None, "'And was that one important?' Because the word for email is masculine, that one uses the masculine form without needing a word for one. Ongoing was describes what that message was about."),
    (1, None, "'Unbelievable. All of this is work.' Literally what barbarity, a lively everyday Spanish reaction whenever an amount, price, or mess is outrageous. Neuter all this needs no word for of."),
    (2, None, "'Well, don't worry.' Starting with the word for good softens the reassurance, just like English well. Negative casual commands flip the ending vowel from a to es and put you in front."),
    (3, None, "'Macarena García. When is this one from?' Unlike English, Spanish never strands from at the end of a question: it asks literally this one, of when is it, with a written accent on when."),
    (4, None, "'Five days ago.' Where English puts ago after the time span, Spanish puts it makes at the front: literally it makes five days."),
    (5, None, "'Oh, my goodness! Oh, Macarena!' Literally my goodness with the stressed word for mine placed after the noun rather than simple my before it, giving the exclamation extra weight."),
    (6, None, "'Wait, what's wrong, Magüi?' Leading with the word for but before what happens captures Álex's sudden alarm as Magüi stares at the screen."),
    (7, None, "'The email is from five days ago.' Putting the little word for of right before five days ago builds the phrase for from five days ago cleanly."),
    (8, None, "'Macarena García left Paquita five days ago.' Earlier this same word meant leaving a parcel on a desk; with a person and the personal marker before Paquita, has left means ended their professional relationship."),
    (9, None, "'Paquita, it's Magüi. Call me when you can, urgent.' Call and me fuse into a single word on the voicemail. After when looking ahead to the future, you can switches its vowel from e to a."),
    (10, None, "'A kiss.' Even in sheer panic, Magüi reflexively closes her Spanish phone message with the customary two-word sign-off."),
    (11, None, "'How did she do that by email?' When talking about sending news by email or by phone, Spanish uses the preposition meaning through or by rather than in."),
    (12, None, "'Calm down.' One long word does the whole job: calm down tacks casual yourself onto the end, adding a written accent to hold the original stress."),
    (13, None, "'How did she do this by spam?' In her shock, Magüi treats the spam folder as if Macarena deliberately sent her breakup letter by spam, swapping that for closer this.")
]
