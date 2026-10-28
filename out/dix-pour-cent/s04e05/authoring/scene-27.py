# Authoring module for dix-pour-cent s04e05 scene 27 (cues 922-923).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e05/authoring/scene-27.py --out out/dix-pour-cent/s04e05/scene-27.json

ID = "dix-pour-cent-s04e05-scene-27"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 27
TITLE = "Vers un nouveau départ  (Toward a New Beginning)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Camille", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 922-923. Strolling along the Parisian quays, Camille and Mathias savor their newfound mutual trust as father "
    "and daughter, ready to face the future side by side."
)

INTRO = (
    "Under the soft afternoon sun, Camille and Mathias walk quietly along the riverbanks of the Seine. "
    "Having left the hospital and agency rivalries behind them, father and daughter take their first peaceful steps together toward a bright future. "
    "Let's listen to the scene in French first."
)

OPENER = "Let's look at Camille and Mathias taking their first steps toward reconciliation step by step."

STORY = [
    ("lea", "Regarde la belle lumière sur Paris.",
     "Look at the beautiful light over Paris.",
     [(922, "c'est bien")], "Camille admires the Parisian skyline"),
    ("mathias", "L'air frais me fait du bien.",
     "The fresh air does me good.",
     [(922, "c'est bien")], "Mathias takes a deep breath of outside air"),
    ("lea", "Tu respires mieux sans ce stress.",
     "You breathe better without that stress.",
     [(922, "c'est bien")], "Points out the positive physical change in him"),
    ("mathias", "Je laisse mes vieux conflits derrière.",
     "I leave my old conflicts behind.",
     [(922, "c'est bien")], "Resolves to abandon his corporate feuds"),
    ("lea", "C'est une nouvelle vie qui commence.",
     "It is a new life beginning.",
     [(922, "c'est bien")], "Welcomes their renewed perspective"),
    ("mathias", "Oui, un nouveau départ pour nous.",
     "Yes, a new start for us.",
     [(923, "Oui")], "Mathias nods with heartfelt conviction"),
    ("lea", "Nous formons une vraie famille désormais.",
     "We form a real family now.",
     [(922, "c'est bien")], "Affirms their deep familial bond"),
    ("mathias", "C'est le plus beau cadeau possible.",
     "It is the most beautiful gift possible.",
     [(922, "c'est bien")], "Mathias treasures this turning point in his life"),
    ("lea", "Prenons le temps de bien vivre.",
     "Let us take the time to live well.",
     [(922, "c'est bien")], "Urges him to savor everyday moments"),
    ("mathias", "C'est bien de marcher avec toi.",
     "It is good to walk with you.",
     [(922, "c'est bien")], "Expresses quiet happiness by her side"),
    ("lea", "Je reste toujours à tes côtés.",
     "I always stay by your side.",
     [(922, "c'est bien")], "Camille pledges her continuous presence"),
    ("mathias", "Notre avenir sera beaucoup plus calme.",
     "Our future will be much calmer.",
     [(922, "c'est bien")], "Envisions a serene future ahead"),
    ("lea", "Profitons ensemble de cette douce journée.",
     "Let us enjoy this gentle day together.",
     [(922, "c'est bien")], "Smiles up at the sunny Paris sky"),
    ("mathias", "Merci pour ton amour si précieux.",
     "Thank you for your precious love.",
     [(922, "c'est bien")], "Mathias thanks her from the bottom of his heart"),
]

WALK = [
    (0, None,
     "'Look at the beautiful light over Paris.' Camille observes the golden sunlight over the capital. The adjective meaning 'beautiful' takes its feminine form here to match the noun it describes."),
    (1, None,
     "'The fresh air does me good.' Mathias relishes being outside the clinical hospital walls. The verb meaning 'does' pairs naturally with the noun for 'air' in everyday conversation."),
    (2, None,
     "'You breathe better without that stress.' Camille notes his relaxed physical posture. The informal 'you' form around 'breathe' marks a direct, personal relationship."),
    (3, None,
     "'I leave my old conflicts behind.' Mathias decides to step back from unnecessary workplace warfare. The descriptive adjective for 'old' agrees in gender and number with its noun."),
    (4, None,
     "'It is a new life beginning.' Camille marks this pivotal moment as a fresh chapter. The verb meaning 'begins' pairs naturally with the noun for 'life' in everyday conversation."),
    (5, None,
     "'Yes, a new start for us.' Mathias agrees that their shared future begins now. The descriptive adjective for 'new' agrees in gender and number with its noun."),
    (6, None,
     "'We form a real family now.' Camille emphasizes the bond they have rebuilt together. The adjective meaning 'real' takes its feminine form here to match the noun it describes."),
    (7, None,
     "'It is the most beautiful gift possible.' Mathias regards their reconciliation as an invaluable blessing. The descriptive adjective for 'beautiful' agrees in gender and number with its noun."),
    (8, None,
     "'Let us take the time to live well.' Camille encourages mindful appreciation of life. Notice how 'let us take' leads directly into the noun meaning 'time'."),
    (9, None,
     "'It is good to walk with you.' Mathias expresses simple satisfaction in their companionship. Mathias uses the casual singular 'you' with 'walk', showing close familiarity."),
    (10, None,
     "'I always stay by your side.' Camille reaffirms her enduring support as his daughter. The informal 'you' form around 'stay' marks a direct, personal relationship."),
    (11, None,
     "'Our future will be much calmer.' Mathias anticipates a life with fewer professional pressures. Notice how 'will be' leads directly into the noun meaning 'future'."),
    (12, None,
     "'Let us enjoy this gentle day together.' Camille invites him to savor the peaceful afternoon. The adjective meaning 'gentle' takes its feminine form here to match the noun it describes."),
    (13, None,
     "'Thank you for your precious love.' Mathias concludes their walk with deep gratitude."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Strolling along the Seine after Mathias's hospital release, father and daughter celebrate their reconciled bond, leaving behind old conflicts to embark on a peaceful and honest future together. When you watch the episode, listen out for the expressions meaning 'look at' and 'beautiful'. You'll catch them now. See you next time."
CLOSING = ("mathias", "C'est bien de marcher avec toi.")
