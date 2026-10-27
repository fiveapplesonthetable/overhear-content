# Authoring module for dix-pour-cent s04e05 scene 17 (cues 736-742).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e05/authoring/scene-17.py --out overhear-content/out/dix-pour-cent/s04e05/scene-17.json

ID = "dix-pour-cent-s04e05-scene-17"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 17
TITLE = "L'aveu d'Hervé  (Hervé's Confession)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Hervé", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 736-742. In the agency hallway, Hervé nervously confesses to Gabriel that he played a role in a "
    "feature film, only to discover that Élise Formain already leaked his secret to everyone."
)

INTRO = (
    "In the hallway at ASK, Hervé stops Gabriel to make a nervous confession about his secret acting career. "
    "However, Gabriel reveals that the secret is already out across the agency. "
    "Let's listen to their exchange in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Gabriel, vous avez une minute?",
     "Gabriel, do you have a minute?",
     [(736, "Gabriel")], "Hervé stops Gabriel in the hallway"),
    ("gabriel", "Oui, qu'est-ce qui se passe?",
     "Yes, what is going on?",
     [(737, "Quoi")], "Gabriel pauses to listen"),
    ("lea", "J'ai quelque chose à vous avouer.",
     "I have something to confess to you.",
     [(737, "J'ai quelque chose à vous avouer")], "Hervé looks nervous"),
    ("gabriel", "Quoi donc? Rien de grave?",
     "What then? Nothing serious?",
     [(737, "Quoi"), (738, "Rien de grave")], "Gabriel asks with concern"),
    ("lea", "Non, mais c'est très délicat.",
     "No, but it is very delicate.",
     [], "Hervé hesitates"),
    ("gabriel", "Allez, parlez, je vous écoute!",
     "Come on, speak, I am listening to you!",
     [], "Gabriel urges him to speak"),
    ("lea", "J'ai joué un rôle au cinéma.",
     "I played a role in a movie.",
     [(739, "J'ai joué un rôle")], "Hervé makes his confession"),
    ("lea", "J'ai tourné dans un vrai film!",
     "I acted in a real movie!",
     [(739, "dans un film")], "Hervé admits his secret"),
    ("gabriel", "Le film de Donzelli? Je sais.",
     "The Donzelli movie? I know.",
     [(740, "Le Donzelli? Je sais")], "Gabriel is completely unsurprised"),
    ("gabriel", "Élise me l'a déjà dit.",
     "Elise already told me.",
     [(740, "Élise me l'a dit")], "Gabriel reveals his source"),
    ("lea", "Quoi? Ce n'est pas vrai!",
     "What? That is not true!",
     [], "Hervé is shocked"),
    ("lea", "Elle devait garder le secret!",
     "She was supposed to keep the secret!",
     [(741, "garder le secret")], "Hervé is outraged at the leak"),
    ("gabriel", "Mon Dieu, vous êtes tellement naïf!",
     "My God, you are so naive!",
     [(742, "Mon Dieu, vous êtes")], "Gabriel shakes his head"),
    ("lea", "On ne peut faire confiance à personne.",
     "You cannot trust anyone.",
     [], "Hervé sighs in disappointment"),
]

WALK = [
    (0, None,
     "'Gabriel, do you have a minute?' Hervé approaches his boss with a hesitant expression. "
     "The question 'vous avez une minute' politely asks for someone's time."),
    (1, None,
     "'Yes, what is going on?' Gabriel stops and gives his assistant his attention. "
     "The interrogative phrase 'qu'est-ce qui se passe' asks what is happening."),
    (2, None,
     "'I have something to confess to you.' Hervé prepares to admit his secret acting job. "
     "The verb 'avouer' means to confess or admit."),
    (3, None,
     "'What then? Nothing serious?' Gabriel hopes there is no crisis at the agency. "
     "The phrase 'rien de grave' asks whether anything bad happened."),
    (4, None,
     "'No, but it is very delicate.' Hervé tries to soften the news before speaking. "
     "The adjective 'delicat' describes a sensitive matter."),
    (5, None,
     "'Come on, speak, I am listening to you!' Gabriel impatiently gestures for him to get to the point. "
     "The imperative 'parlez' is the polite command form."),
    (6, None,
     "'I played a role in a movie.' Hervé finally reveals his appearance on the big screen. "
     "The noun 'role' refers to a character part."),
    (7, None,
     "'I acted in a real movie!' Hervé emphasizes that it was a legitimate feature production. "
     "The verb 'tourner' means to shoot or act in a film."),
    (8, None,
     "'The Donzelli movie? I know.' Gabriel immediately names the director without surprise. "
     "The verb phrase 'je sais' means I know."),
    (9, None,
     "'Elise already told me.' Gabriel explains how the news reached him first. "
     "The adverb 'deja' indicates that something already happened."),
    (10, None,
     "'What? That is not true!' Hervé is stunned that his confidence was betrayed. "
     "The negative clause 'ce n'est pas vrai' expresses disbelief."),
    (11, None,
     "'She was supposed to keep the secret!' Hervé complains that Elise promised not to tell. "
     "The expression 'garder le secret' means to keep a secret."),
    (12, None,
     "'My God, you are so naive!' Gabriel teases Hervé for trusting a rival agency head. "
     "The adjective 'naif' means gullible or innocent."),
    (13, None,
     "'You cannot trust anyone.' Hervé laments the lack of discretion in the film industry. "
     "The phrase 'faire confiance' means to trust."),
]

OUTRO = (
    "Hervé realizes to his dismay that his secret acting debut is already common knowledge at ASK. "
    "Gabriel laughs off his assistant's naivety before heading back to his office. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("gabriel", "Revenez au travail!")
