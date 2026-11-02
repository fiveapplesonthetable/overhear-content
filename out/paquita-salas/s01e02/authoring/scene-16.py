ID = 'paquita-salas-s01e02-scene-16'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 16
TITLE = 'Paquita no está loca  (Paquita Is Not Crazy)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'magui': 'Magüi', 'fernando': 'Fernando', 'paquita': 'Paquita'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Window 00:15:41,480–00:16:30,680 (cues 329–348).'
INTRO = (
    'Standing up in front of the whole auditorium, loyal assistant Magüi defends Paquita against Fernando\'s coldness and explains why Macarena is still on their website. '
    'When they are ordered out of the hall, Paquita refuses to leave on anyone else\'s terms. '
    'Listen to the Spanish first.'
)
OPENER = "Let's hear how Magüi stands up for Paquita."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = (
    'You heard how Spanish expresses "have just done", says "maybe" with a three-word chunk, and softens commands or protests when tensions flare. '
    'See you next time.'
)
CLOSING = ('magui', '¡Adiós!')

STORY = [
    ('magui', 'Perdonad un momento. Quiero decir que Paquita no está loca.',
     "Excuse me a moment. I want to say that Paquita isn't crazy.",
     [(329, 'Perdonad un momento'), (329, 'quiero decir que Paquita no está loca')],
     'Trimmed spoken connector Que yo.'),
    ('magui', 'Lo que tú acabas de hacer no se hace.',
     "What you've just done isn't done.",
     [(330, 'lo que tú acabas de hacer'), (330, 'no se hace')],
     'Joined the two clauses of cue 330 cleanly.'),
    ('fernando', 'Yo no sé quién eres, pero sabes muy poquito de este oficio.',
     "I don't know who you are, but you know very little about this profession.",
     [(331, 'Yo no sé quién eres'), (332, 'pero'), (332, 'muy poquito de este oficio')],
     'Simplified demuestras saber to sabes.'),
    ('magui', 'A lo mejor no sé mucho de esta profesión, pero sé cómo funcionan las personas.',
     "Maybe I don't know much about this profession, but I know how people work.",
     [(335, 'a lo mejor'), (335, 'no sé mucho'), (335, 'esta profesión'), (336, 'pero sé cómo funcionan las personas')],
     'Simplified cómo funciona esta profesión to de esta profesión and omitted coarse cue 337.'),
    ('fernando', 'No tengo la culpa de que me vayan bien las cosas.',
     "It isn't my fault that things are going well for me.",
     [(340, 'no tengo la culpa'), (341, 'de que me vayan bien las cosas')],
     'Joined across cues 340 and 341.'),
    ('fernando', 'Macarena vino a verme porque tú te estás quedando antigua.',
     "Macarena came to see me because you're getting outdated.",
     [(341, 'Macarena vino a verme'), (342, 'porque tú te estás quedando antigua')],
     'Trimmed middle clause para que la representara.'),
    ('fernando', 'A ver si la quitas de la web.',
     'See if you can take her off the website.',
     [(343, 'a ver si la quitas de la web')],
     'Omitted harsh opening clause.'),
    ('magui', 'La página web la llevo yo.',
     'I run the website myself.',
     [(344, 'la página web'), (344, 'la llevo yo')],
     'Unified la web and la página web into one clean clause.'),
    ('magui', 'No me ha dado tiempo todavía a quitarla.',
     "I haven't had time to take her off yet.",
     [(345, 'no me ha dado tiempo todavía a quitarla')],
     'Trimmed opening A lo mejor and trailing tag.'),
    ('magui', '¡No la toques!',
     "Don't touch her!",
     [(346, '¡No la toques!')], ''),
    ('paquita', 'Claro que vamos a abandonar la sala, pero no porque lo digas tú.',
     "Of course we're going to leave the hall, just not because you say so.",
     [(347, 'vamos a abandonar la sala'), (347, 'claro que'), (348, 'pero no'), (348, 'porque lo digas tú')],
     'Condensed cues 347 and 348 and omitted coarse cue 349.'),
]

WALK = [
    (0, None, "'Excuse me a moment. I want to say that Paquita isn't crazy.' Magüi echoes Fernando's plural \"forgive\" to address the room, then answers his \"madness\" jab directly. Using the state word \"está\" before \"crazy\" treats it as how Paquita is acting right now."),
    (1, None, "'What you've just done isn't done.' Combining \"finish\" with \"of\" and an action expresses \"have just done\" in everyday Spanish. At the end, literally \"does not make itself\" is how Spaniards say something is bad form."),
    (2, None, "'I don't know who you are, but you know very little about this profession.' Notice the irregular first-person \"sé\" for \"I know\", written with an accent to distinguish it from \"se\". Shrinking \"little\" with a diminutive ending makes Fernando's put-down sound patronisingly small."),
    (3, None, "'Maybe I don't know much about this profession, but I know how people work.' Spain's favourite conversational chunk for \"maybe\" literally says \"at the best\". Both \"who\" in the last line and \"how\" here carry written accents whenever they ask an indirect question."),
    (4, None, "'It isn't my fault that things are going well for me.' Where English says \"it isn't my fault\", Spanish says \"I don't have the blame\". Notice how \"things go well to me\" puts \"things\" at the very end as the subject."),
    (5, None, "'Macarena came to see me because you're getting outdated.' Here \"me\" attaches smoothly to \"to see\" as one word. Pairing \"staying\" with \"ancient\" or \"old-fashioned\" builds the stinging phrase \"falling behind the times\"."),
    (6, None, "'See if you can take her off the website.' Starting with \"let's see if\" plus the plain present is a classic Spanish way to prod someone into doing something. \"La\" stands for Macarena, and \"the web\" is universal shorthand for an agency website."),
    (7, None, "'I run the website myself.' Earlier \"llevar\" meant representing an actress; here the exact same word means running or managing a webpage. Putting \"the webpage\" first and \"I\" dead last shoulders all the blame away from Paquita."),
    (8, None, "'I haven't had time to take her off yet.' Instead, of \"I haven't had time\", Spanish idiomatically says \"it hasn't given me time yet\". At the end, \"her\" hooks straight onto \"to remove\" as a single word."),
    (9, None, "'Don't touch her!' In a negative command to \"tú\", the \"-ar\" ending flips to \"-es\", and spelling changes \"c\" to \"qu\" so the hard \"k\" sound stays intact. Unlike affirmative commands, \"her\" sits in front rather than attached to the end."),
    (10, None, "'Of course we're going to leave the hall, just not because you say so.' Opening with \"clear that\" gives an emphatic \"of course\". After \"not because\", Spanish switches \"you say\" to \"digas\" because Paquita is rejecting his order as the reason they are leaving."),
]
