# Authoring module for boris-s01e01-scene-03.
ID = 'boris-s01e01-scene-03'
SHOW = 'boris'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Tre regole e sette caffè  (Three Rules and Seven Coffees)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'arianna': 'Arianna', 'alessandro': 'Alessandro', 'biascica': 'Biascica'}
SOURCE_NAME = 'Boris S01E01'
SOURCE_FILE = 'sources/boris/s01/e01.it.srt'
INTRO = (
    'Once Lopez leaves the set, assistant director Arianna lays down three strict ground rules for Alessandro and hands him over to Biascica. '
    'Before trusting the new intern with light stands and coffee, Biascica has one vital question about football. '
    'Hear the Italian conversation first, and let the rhythm wash over you.'
)
OPENER = (
    "Let's unpack Arianna's three rules and Biascica's football test one line at a time."
)
TRANSITION = 'Now listen to the whole exchange again, from the three rules to the seven coffees.'
OUTRO = (
    'You have heard "primo, secondo, terzo" for listing rules, how to ask someone\'s football team, '
    'and the classic cheer "Forza Roma". See you next time.'
)
CLOSING = ('alessandro', 'A presto!')
STORY = [
    ('arianna', 'Vi ricordo che non si fuma sul set.', 'I remind you all that there is no smoking on set.', [(92, 'Vi ricordo che non si fuma sul set')], ''),
    ('arianna', 'Primo: tu non parli mai.', 'First: you never speak.', [(95, 'primo, tu non parli'), (96, 'Mai')], 'Condensed from "se non interpellato. Mai." for A1 simplicity.'),
    ('arianna', 'Secondo: se ti dico una cosa, tu la fai e basta.', 'Second: if I tell you something, you do it and that is all.', [(97, 'Secondo, se ti dico'), (97, 'tu la fai e basta')], ''),
    ('arianna', 'Terzo: tu sei una macchina, sei un furetto.', 'Third: you are a machine, you are a ferret.', [(98, 'Terzo'), (99, 'Tu sei una macchina'), (99, 'sei un furetto')], ''),
    ('arianna', 'Se non ti sta bene, te ne vai.', 'If that does not suit you, you leave.', [(100, 'Se non ti sta bene te ne vai')], ''),
    ('alessandro', 'Va bene, io sono Alessandro.', 'All right, I am Alessandro.', [(101, 'Va bene, io sono Alessandro')], ''),
    ('arianna', 'Sì, non fa niente, vieni con me.', 'Yes, never mind, come with me.', [(102, 'Sì, non fa niente, vieni con me')], ''),
    ('biascica', 'Di che squadra sei?', 'Which team do you support?', [(106, 'che squadra sei')], 'Standardised "Di" from Romanesco "De".'),
    ('alessandro', 'Come, scusa?', 'Sorry, what was that?', [(107, 'Come scusa')], ''),
    ('alessandro', 'Della Roma?', 'Roma?', [(109, 'Della Roma')], ''),
    ('biascica', 'Bravo! Vedi quegli stativi?', 'Good lad! Do you see those light stands?', [(110, 'Bravo'), (111, 'vedi'), (111, 'stativi')], 'Standardised plural "quegli stativi".'),
    ('alessandro', 'Dove li devo portare?', 'Where should I carry them?', [(112, 'Dove li devo portare')], ''),
    ('biascica', 'No, li devi guardare, qua rubano tutto.', 'No, you have to watch them, people steal everything here.', [(113, 'No, li devi'), (113, 'rubano tutto')], 'Standardised "guardare" from Romanesco "guardà".'),
    ('biascica', 'E poi prepara sette caffè per i ragazzi.', 'And then make seven coffees for the guys.', [(114, 'E poi prepara'), (114, 'caffè per i ragazzi'), (115, 'Sette')], 'Combined the extra Roma coffee into one line.'),
    ('alessandro', 'Forza Roma!', 'Go Roma!', [(116, 'Forza Roma')], ''),
]
WALK = [
    (0, None, "'I remind you all that there is no smoking on set.' \"Non si fuma\" literally says \"one does not smoke\", the exact phrasing you will see on \"No smoking\" signs across Italy."),
    (1, None, "'First: you never speak.' Just as in the first scene, \"non\" before \"parli\" pairs up with \"mai\", meaning \"never\", after it."),
    (2, None, "'Second: if I tell you something, you do it and that is all.' Adding \"e basta\" at the end literally means \"and enough\", shutting down any argument on the spot."),
    (3, None, "'Third: you are a machine, you are a ferret.' Arianna counts off \"primo, secondo, terzo\" for \"first, second, third\", and compares a quick intern to a \"furetto\", a darting ferret."),
    (4, None, "'If that does not suit you, you leave.' \"Ti sta bene\" literally asks whether something \"stands well\" with you, while \"te ne vai\" is the brisk everyday chunk for \"you walk away\"."),
    (5, None, "'All right, I am Alessandro.' \"Va bene\" is the universal Italian agreement, literally \"it goes well\", useful in almost every conversation."),
    (6, None, "'Yes, never mind, come with me.' Arianna brushes his name right off with \"non fa niente\", literally \"it makes nothing\", meaning \"it doesn't matter\"."),
    (7, None, "'Which team do you support?' Word for word, Biascica asks \"of what team are you?\" using \"squadra\", the word for a sports team or work crew."),
    (8, None, "'Sorry, what was that?' Pairing \"come\", literally \"how\", with \"scusa\" is a natural, polite way to ask someone to repeat a question."),
    (9, None, "'Roma?' Notice \"della\", combining \"of\" and \"the\", because Italian football clubs carry \"the\" in front of the city name: you belong \"of the Roma\"."),
    (10, None, "'Good lad! Do you see those light stands?' \"Bravo\" praises one male listener; for a woman it changes to \"brava\". \"Stativi\" are the heavy metal stands holding studio lamps."),
    (11, None, "'Where should I carry them?' \"Portare\" covers \"bring\", \"take\", and \"carry\", and little \"li\" stands in for \"them\" right before \"devo\"."),
    (12, None, "'No, you have to watch them, people steal everything here.' Italian uses plural \"rubano\", \"they steal\", without naming a subject whenever English would say \"people steal\"."),
    (13, None, "'And then make seven coffees for the guys.' Words ending in a stressed vowel, like \"caffe\", never change their ending in the plural: one \"caffe\", seven \"caffe\"."),
    (14, None, "'Go Roma!' \"Forza\" literally means \"strength\" or \"force\", and shouting \"Forza\" before a team's name is how Italians cheer."),
]
