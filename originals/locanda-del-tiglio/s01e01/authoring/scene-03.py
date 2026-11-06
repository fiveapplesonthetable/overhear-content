# Authoring module for locanda-del-tiglio-s01e01-scene-03.
ID = 'locanda-del-tiglio-s01e01-scene-03'
SHOW = 'locanda-del-tiglio'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Dove sono i miei occhiali?  (Where Are My Glasses?)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'cesare': 'Cesare', 'chiara': 'Chiara', 'bruno': 'Bruno'}
INTRO = 'Before the first guest arrives, guesthouse owner Cesare hurries in from the courtyard looking flustered. Chiara and Bruno watch as Cesare searches his pockets in a panic. Listen to the whole scene first.'
OPENER = "Let's unpack Cesare's morning panic one line at a time."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = 'Cesare found his glasses on his own forehead just as the taxi pulled up outside. Relax and let the rhythm of the words sink in; see you next time.'
CLOSING = ('cesare', 'Buona giornata!')
STORY = [
    ('cesare', 'Buongiorno a tutti! Benvenuta, Chiara. È tutto pronto?', 'Good morning, everyone! Welcome, Chiara. Is everything ready?'),
    ('chiara', 'Buongiorno! Sì, la reception è pulita e le chiavi sono pronte.', 'Good morning! Yes, the desk is clean and the keys are ready.'),
    ('cesare', "L'ospite della camera quattro resta tutta la settimana. Tutto deve essere perfetto!", "Today's guest in room four is staying all week. Everything must be perfect!"),
    ('bruno', 'Calma, Cesare. La camera è pulita e gli asciugamani sono freschi.', 'Relax, Cesare. The room is clean and the towels are fresh.'),
    ('cesare', 'Devo leggere il registro, ma non trovo i miei occhiali!', 'I need to read the reservation book, but I cannot find my glasses!'),
    ('chiara', 'Sono nella tasca della giacca?', 'Are they in your coat pocket?'),
    ('cesare', 'No, solo la mia penna e tre vecchie ricevute!', 'No, only my pen and three old receipts!'),
    ('bruno', 'Guarda nello specchio dietro il banco, capo.', 'Look in the mirror behind the desk, boss.'),
    ('cesare', 'Perché nello specchio... oh! Sono sulla mia testa!', 'Why would my glasses be in the... oh! They are on my head!'),
    ('chiara', 'Proprio lì sulla fronte, sani e salvi.', 'Right there on your forehead, safe and sound.'),
    ('cesare', 'Non ditelo a nessuno! Ora un bel sorriso quando suona il campanello.', 'Do not tell anyone! Now, smile brightly when the bell rings.'),
    ('bruno', 'Ecco un taxi davanti al cancello proprio adesso.', 'Here comes a taxi at the gate right now.'),
]
WALK = [
    (0, None, ["'Good morning, everyone! Welcome, Chiara. Is everything ready?' Welcome changes its final letter depending on who walks in.", (None, 'Benvenuta'), 'Because Cesare is greeting Chiara, it ends in a; for a man, that final vowel becomes o.']),
    (1, None, ["'Good morning! Yes, the desk is clean and the keys are ready.' Compare Cesare's singular ready with Chiara's plural one here.", (None, 'Sono pronte.'), 'Keys is feminine plural, so ready switches its ending to e to match them.']),
    (2, None, ["'Today's guest in room four is staying all week. Everything must be perfect!' Look at how Italian says all week.", (None, 'Tutta la settimana.'), 'You keep the word for the right in the middle: literally whole the week.']),
    (3, None, ["'Relax, Cesare. The room is clean and the towels are fresh.' Bruno settles his boss down with one calm word, and then names the towels.", (None, 'Gli asciugamani'), 'Built from dry and hands, the Italian word for towel literally means a hand-dryer.']),
    (4, None, ["'I need to read the reservation book, but I cannot find my glasses!' Where English says cannot find, Italian uses the plain present.", (None, 'Non trovo'), 'Literally I do not find, Italian skips can with verbs of finding, seeing, and hearing.']),
    (5, None, ["'Are they in your coat pocket?' Chiara leaves out the word for your completely.", (None, 'Nella tasca della giacca?'), 'With clothing and body parts, Italian prefers the pocket of the coat when it is obvious whose coat it is.']),
    (6, None, "'No, only my pen and three old receipts!' Common everyday describing words like old, new, big, and small often sit before what they describe, just like in English."),
    (7, None, ["'Look in the mirror behind the desk, boss.' Because mirror starts with s plus another consonant, in and the merge into a fuller form.", (None, 'Nello specchio'), 'At the end, Bruno calls Cesare boss in a warm, teasing tone only an old colleague could get away with.']),
    (8, None, ["'Why would my glasses be in the... oh! They are on my head!' On and the blend into one smooth word too.", (None, 'Sulla mia testa!'), 'Whenever on meets the in Italian, the two fuse together rather than staying separate.']),
    (9, None, ["'Right there on your forehead, safe and sound.' Italian has almost the exact twin of the English expression safe and sound.", (None, 'Sani e salvi.'), 'Literally healthy and saved, both words take plural endings here because glasses is plural.']),
    (10, None, ["'Do not tell anyone! Now, smile brightly when the bell rings.' Speaking to both Chiara and Bruno at once, Cesare uses the plural command.", (None, 'Non ditelo'), 'Say to you all and it hook together at the end, meaning do not say it.']),
    (11, None, ["'Here comes a taxi at the gate right now.' One lively pointing word announces something appearing right in front of you.", (None, 'Ecco un taxi'), 'Use that opening word to hand someone a key, point out a taxi, or say here we are.']),
]
