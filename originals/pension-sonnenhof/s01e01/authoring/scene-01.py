# Authoring module for pension-sonnenhof-s01e01-scene-01.
ID = 'pension-sonnenhof-s01e01-scene-01'
SHOW = 'pension-sonnenhof'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Die Klinke anheben  (Lift the Handle)'
LEVEL = 'A1 — beginner'
PAIR = 'de-en'
LABELS = {'klara': 'Klara', 'werner': 'Werner'}
SOURCE_NAME = 'Overhear Original'
INTRO = 'Klara arrives early for her very first morning at the Pension Sonnenhof guesthouse in Leipzig. Behind the front desk, veteran handyman Werner is already pouring strong tea. Listen to the scene first without worrying about catching every word.'
OPENER = "Now let's walk through the conversation one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Klara is inside, the eight brass keys are on the board, and her first morning has begun. Don't worry if a few words went past quickly; they come back all week. See you next time."
CLOSING = ('klara', 'Bis bald!')
STORY = [
    ('klara', 'Guten Morgen! Entschuldigung, ist die Tür zu?', 'Good morning! Excuse me, is the door locked?'),
    ('werner', 'Guten Morgen. Nein, heb zuerst die Klinke hoch und drück.', 'Good morning. No, lift the handle first, then push.'),
    ('klara', 'Oh, sie geht auf! Danke. Ich bin Klara, neu an der Rezeption.', 'Oh, it opens! Thank you. I am Klara, new at the front desk.'),
    ('werner', 'Ich bin Werner. Du bist zehn Minuten zu früh.', 'I am Werner. You are ten minutes early.'),
    ('klara', 'Am ersten Tag gehe ich immer schnell. Wo ist der Computer?', 'On my first day I always walk fast. Where is the computer?'),
    ('werner', 'In der Schublade. Hier nutzen wir dieses große Buch aus Papier.', 'In the drawer. Here we use this big paper book.'),
    ('klara', 'Ein Buch aus Papier? Wirklich?', 'A paper book? Really?'),
    ('werner', 'Papier verliert bei Regen nie die Zimmerliste.', 'Paper never loses the room list when it rains.'),
    ('klara', 'Guter Punkt! Und das hier sind die Schlüssel?', 'Fair point! And these here are the keys?'),
    ('werner', 'Ja, acht Zimmer, acht Messingschlüssel. Zimmer vier kommt heute.', 'Yes, eight rooms, eight brass keys. Room four arrives today.'),
    ('klara', 'Super. Sag mir bitte alles Wichtige.', 'Great. Tell me everything important, please.'),
    ('werner', 'Regel eins: Trink zuerst heißen Tee, dann geh an die Klingel.', 'Rule one: drink hot tea first, then answer the bell.'),
]
WALK = [
    (0, None, ["'Good morning! Excuse me, is the door locked?' Klara starts politely at the entrance. Listen to the tiny word at the very end:", (None, 'zu'), "In German, that everyday word for 'to' also means closed or shut."]),
    (1, None, "'Good morning. No, lift the handle first, then push.' Werner switches straight to friendly, informal commands for a new colleague, dropping the polite ending right from the start."),
    (2, None, ["'Oh, it opens! Thank you. I am Klara, new at the front desk.' Watch how German expresses 'opens' by splitting one action in two:", (None, 'geht auf'), "Word for word, the door 'goes open'."]),
    (3, None, ["'I am Werner. You are ten minutes early.' Here that same little word returns with a second job:", (None, 'zu früh'), "Before a describing word like 'early', it means 'too', so ten minutes early is literally 'too early'."]),
    (4, None, "'On my first day I always walk fast. Where is the computer?' When a German sentence begins with a time phrase like 'on the first day', the action word stays in second place, so Klara says 'walk I' rather than 'I walk'."),
    (5, None, ["'In the drawer. Here we use this big paper book.' Notice the compound word for drawer:", (None, 'Schublade'), "It combines 'push' and 'box', naming a box you slide in and out."]),
    (6, None, "'A paper book? Really?' German says 'a book out of paper' rather than stacking the two words the English way. The final questioning word is your go-to one-word check whenever something surprises you."),
    (7, None, ["'Paper never loses the room list when it rains.' German loves snapping two words together into one neat label:", (None, 'Zimmerliste'), "It simply glues 'room' and 'list' side by side."]),
    (8, None, "'Fair point! And these here are the keys?' Literally she says 'good point', a natural two-word agreement you can use in any workplace conversation."),
    (9, None, ["'Yes, eight rooms, eight brass keys. Room four arrives today.' Another crisp compound appears here:", (None, 'Messingschlüssel'), "German joins 'brass' and 'key' into a single word, and the plural looks identical to the singular."]),
    (10, None, "'Great. Tell me please everything important.' After 'everything', German turns the word 'important' into a standalone thing, meaning 'all that is important'."),
    (11, None, "'Rule one: drink hot tea first, then answer the bell.' Literally Werner tells her to 'go to the bell', the natural everyday way to say 'answer the bell' at a desk or front door."),
]
