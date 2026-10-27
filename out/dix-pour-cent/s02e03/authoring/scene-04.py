# Authoring module for dix-pour-cent s02e03 scene 04 (cues 92-116).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-04.py --out out/dix-pour-cent/s02e03/scene-04.json

ID = "dix-pour-cent-s02e03-scene-04"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 4
TITLE = "Matinée chez ASK  (Morning at ASK)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Camille", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 92-116. Camille approaches Mathias at the agency and convinces him "
               "to have coffee with her visiting mother Annick. Adapted for A1 French.")

INTRO = ("At the ASK agency, the agents and assistants begin a busy morning. "
         "Camille approaches Mathias to ask him to meet her visiting mother Annick for lunch, "
         "putting Mathias in an awkward personal situation. Let's listen to the scene in French first.")

STORY = [
 ("lea", "Mathias, bonjour, tu as une minute?",
  "Mathias, hello, do you have a minute?",
  [(94, "-Bonjour.")], "Added polite request for attention"),
 ("mathias", "Bonjour Camille, je suis très pressé.",
  "Good morning Camille, I am in a hurry.",
  [(94, "-Bonjour.")], "Added busy excuse"),
 ("lea", "Je t'ai dit que maman était là?",
  "Did I tell you that mom was here?",
  [(95, "Je t'ai dit que maman était là ?")], "Kept exact dialogue"),
 ("mathias", "Oui, je crois. Quand est-elle arrivée?",
  "Yes, I think so. When did she arrive?",
  [(96, "Je crois. Quand ?")], "Formulated complete sentence"),
 ("lea", "Elle vient d'arriver à Paris ce matin.",
  "She just arrived in Paris this morning.",
  [(97, "Elle vient d'arriver.")], "Added city and morning time"),
 ("lea", "Si on déjeune, tu pourrais nous rejoindre.",
  "If we have lunch, you could join us.",
  [(98, "Si je l'emmène déjeuner quelque part près d'ici,"), (99, "tu pourrais nous rejoindre.")], "Streamlined invitation"),
 ("mathias", "C'est impossible, je n'ai pas le temps.",
  "It is impossible, I do not have time.",
  [(100, "Je n'ai pas le temps.")], "Prefaced with clear refusal"),
 ("lea", "Demain ou vendredi, elle reste toute la semaine.",
  "Tomorrow or Friday, she is staying all week.",
  [(101, "Demain, ou vendredi ? Elle est là toute la semaine...")], "Combined scheduling options"),
 ("lea", "S'il te plaît, ça me ferait vraiment plaisir.",
  "Please, it would really make me happy.",
  [(103, "S'il te plaît, ça me ferait vraiment plaisir.")], "Kept exact emotional appeal"),
 ("lea", "Ça ferait plaisir à maman aussi.",
  "It would please mom as well.",
  [(104, "À elle aussi.")], "Expanded elliptical phrase"),
 ("mathias", "Ne me regarde pas avec cet air triste.",
  "Do not look at me with that sad look.",
  [(105, "Épargne-moi ton air de chien battu.")], "Replaced idiom with simple descriptive phrase"),
 ("mathias", "D'accord, demain, juste pour le café.",
  "All right, tomorrow, just for coffee.",
  [(106, "Demain. Pour le café.")], "Added agreement and restrictive marker"),
 ("lea", "Merci Mathias, c'est super gentil.",
  "Thank you Mathias, that is super nice.",
  [(106, "Demain. Pour le café.")], "Added warm thank you"),
 ("mathias", "Mais pas un mot aux autres agents.",
  "But not a word to the other agents.",
  [(106, "Demain. Pour le café.")], "Added discreet condition"),
]

OPENER = "Let's examine how Camille convinces Mathias to have coffee with her mother."

WALK = [
 (0, None,
  "'Mathias, hello, do you have a minute?' A polite greeting followed by a request for brief attention."),
 (1, None,
  "'Good morning Camille, I am in a hurry.' A busy professional acknowledgement indicating lack of time."),
 (2, None,
  "'Did I tell you that mom was here?' A compound past question introducing family news."),
 (3, None,
  "'Yes, I think so. When did she arrive?' An interrogative inquiring about the timing of her arrival."),
 (4, None,
  "'She just arrived in Paris this morning.' A recent past construction using 'venir de' with an infinitive."),
 (5, None,
  "'If we have lunch, you could join us.' A conditional proposal suggesting a shared informal meal."),
 (6, None,
  "'It is impossible, I do not have time.' A direct refusal citing professional unavailability."),
 (7, None,
  "'Tomorrow or Friday, she is staying all week.' A temporal alternative offering flexible scheduling."),
 (8, None,
  "'Please, it would really make me happy.' A polite formula followed by a conditional expression of pleasure."),
 (9, None,
  "'It would please mom as well.' An indirect object construction extending the personal request."),
 (10, None,
  "'Do not look at me with that sad look.' A negative imperative reacting to an emotional expression."),
 (11, None,
  "'All right, tomorrow, just for coffee.' A reluctant concession agreeing to a brief morning encounter."),
 (12, None,
  "'Thank you Mathias, that is super nice.' A warm expression of gratitude acknowledging the effort."),
 (13, None,
  "'But not a word to the other agents.' A discreet warning maintaining workplace confidentiality."),
]

TRANSITION = "Now let's listen to Camille and Mathias's quiet discussion again at full speed."

OUTRO = ("Mathias reluctantly agrees to a quick coffee with Annick, fearing that their shared past might be uncovered. "
         "Camille is relieved, though keeping their family connection secret remains a daily challenge.")

CLOSING = ("lea", "Merci beaucoup, Mathias.")
