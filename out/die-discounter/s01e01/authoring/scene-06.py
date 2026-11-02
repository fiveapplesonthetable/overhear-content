# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 06
ID = 'die-discounter-s01e01-scene-06'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 6
TITLE = 'Dein Trinkgeld  (Your Tip)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'flora': 'Flora', 'titus': 'Titus'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Subjunctive aside simplified to clear A1 sentences; vulgar insult omitted at line 9 while preserving Flora\'s eye-rolling pressure.'

INTRO = (
    'As soon as Frau Buchholz walks away, Flora quietly slips two euros out of the cash drawer and offers the coin to Titus. '
    'Titus hesitates, baffled by Flora\'s creative theory of supermarket tipping. '
    'Listen to the German dialogue first.'
)
OPENER = "Let's look closely at how Flora justifies her 'tip' and nudges Titus to take the money."
TRANSITION = "Now let's listen to the whole tipping scene once more."
OUTRO = (
    "Reluctant Titus pockets the two-euro coin just to end the awkward moment at the till. "
    "You have heard useful everyday chunks for saying 'never again', handing something over with 'here you go', declining politely with 'all good', and asking 'seriously?'. "
    "See you next time!"
)
CLOSING = ('titus', 'Auf Wiedersehen!')

STORY = [
    ('flora', 'Und geh nicht wieder weg!', "And don't wander off again!", [(169, 'Und geh nicht wieder weg')], ''),
    ('titus', 'Nein, nie wieder.', 'No, never again.', [(171, 'Nie wieder')], ''),
    ('flora', 'Frau Buchholz gibt mir sicher gern zwei Euro.', 'Frau Buchholz is surely happy to give me two euros.', [(173, 'Frau Buchholz')], 'Recast hypothetical hätte gefragt / hätte safe ja gesagt into A1 present tense; spell out zwei Euro.'),
    ('flora', 'Ich habe mir nur genommen, was mir zusteht.', "I only took for myself what I'm entitled to.", [(177, 'habe ich mir'), (177, 'nur das genommen, was mir zusteht')], ''),
    ('flora', 'Die hassen uns, und wir hassen die.', 'They hate us, and we hate them.', [(179, 'Die hassen uns'), (179, 'Wir hassen die')], ''),
    ('flora', 'Und das ist dein Trinkgeld hier. Bitte schön!', 'And this here is your tip. Here you go!', [(181, 'und das ist dein Trinkgeld hier')], 'Write Bitte schön as two words per standard spelling.'),
    ('titus', 'Alles gut, ich brauche das nicht.', "It's all good, I don't need that.", [(183, 'Alles gut')], 'Complete Titus\'s cut-off protest cleanly.'),
    ('flora', 'Komm, nimm es doch an!', 'Come on, just take it!', [(185, 'nimm es an'), (189, 'Nimm es doch an')], 'Omit slang Alter and vulgarity from cue 191.'),
    ('titus', 'Echt jetzt? Na gut, Entschuldigung.', 'Seriously? Oh alright, sorry.', [(187, 'Echt')], 'Replace English loan Sorry in cue 193 with German Entschuldigung.')
]

WALK = [
    (0, None, "'And don't wander off again!' Here 'go' pairs up with the word for 'away' at the end of the clause to mean 'go away' or 'walk off'. Dropping 'not again' right in front of 'away' turns it into a punchy everyday warning."),
    (1, None, "'No, never again.' Those final two words — literally 'never again' — make one of the handiest short replies in spoken German, whether you are promising a colleague or swearing off a bad idea."),
    (3, None, "'I only took for myself what I'm entitled to.' Notice the little word for 'to me' used twice: first it shows she helped herself to the coins, and at the end it pairs with an action word that literally means 'stands to me' — belongs to me by right."),
    (4, None, "'They hate us, and we hate them.' Once again, spoken German uses the plural word for 'the' where English says 'they' and 'them'. Flipping the two halves around — 'they hate us, we hate them' — makes the contrast land sharply."),
    (5, None, "'And this here is your tip. Here you go!' The German word for a tip is a vivid compound built word for word from 'drink' and 'money' — originally a small coin for a drink. After it, 'please nicely' is what you'll hear whenever someone hands something over."),
    (6, None, "'It's all good, I don't need that.' That two-word opener meaning 'all good' is everywhere in modern Germany: you can say it to reassure someone, wave off an apology, or politely decline an offer."),
    (7, None, "'Come on, just take it!' Watch the vowel shift in the casual command form for 'take', while the separable partner 'on' at the end turns plain 'take' into 'accept'. Slipping that tiny word in the middle adds impatient insistence — 'just take it already!'"),
    (8, None, "'Seriously? Oh alright, sorry.' Pairing the word for 'genuine' or 'real' with 'now' gives the go-to casual reaction for 'seriously?' or 'for real?', followed by 'oh well, good' when Titus finally gives in.")
]
