# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 05
ID = 'die-discounter-s01e01-scene-05'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 5
TITLE = 'An Kasse zwei  (At Checkout Two)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'flora': 'Flora', 'titus': 'Titus'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Numbers spelled out in German words for TTS clarity; customer small talk and checkout prompts retained.'

INTRO = (
    'At checkout two, Flora sits nervous newcomer Titus down for some rapid-fire on-the-job training. '
    'Between pressing the wrong buttons and calling shoppers over, Titus watches Flora charm regular customer Frau Buchholz. '
    'Listen through the German exchange first.'
)
OPENER = "Let's break down the checkout phrases, polite customer forms, and small talk you'll hear in any German supermarket."
TRANSITION = "Now let's listen to the whole checkout lesson again."
OUTRO = (
    "Titus survives his very first customer at the till, and Flora makes him promise to stay put. "
    "You can now invite shoppers to a free checkout, ask politely how someone is doing, say you need a holiday, and name a price at the till. "
    "Until next time!"
)
CLOSING = ('flora', 'Schönen Tag noch!')

STORY = [
    ('flora', 'Okay, jetzt mach mal die Kasse auf.', 'Okay, now open up the till.', [(125, 'Okay, jetzt mach mal die Kasse auf')], ''),
    ('titus', 'Okay, die Kasse ist offen.', 'Okay, the checkout is open.', [(127, 'Okay, die Kasse ist offen')], ''),
    ('flora', 'Trau dich ruhig ein bisschen mehr! Mach ein bisschen lauter.', "Go on, be a bit bolder! Speak a little louder.", [(129, 'Trau dich ruhig ein bisschen mehr'), (131, 'mach ein bisschen lauter')], ''),
    ('titus', 'Sie können gerne zur Kasse zwei kommen! Die ist jetzt frei.', 'You are welcome to come to checkout two! It is free now.', [(135, 'Sie können'), (135, 'gerne zur Kasse'), (135, 'kommen. Die ist jetzt frei')], 'Spell out 2 as zwei and drop filler auch.'),
    ('flora', 'Hallo Frau Buchholz, wie geht es Ihnen? Ich habe Sie lange nicht gesehen.', "Hello Frau Buchholz, how are you? I haven't seen you in a long time.", [(137, 'Hallo Frau'), (139, 'lange nicht'), (139, 'gesehen')], 'Restore standard Buchholz and wie geht es Ihnen from auto-caption Bucholz / ihn.'),
    ('flora', 'Ich brauche auch mal wieder ein bisschen Urlaub.', 'I could really use a bit of a holiday again too.', [(149, 'Ich brauche auch mal wieder ein bisschen Urlaub')], ''),
    ('flora', 'Schneller unten draufdrücken, das habe ich dir gerade gezeigt.', 'Press down at the bottom faster — I just showed you that.', [(153, 'Schneller unten'), (155, 'gerade gezeigt')], 'Join draufdrücken as one compound verb and supply dir.'),
    ('titus', 'Siebenunddreißig Euro fünfzig, bitte. Vielen Dank!', 'Thirty-seven euros fifty, please. Many thanks!', [(159, 'bitte. Danke')], 'Spell out 37,50 in spoken German currency order.'),
    ('titus', 'Ja, ich bleibe jetzt auch hier.', 'Yes, I am staying right here now too.', [(165, 'Ja, ich bleibe jetzt auch'), (163, 'hier')], '')
]

WALK = [
    (0, None, "'Okay, now open up the till.' German builds 'open up' by pairing the everyday action word for 'make' with the word for 'on' or 'open' at the very end. Notice too that the word for cash register covers both the till drawer itself and the whole checkout lane."),
    (2, None, "'Go on, be a bit bolder! Speak a little louder.' Literally, Flora tells him 'dare yourself calmly a bit more' — here the word for 'calmly' acts as a warm encourager meaning 'feel free to' or 'don't hold back'. Then 'make a bit louder' is casual shorthand for speaking up."),
    (3, None, "'You are welcome to come to checkout two! It is free now.' Addressing shoppers calls for the polite 'you', and slipping in the word for 'gladly' is how German says 'you're welcome to'. In the second sentence, 'the' stands in for the feminine checkout lane — 'she is free now'."),
    (4, None, "'Hello Frau Buchholz, how are you? I haven't seen you in a long time.' Word for word, the polite greeting asks 'how goes it to you?', using the formal indirect form of 'you'. Follow that with 'long not seen' and you have a warm, reusable line for any familiar face."),
    (5, None, "'I could really use a bit of a holiday again too.' The plain action word here means 'need', softened by a cluster of small conversational words meaning 'once again a little bit'. In German, the word for holiday specifically means time off work rather than a public bank holiday."),
    (7, None, "'Thirty-seven euros fifty, please. Many thanks!' Listen to how two-digit numbers flip around in German: thirty-seven is spoken literally as 'seven-and-thirty'. At the till, the currency word sits neatly between the whole euros and the cents, never taking a plural ending."),
    (8, None, "'Yes, I am staying right here now too.' Reassuring Flora takes plain everyday words: 'I stay now also here'. Unlike English, German uses the simple present for 'I'm staying right now' without needing an extra '-ing' form.")
]
