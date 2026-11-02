ID = 'paquita-salas-s01e01-scene-07'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 1
SCENE = 7
TITLE = 'Es el buzón  (It\'s Voicemail)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi', 'lidia': 'Lidia'}
SOURCE_NAME = 'Paquita Salas S01E01: Casada con esto'
SOURCE_FILE = 'sources/paquita-salas/s01/e01.es.srt'
SOURCE_NOTE = 'Window 00:06:17,760–00:08:07,560.'
INTRO = ("When the office phone finally rings, Paquita hopes it is Maca, only to hear young actor David asking about a Hyundai commercial. "
         "With Maca's premiere dress still sitting in the office, Paquita leaves Maca an anxious voicemail before praising her performance in the film Vicenta. "
         "Listen to the Spanish first.")
OPENER = "Let's go through the phone calls and voicemail."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how Spanish says 'next week' as 'the week that comes', and how two short object words stack up before 'take down' or 'tack onto' a command. See you next time.")
CLOSING = ('magui', '¡Hasta mañana!')

STORY = [
    ('paquita', '¡Uy! ¡El teléfono!',
     'Oh! The phone!',
     [(138, '¡Uy! ¡El teléfono!')], ''),
    ('paquita', 'David, dime.',
     'David, tell me.',
     [(141, 'David'), (142, 'Dime')], ''),
    ('paquita', 'No llamaron de Hyundai.',
     "They didn't call from Hyundai.",
     [(147, 'No llamaron de Hyundai')], ''),
    ('paquita', 'La semana que viene yo te llamo, ¿vale? Un beso.',
     "I'll call you next week, okay? A kiss.",
     [(149, 'La semana que viene'), (149, 'yo te llamo, ¿vale?'), (149, 'un beso')], ''),
    ('paquita', 'Hija, pensaba que era Maca. Maca nada, ¿no?',
     'Girl, I thought it was Maca. Nothing from Maca, right?',
     [(150, 'Hija, pensaba que era Maca. Maca nada, ¿no?')], ''),
    ('magui', 'Maca nada. Tiene aquí el vestido.',
     'Nothing from Maca. Her dress is here.',
     [(151, 'Maca nada'), (152, 'Tiene aquí el vestido')], ''),
    ('paquita', 'Es el buzón. Maca, escucha.',
     "It's voicemail. Maca, listen.",
     [(156, 'Es el buzón'), (157, 'Maca, escucha')], ''),
    ('paquita', 'Estamos Magüi y yo aquí. Salimos ya a la boda.',
     "Magüi and I are here. We're leaving now for the wedding.",
     [(158, 'estamos Magüi y yo aquí. Salimos ya a la boda')],
     'Trimmed surname tag at the end.'),
    ('paquita', 'Me quedo un poco preocupada porque no consigo localizarte.',
     "I'm a bit worried because I can't reach you.",
     [(159, 'Me quedo un poco preocupada'), (160, 'porque'), (160, 'no consigo localizarte')], ''),
    ('lidia', '¡Dale recuerdos!',
     'Give her my regards!',
     [(161, '¡Dale recuerdos!')], ''),
    ('paquita', 'Lidia, por favor. Tenemos aquí tu vestido.',
     'Lidia, please. We have your dress here.',
     [(162, 'Lidia, por favor. Tenemos aquí tu vestido')], ''),
    ('paquita', 'Te lo bajamos al portero.',
     "We'll take it down to the doorman for you.",
     [(163, 'Te lo bajamos al portero')], ''),
    ('paquita', 'Cuando me escuches, mándame un mensajito.',
     'When you hear me, send me a quick message.',
     [(166, 'Cuando me escuches, mándame un mensajito')], ''),
    ('paquita', 'Vicenta es una película muy bonita y Macarena brilla.',
     'Vicenta is a very lovely film, and Macarena shines.',
     [(169, 'Vicenta'), (169, 'es una película muy bonita'), (177, 'Macarena'), (177, 'Brilla')], '')
]

WALK = [
    (0, None, "'Oh! The phone!' That quick two-letter sound at the start expresses sudden surprise or a small startle when the phone rings. Notice the written accent mark on the word for telephone."),
    (1, None, "'David, tell me.' Answering the phone with tell me is completely polite and natural in Spain, where English would say speaking or go ahead."),
    (2, None, "'They didn't call from Hyundai.' Spanish uses the plural they-called form without naming any subject to mean nobody from Hyundai called."),
    (3, None, "'I'll call you next week, okay? A kiss.' Next week is literally the week that comes. Then Spain's universal check-in word asks okay, and friends or clients routinely sign off phone calls with a kiss."),
    (4, None, "'Girl, I thought it was Maca. Nothing from Maca, right?' Older Spanish women warmly address younger women with the word for daughter even when they aren't related. Putting nothing right after Maca makes a crisp shorthand question."),
    (5, None, "'Nothing from Maca. Her dress is here.' Literally, she has here the dress: instead of saying her dress, Spanish says she has the dress here."),
    (6, None, "'It's voicemail. Maca, listen.' The word for letterbox or mailbox also means phone voicemail in Spain. Then Paquita uses the casual command form of listen."),
    (7, None, "'Magüi and I are here. We're leaving now for the wedding.' Spanish happily puts we are before Magüi and I. In the second sentence, present-tense we go out plus already means we're heading out right now."),
    (8, None, "'I'm a bit worried because I can't reach you.' Literally, I remain a little worried, with the feminine ending matching Paquita. After I don't manage, to locate tacks casual you onto its end."),
    (9, None, "'Give her my regards!' Literally, give to her memories: plural memories is the everyday Spanish word for regards or warm wishes to pass along."),
    (10, None, "'Lidia, please. We have your dress here.' Literally, for favour, the universal polite phrase for please, used here to hush Lidia while recording the message."),
    (11, None, "'We'll take it down to the doorman for you.' Look at the neat chain at the front: for you, then masculine it for the dress, then we bring down. Before masculine doorman, to plus the contracts into one two-letter word."),
    (12, None, "'When you hear me, send me a quick message.' After when talking about the future, listen switches its vowel from a to e. At the end, adding the affectionate diminutive ending turns message into a quick little text."),
    (13, None, "'Vicenta is a very lovely film, and Macarena shines.' Notice how very lovely sits after the word for film rather than before it. The final word literally means shines or sparkles.")
]
