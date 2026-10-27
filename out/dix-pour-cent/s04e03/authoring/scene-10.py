# Authoring module for dix-pour-cent s04e03 scene 10 (cues 421-453).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e03/authoring/scene-10.py --out overhear-content/out/dix-pour-cent/s04e03/scene-10.json

ID = "dix-pour-cent-s04e03-scene-10"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 10
TITLE = "Coincés dans l'ascenseur  (Stuck in the Elevator)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "elise": "emilie"}
LABELS = {"lea": "Gabriel", "elise": "Élise"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 405-434. Gabriel tries to escape from Élise Formain by slipping into the ASK elevator, "
    "but she forces her way inside to demand a truce. When the lift abruptly stalls between floors, "
    "Gabriel succumbs to violent claustrophobia and desperately messages colleagues for help."
)

INTRO = (
    "Determined to avoid his new colleague Elise Formain, Gabriel Sarda dashes into the ASK elevator. "
    "Elise slips between the closing doors at the last second, cornering Gabriel to demand a fresh start. "
    "When the cabin suddenly screeches to a halt between floors, a terrifying ordeal begins for the claustrophobic agent. "
    "Let's listen to their predicament in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Pourquoi tu montes dans cet ascenseur?",
     "Why do you get in this elevator?",
     [(406, "Pas maintenant !"), (407, "Attends !")], "Gabriel questions her entrance"),
    ("elise", "Nous devons parler de notre travail.",
     "We must talk about our work.",
     [(411, "Tu ne crois pas qu'on devrait se parler")], "Élise demands a conversation"),
    ("lea", "L'atmosphère est déjà très claire.",
     "The atmosphere is already very clear.",
     [(416, "L'atmosphère est très claire")], "Gabriel insists everything is fine"),
    ("elise", "Tu me détestes depuis mon arrivée.",
     "You hate me since my arrival.",
     [(412, "mon arrivée te reste en travers de la gorge")], "Élise confronts his hostility"),
    ("lea", "Tu as volé nos meilleurs clients!",
     "You stole our best clients!",
     [(415, "clarifier l'atmosphère")], "Gabriel brings up past betrayals"),
    ("elise", "C'est le jeu de notre métier.",
     "That is the game of our profession.",
     [(414, "les conditions du dialogue")], "Élise defends aggressive competition"),
    ("lea", "Appuie sur le bouton pour descendre.",
     "Press the button to go down.",
     [(408, "Fermeture des portes")], "Gabriel wants the ride to end"),
    ("elise", "Attends, l'ascenseur s'arrête tout seul!",
     "Wait, the elevator stops by itself!",
     [(421, "Merde, non")], "Élise notices the elevator halting"),
    ("lea", "Non, nous sommes totalement bloqués!",
     "No, we are completely blocked!",
     [(422, "Oh, non")], "Gabriel realizes they are stuck"),
    ("elise", "Ne panique pas, ce n'est rien.",
     "Do not panic, it is nothing.",
     [(424, "Ça va ?")], "Élise tries to maintain calm"),
    ("lea", "Je suis extrêmement claustrophobe!",
     "I am extremely claustrophobic!",
     [(426, "claustrophobe"), (427, "Très claustrophobe")], "Gabriel confesses his phobia"),
    ("elise", "Respire calmement, ils vont nous aider.",
     "Breathe calmly, they will help us.",
     [(429, "Allez")], "Élise offers reassuring words"),
    ("lea", "J'envoie un message d'urgence à Andréa.",
     "I send an emergency text to Andrea.",
     [(431, "À l'aide, je suis coincée")], "Gabriel desperately texts for help"),
    ("elise", "Nous allons passer du temps ensemble!",
     "We are going to spend time together!",
     [(428, "C'est nul")], "Élise notes the forced companionship"),
]

WALK = [
    (0, None,
     "'Why do you get in this elevator?' Gabriel demands to know why Elise followed him into the elevator. "
     "The masculine noun 'ascenseur' means elevator or lift."),
    (1, None,
     "'We must talk about our work.' Elise insists on establishing an open dialogue with her reluctant peer. "
     "The modal verb 'devons' expresses duty or necessity."),
    (2, None,
     "'The atmosphere is already very clear.' Gabriel coldly dismisses her proposal to clear the air. "
     "The adverb 'deja' means already."),
    (3, None,
     "'You hate me since my arrival.' Elise bluntly confronts Gabriel about his lingering resentment. "
     "The verb 'detester' means to hate or loathe."),
    (4, None,
     "'You stole our best clients!' Gabriel accuses her of poaching ASK talent while at StarMedia. "
     "The past participle 'vole' comes from the verb 'voler'."),
    (5, None,
     "'That is the game of our profession.' Elise defends competitive poaching as standard industry reality. "
     "The masculine noun 'metier' means profession or line of work."),
    (6, None,
     "'Press the button to go down.' Gabriel just wants the elevator to reach the lobby so he can leave. "
     "The verb 'appuyer' means to press."),
    (7, None,
     "'Wait, the elevator stops by itself!' Elise notices the machinery shudder and stall. "
     "The reflexive verb 's'arreter' means to stop."),
    (8, None,
     "'No, we are completely blocked!' Gabriel realizes the cabin is trapped between floors. "
     "The adjective 'bloques' means stuck or blocked."),
    (9, None,
     "'Do not panic, it is nothing.' Elise tries to reassure her visibly shaking colleague. "
     "The negative imperative 'ne panique pas' means do not panic."),
    (10, None,
     "'I am extremely claustrophobic!' Gabriel reveals his severe phobia of confined spaces. "
     "The adjective 'claustrophobe' describes someone who fears enclosed areas."),
    (11, None,
     "'Breathe calmly, they will help us.' Elise instructs Gabriel to steady his breathing. "
     "The imperative 'respire' comes from the verb 'respirer'."),
    (12, None,
     "'I send an emergency text to Andrea.' Gabriel frantically pulls out his phone to seek rescue. "
     "The feminine noun 'urgence' means emergency."),
    (13, None,
     "'We are going to spend time together!' Elise ironically remarks that fate has forced them to bond. "
     "The near-future phrase 'allons passer' means are going to spend."),
]

OUTRO = (
    "Trapped inside the broken elevator, Gabriel struggles to breathe as panic overtakes him. "
    "Elise realizes she must keep him calm until the building technicians arrive to pry open the doors. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Sortez-nous de là tout de suite!")
