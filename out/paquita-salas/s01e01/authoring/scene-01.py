ID = 'paquita-salas-s01e01-scene-01'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = "Soy representante  (I'm an Agent — Taster)"
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi'}
SOURCE_NAME = 'Paquita Salas S01E01: Casada con esto'
SOURCE_FILE = 'sources/paquita-salas/s01/e01.es.srt'
SOURCE_NOTE = ('Native Spanish captions extracted directly from original episode stream 4, tagged spa. '
               'No English backtranslation. Opening source window 00:00:05,760–00:01:17,520; '
               'speaker identities checked against actual footage and the Magüi Moreno lower-third. '
               'See SOURCE-REVIEW.json for independent audio-check status and exact adaptation decisions.')
INTRO = ("Paquita Salas is a comedy about a Spanish talent agent and her small agency. "
         "Her assistant praises her, and Paquita confidently explains the business, until she asks whether her star client has called. "
         "Listen to the Spanish first, then we'll go through it together.")
OPENER = "Let's start with how Paquita introduces herself."
TRANSITION = "Now listen to the whole scene again."
OUTRO = ("You heard one word used both for years in business and for representing an actress. "
         "You also heard how Spanish asks whether a phone call has happened, then makes the same statement negative. See you next time.")
CLOSING = ('paquita', '¡Hasta pronto!')

STORY = [
    ('paquita', 'Hola, soy Paquita Salas y soy representante.',
     "Hello, I'm Paquita Salas, and I'm an agent.",
     [(1, 'Hola, soy Paquita Salas'), (1, 'y soy representante')], ''),
    ('magui', 'Paquita es un crack.',
     "Paquita is brilliant.", [(6, 'Paquita es'), (6, '"crack"')],
     'Removed the hesitation and subtitle quotation marks. Independent small and production reference ASR both hear un crack; the authored caption has una. This learner line follows the corroborated source-audio article without claiming a human listening certificate.'),
    ('magui', 'Todo el mundo quiere a Paquita muchísimo.',
     'Everyone loves Paquita very much.', [(7, 'Todo el mundo quiere'), (7, 'a Paquita muchísimo')],
     'Omitted the separate opening praise and the trailing conversational aside.'),
    ('paquita', 'Está mal que yo lo diga, pero a mí todo el mundo me adora.',
     "I shouldn't say it myself, but everyone adores me.",
     [(8, 'Está mal que yo lo diga')],
     'Restored a mí todo el mundo me adora from actual source audio and independent unprompted ASR; the caption condenses this to plural todos me adoran. Omitted the hesitation tag. Learner grammar now follows the source-audio wording.'),
    ('paquita', 'Llevamos más de veinticinco años.',
     "We've been in business for more than twenty-five years.",
     [(15, 'Llevamos más de'), (15, 'años')],
     'Spelled out the caption numeral 25 for native speech; the duration refers to the agency introduced in the surrounding source.'),
    ('paquita', 'Empezamos como agencia de modelos.',
     'We started out as a modelling agency.', [(15, 'Empezamos'), (15, 'agencia de modelos')],
     'Restored como from independent small and production-reference ASR of the actual audio; the authored caption has de. The meaning is unchanged: the business started as a modelling agency.'),
    ('paquita', 'Poco a poco hemos ido creciendo.',
     "Little by little, we've grown.", [(16, 'poco a poco'), (16, 'creciendo')],
     'Restored hemos ido creciendo from the actual source-audio check; the caption compresses this to fuimos creciendo. Omitted the following clause about earning the industry\'s trust.'),
    ('paquita', 'Somos expertos en generar éxito.',
     "We're experts at creating success.", [(18, 'Somos expertos en generar éxito')], ''),
    ('paquita', 'Ahora mismo llevamos a Macarena García.',
     'At the moment, we represent Macarena García.',
     [(20, 'Ahora mismo llevamos'), (20, 'a Macarena García')], ''),
    ('paquita', '¿Ha llamado Maca?',
     'Has Maca called?', [(22, '¿ha llamado Maca?')],
     'Removed the opening hesitation and optional vocative Magüi. Three synthesized takes did not independently verify the name realization, so the beginner adaptation omits that address without changing who asks or the question about Maca. Maca is the familiar short name for Macarena García, not another client.'),
    ('paquita', 'No, Maca no ha llamado.',
     "No, Maca hasn't called.", [(23, 'No, Maca no ha llamado')],
     'Retained the complete answer; omitted the following unfinished complaint. The source shot shows Paquita turning back towards the camera.'),
    ('paquita', 'Actuar es un oficio.',
     'Acting is a profession.', [(24, 'Actuar'), (25, 'es un oficio')],
     'Joined one sentence split across two caption cues; removed caption quotation marks.'),
    ('paquita', 'Tratamos de trabajar con gente que tiene esto muy claro.',
     'We try to work with people who understand that very clearly.',
     [(26, 'Tratamos de trabajar'), (26, 'con gente que tiene esto muy claro')],
     'The demonstrative points back to acting being a profession. Authored native captions and the independent large-model source check agree on esto; the small decoder\'s eso was rejected. Omitted the next, profane clause rather than rewriting its content.')
]

WALK = [
    (0, None, "'Hello, I'm Paquita Salas, and I'm an agent.' The same form of am introduces both her name and her job. There is no word for an before agent here: in a simple job description like this, Spanish usually leaves it out."),
    (1, None, "'Paquita is brilliant.' The borrowed word describes someone exceptionally good at something. The word for a before it is masculine here, although she is talking about a woman. This praise word can be used that way; it does not refer to a break or a crack in an object."),
    (2, None, "'Everyone loves Paquita very much.' Everyone is literally all the world, so the verb is singular. The little word before Paquita marks a person as the object of loves. It does not mean that the love is moving towards her."),
    (3, None, "'I shouldn't say it myself, but everyone adores me.' The opening literally says it is bad that I say it. The short word for it points to the boast that follows. Me is emphasized once at the beginning of the boast, and another me still sits just before adores. This doubling puts the spotlight on Paquita herself."),
    (4, None, "'We've been in business for more than twenty-five years.' Spanish uses a present-tense verb with the length of time to say how long something has continued. More than introduces the number; it does not mean exactly twenty-five."),
    (5, None, "'We started out as a modelling agency.' Started describes a completed event. This particular we form is also used for we start. Her story about the agency's beginning tells us that she means the past."),
    (6, None, "'Little by little, we've grown.' The repeated word for little makes the phrase mean gradually. The rest literally says we have gone growing. Spanish uses that pattern for gradual progress up to now."),
    (7, None, "'We're experts at creating success.' The word for experts has an ending meaning more than one, to match we. After experts at, Spanish uses the basic form meaning to create. The final word means success, rather than an exit from a building."),
    (8, None, "'At the moment, we represent Macarena García.' Earlier, this same word introduced the years they have been in business. Here it means represent or manage a client. The little word before Macarena marks the person they represent, and now means at the present time."),
    (9, None, "'Has Maca called?' She uses a short name for Macarena. Has plus called asks whether the call has happened. There is no separate word for she: the name at the end tells us who she is asking about."),
    (10, None, "'No, Maca hasn't called.' The first no is the answer. The second makes the statement negative and sits before has called. Called keeps the same ending here; it does not change to a feminine form because Maca is a woman."),
    (11, None, "'Acting is a profession.' The unconjugated form meaning to act names the activity itself. English uses acting here. Unlike the earlier job description about herself, this sentence includes a word for a before profession."),
    (12, None, "'We try to work with people who understand that very clearly.' Try followed by a small linking word and to work describes an attempt. People is grammatically singular in this Spanish sentence, so the verb after who is singular too. That points back to acting being a profession.")
]
