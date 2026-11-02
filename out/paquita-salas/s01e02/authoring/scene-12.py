ID = 'paquita-salas-s01e02-scene-12'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 12
TITLE = 'Es ella  (We Found Her)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi', 'director': 'Director'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Window 00:11:25,520–00:12:40,720.'
INTRO = ("As the play ends to loud applause, Paquita leaps to her feet cheering that Mariona is the all-round actress they have been searching for. "
         "Then the school director steps out to invite a VIP guest from the front row up onto the stage: Fernando Canelón. "
         "Listen to the scene first.")
OPENER = "Let's go through the applause and the director's speech."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how Spanish builds big praise words like 'tremendous play', how 'put myself of foot' means 'stand up', and why 'Primera Fila' puns on sitting in the front row. See you in the next scene.")
CLOSING = ('paquita', '¡Buenas noches!')

STORY = [
    ('paquita', '¡Bravo!',
     'Bravo!',
     [(244, '¡Bravo!')], ''),
    ('paquita', '¡Ay, que la tenemos! Es ella.',
     "Oh, we've found her! She's the one.",
     [(246, 'que la tenemos'), (246, 'es ella')],
     'Trimmed repeated interjections and connector es que.'),
    ('magui', 'Tiene tres sesenta.',
     'She has the full three-sixty.',
     [(247, 'Tiene')],
     'Spelled out the numeral 360.'),
    ('paquita', 'Qué obrón ha hecho. Me voy a poner de pie.',
     "What a tremendous play she's put on. I'm going to stand up.",
     [(248, 'qué obrón ha hecho'), (249, 'Me voy a poner de pie')],
     'Joined across two cues and trimmed repetition.'),
    ('paquita', 'Qué elegancia. ¡Guapa!',
     'Such elegance. Gorgeous!',
     [(250, 'Qué elegancia'), (251, '¡Guapa!')],
     'Joined across two cues.'),
    ('director', 'Muchas gracias a vosotros, chicos.',
     'Many thanks to all of you, everyone.',
     [(255, 'Muchas gracias'), (256, 'a vosotros, chicos')],
     'Joined across two cues and omitted sobre todo.'),
    ('director', 'Enhorabuena, estoy emocionadísimo.',
     "Congratulations, I'm deeply moved.",
     [(256, 'Enhorabuena, estoy emocionadísimo')], ''),
    ('director', 'Quería invitar al escenario a una persona muy importante.',
     'I wanted to invite a very important person onto the stage.',
     [(257, 'Quería invitar al escenario a una persona muy importante')], ''),
    ('director', 'Hoy terminan su trayectoria aquí en la escuela Primera Fila.',
     'Today they finish their journey here at the Primera Fila school.',
     [(259, 'hoy terminan'), (260, 'su trayectoria'), (260, 'aquí, en la escuela Primera Fila')],
     'Omitted brillantísima and joined across two cues.'),
    ('director', 'Además, está en primera fila.',
     "What's more, he's in the front row.",
     [(261, 'Además, está en primera fila')], ''),
    ('director', 'Por favor, Fernando Canelón, de la agencia Red Carpet. Bienvenido.',
     'Please welcome Fernando Canelón, from the Red Carpet agency. Welcome.',
     [(261, 'Por favor, Fernando Canelón'), (262, 'de la agencia Red Carpet. Bienvenido')],
     'Joined across two cues.')
]

WALK = [
    (0, None, """'Bravo!' Theatre audiences across Spain shout this classic Italian loanword to cheer a great performance."""),
    (1, None, """'Oh, we've found her! She's the one.' Slipping the little word "that" before "we have her" adds excited punch in spoken Spanish, like "oh, we really have her!". Then two crisp words — literally "is she" — mean "she's the one"."""),
    (2, None, """'She has the full three-sixty.' Instead, of saying "she is", Magüi says "she has three sixty", treating complete all-round talent as something an actress possesses."""),
    (3, None, """'What a tremendous play she's put on. I'm going to stand up.' Adding the big "-ón" ending to the term "play" supersizes it into "a powerhouse performance". In the second sentence, "put myself of foot" is the everyday Spanish chunk for standing up."""),
    (4, None, """'Such elegance. Gorgeous!' Shouting the feminine word "pretty" or "gorgeous" from your seat is a classic, affectionate theatre cheer in Spain — right alongside "bravo!"."""),
    (5, None, """'Many thanks to all of you, everyone.' Notice Spain's informal plural word "you all", which speakers in Madrid use constantly with groups of friends or students. At the end, the masculine plural for "youngsters" addresses a mixed group of men and women."""),
    (6, None, """'Congratulations, I'm deeply moved.' That warm single word "congratulations" is built from "in good hour". And beware a classic false friend: the word after "I am" usually means "touched" or "moved" with emotion rather than hyper."""),
    (7, None, """'I wanted to invite a very important person onto the stage.' Saying "I wanted to invite" sounds softer and more polite than a blunt "I want". Next comes "al", which merges "to" and masculine "the" before "stage", followed by personal "a" before "a person"."""),
    (8, None, """'Today they finish their journey here at the Primera Fila school.' The Spanish word "trajectory" is an everyday way to talk about someone's training path or career journey. Notice how present-tense "they finish" marks a milestone happening today."""),
    (9, None, """'What's more, he's in the front row.' Opening with a handy connector for "besides" or "what's more", the director makes a dad joke on the school's name: lowercase "primera fila" literally means sitting in the "front row"."""),
    (10, None, """'Please welcome Fernando Canelón, from the Red Carpet agency. Welcome.' Literally, "well come", the closing word changes its ending to match who arrives — masculine "-o" here for Fernando, or "-a" for a woman.""")
]
