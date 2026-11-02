ID = 'paquita-salas-s01e02-scene-04'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 4
TITLE = "La estantería de los videobooks  (The Showreel Shelf)"
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Native Spanish captions from episode stream. Scene window 00:03:04,760–00:04:11,600.'
INTRO = ("Back in the PS Management office, Paquita shows off the shelf where hopeful actors send their showreels by courier. "
         "As she and Magüi browse through old reels, Paquita passionately defends the wealth of acting talent in Spain and praises stars known by a single first name like Carmen. "
         "Listen to the Spanish first.")
OPENER = "Let's walk through what Paquita and Magüi say at the showreel shelf."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how Spanish borrows 'videobook' for an actor's showreel, how 'the one of' stands in for apostrophe-s, "
         "and how 'itself speaks' expresses 'people mean'. See you next time.")
CLOSING = ('paquita', '¡Nos vemos!')

STORY = [
    ('paquita', 'Esta es la estantería de los videobooks.',
     'This is the shelf of showreels.',
     [(55, 'esta es la estantería de los'), (55, 'videobooks')],
     'Removed discourse opener, tag question, and subtitle quotation marks.'),
    ('paquita', 'Vienen a veces a dejarlos por mensajería.',
     'Sometimes people come to drop them off by courier.',
     [(57, 'vienen a veces a dejarlos'), (58, 'Mensajería')],
     'Combined with por mensajería across the two cues.'),
    ('paquita', 'Ha llegado el momento de verlos.',
     'The time has come to watch them.',
     [(59, 'ha llegado el momento de verlos')],
     'Trimmed opening clause.'),
    ('magui', 'Mira el de Miguel Ángel Muñoz.',
     "Look at Miguel Ángel Muñoz's one.",
     [(70, 'Mira, el de Miguel Ángel Muñoz')],
     'Removed comma after Mira.'),
    ('paquita', 'Empezó con nosotros.',
     'He started out with us.',
     [(71, 'Empezó con nosotros')],
     'Omitted trailing fragment with numeral.'),
    ('paquita', 'Hay muchísimo talento en España.',
     'There is tons of talent in Spain.',
     [(72, 'talento en España'), (72, 'Hay muchísimo en España')],
     'Combined noun and affirmative statement.'),
    ('paquita', 'Que no os engañen.',
     "Don't let them fool you.",
     [(73, 'Que no os engañen')], ''),
    ('magui', 'Está bien elegida la foto.',
     'The photo is well chosen.',
     [(75, 'Está bien elegida la foto')],
     'Trimmed second clause.'),
    ('paquita', 'Es importante la gente que solo se pone un nombre.',
     'People who only use one name are important.',
     [(76, 'Es importante la gente que solo se pone un nombre')], ''),
    ('magui', '¿Qué Carmen es?',
     'Which Carmen is it?',
     [(80, '¿Qué Carmen es?')], ''),
    ('paquita', 'Carmen Sevilla.',
     'Carmen Sevilla.',
     [(81, 'Carmen Sevilla')], ''),
    ('paquita', 'Solo dices Carmen y ya sabes de quién se habla.',
     'You just say Carmen and you already know who people mean.',
     [(82, 'Solo dices'), (82, 'Carmen'), (82, 'y ya sabes de quién se habla')],
     'Removed subtitle quotation marks.')
]

WALK = [
    (0, None, "'This is the shelf of showreels.' Built from the word for \"shelf\", the longer feminine word here means a whole bookcase or shelving unit. Spanish casting agencies borrow the English compound \"videobook\" for an actor's video showreel."),
    (1, None, "'Sometimes people come to drop them off by courier.' Literally \"they come at times to leave them by courier\", using plural \"they come\" without naming who, where English says \"people come\". Notice how \"them\" tacks right onto the end of \"to leave\"."),
    (2, None, "'The time has come to watch them.' Literally \"has arrived the moment of to see them\", putting \"has arrived\" ahead of \"the moment\". At the end, the little word for \"them\" attaches directly onto \"to see\" as one smooth word."),
    (3, None, "'Look at Miguel Ángel Muñoz's one.' Instead of adding an apostrophe-s to the actor's name, Spanish says \"the of Miguel Ángel Muñoz\", letting masculine \"the\" stand in for \"the showreel\" without repeating the word."),
    (4, None, "'He started out with us.' The stressed -ó ending marks a completed past event for \"he\" or \"she\", so no separate word for \"he\" is needed. After \"with\", Spanish uses the full plural word for \"us\"."),
    (5, None, "'There is tons of talent in Spain.' Adding the intensifying ending -ísimo onto \"much\" boosts it from \"a lot of\" to \"tons of\" or \"so much\", matching the masculine singular ending of \"talent\"."),
    (6, None, "'Don't let them fool you.' Starting with \"that\" plus \"not\" creates an emphatic warning, literally \"that they not deceive you all\". In Spain, the little two-letter word before \"fool\" is the casual plural \"you\" addressed to everyone watching."),
    (7, None, "'The photo is well chosen.' Even though the clipped everyday word for \"photo\" ends in -o, it stays feminine because it is short for \"photograph\", so \"chosen\" takes the feminine -an ending. Putting \"the photo\" at the end highlights the praise \"is well chosen\" first."),
    (8, None, "'People who only use one name are important.' Because the collective word for \"people\" is grammatically singular, \"is important\" stays singular too. Towards the end, \"puts on oneself a name\" is the natural Spanish idiom for adopting a stage name."),
    (9, None, "'Which Carmen is it?' Right before a name or thing, the simple word for \"what\" does the job of English \"which\", asking Paquita to narrow down which famous Carmen she means."),
    (10, None, "'Carmen Sevilla.' Paquita names legendary Spanish actress, singer, and television presenter Carmen Sevilla, whose stage surname comes from her home city of Sevilla rather than her family name."),
    (11, None, "'You just say Carmen and you already know who people mean.' Spanish never strands \"of\" or \"about\" at the end of a question clause, saying \"of whom\" together rather than \"who ... about\". Then \"itself speaks\" works as an impersonal way to say \"people are talking\".")
]
