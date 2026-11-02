ID = 'paquita-salas-s01e02-scene-01'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = "Cuando una puerta se cierra  (When One Door Closes)"
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Native Spanish captions from episode stream. Scene window 00:00:12,240–00:01:06,280.'
INTRO = ("In the PS Management office in Madrid, Paquita and her assistant Magüi struggle to take Macarena's framed poster down from the wall. "
         "Once the frame finally comes off, Paquita quotes a classic Spanish proverb about doors opening and declares the start of their talent hunt. "
         "Listen to the Spanish first, then we'll walk through each line.")
OPENER = "Let's start with Paquita telling Magüi to take the poster down."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how Spanish glues object words like 'it' and 'me' straight onto the end of casual commands, "
         "and how adding 'self' turns 'closes' and 'opens' into things a door appears to do on its own. See you next time.")
CLOSING = ('paquita', '¡Hasta pronto!')

STORY = [
    ('paquita', 'Quítalo, claro.',
     'Take it down, of course.',
     [(1, 'Quítalo, claro')], ''),
    ('magui', 'Lo estoy quitando.',
     "I'm taking it down.",
     [(2, 'Lo estoy quitando')], ''),
    ('magui', 'No puedo sola.',
     "I can't do it on my own.",
     [(3, 'No puedo sola')], ''),
    ('paquita', 'Dame la mano.',
     'Give me your hand.',
     [(5, 'Dame la mano')], ''),
    ('magui', '¿Esto está clavado?',
     'Is this nailed in?',
     [(7, '¿Esto está clavado?')], ''),
    ('paquita', 'Espera, cojo de abajo.',
     "Hold on, I'll grab from underneath.",
     [(7, 'Espera, cojo de abajo')], ''),
    ('paquita', 'Tú tira de ahí.',
     'You pull from there.',
     [(11, 'Tú tira de ahí')], ''),
    ('magui', 'Uno, dos y tres.',
     'One, two, and three.',
     [(12, 'Uno, dos y tres')], ''),
    ('paquita', 'Ya está.',
     "There, it's done.",
     [(13, 'Ya está')], ''),
    ('paquita', 'Ya sabes lo que dice el refranero español.',
     'You know what Spanish proverbs say.',
     [(15, 'Ya sabes lo que dice el refranero español')], ''),
    ('paquita', 'Cuando una puerta se cierra, una puerta se abre.',
     'When one door closes, a door opens.',
     [(16, 'Cuando una puerta'), (16, 'se cierra'), (17, 'Una puerta se abre')],
     'Removed hesitation and subtitle quotation marks.'),
    ('paquita', 'Ahora empieza la caza de talentos.',
     'Now the talent hunt begins.',
     [(17, 'ahora empieza'), (18, 'la caza'), (19, 'De talentos')],
     'Combined across three cues and removed subtitle quotation marks.')
]

WALK = [
    (0, None, "'Take it down, of course.' The first word packs the casual command form meaning \"remove\" and the word for \"it\" into a single word. Adding the word for \"clear\" at the end is a handy way to say \"of course\" or \"obviously\"."),
    (1, None, "'I'm taking it down.' Notice how the little word for \"it\" jumps in front of \"am\" here, whereas in the command a moment ago it tucked onto the end. The -ando ending works just like English -ing for something happening right now."),
    (2, None, "'I can't do it on my own.' Spanish needs no extra words for \"do it\" after \"I can't\", leaving the meaning compact and natural. Because Magüi is a woman, the word for \"alone\" takes the feminine -an ending rather than -o."),
    (3, None, "'Give me your hand.' Once again \"me\" attaches straight onto the short command form for \"give\", making one brisk two-syllable word. For body parts, Spanish says \"the hand\" rather than \"your hand\"."),
    (4, None, "'Is this nailed in?' The word for \"this\" uses its neuter -o form because Magüi is pointing at the whole framed object without naming it. Built from the word for \"nail\", the final word describes the state of being nailed to the wall."),
    (5, None, "'Hold on, I'll grab from underneath.' In Spain, this everyday word means \"take\", \"catch\", or \"grab hold of\", and Paquita uses the present form \"I grab\" for what she is about to do right now. Literally \"of underneath\" means \"from the bottom\"."),
    (6, None, "'You pull from there.' Putting the word for \"you\" up front contrasts Magüi's job with Paquita's own grip down below. Notice that \"pull\" pairs with the little word for \"of\" or \"from\" when you tug on something."),
    (7, None, "'One, two, and three.' Counting a lift out loud uses the standalone masculine form \"uno\" rather than the shortened \"un\" that appears before masculine words. Between the last two numbers, Spanish slips in the single-letter word for \"and\"."),
    (8, None, "'There, it's done.' Literally \"already it is\", a tiny two-word chunk you'll hear everywhere in Spain the instant a task finishes. You can swap in this same handy phrase when food is ready, a payment goes through, or a problem is sorted."),
    (9, None, "'You know what Spanish proverbs say.' Rather than a plural word for \"proverbs\", Spanish has a collective singular word built from the root for \"saying\", meaning the whole treasury of traditional folk sayings. In the middle, a two-word chunk literally means \"that which\" for \"what\"."),
    (10, None, "'When one door closes, a door opens.' Both \"closes\" and \"opens\" put a tiny word meaning \"itself\" right before the action, which is how Spanish describes doors shutting or opening without naming who pushed them. Notice how the feminine word \"una\" covers both \"one\" and \"a\"."),
    (11, None, "'Now the talent hunt begins.' Spanish flips the English order to literally \"the hunt of talents\", making \"talents\" plural after \"of\". The word for \"begins\" sits right after \"now\", putting the spotlight on \"the talent hunt\" at the very end.")
]
