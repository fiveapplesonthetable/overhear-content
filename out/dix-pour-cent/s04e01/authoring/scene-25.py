# Authoring module for dix-pour-cent s04e01 scene 25 (cues 1005-1009).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-25.py --out out/dix-pour-cent/s04e01/scene-25.json

ID = "dix-pour-cent-s04e01-scene-25"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 25
TITLE = "Loin de la fête  (Far from the Party)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1005-1009. Leaving the Cesar ceremony in a taxi, Noemie asks Mathias to skip the Fouquet's afterparty. "
    "She complains about her itchy dress and asks to return straight to the hotel so they can spend the night together."
)

INTRO = (
    "Driving through Paris in a taxi after the Cesar ceremony, Noemie convinces Mathias to skip the lavish afterparty at Fouquet's so they can escape the crowds. Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Veux-tu vraiment aller au grand dîner?",
     "Do you really want to go to the big dinner?",
     [(1005, "aller au Fouquet's")], "Noemie leans toward Mathias in the taxi"),
    ("lea", "Le Fouquet's est plein de monde.",
     "The Fouquet's is full of people.",
     [(1005, "aller au Fouquet's")], ""),
    ("lea", "Tout le monde va t'accaparer là-bas.",
     "Everyone will monopolize you over there.",
     [(1006, "va t'accaparer")], "Warns him of the industry crowds"),
    ("lea", "Je n'aurai pas une minute seule.",
     "I will not have a single minute alone.",
     [(1006, "pas une minute avec toi")], ""),
    ("lea", "Je veux passer la soirée ensemble.",
     "I want to spend the evening together.",
     [(1006, "pas une minute avec toi")], "Expresses her wish for private time"),
    ("mathias", "Nous faisons ce que tu souhaites.",
     "We do whatever you wish.",
     [(1007, "ce que tu veux, chéri")], "Mathias smiles affectionately"),
    ("mathias", "Tu es ma priorité absolue, chérie.",
     "You are my absolute priority, darling.",
     [(1007, "ce que tu veux, chéri")], ""),
    ("lea", "Je veux enlever cette robe rouge.",
     "I want to take off this red dress.",
     [(1008, "enlever cette robe maintenant")], "Noemie adjusts her uncomfortable gown"),
    ("lea", "Elle gratte depuis le début.",
     "It has been scratching since the beginning.",
     [(1009, "Elle gratte tellement")], ""),
    ("lea", "Ce tissu est un vrai cauchemar.",
     "This fabric is a real nightmare.",
     [(1009, "c'est un cauchemar")], "Laughs at the agony of red-carpet fashion"),
    ("mathias", "Tu étais splendide sur le tapis.",
     "You were splendid on the red carpet.",
     [(1007, "ce que tu veux, chéri")], "Compliments her look warmly"),
    ("lea", "Mais elle me fait souffrir terriblement.",
     "But it makes me suffer terribly.",
     [(1009, "c'est un cauchemar")], ""),
    ("mathias", "Alors, nous rentrons directement à l'hôtel.",
     "So, we return directly to the hotel.",
     [(1007, "ce que tu veux, chéri")], "Agrees to skip the reception completely"),
    ("lea", "C'est la meilleure idée de la soirée.",
     "That is the best idea of the evening.",
     [(1008, "enlever cette robe maintenant")], "Noemie relaxes with relief against his shoulder"),
]

OPENER = "Let's examine how Noemie and Mathias choose intimacy over industry glamour step by step."

WALK = [
    (0, None,
     "'Do you really want to go to the big dinner?' Noemie questions attending the official post-ceremony reception."),
    (1, None,
     "'The Fouquet's is full of people.' Noemie points out the overwhelming crowd waiting at the venue."),
    (2, None,
     "'Everyone will monopolize you over there.' Noemie predicts that filmmakers will crowd Mathias."),
    (3, None,
     "'I will not have a single minute alone.' Noemie regrets that they will have no privacy."),
    (4, None,
     "'I want to spend the evening together.' Noemie expresses her desire for quiet romance."),
    (5, None,
     "'We do whatever you wish.' Mathias gladly yields to her preferences."),
    (6, None,
     "'You are my absolute priority, darling.' Mathias reassures Noemie of his devotion."),
    (7, None,
     "'I want to take off this red dress.' Noemie confesses her immediate practical wish."),
    (8, None,
     "'It has been scratching since the beginning.' Noemie complains about the irritable material."),
    (9, None,
     "'This fabric is a real nightmare.' Noemie laughs about the uncomfortable designer gown."),
    (10, None,
     "'You were splendid on the red carpet.' Mathias compliments her elegant appearance."),
    (11, None,
     "'But it makes me suffer terribly.' Noemie jokes about paying the price for fashion."),
    (12, None,
     "'So, we return directly to the hotel.' Mathias gives instructions to skip the party."),
    (13, None,
     "'That is the best idea of the evening.' Noemie smiles with relief in the taxi."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "In the quiet privacy of the taxi, Noemie complains about her uncomfortable dress and Mathias happily agrees to bypass the industry party to spend the night alone with her."
CLOSING = ("mathias", "Nous faisons ce que tu souhaites.")
