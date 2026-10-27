# Authoring module for dix-pour-cent s03e04 scene 13 (cues 739-802).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e04/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s03e04/scene-13.json

ID = "dix-pour-cent-s03e04-scene-13"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 13
TITLE = "Le showcase du conservatoire  (The Conservatory Showcase)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "valentin": "theo", "actrice": "emilie"}
LABELS = {"lea": "Camille", "valentin": "Valentin", "actrice": "Élève"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 739-802. At a drama conservatory showcase, Camille scouts promising new talent, "
    "gives her business card to a young actress, and shares a playful encounter with student actor Valentin."
)

INTRO = (
    "At a drama school showcase in Paris, Camille scouts for fresh acting talent. "
    "After congratulating a student actress and handing her a business card, she bumps into a charming young actor named Valentin. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Votre scène avec Créon était magnifique.",
     "Your scene with Creon was magnificent.",
     [(739, "scène avec Créon")], ""),
    ("actrice", "Merci beaucoup, c'est très gentil.",
     "Thank you very much, that is very kind.",
     [(740, "merci, c'est gentil")], ""),
    ("lea", "Est-ce que vous avez un agent?",
     "Do you have an agent?",
     [(741, "Vous avez un agent")], ""),
    ("actrice", "Non, je n'en ai pas encore.",
     "No, I do not have one yet.",
     [(743, "pas encore")], ""),
    ("lea", "Tenez, voici ma carte professionnelle.",
     "Here, this is my business card.",
     [(746, "Ma carte")], ""),
    ("valentin", "Attention, vous m'avez touché l'épaule!",
     "Watch out, you touched my shoulder!",
     [(749, "l'épaule"), (750, "touché")], ""),
    ("lea", "Pardon, je contrôle mal ma force.",
     "Sorry, I do not control my strength well.",
     [(751, "contrôle pas trop ma force")], ""),
    ("lea", "Je suis Camille Valentini, nouvel agent.",
     "I am Camille Valentini, a new agent.",
     [(752, "Camille Valentini, le nouvel agent")], ""),
    ("valentin", "Moi, j'avais un tout petit rôle.",
     "As for me, I had a very small part.",
     [(761, "j'avais qu'un petit rôle")], ""),
    ("lea", "Il n'y a pas de petits rôles.",
     "There are no small parts.",
     [(762, "pas de petit rôle")], ""),
    ("valentin", "Tu es un petit agent prometteur?",
     "You are a promising junior agent?",
     [(769, "T'es un petit agent"), (770, "plein d'avenir")], ""),
    ("lea", "Exactement, je repère les futures stars.",
     "Exactly, I scout future stars.",
     [(771, "repère les futures grosses stars")], ""),
    ("lea", "Attends, comment est-ce que tu t'appelles?",
     "Wait, what is your name?",
     [(778, "Attends, tu t'appelles comment")], ""),
    ("valentin", "Valentin, comme Valentini sans le i.",
     "Valentin, like Valentini without the i.",
     [(779, "Valentin. Comme Valentini, mais sans le i")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Your scene with Creon was magnificent.' Camille compliments a young student after the showcase. "
     "The descriptive adjective praises the dramatic performance."),
    (1, None,
     "'Thank you very much, that is very kind.' The young actress accepts the praise politely. "
     "The polite expression shows gratitude."),
    (2, None,
     "'Do you have an agent?' Camille inquires about her professional representation. "
     "The direct question explores potential representation."),
    (3, None,
     "'No, I do not have one yet.' The student confirms she is currently unrepresented. "
     "The temporal adverb indicates availability for signing."),
    (4, None,
     "'Here, this is my business card.' Camille hands over her contact details. "
     "The demonstrative phrase initiates a professional connection."),
    (5, None,
     "'Watch out, you touched my shoulder!' A handsome student actor playfully protests a bump. "
     "The exclamation calls attention to the collision."),
    (6, None,
     "'Sorry, I do not control my strength well.' Camille jokingly apologizes for the contact. "
     "The light apology eases the encounter."),
    (7, None,
     "'I am Camille Valentini, a new agent.' She introduces herself with her agency title. "
     "The proper noun states her professional identity."),
    (8, None,
     "'As for me, I had a very small part.' Valentin downplays his brief performance in the show. "
     "The limiting phrase expresses modest experience."),
    (9, None,
     "'There are no small parts.' Camille quotes the classic theatre maxim. "
     "The negative existential phrase encourages the student."),
    (10, None,
     "'You are a promising junior agent?' Valentin teasingly asks about her career ambition. "
     "The playful question continues their friendly banter."),
    (11, None,
     "'Exactly, I scout future stars.' Camille affirms her talent scouting mission. "
     "The professional phrase defines her purpose at the conservatory."),
    (12, None,
     "'Wait, what is your name?' She asks for his identity before parting. "
     "The familiar question seeks his first name."),
    (13, None,
     "'Valentin, like Valentini without the i.' He reveals the witty resemblance to her surname. "
     "The humorous comparison seals their connection.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Scouting drama showcases brings unexpected encounters and exciting new connections for an ambitious talent agent. "
    "Listen to the conversation once more in French."
)

CLOSING = ("valentin", "On va se revoir très bientôt.")
