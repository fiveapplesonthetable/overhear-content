# Authoring module for dix-pour-cent s03e04 scene 23 (cues 1221-1259).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-23.py --out out/dix-pour-cent/s03e04/scene-23.json

ID = "dix-pour-cent-s03e04-scene-23"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 23
TITLE = "Le secret d'Isabelle Huppert  (Isabelle Huppert's Secret)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "marcel"}
LABELS = {"lea": "Isabelle", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 1221-1259. Gabriel visits Isabelle Huppert at her apartment to make sure she is resting "
               "after halting production, only to discover she is secretly shooting an experimental film.")

INTRO = ("At Isabelle Huppert's Parisian apartment, Gabriel drops by to ensure his exhausted star actress is finally resting. "
         "Instead of relaxing in bed, Isabelle confesses that she is secretly filming an experimental indie project in her living room. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's explore the dialogue line by line and examine the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to consolidate the expressions."

STORY = [
 ("gabriel", "Comment ça va, toi?",
  "How are you doing?",
  [(1221, "Ça va, toi")], "Checking on Isabelle"),
 ("lea", "Je m'en veux un peu.",
  "I blame myself a little.",
  [(1222, "Je m'en veux.")], "Feeling guilty"),
 ("lea", "L'assurance va couvrir l'interruption?",
  "Will the insurance cover the shutdown?",
  [(1227, "l'interruption du tournage")], "Asking about insurance"),
 ("gabriel", "Ce n'est pas ton problème.",
  "It is not your problem.",
  [(1228, "ton problème.")], "Reassuring her"),
 ("gabriel", "Tu te reposes à la maison.",
  "You rest at home.",
  [(1232, "tu te reposes")], "Insisting on rest"),
 ("lea", "Je ne bouge plus maintenant.",
  "I am not moving anymore now.",
  [(1234, "je ne bouge plus")], "Promising to stay still"),
 ("gabriel", "Mais tu fais quoi, là?",
  "But what are you doing here?",
  [(1244, "tu fais quoi, là")], "Noticing film set"),
 ("gabriel", "Tu tournes un film chez toi?",
  "Are you shooting a movie at home?",
  [(1245, "tu tournes un film")], "Expressing shock"),
 ("lea", "C'est un petit film expérimental.",
  "It is a small experimental film.",
  [(1248, "film, comme ça, expérimental.")], "Explaining project"),
 ("lea", "On fait ça vite fait.",
  "We are doing this quickly.",
  [(1250, "vite fait bien fait.")], "Downplaying production"),
 ("gabriel", "Il faut que tu te reposes.",
  "You need to rest.",
  [(1255, "Il faut que tu te reposes.")], "Reiterating doctor orders"),
 ("lea", "Mais nous nous amusons tellement.",
  "But we are having so much fun.",
  [(1256, "on s'amuse.")], "Defending artistic joy"),
 ("lea", "Pas de contrat, pas de producteur.",
  "No contract, no producer.",
  [(1257, "pas de contrat, pas de producteur.")], "Emphasizing freedom"),
 ("lea", "Juste la caméra et moi.",
  "Just the camera and me.",
  [(1259, "Et moi.")], "Pure love of cinema"),
]

WALK = [
 (0, None,
  "'How are you doing?' Gabriel asks Isabelle warmly as he arrives at her home. "
  "The expression 'comment ca va' checks on someone's well-being."),
 (1, None,
  "'I blame myself a little.' Isabelle admits she feels guilty about exhausting herself. "
  "The pronominal idiom 's'en vouloir' means to feel guilty or blame oneself."),
 (2, None,
  "'Will the insurance cover the shutdown?' Isabelle worries about the financial consequences of interrupting the shoot. "
  "The noun 'interruption' denotes temporary halting of work."),
 (3, None,
  "'It is not your problem.' Gabriel reassures her that financial matters belong to the producers. "
  "The possessive adjective 'ton' agrees with masculine singular nouns."),
 (4, None,
  "'You rest at home.' Gabriel insists she take care of herself and stay in bed. "
  "The reflexive verb 'se reposer' means to rest."),
 (5, None,
  "'I am not moving anymore now.' Isabelle promises she will not leave the apartment. "
  "The negative structure 'ne plus' indicates an action has ceased."),
 (6, None,
  "'But what are you doing here?' Gabriel suddenly spots film equipment and cameras in her living room. "
  "The adverb 'quoi' is used in informal spoken questions."),
 (7, None,
  "'Are you shooting a movie at home?' Gabriel realizes in disbelief that a film crew is present. "
  "The verb 'tourner' means to shoot or film a movie."),
 (8, None,
  "'It is a small experimental film.' Isabelle explains the artistic nature of the spontaneous project. "
  "The adjective 'experimental' describes avant-garde filmmaking."),
 (9, None,
  "'We are doing this quickly.' Isabelle describes the informal speed of the low-budget production. "
  "The colloquial idiom 'vite fait' means done quickly or knocked out rapidly."),
 (10, None,
  "'You need to rest.' Gabriel reminds her firmly of her doctor's orders. "
  "The impersonal expression 'il faut que' takes a subjunctive verb clause."),
 (11, None,
  "'But we are having so much fun.' Isabelle defends her passion for filmmaking without commercial pressure. "
  "The reflexive verb 's'amuser' means to have fun or enjoy oneself."),
 (12, None,
  "'No contract, no producer.' Isabelle celebrates the pure freedom of making cinema without bureaucracy. "
  "The negative preposition 'pas de' expresses complete absence."),
 (13, None,
  "'Just the camera and me.' Isabelle concludes with poetic dedication to her lifelong craft. "
  "The adverb 'juste' emphasizes simplicity and purity."),
]

OUTRO = ("Gabriel realizes that no contract or doctor's order can ever keep Isabelle away from the camera. "
         "Her boundless passion for cinema defines her extraordinary dedication to her art. "
         "Now, let's review the scene one last time.")

CLOSING = ("lea", "Juste la caméra et moi.")
