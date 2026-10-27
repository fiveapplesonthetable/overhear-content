# Authoring module for dix-pour-cent s03e03 scene 17 (cues 1048-1084).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e03/authoring/scene-17.py --out out/dix-pour-cent/s03e03/scene-17.json

ID = "dix-pour-cent-s03e03-scene-17"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 17
TITLE = "Croiser Guy Marchand  (Crossing Paths with Guy Marchand)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "guy": "theo"}
LABELS = {"lea": "Andréa", "guy": "Guy"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1048-1084. At the ASK agency, Andréa crosses paths with veteran actor Guy Marchand. "
    "When Guy mentions seeing her on Avenue de Trudaine, Andréa covers by claiming she was apartment-hunting with Colette, "
    "then chides Guy for relying on a fortune-teller."
)

INTRO = (
    "At the agency, Andrea bumps into veteran actor Guy Marchand, who casually reveals he saw her on Avenue de Trudaine earlier. "
    "To protect her confidential agency meetings, Andrea invents a story about apartment hunting, before teasing Guy about his tarot card reader. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("guy", "Andréa, on ne se quitte plus!",
     "Andrea, we never leave each other anymore!",
     [(1049, "On n'arrête pas de se voir")], "Guy jokes about bumping into Andrea repeatedly"),
    ("lea", "Bonjour Guy, comment vas-tu aujourd'hui?",
     "Hello Guy, how are you today?",
     [(1048, "Guy, bah ça alors")], "Andrea greets her client warmly"),
    ("guy", "Je t'ai vue ce matin.",
     "I saw you this morning.",
     [(1050, "croisés ce matin")], "Guy mentions their earlier near-encounter"),
    ("guy", "Tu marchais avenue de Trudaine.",
     "You were walking on Avenue de Trudaine.",
     [(1050, "avenue de Truden")], "Guy names the exact location"),
    ("lea", "Oui, je visitais un petit appartement.",
     "Yes, I was visiting a small apartment.",
     [(1051, "J'ai visité un appart")], "Andrea invents a quick cover story"),
    ("lea", "Nous cherchons un logement avec Colette.",
     "We are looking for housing with Colette.",
     [(1053, "Avec Colette pour le bébé")], "Andrea adds personal details about the baby"),
    ("guy", "C'est un quartier très agréable.",
     "It is a very pleasant neighborhood.",
     [(1060, "C'est très joli, là-bas")], "Guy approves of the location"),
    ("lea", "Tu viens pour un nouveau rôle?",
     "Are you coming for a new role?",
     [(1072, "J'avais un doute sur un rôle")], "Andrea redirects the discussion to work"),
    ("guy", "J'avais un doute sur ce projet.",
     "I had a doubt about this project.",
     [(1072, "J'avais un doute sur un rôle")], "Guy admits his artistic uncertainty"),
    ("guy", "Ma voyante lit dans les cartes.",
     "My fortune teller reads the cards.",
     [(1078, "La carte au Mansi, c'est sérieux")], "Guy explains his unusual consultation method"),
    ("lea", "Tu écoutes encore cette femme?",
     "Are you still listening to that woman?",
     [(1070, "T'es encore allé voir ta voyante")], "Andrea expresses mock disbelief"),
    ("lea", "C'est moi ton agent officiel!",
     "I am your official agent!",
     [(1074, "mes conseils à moi, ton agent")], "Andrea reasserts her professional authority"),
    ("guy", "Ne sois pas jalouse, Andréa!",
     "Do not be jealous, Andrea!",
     [(1077, "Arrête, je te l'ai déjà dit")], "Guy teases Andrea affectionately"),
    ("guy", "Tu restes ma petite reine.",
     "You remain my little queen.",
     [(1083, "Ma p'tite reine")], "Guy closes with a loving pet name")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Andrea, we never leave each other anymore!' Guy jokes about seeing Andrea all day. "
     "The reflexive reciprocal verb expresses constant running into each other."),
    (1, None,
     "'Hello Guy, how are you today?' Andrea greets her client with pleasant cheer. "
     "The familiar question asks about his current state."),
    (2, None,
     "'I saw you this morning.' Guy mentions having spotted her earlier in Paris. "
     "The compound past verb with a direct object pronoun refers to their earlier crossing."),
    (3, None,
     "'You were walking on Avenue de Trudaine.' Guy specifies the street where he saw her. "
     "The imperfect verb depicts ongoing past motion on the street."),
    (4, None,
     "'Yes, I was visiting a small apartment.' Andrea quickly manufactures an alibi. "
     "The imperfect verb describes a plausible past activity."),
    (5, None,
     "'We are looking for housing with Colette.' Andrea mentions her partner to sell the excuse. "
     "The present tense verb indicates an ongoing family search."),
    (6, None,
     "'It is a very pleasant neighborhood.' Guy compliments the Parisian area. "
     "The presentative construction with an adjective praises the location."),
    (7, None,
     "'Are you coming for a new role?' Andrea steers the conversation back to career business. "
     "The present verb inquires about his reason for visiting the agency."),
    (8, None,
     "'I had a doubt about this project.' Guy admits having second thoughts about a script. "
     "The imperfect verb reveals his hesitation over a part."),
    (9, None,
     "'My fortune teller reads the cards.' Guy reveals his supernatural consulting habit. "
     "The present verb describes tarot card divination."),
    (10, None,
     "'Are you still listening to that woman?' Andrea questions his reliance on clairvoyance. "
     "The adverb of continuation expresses incredulous exasperation."),
    (11, None,
     "'I am your official agent!' Andrea insists on her primary advisory role. "
     "The emphatic cleft construction asserts legitimate professional guidance."),
    (12, None,
     "'Do not be jealous, Andrea!' Guy playfully dismisses her annoyance. "
     "The negative subjunctive imperative teases her possessiveness."),
    (13, None,
     "'You remain my little queen.' Guy charms Andrea with his favorite affectionate title. "
     "The present linking verb reaffirms their warm, longstanding bond.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "With quick thinking and charm, Andrea deflects suspicion while keeping her colorful client Guy Marchand on track. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("guy", "Tu restes ma petite reine.")
