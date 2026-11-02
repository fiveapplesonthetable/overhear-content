# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 20
ID = 'die-discounter-s01e01-scene-20'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 20
TITLE = 'Das sind meine Nüsse  (Those Are My Nuts)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'jonas': 'Jonas', 'fahri': 'Fahri'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Auto-caption Wir haben die geklaut corrected to Sie haben die geklaut; z.B. expanded out for spoken clarity.'

INTRO = (
    "Minutes after asking actor Fahri for a selfie, overzealous security guard Jonas stops him at the exit over an open bag of nuts. "
    "Fahri insists he brought the nuts in with him, while Jonas solemnly explains his martial-arts 'throw roll' technique to the camera. "
    "Listen to the German scene first."
)
OPENER = "Let's unpack how Jonas escorts Fahri to the office and boasts about his security tactics."
TRANSITION = "Now let's hear the whole exit confrontation once more."
OUTRO = (
    "Poor Fahri goes from celebrity selfie guest to shoplifting suspect in under ten minutes, marched straight toward Thorsten's office. "
    "You have practised asking someone politely to step into an office, asking 'why?' in surprise, apologizing for forgetting something, and describing left and right. "
    "See you next time!"
)
CLOSING = ('jonas', 'Bis später!')

STORY = [
    ('fahri', 'Moment, wir haben doch eben schon ein Foto gemacht!', 'Hang on, we just took a photo together a moment ago!', [(639, 'haben eben schon Foto gemacht')], ''),
    ('jonas', 'Ja, genau. Ich muss Sie trotzdem bitten, kurz in mein Büro zu kommen.', 'Yes, exactly. Even so, I have to ask you to step into my office briefly.', [(641, 'Ja, genau. Ich muss'), (641, 'bitten, in'), (643, 'mein Büro zu kommen')], ''),
    ('fahri', 'Wieso denn? Was ist los? Das sind meine Nüsse!', 'Why on earth? What is going on? Those are my nuts!', [(646, 'Wieso'), (649, 'Das sind meine Nüsse')], ''),
    ('jonas', 'Nein, Sie haben die Nüsse hier im Laden geklaut.', 'No, you stole those nuts right here in the shop.', [(651, 'haben die geklaut')], 'Restore formal Sie from auto-caption Wir.'),
    ('fahri', 'Entschuldigung, das habe ich vergessen! Ich wollte die am Anfang zeigen.', 'Sorry, I forgot! I meant to show them at the beginning.', [(653, 'Entschuldigung, habe ich vergessen'), (655, 'am Anfang zeigen')], 'Simplify past modal subjunctive hätte zeigen müssen to A1 wollte zeigen.'),
    ('jonas', 'Ja, leider zu spät. Kommen Sie bitte mit.', 'Yes, unfortunately too late. Please come with me.', [(657, 'Ja'), (657, 'leider')], ''),
    ('jonas', 'In solchen Situationen lasse ich es gar nicht zur Flucht kommen.', 'In situations like this, I never let an escape happen in the first place.', [(661, 'in solchen Situationen lasse ich es'), (663, 'gar nicht zur Flucht kommen')], ''),
    ('jonas', 'Wenn er rechts oder links an mir vorbei will, packe ich ihn sofort am Arm.', 'If he tries to get past me on the right or left, I grab him straight by the arm.', [(667, 'rechts oder links'), (669, 'ihn am Arm packen')], ''),
    ('jonas', 'Dann mache ich zum Beispiel eine Wurfrolle, das geht ganz schnell.', 'Then I do a throw-and-roll, for example — it happens super fast.', [(675, 'eine Wurfrolle'), (677, 'Das geht ganz schnell')], 'Spell out z.B. as zum Beispiel.')
]

WALK = [
    (0, None, "'Hang on, we just took a photo together a moment ago!' That little four-letter time word in the middle means 'just a moment ago' — super handy whenever you refer back to something that happened minutes earlier."),
    (1, None, "'Yes, exactly. Even so, I have to ask you to step into my office briefly.' Notice how the everyday word for 'please' is also the action word meaning 'to ask someone politely to do something', paired here with the connector for 'even so'."),
    (2, None, "'Why on earth? What is going on? Those are my nuts!' Spoken German loves this casual question word for 'how come?' or 'why?', built from 'how' and 'so'. Follow it with 'what is loose?' and you have the everyday question for 'what's going on?'."),
    (3, None, "'No, you stole those nuts right here in the shop.' Jonas uses the colloquial everyday word for 'stole' or 'nicked' — you'll hear this word in conversation far more often than the formal police-report word for stealing."),
    (4, None, "'Sorry, I forgot! I meant to show them at the beginning.' Putting 'at the beginning' right before 'show' keeps the sentence clear: where English says 'I meant to show them', German simply says 'I wanted to show them'."),
    (7, None, "'If he tries to get past me on the right or left, I grab him straight by the arm.' Notice how German drops the motion word after 'wants': saying 'if he past me wants' naturally means 'if he wants to get past me', flanked by the words for 'right or left'."),
    (8, None, "'Then I do a throw-and-roll, for example — it happens super fast.' Two reusable chunks shine here: the two-word phrase for 'for example', and the closing four words literally meaning 'that goes quite fast'.")
]
