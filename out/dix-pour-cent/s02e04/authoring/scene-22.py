# Authoring module for dix-pour-cent-s02e04-scene-22.
ID = 'dix-pour-cent-s02e04-scene-22'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 4
SCENE = 22
TITLE = 'Confrontation dans le couloir  (Hallway Confrontation)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
VOICES = {'narrator': 'sky', 'camille': 'emilie', 'gabriel': 'theo', 'hicham': 'marcel'}
LABELS = {'camille': 'Camille', 'gabriel': 'Gabriel', 'hicham': 'Hicham'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E04'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e04.fr.dual.srt'
INTRO = "In the bustling hallway of ASK, Gabriel steps out of his office to ask for quiet as colleagues chat nearby. A tense exchange between Gabriel, Hicham, and Camille reveals ongoing friction over power and personal loyalties at the agency. Listen to the scene in French first. Don't worry about catching every word."
OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."
TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."
OUTRO = "Gabriel continues to worry about Hicham's true intentions despite Camille's calming words. Remember the essential French idiom for holding a grudge against someone: en vouloir a quelqu'un. See you next time!"
CLOSING = ('camille', 'Bonne soirée!')
STORY = [
    ('gabriel', 'Je vous entends depuis mon bureau.', 'I can hear you from my office.', [(624, 'Je vous entends ricaner depuis mon bureau.')], ''),
    ('camille', 'Bonjour, vous pourriez être plus discrets?', 'Hello, could you be more discreet?', [(628, 'Bonjour. Vous pourriez être plus discrets ?')], ''),
    ('hicham', 'On se détend juste un petit moment.', 'We are just relaxing for a moment.', [(631, 'On se détend juste un moment.')], ''),
    ('hicham', 'Si ça dérange, je peux partir.', 'If it bothers you, I can leave.', [(632, 'Si ça vous dérange, je pars.')], ''),
    ('gabriel', 'Ne prenez pas les choses comme ça.', 'Do not take things like that.', [(633, '-Prenez pas ça comme ça.')], ''),
    ('hicham', "J'ai l'habitude de ces remarques.", 'I am used to these remarks.', [(633, "-J'ai l'habitude.")], ''),
    ('hicham', 'Au revoir, Camille. Bonne journée.', 'Goodbye, Camille. Have a good day.', [(634, '-Au revoir, Camille. -Au revoir.'), (635, 'Et bonne chance avec Adjani.')], ''),
    ('camille', 'Au revoir Hicham, à très bientôt.', 'Goodbye Hicham, see you very soon.', [(634, '-Au revoir.')], ''),
    ('gabriel', "Qu'est-ce qu'il a contre nous?", 'What does he have against us?', [(636, "-Qu'est-ce qu'il a ?")], ''),
    ('camille', 'Je ne sais pas du tout.', 'I do not know at all.', [(636, '-Je sais pas.')], ''),
    ('gabriel', "Il m'en veut encore beaucoup?", 'Is he still very angry with me?', [(637, "Il m'en veut encore ?")], ''),
    ('camille', "Il t'a quand même rendu service.", 'He still did you a favor.', [(638, "Il n'a pas hésité à te rendre service.")], ''),
    ('gabriel', "Il l'a fait pour toi seulement.", 'He did it for you only.', [(639, "Il l'a fait pour toi, pas pour moi.")], ''),
    ('camille', "Arrête d'imaginer le pire, Gabriel.", 'Stop imagining the worst, Gabriel.', [(638, "Il n'a pas hésité à te rendre service.")], ''),
]
WALK = [
    (0, None, "'I can hear you from my office.' Gabriel complains about the noisy laughter drifting down the corridor. Listen for the expression meaning 'hear', which leads naturally into 'office'."),
    (1, None, "'Hello, could you be more discreet?' Camille asks the men to keep their voices down near client offices. Listen for the expression meaning 'hello', which leads naturally into 'discreet'."),
    (2, None, "'We are just relaxing for a moment.' Hicham defends their brief pause in the work day. Listen for the expression meaning 'relax', which leads naturally into 'moment'."),
    (3, None, "'If it bothers you, I can leave.' The touchy executive threatens to walk away from the area. The key word here means 'bothers', paired with 'to leave' to make the point clear."),
    (4, None, "'Do not take things like that.' Gabriel urges his partner not to react defensively. The adverb meaning 'not' sharpens the verb for 'take' here."),
    (5, None, "'I am used to these remarks.' Hicham shrugs off the criticism with weary indifference. Listen for the expression meaning 'I have', which leads naturally into 'remarks'."),
    (6, None, "'Goodbye, Camille. Have a good day.' He bids a polite farewell to the young assistant. The adjective meaning 'good' agrees in gender and number with the noun's noun 'goodbye'."),
    (7, None, "'Goodbye Hicham, see you very soon.' Camille responds courteously as he departs down the hall. The expression a tres bientot means see you very soon."),
    (8, None, "'What does he have against us?' Gabriel wonders why tension lingers between the agency partners. Listen for the expression meaning 'has', which leads naturally into 'has'."),
    (9, None, "'I do not know at all.' Camille declines to take sides in the ongoing executive friction. The verb meaning 'know' anchors the whole remark."),
    (10, None, "'Is he still very angry with me?' Gabriel fears that past disagreements have poisoned their working relationship. Listen for the expression meaning 'wants', which leads naturally into 'a lot'."),
    (11, None, "'He still did you a favor.' The assistant points out that Hicham helped out despite their differences. Camille opens with the word for 'has' and lands on 'service' at the close."),
    (12, None, "'He did it for you only.' Gabriel remains convinced that Hicham acts solely out of personal loyalty to Camille. Gabriel opens with the word for 'has' and lands on 'only' at the close."),
    (13, None, "'Stop imagining the worst, Gabriel.' Camille encourages her colleague to stop overthinking every interaction. Camille opens with the word for 'stop' and lands on 'worst' at the close."),
]
