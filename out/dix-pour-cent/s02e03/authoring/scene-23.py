# Authoring module for dix-pour-cent s02e03 scene 23 (cues 595-620).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-23.py --out out/dix-pour-cent/s02e03/scene-23.json

ID = "dix-pour-cent-s02e03-scene-23"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 23
TITLE = "Arrivée au Laser Game  (Arrival at the Laser Game)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "elvis": "marcel"}
LABELS = {"lea": "Norman", "hicham": "Hicham", "elvis": "Elvis"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 595-620. Hicham, Elvis, and Norman arrive at the laser game center for Elvis's tenth birthday party. "
    "Surrounded by excited children, Norman meets the birthday boy and gets ready for the game."
)

INTRO = (
    "At the laser game arena, young guests eagerly await the guest of honor for Elvis's tenth birthday party. "
    "When internet star Norman Thavaud arrives, the excitement peaks as he meets the birthday boy and gets ready for battle. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("hicham", "Regardez, Norman est enfin là!",
     "Look, Norman is finally here!",
     [(599, "Norman ! Regardez, Norman est là !")], ""),
    ("lea", "Bonjour à tous les enfants!",
     "Hello to all the children!",
     [(601, "-Ça va, les enfants ?")], ""),
    ("elvis", "Je peux avoir un autographe?",
     "Can I have an autograph?",
     [(601, "-Je peux avoir un autographe ?")], ""),
    ("lea", "Oui bien sûr, avec plaisir.",
     "Yes of course, with pleasure.",
     [(602, "Tout le monde va bien ?")], ""),
    ("lea", "Qui est le chef ici?",
     "Who is the boss here?",
     [(603, "-C'est qui le chef ici ?")], ""),
    ("elvis", "C'est moi le grand chef!",
     "I am the big boss!",
     [(603, "-Lui !")], ""),
    ("lea", "Tu m'as défié au jeu?",
     "You challenged me to the game?",
     [(604, "Le gamin de 10 ans qui m'a défié au laser game ?")], ""),
    ("elvis", "Oui, j'ai une super équipe.",
     "Yes, I have a great team.",
     [(606, "T'as une bonne équipe ?")], ""),
    ("lea", "Je suis très fort aussi.",
     "I am very good too.",
     [(606, "Je suis très fort là-dedans.")], ""),
    ("hicham", "C'est ton anniversaire aujourd'hui, Elvis.",
     "It is your birthday today, Elvis.",
     [(611, "C'est ton anniversaire, ta fête.")], ""),
    ("elvis", "On va gagner la partie!",
     "We are going to win the game!",
     [(607, "-Allez, on se bat !")], ""),
    ("lea", "Ne sois pas trop timide.",
     "Do not be too shy.",
     [(610, "Fais pas le timide.")], ""),
    ("hicham", "Amusez-vous bien tous ensemble.",
     "Have good fun all together.",
     [(612, "Allez.")], ""),
    ("lea", "C'est parti pour le combat!",
     "Here we go for the fight!",
     [(607, "-Allez, on se bat !")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'Look, Norman is finally here!' Hicham announces the arrival of the special guest to the gathering. "
     "The imperative regardez directs everyone's attention."),
    (1, None,
     "'Hello to all the children!' The YouTube star greets the young guests warmly. "
     "The phrase a tous means to everyone or to all."),
    (2, None,
     "'Can I have an autograph?' The birthday boy excitedly asks for a signed souvenir. "
     "The modal verb peux expresses a polite request."),
    (3, None,
     "'Yes of course, with pleasure.' Norman gladly agrees to sign for his young admirer. "
     "The fixed expression bien sur means of course."),
    (4, None,
     "'Who is the boss here?' He playfully asks who is in charge of the celebration. "
     "The interrogative pronoun qui asks about a person."),
    (5, None,
     "'I am the big boss!' Elvis proudly steps forward as the guest of honor. "
     "The stressed pronoun moi reinforces the subject."),
    (6, None,
     "'You challenged me to the game?' Norman recalls the friendly duel proposed for the afternoon. "
     "The compound past tense as defie uses the auxiliary avoir."),
    (7, None,
     "'Yes, I have a great team.' The boy boasts about his squad of friends ready to play. "
     "The invariable adjective super means fantastic or great."),
    (8, None,
     "'I am very good too.' The celebrity playfully warns that he is also a formidable opponent. "
     "The adjective fort means strong or skilled."),
    (9, None,
     "'It is your birthday today, Elvis.' The proud father reminds his son to enjoy his special moment. "
     "The adverb aujourd'hui indicates the present day."),
    (10, None,
     "'We are going to win the game!' The youngster confidently predicts victory for his side. "
     "The near future structure va gagner combines aller with an infinitive."),
    (11, None,
     "'Do not be too shy.' Norman kindly encourages the boy to relax and have fun. "
     "The subjunctive form sois follows ne in a negative command."),
    (12, None,
     "'Have good fun all together.' Hicham sends the kids off to begin their laser adventure. "
     "The reflexive imperative amusez-vous means have fun."),
    (13, None,
     "'Here we go for the fight!' Norman joins the children as the match kicks off. "
     "The idiomatic phrase c'est parti marks the start of an activity."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Surrounded by cheering kids, Norman dives into the laser tag arena to give Elvis an unforgettable birthday match. "
    "Notice how the near future is formed with aller followed by an infinitive: on va gagner."
)

CLOSING = ("lea", "C'est parti pour le combat!")
