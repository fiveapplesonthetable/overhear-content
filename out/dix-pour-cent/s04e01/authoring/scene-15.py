# Authoring module for dix-pour-cent s04e01 scene 15 (cues 732-815).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e01/authoring/scene-15.py --out overhear-content/out/dix-pour-cent/s04e01/scene-15.json

ID = "dix-pour-cent-s04e01-scene-15"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 15
TITLE = "La fausse jambe cassée  (The Fake Broken Leg)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "charlotte": "emilie", "paco": "theo"}
LABELS = {"lea": "Andréa", "charlotte": "Charlotte", "paco": "Paco"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 732-815. At Charlotte Gainsbourg's apartment, Andréa invents a broken leg excuse "
    "to pull Charlotte from an awful sci-fi film, calling in prop master Paco to fit a fake plaster cast."
)

INTRO = (
    "At Charlotte Gainsbourg's apartment, Andrea hatches an audacious scheme to rescue her star client from an awful sci-fi film. "
    "To avoid hurting her director friend Oscar, Andrea brings in prop master Paco to fit Charlotte with a fake plaster cast before Oscar arrives. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Ce film de science-fiction sera un navet.",
     "This science fiction movie will be a dud.",
     [(762, "ça va être un navet total")], ""),
    ("charlotte", "Je veux faire ce film par amitié.",
     "I want to do this film out of friendship.",
     [(764, "j'en ferai un par amitié")], ""),
    ("lea", "Je ne peux pas te laisser faire.",
     "I cannot let you do that.",
     [(765, "Je ne peux pas te laisser faire")], ""),
    ("lea", "J'ai dit à Oscar que tu étais blessée.",
     "I told Oscar that you were injured.",
     [(774, "Elle est à l'hôpital. Elle s'est cassé la jambe")], ""),
    ("charlotte", "Quoi, tu lui as dit cela?",
     "What, you told him that?",
     [(776, "Pourquoi t'as dû lui dire ça")], ""),
    ("lea", "Oui, tu as une jambe cassée!",
     "Yes, you have a broken leg!",
     [(774, "s'est cassé la jambe")], ""),
    ("charlotte", "Mais Oscar arrive chez moi maintenant!",
     "But Oscar is arriving at my place now!",
     [(781, "Il arrête pas de m'envoyer des SMS")], ""),
    ("lea", "Paco est là pour nous aider.",
     "Paco is here to help us.",
     [(783, "Regardez, j'ai tout prévu. Paco")], ""),
    ("paco", "Bonjour, Charlotte, c'est un grand honneur.",
     "Hello, Charlotte, it is a great honor.",
     [(787, "Bonjour, c'est un honneur")], ""),
    ("paco", "Je suis accessoiriste pour le cinéma.",
     "I am a prop master for cinema.",
     [(790, "il est aussi accessoiriste")], ""),
    ("paco", "Voici un faux plâtre très élégant.",
     "Here is a very elegant fake cast.",
     [(799, "Élégant")], ""),
    ("charlotte", "C'est parfait, enfilons cette fausse botte!",
     "It is perfect, let us slip on this fake boot!",
     [(800, "j'aime bien le plâtre"), (812, "C'est comme une botte")], ""),
    ("lea", "Attention, Oscar sonne à l'interphone!",
     "Watch out, Oscar is ringing the intercom!",
     [(805, "l'interphone")], ""),
    ("charlotte", "Vite, assieds-moi sur le canapé!",
     "Quickly, sit me down on the sofa!",
     [(809, "Assieds-toi, là"), (810, "dépêche-toi")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'This science fiction movie will be a dud.' Andrea gives her blunt opinion on the amateurish script. "
     "The future tense warns of artistic failure."),
    (1, None,
     "'I want to do this film out of friendship.' Charlotte defends her loyalty to her childhood pal. "
     "The prepositional phrase highlights her loyalty."),
    (2, None,
     "'I cannot let you do that.' The agent firmly protects her star's professional standing. "
     "The modal negation refuses an artistic blunder."),
    (3, None,
     "'I told Oscar that you were injured.' Andrea reveals the white lie she invented to save the situation. "
     "The past tense confesses the trick."),
    (4, None,
     "'What, you told him that?' Charlotte reacts with shock at her agent's bold fabrication. "
     "The short question expresses disbelief."),
    (5, None,
     "'Yes, you have a broken leg!' Andrea commits to the medical cover story. "
     "The exclamation details the fake diagnosis."),
    (6, None,
     "'But Oscar is arriving at my place now!' Panic strikes as the director approaches the building. "
     "The present tense stresses the immediate emergency."),
    (7, None,
     "'Paco is here to help us.' The agent introduces her clever solution to the problem. "
     "The simple statement presents their savior."),
    (8, None,
     "'Hello, Charlotte, it is a great honor.' The prop specialist politely greets the acclaimed actress. "
     "The courteous noun phrase conveys genuine admiration."),
    (9, None,
     "'I am a prop master for cinema.' Paco explains his artistic trade with quiet pride. "
     "The professional noun clarifies his expertise."),
    (10, None,
     "'Here is a very elegant fake cast.' He presents the best medical prop from his collection. "
     "The positive adjective flatters her style."),
    (11, None,
     "'It is perfect, let us slip on this fake boot!' Charlotte embraces the comical subterfuge with enthusiasm. "
     "The imperative verb initiates the disguise."),
    (12, None,
     "'Watch out, Oscar is ringing the intercom!' Andrea sounds the alarm as the guest arrives at the door. "
     "The alert heightens the comedic tension."),
    (13, None,
     "'Quickly, sit me down on the sofa!' Charlotte gets into position to play the role of an invalid. "
     "The imperative verb completes the scene.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "With a fake plaster cast and seconds to spare, Charlotte and Andrea prepare for Oscar's sudden inspection. "
    "Listen to the conversation once more in French."
)

CLOSING = ("charlotte", "Cette fausse blessure est presque magique.")
