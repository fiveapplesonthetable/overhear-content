# Authoring module for pension-sonnenhof-s01e03-scene-07.
ID = 'pension-sonnenhof-s01e03-scene-07'
SHOW = 'pension-sonnenhof'
SEASON = 1
EPISODE = 3
SCENE = 7
TITLE = 'Das Notizheft zurückbringen  (Returning the Notebook)'
LEVEL = 'A1 — beginner'
PAIR = 'de-en'
LABELS = {'klara': 'Klara', 'lukas': 'Lukas'}
SOURCE_NAME = 'Overhear Original'
INTRO = "Klara climbs up to the attic door to return Lukas's forgotten leather notebook, trying hard to act normal despite thinking he is a secret hotel inspector. Listen first."
OPENER = "Now let's listen to their upstairs exchange line by line."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = 'Lukas got his notebook back without suspecting a thing, yet that cooling radiator is a warning sign. One final scene in Episode 3, down to the cellar! See you next time.'
CLOSING = ('lukas', 'Bis morgen!')
STORY = [
    ('klara', 'Entschuldigung, Herr Lukas? Ich hoffe, ich störe Sie nicht.', 'Excuse me, Mr Lukas? I hope I am not disturbing you.'),
    ('lukas', 'Oh, mein Lederheft! Vielen Dank! Ich habe es gerade schon gesucht.', 'Oh, my leather notebook! Many thanks! I was just looking for it.'),
    ('klara', 'Sie haben es unten neben der Suppentasse liegen lassen.', 'You left it lying downstairs beside the soup cup.'),
    ('lukas', 'Alle meine Straßennotizen von dieser Woche stehen darin. Sie retten mich.', 'All my street notes from this week are in it. You are saving me.'),
    ('klara', 'Wir freuen uns, dass unser Hof ruhig genug für Ihre... Arbeit ist.', 'We are glad that our courtyard is quiet enough for your... work.'),
    ('lukas', 'Sehr ruhig! Aber haben Sie gerade ein metallisches Klopfen gehört?', 'Very quiet! Though did you just hear a metallic knocking?'),
    ('klara', 'Ja! Es klang wie das Heizungsrohr dort in der Ecke.', 'Yes! It sounded like the heating pipe there in the corner.'),
    ('lukas', 'Fühlen Sie mal am Heizkörper: Oben ist er warm, unten wird er schon kühl.', 'Feel the radiator: at the top it is warm, at the bottom it is turning cool.'),
    ('klara', 'Oh! Manchmal haben alte Rohre abends eine kleine Luftblase.', 'Oh! Sometimes old pipes have a little air bubble in the evening.'),
    ('lukas', 'Ich habe eine warme Decke, mir geht es heute Nacht bestens.', 'I have a warm blanket, I am completely fine tonight.'),
    ('klara', 'Danke für Ihre Geduld! Werner prüft sofort unten den Keller.', 'Thank you for your patience! Werner will check the cellar downstairs right away.'),
    ('lukas', 'Schönen Abend noch, Klara. Bis morgen beim Frühstück.', 'Have a nice evening, Klara. See you tomorrow at breakfast.'),
]
WALK = [
    (0, None, ["'Excuse me, Mr Lukas? I hope I am not disturbing you.' Polite doorway opener:", (None, 'ich störe Sie nicht.'), 'Use it whenever you knock on an office or guest-room door.']),
    (1, None, "'Oh, my leather notebook! Many thanks! I was just looking for it.' In German, slipping 'just already' into 'I have searched' means 'I was just looking for it'."),
    (2, None, ["'You left it lying downstairs beside the soup cup.' Notice the natural double-action pair at the end:", (None, 'liegen lassen.'), "Literally 'let lie', how German says you forgot something on a table."]),
    (3, None, "'All my street notes from this week are in it. You are saving me.' In German, written notes literally 'stand' inside a notebook."),
    (4, None, "'We are glad that our courtyard is quiet enough for your... work.' Notice how the word for 'enough' sits after 'quiet', matching English order."),
    (5, None, "'Very quiet! Though did you just hear a metallic knocking?' In German, writing 'knock' with a capital letter turns the sound itself into 'a knocking'."),
    (6, None, ["'Yes! It sounded like the heating pipe there in the corner.' Clear household compound:", (None, 'Heizungsrohr'), 'Heating plus pipe names the radiator pipe in the corner.']),
    (7, None, ["'Feel the radiator: at the top it is warm, at the bottom it is turning cool.' Look at the literal build of 'radiator':", (None, 'Heizkörper:'), "Word for word, a radiator is a 'heating-body'."]),
    (8, None, ["'Oh! Sometimes old pipes have a little air bubble in the evening.' Look at the transparent compound at the close:", (None, 'Luftblase.'), 'Air plus bubble gives you an air bubble in the pipe.']),
    (9, None, ["'I have a warm blanket, I am completely fine tonight.' Warm idiomatic reassurance:", (None, 'mir geht es'), "Literally 'to me goes it', followed by 'best of all' for 'I am completely fine'."]),
    (10, None, ["'Thank you for your patience! Werner will check the cellar downstairs right away.' A lovely everyday quality word:", (None, 'Geduld!'), 'It means patience—handy whenever someone waits kindly.']),
    (11, None, ["'Have a nice evening, Klara. See you tomorrow at breakfast.' Notice that friendly little trailing word:", (None, 'Schönen Abend noch'), "Tucking 'still' after 'nice evening' wishes someone a pleasant rest of the evening."]),
]
