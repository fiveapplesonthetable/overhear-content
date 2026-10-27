# Authoring module for dix-pour-cent s02e06 scene 18 (cues 482-511).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-18.py --out out/dix-pour-cent/s02e06/scene-18.json

ID = "dix-pour-cent-s02e06-scene-18"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 18
TITLE = "Face à la vérité  (I Can't Love You)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Catherine", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 482-511. In Mathias's hotel room at Cannes, his wife Catherine arrives unexpectedly. "
    "She tells him she visited Camille in Mandelieu and found her in despair. Catherine urges Mathias "
    "to stop hiding behind excuses and finally act like a caring father to his daughter."
)

INTRO = (
    "In a hotel room at the Cannes Film Festival, Mathias receives an unexpected visit from his wife Catherine. "
    "Having visited Camille in Mandelieu, Catherine delivers an ultimatum about his duties as a father. "
    "Listen to the scene in French first."
)

STORY = [
    ("mathias", "Catherine? Quelle surprise de te voir à Cannes!",
     "Catherine? What a surprise to see you in Cannes!",
     [(486, "Bonjour, monsieur."), (489, "Si, c'est ma femme.")], ""),
    ("lea", "Je suis allée à Mandelieu avant de venir.",
     "I went to Mandelieu before coming.",
     [(493, "Je suis allée à Mandelieu.")], ""),
    ("mathias", "Pourquoi es-tu allée là-bas?",
     "Why did you go over there?",
     [(495, "Pourquoi tu fais ça ?")], ""),
    ("lea", "J'ai vu Camille et sa mère au salon.",
     "I saw Camille and her mother at the salon.",
     [(494, "J'ai vu Camille et Annick et le salon de coiffure.")], ""),
    ("mathias", "C'est du passé, arrête de te torturer.",
     "It is in the past, stop torturing yourself.",
     [(496, "C'est du passé. Arrête de te torturer.")], ""),
    ("lea", "Ce n'est pas le passé qui me préoccupe.",
     "It is not the past that worries me.",
     [(498, "Ce n'est pas le passé qui me pèse, c'est Camille.")], ""),
    ("lea", "C'est Camille qui va vraiment très mal.",
     "It is Camille who is doing really badly.",
     [(498, "c'est Camille."), (500, "Elle va vraiment très mal.")], ""),
    ("mathias", "Elle a quitté l'agence, c'était mieux ainsi.",
     "She left the agency, it was better like that.",
     [(499, "Elle a quitté l'agence et tu ne fais rien."), (503, "J'ai pensé que c'était mieux ainsi")], ""),
    ("lea", "Tu as au moins pris de ses nouvelles?",
     "Did you at least ask how she is doing?",
     [(501, "Tu l'as au moins appelée ? -Oui.")], ""),
    ("mathias", "Pas depuis plusieurs jours, pour te protéger.",
     "Not for several days, to protect you.",
     [(502, "Pas depuis un jour ou deux."), (504, "que tu serais soulagée de savoir qu'elle était rentrée")], ""),
    ("lea", "Arrête de te cacher derrière ce prétexte!",
     "Stop hiding behind this pretext!",
     [(508, "Arrête ça, de penser à ma place"), (509, "Arrête de me protéger.")], ""),
    ("lea", "Camille a besoin de son père, Mathias.",
     "Camille needs her father, Mathias.",
     [(506, "C'est ta fille, Mathias.")], ""),
    ("mathias", "J'avais tellement peur de perdre ton amour.",
     "I was so afraid of losing your love.",
     [(507, "Je t'ai mis en premier.")], ""),
    ("lea", "Je ne veux pas d'un homme qui fuit ses devoirs.",
     "I do not want a man who flees his duties.",
     [(511, "Je ne peux pas t'aimer si je ne sais pas qui tu es vraiment.")], ""),
    ("mathias", "Tu as raison, j'ai été lâche avec elle.",
     "You are right, I was cowardly with her.",
     [(499, "et tu ne fais rien.")], ""),
    ("lea", "Appelle ta fille maintenant et assume ton rôle.",
     "Call your daughter now and take on your role.",
     [(510, "Qu'est-ce que tu veux ?"), (511, "Je ne peux pas t'aimer")], "")
]

OPENER = "Let's examine how Catherine confronts Mathias about the future of Camille."

WALK = [
    (0, None,
     "'Catherine? What a surprise to see you in Cannes!' Mathias reacts with astonishment. "
     "The exclamative phrase quelle surprise expresses deep astonishment."),
    (1, None,
     "'I went to Mandelieu before coming.' Catherine reveals her unexpected trip. "
     "The compound past suis allée agrees with the feminine subject."),
    (2, None,
     "'Why did you go over there?' Mathias is alarmed by her journey. "
     "The question word pourquoi inquires about her motive."),
    (3, None,
     "'I saw Camille and her mother at the salon.' Catherine describes her visit calmly. "
     "The compound past ai vu comes from voir."),
    (4, None,
     "'It is in the past, stop torturing yourself.' Mathias attempts to avoid the painful topic. "
     "The reflexive imperative arrête de te torturer urges peace."),
    (5, None,
     "'It is not the past that worries me.' Catherine clarifies her real motivation. "
     "The relative clause qui me préoccupe emphasizes the true subject."),
    (6, None,
     "'It is Camille who is doing really badly.' Catherine expresses genuine concern for the young woman. "
     "The phrase va très mal describes suffering."),
    (7, None,
     "'She left the agency, it was better like that.' Mathias rationalizes his passivity. "
     "The adverb ainsi means in this manner or like that."),
    (8, None,
     "'Did you at least ask how she is doing?' Catherine demands accountability. "
     "The expression prendre des nouvelles means to check on someone."),
    (9, None,
     "'Not for several days, to protect you.' Mathias claims he acted out of consideration for his wife. "
     "The prepositional phrase pour te protéger indicates purpose."),
    (10, None,
     "'Stop hiding behind this pretext!' Catherine calls out his avoidance. "
     "The prepositional phrase derrière ce prétexte means behind this excuse."),
    (11, None,
     "'Camille needs her father, Mathias.' Catherine delivers a direct moral appeal. "
     "The verbal locution avoir besoin de means to need."),
    (12, None,
     "'I was so afraid of losing your love.' Mathias confesses his deep insecurity. "
     "The imperfect avais peur conveys his ongoing fear."),
    (13, None,
     "'I do not want a man who flees his duties.' Catherine demands integrity and responsibility. "
     "The verb fuit comes from fuir."),
    (14, None,
     "'You are right, I was cowardly with her.' Mathias finally recognizes his failings. "
     "The adjective lâche means cowardly or spineless."),
    (15, None,
     "'Call your daughter now and take on your role.' Catherine urges him to act honorably. "
     "The imperative assume commands taking responsibility.")
]

TRANSITION = "Now let's listen to the painful confrontation once more at normal pace."

OUTRO = (
    "In Cannes, Catherine delivers a necessary truth that forces Mathias to face his responsibilities as a father. "
    "Listen to the poignant conversation once more in French."
)

CLOSING = ("lea", "Appelle ta fille maintenant et assume ton rôle.")
