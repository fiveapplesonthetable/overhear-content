ID = 'paquita-salas-s01e02-scene-11'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 2
SCENE = 11
TITLE = 'Mira esa chica  (Look at That Girl)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'magui': 'Magüi', 'mariona': 'Mariona'}
SOURCE_NAME = 'Paquita Salas S01E02: La actriz 360'
SOURCE_FILE = 'sources/paquita-salas/s01/e02.es.srt'
SOURCE_NOTE = 'Window 00:10:00,000–00:11:08,120.'
INTRO = ("As the showcase is about to start, Paquita tells Magüi how fond she still is of Fernando and admits her pre-show nerves. "
         "Then student actress Mariona steps onstage as Hedda Gabler and instantly catches Paquita's eye. "
         "Listen to the Spanish first.")
OPENER = "Let's hear each line again and unpack how it works."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard how Spanish expresses affection as 'having fondness', how stage dialogue switches to polite 'usted' commands, and how 'until to die' means 'to death'. See you next time.")
CLOSING = ('paquita', '¡Hasta la próxima!')

STORY = [
    ('paquita', 'Bueno, esto va a empezar.',
     'Right, this is about to start.',
     [(219, 'Bueno'), (219, 'esto va a empezar')],
     'Trimmed opening exclamation and connector que.'),
    ('paquita', 'Luego hablamos. Hasta luego.',
     "We'll talk later. See you later.",
     [(222, 'Luego hablamos'), (222, 'Hasta luego')],
     'Trimmed Hasta ahora and gracias.'),
    ('magui', 'Se ve que te tiene mucho cariño.',
     "You can tell he's very fond of you.",
     [(224, 'Se ve que te tiene mucho cariño')],
     'Trimmed confirmation tags.'),
    ('paquita', 'Es muy buen niño. Yo le quiero mucho.',
     "He's a very good lad. I love him very much.",
     [(225, 'Es muy buen niño. Yo le quiero mucho')],
     'Trimmed opening sí, sí, sí.'),
    ('magui', 'Qué nervios.',
     'What nerves.',
     [(228, 'Qué nervios')], ''),
    ('paquita', 'Muchos nervios. ¿Y ellos cómo tienen que estar?',
     'Such nerves. And how nervous must they be?',
     [(229, 'Muchos nervios. ¿Y ellos cómo tienen que estar?')], ''),
    ('mariona', '¡Ay! Cállese usted ya, se lo ruego.',
     'Oh! Be quiet now, I beg you.',
     [(235, '¡Ay! Cállese usted ya, se lo ruego')], ''),
    ('mariona', 'Mi destino está claramente trazado.',
     'My destiny is clearly mapped out.',
     [(236, 'mi destino está claramente trazado')],
     'Trimmed opening clause to keep sentence focused.'),
    ('mariona', '¿Quiere usted saberlo?',
     'Do you want to know what it is?',
     [(237, '¿Quiere usted saberlo?')], ''),
    ('paquita', 'Mira esa chica.',
     'Look at that girl.',
     [(238, 'Mira esa chica')],
     'Extracted whispered aside.'),
    ('mariona', 'Aburrirme hasta morir.',
     'Boring myself to death.',
     [(239, 'Aburrirme hasta morir')],
     'Trimmed repeated opening words.')
]

WALK = [
    (0, None, """'Right, this is about to start.' Opening with the term "good" works like English "well" or "right" when wrapping up a chat. Then "goes to start" expresses something about to happen any second."""),
    (1, None, """'We'll talk later. See you later.' Present-tense "later we talk" is Spain's natural everyday promise to catch up soon, without needing a future form. Notice the same word "later" returning after "until" in "see you later"."""),
    (2, None, """'You can tell he's very fond of you.' Literally, "itself sees that", that neat two-word opener means "it's obvious that" or "you can tell". After it, Spanish says "he has much fondness for you"."""),
    (3, None, """'He's a very good lad. I love him very much.' Placed right before "boy", the masculine word "good" drops its final "-o" to become a crisp single syllable. Calling a grown former assistant a "good boy" shows Paquita's motherly warmth."""),
    (4, None, """'What nerves.' Two quick words — literally "what nerves" — are how Spaniards confess butterflies before an exam, a match, or curtain-up."""),
    (5, None, """'Such nerves. And how nervous must they be?' Here "have to be" doesn't express a rule or duty — it wonders aloud "imagine how they must be feeling!". Spanish uses "be" for temporary feelings like stage fright."""),
    (6, None, """'Oh! Be quiet now, I beg you.' On stage in a classic period play, Mariona switches to formal "usted" commands, attaching "yourself" onto "be quiet". At the end, "to you it I beg" stacks two tiny words right before "beg"."""),
    (7, None, """'My destiny is clearly mapped out.' Adding the "-mente" ending to the feminine form of "clear" works just like adding "-ly" in English "clearly". The final word literally means "traced" or "drawn" like a line on a map."""),
    (8, None, """'Do you want to know what it is?' Again, formal "usted" sits right after "wants" for polite theatrical distance. At the end, "it" glues straight onto "to know" to make one smooth word."""),
    (9, None, """'Look at that girl.' Unlike English "look at", the Spanish command for "look" takes no extra term "at" before "that girl". Notice the feminine form of "that" matching "girl"."""),
    (10, None, """'Boring myself to death.' Adding "myself" onto "to bore" means getting bored rather than boring someone else. Literally, "until to die", those final two words match English "to death".""")
]
