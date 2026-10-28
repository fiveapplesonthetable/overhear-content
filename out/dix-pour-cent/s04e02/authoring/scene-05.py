# Authoring module for dix-pour-cent s04e02 scene 05 (cues 261-337).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-05.py --out out/dix-pour-cent/s04e02/scene-05.json

ID = "dix-pour-cent-s04e02-scene-05"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 5
TITLE = "La perle rare  (The Rare Pearl)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "arlette": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Camille", "arlette": "Arlette", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 261-337. Camille struggles to find an expressive actress for Valerie Donzelli's film, "
               "until Arlette advises her to seek real talent out in the Parisian streets.")

INTRO = ("At the ASK agency, Camille searches desperately for an unusual actress to satisfy director Valerie Donzelli. "
         "Arlette passes on legendary advice from founder Samuel Kerr about scouting authentic faces in the street. "
         "Let's listen to their exchange in French first.")

STORY = [
    ("lea", "La réalisatrice refuse toutes mes actrices.",
     "The director rejects all my actresses.",
     [(322, "Elle refuse toutes mes actrices.")], "Camille vents her frustration regarding casting decisions"),
    ("arlette", "Pourquoi? Tes comédiennes sont pourtant très bien.",
     "Why? Your actresses are very good though.",
     [(323, "Tes filles sont bien.")], "Arlette defends the quality of the agency roster"),
    ("lea", "Elle les trouve beaucoup trop banales.",
     "She finds them much too plain.",
     [(322, "trop banales")], "Camille quotes the director's harsh assessment"),
    ("lea", "Elle cherche une femme avec du relief.",
     "She is looking for a woman with character.",
     [(324, "pas assez de relief")], "Camille specifies the desired screen presence"),
    ("arlette", "Elle veut un personnage à la Almodovar?",
     "She wants an Almodovar-style character?",
     [(318, "un personnage à la Almodovar")], "Arlette pinpoints the director's aesthetic reference"),
    ("lea", "Oui, un visage unique et très expressif.",
     "Yes, a unique and very expressive face.",
     [(315, "elle veut un visage !")], "Camille confirms the need for strong visual personality"),
    ("arlette", "Samuel donnait toujours un très bon conseil.",
     "Samuel always gave very good advice.",
     [(326, "Samuel disait toujours")], "Arlette invokes the wisdom of ASK's founder"),
    ("lea", "Quel conseil? Dis-moi vite, Arlette!",
     "What advice? Tell me quickly, Arlette!",
     [(326, "cherche dans la rue")], "Camille eagerly asks for guidance"),
    ("arlette", "Cherche tes acteurs dans la rue!",
     "Look for your actors in the street!",
     [(326, "cherche dans la rue")], "Arlette shares Samuel's scouting philosophy"),
    ("arlette", "Il faut observer et les débusquer!",
     "You have to observe and track them down!",
     [(331, "Les débusquer !")], "Arlette encourages active instincts over talent catalogues"),
    ("lea", "Attends, je crois que j'ai trouvé!",
     "Wait, I think that I found her!",
     [(334, "J'ai trouvé.")], "Camille has a sudden flash of inspiration"),
    ("gabriel", "Qui as-tu trouvé? Une actrice connue?",
     "Who did you find? A famous actress?",
     [(335, "Mais j'ai trouvé !")], "Gabriel asks for details about this unexpected discovery"),
    ("lea", "Une touriste espagnole croisée dans le métro!",
     "A Spanish tourist crossed paths with in the subway!",
     [(264, "C'est ma première fois à Paris.")], "Camille remembers the dramatic woman at the metro turnstile"),
]

OPENER = "Let's explore Camille and Arlette's casting discussion line by line."

WALK = [
    (0, None,
     "'The director rejects all my actresses.' Camille explains that none of her submitted candidates pleased the director. Notice how 'refuses' leads directly into the noun meaning 'director'."),
    (1, None,
     "'Why? Your actresses are very good though.' Arlette expresses surprise, knowing the agency represents talented women. Arlette uses the casual singular 'you' with 'actresses', showing close familiarity."),
    (2, None,
     "'She finds them much too plain.' Camille relays that the production wants someone far less conventional. The clause hinges on the everyday verb meaning 'finds'."),
    (3, None,
     "'She is looking for a woman with character.' Camille clarifies that the role demands unique texture and grit. The verb meaning 'is looking for' pairs naturally with the noun for 'woman' in everyday conversation."),
    (4, None,
     "'She wants an Almodovar-style character?' Arlette recognizes the vibrant, melodramatic archetype being sought. In everyday spoken French, rising intonation on 'wants' at the end is enough to turn the sentence into a question."),
    (5, None,
     "'Yes, a unique and very expressive face.' Camille affirms that the part requires intense visual charisma. The descriptive adjective for 'unique' agrees in gender and number with its noun."),
    (6, None,
     "'Samuel always gave very good advice.' Arlette reflects on how Samuel Kerr handled impossible casting requests. Notice how 'gave' leads directly into the noun meaning 'advice.'."),
    (7, None,
     "'What advice? Tell me quickly, Arlette!' Camille asks for Samuel's secret technique. The verb meaning 'tell me' pairs naturally with the noun for 'advice?' in everyday conversation."),
    (8, None,
     "'Look for your actors in the street!' Arlette reveals that great natural performers are found in everyday life. The informal 'you' form around 'look for' marks a direct, personal relationship."),
    (9, None,
     "'You have to observe and track them down!' Arlette urges Camille to rely on keen intuition rather than agency files. The clause hinges on the everyday verb meaning 'is necessary'."),
    (10, None,
     "'Wait, I think that I found her!' Camille suddenly connects Arlette's advice to a real morning encounter. Notice how the short vowel drops before a vowel sound around 'wait', making the phrase flow smoothly as one unit."),
    (11, None,
     "'Who did you find? A famous actress?' Gabriel inquires whether Camille discovered a celebrated film star. The adjective meaning 'famous?' takes its feminine form here to match the noun it describes."),
    (12, None,
     "'A Spanish tourist crossed paths with in the subway!' Camille recalls the passionate foreign traveler from the subway station. Notice how 'crossed paths with' leads directly into the noun meaning 'tourist'."),
]

TRANSITION = "Now let's listen to Camille and Arlette's dialogue once more from start to finish."

OUTRO = ("Camille learns that real cinematic presence often hides in everyday encounters outside agency offices. "
         "Let's review the key casting and observation vocabulary from this scene.")

CLOSING = ("lea", "Une touriste espagnole croisée dans le métro!")
