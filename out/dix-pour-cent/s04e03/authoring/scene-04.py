# Authoring module for dix-pour-cent s04e03 scene 04 (cues 50-111).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e03/authoring/scene-04.py --out overhear-content/out/dix-pour-cent/s04e03/scene-04.json

ID = "dix-pour-cent-s04e03-scene-04"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 4
TITLE = "Le hoquet de José  (José's Hiccups)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jose": "theo"}
LABELS = {"lea": "Andréa", "jose": "José"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 50-111. On set for a period film, actor José Garcia suffers a sudden fit of hiccups that threatens "
    "the shoot. Andréa listens as he confides an intense romantic affair from his past, curing his symptoms in the process."
)

INTRO = (
    "On the film set, actor Jose Garcia suffers an unbearable attack of hiccups that halts the shoot. "
    "Andrea steps in and uncovers the hidden romantic anxiety behind his physical distress. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's explore Jose and Andrea's intimate discussion line by line."
TRANSITION = "Now let's listen to Jose and Andrea's full conversation once again from start to finish."

STORY = [
    ("jose", "Je ne peux pas tourner ainsi!",
     "I cannot shoot like this!",
     [(51, "Je peux pas tourner")], "José complains about his condition on set"),
    ("lea", "C'est seulement un petit hoquet.",
     "It is only a little hiccup.",
     [(53, "juste un hoquet")], "Andréa tries to minimize his panic"),
    ("jose", "Je vais boire à l'envers.",
     "I will drink upside down.",
     [(54, "boire à l'envers")], "José tries a traditional hiccup remedy"),
    ("lea", "Quel est le problème avec Laurence?",
     "What is the problem with Laurence?",
     [(68, "Le problème avec Laurence")], "Andréa addresses the emotional root cause"),
    ("jose", "On s'est rencontrés sur un tournage.",
     "We met on a film shoot.",
     [(73, "On s'est rencontrés")], "José recalls their first meeting"),
    ("jose", "Ce fut un coup de foudre.",
     "It was love at first sight.",
     [(77, "coup de foudre")], "José describes their sudden romantic passion"),
    ("jose", "Nous avons vécu deux mois de passion.",
     "We lived two months of passion.",
     [(81, "on a vécu"), (82, "de passion")], "José reminisces about their intense affair"),
    ("lea", "Et tu es allé à l'hôtel?",
     "And you went to the hotel?",
     [(89, "chambre d'hôtel")], "Andréa asks about their secret rendezvous"),
    ("jose", "Je me suis arrêté devant la porte.",
     "I stopped in front of the door.",
     [(94, "devant la porte")], "José remembers hesitating at the threshold"),
    ("jose", "Je suis parti pour éviter le drame.",
     "I left to avoid the drama.",
     [(99, "je suis parti")], "José explains why he walked away"),
    ("lea", "Tu as fait ce qu'il fallait.",
     "You did what was necessary.",
     [(104, "ce qu'il fallait faire")], "Andréa validates his difficult moral decision"),
    ("jose", "Regarde, mon hoquet est enfin parti!",
     "Look, my hiccup is finally gone!",
     [(109, "C'est parti !")], "José realizes his hiccups have vanished"),
    ("lea", "Qu'est-ce que je t'avais dit?",
     "What did I tell you?",
     [(110, "Qu'est-ce que je t'avais dit ?")], "Andréa smiles at the success of her therapy"),
    ("jose", "Allez, on y va maintenant!",
     "Come on, let's go now!",
     [(111, "Allez ! On y va !")], "José heads back to the set with renewed energy"),
]

WALK = [
    (0, None,
     "'I cannot shoot like this!' Jose complains that he cannot film in his current state. Notice the classic French sandwich negation wrapping right around 'can'."),
    (1, None,
     "'It is only a little hiccup.' Andrea attempts to downplay his nervous panic. The key noun here means 'hiccup.', anchored by its matching French article."),
    (2, None,
     "'I will drink upside down.' Jose tries an old folk remedy to stop the spasms. French forms the near future by pairing the present tense of 'to go' directly with 'to drink'."),
    (3, None,
     "'What is the problem with Laurence?' Andrea zeroes in on the true emotional issue. The key noun here means 'problem', anchored by its matching French article."),
    (4, None,
     "'We met on a film shoot.' Jose recalls their first meeting twenty years ago. Notice how 'met' leads directly into the noun meaning 'shoot.'."),
    (5, None,
     "'It was love at first sight.' Jose describes the instant romantic spark between them. Notice how 'was' leads directly into the noun meaning 'strike'."),
    (6, None,
     "'We lived two months of passion.' Jose recounts the secret affair they once shared. The verb meaning 'have' pairs naturally with the noun for 'months' in everyday conversation."),
    (7, None,
     "'And you went to the hotel?' Andrea asks about their planned final rendezvous. Notice how 'gone' leads directly into the noun meaning 'hotel?'."),
    (8, None,
     "'I stopped in front of the door.' Jose remembers pausing outside hotel room ten. This conversational past tense combines a helper verb with the past participle for 'stopped'."),
    (9, None,
     "'I left to avoid the drama.' Jose explains that he walked away to protect others. The verb meaning 'left' pairs naturally with the noun for 'drama.' in everyday conversation."),
    (10, None,
     "'You did what was necessary.' Andrea reassures him that he made the right choice. The clause hinges on the everyday verb meaning 'have'."),
    (11, None,
     "'Look, my hiccup is finally gone!' Jose realizes that the emotional release cured him. Dropping the subject pronoun turns the verb for 'look' into a direct, punchy command."),
    (12, None,
     "'What did I tell you?' Andrea smiles at the successful cure of his hiccups. In spoken French, the little word before 'had' drops its final vowel and attaches with an apostrophe."),
    (13, None,
     "'Come on, let's go now!' Jose returns eagerly to the set to resume filming. The clause hinges on the everyday verb meaning 'go'."),
]

OUTRO = (
    "By confronting his buried romantic memories, Jose overcomes his physical anxiety and returns happily to the movie set. "
    "Let's review the key vocabulary from this scene."
)

CLOSING = ("jose", "Allez, on y va maintenant!")
