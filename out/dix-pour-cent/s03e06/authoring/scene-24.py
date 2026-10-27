# Authoring module for dix-pour-cent s03e06 scene 24 (cues 1222-1290).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-24.py --out out/dix-pour-cent/s03e06/scene-24.json

ID = "dix-pour-cent-s03e06-scene-24"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 24
TITLE = "Le discours des trente ans  (The Thirty-Year Speech)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1222-1290. On the gala stage, Hicham delivers a moving speech celebrating thirty years of ASK and honoring Arlette. "
    "Off-stage, Andrea confronts Mathias, revealing that the team has united and defeated his takeover plan."
)

INTRO = (
    "On the gala stage, Hicham delivers a moving speech celebrating thirty years of ASK and honoring Arlette. "
    "Off-stage, Andrea confronts Mathias, revealing that the team has united and defeated his takeover plan. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("hicham", "Bonsoir tout le monde, soyez les bienvenus!",
     "Good evening everyone, be welcome!",
     [(1246, "Bonsoir, tout le monde")], "Welcomed the gathered assembly warmly"),
    ("hicham", "Merci d'être venus si nombreux ce soir.",
     "Thank you for coming in such numbers tonight.",
     [(1250, "Merci d'être venus si nombreux")], "Expressed gratitude for the enormous turnout"),
    ("hicham", "La réussite chez ASK est toujours collective.",
     "Success at ASK is always collective.",
     [(1252, "la réussite à SK, elle est collective")], "Stressed the collaborative nature of success"),
    ("hicham", "ASK n'existerait pas sans vous tous.",
     "ASK would not exist without all of you.",
     [(1257, "SK n'existerait pas sans vous tous")], "Acknowledged the vital support of everyone"),
    ("hicham", "Ce soir, célébrons le talent des agents.",
     "Tonight, let us celebrate the talent of agents.",
     [(1260, "ce sont ceux de vos agents")], "Dedicated the gala honors to agency staff"),
    ("hicham", "Une personne incarne véritablement notre belle agence.",
     "One person truly embodies our fine agency.",
     [(1264, "Quelqu'un qui incarne véritablement SK")], "Introduced the iconic guest of honor"),
    ("hicham", "La très grande et irremplaçable Arlette!",
     "The very great and irreplaceable Arlette!",
     [(1271, "La très grande Arlette")], "Announced Arlette with reverence"),
    ("hicham", "Sans elle, nous ne serions rien aujourd'hui.",
     "Without her, we would be nothing today.",
     [(1272, "Sans elle, on serait pas là ce soir")], "Credited her with the existence of ASK"),
    ("lea", "Tout le public applaudit avec une vive émotion.",
     "The whole audience applauds with deep emotion.",
     [(1273, "Merci, Arlette")], "Described the room standing ovation"),
    ("lea", "Mathias voulait annoncer son départ en public.",
     "Mathias wanted to announce his departure in public.",
     [(1283, "devant tout le monde")], "Noted his intended dramatic defection"),
    ("lea", "Mais ce n'est pas du tout élégant.",
     "But that is not elegant at all.",
     [(1283, "C'est pas très classe")], "Criticized his lack of style"),
    ("lea", "Tu as sous-estimé tes propres collègues, Mathias.",
     "You underestimated your own colleagues, Mathias.",
     [(1285, "Tu as sous-estimé tes collègues, Mathias")], "Pointed out his fatal miscalculation"),
    ("lea", "Nous nous sommes unis pour sauver l'agence.",
     "We united to save the agency.",
     [(1288, "ils les ont retournés")], "Explained their secret coalition"),
    ("lea", "Tu as joué en solitaire et tu as perdu.",
     "You played solo and you lost.",
     [(1290, "t'as perdu")], "Delivered the final verdict")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Good evening everyone, be welcome!' Hicham greets the glittering gala crowd. "
     "The welcoming formula opens the official anniversary ceremony."),
    (1, None,
     "'Thank you for coming in such numbers tonight.' Hicham smiles at the packed ballroom. "
     "The courteous phrase thanks the assembled artists and partners."),
    (2, None,
     "'Success at ASK is always collective.' Hicham highlights their shared ethos. "
     "The predicate adjective underscores team solidarity over personal ego."),
    (3, None,
     "'ASK would not exist without all of you.' Hicham honors the artists and employees. "
     "The conditional verb construction expresses essential dependence."),
    (4, None,
     "'Tonight, let us celebrate the talent of agents.' Hicham turns the spotlight onto his colleagues. "
     "The first-person plural imperative invites joint celebration."),
    (5, None,
     "'One person truly embodies our fine agency.' Hicham prepares the crowd for a legend. "
     "The transitive verb introduces the symbolic pillar of ASK."),
    (6, None,
     "'The very great and irreplaceable Arlette!' Hicham names the veteran agent with admiration. "
     "The exclamatory phrase draws enthusiastic cheers from the room."),
    (7, None,
     "'Without her, we would be nothing today.' Hicham delivers his ultimate tribute. "
     "The negative conditional clause credits her foundational role."),
    (8, None,
     "'The whole audience applauds with deep emotion.' Andrea takes in the roaring applause. "
     "The present tense sentence describes the heartfelt ovation for Arlette."),
    (9, None,
     "'Mathias wanted to announce his departure in public.' Andrea recalls his intended rebellion. "
     "The imperfect modal verb highlights his planned betrayal."),
    (10, None,
     "'But that is not elegant at all.' Andrea condemns such bitterness on an anniversary night. "
     "The colloquial negation rejects spiteful theater."),
    (11, None,
     "'You underestimated your own colleagues, Mathias.' Andrea confronts him directly off-stage. "
     "The compound past verb diagnoses his major tactical blunder."),
    (12, None,
     "'We united to save the agency.' Andrea reveals the solidarity of the other agents. "
     "The reflexive compound past verb shows collective defense."),
    (13, None,
     "'You played solo and you lost.' Andrea delivers the blunt conclusion of the season. "
     "The parallel compound past verbs seal his complete isolation.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "As Hicham leads the room in celebrating Arlette, Andrea delivers a stinging lesson to a defeated Mathias. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("lea", "Tu as joué en solitaire et tu as perdu.")
