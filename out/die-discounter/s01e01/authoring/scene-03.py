# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 03
ID = 'die-discounter-s01e01-scene-03'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 3
TITLE = 'Sabine kommt heute  (Sabine Is Coming Today)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'pina': 'Pina', 'thorsten': 'Thorsten', 'wilhelm': 'Wilhelm'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Colloquial contractions (war\'n, woll) expanded into clean spoken German for A1 learners.'

INTRO = (
    'Thorsten hangs up the office phone looking pale. '
    'Company owner Sabine Kolinski wants to drop by the Altona store today, and when Thorsten hurries out into the aisles, nobody is working except older employee Wilhelm. '
    'Just listen to the German scene first.'
)
OPENER = "Let's unpack Thorsten's panic and the everyday questions you can use when looking for people."
TRANSITION = "Now let's listen to the whole aisle scene once more."
OUTRO = (
    "Every single employee except Wilhelm is outside taking a break while the boss is on her way. "
    "You have heard how to ask who just called, talk about someone dropping by, compare things, and ask where everyone has gone. "
    "Until next time!"
)
CLOSING = ('pina', 'Bis bald!')

STORY = [
    ('pina', 'Okay, wer war denn das?', 'Okay, who was that then?', [(43, 'Okay')], 'Auto-caption writes Wer waren das for contracted spoken Wer war\'n das (Wer war denn das?).'),
    ('thorsten', 'Das war Sabine Kolinski, die Chefin der drei Filialen hier.', 'That was Sabine Kolinski, the boss of the three branches here.', [(47, 'Sabine Kolinski'), (47, 'Chefin der drei'), (47, 'Filialen hier')], 'Trim redundant Inhaberin und to keep a clean A1 apposition.'),
    ('thorsten', 'Sie will heute noch mal vorbeigucken.', 'She wants to drop by again today.', [(49, 'noch mal vorbeigucken')], 'Expand clipped colloquial Woll to Sie will heute.'),
    ('thorsten', 'Sabine Kolinski ist wie eine Spinne.', 'Sabine Kolinski is like a spider.', [(53, 'ist wie eine Spinne')], 'Fix auto-caption spelling Kulinski to Kolinski.'),
    ('thorsten', 'Aber sie hat noch mehr Angst vor uns als wir vor ihr.', 'Though she is even more afraid of us than we are of her.', [(57, 'mehr Angst vor'), (57, 'als')], 'Clarify Thorsten\'s tangled spider proverb into clean A1 German.'),
    ('thorsten', 'Bin ich hier eigentlich der Einzige im Laden?', 'Am I actually the only one in the shop here?', [(61, 'Bin ich hier eigentlich der einzige im Laden')], 'Capitalize nominalized der Einzige per standard orthography.'),
    ('thorsten', 'Wo sind denn hier eigentlich alle?', 'Where is everybody around here, anyway?', [(63, 'Wo sind denn hier eigentlich alle')], ''),
    ('thorsten', 'Wilhelm, wo sind denn alle?', 'Wilhelm, where is everyone?', [(65, 'Wilhelm, wo sind denn'), (65, 'alle')], 'Drop repeated eigentlich for natural rhythm.'),
    ('wilhelm', 'Die sind alle draußen und machen Pause.', 'They are all outside taking a break.', [(67, 'sind draußen')], 'Recast Draußen rauchen as draußen und machen Pause for clean A1 workplace vocabulary.')
]

WALK = [
    (0, None, "'Okay, who was that then?' Pina's short question starts with the question word for 'who', followed straightaway by 'was'. Slipping that little middle softener in before 'that' makes the question sound curious and conversational rather than abrupt."),
    (1, None, "'That was Sabine Kolinski, the boss of the three branches here.' Notice the feminine ending on the word for female boss — German adds that two-letter suffix to many job titles when talking about a woman. The word for store branches is what you'll see on supermarket chains across Germany."),
    (2, None, "'She wants to drop by again today.' The compound at the end joins 'past' and 'look' to mean 'drop by for a quick look', a casual Northern favourite. Pairing the two little words before it gives the handy chunk for 'one more time' or 'again'."),
    (3, None, "'Sabine Kolinski is like a spider.' Comparing two things is wonderfully direct: the same small word that asks 'how?' also means 'like' in comparisons. You can use that exact bridge whenever you say one person or thing is like another."),
    (4, None, "'Though she is even more afraid of us than we are of her.' Where English says 'to be afraid', German literally says 'to have fear' followed by the preposition for 'in front of'. Thorsten botches the old saying about spiders to pretend he isn't terrified of his boss."),
    (5, None, "'Am I actually the only one in the shop here?' Putting the verb first turns the statement into a yes-or-no question. Notice how 'in the shop' squeezes two words into one contraction, and 'actually' adds a note of exasperated disbelief."),
    (6, None, "'Where is everybody around here, anyway?' Where English treats 'everybody' as singular — 'where is everybody?' — German treats the word for 'all' as plural, pairing it with 'are'. Stacking two little flavour words in the middle makes his frustration unmistakable."),
    (8, None, "'They are all outside taking a break.' In casual speech, German speakers constantly use the plural word for 'the' as an everyday stand-in for 'they'. At the end, 'making pause' is the standard workplace expression for taking a break.")
]
