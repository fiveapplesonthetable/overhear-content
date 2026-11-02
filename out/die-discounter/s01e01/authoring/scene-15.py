# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 15
ID = 'die-discounter-s01e01-scene-15'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 15
TITLE = 'Deck die Kamera ab  (Cover the Camera)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'peter': 'Peter', 'titus': 'Titus'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = '15000 € spelled out as fünfzehntausend Euro; colloquial vors Regal and keinen Bock preserved.'

INTRO = (
    "In one of the grocery aisles, Peter recruits reluctant newcomer Titus for another questionable task: standing in front of a high shelf to block the new security camera while Peter pockets snacks. "
    "Titus protests that he is still in his trial week, while Peter complains about the fifteen thousand euros Thorsten supposedly got to install the cameras. "
    "Listen to the German conversation first."
)
OPENER = "Let's walk through Peter's sneaky instructions and Titus's very relatable trial-week protest."
TRANSITION = "Now let's listen to the whole camera-blocking scene again."
OUTRO = (
    "Wait — fifteen thousand euros for cameras? Hold onto that detail, because it is about to blow up in Thorsten's office. "
    "You have practised telling someone where to stand, saying 'pretend that...', saying you really don't feel like doing something, and talking about how long something has been there. "
    "Until next time!"
)
CLOSING = ('titus', 'Tschüss!')

STORY = [
    ('peter', 'Stell dich mal vors Regal und deck die Kamera ab.', 'Go stand in front of the shelf and block the camera.', [(440, 'Stell dich mal vors Regal'), (441, 'und deck'), (441, 'die Kamera ab')], ''),
    ('peter', 'Tu einfach so, als ob wir hier etwas sortieren.', 'Just pretend we are sorting something here.', [(441, 'Tu'), (441, 'so als'), (443, 'irgendwas da sortieren')], 'Supply ob in als ob for clean A1 structure.'),
    ('titus', 'Peter, ich habe echt keinen Bock in meiner ersten Woche.', "Peter, I really don't feel like doing this in my first week.", [(447, 'Peter, ich habe'), (447, 'echt keinen Bock in meiner ersten Woche')], ''),
    ('peter', 'Komm schon, mach das jetzt einfach!', 'Come on, just do it now!', [(449, 'mach das jetzt')], ''),
    ('titus', 'Ich bin in meiner Probewoche! Ich habe keinen Bock, jetzt zu fliegen.', "I'm in my trial week! I don't feel like getting fired right now.", [(451, 'meiner Probewoche. Ich habe keinen'), (453, 'Bock jetzt zu fliegen')], ''),
    ('peter', 'Seit zwei Wochen sind hier überall neue Kameras.', 'For the past two weeks there have been new cameras everywhere here.', [(465, 'Seit zwei Wochen sind'), (465, 'neue Kameras')], 'Restore überall from auto-caption truncation über.'),
    ('peter', 'Dafür hat Thorsten fünfzehntausend Euro bekommen.', 'Thorsten got fifteen thousand euros for that.', [(467, 'für bekommen')], 'Spell out 15000 € as fünfzehntausend Euro and restore Thorsten.'),
    ('peter', 'Seitdem kann ich hier nichts mehr mitnehmen. Ist sie jetzt abgedeckt?', "Since then I haven't been able to pocket anything here. Is it covered now?", [(469, 'seitdem kann ich hier nicht'), (475, 'ist sie abgedeckt'), (477, 'jetzt')], 'Simplify idiom mitgehen lassen to clear A1 mitnehmen.'),
    ('titus', 'Ja, jetzt ist sie abgedeckt. Okay.', 'Yes, it is covered now. Okay.', [(479, 'Ja'), (481, 'Okay')], '')
]

WALK = [
    (0, None, "'Go stand in front of the shelf and block the camera.' Literally, Peter says 'place yourself before-the shelf', squeezing 'before' and 'the' into one punchy spoken contraction. Then 'cover' pairs with 'off' at the end to mean blocking a view."),
    (1, None, "'Just pretend we are sorting something here.' Where English uses one word for 'pretend', German literally says 'do simply so, as whether...' and sends the word for 'sorting' to the end of the clause."),
    (2, None, "'Peter, I really don't feel like doing this in my first week.' Having 'no billy-goat' is the most famous casual idiom in Germany for 'I really can't be bothered' or 'I'm not up for it' — casual with friends, though not one for a job interview!"),
    (4, None, "'I'm in my trial week! I don't feel like getting fired right now.' Look at the neat workplace compound joining 'trial' and 'week'. At the close, the everyday word for 'to fly' doubles in casual speech as 'to get kicked out' or 'be fired'."),
    (5, None, "'For the past two weeks there have been new cameras everywhere here.' Unlike English, which reaches for 'have been', German pairs the word for 'since' with the simple present whenever something started in the past and is still happening right now."),
    (6, None, "'Thorsten got fifteen thousand euros for that.' Watch out for a classic false friend: the German action word that sounds like English 'become' actually means 'to get' or 'to receive' — never 'become'!"),
    (7, None, "'Since then I haven't been able to pocket anything here. Is it covered now?' The word for 'since then' is built from 'since' and 'then', while 'take with' at the end is Peter's shameless euphemism for pocketing store stock.")
]
