# Authoring module for dix-pour-cent s03e06 scene 13 (cues 621-622).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s03e06/scene-13.json

ID = "dix-pour-cent-s03e06-scene-13"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 13
TITLE = "La doublure sur le plateau  (The Double on Set)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "directeur": "theo"}
LABELS = {"lea": "Gabriel", "directeur": "Le réalisateur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 621-622. On the movie set, Gabriel and the director film the ghost scene "
               "using Isabelle Huppert's stand-in double.")

INTRO = ("On the dimly lit film set, Gabriel is trying to keep the production moving forward smoothly. "
         "With Isabelle away at the agency party, her stand-in double steps into the role of the mysterious ghost. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Regarde cette silhouette dans la brume.",
  "Look at this silhouette in the mist.",
  [(621, "Cette pâleur spectrale")], "Observing ghost"),
 ("directeur", "Cette pâleur spectrale me semble étrange.",
  "That ghostly pallor seems strange to me.",
  [(621, "Cette pâleur spectrale")], "Critiquing look"),
 ("lea", "C'est l'effet voulu par l'histoire.",
  "It is the effect intended by the story.",
  [(621, "ce regard, mais qui est de vous")], "Defending effect"),
 ("directeur", "Son regard ne me rappelle personne.",
  "Her look reminds me of nobody.",
  [(621, "ce regard, mais qui est de vous")], "Questioning gaze"),
 ("lea", "Elle incarne un fantôme sans nom.",
  "She embodies a nameless ghost.",
  [(621, "Je sais plus")], "Explaining ghost"),
 ("directeur", "Le public va reconnaître la doublure.",
  "The audience will recognize the stand-in.",
  [(622, "J'ai changé de visage")], "Fearing recognition"),
 ("lea", "L'éclairage masque tous les traits.",
  "The lighting conceals all features.",
  [(622, "J'ai changé de visage")], "Assuring lighting"),
 ("directeur", "Elle doit dire la phrase clé.",
  "She must say the key sentence.",
  [(622, "J'ai changé de visage")], "Demanding line"),
 ("lea", "J'ai changé de visage.",
  "I changed my face.",
  [(622, "J'ai changé de visage")], "Reciting line"),
 ("directeur", "Cette réplique fonctionne très bien.",
  "This line works very well.",
  [(622, "J'ai changé de visage")], "Approving line"),
 ("lea", "La magie du cinéma opère toujours.",
  "Cinema magic always works.",
  [(621, "Cette pâleur spectrale")], "Praising cinema"),
 ("directeur", "Tournons cette prise sans attendre.",
  "Let's film this take without waiting.",
  [(621, "Cette pâleur spectrale")], "Deciding to film"),
 ("lea", "Silence sur le plateau, s'il vous plaît!",
  "Silence on set, please!",
  [(621, "Cette pâleur spectrale")], "Calling for quiet"),
 ("directeur", "Action! Tout le monde est prêt.",
  "Action! Everyone is ready.",
  [(621, "Cette pâleur spectrale")], "Starting take"),
]

WALK = [
 (0, None,
  "'Look at this silhouette in the mist.' Gabriel points toward the mysterious actress. "
  "The imperative form 'regarde' is used to draw attention."),
 (1, None,
  "'That ghostly pallor seems strange to me.' The director studies her unusual appearance. "
  "The adjective 'spectrale' evokes an eerie apparition."),
 (2, None,
  "'It is the effect intended by the story.' Gabriel justifies the eerie visual tone. "
  "The past participle 'voulu' acts as an adjective."),
 (3, None,
  "'Her look reminds me of nobody.' The director feels the face is unfamiliar. "
  "The verb 'rappeler' means to remind or call to mind."),
 (4, None,
  "'She embodies a nameless ghost.' Gabriel explains the mystical role. "
  "The noun 'fantome' describes a spirit from beyond."),
 (5, None,
  "'The audience will recognize the stand-in.' The director worries about viewer scrutiny. "
  "The noun 'doublure' refers to an actor substitute."),
 (6, None,
  "'The lighting conceals all features.' Gabriel explains the visual illusion. "
  "The verb 'masquer' means to hide or obscure from view."),
 (7, None,
  "'She must say the key sentence.' The director insists on the crucial dialogue line. "
  "The noun 'cle' figuratively designates something essential."),
 (8, None,
  "'I changed my face.' Gabriel quotes the mysterious character line. "
  "The passe compose 'ai change' describes a completed transformation."),
 (9, None,
  "'This line works very well.' The director appreciates the poetic phrasing. "
  "The verb 'fonctionner' means to work effectively."),
 (10, None,
  "'Cinema magic always works.' Gabriel praises the power of artistic illusion. "
  "The verb 'operer' means to produce an intended effect."),
 (11, None,
  "'Let's film this take without waiting.' The director decides to start rolling. "
  "The imperative 'tournons' invites immediate shooting."),
 (12, None,
  "'Silence on set, please!' Gabriel calls for absolute quiet around the cameras. "
  "The politeness formula 's'il vous plait' is essential."),
 (13, None,
  "'Action! Everyone is ready.' The director begins the crucial camera take. "
  "The adjective 'pret' indicates readiness to perform."),
]

OUTRO = ("Gabriel manages to reassure the director about the stand-in's eerie performance on set. "
         "The scene is salvaged just in time, allowing the secret plan to continue. "
         "Now, let's review the scene one last time.")

CLOSING = ("directeur", "Action! Tout le monde est prêt.")
