ID = 'paquita-salas-s01e01-scene-11'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 1
SCENE = 11
TITLE = 'Casada con esto  (Married to This Job)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'alex': 'Álex', 'paquita': 'Paquita', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E01: Casada con esto'
SOURCE_FILE = 'sources/paquita-salas/s01/e01.es.srt'
SOURCE_NOTE = 'Window 00:11:41,760–00:13:47,800.'
INTRO = ("Having finished checking the socket, Álex asks whether Paquita and Magüi have looked inside their spam folder — and uncovers over a hundred unread industry emails, including Juanfran's urgent warnings. "
         "Paquita forgives a mortified Magüi and calls off Paco's wedding so she can drive Maca to Valladolid herself. "
         "Listen to the Spanish first.")
OPENER = "Let's walk through the spam-folder discovery and Paquita's decision."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how 'soler' expresses things that usually happen, and the episode's title line 'casada con esto' — married to this job. See you next time.")
CLOSING = ('paquita', '¡Hasta pronto!')

STORY = [
    ('alex', 'Oye, ¿habéis mirado en la carpeta de spam?',
     'Hey, have you looked in the spam folder?',
     [(270, 'Oye'), (270, 'habéis mirado en la carpeta de'), (270, 'spam')], ''),
    ('paquita', '¿Eso qué es? Yo no tengo carpeta de spam.',
     "What's that? I don't have a spam folder.",
     [(271, '¿Eso qué es?'), (272, 'Yo no tengo'), (272, 'spam')],
     'Used carpeta de spam consistently with Álex\'s question.'),
    ('alex', 'Es la carpeta donde van los correos de contactos que no tienes guardados.',
     "It's the folder where emails from contacts you haven't saved go.",
     [(273, 'es la carpeta donde van los correos de contactos'), (274, 'que no tienes guardados')], ''),
    ('alex', 'Mira, aquí. Está llena totalmente.',
     "Look, here. It's completely full.",
     [(276, 'Mira. Aquí'), (288, 'Está llena, totalmente')],
     'Avoided coarse exclamation in cue 277.'),
    ('magui', 'Mira, de ayer y de muchos días.',
     'Look, from yesterday and from many days ago.',
     [(280, 'Mira, de ayer'), (281, 'De muchos días')], ''),
    ('alex', 'Juanfran, urgente. Cambio de horario, Macarena García.',
     'Juanfran, urgent. Schedule change, Macarena García.',
     [(281, 'Juanfran, urgente'), (282, 'Cambio de horario, Macarena García')], ''),
    ('magui', 'Paquita, no lo sabía, de verdad. Yo no había mirado esa carpeta.',
     "Paquita, I didn't know, honestly. I hadn't checked that folder.",
     [(291, 'Paquita, no lo sabía. De verdad'), (287, 'yo no había mirado')],
     'Replaced la cuenta with esa carpeta for clarity.'),
    ('paquita', 'Esto es un problema que suele pasar. No te preocupes.',
     "This is a problem that often happens. Don't worry.",
     [(293, 'Esto es un problema que suele pasar'), (294, 'no te preocupes')], ''),
    ('paquita', 'Tú te quedas solucionando lo del mail.',
     'You stay here sorting out the email issue.',
     [(296, 'Tú te quedas solucionando lo del mail')], ''),
    ('paquita', 'No puede ser que Maca se pierda el estreno de la Seminci.',
     "Maca can't miss the Seminci premiere.",
     [(297, 'no puede ser'), (297, 'que Maca'), (298, 'se pierda el estreno de la Seminci')], ''),
    ('paquita', 'Hoy no hay boda, que yo estoy casada con esto.',
     "There's no wedding today, because I'm married to this job.",
     [(299, 'Hoy no hay boda, que yo estoy casada con esto')], ''),
    ('magui', 'Quiero pedir disculpas a Macarena García por arruinar su gran noche.',
     'I want to apologise to Macarena García for ruining her big night.',
     [(300, 'Quiero pedir disculpas a Macarena García'), (301, 'por arruinar su gran noche')], ''),
    ('magui', 'No pasará nunca más. Te lo prometo.',
     'It will never happen again. I promise you.',
     [(307, 'No pasará nunca más'), (308, 'Te lo prometo')], '')
]

WALK = [
    (0, None, "'Hey, have you looked in the spam folder?' Castilian Spanish uses the plural you-all form of have when addressing two friends together. Folder is feminine, and literally folder of spam."),
    (1, None, "'What's that? I don't have a spam folder.' Putting that before what is turns the question into a puzzled what on earth is that, using neuter that because she doesn't even recognise the word spam."),
    (2, None, "'It's the folder where emails from contacts you haven't saved go.' Alongside borrowed mail, Spanish uses the native plural word for post or messages. At the end, saved takes a masculine plural ending to match contacts."),
    (3, None, "'Look, here. It's completely full.' Because folder is feminine, full ends in a, and takes the state form because the folder has filled up over time."),
    (4, None, "'Look, from yesterday and from many days ago.' Notice how Spanish needs no word for ago here: simply saying of yesterday and of many days tells us how old the messages are."),
    (5, None, "'Juanfran, urgent. Schedule change, Macarena García.' Álex reads out the email subject line word for word: urgent keeps the same final vowel for either gender, and change of schedule needs no word for a."),
    (6, None, "'Paquita, I didn't know, honestly. I hadn't checked that folder.' Spanish always includes the little word for it in I didn't know it, even where English stops at I didn't know. Then I had not looked places the oversight earlier than now."),
    (7, None, "'This is a problem that often happens. Don't worry.' Notice that word ending in a: problem is masculine in Spanish despite its final vowel! After that, a handy helper word plus to happen means tends to happen or usually happens."),
    (8, None, "'You stay here sorting out the email issue.' Combining you remain with an ing-form means you stay behind working on it, and that neat neuter phrase at the end means the email business."),
    (9, None, "'Maca can't miss the Seminci premiere.' Losing something is one thing, but adding the little word for herself turns lose into miss out on an event. Premiere is masculine here."),
    (10, None, "'There's no wedding today, because I'm married to this job.' Here is the episode's title! Where English is married to something, Spanish says married with this, and links the reason with casual that meaning because."),
    (11, None, "'I want to apologise to Macarena García for ruining her big night.' Apologising is literally asking for excuses. Before night, the word for great drops its final syllable so it means big or special rather than physically large."),
    (12, None, "'It will never happen again. I promise you.' Literally it will not happen never more, stacking negative words together for emphasis, followed by to you it I promise.")
]
