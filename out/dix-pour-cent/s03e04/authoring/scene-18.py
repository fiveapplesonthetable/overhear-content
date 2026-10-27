# Authoring module for dix-pour-cent s03e04 scene 18 (cues 931-934).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-18.py --out out/dix-pour-cent/s03e04/scene-18.json

ID = "dix-pour-cent-s03e04-scene-18"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 18
TITLE = "Chez Noémie  (At Noémie's Apartment)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 931-934. Inside Noémie's apartment, Noémie prepares coffee while Mathias confesses that he cannot manage without her, "
    "asking her to forgive him and return to the agency."
)

INTRO = (
    "Inside Noémie's apartment, Noémie prepares coffee while Mathias confesses that he cannot manage without her, asking her to forgive him and return to the agency. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Entrez Mathias, posez votre manteau.",
     "Come in Mathias, put down your coat.",
     [(930, "J'arrive")], "Noémie welcomes Mathias inside"),
    ("mathias", "Merci Noémie, votre appartement est charmant.",
     "Thank you Noémie, your apartment is charming.",
     [(932, "Je vous ai pas demandé")], "Mathias compliments her living space"),
    ("lea", "Voulez-vous une tasse de café?",
     "Would you like a cup of coffee?",
     [(932, "vous voulez du café")], "Noémie offers fresh hot coffee"),
    ("mathias", "Avec grand plaisir, chère Noémie.",
     "With great pleasure, dear Noémie.",
     [(932, "du café")], "Mathias accepts with polite gratitude"),
    ("lea", "Prenez aussi ces bons croissants.",
     "Take these good croissants too.",
     [(932, "vous voulez")], "Noémie serves the breakfast pastries"),
    ("mathias", "Noémie, vous me manquez tellement.",
     "Noémie, I miss you so much.",
     [(933, "Je peux me passer de vous")], "Mathias expresses his emotional longing"),
    ("mathias", "Je ne peux plus me passer de vous.",
     "I can no longer manage without you.",
     [(933, "Je peux me passer de vous")], "Mathias confesses his deep dependence"),
    ("lea", "Pourtant, vous m'avez blessée autrefois.",
     "Yet, you hurt me in the past.",
     [(934, "Avec mon dos")], "Noémie recalls painful past memories"),
    ("mathias", "J'ai commis de terribles erreurs.",
     "I made terrible mistakes.",
     [(933, "de vous")], "Mathias openly acknowledges his wrongdoing"),
    ("mathias", "L'agence a besoin de vous.",
     "The agency needs you.",
     [(933, "passer de vous")], "Mathias highlights her professional worth"),
    ("mathias", "Et moi aussi, j'ai besoin de vous.",
     "And I too, I need you.",
     [(933, "de vous")], "Mathias speaks from personal vulnerability"),
    ("lea", "C'est difficile de tout oublier.",
     "It is difficult to forget everything.",
     [(934, "et tout")], "Noémie admits lingering hesitation"),
    ("mathias", "Revenez travailler avec moi, Noémie.",
     "Come back to work with me, Noémie.",
     [(933, "Je peux me passer de vous")], "Mathias makes a direct plea"),
    ("lea", "Laissez-moi un peu de temps.",
     "Give me a little time.",
     [(934, "je")], "Noémie asks for time to consider")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Come in Mathias, put down your coat.' Noémie invites him into her hallway. "
     "The polite imperative verbs offer domestic hospitality."),
    (1, None,
     "'Thank you Noémie, your apartment is charming.' Mathias compliments her interior decor. "
     "The appreciative adjective creates an intimate, warm tone."),
    (2, None,
     "'Would you like a cup of coffee?' Noémie prepares breakfast refreshments. "
     "The inverted modal question politely offers hot coffee."),
    (3, None,
     "'With great pleasure, dear Noémie.' Mathias accepts her breakfast offer. "
     "The courteous prepositional phrase conveys appreciative pleasure."),
    (4, None,
     "'Take these good croissants too.' Noémie lays out the fresh pastries. "
     "The friendly imperative encourages sharing the food."),
    (5, None,
     "'Noémie, I miss you so much.' Mathias speaks from the bottom of his heart. "
     "The pronominal construction expresses intense emotional absence."),
    (6, None,
     "'I can no longer manage without you.' Mathias admits his complete helplessness. "
     "The negative modal construction confesses essential professional and personal need."),
    (7, None,
     "'Yet, you hurt me in the past.' Noémie reminds him of broken promises. "
     "The compound past verb recalls past emotional wounds."),
    (8, None,
     "'I made terrible mistakes.' Mathias takes full personal responsibility. "
     "The compound past verb with an adjective demonstrates sincere remorse."),
    (9, None,
     "'The agency needs you.' Mathias appeals to her proven indispensability at ASK. "
     "The present verbal idiom underscores organizational reliance."),
    (10, None,
     "'And I too, I need you.' Mathias moves beyond business to personal truth. "
     "The emphatic personal pronoun stresses his own vulnerability."),
    (11, None,
     "'It is difficult to forget everything.' Noémie expresses natural caution. "
     "The impersonal construction reflects deep emotional scars."),
    (12, None,
     "'Come back to work with me, Noémie.' Mathias makes his heartfelt proposal. "
     "The imperative verb pleads for a fresh professional reunion."),
    (13, None,
     "'Give me a little time.' Noémie keeps the door open while asking for space. "
     "The gentle imperative seeks patience and emotional breathing room.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "Over warm coffee and croissants, Mathias lays his heart bare, begging Noémie to return to his side. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("lea", "Laissez-moi un peu de temps.")
