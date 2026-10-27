# Authoring module for dix-pour-cent s02e04 scene 17 (cues 448-480).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-17.py --out out/dix-pour-cent/s02e04/scene-17.json

ID = "dix-pour-cent-s02e04-scene-17"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 17
TITLE = "L'entretien de Benoît  (Benoît's Interview)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "benoit": "theo"}
LABELS = {"lea": "Noémie", "benoit": "Benoît"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 448-480. Benoît Larroque waits in the lobby for his job interview to become an assistant at ASK. "
    "Noémie chats with him and mischievously terrifies him with absurd, dangerous stories about working exclusively "
    "for superstar client Gérard Depardieu, causing him to flee before the interview even starts."
)

INTRO = (
    "In the lobby of ASK, job applicant Benoît Larroque waits nervously for his interview to become an assistant. "
    "Noémie offers him a cup of coffee and casually paints a terrifying picture of life assisting Gérard Depardieu. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Tiens, Benoît. Voici ton café.",
     "Here, Benoît. Here is your coffee.",
     [(448, "Tiens, Benoît. -Merci")], ""),
    ("benoit", "Merci. Tu travailles ici?",
     "Thanks. Do you work here?",
     [(450, "Non, ça va"), (451, "Merci")], ""),
    ("lea", "Oui, je suis assistante.",
     "Yes, I am an assistant.",
     [(452, "Non, merci à vous")], ""),
    ("lea", "Tu viens pour le poste d'assistant?",
     "You are here for the assistant job?",
     [(456, "C'est vous le candidat")], ""),
    ("benoit", "Oui, je passe un entretien.",
     "Yes, I am having an interview.",
     [(457, "Oui, mais ils n'en avaient pas parlé")], ""),
    ("lea", "C'est pour travailler avec Gérard Depardieu.",
     "It is to work with Gérard Depardieu.",
     [(454, "exclusivement avec Depardieu")], ""),
    ("benoit", "Avec Depardieu? Il est difficile?",
     "With Depardieu? Is he difficult?",
     [(455, "Pardon"), (458, "Apparemment, il est difficile")], ""),
    ("lea", "Disons qu'il est très entier.",
     "Let's say he is quite extreme.",
     [(459, "Disons qu'il est entier")], ""),
    ("lea", "Tu as une bonne mutuelle santé?",
     "Do you have good health insurance?",
     [(460, "Vous avez une mutuelle")], ""),
    ("benoit", "Une mutuelle normale. Pourquoi?",
     "Standard insurance. Why?",
     [(461, "La normale"), (462, "Pourquoi")], ""),
    ("lea", "En cas de fractures du dos.",
     "In case of back fractures.",
     [(463, "En cas de fractures, de problèmes de dos")], ""),
    ("lea", "Gérard est un vrai poids lourd.",
     "Gérard is a real heavyweight.",
     [(464, "C'est un poids lourd")], ""),
    ("lea", "Tu es déjà allé en Russie?",
     "Have you ever been to Russia?",
     [(467, "Vous êtes déjà allé en Russie")], ""),
    ("benoit", "Non, je n'y suis jamais allé.",
     "No, I have never been there.",
     [(468, "Non, jamais")], ""),
    ("lea", "Là-bas, ils jouent à la roulette russe.",
     "Over there, they play Russian roulette.",
     [(470, "boivent, jouent à la roulette russe")], ""),
    ("benoit", "Je crois que je vais partir.",
     "I think that I will leave.",
     [(472, "Benoît Larroque"), (473, "Non")], "")
]

OPENER = "Let's examine how Noémie terrifies the new job applicant."

WALK = [
    (0, None,
     "'Here, Benoît. Here is your coffee.' Noémie hands him a warm beverage. "
     "The interjection tiens is often used when offering something."),
    (1, None,
     "'Thanks. Do you work here?' Benoît starts polite small talk. "
     "The adverb ici indicates the agency premises."),
    (2, None,
     "'Yes, I am an assistant.' Noémie confirms her administrative role. "
     "The feminine noun assistante takes no article after être."),
    (3, None,
     "'You are here for the assistant job?' She inquires about his presence. "
     "The noun phrase le poste d'assistant means the assistant position."),
    (4, None,
     "'Yes, I am having an interview.' Benoît explains his purpose. "
     "The expression passer un entretien means to attend a job interview."),
    (5, None,
     "'It is to work with Gérard Depardieu.' Noémie drops the intimidating name. "
     "The prepositional infinitive pour travailler indicates intended purpose."),
    (6, None,
     "'With Depardieu? Is he difficult?' Benoît asks nervously. "
     "The adjective difficile describes an exacting personality."),
    (7, None,
     "'Let's say he is quite extreme.' Noémie uses a classic euphemism. "
     "The adjective entier means uncompromising or intense."),
    (8, None,
     "'Do you have good health insurance?' She raises medical concerns immediately. "
     "The feminine noun mutuelle refers to complementary healthcare coverage."),
    (9, None,
     "'Standard insurance. Why?' Benoît becomes alarmed. "
     "The question word pourquoi inquires about her motive."),
    (10, None,
     "'In case of back fractures.' Noémie lists physical hazards casually. "
     "The prepositional locution en cas de means in case of."),
    (11, None,
     "'Gérard is a real heavyweight.' She emphasizes his imposing stature. "
     "The compound noun poids lourd literally means heavy vehicle or boxer."),
    (12, None,
     "'Have you ever been to Russia?' She asks about international travel. "
     "The adverb déjà means already or ever in questions."),
    (13, None,
     "'No, I have never been there.' Benoît admits his lack of experience. "
     "The adverbial pronoun y replaces the destination en Russie."),
    (14, None,
     "'Over there, they play Russian roulette.' She spins a terrifying tale. "
     "The noun phrase roulette russe refers to the deadly game."),
    (15, None,
     "'I think that I will leave.' Benoît decides to flee the agency. "
     "The immediate future vais partir combines aller with partir.")
]

TRANSITION = "Now let's listen to Noémie's wild warnings once more at normal speed."

OUTRO = (
    "Frightened by Noémie's absurd warnings, Benoît abandons the interview and rushes out the door. "
    "Listen to the hilarious conversation once more in French."
)

CLOSING = ("benoit", "Je crois que je vais partir.")
