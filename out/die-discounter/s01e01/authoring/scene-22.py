# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 22
ID = 'die-discounter-s01e01-scene-22'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 22
TITLE = 'Das geht auf mich  (It Is on Me)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'jonas': 'Jonas', 'thorsten': 'Thorsten', 'fahri': 'Fahri'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Vulgarity in cue 755 omitted per quality spec; preserves the comedic escalation from geht auf mich to Jonas tackling Fahri.'

INTRO = (
    "Trying to act like a big shot in front of Fahri, Thorsten waves off the stolen nuts and declares they are on the house. "
    "When Fahri keeps poking fun at him, Thorsten loses his temper — and overeager Jonas leaps across the office to tackle Fahri to the floor as the first episode ends in chaos. "
    "Listen to the German finale first."
)
OPENER = "Let's unpack 'it's on me', Thorsten's outburst, and the chaotic finale commands."
TRANSITION = "Now let's hear the whole finale scene once more from top to bottom."
OUTRO = (
    "And just like that, Thorsten's chaotic first day with Titus ends with a celebrity pinned to the office carpet by Jonas! "
    "Across Episode One you have learned dozens of authentic German supermarket, workplace, and everyday expressions — from 'keep the change' and 'it's on me' to 'hands off!'. "
    "See you next time!"
)
CLOSING = ('thorsten', 'Auf Wiedersehen!')

STORY = [
    ('jonas', 'Thorsten, er hat hier Nüsse geklaut und einfach eingesteckt.', 'Thorsten, he stole nuts here and just pocketed them.', [(743, 'geklaut'), (745, 'eingesteckt')], ''),
    ('thorsten', 'Ach komm, das ist egal! Das geht heute auf mich.', "Oh come on, it doesn't matter! That's on me today.", [(747, 'geht auf mich')], 'Replace English Come on with German Ach komm.'),
    ('fahri', 'Oh, wie großzügig! Dir gehört wohl jetzt der ganze Laden?', 'Oh, how generous! So the whole shop belongs to you now, does it?', [(751, 'Oh, du groß'), (753, 'der Laden jetzt')], 'Expand clipped Oh, du groß into clean A1 Oh, wie großzügig!'),
    ('thorsten', 'Und ihr Schauspieler? Immer nur Champagner und Kaviar, oder was?', 'And you actors? Always just champagne and caviar, or what?', [(763, 'oder was'), (763, 'Champagner und')], 'Omit cue 755 vulgarity and spell Kaviar in standard German.'),
    ('thorsten', 'Jetzt reicht es! Hör sofort auf damit!', "That's enough now! Cut that out right now!", [(769, 'hör auf')], ''),
    ('jonas', 'Los, los! Keine Bewegung!', "Go, go! Don't move!", [(772, 'Los, los')], ''),
    ('fahri', 'Moment, Stopp! Ich habe schon aufgegeben!', 'Wait, stop! I already gave up!', [(773, 'Ich habe aufgegeben')], ''),
    ('thorsten', 'Jonas, lass das! Finger weg von ihm!', 'Jonas, stop that! Hands off him!', [(775, 'Finger weg')], ''),
    ('thorsten', 'Okay, Entschuldigung! Komm hoch, Fahri, komm.', 'Okay, sorry! Come on up, Fahri, get up.', [(777, 'Okay, komm, komm hoch. Komm')], '')
]

WALK = [
    (0, None, "'Thorsten, he stole nuts here and just pocketed them.' That final word literally joins 'in' and 'stuck' — sticking something into a pocket or bag, whether keys of your own or unpaid snacks in a shop."),
    (1, None, "'Oh come on, it doesn't matter! That's on me today.' Two top-tier everyday expressions sit side by side here: 'that is equal' means 'it doesn't matter', and 'that goes onto me' is the exact way to say 'it's on me!' when paying for someone."),
    (3, None, "'And you actors? Always just champagne and caviar, or what?' Look at the vivid German word for an actor: it literally glues 'show' and 'player' together — a 'show-player'! Tacking 'or what?' onto the end adds sharp sarcasm."),
    (4, None, "'That's enough now! Cut that out right now!' Literally, 'now suffices it!' is what German speakers snap when their patience runs out, followed by 'stop therewith!' with 'up' and 'therewith' closing the command."),
    (5, None, "'Go, go! Don't move!' Shouting the word for 'loose!' is how German says 'go!' at the start of a race or an action movie, and 'no movement!' matches English 'don't move!' in security dramas."),
    (6, None, "'Wait, stop! I already gave up!' Just like English 'give up', German pairs 'give' with the prefix 'up', tucking 'ge-' right between the prefix and the stem in the past form."),
    (7, None, "'Jonas, stop that! Hands off him!' Where English shouts 'hands off!', German literally says 'fingers away!' — a punchy two-word warning you'll hear from parents, bosses, and friends alike."),
    (8, None, "'Okay, sorry! Come on up, Fahri, get up.' Pairing 'come' with the word for 'high' or 'up' gives the natural everyday phrase for helping someone back onto their feet.")
]
