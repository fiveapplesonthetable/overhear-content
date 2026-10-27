# Authoring module for dix-pour-cent s03e05 scene 05 (cues 110-119).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-05.py --out out/dix-pour-cent/s03e05/scene-05.json

ID = "dix-pour-cent-s03e05-scene-05"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 5
TITLE = "Trente ans d'ASK  (Thirty Years of ASK)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "marcel", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 110-119. After Hicham storms out of a heated meeting, Mathias, Gabriel, and Andrea "
               "react to his animal metaphors and worry about ASK's upcoming thirtieth anniversary. Adapted for A1 French.")

INTRO = ("In the meeting room at ASK, Hicham Janowski has just stormed out after an angry confrontation about agency finances. "
         "Mathias, Gabriel, and Andrea stay behind to discuss his outburst and the upcoming agency anniversary. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("mathias", "Hicham est vraiment furieux contre nous.",
     "Hicham is truly furious with us.",
     [(110, "Avec tout ce que je vous ai donné")], "Mathias takes in the shouting"),
    ("gabriel", "Il a peur de perdre son investissement.",
     "He is afraid of losing his investment.",
     [(112, "perdre la moitié de mon investissement")], "Gabriel understands Hicham's panic"),
    ("lea", "Il n'arrête pas de nous crier dessus.",
     "He does not stop shouting at us.",
     [(113, "déconner sur toute la ligne")], "Andrea vents her frustration"),
    ("mathias", "Il a parlé de vache à lait!",
     "He spoke of a cash cow!",
     [(114, "vache à lait")], "Mathias cites the farm idiom"),
    ("gabriel", "Et aussi de dindon de la farce!",
     "And also of a fall guy!",
     [(115, "Le dindon de la farce ?")], "Gabriel recalls the other animal insult"),
    ("lea", "Il nous a dit de gérer notre merdier.",
     "He told us to sort out our mess.",
     [(116, "gérez votre merdier")], "Andrea repeats Hicham's exact command"),
    ("mathias", "Il est très métaphore animalière, non?",
     "He is very into animal metaphors, isn't he?",
     [(117, "Il est très métaphore animalière, Hicham, non ?")], "Mathias finds humor in the rant"),
    ("gabriel", "C'est vrai, il adore les animaux!",
     "That is true, he loves animals!",
     [(117, "métaphore animalière")], "Gabriel chuckles at the observation"),
    ("lea", "Mais la situation reste très grave.",
     "But the situation remains very serious.",
     [(118, "En attendant")], "Andrea redirects to agency realities"),
    ("mathias", "Nous devons fêter l'anniversaire d'ASK.",
     "We must celebrate ASK's anniversary.",
     [(118, "il est 30 ans d'ASK")], "Mathias reminds them of the party"),
    ("gabriel", "Ce sont bientôt les trente ans.",
     "The thirty years are coming soon.",
     [(118, "30 ans d'ASK")], "Gabriel checks the approaching date"),
    ("lea", "Ça risque de ressembler à des funérailles!",
     "It is likely to look like a funeral!",
     [(119, "Ça risque fort de ressembler à des funérailles")], "Andrea warns of a dark atmosphere"),
    ("mathias", "Nous devons trouver une solution rapide.",
     "We must find a quick solution.",
     [(116, "gérez votre merdier")], "Mathias urges everyone to take action"),
]

OPENER = "Let's explore how the three partners react to Hicham's rant line by line."

WALK = [
    (0, None,
     "'Hicham is truly furious with us.' Mathias summarizes the tense mood left behind by Hicham's sudden departure."),
    (1, None,
     "'He is afraid of losing his investment.' Gabriel points out the financial panic driving their boss."),
    (2, None,
     "'He does not stop shouting at us.' Andrea notes the aggressive tone directed at the agency partners."),
    (3, None,
     "'He spoke of a cash cow!' Mathias quotes Hicham's colorful complaint about funding the agency."),
    (4, None,
     "'And also of a fall guy!' Gabriel repeats another humorous animal phrase from Hicham's tirade."),
    (5, None,
     "'He told us to sort out our mess.' Andrea recalls Hicham's sharp parting command."),
    (6, None,
     "'He is very into animal metaphors, isn't he?' Mathias jokes about Hicham's vivid choice of words."),
    (7, None,
     "'That is true, he loves animals!' Gabriel laughs at the recurring farm animal references."),
    (8, None,
     "'But the situation remains very serious.' Andrea brings everyone back to their urgent business reality."),
    (9, None,
     "'We must celebrate ASK's anniversary.' Mathias mentions the major celebration planned for the agency."),
    (10, None,
     "'The thirty years are coming soon.' Gabriel reminds them that the milestone date is approaching fast."),
    (11, None,
     "'It is likely to look like a funeral!' Andrea fears the party will turn into a gloomy disaster."),
    (12, None,
     "'We must find a quick solution.' Mathias urges the partners to take immediate action."),
]

TRANSITION = "Now let's listen to the partners' conversation once more from start to finish."

OUTRO = ("Mathias, Gabriel, and Andrea joke about Hicham's colorful phrasing while confronting the reality of ASK's crisis. "
         "Let's review the key vocabulary from this office scene.")

CLOSING = ("lea", "Ça risque de ressembler à des funérailles!")
