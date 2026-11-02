# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 14
ID = 'die-discounter-s01e01-scene-14'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 14
TITLE = 'Ein cooler Roller  (A Cool Scooter)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'kunde': 'Der Kunde', 'pina': 'Pina'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Includes raw rolling cue 437 reaction as Pina test-rides the customer\'s electric scooter.'

INTRO = (
    "Back in the aisle, Pina brings the shopper a plastic trolley token after Wilhelm frees his stuck house key. "
    "Spotting the customer's sleek electric scooter, Pina admires it and immediately gets invited to take a quick spin right between the supermarket shelves. "
    "Listen to the German conversation first."
)
OPENER = "Let's unpack their friendly exchange and the simple instructions for riding an electric scooter."
TRANSITION = "Now let's hear the whole scooter scene once more."
OUTRO = (
    "Pina glides happily down the aisle on the electric scooter just before Thorsten's office summons catches up with her. "
    "You now know how to compliment someone's ride, ask if someone feels like trying a turn, and give quick button-and-push instructions. "
    "See you next time!"
)
CLOSING = ('kunde', 'Bis bald!')

STORY = [
    ('pina', 'Bitte schön, hier ist ein Chip für deinen Wagen.', 'Here you go, here is a token for your trolley.', [], 'Bridges Pina handing the customer the token right before his Danke in cue 427.'),
    ('kunde', 'Danke, das ging jetzt echt schnell!', 'Thanks, that went really fast just now!', [(427, 'Danke')], ''),
    ('pina', 'Gern! Das ist aber ein cooler Roller.', "You're welcome! That's a cool scooter, though.", [(427, 'Gern. Cooler Roller')], ''),
    ('kunde', 'Danke! Magst du mal kurz fahren?', 'Thanks! Feel like taking it for a quick ride?', [(429, 'Magst du mal fahren')], ''),
    ('pina', 'Echt? Okay, sehr gerne!', 'Really? Okay, I would love to!', [(432, 'Okay')], ''),
    ('kunde', 'Du musst einfach hier oben drücken.', 'You just have to press up here.', [(433, 'einfach hier drücken')], ''),
    ('kunde', 'Ja, genau, und jetzt ein bisschen anstoßen.', 'Yes, exactly, and now push off a little.', [(435, 'Ja'), (435, 'bisschen anstoßen')], ''),
    ('pina', 'Oh, der fährt ja super schnell! Das macht Spaß!', 'Oh, it goes super fast! This is fun!', [], 'Adapted from raw rolling cue 437 exclamation as Pina rides down the aisle.')
]

WALK = [
    (1, None, "'Thanks, that went really fast just now!' Saying something 'went really fast' uses a handy phrase built on the past form of 'go' — a natural compliment you'll hear whenever a repair or errand is sorted out quickly."),
    (2, None, "'You're welcome! That's a cool scooter, though.' The clipped one-syllable form of 'gladly' sounds breezy and informal. Notice that the German word for a kick or electric scooter comes from the action word for 'to roll', and middle 'but' here means an admiring 'though!' rather than a contradiction."),
    (3, None, "'Thanks! Feel like taking it for a quick ride?' Starting a casual question with 'do you like' plus that tiny word for 'once' is a friendly, reusable way to offer someone a turn."),
    (4, None, "'Really? Okay, I would love to!' Pairing the words for 'very' and 'gladly' gives the warmest everyday phrase for 'yes, I'd love to!' in Germany, without needing a full sentence."),
    (5, None, "'You just have to press up here.' The word for 'simply' or 'just' keeps instructions relaxed, while 'press' waits cleanly at the end after 'must'."),
    (6, None, "'Yes, exactly, and now push off a little.' That single word for 'exactly' confirms she's doing it right, and the final compound joins 'against' and 'push' for kicking off from the floor to get rolling."),
    (7, None, "'Oh, it goes super fast! This is fun!' Notice two classic German habits side by side: wheeled vehicles 'drive' rather than 'go', and something enjoyable literally 'makes fun' rather than 'is fun'.")
]
