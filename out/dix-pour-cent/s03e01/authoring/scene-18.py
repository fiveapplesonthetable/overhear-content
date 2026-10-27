# Authoring module for dix-pour-cent s03e01 scene 18 (cues 604-632).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-18.py --out out/dix-pour-cent/s03e01/scene-18.json

ID = "dix-pour-cent-s03e01-scene-18"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 18
TITLE = "Le conseil de Samuel  (Samuel's Advice)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "annick": "emilie"}
LABELS = {"lea": "Camille", "mathias": "Mathias", "annick": "Annick"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 604-632. Mathias arrives at Camille's apartment. Annick asks if Camille has what it takes "
    "to be an agent, and Mathias praises her instincts before sharing Samuel Kerr's core rule."
)

INTRO = (
    "Mathias arrives at Camille's apartment late in the evening and finds Annick and Camille talking. "
    "Annick asks Mathias whether Camille truly has the qualities required to succeed in show business. "
    "Listen to the conversation in French first."
)

STORY = [
    ("mathias", "Ta mère a raison, va te coucher.",
     "Your mother is right, go to bed.",
     [(604, "Ta mère a raison, tu dois aller te coucher.")], ""),
    ("annick", "Est-ce qu'elle va réussir dans ce travail?",
     "Is she going to succeed in this job?",
     [(610, "Bon, elle va y arriver, non ? Qu'est-ce que tu en penses, toi ?")], ""),
    ("mathias", "Camille a toutes les qualités d'un agent.",
     "Camille has all the qualities of an agent.",
     [(617, "elle a beaucoup des qualités qu'il faut"), (618, "pour faire un bon agent.")], ""),
    ("annick", "Quelles sont ses vraies forces?",
     "What are her real strengths?",
     [(619, "Elle est fine, elle a de l'instinct,")], ""),
    ("mathias", "Elle est courageuse et très fine.",
     "She is courageous and very sharp.",
     [(620, "elle est pugnace, elle est courageuse.")], ""),
    ("annick", "Je sens venir un grand défaut!",
     "I feel a big flaw coming!",
     [(621, "Je sens venir le mais.")], ""),
    ("mathias", "Elle manque encore de confiance en elle.",
     "She still lacks confidence in herself.",
     [(622, "Mais elle manque encore de confiance en elle.")], ""),
    ("lea", "Arrêtez de parler comme des psychiatres!",
     "Stop talking like psychiatrists!",
     [(626, "Puis c'est quoi, cette fausse séance de psy ?")], ""),
    ("annick", "Écoute ton père pour une fois.",
     "Listen to your father for once.",
     [(627, "Camille, écoute ton père.")], ""),
    ("lea", "Je suis là dans la pièce!",
     "I am here in the room!",
     [(625, "Parler de moi comme si j'étais pas là.")], ""),
    ("mathias", "Rappelle-toi la leçon de Samuel Kerr.",
     "Remember the lesson of Samuel Kerr.",
     [(630, "Tu sais ce que disait Samuel ?")], ""),
    ("lea", "Quelle était sa règle préférée?",
     "What was his favorite rule?",
     [(630, "Tu sais ce que disait Samuel ?")], ""),
    ("mathias", "Ne montre jamais ton besoin aux acteurs.",
     "Never show your need to actors.",
     [(631, "Ne laisse pas un acteur croire que t'as besoin de lui,")], ""),
    ("mathias", "Fais croire qu'ils ont besoin de toi.",
     "Make them believe that they need you.",
     [(632, "mais toi, fais-lui croire qu'il a besoin de toi.")], "")
]

OPENER = "Let us discover how Mathias evaluates Camille's potential as an agent."

WALK = [
    (0, None,
     "'Your mother is right, go to bed.' Mathias agrees with Annick about resting. "
     "The idiom avoir raison means to be right."),
    (1, None,
     "'Is she going to succeed in this job?' Annick inquires about her daughter's future. "
     "The verb réussir means to succeed."),
    (2, None,
     "'Camille has all the qualities of an agent.' Mathias acknowledges her professional promise. "
     "The plural noun qualités means strengths or qualities."),
    (3, None,
     "'What are her real strengths?' Annick wants specific details. "
     "The feminine plural noun forces refers to strong attributes."),
    (4, None,
     "'She is courageous and very sharp.' Mathias praises her instincts. "
     "The feminine adjective fine denotes subtlety and intelligence."),
    (5, None,
     "'I feel a big flaw coming!' Annick anticipates a reservation. "
     "The verb phrase sentir venir means to sense something approaching."),
    (6, None,
     "'She still lacks confidence in herself.' Mathias identifies her main challenge. "
     "The phrase manquer de means to lack."),
    (7, None,
     "'Stop talking like psychiatrists!' Camille protests being analyzed. "
     "The plural imperative arrêtez expresses frustration."),
    (8, None,
     "'Listen to your father for once.' Annick encourages Camille to pay attention. "
     "The imperative écoute addresses Camille."),
    (9, None,
     "'I am here in the room!' Camille insists on being acknowledged. "
     "The noun pièce means room."),
    (10, None,
     "'Remember the lesson of Samuel Kerr.' Mathias invokes the legendary founder. "
     "The reflexive imperative rappelle-toi means remember."),
    (11, None,
     "'What was his favorite rule?' Camille asks about Samuel's wisdom. "
     "The feminine adjective préférée agrees with règle."),
    (12, None,
     "'Never show your need to actors.' Mathias shares an essential agency principle. "
     "The negative imperative ne montre jamais means never show."),
    (13, None,
     "'Make them believe that they need you.' Mathias delivers Samuel's famous rule. "
     "The causative structure faire croire means to make someone believe.")
]

TRANSITION = "Now let us listen to the advice once more at normal conversational speed."

OUTRO = (
    "Mathias passes down the agency wisdom of Samuel Kerr to Camille, encouraging her to believe in her value. "
    "Listen to the scene once more in French."
)

CLOSING = ("mathias", "Fais croire qu'ils ont besoin de toi.")
