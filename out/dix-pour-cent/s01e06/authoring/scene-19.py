ID = "dix-pour-cent-s01e06-scene-19"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 19
TITLE = "Le secret de François  (François's Secret)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "christophe": "theo", "francois": "marcel"}
LABELS = {"lea": "Andréa", "christophe": "Christophe", "francois": "François"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"

INTRO = (
    "On her way out of the agency, Andréa reassures Colette on the phone that she is wearing "
    "a simple, casual outfit and only stopping for a quick drink at the rehearsal studio to "
    "save the play before joining Colette's friends for dessert. Outside the studio, Andréa "
    "meets François and brings him into Christophe Bel's birthday party. "
    "Let's listen to the scene in French first; don't worry about catching every word."
)

STORY = [
    ("lea", "Tu as apporté un cadeau?",
     "Did you bring a present?",
     [(508, "apporté un cadeau")],
     "spoken 'T'as' expanded to 'Tu as'"),
    ("christophe", "Très bien. Très drôle. Je suis content que ça t'amuse.",
     "Very good. Very funny. I'm glad that amuses you.",
     [(511, "Très bien. Très drôle"), (513, "Je suis content que ça t'amuse")], ""),
    ("christophe", "Je dois m'occuper de la musique. Profite de l'ambiance.",
     "I have to take care of the music. Enjoy the atmosphere.",
     [(514, "Je dois m'occuper de la musique"), (515, "Profite de l'ambiance")], ""),
    ("francois", "Il ne me parle pas! Il m'invite, et il m'ignore!",
     "He isn't talking to me! He invites me, and he ignores me!",
     [(516, "Il ne me parle pas"), (516, "Il m'invite, et il m'ignore")], ""),
    ("lea", "Attends, il va revenir.",
     "Wait, he's going to come back.",
     [(517, "Attends, il va revenir")], ""),
    ("lea", "C'est sa fête, il est stressé. Donne-lui le temps.",
     "It's his party, he's stressed. Give him time.",
     [(518, "C'est sa fête, il est stressé. Donne-lui le temps")], ""),
    ("francois", "Non, je m'en vais.",
     "No, I'm leaving.",
     [(519, "Non, je m'en vais")], ""),
    ("lea", "Quoi? Non, reste! François!",
     "What? No, stay! François!",
     [(520, "Quoi"), (520, "Non, reste"), (520, "François")], ""),
    ("lea", "Christophe, vous êtes faits pour travailler ensemble.",
     "Christophe, you are made to work together.",
     [(523, "Christophe, vous êtes faits pour travailler ensemble")], ""),
    ("christophe", "Donne-moi une bonne raison.",
     "Give me one good reason.",
     [(524, "Donne-moi une bonne raison")], ""),
    ("lea", "C'est un grand acteur!",
     "He's a great actor!",
     [(525, "C'est un grand acteur")], ""),
    ("christophe", "Il n'a aucun respect! Je ne peux pas le diriger dans ma pièce!",
     "He has no respect! I can't direct him in my play!",
     [(525, "Il n'a aucun respect"), (526, "Je ne peux pas le diriger dans ma pièce")], ""),
    ("lea", "Ce n'est pas qu'il ne veut pas!",
     "It's not that he doesn't want to!",
     [(527, "pas qu'il ne veut pas")],
     "spoken 'C'est pas' restored to 'Ce n'est pas'"),
    ("christophe", "Alors quel est le problème? Il ne peut pas?",
     "Then what is the problem? He can't?",
     [(527, "Alors quel est le problème"), (528, "Il ne peut pas")], ""),
    ("lea", "Il ne faut le dire à personne. Il ne sait pas nager.",
     "You mustn't tell anyone. He doesn't know how to swim.",
     [(529, "Il ne faut le dire à personne"), (530, "Il ne sait pas nager")], ""),
    ("christophe", "Quoi?",
     "What?",
     [(531, "Quoi")], ""),
    ("lea", "Il ne sait pas nager!",
     "He doesn't know how to swim!",
     [(531, "Il ne sait pas nager")], ""),
]

OPENER = "Let's go through it slowly. As they arrive at the party, Andréa spots what François is holding."

WALK = [
    (0, None,
     "'Did you bring a present?' François brought an inflatable yellow duck as a tongue-in-cheek peace offering for Christophe."),
    (1, "Très bien. Très drôle.",
     "'Very good. Very funny.' Christophe is not amused when François hands him the plastic duck."),
    (1, "Je suis content que ça t'amuse.",
     "'I'm glad that amuses you.'"),
    (2, "Je dois m'occuper de la musique.",
     "'I have to take care of the music.' Literally 'occupy myself with the music'."),
    (2, "Profite de l'ambiance.",
     "'Enjoy the atmosphere.' Christophe walks away coldly."),
    (3, None,
     "'He isn't talking to me! He invites me, and he ignores me!' Remember that Christophe didn't actually send that invitation text—Colette sent it from Andréa's phone as a joke!"),
    (4, None,
     "'Wait, he's going to come back.'"),
    (5, None,
     "'It's his party, he's stressed. Give him time.'"),
    (6, None,
     "'No, I'm leaving.' Literally 'I go away from here'."),
    (7, None,
     "'What? No, stay! François!' As François heads for the door, Andréa corners Christophe."),
    (8, None,
     "'Christophe, you are made to work together.'"),
    (9, None,
     "'Give me one good reason.'"),
    (10, None,
     "'He's a great actor!' When placed before the noun, the adjective for 'tall' or 'big' means 'great'."),
    (11, None,
     "'He has no respect! I can't direct him in my play!' Here 'room' or 'piece' means a theatre play."),
    (12, None,
     "'It's not that he doesn't want to!'"),
    (13, None,
     "'Then what is the problem? He can't?'"),
    (14, "Il ne faut le dire à personne.",
     "'You mustn't tell anyone.' Literally 'one must tell it to nobody'."),
    (14, "Il ne sait pas nager.",
     "'He doesn't know how to swim.' That is the real reason François has been terrified of the swimming pool all along!"),
    (15, None,
     "'What?' Christophe is stunned."),
    (16, None,
     "'He doesn't know how to swim!'"),
]

TRANSITION = "Now let's hear the whole scene again from start to finish."

OUTRO = (
    "Now that Christophe knows the real reason François refused to get into the pool, he "
    "immediately runs after François to catch him before he leaves. See you in the next scene."
)
CLOSING = ("christophe", "François, attends!")
