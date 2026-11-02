# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 13
ID = 'die-discounter-s01e01-scene-13'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 13
TITLE = 'Die Zahlen sehen schlecht aus  (The Numbers Look Bad)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'thorsten': 'Thorsten', 'beyza': 'Beyza'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Retains the rapid comedic back-and-forth over Die Zahlen sehen nicht so gut aus and Thorsten calling Pina to rescue him.'

INTRO = (
    "Sitting across from Thorsten in the branch office, Beyza opens the store ledger and gets straight to the point: the numbers do not look good. "
    "Thorsten stalls with nervous questions until he gives up and calls deputy manager Pina over the intercom. "
    "Listen to the German exchange first."
)
OPENER = "Let's unpack Beyza's blunt assessment and all the everyday ways Thorsten asks 'what do you mean by that?'"
TRANSITION = "Now let's listen to the whole office confrontation again."
OUTRO = (
    "Whenever a real business question lands on his desk, Thorsten hits the intercom button for Pina. "
    "You have practised saying how things look, asking what someone means, asking what something is supposed to mean, and calling a colleague into an office. "
    "Until next time!"
)
CLOSING = ('thorsten', 'Bis später!')

STORY = [
    ('thorsten', 'So, schön, dass du da bist!', "Right then, lovely that you're here!", [(397, 'So, schön, dass du da bist')], ''),
    ('beyza', 'Die Zahlen sehen ja nicht so gut aus, oder?', "The numbers don't look so good, do they?", [(399, 'Die Zahlen sehen ja nicht so gut aus')], 'Replace northern tag ne? with standard universal tag oder?.'),
    ('thorsten', 'Wie meinst du das jetzt?', 'What do you mean by that now?', [(403, 'Wie meinst du'), (403, 'jetzt')], 'Supply object das for complete A1 phrasing.'),
    ('beyza', 'Wie meine ich das? Also, die Zahlen sehen nicht so gut aus.', "What do I mean? Well, the numbers don't look so good.", [(405, 'wie meine ich'), (407, 'Also, die Zahlen sehen nicht so gut aus')], ''),
    ('thorsten', 'Ja, aber was heißt das genau?', 'Yes, right, what does that mean exactly?', [(409, 'Was heißt das')], ''),
    ('beyza', 'Was heißt das wohl? Die Zahlen sind einfach schlecht.', 'What do you think it means? The numbers are simply bad.', [(411, 'Was heißt'), (413, 'Zahlen')], 'Distil Beyza\'s incredulous echo into crisp A1 German.'),
    ('thorsten', 'Ja, ich weiß, aber was soll das sozusagen heißen?', 'Yes, I know, only what is that supposed to mean, so to speak?', [(413, 'Ja, ich weiß aber'), (415, 'was soll das heißen sozusagen')], ''),
    ('thorsten', 'Moment, wo ist eigentlich Pina?', 'Hang on, where is Pina actually?', [(417, 'Wo ist Pina')], ''),
    ('thorsten', 'Pina, bitte sofort in mein Büro!', 'Pina, to my office right away, please!', [(421, 'Pina bitte. Mein Büro')], '')
]

WALK = [
    (1, None, "'The numbers don't look so good, do they?' Saying something 'looks good' or 'not so good' uses a split-apart expression built from 'see' and 'out' at the end. Tacking the word for 'or?' onto the close turns any statement into 'don't they?' or 'right?'."),
    (2, None, "'What do you mean by that now?' Watch how English 'what do you mean?' starts with the word for 'how' rather than 'what' in German — literally 'how mean you that now?'. That single swap will make your questions sound instantly natural."),
    (4, None, "'Yes, right, what does that mean exactly?' When asking what a word, sign, or remark means, German reaches for the same action word used to state a name — literally 'what is that called exactly?'."),
    (5, None, "'What do you think it means? The numbers are simply bad.' Slipping that little middle word in after 'what means that' adds dry irony — 'what do you suppose it means?' — before Beyza spells it out with the plain word for 'simply'."),
    (6, None, "'Yes, I know, only what is that supposed to mean, so to speak?' Pairing 'should' with 'mean' at the end creates a classic reusable chunk: 'what is that supposed to mean?', padded out with Thorsten's nervous 'so to speak'."),
    (8, None, "'Pina, to my office right away, please!' Announcements over a shop loudspeaker often drop the action word completely: literally 'into my office' says everything needed in three brisk words.")
]
