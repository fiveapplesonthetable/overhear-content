ID = 'paquita-salas-s01e02-scene-05'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = "Una joya por descubrir  (A Gem to Discover)"
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Native Spanish captions from episode stream. Scene window 00:04:11,680–00:04:54,720.'
INTRO = ("Continuing through the showreel shelf, Paquita and Magüi set aside reels they have already watched and come across actor Aakif Ndel. "
         "Agreeing that casting agencies need to broaden their perspective, Paquita pulls his reel out as a potential gem to discover. "
         "Listen to the Spanish first.")
OPENER = "Let's go through the scene as Paquita and Magüi sort the reels."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how Spanish puts an object like 'these ones' at the front and echoes it with 'them', "
         "how 'there is that' expresses 'one must', and how casual Spanish uses 'equal' to mean 'maybe'. See you next time.")
CLOSING = ('magui', '¡Hasta mañana!')

STORY = [
    ('paquita', '¿Qué tenemos? Tenemos muchas cosas.',
     'What do we have? We have lots of things.',
     [(84, '¿Qué tenemos? Tenemos muchas cosas')], ''),
    ('paquita', '¿Qué más hay por aquí?',
     'What else is around here?',
     [(84, '¿qué más hay por aquí?')],
     'Trimmed conversational fillers.'),
    ('magui', 'Estos ya los hemos visto.',
     "We've already seen these ones.",
     [(85, 'Estos ya los hemos visto')],
     'Omitted trailing tampoco.'),
    ('magui', 'Aakif Ndel.',
     'Aakif Ndel.',
     [(91, 'Aakif Ndel')], ''),
    ('paquita', 'Hay que abrir un poco la óptica.',
     'We need to broaden our perspective a little.',
     [(94, 'hay que abrir'), (95, 'Un poco la óptica')],
     'Combined across cues into a clean standalone sentence.'),
    ('magui', 'Ya era hora también.',
     'It was about time, too.',
     [(95, 'Ya era hora también')], ''),
    ('paquita', 'Es verdad.',
     "That's true.",
     [(96, 'Es verdad')], ''),
    ('paquita', 'Pues este apártalo.',
     'Well, set this one aside.',
     [(96, 'Pues este apártalo')],
     'Split compound sentence into standalone clauses.'),
    ('paquita', 'Este lo vamos a ver.',
     'We are going to watch this one.',
     [(96, 'este lo vamos a ver')],
     'Removed leading conjunction porque.'),
    ('paquita', 'Igual aquí hay una joya por descubrir.',
     'Maybe there is a gem to discover here.',
     [(97, 'igual aquí hay una joya por descubrir')],
     'Removed leading conjunction porque.'),
    ('paquita', 'A veces también lo llaman para protagonizar.',
     'Sometimes they also call him for a leading role.',
     [(98, 'a veces'), (98, 'también lo llaman para protagonizar')],
     'Omitted racial noun phrase.')
]

WALK = [
    (0, None, "'What do we have? We have lots of things.' Because the -emos ending already means \"we\", Spanish needs no separate word for \"we\" in either the question or the answer. Notice the feminine plural -as ending on \"lots of\" to match \"things\"."),
    (1, None, "'What else is around here?' Literally \"what more is there through here?\", using \"more\" where English says \"else\". Pairing \"by\" or \"through\" with \"here\" softens plain \"here\" into \"around here\"."),
    (2, None, "'We've already seen these ones.' Putting \"these ones\" right at the start highlights which showreels Magüi is pointing to, and Spanish then echoes them with a little word for \"them\" before \"we have seen\". Notice the irregular past form \"seen\"."),
    (3, None, "'Aakif Ndel.' After sounding out the unfamiliar spelling on the label, Magüi reads the actor's full name clearly off the spine of his showreel case."),
    (4, None, "'We need to broaden our perspective a little.' Starting with a two-word chunk that literally says \"there is that\" is Spain's go-to way to say \"one must\" or \"we need to\" without singling anyone out. Literally \"open a little the lens\" is a vivid idiom for broadening your outlook."),
    (5, None, "'It was about time, too.' Literally \"already it was hour\", a fixed everyday expression for \"about time!\" when something overdue finally happens. You can use this exact three-word core whenever someone is late or slow to change."),
    (6, None, "'That's true.' Literally \"it is truth\", using the word for \"truth\" rather than a describing word for \"true\", and needing no word for \"that\" at the front."),
    (7, None, "'Well, set this one aside.' Once again Paquita puts \"this one\" first, then glues \"it\" straight onto the casual command form meaning \"put aside\" or \"separate\". That opening word means \"well then\" or \"so\"."),
    (8, None, "'We are going to watch this one.' Putting \"this one\" up front again triggers the little word for \"it\" right before \"we are going to watch\". In Spanish, \"we go to\" plus \"to see\" is the everyday way to talk about an immediate plan."),
    (9, None, "'Maybe there is a gem to discover here.' Although the first word usually means \"equal\" or \"the same\", in everyday Peninsular chat it constantly means \"maybe\" or \"for all we know\". Near the end, \"for to discover\" is how Spanish expresses \"yet to be discovered\"."),
    (10, None, "'Sometimes they also call him for a leading role.' Literally \"at times\" means \"sometimes\", and \"they call\" works impersonally for casting directors in general. After \"for\", Spanish uses a single action word meaning \"to play the lead\" rather than \"a leading role\".")
]
