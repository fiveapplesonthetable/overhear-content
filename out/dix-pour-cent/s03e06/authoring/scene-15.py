# Authoring module for dix-pour-cent s03e06 scene 15 (cues 627-638).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-15.py --out overhear-content/out/dix-pour-cent/s03e06/scene-15.json

ID = "dix-pour-cent-s03e06-scene-15"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 15
TITLE = "La mission secrète de Renard  (Renard's Secret Mission)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "renard": "theo"}
LABELS = {"lea": "Mathias", "renard": "Renard"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 627-638. Outside ASK, Mathias assigns a confidential mission "
               "to security guard Renard.")

INTRO = ("Outside the agency building, the preparations for the grand anniversary party are underway. "
         "Mathias approaches the security guard Renard to give him an urgent and confidential assignment. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Ça va, Renard?",
  "Are you alright, Renard?",
  [(627, "Ça va, Renard ?")], "Greeting guard"),
 ("renard", "Ça va, tout se passe bien.",
  "Everything is going fine.",
  [(628, "Ça va, ça se rend bien")], "Reporting status"),
 ("lea", "J'ai une mission spéciale pour toi.",
  "I have a special mission for you.",
  [(629, "j'ai une mission spéciale pour toi")], "Giving mission"),
 ("renard", "Je t'écoute attentivement, Mathias.",
  "I am listening attentively, Mathias.",
  [(630, "Je t'écoute")], "Listening to instructions"),
 ("lea", "Deux invités américains vont arriver ce soir.",
  "Two American guests will arrive tonight.",
  [(631, "il y a deux Américains qui vont arriver")], "Announcing guests"),
 ("renard", "Tu as leurs noms précis?",
  "Do you have their exact names?",
  [(631, "Marcel Amos, Scott Downing")], "Asking for names"),
 ("lea", "Marcel Amos et Scott Downing.",
  "Marcel Amos and Scott Downing.",
  [(631, "Marcel Amos, Scott Downing")], "Giving names"),
 ("renard", "À quelle heure arrivent-ils ici?",
  "At what time do they arrive here?",
  [(631, "À 22h")], "Asking time"),
 ("lea", "Ils arrivent précisément à vingt-deux heures.",
  "They arrive precisely at ten PM.",
  [(631, "À 22h")], "Stating hour"),
 ("renard", "Que dois-je faire exactement?",
  "What must I do exactly?",
  [(632, "tu me préviennes")], "Asking instructions"),
 ("lea", "Préviens-moi dès leur arrivée en bas.",
  "Notify me as soon as they arrive downstairs.",
  [(632, "tu me préviennes quand ils sont en bas")], "Giving order"),
 ("renard", "Cette affaire reste ultra confidentielle?",
  "Does this matter stay strictly confidential?",
  [(634, "Ultra confidentiel, hein")], "Confirming secrecy"),
 ("lea", "Oui, personne ne doit savoir cela.",
  "Yes, nobody must know that.",
  [(634, "Ultra confidentiel, hein")], "Demanding discretion"),
 ("renard", "Je garde le secret absolu.",
  "I keep absolute secrecy.",
  [(636, "Je peux compter sur toi")], "Promising silence"),
]

WALK = [
 (0, None,
  "'Are you alright, Renard?' Mathias greets the security guard. "
  "The familiar question 'ca va' is standard in French greetings."),
 (1, None,
  "'Everything is going fine.' Renard reports that all operations are running smoothly. "
  "The pronominal verb 'se passer' means to happen or proceed."),
 (2, None,
  "'I have a special mission for you.' Mathias entrusts him with a private assignment. "
  "The adjective 'speciale' emphasizes extraordinary importance."),
 (3, None,
  "'I am listening attentively, Mathias.' Renard gives his full attention. "
  "The adverb 'attentivement' indicates careful focus."),
 (4, None,
  "'Two American guests will arrive tonight.' Mathias prepares for the VIP arrival. "
  "The near future 'vont arriver' describes an impending event."),
 (5, None,
  "'Do you have their exact names?' Renard asks for clear identification details. "
  "The adjective 'precis' denotes distinct accuracy."),
 (6, None,
  "'Marcel Amos and Scott Downing.' Mathias names the two prominent film figures. "
  "Proper nouns identify specific individuals clearly."),
 (7, None,
  "'At what time do they arrive here?' Renard inquires about the expected schedule. "
  "The interrogative phrase 'a quelle heure' asks for the exact time."),
 (8, None,
  "'They arrive precisely at ten PM.' Mathias gives the specific hour of the meeting. "
  "In French, 22h is expressed as 'vingt-deux heures'."),
 (9, None,
  "'What must I do exactly?' Renard asks for his exact instructions. "
  "The inverted modal question 'que dois-je faire' is very polite."),
 (10, None,
  "'Notify me as soon as they arrive downstairs.' Mathias gives clear orders. "
  "The imperative 'previens-moi' demands prompt notification."),
 (11, None,
  "'Does this matter stay strictly confidential?' Renard checks the required level of discretion. "
  "The adjective 'confidentielle' describes sensitive private business."),
 (12, None,
  "'Yes, nobody must know that.' Mathias confirms the need for total discretion. "
  "The negative pronoun 'personne' signifies not a single person."),
 (13, None,
  "'I keep absolute secrecy.' Renard promises complete loyalty and confidentiality. "
  "The adjective 'absolu' means complete and unconditional."),
]

OUTRO = ("Mathias secures Renard's cooperation for the secret arrival of the American executives. "
         "With the security guard on alert, Mathias's hidden scheme can proceed undisturbed. "
         "Now, let's review the scene one last time.")

CLOSING = ("renard", "Je garde le secret absolu.")
