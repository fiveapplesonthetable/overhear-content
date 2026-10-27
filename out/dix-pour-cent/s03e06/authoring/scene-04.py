# Authoring module for dix-pour-cent s03e06 scene 04 (cues 316-342).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-04.py --out out/dix-pour-cent/s03e06/scene-04.json

ID = "dix-pour-cent-s03e06-scene-04"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 4
TITLE = "Trêve provisoire  (Temporary Truce)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 316-342. Mathias tries to placate Gabriel and Andrea with higher shares before the gala. Adapted for A1 French.")

INTRO = ("With the agency's thirtieth anniversary gala about to begin, Mathias approaches Andrea and Gabriel in a bid for peace. "
         "Recognizing that thirty years of shared history cannot be easily erased, he offers to increase their shares and salaries under his leadership. "
         "Though Gabriel reacts with pride and indignation, Andrea urges caution to maintain an unbroken facade in front of their clients. "
         "Let's listen to the scene in French first.")

STORY = [
 ("mathias", "C'est la fête pour nos trente ans.",
  "It is the party for our thirty years.",
  [(318, "C'est la fête")], "Set celebratory context"),
 ("mathias", "Notre agence tient depuis trente longues années.",
  "Our agency has lasted for thirty long years.",
  [(320, "ça fait trente ans que ça tient")], "Recalled historic milestone"),
 ("mathias", "Ce succès existe grâce à nous quatre.",
  "This success exists thanks to the four of us.",
  [(321, "C'est grâce à nous")], "Acknowledged founding partners"),
 ("mathias", "Nous n'avons pas besoin d'être amis.",
  "We do not need to be friends.",
  [(322, "faire tenir cette agence")], "Stated pragmatic working reality"),
 ("mathias", "Je veux faire grandir cette belle agence.",
  "I want to grow this beautiful agency.",
  [(322, "faire tenir cette agence")], "Declared corporate ambitions"),
 ("mathias", "Je suis prêt à revaloriser vos parts.",
  "I am ready to increase your shares.",
  [(325, "revaloriser vos parts")], "Offered financial incentive"),
 ("mathias", "Je peux aussi augmenter vos salaires fixes.",
  "I can also increase your fixed salaries.",
  [(327, "Ou vos fixes")], "Proposed salary improvement"),
 ("mathias", "Je suis prêt à discuter calmement ensemble.",
  "I am ready to discuss calmly together.",
  [(329, "Je suis prêt à discuter")], "Invited peaceful negotiation"),
 ("gabriel", "Nous ne sommes pas des mendiants, Mathias.",
  "We are not beggars, Mathias.",
  [(330, "on n'est pas les mendiants")], "Rejected condescending offer"),
 ("lea", "Attends un peu, cette offre se réfléchit.",
  "Wait a bit, this offer is worth considering.",
  [(332, "Ça se réfléchit")], "Suggested pragmatic pause"),
 ("gabriel", "Il n'y a absolument rien à négocier!",
  "There is absolutely nothing to negotiate!",
  [(334, "y a rien à réfléchir")], "Maintained strict defiance"),
 ("lea", "Nous n'allons pas nous déchirer ce soir.",
  "We are not going to tear each other apart tonight.",
  [(338, "On va pas se déchirer ce soir")], "Urged public restraint"),
 ("lea", "Nos clients observent notre équipe avec attention.",
  "Our clients are watching our team closely.",
  [(338, "On va pas se déchirer ce soir")], "Reminded team of VIP audience"),
 ("mathias", "Nous valons tous beaucoup mieux que ça.",
  "We are all worth much better than that.",
  [(340, "On vaut mieux que ça")], "Appealed to collective professional pride"),
]

OPENER = "Let's observe as Mathias offers financial concessions while Andrea urges public restraint."

WALK = [
 (0, None,
  "'It is the party for our thirty years.' A celebratory opening emphasizing the historic anniversary milestone."),
 (1, None,
  "'Our agency has lasted for thirty long years.' A nostalgic acknowledgment recognizing three decades of collective endurance."),
 (2, None,
  "'This success exists thanks to the four of us.' A generous admission crediting the original founding quartet."),
 (3, None,
  "'We do not need to be friends.' A pragmatic statement prioritizing professional collaboration over personal affection."),
 (4, None,
  "'I want to grow this beautiful agency.' An ambitious promise declaring an expansive corporate future for ASK."),
 (5, None,
  "'I am ready to increase your shares.' A major financial concession offering increased ownership stakes."),
 (6, None,
  "'I can also increase your fixed salaries.' An additional financial enticement proposing higher base compensation."),
 (7, None,
  "'I am ready to discuss calmly together.' A diplomatic invitation seeking peaceful terms of reconciliation."),
 (8, None,
  "'We are not beggars, Mathias.' An indignant rebuke rejecting what sounds like patronizing charity."),
 (9, None,
  "'Wait a bit, this offer is worth considering.' A calculating intervention calling for thoughtful deliberation."),
 (10, None,
  "'There is absolutely nothing to negotiate!' An uncompromising refusal shutting down further corporate horse-trading."),
 (11, None,
  "'We are not going to tear each other apart tonight.' A sensible appeal enforcing decorum before an audience of film industry guests."),
 (12, None,
  "'Our clients are watching our team closely.' A sobering reminder highlighting the professional scrutiny surrounding the gala."),
 (13, None,
  "'We are all worth much better than that.' An earnest conclusion appealing to mutual self-respect and dignity."),
]

TRANSITION = "Now let's listen to Mathias, Andrea, and Gabriel concluding their truce at full speed."

OUTRO = ("Agreeing to present a united front for the anniversary gala, the partners bury their grievances for a few brief hours. "
         "Yet behind the smiles and flowing champagne, the quiet battle for the agency's destiny has only just begun.")

CLOSING = ("lea", "Gardons la tête haute.")
