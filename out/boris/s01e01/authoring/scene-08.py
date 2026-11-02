# Authoring module for boris-s01e01-scene-08.
ID = 'boris-s01e01-scene-08'
SHOW = 'boris'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = 'Stanis vuole mollare  (Stanis Wants to Quit)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'alessandro': 'Alessandro', 'stanis': 'Stanis', 'arianna': 'Arianna'}
SOURCE_NAME = 'Boris S01E01'
SOURCE_FILE = 'sources/boris/s01/e01.it.srt'
INTRO = (
    'Out in the studio corridor, Alessandro knocks on doors looking for Duccio, while Stanis corners Arianna with a dramatic threat to quit the show. '
    'Arianna has zero patience for another crisis and calls Stanis\'s bluff in seconds. '
    'Listen to the Italian scene first; you do not need to catch every word.'
)
OPENER = (
    "Let's walk through Stanis's melodramatic threat and Arianna's no-nonsense reply."
)
TRANSITION = 'Now listen to the corridor standoff once more all the way through.'
OUTRO = (
    'You have heard "smettila" for "knock it off", "sul serio" for "seriously", '
    'and Stanis\'s favourite insult, "troppo italiana". See you next time.'
)
CLOSING = ('arianna', 'Ciao!')
STORY = [
    ('alessandro', 'Duccio? Duccio?', 'Duccio? Duccio?', [(293, 'Duccio, Duccio')], ''),
    ('stanis', 'Senti, ho pensato di mollare la serie.', 'Listen, I have been thinking of quitting the series.', [(294, 'Senti, ho pensato di mollare la serie')], ''),
    ('stanis', 'Che effetto ti fa?', 'How does that make you feel?', [(295, 'Che effetto ti fa')], ''),
    ('arianna', 'Smettila, Stanis.', 'Stop it, Stanis.', [(296, 'Smettila Stanis')], ''),
    ('stanis', 'No, sul serio, Arianna, perché io non sono contento.', 'No, seriously, Arianna, because I am not happy.', [(297, 'No, sul serio Arianna'), (298, 'Perché io non sono contento')], ''),
    ('stanis', 'Quando non sono contento, entrano in azione i miei avvocati.', 'When I am not happy, my lawyers swing into action.', [(299, 'quando io non sono contento'), (300, 'i miei avvocati')], 'Whisper heard "in relazione"; restored to standard idiom "in azione".'),
    ('stanis', 'Sai che stanno facendo? Stanno sciogliendo il mio contratto.', 'Do you know what they are doing? They are dissolving my contract.', [(301, 'Sai che stanno facendo'), (302, 'Stanno sciogliendo il mio contratto')], ''),
    ('arianna', 'Abbiamo un sacco di problemi, Stanis. Dai, fai il bravo.', 'We have tons of problems, Stanis. Come on, behave yourself.', [(303, 'Abbiamo un sacco di problemi Stanis, dai fai il bravo')], ''),
    ('stanis', 'Sì, ma tu che dici? La mollo?', 'Yes, but what do you say? Should I drop it?', [(304, 'Sì ma tu che dici'), (305, 'La mollo')], ''),
    ('arianna', 'Sei un cretino, Stanis.', 'You are an idiot, Stanis.', [(307, 'Sei un cretino Stanis')], ''),
    ('stanis', 'Ok, però Corinna è troppo italiana.', 'Okay, though Corinna is too Italian.', [(308, 'Ok'), (308, 'però Corinna è'), (309, 'troppo italiana')], 'Omitted vulgarity for A1 focus.'),
]
WALK = [
    (0, None, "'Duccio? Duccio?' Alessandro wanders down the dim corridor calling out for the director of photography."),
    (1, None, "'Listen, I have been thinking of quitting the series.' Earlier Stanis joked \"mollo questa serie\"; now he brings back \"mollare\" with \"ho pensato di\", \"I've thought about\"."),
    (2, None, "'How does that make you feel?' Word for word, \"che effetto ti fa?\" asks \"what effect does it make on you?\", fishing for a gasp that never comes."),
    (3, None, "'Stop it, Stanis.' Adding \"la\" onto \"smetti\" makes the punchy everyday command \"smettila!\" — \"cut it out!\" or \"drop it!\""),
    (4, None, "'No, seriously, Arianna, because I am not happy.' \"Sul serio\" is the go-to two-word phrase for \"seriously\" or \"for real\"."),
    (5, None, "'When I am not happy, my lawyers swing into action.' \"Entrare in azione\" literally means \"to enter into action\", and \"avvocati\" is the plural of \"avvocato\", lawyer."),
    (6, None, "'Do you know what they are doing? They are dissolving my contract.' \"Sciogliere\" normally means melting snow or untying a knot; in legal talk it means dissolving a contract."),
    (7, None, "'We have tons of problems, Stanis. Come on, behave yourself.' \"Un sacco di\" literally says \"a sack of\", a favourite casual way to say \"loads of\", and \"fai il bravo\" talks to Stanis like a naughty child."),
    (8, None, "'Yes, but what do you say? Should I drop it?' Notice how \"tu che dici?\", \"what do you say?\", stands in for English \"what do you think?\" when asking for advice."),
    (9, None, "'You are an idiot, Stanis.' Arianna refuses to play along and punctures his drama in four blunt words."),
    (10, None, "'Okay, though Corinna is too Italian.' Stanis caves immediately. Throughout the show, his pretentious catchphrase is dismissing anything messy or melodramatic as \"troppo italiano\", too Italian."),
]
