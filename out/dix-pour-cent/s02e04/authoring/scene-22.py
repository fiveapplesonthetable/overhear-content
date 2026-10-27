# Authoring module for dix-pour-cent s02e04 scene 22 (cues 624-639).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-22.py --out out/dix-pour-cent/s02e04/scene-22.json

ID = "dix-pour-cent-s02e04-scene-22"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 22
TITLE = "Confrontation dans le couloir  (Hallway Confrontation)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "hicham": "marcel"}
LABELS = {"lea": "Camille", "gabriel": "Gabriel", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 624-639. Gabriel confronts Hicham in the hallway about his noisy interruptions during the interviews. "
    "Camille tries to mediate between the two agents."
)

INTRO = (
    "In the bustling hallway of ASK, Gabriel steps out of his office to ask for quiet as colleagues chat nearby. "
    "A tense exchange between Gabriel, Hicham, and Camille reveals ongoing friction over power and personal loyalties at the agency. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("gabriel", "Je vous entends depuis mon bureau.",
     "I can hear you from my office.",
     [(624, "Je vous entends ricaner depuis mon bureau.")], ""),
    ("lea", "Bonjour, vous pourriez être plus discrets?",
     "Hello, could you be more discreet?",
     [(628, "Bonjour. Vous pourriez être plus discrets ?")], ""),
    ("hicham", "On se détend juste un petit moment.",
     "We are just relaxing for a moment.",
     [(631, "On se détend juste un moment.")], ""),
    ("hicham", "Si ça dérange, je peux partir.",
     "If it bothers you, I can leave.",
     [(632, "Si ça vous dérange, je pars.")], ""),
    ("gabriel", "Ne prenez pas les choses comme ça.",
     "Do not take things like that.",
     [(633, "-Prenez pas ça comme ça.")], ""),
    ("hicham", "J'ai l'habitude de ces remarques.",
     "I am used to these remarks.",
     [(633, "-J'ai l'habitude.")], ""),
    ("hicham", "Au revoir, Camille. Bonne journée.",
     "Goodbye, Camille. Have a good day.",
     [(634, "-Au revoir, Camille. -Au revoir."), (635, "Et bonne chance avec Adjani.")], ""),
    ("lea", "Au revoir Hicham, à très bientôt.",
     "Goodbye Hicham, see you very soon.",
     [(634, "-Au revoir.")], ""),
    ("gabriel", "Qu'est-ce qu'il a contre nous?",
     "What does he have against us?",
     [(636, "-Qu'est-ce qu'il a ?")], ""),
    ("lea", "Je ne sais pas du tout.",
     "I do not know at all.",
     [(636, "-Je sais pas.")], ""),
    ("gabriel", "Il m'en veut encore beaucoup?",
     "Is he still very angry with me?",
     [(637, "Il m'en veut encore ?")], ""),
    ("lea", "Il t'a quand même rendu service.",
     "He still did you a favor.",
     [(638, "Il n'a pas hésité à te rendre service.")], ""),
    ("gabriel", "Il l'a fait pour toi seulement.",
     "He did it for you only.",
     [(639, "Il l'a fait pour toi, pas pour moi.")], ""),
    ("lea", "Arrête d'imaginer le pire, Gabriel.",
     "Stop imagining the worst, Gabriel.",
     [(638, "Il n'a pas hésité à te rendre service.")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'I can hear you from my office.' Gabriel complains about the noisy laughter drifting down the corridor. "
     "The verb entends indicates hearing sensory input."),
    (1, None,
     "'Hello, could you be more discreet?' Camille asks the men to keep their voices down near client offices. "
     "The conditional pourriez softens a polite request."),
    (2, None,
     "'We are just relaxing for a moment.' Hicham defends their brief pause in the work day. "
     "The reflexive verb se detend means to unwind."),
    (3, None,
     "'If it bothers you, I can leave.' The touchy executive threatens to walk away from the area. "
     "The verb derange means to disturb or bother."),
    (4, None,
     "'Do not take things like that.' Gabriel urges his partner not to react defensively. "
     "The negative imperative ne prenez pas advises moderation."),
    (5, None,
     "'I am used to these remarks.' Hicham shrugs off the criticism with weary indifference. "
     "The idiom avoir l'habitude means to be accustomed to something."),
    (6, None,
     "'Goodbye, Camille. Have a good day.' He bids a polite farewell to the young assistant. "
     "The formulaic farewell au revoir is standard in professional settings."),
    (7, None,
     "'Goodbye Hicham, see you very soon.' Camille responds courteously as he departs down the hall. "
     "The expression a tres bientot means see you very soon."),
    (8, None,
     "'What does he have against us?' Gabriel wonders why tension lingers between the agency partners. "
     "The preposition contre denotes opposition or resentment."),
    (9, None,
     "'I do not know at all.' Camille declines to take sides in the ongoing executive friction. "
     "The phrase du tout intensifies the negation."),
    (10, None,
     "'Is he still very angry with me?' Gabriel fears that past disagreements have poisoned their working relationship. "
     "The idiomatic structure en vouloir a quelqu'un means to hold a grudge against someone."),
    (11, None,
     "'He still did you a favor.' The assistant points out that Hicham helped out despite their differences. "
     "The phrase rendre service means to do someone a favor."),
    (12, None,
     "'He did it for you only.' Gabriel remains convinced that Hicham acts solely out of personal loyalty to Camille. "
     "The adverb seulement restricts the scope of the action."),
    (13, None,
     "'Stop imagining the worst, Gabriel.' Camille encourages her colleague to stop overthinking every interaction. "
     "The superlative le pire refers to the worst possible outcome."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Gabriel continues to worry about Hicham's true intentions despite Camille's calming words. "
    "Remember the essential French idiom for holding a grudge against someone: en vouloir a quelqu'un."
)

CLOSING = ("lea", "Arrête d'imaginer le pire, Gabriel.")
