# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 21
ID = 'die-discounter-s01e01-scene-21'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 21
TITLE = 'Der schöne Thorsten  (Handsome Thorsten)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'thorsten': 'Thorsten', 'fahri': 'Fahri'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Auto-caption Fari / Torsten / Markleiter restored to Fahri / Thorsten / Marktleiter.'

INTRO = (
    "When Jonas marches his 'shoplifter' into the office, Thorsten freezes: he actually knows Fahri from the old days! "
    "Putting on a big show of importance, Thorsten brags about being store manager over eight employees — then privately confesses to the camera that he cannot stand the guy. "
    "Listen to the German conversation first."
)
OPENER = "Let's walk through Fahri's teasing greeting, Thorsten's bragging, and a classic German proverb."
TRANSITION = "Now let's listen to the whole reunion scene again."
OUTRO = (
    "Smiling to Fahri's face while telling the documentary crew 'I hate him' — classic Thorsten! "
    "You now know how to ask who owns something, name a store manager, use the proverb 'all that glitters is not gold', and talk about stress and bad influence. "
    "Until next time!"
)
CLOSING = ('thorsten', 'Tschüss!')

STORY = [
    ('thorsten', 'Fahri! Was machst du denn hier?', 'Fahri! What on earth are you doing here?', [(679, 'Fari')], 'Restore spelling Fahri from auto-caption Fari.'),
    ('fahri', 'Der schöne Thorsten! Na, mein Lieber, arbeitest du etwa hier?', 'Handsome Thorsten! Well hello, my friend — do you work here or something?', [(683, 'Der schöne'), (685, 'Na, mein lieber'), (685, 'arbeitest'), (685, 'hier')], 'Capitalize nominalized mein Lieber.'),
    ('thorsten', 'Ja, klar, das hier ist mein Laden!', 'Yes, of course, this is my shop here!', [(687, 'Mein Laden hier')], ''),
    ('fahri', 'Wie, dein Laden? Gehört Kolinski jetzt dir?', 'What do you mean, your shop? Does Kolinski belong to you now?', [(689, 'Wie dein Laden'), (701, 'Kolinski, gehört dir')], ''),
    ('thorsten', 'Ich bin der Marktleiter! Ich habe acht Leute unter mir.', "I'm the store manager! I have eight people under me.", [(699, 'Acht Leute unter mir')], 'Restore Marktleiter from auto-caption Markleiter.'),
    ('thorsten', 'Nee, wir haben drei Filialen, und ich bin der Leiter hier in Altona.', "Nah, we have three branches, and I'm the manager here in Altona.", [(705, 'Nee, wir haben drei Filialen'), (707, 'Ich bin der Leiter'), (707, 'hier Altona')], ''),
    ('thorsten', 'Es ist nicht alles Gold, was glänzt. Ich habe schon viel Stress.', 'Not everything that glitters is gold. I do have a lot of stress.', [(713, 'es ist nicht alles'), (713, 'Gold'), (715, 'schon Stress')], 'Restore clean proverb Es ist nicht alles Gold, was glänzt.'),
    ('thorsten', 'Ganz ehrlich: Ich hasse ihn.', 'Quite honestly: I hate him.', [(719, 'Ich hasse ihn')], ''),
    ('thorsten', 'Er war schon immer ein schlechter Einfluss. Für Geld macht er alles.', 'He has always been a bad influence. He will do anything for money.', [(733, 'schlechter Einfluss'), (735, 'Für Geld macht er alles')], '')
]

WALK = [
    (0, None, "'Fahri! What on earth are you doing here?' Literally asking 'what make you then here?' is the classic surprised greeting you'll hear whenever friends bump into each other unexpectedly."),
    (1, None, "'Handsome Thorsten! Well hello, my friend — do you work here or something?' Calling someone 'my dear one' can be warm or playfully mocking. At the end, slipping in that little word for 'perhaps' or 'don't tell me' signals amused disbelief."),
    (3, None, "'What do you mean, your shop? Does Kolinski belong to you now?' Ownership in German very often uses the action word for 'belongs to' — literally 'belongs Kolinski now to-you?' rather than 'do you own it?'."),
    (4, None, "'I'm the store manager! I have eight people under me.' Look at the crisp job-title compound built from 'market' and 'leader' — the standard word on a German supermarket manager's name badge."),
    (6, None, "'Not everything that glitters is gold. I do have a lot of stress.' German shares the exact same proverb as English — word for word, 'it is not everything gold, what shines' — followed by the international word 'stress', capitalized like every German noun."),
    (7, None, "'Quite honestly: I hate him.' That handy phrase meaning 'quite honestly' sets up Thorsten's deadpan confession to the camera."),
    (8, None, "'He has always been a bad influence. He will do anything for money.' Look closely at the word for 'influence': it literally joins 'in' and 'flow', built on the exact same idea as English 'in-fluence'!")
]
