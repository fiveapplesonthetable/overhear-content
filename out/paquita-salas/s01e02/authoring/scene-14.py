ID = 'paquita-salas-s01e02-scene-14'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 14
TITLE = 'Veinticinco años de trayectoria  (Twenty-Five Years in the Business)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'fernando': 'Fernando', 'director': 'Director'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Window 00:13:40,360–00:14:45,880 (cues 282–307).'
INTRO = (
    'Holding the microphone onstage, Paquita boasts about PS Management, reminds everyone that Fernando started out as her assistant, and promises to sign one student. '
    'As soon as she steps down, the school director drops a bombshell about Macarena García. '
    'Listen to the scene first.'
)
OPENER = "Let's go through Paquita's speech and the director's surprise announcement."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = (
    'You heard how Spanish adds playful endings for a cosy industry or a smash-hit play, and how the director reveals Fernando\'s newest signing. '
    'See you next time.'
)
CLOSING = ('paquita', '¡Hasta pronto!')

STORY = [
    ('paquita', 'En PS tenemos una trayectoria de veinticinco años.',
     'At PS we have a twenty-five-year track record.',
     [(284, 'En PS tenemos una trayectoria de'), (284, 'años')],
     'Spelled out the numeral 25.'),
    ('paquita', 'De hecho, Fernando empezó con nosotros, ¿verdad, Fernando?',
     'In fact, Fernando started out with us, right, Fernando?',
     [(285, 'De hecho, Fernando empezó con nosotros, ¿verdad, Fernando?')], ''),
    ('fernando', 'Sí, trabajamos juntos.',
     'Yes, we worked together.',
     [(286, 'Sí, trabajamos juntos')],
     'Kept first sentence of cue 286.'),
    ('paquita', 'Yo le enseñé a moverse en este mundillo.',
     'I taught him how to get around in this little world.',
     [(287, 'Yo le enseñé a moverse en este mundillo')], ''),
    ('paquita', 'En PS hemos hecho tele, cine y, sobre todo, teatro.',
     "At PS we've done telly, film, and above all, theatre.",
     [(288, 'en PS hemos hecho tele'), (289, 'cine'), (290, 'sobre todo'), (290, 'teatro')],
     'Condensed repeated en PS hemos hecho across cues 288–290.'),
    ('paquita', 'Quería daros una buena noticia.',
     'I wanted to give you all some good news.',
     [(292, 'quería daros una buena noticia')],
     'Trimmed opening discourse filler.'),
    ('paquita', 'En PS nos encantan los nuevos talentos.',
     'At PS we love new talent.',
     [(293, 'en PS nos encantan los nuevos talentos')],
     'Trimmed leading decir que.'),
    ('paquita', 'Vamos a representar a uno de vosotros y convertirle en una estrella.',
     "We're going to represent one of you and turn you into a star.",
     [(294, 'vamos a representar a uno de vosotros'), (295, 'y convertirle en una estrella')],
     'Trimmed leading hemos pensado que.'),
    ('paquita', 'Luego os comunicamos nuestra decisión.',
     "We'll let you know our decision later.",
     [(295, 'luego os comunicamos'), (296, 'nuestra decisión')],
     'Joined clause across cues 295 and 296.'),
    ('paquita', 'Te ha quedado un obrón. Muchas gracias.',
     'Your play turned out amazing. Thank you very much.',
     [(299, 'Te ha quedado un obrón'), (297, 'Muchas gracias')],
     'Combined Paquita praise and thanks.'),
    ('director', 'Fernando Canelón es representante de los artistas más importantes de este país.',
     'Fernando Canelón is the agent for the most important artists in this country.',
     [(301, 'Fernando Canelón'), (302, 'Representante de los artistas más importantes de este país')],
     'Linked title to name with es.'),
    ('director', 'Y tiene la reciente incorporación de Macarena García.',
     'And he has the recent addition of Macarena García.',
     [(307, 'Y'), (307, 'la reciente incorporación de Macarena García')],
     'Added tiene so the announcement stands as a complete sentence.'),
]

WALK = [
    (0, None, "'At PS we have a twenty-five-year track record.' The noun here is related to English \"trajectory\" and means a career path or professional history. Twenty-five is written as one joined word in Spanish, blending \"twenty\" and \"five\" seamlessly."),
    (1, None, "'In fact, Fernando started out with us, right, Fernando?' The opener literally says \"of fact\", a handy two-word chunk whenever you want to add proof. Tacking \"truth?\" onto the end turns any statement into \"right?\" or \"isn't that so?\"."),
    (2, None, "'Yes, we worked together.' For regular \"-ar\" actions, \"we work\" and \"we worked\" sound and look identical, with context making the past time clear. \"Together\" carries a plural ending to match Fernando and Paquita."),
    (3, None, "'I taught him how to get around in this little world.' The word for \"taught\" also means \"showed\", and \"move oneself\" captures navigating an industry. Adding a cosy diminutive ending to \"world\" gives Spain's classic term for a tight-knit scene like showbiz."),
    (4, None, "'At PS we've done telly, film, and above all, theatre.' Notice how \"television\" clips down to a friendly two-syllable short form in everyday speech. Before \"theatre\", \"above all\" literally says \"over everything\"."),
    (5, None, "'I wanted to give you all some good news.' Saying \"I wanted\" rather than \"I want\" sounds warm and unpushy onstage, just like in polite English. Notice that \"a good news\" is countable and singular in Spanish, whereas English treats \"news\" as uncountable."),
    (6, None, "'At PS we love new talent.' Instead of \"we love new talents\", Spanish flips the structure to \"new talents enchant us\". Because \"talents\" drives the action, the word for \"enchant\" takes a plural ending."),
    (7, None, "'We're going to represent one of you and turn you into a star.' Near the end, \"to turn him\" glues the object ending straight onto the basic form, followed by \"in a star\" where English says \"into a star\". Notice that \"star\" stays feminine even when referring to a male student."),
    (8, None, "'We'll let you know our decision later.' Starting with the everyday word for \"later\" lets Spanish use the simple present \"we communicate to you\" for a near-future plan. The tiny two-letter word before it means \"to you all\" in Spain."),
    (9, None, "'Your play turned out amazing. Thank you very much.' Literally \"to you has remained a huge play\", a natural Spanish idiom for how creative work turns out. Tacking a big expressive suffix onto the feminine word for \"play\" makes it booming and masculine: \"a smash of a play\"."),
    (10, None, "'Fernando Canelón is the agent for the most important artists in this country.' To build \"the most important\", Spanish places \"more\" after the noun \"artists\" rather than before it. Notice that \"artists\" ends in \"-a\" even when masculine, with \"the\" showing the gender."),
    (11, None, "'And he has the recent addition of Macarena García.' In agencies and sports teams alike, Spanish uses \"incorporation\" for a newly signed member joining the roster. Hearing Macarena's full name onstage is how Paquita discovers her star has left."),
]
