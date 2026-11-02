ID = 'paquita-salas-s01e01-scene-01'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = "Soy representante  (I'm an Agent)"
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E01: Casada con esto'
SOURCE_FILE = 'sources/paquita-salas/s01/e01.es.srt'
SOURCE_NOTE = ('Native Spanish captions from episode stream 4. Opening window 00:00:05,760–00:01:17,520.')
INTRO = ("Paquita Salas is a comedy about a Spanish talent agent and her small agency in Madrid. "
         "Her assistant Magüi praises her, and Paquita confidently explains the business, until she asks whether her star client Macarena has called. "
         "Listen to the Spanish first, then we'll go through it together.")
OPENER = "Let's start with how Paquita introduces herself."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard one word used both for years in business and for representing an actress. "
         "You also heard how Spanish asks whether a phone call has happened, then makes the same statement negative. See you next time.")
CLOSING = ('paquita', '¡Hasta pronto!')

STORY = [
    ('paquita', 'Hola, soy Paquita Salas y soy representante.',
     "Hello, I'm Paquita Salas, and I'm an agent.",
     [(1, 'Hola, soy Paquita Salas'), (1, 'y soy representante')], ''),
    ('magui', 'Paquita es un crack.',
     'Paquita is brilliant.', [(6, 'Paquita es'), (6, '"crack"')],
     'Removed hesitation and subtitle quotation marks.'),
    ('magui', 'Todo el mundo quiere a Paquita muchísimo.',
     'Everyone loves Paquita very much.', [(7, 'Todo el mundo quiere'), (7, 'a Paquita muchísimo')],
     'Omitted the separate opening praise and trailing conversational tag.'),
    ('paquita', 'Está mal que yo lo diga, pero a mí todo el mundo me adora.',
     "I shouldn't say it myself, but everyone adores me.",
     [(8, 'Está mal que yo lo diga')],
     'Restored singular todo el mundo me adora from audio.'),
    ('paquita', 'Llevamos más de veinticinco años.',
     "We've been in business for more than twenty-five years.",
     [(15, 'Llevamos más de'), (15, 'años')],
     'Spelled out the numeral 25.'),
    ('paquita', 'Empezamos como agencia de modelos.',
     'We started out as a modelling agency.', [(15, 'Empezamos'), (15, 'agencia de modelos')],
     'Used como for the initial role.'),
    ('paquita', 'Poco a poco hemos ido creciendo.',
     "Little by little, we've grown.", [(16, 'poco a poco'), (16, 'creciendo')],
     'Omitted the trailing clause.'),
    ('paquita', 'Somos expertos en generar éxito.',
     "We're experts at creating success.", [(18, 'Somos expertos en generar éxito')], ''),
    ('paquita', 'Ahora mismo llevamos a Macarena García.',
     'At the moment, we represent Macarena García.',
     [(20, 'Ahora mismo llevamos'), (20, 'a Macarena García')], ''),
    ('paquita', '¿Ha llamado Maca?',
     'Has Maca called?', [(22, '¿ha llamado Maca?')],
     'Omitted hesitation and vocative.'),
    ('paquita', 'No, Maca no ha llamado.',
     "No, Maca hasn't called.", [(23, 'No, Maca no ha llamado')],
     'Omitted unfinished complaint.'),
    ('paquita', 'Actuar es un oficio.',
     'Acting is a profession.', [(24, 'Actuar'), (25, 'es un oficio')],
     'Joined sentence across two cues.'),
    ('paquita', 'Tratamos de trabajar con gente que tiene esto muy claro.',
     'We try to work with people who understand that very clearly.',
     [(26, 'Tratamos de trabajar'), (26, 'con gente que tiene esto muy claro')],
     'Omitted the profane second clause.')
]

WALK = [
    (0, None, "'Hello, I'm Paquita Salas, and I'm an agent.' The same form of am introduces both her name and her job. There is no word for an before agent here: in a simple job description like this, Spanish usually leaves it out."),
    (1, None, "'Paquita is brilliant.' The borrowed word describes someone exceptionally good at something. The word for a before it is masculine here, although she is talking about a woman. This praise word can be used that way; it does not refer to a break or a crack in an object."),
    (2, None, "'Everyone loves Paquita very much.' Everyone is literally all the world, so the verb is singular. The little word before Paquita marks a person as the object of loves. It does not mean that the love is moving towards her."),
    (3, None, "'I shouldn't say it myself, but everyone adores me.' The opening literally says it is bad that I say it. The short word for it points to the boast that follows. Me is emphasized once at the beginning of the boast, and another me still sits just before adores. This doubling puts the spotlight on Paquita herself."),
    (4, None, "'We've been in business for more than twenty-five years.' Spanish uses a present-tense verb with the length of time to say how long something has continued. More than introduces the number; it does not mean exactly twenty-five."),
    (5, None, "'We started out as a modelling agency.' Started describes a completed event, while the word for as introduces their original role. Notice how models is plural after of, literally agency of models."),
    (6, None, "'Little by little, we've grown.' The repeated word for little makes the phrase mean gradually. The rest literally says we have gone growing, a handy way to show steady progress up to now."),
    (7, None, "'We're experts at creating success.' The word for experts has an ending meaning more than one, to match we. After experts at, Spanish uses the basic form meaning to create. The final word means success, rather than an exit from a building."),
    (8, None, "'At the moment, we represent Macarena García.' Earlier, this same word introduced the years they have been in business. Here it means represent or manage a client. The little word before Macarena marks the person they represent, and right now means at the present time."),
    (9, None, "'Has Maca called?' Here Maca is short for Macarena. Has plus called asks whether the phone call has happened, and there is no separate word for she because the name at the end tells us who Paquita means."),
    (10, None, "'No, Maca hasn't called.' The first no is the standalone answer, while the second sits right before has called to make the statement negative. Called keeps the same masculine ending here even though Maca is a woman."),
    (11, None, "'Acting is a profession.' The basic form meaning to act names the activity itself, where English uses acting. Unlike the earlier job description about herself, this sentence includes the word for a before profession."),
    (12, None, "'We try to work with people who understand that very clearly.' Try followed by a small linking word and to work describes an attempt. People is singular in Spanish, so the form after who is singular too, and literally says has this very clear.")
]
