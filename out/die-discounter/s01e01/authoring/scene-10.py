# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 10
ID = 'die-discounter-s01e01-scene-10'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 10
TITLE = 'Die Tür vom Kühlraum  (The Cold-Room Door)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'peter': 'Peter', 'titus': 'Titus'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Profanities in cues 305 and 355 omitted per quality spec; Lightwolf restored to Leitwolf.'

INTRO = (
    "Back in the stockroom, self-styled alpha male Peter gives Titus his own dubious tour of the store rules and the walk-in cold room. "
    "Peter warns that a cardboard pizza box must always prop the heavy door open — and instantly panics when they step inside and realize the box is gone. "
    "Listen to the German scene first."
)
OPENER = "Let's unpack Peter's stockroom tour, his boastful 'lead wolf' speech, and the cold-room door panic."
TRANSITION = "Now let's listen to the whole cold-room scene again."
OUTRO = (
    "False alarm or not, Titus quickly learns that Peter's grand 'lead wolf' act crumbles the second a heavy door clicks shut. "
    "You have heard how to talk about important rules, name parts of a workplace, explain why you do something with 'so that', and react when something goes missing. "
    "Until next time!"
)
CLOSING = ('titus', 'Tschüss!')

STORY = [
    ('peter', 'Was die anderen alle sagen, das kannst du vergessen.', 'Whatever all the others say, you can forget about that.', [(299, 'was die anderen alle sagen, das'), (301, 'kannst du'), (301, 'vergessen')], ''),
    ('peter', 'Es gibt hier nur eine wichtige Regel: Hör darauf, was ich sage.', 'There is only one important rule here: listen to what I say.', [(305, 'nur eine wichtige Regel'), (309, 'Hör darauf, was ich sage')], 'Combine cues 305 and 309 while omitting the profanity in cue 305.'),
    ('peter', 'Respektiere mich, und dann ist alles gut.', 'Respect me, and then everything is fine.', [(311, 'Respektiere mich und dann ist alles')], 'Replace English loan cool with German gut.'),
    ('peter', 'Ich bin hier im Laden sozusagen der Leitwolf.', 'In this shop I am the alpha wolf, so to speak.', [(315, 'bin ich sozusagen der')], 'Correct auto-caption Lightwolf to German Leitwolf.'),
    ('peter', 'Also, das ist das Lager, und das hier ist der Kühlraum.', 'So, that is the stockroom, and this here is the cold room.', [(321, 'das ist das Lager'), (325, 'Das ist der Kühlraum')], ''),
    ('titus', 'Okay, alles klar.', 'Okay, got it.', [(327, 'Okay')], 'Expand single-word Okay into natural two-beat acknowledgment.'),
    ('peter', 'Mach mal die Tür auf, damit du verstehst, wie das geht.', 'Open the door so that you understand how it works.', [(331, 'die Tür auf, damit du'), (333, 'verstehst, wie das geht')], ''),
    ('peter', 'Zwischen die Tür und die Wand muss immer eine Packung, sonst entsteht Druck.', 'A box always has to go between the door and the wall, otherwise pressure builds up.', [(337, 'zwischen die Tür und die'), (339, 'die Wand'), (343, 'entsteht'), (343, 'Druck')], 'Condense rambling vacuum explanation into one clear A1 cause-and-effect sentence.'),
    ('peter', 'Moment, wo ist die Pizza? Du musst die Packung wieder reinpacken!', 'Wait, where is the pizza? You have to wedge the box back in!', [(351, 'wo ist die Pizza'), (353, 'du musst die'), (353, 'wieder reinpacken')], 'Replace slang Diger with Moment and omit cue 355 profanity.')
]

WALK = [
    (0, None, "'Whatever all the others say, you can forget about that.' Notice the idiomatic punch of the closing phrase: literally 'that can you forget', a handy chunk whenever you mean 'forget about it' or 'ignore all that'."),
    (1, None, "'There is only one important rule here: listen to what I say.' After the colon, the word for 'thereto' points forward to the clause 'what I say' — a neat two-step link you'll hear whenever listening, waiting, or hoping connects to a whole idea."),
    (3, None, "'In this shop I am the alpha wolf, so to speak.' Peter's favourite filler literally joins 'so to say' into one smooth word meaning 'so to speak'. His boastful title compounds 'lead' and 'wolf' for the leader of the pack."),
    (4, None, "'So, that is the stockroom, and this here is the cold room.' Look at how transparent workplace compounds are: the word for the walk-in fridge is built from 'cool' and 'room' glued into one noun."),
    (5, None, "'Okay, got it.' Pairing 'all' with 'clear' is one of the most useful two-word responses in German — you'll hear it constantly for 'got it', 'makes sense', or 'sounds good'."),
    (6, None, "'Open the door so that you understand how it works.' After 'open the door', the linking word means 'so that', sending 'understand' to the end of its clause. Then the closing three words literally say 'how that goes', the standard way to say 'how it works'."),
    (8, None, "'Wait, where is the pizza? You have to wedge the box back in!' Panic hits in two short beats: a direct 'where is...?' question, followed by 'must' near the front and a compound action word meaning 'pack back inside' right at the end.")
]
