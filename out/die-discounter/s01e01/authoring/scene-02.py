# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 02
ID = 'die-discounter-s01e01-scene-02'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 2
TITLE = 'Die Obstbestellung  (The Fruit Order)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'pina': 'Pina', 'thorsten': 'Thorsten'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Native German automatic captions checked against episode context; Kerob corrected to Kernobst and Kraus Apparat restored to Kruse am Apparat.'

INTRO = (
    'Inside the Hamburg supermarket Feinkost Kolinski, deputy manager Pina updates branch boss Thorsten on the fruit order before the weekend rush. '
    'Just as she brings up last week\'s delivery trouble, the office phone interrupts them. '
    'Listen to the German conversation first without worrying about catching every detail.'
)
OPENER = "Let's walk through Pina's fruit order and see how workplace updates and polite suggestions sound in everyday German."
TRANSITION = "Now let's hear the whole office exchange again from start to finish."
OUTRO = (
    "Thorsten grabs the ringing phone before Pina can finish explaining the delivery mix-up. "
    "You now have handy ways to update a colleague, suggest a bigger order for the weekend, talk about half of something selling, and answer a work phone. "
    "See you next time!"
)
CLOSING = ('pina', 'Bis später!')

STORY = [
    ('pina', 'Ich halte dich kurz auf dem Laufenden, was wir bestellt haben.', 'Let me quickly keep you posted on what we ordered.', [(7, 'halte kurz auf dem'), (7, 'bestellt haben')], 'Expand clipped opening and restore Laufenden from auto-caption Laufen.'),
    ('pina', 'Wir haben Erdbeeren und Bananen bestellt.', 'We ordered strawberries and bananas.', [(9, 'Erdbeeren'), (9, 'bestellt, Bananen')], 'Drop specific crate counts to keep the opening list crisp for beginners.'),
    ('pina', 'Das Wochenende kommt, und die Leute gehen an den Strand.', 'The weekend is coming, and people are going to the beach.', [(13, 'Das Wochenende kommt. Die Leute gehen')], 'Restore full article den in an den Strand from spoken contraction an Strand.'),
    ('pina', 'Wollen wir bei den Wassermelonen die doppelte Menge bestellen?', 'Shall we order double the amount of watermelons?', [(11, 'bei den Wassermelonen'), (17, 'doppelte Menge bestellen')], 'Recast Was hältst du davon, wenn wir... into direct A1 Wollen wir...? suggestion.'),
    ('thorsten', 'Eigentlich geht doch Kernobst gerade gut.', 'Actually, pome fruit is selling well right now, isn\'t it?', [(21, 'Eigentlich'), (21, 'geht doch'), (21, 'gerade gut')], 'Auto-caption mishears Kernobst (apples and pears) as Kerob.'),
    ('pina', 'Nee, eigentlich gerade nicht so, das haben wir letzte Woche gesehen.', 'Nah, not really right now — we saw that last week.', [(23, 'Nee, eigentlich gerade nicht so'), (25, 'haben wir letzte Woche gesehen')], ''),
    ('pina', 'Da haben wir nur die Hälfte verkauft.', 'We only sold half of it then.', [(27, 'nur die Hälfte verkauft')], 'Recast passive wurde verkauft into active haben wir verkauft for A1 clarity.'),
    ('pina', 'Übrigens gab es letzte Woche ein bisschen Lieferprobleme.', 'By the way, there were some delivery problems last week.', [(35, 'Übrigens letzte Woche'), (37, 'Lieferprobleme')], 'Trim Kommunikationsprobleme oder and omit preceding swear word.'),
    ('thorsten', 'Kruse am Apparat!', 'Kruse speaking!', [(39, 'Apparat')], 'Auto-caption writes Kraus Apparat for Thorsten Kruse answering the office phone.')
]

WALK = [
    (0, None, "'Let me quickly keep you posted on what we ordered.' Pina opens with a lively workplace idiom that literally pictures holding someone on the running track so they stay up to speed. Adding the little word for briefly makes the update sound brisk and considerate."),
    (1, None, "'We ordered strawberries and bananas.' Notice how German wraps the past action around the middle of the sentence: the helper comes second, while the word for ordered waits right at the end. Both fruit names are transparent compounds or international cousins that are easy to spot."),
    (2, None, "'The weekend is coming, and people are going to the beach.' The word for weekend joins week and end into one neat block, just like English. At the close, going to the beach uses the preposition for onto the edge of the water rather than the plain word for to."),
    (3, None, "'Shall we order double the amount of watermelons?' Starting a question with this modal action word is the everyday way to say 'shall we' when making a team suggestion. The word for watermelons is built word for word from water and melons, and the final action word again lands cleanly at the end."),
    (4, None, "'Actually, pome fruit is selling well right now, isn't it?' Thorsten reaches for a supermarket trade compound meaning seeded orchard fruit like apples and pears. Notice how the everyday verb for 'goes' doubles here as 'sells', while the little middle particle nudges Pina to agree."),
    (5, None, "'Nah, not really right now — we saw that last week.' That casual northern word for 'nah' is softer and more relaxed than a textbook 'no' among coworkers. She softens her pushback further with a handy chunk meaning 'not really right now' before backing it up with last week's results."),
    (7, None, "'By the way, there were some delivery problems last week.' The opening transition word is what you can say whenever a side topic pops into your head. Because it takes the first slot, 'there was' flips its order right behind it, leading into the compound word for delivery problems."),
    (8, None, "'Kruse speaking!' On a German landline, people often give their surname followed by 'at the apparatus' — meaning at the telephone set. Swap in your own last name and you have a classic, slightly old-school way to pick up an office phone.")
]
