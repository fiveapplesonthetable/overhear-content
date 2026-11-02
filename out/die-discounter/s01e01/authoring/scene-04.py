# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 04
ID = 'die-discounter-s01e01-scene-04'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 4
TITLE = 'Mein erster Tag  (My First Day)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'titus': 'Titus', 'peter': 'Peter', 'thorsten': 'Thorsten'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Incorporates the verified Titus first-day lines alongside Peter\'s break banter and Thorsten\'s loading-bay outburst.'

INTRO = (
    'Out on the loading bay behind the supermarket, teenager Titus introduces himself to the documentary camera on his very first shift. '
    'Veteran coworker Peter barely finishes teasing him before Thorsten bursts through the back door in a panic over Sabine\'s visit. '
    'Listen to the German first without worrying about catching every word.'
)
OPENER = "Let's go line by line through Titus's self-introduction and Thorsten's frantic orders."
TRANSITION = "Now let's hear the entire loading-bay scene once more."
OUTRO = (
    "So much for a quiet first morning — Titus is sent straight inside while the others scramble to the tills and the stockroom. "
    "You have practised introducing yourself, explaining why you are somewhere, talking about a real problem, and giving polite workplace instructions. "
    "See you next time!"
)
CLOSING = ('titus', 'Tschüss!')

STORY = [
    ('titus', 'Ja, ich bin Titus.', "Yes, I'm Titus.", [(73, 'Ja, ich bin Titus')], ''),
    ('titus', 'Heute ist mein erster Tag hier.', 'Today is my first day here.', [(73, 'Tag hier')], 'Recast Ich habe heute meinen ersten Tag hier in the nominative for beginner clarity.'),
    ('titus', 'Die anderen kenne ich noch nicht so gut.', "I don't know the others very well yet.", [(75, 'kenne ich'), (77, 'noch nicht so gut')], 'Restore Die anderen from auto-caption truncation Die ander.'),
    ('titus', 'Aber ich bin nicht hier, um Freunde zu finden.', "But I'm not here to make friends.", [(79, 'aber ich bin'), (79, 'nicht hier, um'), (81, 'Freunde zu finden')], 'Drop optional hedge jetzt.'),
    ('titus', 'Ich bin hier, um Geld zu verdienen.', "I'm here to earn money.", [(81, 'um Geld zu verdienen')], 'Drop conversational hedges ja eigentlich eher.'),
    ('peter', 'Natürlich! Komm mal her, Kleiner.', 'Of course! Come over here for a second, kid.', [(83, 'Natürlich'), (89, 'komm her')], 'Replace cigarette demand with friendly-bossy workplace beckoning.'),
    ('thorsten', 'Ich suche den ganzen Laden nach euch ab! Wir haben ein richtiges Problem.', "I've been searching the whole shop for you! We have a real problem.", [(99, 'Ich suche den ganzen Laden nach euch ab'), (101, 'ein richtiges Problem')], ''),
    ('thorsten', 'Sabine kommt gleich! Könnt ihr mal bitte an die Kasse gehen?', 'Sabine is coming any minute! Could you please go to the checkout?', [(103, 'Sabine kommt gleich'), (105, 'könnt ihr mal bitte an die Kasse gehen')], 'Omit garbled character names in auto-caption.'),
    ('thorsten', 'Und ihr beiden räumt mal das Lager auf! Ich fasse es nicht.', "And you two tidy up the stockroom! I can't believe this.", [(107, 'und ihr beiden räumt mal das Lager auf'), (109, 'fasse es nicht')], '')
]

WALK = [
    (0, None, "'Yes, I'm Titus.' Two crisp words before his name state who he is. Swap in your own name after that pair and you have the most natural self-introduction in German, with a casual 'yes' up front answering the camera crew."),
    (1, None, "'Today is my first day here.' Starting with the time word 'today' pulls the action word 'is' right behind it into second place, ahead of 'my first day'. Notice the masculine '-er' ending on the word for 'first' matching the word for 'day'."),
    (2, None, "'I don't know the others very well yet.' Putting 'the others' first spotlights his new coworkers right away. German uses this knowing word specifically for being acquainted with people or places, rather than knowing a fact, and the two-word chunk for 'not yet' leaves room for that to change."),
    (3, None, "'But I'm not here to make friends.' After the comma, a neat two-part frame expresses purpose — 'in order to'. Word for word, German says 'to find friends' where English says 'to make friends', tucking the action word right at the end."),
    (4, None, "'I'm here to earn money.' Titus repeats that exact purpose frame, swapping in 'earn money' to state his real goal. Unlike English, no extra 'some' is needed before the word for money when speaking in general."),
    (6, None, "'I've been searching the whole shop for you! We have a real problem.' Thorsten uses a split-apart expression for 'search thoroughly': the core word for 'search' sits near the front while its separable partner snaps shut at the end of the sentence."),
    (7, None, "'Sabine is coming any minute! Could you please go to the checkout?' Right after 'comes', that little time word means 'right away' or 'any minute now'. Even in a panic, pairing 'can you all' with 'just please' is a reusable way to soften a group instruction."),
    (8, None, "'And you two tidy up the stockroom! I can't believe this.' 'Tidy up' splits around the word for stockroom, sending 'up' to the end. His final outburst literally means 'I cannot grasp it', the go-to exclamation when something leaves you speechless.")
]
