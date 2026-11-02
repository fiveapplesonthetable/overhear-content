# Authoring module for dix-pour-cent-s02e03-scene-04.
ID = 'dix-pour-cent-s02e03-scene-04'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 3
SCENE = 4
TITLE = 'Matinée chez ASK  (Morning at ASK)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E03'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e03.fr.dual.srt'
INTRO = "At the ASK agency, the agents and assistants begin a busy morning. Camille approaches Mathias to ask him to meet her visiting mother Annick for lunch, putting Mathias in an awkward personal situation. Let's listen to the scene in French first."
OPENER = "Let's examine how Camille convinces Mathias to have coffee with her mother."
TRANSITION = "Now let's hear Camille and Mathias's quiet discussion again at full speed."
OUTRO = 'Mathias reluctantly agrees to a quick coffee with Annick, fearing that their shared past might be uncovered. Camille is relieved, though keeping their family connection secret remains a daily challenge. See you next time!'
CLOSING = ('camille', 'Bonne journée!')
STORY = [
    ('camille', 'Mathias, bonjour, tu as une minute?', 'Mathias, hello, do you have a minute?', [(94, '-Bonjour.')], ''),
    ('mathias', 'Bonjour Camille, je suis très pressé.', 'Good morning Camille, I am in a hurry.', [(94, '-Bonjour.')], ''),
    ('camille', "Je t'ai dit que maman était là?", 'Did I tell you that mom was here?', [(95, "Je t'ai dit que maman était là ?")], ''),
    ('mathias', 'Oui, je crois. Quand est-elle arrivée?', 'Yes, I think so. When did she arrive?', [(96, 'Je crois. Quand ?')], ''),
    ('camille', "Elle vient d'arriver à Paris ce matin.", 'She just arrived in Paris this morning.', [(97, "Elle vient d'arriver.")], ''),
    ('camille', 'Si on déjeune, tu pourrais nous rejoindre.', 'If we have lunch, you could join us.', [(98, "Si je l'emmène déjeuner quelque part près d'ici,"), (99, 'tu pourrais nous rejoindre.')], ''),
    ('mathias', "C'est impossible, je n'ai pas le temps.", 'It is impossible, I do not have time.', [(100, "Je n'ai pas le temps.")], ''),
    ('camille', 'Demain ou vendredi, elle reste toute la semaine.', 'Tomorrow or Friday, she is staying all week.', [(101, 'Demain, ou vendredi ? Elle est là toute la semaine...')], ''),
    ('camille', "S'il te plaît, ça me ferait vraiment plaisir.", 'Please, it would really make me happy.', [(103, "S'il te plaît, ça me ferait vraiment plaisir.")], ''),
    ('camille', 'Ça ferait plaisir à maman aussi.', 'It would please mom as well.', [(104, 'À elle aussi.')], ''),
    ('mathias', 'Ne me regarde pas avec cet air triste.', 'Do not look at me with that sad look.', [(105, 'Épargne-moi ton air de chien battu.')], ''),
    ('mathias', "D'accord, demain, juste pour le café.", 'All right, tomorrow, just for coffee.', [(106, 'Demain. Pour le café.')], ''),
    ('camille', "Merci Mathias, c'est super gentil.", 'Thank you Mathias, that is super nice.', [(106, 'Demain. Pour le café.')], ''),
    ('mathias', 'Mais pas un mot aux autres agents.', 'But not a word to the other agents.', [(106, 'Demain. Pour le café.')], ''),
]
WALK = [
    (0, None, "'Mathias, hello, do you have a minute?' Even in an office, Camille uses casual 'you' with Mathias here, turning 'you have a minute' into a question through rising pitch alone."),
    (1, None, "'Good morning Camille, I am in a hurry.' Literally 'I am very pressed', French uses a cognate of 'pressed' where English says 'in a rush'."),
    (2, None, "'Did I tell you that mom was here?' Notice that French never drops the linking 'that' after 'told you', unlike English where 'did I tell you mom was here' needs no connector."),
    (3, None, "'Yes, I think so. When did she arrive?' French says simply 'I believe' without adding 'so', and 'arrived' gains a silent extra '-e' in writing to match a female traveler."),
    (4, None, "'She just arrived in Paris this morning.' Built from 'she comes from arriving', this handy construction expresses something that happened moments ago."),
    (5, None, "'If we have lunch, you could join us.' Softening the invitation with 'you could' sounds polite and tentative in French, while 'us' sits directly before 'join'."),
    (6, None, "'It is impossible, I do not have time.' Even in the negative, 'I do not have the time' keeps 'the' in French, right after the exact cognate 'impossible'."),
    (7, None, "'Tomorrow or Friday, she is staying all week.' Unlike English, French writes days of the week in lowercase, and uses present 'stays' to cover 'is staying'."),
    (8, None, "'Please, it would really make me happy.' Taken word-for-word, casual 'please' says 'if it pleases you', and 'make me pleasure' is the warm French idiom meaning 'make me happy'."),
    (9, None, "'It would please mom as well.' Swapping 'me' for 'to mom' reuses that same 'make pleasure' expression, capped off with 'also' to mean 'as well'."),
    (10, None, "'Do not look at me with that sad look.' French needs no 'at' after 'look', placing 'me' before the command, while 'air' means someone's facial expression."),
    (11, None, "'All right, tomorrow, just for coffee.' Notice French says 'for the coffee' with 'the' included, using one word to mean both the drink and a neighborhood cafe."),
    (12, None, "'Thank you Mathias, that is super nice.' Casual 'super' works right before 'kind' in spoken French just as in English, without changing its spelling."),
    (13, None, "'But not a word to the other agents.' Combining 'to' and 'the' into a single three-letter contraction before 'other agents' is mandatory in French rather than keeping them separate."),
]
