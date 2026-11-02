# Authoring module for boris-s01e01-scene-10.
ID = 'boris-s01e01-scene-10'
SHOW = 'boris'
SEASON = 1
EPISODE = 1
SCENE = 10
TITLE = 'Un giornalista sul set  (A Journalist on Set)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'sergio': 'Sergio', 'rene': 'René', 'alessandro': 'Alessandro'}
SOURCE_NAME = 'Boris S01E01'
SOURCE_FILE = 'sources/boris/s01/e01.it.srt'
INTRO = (
    'Back on the sidelines of Studio 2, production manager Sergio starts his phone call with the network sounding tough about Corinna\'s age, then folds completely within ten seconds. '
    'Meanwhile, Rene apologises to Alessandro and points out an influential newspaper critic watching the chaos. '
    'Listen to the Italian scene first without worrying about catching every detail.'
)
OPENER = (
    "Let's trace Sergio's instant retreat on the phone and Rene's warning about the journalist."
)
TRANSITION = 'Now hear the phone call and the sideline warning once more in full.'
OUTRO = (
    'You have heard "punto e basta" for "period", "non c\'e problema" for "no problem", '
    'and "fare una brutta figura" for embarrassing yourself. See you next time.'
)
CLOSING = ('sergio', 'Buona giornata!')
STORY = [
    ('sergio', 'Pronto? Qualcuno ha fatto un grosso errore.', 'Hello? Someone made a big mistake.', [(325, 'Pronto'), (326, 'qualcuno ha fatto un grosso errore')], ''),
    ('sergio', 'Questa deve dire che ha trentaquattro anni, punto e basta.', 'She has to say that she is thirty-four, period.', [(327, 'Questa deve dire che ha'), (327, 'anni'), (327, 'e basta')], 'Whisper heard "butta e basta" and "34"; restored to "punto e basta" and "trentaquattro".'),
    ('rene', 'Che ha detto Duccio?', 'What did Duccio say?', [(328, 'che ha detto')], 'Whisper heard "Lucio"; restored character name "Duccio".'),
    ('alessandro', "Non l'ho trovato.", 'I did not find him.', [(328, "non l'ho trovato")], ''),
    ('sergio', 'La risolviamo, non si preoccupi.', 'We will sort it out, do not worry.', [(328, 'La risolviamo'), (329, 'non si preoccupi')], ''),
    ('sergio', "Va bene, non c'è problema. Arrivederci.", 'All right, no problem. Goodbye.', [(329, "Va bene, non c'è problema"), (329, 'Arrivederci')], ''),
    ('rene', 'Che facciamo?', 'What do we do?', [(331, 'Che facciamo')], ''),
    ('sergio', 'Stiamo risolvendo.', 'We are sorting it out.', [(336, 'Stiamo risolvendo')], ''),
    ('rene', 'Ciao. Scusa per prima.', 'Hi. Sorry about earlier.', [(338, 'Ciao'), (340, 'scusa per prima')], ''),
    ('rene', 'Ho fatto una brutta figura con Antonio Di Pollina di Repubblica.', 'I made a fool of myself in front of Antonio Di Pollina from Repubblica.', [(341, 'ho fatto'), (341, 'una figura'), (342, 'con Antonio Di Pollina di Repubblica')], 'Softened "figura di merda" to standard idiom "brutta figura".'),
    ('alessandro', "C'è un giornalista?", 'Is there a journalist here?', [(343, "c'è un giornalista")], ''),
    ('rene', "Sì, c'è. Eccolo là.", 'Yes, there is. There he is over there.', [(344, 'Sì'), (344, "c'è"), (345, 'Eccolo là')], ''),
    ('rene', 'Parlano sempre male della televisione.', 'They always speak badly of television.', [(348, 'parlano sempre male della televisione')], ''),
    ('rene', 'Scrive un articolo su di noi.', 'He is writing an article about us.', [(350, 'Scrive un articolo su di noi')], ''),
]
WALK = [
    (0, None, "'Hello? Someone made a big mistake.' Italians answer the phone with \"pronto?\", literally \"ready?\", dating back to early switchboard operators."),
    (1, None, "'She has to say that she is thirty-four, period.' \"Punto e basta\" literally says \"full stop and enough\", the ultimate Italian way to declare a topic closed — right before Sergio caves."),
    (2, None, "'What did Duccio say?' Short \"che\" at the start of a question works just like \"cosa\" for \"what\": \"che ha detto?\""),
    (3, None, "'I did not find him.' Alessandro covers for Duccio! Before \"ho\", \"lo\" for \"him\" drops its vowel to become \"l'ho trovato\"."),
    (4, None, "'We will sort it out, do not worry.' Notice how fast Sergio switches to ultra-polite \"non si preoccupi\", addressing the network boss respectfully as \"lei\"."),
    (5, None, "'All right, no problem. Goodbye.' \"Non c'e problema\" is the effortless everyday twin of English \"no problem\"."),
    (6, None, "'What do we do?' In Italian, \"che facciamo?\" covers both \"what are we doing?\" and \"what shall we do now?\""),
    (7, None, "'We are sorting it out.' Pairing \"stiamo\" with \"risolvendo\" emphasises action right in progress: \"we're in the middle of fixing it\"."),
    (8, None, "'Hi. Sorry about earlier.' \"Prima\" means \"before\" or \"earlier\", so \"scusa per prima\" is the natural way to apologise for an earlier outburst."),
    (9, None, "'I made a fool of myself in front of Antonio Di Pollina from Repubblica.' \"Fare una brutta figura\" — literally \"making an ugly figure\" — is Italy's classic cultural phrase for losing face in public."),
    (10, None, "'Is there a journalist here?' Like \"regista\" and \"stagista\", \"giornalista\" ends in \"-ista\" and serves for men and women alike, with \"un\" marking a male reporter here."),
    (11, None, "'Yes, there is. There he is over there.' \"Ecco\" points someone out, and hooking \"lo\" onto it makes \"eccolo la\", \"there he is over there\"."),
    (12, None, "'They always speak badly of television.' Just like \"andare male\" earlier, \"parlare male di\" literally says \"to speak badly of\", meaning to trash or pan something."),
    (13, None, "'He is writing an article about us.' Where English says \"an article about us\", Italian stacks \"su di\" before personal words like \"noi\": \"su di noi\"."),
]
