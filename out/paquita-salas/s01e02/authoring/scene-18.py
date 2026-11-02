ID = 'paquita-salas-s01e02-scene-18'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 18
TITLE = 'Vas a triunfar  (You Are Going to Triumph)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi', 'mariona': 'Mariona'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Window 00:18:07,240–00:18:42,600 plus merged closing montage 00:18:42,680–00:20:32,280 (cues 381–393).'
INTRO = (
    'Cheering from the aisle, Paquita promises Mariona roles in Spain\'s biggest television series and marches proudly out of the theatre with Magüi. '
    'As the upbeat closing montage plays, Paquita welcomes Mariona through the door of PS Management. '
    'Listen to the finale first.'
)
OPENER = "Let's go through Paquita's triumphant exit and Mariona's welcome."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = (
    'You heard how Spanish cheers a future star on, marches out in style, talks about being good at something, and says "welcome". '
    'See you next time.'
)
CLOSING = ('paquita', '¡Nos vemos!')

STORY = [
    ('paquita', 'Cariño, claro que vas a triunfar.',
     "Darling, of course you're going to triumph.",
     [(381, 'Cariño, claro que vas a triunfar')],
     'Split first clause of cue 381.'),
    ('paquita', 'Claro que eres una estrella.',
     "Of course you're a star.",
     [(381, 'claro que eres una'), (381, 'estrella')],
     'Omitted coarse intensifier before estrella.'),
    ('paquita', 'Tú harás Velvet, Vis a vis y El secreto de Puente Viejo.',
     "You'll do Velvet, Vis a vis, and El secreto de Puente Viejo.",
     [(382, 'tú harás Velvet'), (382, 'Vis a vis'), (383, 'y'), (383, 'El secreto de Puente Viejo')],
     'Removed subtitle quotation marks, hasta, and coarse trailing clause.'),
    ('paquita', 'A ti ya te pillaré, Canelón. Vámonos.',
     "I'll catch up with you later, Canelón. Let's go.",
     [(384, 'A ti ya te pillaré, Canelón. Vámonos')],
     'Trimmed opening Y a ti.'),
    ('paquita', 'Venga, desfilando.',
     'Come on, marching out.',
     [(385, 'Venga, desfilando')], ''),
    ('paquita', 'Por favor, no me toques, señor.',
     "Please don't touch me, sir.",
     [(387, 'Por favor, no me toques, señor')],
     'Trimmed repeated Por favor, ¿eh?.'),
    ('magui', '¡No la toques!',
     "Don't touch her!",
     [(388, '¡No la toques!')], ''),
    ('mariona', 'Todo va genial.',
     'Everything is going great.',
     [(389, 'todo va genial')],
     'Adapted upbeat montage line without leading lyric # Que.'),
    ('paquita', 'A mí disimular se me da muy bien.',
     'Putting on a brave face comes very naturally to me.',
     [(391, 'a mí disimular se me da muy bien')],
     'Adapted montage line without leading lyric # que.'),
    ('mariona', 'Si quieres, te digo que estoy muy bien.',
     "If you like, I'll tell you I'm doing really well.",
     [(392, 'Si quieres, te digo'), (393, 'que estoy muy bien')],
     'Joined montage lines 392 and 393 cleanly.'),
    ('paquita', 'Bienvenida.',
     'Welcome.',
     [(393, 'Bienvenida')], ''),
]

WALK = [
    (0, None, "'Darling, of course you're going to triumph.' Paquita opens with her signature term of endearment, literally \"fondness\", then pairs \"clear that\" with \"you are going to triumph\" to sound completely certain."),
    (1, None, "'Of course you're a star.' Repeating \"clear that\" hammers the encouragement home. Here Paquita uses permanent \"eres\" because being a star is who Mariona truly is."),
    (2, None, "'You'll do Velvet, Vis a vis, and El secreto de Puente Viejo.' Instead, of \"going to do\", Paquita steps up to the punchy one-word future \"you will do\" as she reels off three huge Spanish television hits of the era."),
    (3, None, "'I'll catch up with you later, Canelón. Let's go.' In Spain, the casual action word \"pillar\" means \"catch\" or \"nab\", so \"I'll catch you\" promises Fernando a future reckoning. \"Vámonos\" glues \"us\" onto \"we go\" for a brisk \"let's get out of here\"."),
    (4, None, "'Come on, marching out.' Originally used for soldiers or runway models parading in formation, this \"-ando\" word is a funny Spanish way to say \"move along\" with your head held high."),
    (5, None, "'Please don't touch me, sir.' Swapping \"her\" for \"me\" turns Magüi's earlier warning into \"don't touch me\". Adding polite \"señor\" at the end makes Paquita's brush-off extra icy."),
    (6, None, "'Don't touch her!' Backing her boss up on cue, Magüi fires the exact same three-word warning back at the staff member, swapping \"me\" back to \"la\" for Paquita."),
    (7, None, "'Everything is going great.' Literally \"all goes brilliant\", using \"goes\" just like English \"how's it going?\". In Spain, \"genial\" is a favourite everyday praise word meaning \"great\" or \"brilliant\", rather than \"friendly\"."),
    (8, None, "'Putting on a brave face comes very naturally to me.' The basic word \"disimular\" means hiding your real feelings and acting as if nothing happened. Around it, \"it gives itself very well to me\" is Spain's go-to idiom for being naturally good at any skill."),
    (9, None, "'If you like, I'll tell you I'm doing really well.' Notice unaccented \"si\" for \"if\", versus accented \"sí\" for \"yes\", followed by \"you want\" where English says \"if you like\". Present-tense \"I tell you\" naturally covers an immediate offer."),
    (10, None, "'Welcome.' Built from \"well\" and \"arrived\", Spanish \"welcome\" changes its ending to match whoever walks through the door. Ending in \"-a\" greets Mariona personally as the newest actress at PS Management."),
]
