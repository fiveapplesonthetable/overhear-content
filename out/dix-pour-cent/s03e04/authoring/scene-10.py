# Authoring module for dix-pour-cent s03e04 scene 10 (cues 672-693).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e04/authoring/scene-10.py --out overhear-content/out/dix-pour-cent/s03e04/scene-10.json

ID = "dix-pour-cent-s03e04-scene-10"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 10
TITLE = "Détour pour la radio  (Detour for the Radio)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Isabelle Huppert", "mathias": "Mathias Barneville"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 672-693. Mathias drives Isabelle Huppert to her night shoot, acting as private chauffeur. "
    "When Laure Adler calls about a live radio interview that Isabelle completely forgot, Mathias panics, "
    "but Isabelle insists on taking a quick twenty-minute detour. Adapted for A1 French."
)

INTRO = (
    "While Mathias drives Isabelle Huppert across Paris to her night shoot, an unexpected call throws their schedule into chaos. "
    "Laure Adler is waiting for a live radio broadcast that Isabelle completely forgot. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
    ("lea", "C'est très beau, cette solidarité entre agents.",
     "That is very nice, this solidarity between agents.",
     [(672, "drôlement beau, cette solidarité entre agents")], "Praising solidarity"),
    ("mathias", "Vous conduire me fait vraiment plaisir, Isabelle.",
     "Driving you gives me real pleasure, Isabelle.",
     [(674, "Ça me fait plaisir")], "Offering chauffeur service"),
    ("lea", "Vous aimez jouer les chauffeurs privés?",
     "You like playing private chauffeurs?",
     [(675, "jouer les chauffeurs privés")], "Joking about driving"),
    ("mathias", "Il y a de l'eau et des bonbons.",
     "There is water and sweets.",
     [(676, "de l'eau et des bonbons")], "Offering refreshments"),
    ("lea", "Allô? Oui, je suis en route!",
     "Hello? Yes, I am on my way!",
     [(677, "Allô ? Oui, oui, bien sûr"), (678, "je suis en route")], "Answering urgent phone call"),
    ("lea", "J'arrive dans cinq minutes pour l'émission.",
     "I arrive in five minutes for the broadcast.",
     [(679, "je suis là dans cinq minutes")], "Promising quick arrival"),
    ("mathias", "Ce sont les producteurs américains au téléphone?",
     "Is that the American producers on the phone?",
     [(681, "C'est les Américains ?")], "Inquiring about call"),
    ("lea", "Non, c'était la journaliste Laure Adler.",
     "No, that was the journalist Laure Adler.",
     [(682, "Non, c'était Laura Adler")], "Identifying caller"),
    ("lea", "Elle m'attend en direct à la radio.",
     "She is waiting for me live on the radio.",
     [(683, "Elle m'attend pour faire son émission en direct à la radio")], "Explaining radio interview"),
    ("lea", "Cette interview est sortie de ma tête!",
     "This interview slipped my mind!",
     [(684, "C'est prévu"), (685, "Ça m'est complètement sorti de la tête")], "Confessing oversight"),
    ("mathias", "Ce n'est pas possible ce soir, Isabelle!",
     "That is not possible tonight, Isabelle!",
     [(686, "Ah non, mais c'est pas possible, ça, Isabelle")], "Panicking over schedule"),
    ("lea", "Cette émission prendra seulement vingt minutes.",
     "This show will take only twenty minutes.",
     [(688, "Ça prendra vingt minutes, tout au plus")], "Minimizing interview duration"),
    ("lea", "Je ne peux pas planter une amie.",
     "I cannot stand up a friend.",
     [(689, "Mais je peux pas planter Laura Adler"), (690, "Ça se fait pas")], "Refusing to cancel"),
    ("mathias", "Nous allons être très en retard!",
     "We are going to be very late!",
     [(688, "tout au plus")], "Fearing production delays"),
]

WALK = [
    (0, None,
     "'That is very nice, this solidarity between agents.' Isabelle compliments Mathias on helping out. "
     "The preposition 'entre' denotes relations between individuals."),
    (1, None,
     "'Driving you gives me real pleasure, Isabelle.' Mathias assures his client that he is happy to assist. "
     "The verb 'conduire' means to drive."),
    (2, None,
     "'You like playing private chauffeurs?' Isabelle teases Mathias about his driving role. "
     "The verb 'jouer' idiomatically means to act as or play the part of."),
    (3, None,
     "'There is water and sweets.' Mathias points out the comforts in the back of the car. "
     "The noun 'bonbon' refers to candy or sweets."),
    (4, None,
     "'Hello? Yes, I am on my way!' Isabelle answers an unexpected phone call. "
     "The expression 'etre en route' means to be on one's way."),
    (5, None,
     "'I arrive in five minutes for the broadcast.' Isabelle promises to reach the studio quickly. "
     "The noun 'emission' denotes a broadcast or show."),
    (6, None,
     "'Is that the American producers on the phone?' Mathias worries that the American crew is calling. "
     "The demonstrative 'ce sont' introduces plural subjects."),
    (7, None,
     "'No, that was the journalist Laure Adler.' Isabelle identifies the prominent cultural interviewer. "
     "The demonstrative phrase 'c'etait' refers to a past situation."),
    (8, None,
     "'She is waiting for me live on the radio.' Isabelle explains the broadcast format. "
     "The phrase 'en direct' means live on air."),
    (9, None,
     "'This interview slipped my mind!' Isabelle admits she forgot the appointment. "
     "The idiom 'sortir de la tete' means to slip one's mind."),
    (10, None,
     "'That is not possible tonight, Isabelle!' Mathias panics over their tight schedule. "
     "The negation 'ce n'est pas' refutes feasibility."),
    (11, None,
     "'This show will take only twenty minutes.' Isabelle downplays the detour duration. "
     "The adverb 'seulement' restricts the amount of time."),
    (12, None,
     "'I cannot stand up a friend.' Isabelle refuses to ditch the host. "
     "The colloquial verb 'planter' means to stand someone up."),
    (13, None,
     "'We are going to be very late!' Mathias stresses the impending production delay. "
     "The expression 'etre en retard' means to be late."),
]

OUTRO = (
    "Mathias discovers that managing Isabelle Huppert means coping with whirlwind artistic detours at any moment. "
    "Despite the strict film schedule, the radio appearance cannot be skipped. "
    "Now let's listen to the scene once more."
)

CLOSING = ("mathias", "Nous allons être très en retard!")
