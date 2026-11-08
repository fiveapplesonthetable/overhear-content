# Authoring module for locanda-del-tiglio-s01e01-scene-01.
ID = 'locanda-del-tiglio-s01e01-scene-01'
SHOW = 'locanda-del-tiglio'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Alza la maniglia  (Lift the Handle)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'chiara': 'Chiara', 'bruno': 'Bruno'}
INTRO = 'Chiara arrives early for her very first morning at the Locanda del Tiglio guesthouse in Bologna. Behind the front desk, veteran handyman Bruno is already pouring strong hot tea. Listen to the scene first without worrying about catching every word.'
OPENER = "Now let's walk through their first meeting one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Chiara is inside, the eight brass keys are on the board, and her first morning has begun. Don't worry if a few words went past quickly; they come back all week. See you next time."
CLOSING = ('chiara', 'A presto!')
STORY = [
    ('chiara', 'Buongiorno! Scusi, la porta è chiusa?', 'Good morning! Excuse me, is the door locked?'),
    ('bruno', 'Buongiorno. No, prima alza la maniglia e poi spingi.', 'Good morning. No, lift the handle first, then push.'),
    ('chiara', 'Ah, si apre! Grazie. Sono Chiara, la nuova addetta alla reception.', 'Oh, it opens! Thank you. I am Chiara, the new receptionist.'),
    ('bruno', 'Io sono Bruno. Sei in anticipo di dieci minuti.', 'I am Bruno. You are ten minutes early.'),
    ('chiara', "Cammino sempre veloce il primo giorno. Dov'è il computer?", 'I always walk fast on my first day. Where is the computer?'),
    ('bruno', 'Nel cassetto. Qui usiamo questo grande registro di carta e una matita.', 'In the drawer. Here we use this big paper book and a pencil.'),
    ('chiara', 'Un registro di carta? Davvero?', 'A paper book? Really?'),
    ('bruno', 'La carta funziona ancora quando va via la corrente.', 'Paper still works when the power goes out.'),
    ('chiara', 'Giusto! E queste sono le chiavi?', 'Fair enough! And these are the keys?'),
    ('bruno', "Sì, otto camere e otto chiavi di ottone. L'ospite della camera quattro arriva oggi.", "Yes, eight rooms, eight brass keys. Room four's guest arrives today."),
    ('chiara', 'Perfetto. Dimmi tutto quello che devo sapere.', 'Great. Tell me everything I need to know.'),
    ('bruno', 'Prima regola: bevi il tè caldo, poi rispondi al campanello.', 'Rule one: drink hot tea first, then answer the bell.'),
]
WALK = [
    (0, None, ["'Good morning! Excuse me, is the door locked?' Chiara starts with the polite way to get a stranger's attention.", (None, 'Scusi.'), 'At the end, Italian turns a statement into a yes-or-no question simply by raising the voice, without changing the word order.']),
    (1, None, ["'Good morning. No, lift the handle first, then push.' Bruno pairs two time markers to sequence his instructions.", (None, 'Prima.'), 'That means first, and later in the sentence the little word for then shows the second step.']),
    (2, None, ["'Oh, it opens! Thank you. I am Chiara, the new receptionist.' Notice how Italian says a door opens by itself.", (None, 'Si apre!'), 'She also drops the word for I when introducing herself, since the form of to be already tells us who is speaking.']),
    (3, None, ["'I am Bruno. You are ten minutes early.' Bruno includes the word for I here for contrast: you are Chiara, and I am Bruno.", (None, 'In anticipo.'), 'Literally in advance, that handy two-word chunk is the everyday Italian way to say someone arrived early.']),
    (4, None, ["'I always walk fast on my first day. Where is the computer?' Two tiny words squeeze together at the start of her question.", (None, "Dov'è"), 'Where and is merge with an apostrophe so the vowels flow smoothly in one beat.']),
    (5, None, ["'In the drawer. Here we use this big paper book and a pencil.' Italian joins in and the into one compact word before drawer.", (None, 'Nel cassetto.'), 'Further on, paper book is built as book of paper, which is how Italian names what an object is made from.']),
    (6, None, ["'A paper book? Really?' Chiara cannot hide her surprise at a desk with no screen.", (None, 'Davvero?'), 'Built from the word for true, this single word works anywhere you would say really or seriously in English.']),
    (7, None, ["'Paper still works when the power goes out.' Watch how Italian builds never around the action.", (None, 'funziona ancora'), 'Not goes before loses and never comes right after it; in Italian the two negatives team up instead of cancelling out.']),
    (8, None, ["'Fair enough! And these are the keys?' One crisp word concedes Bruno's point right away.", (None, 'Giusto!'), 'It literally means right or fair, and Italian speakers use it constantly to agree with good common sense.']),
    (9, None, ["'Yes, eight rooms, eight brass keys. Room four's guest arrives today.' Notice the ending change from singular to plural.", (None, 'Otto camere'), 'The singular ends in a, and in the plural that final vowel shifts to e.']),
    (10, None, ["'Great. Tell me everything I need to know.' Now that they are colleagues, Chiara switches to casual speech.", (None, 'Dimmi'), 'Tell and to me fuse into one punchy word, doubling the m sound in the middle.']),
    (11, None, ["'Rule one: drink hot tea first, then answer the bell.' Italian puts the describing word after the drink.", (None, 'Il tè caldo'), 'Literally the tea hot, that noun-first order is standard whenever you describe food, drinks, or colours.']),
]
