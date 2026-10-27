# Authoring module for dix-pour-cent s03e05 scene 14 (cues 449-621).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e05/authoring/scene-14.py --out overhear-content/out/dix-pour-cent/s03e05/scene-14.json

ID = "dix-pour-cent-s03e05-scene-14"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 14
TITLE = "La clause de nudité  (The Nudity Clause)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "birag": "theo"}
LABELS = {"lea": "Andréa", "birag": "Jean-Luc Birag"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 460-505. Andréa confronts director Jean-Luc Birag over Béatrice Dalle's contract. "
    "While Birag claims the morgue scene qualifies as a love scene justifying nudity under the contract's ambiguous clause, "
    "Andréa furiously denounces his word games and defends her client against an exploitative demand. Adapted for A1 French."
)

INTRO = (
    "Armed with sticky notes and the signed contract, director Jean-Luc Birag tries to justify an unscripted nude scene. "
    "He claims that a cold sequence set in a morgue counts as an essential love scene. "
    "Let's listen to Andrea's sharp defense in French first."
)

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
    ("birag", "Voici le contrat signé de Béatrice Dalle.",
     "Here is the signed contract of Beatrice Dalle.",
     [(461, "C'est le contrat de Béatrice")], "Presenting contract"),
    ("birag", "L'actrice accepte de se dénuder au tournage.",
     "The actress agrees to appear nude during shooting.",
     [(467, "L'actrice acceptera de se dénuder")], "Citing nudity clause"),
    ("birag", "Cette décision est à ma seule discrétion.",
     "This decision is at my sole discretion.",
     [(468, "à la discrétion du metteur en scène")], "Asserting director control"),
    ("lea", "Seulement pour une vraie scène d'amour!",
     "Only for a true love scene!",
     [(470, "qu'il s'agisse d'une scène d'amour")], "Reminding of condition"),
    ("lea", "Or votre scène se passe à la morgue.",
     "Yet your scene takes place in the morgue.",
     [(474, "C'est une scène de morgue")], "Highlighting morgue setting"),
    ("birag", "L'homme regarde son grand amour décédé.",
     "The man gazes upon his deceased great love.",
     [(479, "corps mort"), (480, "femme qu'il aime")], "Justifying scene romance"),
    ("birag", "C'est une scène d'amour très pure.",
     "It is a very pure love scene.",
     [(484, "Avec amour"), (487, "c'est une scène d'amour")], "Defending creative vision"),
    ("lea", "Arrêtez, vous jouez sur les mots!",
     "Stop, you are playing on words!",
     [(490, "Mais arrête"), (492, "Tu joues sur les mots")], "Accusing of bad faith"),
    ("lea", "Une scène d'amour signifie une scène intime.",
     "A love scene means an intimate scene.",
     [(494, "ça veut dire une scène de sexe")], "Clarifying industry term"),
    ("birag", "Le contrat indique bien une scène d'amour.",
     "The contract clearly indicates a love scene.",
     [(496, "Sauf qu'il y a écrit scène d'amour")], "Insisting on contract wording"),
    ("lea", "Béatrice refuse de tourner nue dans ce sac.",
     "Beatrice refuses to shoot naked in this bag.",
     [(485, "sac mortuaire"), (486, "scène nue si je veux")], "Declaring client refusal"),
    ("birag", "Béatrice doit reprendre le tournage cet après-midi.",
     "Beatrice must resume shooting this afternoon.",
     [(502, "reprend ça par midi avec Béatrice")], "Issuing deadline"),
    ("birag", "Sinon, nous déclarerons une rupture de contrat.",
     "Otherwise, we will declare a breach of contract.",
     [(504, "que c'est une rupture de contrat")], "Threatening breach of contract"),
    ("lea", "Nous défendrons notre actrice jusqu'au bout!",
     "We will defend our actress all the way!",
     [(505, "pas envie d'en arriver là")], "Promising fierce defense"),
]

WALK = [
    (0, None,
     "'Here is the signed contract of Beatrice Dalle.' Director Birag presents the binding legal document. "
     "The past participle 'signe' functions as an adjective."),
    (1, None,
     "'The actress agrees to appear nude during shooting.' Birag points directly to the controversial nudity clause. "
     "The reflexive verb 'se denuder' means to strip or appear naked."),
    (2, None,
     "'This decision is at my sole discretion.' Birag asserts his unilateral creative authority. "
     "The noun 'discretion' indicates personal decision-making power."),
    (3, None,
     "'Only for a true love scene!' Andrea firmly challenges the director's interpretation. "
     "The adverb 'seulement' restricts the permissible circumstances."),
    (4, None,
     "'Yet your scene takes place in the morgue.' Andrea exposes the absurd setting for a supposed romance. "
     "The feminine noun 'morgue' denotes a mortuary."),
    (5, None,
     "'The man gazes upon his deceased great love.' Birag attempts to romanticize the chilling sequence. "
     "The adjective 'decede' means deceased or departed."),
    (6, None,
     "'It is a very pure love scene.' The director insists on the emotional essence of the moment. "
     "The feminine adjective 'pure' conveys unblemished nobility."),
    (7, None,
     "'Stop, you are playing on words!' Andrea furiously cuts through his rhetorical sophistry. "
     "The idiom 'jouer sur les mots' means to quibble or manipulate terms."),
    (8, None,
     "'A love scene means an intimate scene.' Andrea clarifies what standard contract language intended. "
     "The verb 'signifier' means to mean or signify."),
    (9, None,
     "'The contract clearly indicates a love scene.' Birag clings tightly to the literal phrasing. "
     "The verb 'indiquer' means to indicate or state."),
    (10, None,
     "'Beatrice refuses to shoot naked in this bag.' Andrea stands squarely behind her client's refusal. "
     "The masculine noun 'sac' refers to a bag or sack."),
    (11, None,
     "'Beatrice must resume shooting this afternoon.' The director issues a non-negotiable ultimatum. "
     "The noun 'apres-midi' designates the afternoon."),
    (12, None,
     "'Otherwise, we will declare a breach of contract.' Birag threatens formal legal retaliation. "
     "The feminine noun 'rupture' means breach or termination."),
    (13, None,
     "'We will defend our actress all the way!' Andrea vows complete loyalty to Beatrice. "
     "The idiom 'jusqu'au bout' means to the very end."),
]

OUTRO = (
    "Andrea Martel stands up courageously against artistic manipulation and legal intimidation. "
    "She protects Beatrice Dalle's dignity, knowing full well that a fierce legal battle with the producers lies ahead. "
    "Now let's listen to the scene once more."
)

CLOSING = ("lea", "Nous défendrons notre actrice jusqu'au bout!")
