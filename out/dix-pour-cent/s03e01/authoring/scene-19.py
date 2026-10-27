# Authoring module for dix-pour-cent s03e01 scene 19 (cues 633-667).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-19.py --out out/dix-pour-cent/s03e01/scene-19.json

ID = "dix-pour-cent-s03e01-scene-19"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 19
TITLE = "Le cadeau d'Hicham  (Hicham's Gift)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 633-667. In their apartment, Colette and Andréa unpack an extravagant baby cradle sent by Hicham, "
    "triggering tensions over Hicham's role and the pressures of Andréa's pregnancy."
)

INTRO = (
    "In their apartment, Andrea and Colette find an expensive baby crib delivered to their doorstep. "
    "Colette is unsettled by Hicham's generous intrusion, leading to a tense discussion about their family boundaries. "
    "Listen to the conversation in French first."
)

STORY = [
    ("colette", "Regarde ce grand berceau magnifique!",
     "Look at this magnificent big crib!",
     [(633, "Oh, putain !"), (643, "Puis, franchement, pas mal, le berceau.")], ""),
    ("lea", "Ce cadeau ne vient pas de ma mère.",
     "This gift does not come from my mother.",
     [(636, "C'est pas ma mère, c'est Hicham.")], ""),
    ("colette", "Qui a envoyé ce berceau luxueux?",
     "Who sent this luxurious crib?",
     [(636, "C'est pas ma mère, c'est Hicham.")], ""),
    ("lea", "C'est Hicham pour la petite puce.",
     "It is Hicham for the little flea.",
     [(638, "Pour que la petite puce fasse de beaux rêves.")], ""),
    ("colette", "Hicham prend trop de place chez nous!",
     "Hicham takes up too much room in our home!",
     [(641, "Ça creusait dans notre vie.")], ""),
    ("lea", "Je garde mes distances avec lui.",
     "I keep my distance from him.",
     [(646, "Arrête, je passe mon temps à te tenir à distance.")], ""),
    ("colette", "Tu ne fixes pas de limites claires.",
     "You do not set clear boundaries.",
     [(645, "C'est toi aussi qui est pas claire.")], ""),
    ("lea", "Tu m'en veux pour cette situation?",
     "Are you angry with me for this situation?",
     [(654, "Tu m'en veux, là, en fait ?")], ""),
    ("colette", "Tu savais que ce serait difficile.",
     "You knew that it would be difficult.",
     [(656, "Tu le savais que ce serait compliqué avec Hicham.")], ""),
    ("lea", "J'ai perdu mon poste à New York.",
     "I lost my post in New York.",
     [(661, "T'en avais rien à foutre que je perde mon boulot à New York.")], ""),
    ("lea", "Je le vois tous les jours au travail.",
     "I see him every day at work.",
     [(662, "T'en avais rien à foutre que je me tape sa gueule tous les jours au boulot.")], ""),
    ("colette", "C'est injuste de me reprocher cela.",
     "It is unfair to blame me for that.",
     [(665, "Alors, c'est dégueulasse de me dire ça.")], ""),
    ("colette", "Je veux fonder cette famille avec toi.",
     "I want to build this family with you.",
     [(666, "Je suis heureuse de le faire.")], ""),
    ("lea", "Ce bébé est notre plus belle aventure.",
     "This baby is our most beautiful adventure.",
     [(667, "Le truc le plus fou que j'ai jamais fait de ma vie, c'est grâce à toi.")], "")
]

OPENER = "Let us observe how Andrea and Colette react to an unexpected gift from Hicham."

WALK = [
    (0, None,
     "'Look at this magnificent big crib!' Colette discovers the delivery. "
     "The noun berceau refers to a baby crib or cradle."),
    (1, None,
     "'This gift does not come from my mother.' Andrea clarifies the origin of the item. "
     "The negative structure ne... pas surrounds the verb."),
    (2, None,
     "'Who sent this luxurious crib?' Colette asks with rising suspicion. "
     "The pronoun qui asks who."),
    (3, None,
     "'It is Hicham for the little flea.' Andrea shares Hicham's affectionate note. "
     "The affectionate phrase petite puce means little sweetie."),
    (4, None,
     "'Hicham takes up too much room in our home!' Colette voices her discomfort. "
     "The expression prendre de la place means to take up space."),
    (5, None,
     "'I keep my distance from him.' Andrea defends her daily behavior. "
     "The phrase garder ses distances means to keep at arm's length."),
    (6, None,
     "'You do not set clear boundaries.' Colette expects firmer rules. "
     "The feminine plural noun limites means boundaries."),
    (7, None,
     "'Are you angry with me for this situation?' Andrea senses lingering resentment. "
     "The idiom en vouloir à quelqu'un means to hold a grudge."),
    (8, None,
     "'You knew that it would be difficult.' Colette recalls their prior discussions. "
     "The conditional form serait indicates a future in the past."),
    (9, None,
     "'I lost my post in New York.' Andrea reminds her of personal sacrifices. "
     "The past tense ai perdu comes from perdre."),
    (10, None,
     "'I see him every day at work.' Andrea highlights her daily professional stress. "
     "The adverbial phrase tous les jours means every day."),
    (11, None,
     "'It is unfair to blame me for that.' Colette rejects unfair accusations. "
     "The construction il est followed by de and an infinitive expresses an evaluation."),
    (12, None,
     "'I want to build this family with you.' Colette reaffirms her emotional commitment. "
     "The verb fonder means to found or build."),
    (13, None,
     "'This baby is our most beautiful adventure.' Andrea softens the argument with love. "
     "The superlative structure notre plus belle modifies aventure.")
]

TRANSITION = "Now let us listen to the couple's conversation once more at natural speed."

OUTRO = (
    "Andrea and Colette navigate the emotional and practical complexities of expecting a baby together. "
    "Listen to the dialogue once more in French."
)

CLOSING = ("lea", "Ce bébé est notre plus belle aventure.")
