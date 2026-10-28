# Authoring module for dix-pour-cent s04e01 scene 26 (cues 1010-1012).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-26.py --out out/dix-pour-cent/s04e01/scene-26.json

ID = "dix-pour-cent-s04e01-scene-26"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 26
TITLE = "Folle de toi  (Mad About You)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1010-1012. Mathias laughs affectionately and tells Noemie she is completely mad. "
    "Noemie passionately declares that she is mad about him, and they embrace in the taxi as the episode ends."
)

INTRO = (
    "In the back of the taxi leaving the Cesar ceremony, Mathias laughs affectionately at Noemie's playful humor before she passionately declares her love. Let's listen to the scene in French first."
)

STORY = [
    ("mathias", "Tu es complètement folle, Noémie!",
     "You are completely mad, Noemie!",
     [(1010, "Tu es complètement folle")], "Mathias laughs affectionately"),
    ("lea", "Oui, je suis folle de toi!",
     "Yes, I am mad about you!",
     [(1011, "Folle de toi")], "Noemie declares her love joyfully"),
    ("mathias", "Tu me fais tellement rire.",
     "You make me laugh so much.",
     [(1010, "Tu es complètement folle")], ""),
    ("lea", "Nous commençons une nouvelle vie ensemble.",
     "We are starting a new life together.",
     [(1011, "Folle de toi")], "Noemie smiles tenderly"),
    ("mathias", "Tu as quitté l'agence pour moi.",
     "You left the agency for me.",
     [(1010, "Tu es complètement folle")], ""),
    ("lea", "Je te suivrais partout à Paris.",
     "I would follow you everywhere in Paris.",
     [(1011, "Folle de toi")], ""),
    ("mathias", "Nous serons libres avec notre société.",
     "We will be free with our company.",
     [(1010, "Tu es complètement folle")], "Mathias looks forward to their future"),
    ("lea", "Tu seras un producteur très puissant.",
     "You will be a very powerful producer.",
     [(1011, "Folle de toi")], ""),
    ("mathias", "Et tu seras ma plus proche alliée.",
     "And you will be my closest ally.",
     [(1010, "Tu es complètement folle")], ""),
    ("lea", "Je serai toujours à tes côtés.",
     "I will always be by your side.",
     [(1011, "Folle de toi")], "Reassures him of her unwavering devotion"),
    ("mathias", "Rien ne peut nous arrêter maintenant.",
     "Nothing can stop us now.",
     [(1010, "Tu es complètement folle")], ""),
    ("lea", "Embrasse-moi tendrement dans ce taxi.",
     "Kiss me tenderly in this taxi.",
     [(1011, "Folle de toi")], "Noemie leans into him with affection"),
    ("mathias", "C'est le début de notre triomphe.",
     "This is the beginning of our triumph.",
     [(1010, "Tu es complètement folle")], ""),
    ("lea", "Je t'aime de tout mon cœur.",
     "I love you with all my heart.",
     [(1011, "Folle de toi")], "They share a passionate kiss as Paris passes by"),
]

OPENER = "Let's examine Noemie and Mathias's tender and romantic final exchange line by line."

WALK = [
    (0, None,
     "'You are completely mad, Noemie!' Mathias laughs with deep affection in the dark cab. The adjective meaning 'mad' takes its feminine form here to match the noun it describes."),
    (1, None,
     "'Yes, I am mad about you!' Noemie cheerfully declares her passionate love for Mathias. The informal 'you' form around 'this line' marks a direct, personal relationship."),
    (2, None,
     "'You make me laugh so much.' Mathias appreciates her warmth and spontaneous humor. Mathias uses the casual singular 'you' with 'make', showing close familiarity."),
    (3, None,
     "'We are starting a new life together.' Noemie anticipates their fresh personal adventure. Notice how 'start' leads directly into the noun meaning 'life'."),
    (4, None,
     "'You left the agency for me.' Mathias acknowledges her bold sacrifice to stand with him. The informal 'you' form around 'have' marks a direct, personal relationship."),
    (5, None,
     "'I would follow you everywhere in Paris.' Noemie affirms her unwavering personal devotion. The informal 'you' form around 'would follow' marks a direct, personal relationship."),
    (6, None,
     "'We will be free with our company.' Mathias looks forward to creative independence. Notice how 'will be' leads directly into the noun meaning 'company'."),
    (7, None,
     "'You will be a very powerful producer.' Noemie expresses supreme confidence in his talent. The descriptive adjective for 'powerful' agrees in gender and number with its noun."),
    (8, None,
     "'And you will be my closest ally.' Mathias values her as an indispensable collaborator. Notice how 'will be' leads directly into the noun meaning 'ally'."),
    (9, None,
     "'I will always be by your side.' Noemie promises enduring personal loyalty. The informal 'you' form around 'will be' marks a direct, personal relationship."),
    (10, None,
     "'Nothing can stop us now.' Mathias feels invincible as they begin their venture. The two-part negative frame surrounds 'can' to mean 'nothing at all'."),
    (11, None,
     "'Kiss me tenderly in this taxi.' Noemie leans into Mathias as the city lights drift past. Notice how 'kiss' leads directly into the noun meaning 'taxi'."),
    (12, None,
     "'This is the beginning of our triumph.' Mathias smiles warmly in shared romantic triumph. The key noun here means 'beginning', anchored by its matching French article."),
    (13, None,
     "'I love you with all my heart.' Noemie closes the evening with a heartfelt vow."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "As Paris glides by through the taxi windows, Mathias and Noemie celebrate their shared love and professional partnership, sealing their future together with a passionate kiss as the season premiere concludes. When you watch the episode, listen out for the expressions meaning 'crazy' and 'laugh'. You'll catch them now. See you next time."
CLOSING = ("lea", "Oui, je suis folle de toi!")
