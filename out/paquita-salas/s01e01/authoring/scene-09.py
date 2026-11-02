ID = 'paquita-salas-s01e01-scene-09'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 1
SCENE = 9
TITLE = 'Hay un cambio de plan  (There\'s a Change of Plan)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E01: Casada con esto'
SOURCE_FILE = 'sources/paquita-salas/s01/e01.es.srt'
SOURCE_NOTE = 'Window 00:09:03,880–00:10:23,160.'
INTRO = ("Paquita phones production coordinator Juanfran on Macarena's television set to ask him to text her when Maca leaves for the half-past-six train. "
         "Instead, she learns that filming was pushed back to half past eight, meaning Maca will miss her train to the Seminci festival in Valladolid. "
         "Listen to the Spanish first.")
OPENER = "Let's trace how the schedule mix-up comes to light."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how Spanish tells the time on the half-hour with 'and a half', and how 'no puede ser' reacts to bad news. See you in the next scene.")
CLOSING = ('paquita', '¡Hasta pronto!')

STORY = [
    ('paquita', 'Juanfran, soy Paquita Salas. ¿Qué tal?',
     "Juanfran, it's Paquita Salas. How are things?",
     [(207, 'Juanfran, Paquita Salas'), (208, '¿Qué tal?')],
     'Added soy for natural phone introduction.'),
    ('paquita', 'Te llamo porque no localizo a Maqui esta tarde.',
     "I'm calling you because I can't reach Maqui this afternoon.",
     [(209, 'te llamo porque'), (209, 'no localizo a Maqui esta tarde')], ''),
    ('paquita', 'Cuando ella salga para la RENFE, ¿me podéis mandar un WhatsApp?',
     'When she leaves for the train station, can you send me a WhatsApp?',
     [(211, 'Cuando ella salga para la RENFE'), (212, '¿me podéis mandar un WhatsApp?')], ''),
    ('paquita', 'Sí, a las seis y media.',
     'Yes, at half past six.',
     [(214, 'Sí, a las')],
     'Spelled out 18:30 in natural spoken twelve-hour Spanish.'),
    ('paquita', '¿Cómo? ¿Hay un cambio de plan?',
     "What? There's a change of plan?",
     [(216, '¿Cómo?'), (217, 'hay un cambio de plan')], ''),
    ('paquita', '¿De horario? ¿A qué hora sale?',
     'To the schedule? What time does she finish?',
     [(218, '¿De horario?'), (218, '¿A qué hora sale?')], ''),
    ('paquita', '¿Maca hoy sale a las ocho y media?',
     'Maca finishes at half past eight today?',
     [(219, 'Maca hoy sale a las')],
     'Spelled out 20:30 in natural spoken twelve-hour Spanish.'),
    ('paquita', '¿Y me has mandado un mail con eso?',
     'And you sent me an email about that?',
     [(220, '¿Y me has mandado un mail con eso?')], ''),
    ('magui', '¿Qué mail? No hay mail.',
     "What email? There's no email.",
     [(223, '¿Qué mail? No hay mail')], ''),
    ('paquita', 'Parece que había un mail, pero nunca llegó.',
     'Apparently there was an email, but it never arrived.',
     [(224, 'Parece'), (224, 'que había un mail, pero nunca llegó')], ''),
    ('magui', 'Era un mail que avisaba de un cambio de horario en la serie.',
     'It was an email warning about a schedule change on the series.',
     [(228, 'Era un mail que avisaba de un cambio de horario'), (229, 'en la serie')], ''),
    ('magui', 'Ya habíamos comprado el billete para la Seminci esta noche.',
     'We had already bought the ticket for Seminci tonight.',
     [(230, 'ya'), (230, 'habíamos comprado el billete'), (231, 'para'), (231, 'la Seminci esta noche')], ''),
    ('paquita', 'Ahora no llega. No puede ser.',
     "Now she won't make it. It can't be.",
     [(232, 'Ahora no llega'), (233, 'No puede ser')], '')
]

WALK = [
    (0, None, "'Juanfran, it's Paquita Salas. How are things?' On the phone, Spanish introduces yourself with I am rather than it is. Then that crisp two-word greeting asks how things are going."),
    (1, None, "'I'm calling you because I can't reach Maqui this afternoon.' Here Maqui is another affectionate nickname Paquita uses for Macarena. Notice the personal marker before Maqui and the feminine word for this before afternoon."),
    (2, None, "'When she leaves for the train station, can you send me a WhatsApp?' Spaniards often say the RENFE, using the rail company's name as the word for the train station itself. After when referring to later today, leaves uses its g-stem form rather than regular sale."),
    (3, None, "'Yes, at half past six.' Even when written timetables show eighteen thirty, everyday spoken Spanish says at the six and half, using feminine plural the because hours is understood."),
    (4, None, "'What? There's a change of plan?' When you mishear or can't believe what someone just said on the phone, asking the word for how is much more polite in English's place for what."),
    (5, None, "'To the schedule? What time does she finish?' Literally at what hour does she go out: leaving work or wrapping a shoot uses the everyday word for go out."),
    (6, None, "'Maca finishes at half past eight today?' Keeping statement word order rather than adding a helper word like English does turns the new time into an incredulous question."),
    (7, None, "'And you sent me an email about that?' In Peninsular Spanish, speakers reach for the two-word form you have sent when talking about earlier today, and link the topic with that rather than about that."),
    (8, None, "'What email? There's no email.' After there is no, Spanish drops the word for an, saying literally no there-is mail."),
    (9, None, "'Apparently there was an email, but it never arrived.' Literally it seems that there was an email: ongoing there was sets the background, while completed arrived says it never showed up."),
    (10, None, "'It was an email warning about a schedule change on the series.' Where English uses warning with ing, Spanish uses a clause meaning that warned of a change of schedule."),
    (11, None, "'We had already bought the ticket for Seminci tonight.' Putting the tiny word for already right at the start stresses that the train ticket was paid for before they heard any news."),
    (12, None, "'Now she won't make it. It can't be.' Present-tense she doesn't arrive works where English uses won't make it. Then the handy phrase at the end literally means it cannot be.")
]
