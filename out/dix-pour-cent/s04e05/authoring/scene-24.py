# Authoring module for dix-pour-cent s04e05 scene 24 (cues 878-916).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e05/authoring/scene-24.py --out out/dix-pour-cent/s04e05/scene-24.json

ID = "dix-pour-cent-s04e05-scene-24"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 24
TITLE = "La colère de Noemie  (Noemie's Fury)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noemie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 878-916. At the hospital following Mathias's coronary attack, producer Igor de Serisy tries to push "
    "Mathias immediately back to work. A furious Noemie steps between them to protect Mathias's life, fiercely "
    "denouncing Igor's callous cruelty and refusing to let Mathias kill himself for a movie."
)

INTRO = (
    "In his hospital room, Mathias is discharged with a portable heart monitor following a terrifying heart attack. "
    "When ruthless producer Igor de Serisy storms in to drag him immediately to a meeting, Noemie erupts in righteous fury to defend Mathias's life. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Le médecin t'a posé ce moniteur?",
     "Did the doctor place this monitor on you?",
     [(878, "surveiller votre rythme cardiaque")], "Inquired about the medical equipment"),
    ("mathias", "Oui, pour surveiller mon rythme cardiaque.",
     "Yes, to monitor my heart rate.",
     [(878, "surveiller votre rythme cardiaque")], "Explained the doctor's instructions"),
    ("lea", "Tu dois te reposer à la maison.",
     "You must rest at home.",
     [(888, "Prêt à rentrer à la maison?")], "Insisted on immediate rest"),
    ("mathias", "Igor veut aller chez le réalisateur.",
     "Igor wants to go to the director's house.",
     [(895, "On a rendez-vous avec Jean-Jacques Annaud")], "Mentioned the urgent work meeting"),
    ("lea", "Tu as failli mourir d'un infarctus!",
     "You almost died of a heart attack!",
     [(898, "il a fait un infarctus?"), (906, "Tu as failli mourir")], "Reminded him of the mortal danger"),
    ("mathias", "C'est un rendez-vous très important aujourd'hui.",
     "It is a very important meeting today.",
     [(896, "Tu vas travailler là, maintenant?")], "Tried to justify the professional pressure"),
    ("lea", "Igor traite tout le monde sans pitié.",
     "Igor treats everyone without mercy.",
     [(904, "tout le monde est traité comme de la merde")], "Denounced the producer's utter callousness"),
    ("mathias", "Il m'a quand même apporté des chocolats.",
     "He still brought me chocolates.",
     [(892, "Trois chocolats")], "Defended the producer with a weak excuse"),
    ("lea", "Ne cherche pas à le défendre encore!",
     "Do not try to defend him again!",
     [(905, "Tu le défends?")], "Ordered him to stop defending his abuser"),
    ("mathias", "Je ne veux pas perdre ce projet.",
     "I do not want to lose this project.",
     [(897, "j'ai dit à Jean-Jacques")], "Confessed his underlying business anxiety"),
    ("lea", "Ta vie vaut plus que ce film.",
     "Your life is worth more than this film.",
     [(906, "ne te laisse pas une demi-seconde pour te reposer")], "Reminded him of what truly matters"),
    ("mathias", "Tu es vraiment en colère, ma chérie.",
     "You are truly angry, my darling.",
     [(910, "je suis en colère!")], "Averred her fiery determination"),
    ("lea", "Je refuse de te laisser mourir bêtement.",
     "I refuse to let you die stupidly.",
     [(916, "Va te faire foutre")], "Vowed to protect his life against the industry"),
    ("mathias", "Rentrons chez nous nous reposer ensemble.",
     "Let us go home to rest together.",
     [(888, "rentrer à la maison")], "Finally accepted her caring counsel"),
]

WALK = [
    (0, None,
     "'Did the doctor place this monitor on you?' Noemie examines the device on Mathias's chest. "
     "The compound past verb t'a posé introduces the medical context."),
    (1, None,
     "'Yes, to monitor my heart rate.' Mathias explains the safeguard. "
     "The infinitive phrase pour surveiller states the clinical purpose."),
    (2, None,
     "'You must rest at home.' Noemie insists on immediate convalescence. "
     "The reflexive verb te reposer emphasizes personal recovery."),
    (3, None,
     "'Igor wants to go to the director's house.' Mathias nervously mentions the meeting. "
     "The prepositional phrase chez le réalisateur identifies the proposed stop."),
    (4, None,
     "'You almost died of a heart attack!' Noemie reminds him of how close he came to death. "
     "The verb phrase as failli mourir highlights the life-or-death stakes."),
    (5, None,
     "'It is a very important meeting today.' Mathias struggles with workplace duty. "
     "The adjective phrase très important reflects his chronic anxiety."),
    (6, None,
     "'Igor treats everyone without mercy.' Noemie condemns the producer's exploitation. "
     "The prepositional phrase sans pitié describes ruthless abuse."),
    (7, None,
     "'He still brought me chocolates.' Mathias offers a pathetic defense of his partner. "
     "The conjunction quand même grasps at superficial kindness."),
    (8, None,
     "'Do not try to defend him again!' Noemie cuts through his excuses. "
     "The negative imperative ne cherche pas refuses compromise."),
    (9, None,
     "'I do not want to lose this project.' Mathias admits his fear of failure. "
     "The negative structure ne veux pas perdre captures commercial panic."),
    (10, None,
     "'Your life is worth more than this film.' Noemie reestablishes human priorities. "
     "The comparative expression vaut plus que puts work below health."),
    (11, None,
     "'You are truly angry, my darling.' Mathias feels both chastised and deeply loved. "
     "The prepositional phrase en colère registers her passionate defense."),
    (12, None,
     "'I refuse to let you die stupidly.' Noemie stands between him and exhaustion. "
     "The adverb bêtement rejects unnecessary self-destruction."),
    (13, None,
     "'Let us go home to rest together.' Mathias surrenders to love and good sense. "
     "The imperative verb rentrons promises recovery and peace."),
]

OUTRO = "Mathias smiles gently and takes Noemie's hand, grateful for her fierce love and protective strength. When you watch the episode, listen out for the expressions meaning 'doctor' and 'placed'. You'll catch them now. See you next time."
CLOSING = ("mathias", "Rentrons chez nous nous reposer ensemble.")
