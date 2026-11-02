ID = 'paquita-salas-s01e02-scene-02'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = "La actriz tres sesenta  (The All-Round Actress)"
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Native Spanish captions from episode stream. Scene window 00:01:06,360–00:02:16,360.'
INTRO = ("Sitting in the PS Management office, Paquita and Magüi describe their ideal all-round actress who excels in drama, comedy, singing, and dancing. "
         "After holding up Natalie Portman as a perfect example, Magüi admits she wants breakfast and Paquita recalls that Macarena never ate in the morning. "
         "Listen to the Spanish first.")
OPENER = "Let's hear how Paquita defines the ideal actress they want to sign."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how Spanish drops 'for' inside 'look for', how breakfast is a single action word literally meaning 'un-fast', "
         "and how feelings like wanting or liking put the person at the front with 'to me' or 'to Macarena'. See you next time.")
CLOSING = ('magui', '¡Hasta luego!')

STORY = [
    ('paquita', 'Nosotros buscamos a la actriz tres sesenta.',
     'We are looking for the three-sixty actress.',
     [(22, 'nosotros buscamos a'), (23, 'la actriz')],
     'Spelled out 360 as tres sesenta.'),
    ('paquita', 'Es buena en drama y es buena en comedia.',
     'She is good at drama and she is good at comedy.',
     [(24, 'es buena en drama'), (24, 'es buena en comedia')],
     'Linked the two parallel clauses with y.'),
    ('magui', 'Quizás sabe cantar y bailar.',
     'Maybe she can sing and dance.',
     [(25, 'quizás sabe cantar y bailar')],
     'Trimmed trailing relative clause.'),
    ('paquita', 'Ser buena persona es una cosa bonita en la vida.',
     'Being a good person is a lovely thing in life.',
     [(27, 'Ser buena persona'), (28, 'es una cosa bonita en la vida')], ''),
    ('paquita', 'Natalie Portman es un ejemplo perfecto.',
     'Natalie Portman is a perfect example.',
     [(34, 'Natalie Portman es'), (35, 'un ejemplo perfecto')],
     'Trimmed trailing prepositional phrase.'),
    ('magui', 'Está muy bien, Paquita.',
     "That's very good, Paquita.",
     [(37, 'Está muy bien, Paquita')], ''),
    ('magui', 'Me apetece desayunar.',
     'I feel like having breakfast.',
     [(37, 'Me apetece desayunar')], ''),
    ('magui', 'Me he levantado pronto.',
     'I got up early.',
     [(38, 'me he levantado pronto')],
     'Trimmed spoken fillers.'),
    ('paquita', 'Desayunar es muy importante.',
     'Having breakfast is very important.',
     [(39, 'Desayunar es muy importante')],
     'Kept first clause without repetition.'),
    ('paquita', 'Es la comida más importante del día.',
     'It is the most important meal of the day.',
     [(40, 'La comida más importante del día')],
     'Added Es to form a complete beginner sentence.'),
    ('paquita', 'A Macarena nunca le gustó desayunar.',
     'Macarena never liked having breakfast.',
     [(41, 'A Macarena nunca le gustó desayunar')], ''),
    ('paquita', 'Estaba muy delgadita.',
     'She was very slim.',
     [(43, 'Estaba muy delgadita')], '')
]

WALK = [
    (0, None, "'We are looking for the three-sixty actress.' One Spanish word already means \"look for\", so the little \"a\" after it is not \"for\" — it marks a person as the object. Splitting three hundred and sixty into \"three sixty\" mirrors casual English \"three-sixty\" for a complete all-rounder."),
    (1, None, "'She is good at drama and she is good at comedy.' Where English says \"good at\", Spanish uses the little word meaning \"in\". Notice the feminine -an ending on \"good\" because Paquita is describing a female performer."),
    (2, None, "'Maybe she can sing and dance.' For learned skills like singing or dancing, Spanish uses the word meaning \"knows\" followed directly by \"to sing\" and \"to dance\", with no word for \"how\" in between. At the start, the word for \"maybe\" works with or without its final -s."),
    (3, None, "'Being a good person is a lovely thing in life.' Starting with the basic form \"to be\" is how Spanish expresses \"being\" as an idea. Near the end, Spanish says \"in the life\" rather than bare \"in life\" when talking about life in general."),
    (4, None, "'Natalie Portman is a perfect example.' Even though Natalie Portman is a woman, the words for \"a\" and \"perfect\" stay masculine because they match the masculine word \"example\". Describing words like \"perfect\" normally sit right after the word they describe."),
    (5, None, "'That's very good, Paquita.' Using the state-and-condition form of \"is\" with \"very well\" is Spain's standard everyday way to approve of an idea or plan. You can swap in this handy chunk whenever someone makes a fair point."),
    (6, None, "'I feel like having breakfast.' Literally \"to me it appeals to breakfast\", a natural Spanish way to say what you fancy eating or doing right now. Notice how English needs \"having breakfast\", whereas Spanish packs the whole meal into one single word built from \"un-fast\"."),
    (7, None, "'I got up early.' Because \"getting up\" literally means \"lifting oneself\", \"myself\" sits at the very front before \"have lifted\". In Spain, this \"have\" past form is the normal choice for something that happened earlier this same morning, and the final word covers both \"soon\" and \"early\"."),
    (8, None, "'Having breakfast is very important.' Once again that single action word meaning \"to eat breakfast\" acts as the subject of the sentence where English uses an -ing form. \"Important\" ends in -e, so its singular form never changes between masculine and feminine."),
    (9, None, "'It is the most important meal of the day.' Built from the root for \"eat\", the word for \"meal\" also means \"food\" or \"lunch\" depending on context. Towards the end, \"of\" and masculine \"the\" fuse together into one short word meaning \"of the\"."),
    (10, None, "'Macarena never liked having breakfast.' Instead of making Macarena the subject of \"liked\", Spanish says \"to Macarena never to her pleased to breakfast\". Both \"to Macarena\" and the tiny word for \"to her\" appear together, which is standard whenever you name the person up front."),
    (11, None, "'She was very slim.' Adding the affectionate diminutive ending -ita onto the word for \"thin\" softens the description to \"slim\" or \"petite\" rather than sounding harsh. Paquita also chooses the state form \"was\" because weight and appearance can change.")
]
