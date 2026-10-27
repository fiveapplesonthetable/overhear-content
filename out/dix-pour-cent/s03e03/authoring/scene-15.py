# Authoring module for dix-pour-cent s03e03 scene 15 (cues 737-909).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e03/authoring/scene-15.py --out overhear-content/out/dix-pour-cent/s03e03/scene-15.json

ID = "dix-pour-cent-s03e03-scene-15"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 15
TITLE = "Donner la réplique  (Running Lines)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gerard": "theo", "samy": "marcel"}
LABELS = {"lea": "Camille", "gerard": "Gérard Lanvin", "samy": "Samy"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 737-909. In the studio corridor, Camille reminds Gérard Lanvin that he is the star of the project, "
    "while Gérard generously agrees to run lines with eager newcomer Samy."
)

INTRO = (
    "In the film studio hallway, Camille encourages Gerard Lanvin to assert his authority as the lead star. "
    "When nervous newcomer Samy returns for his final audition, Gerard's warm heart prevails and he agrees to run lines with him. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Samy n'est pas encore engagé.",
     "Samy is not yet hired.",
     [(869, "il est pas encore engagé")], ""),
    ("lea", "C'est toi la vedette, Gérard.",
     "You are the star, Gerard.",
     [(871, "la vedette, Gérard")], ""),
    ("gerard", "Moi, j'ai juste voulu aider.",
     "I only wanted to help.",
     [(872, "Moi, j'ai juste voulu aider")], ""),
    ("gerard", "Je ne peux pas priver ce môme.",
     "I cannot deprive this kid.",
     [(876, "ce môme"), (877, "Je peux pas faire ça")], ""),
    ("lea", "Moi, je pense qu'il va surprendre.",
     "I think he will surprise everyone.",
     [(884, "pense qu'il va nous surprendre")], ""),
    ("lea", "Il peut faire ses cascades lui-même.",
     "He can do his own stunts.",
     [(886, "faire ses cascades lui-même")], ""),
    ("gerard", "Sans blague, c'est formidable pour nous.",
     "No kidding, that is wonderful for us.",
     [(887, "Sans blague")], ""),
    ("samy", "Bonjour! Vous allez bien, Gérard?",
     "Hello! Are you doing well, Gerard?",
     [(893, "Vous allez bien")], ""),
    ("samy", "Je suis désolé pour tout à l'heure.",
     "I am sorry about earlier.",
     [(895, "désolé pour tout à l'heure")], ""),
    ("samy", "Vous êtes venu me donner la réplique?",
     "Did you come to run lines with me?",
     [(896, "la réplique")], ""),
    ("samy", "Vous êtes un porte-bonheur pour moi.",
     "You are a lucky charm for me.",
     [(898, "bonheur pour moi, Gérard")], ""),
    ("lea", "Je pense que Gérard est très occupé.",
     "I think Gerard is very busy.",
     [(899, "Gérard a d'autres choses à faire")], ""),
    ("gerard", "Non, je vais te donner la réplique.",
     "No, I will run lines with you.",
     [(906, "donner, la réplique")], ""),
    ("samy", "Merci beaucoup pour votre aide, Gérard!",
     "Thank you so much for your help, Gerard!",
     [(909, "Merci, Gérard")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Samy is not yet hired.' Camille reminds Gerard that the casting decision is not final. "
     "The negative adverb clarifies the status of the contract."),
    (1, None,
     "'You are the star, Gerard.' She emphasizes his creative authority on the movie project. "
     "The emphatic pronoun confirms his lead status."),
    (2, None,
     "'I only wanted to help.' Gerard admits that his generous intentions created complications. "
     "The restrictive phrase explains his original motive."),
    (3, None,
     "'I cannot deprive this kid.' He refuses to crush a young actor's big opportunity. "
     "The negative modal verb demonstrates his moral integrity."),
    (4, None,
     "'I think he will surprise everyone.' Camille expresses genuine faith in the newcomer's potential. "
     "The cognitive verb conveys optimistic confidence."),
    (5, None,
     "'He can do his own stunts.' She highlights an impressive physical asset of the candidate. "
     "The modal construction details his athletic skills."),
    (6, None,
     "'No kidding, that is wonderful for us.' Gerard reacts with dry irony to the stunt claim. "
     "The idiomatic exclamation expresses sarcastic amusement."),
    (7, None,
     "'Hello! Are you doing well, Gerard?' Samy cheerfully greets the veteran actor. "
     "The friendly greeting opens their conversation politely."),
    (8, None,
     "'I am sorry about earlier.' The newcomer apologizes for his disruptive rehearsal behavior. "
     "The past time adverb points back to the incident."),
    (9, None,
     "'Did you come to run lines with me?' Samy hopes Gerard will rehearse the dialogue again. "
     "The motion verb asks about his willingness to practice."),
    (10, None,
     "'You are a lucky charm for me.' He warmly praises Gerard's reassuring presence on set. "
     "The compound noun pays a heartfelt compliment."),
    (11, None,
     "'I think Gerard is very busy.' Camille tries to protect the star from extra demands. "
     "The opinion verb tactfully intervenes to shield the actor."),
    (12, None,
     "'No, I will run lines with you.' Gerard softens and graciously offers to rehearse the lines. "
     "The future verb confirms his kind decision."),
    (13, None,
     "'Thank you so much for your help, Gerard!' Samy rejoices at the veteran's generous gesture. "
     "The enthusiastic formula expresses profound relief.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Generosity wins out over frustration as Gerard Lanvin steps up to support a young talent. "
    "Listen to the conversation once more in French."
)

CLOSING = ("gerard", "Allez, voyons cette scène ensemble.")
