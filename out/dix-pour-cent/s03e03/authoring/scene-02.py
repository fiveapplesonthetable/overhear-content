# Authoring module for dix-pour-cent s03e03 scene 02 (cues 104-213).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e03/authoring/scene-02.py --out out/dix-pour-cent/s03e03/scene-02.json

ID = "dix-pour-cent-s03e03-scene-02"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 2
TITLE = "Projet d'agence secrète  (Secret Agency Project)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 104-213. Andréa and Gabriel prepare to launch a rival agency and review legal constraints with their lawyer. Adapted for A1 French.")

INTRO = ("Andrea Martel and Gabriel Sarda plan to break away from ASK to launch an independent talent agency. "
         "Meeting secretly with their attorney, they review strict commercial regulations to protect their future enterprise. "
         "Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "L'avocat a confirmé notre rendez-vous secret.",
  "The lawyer confirmed our secret meeting.",
  [(104, "C'est bon, il a confirmé."), (105, "Rendez-vous dans une demi-heure à Belleville.")], "Confirmed legal meeting"),
 ("lea", "Parfait, nous devons rester très discrets.",
  "Perfect, we must remain very discreet.",
  [(133, "on voulait rester discret.")], "Emphasized utmost discretion"),
 ("gabriel", "Hicham ne doit rien soupçonner.",
  "Hicham must suspect nothing.",
  [(109, "fais profil bas avec Hicham.")], "Warned against executive suspicion"),
 ("lea", "Nous voulons créer notre propre agence.",
  "We want to create our own agency.",
  [(140, "monter une agence concurrente")], "Asserted desire for independence"),
 ("gabriel", "Quels sont les risques légaux?",
  "What are the legal risks?",
  [(146, "qu'est-ce qu'on risque ?")], "Asked about legal liabilities"),
 ("lea", "Il faut éviter le démantèlement d'ASK.",
  "We must avoid asset stripping ASK.",
  [(149, "Ça s'appelle du démantèlement.")], "Identified legal pitfall"),
 ("gabriel", "Que dit la loi exactement?",
  "What does the law say exactly?",
  [(147, "atteignent 50 % de celui de la société.")], "Sought statutory specifics"),
 ("lea", "Nos chiffres cumulés restent sous cinquante pour cent.",
  "Our combined figures remain under fifty percent.",
  [(147, "atteignent 50 % de celui de la société.")], "Cited financial ceiling"),
 ("gabriel", "Nous respectons cette règle essentielle.",
  "We respect this essential rule.",
  [(154, "On est bons, non ?")], "Confirmed statutory compliance"),
 ("lea", "Ne signe aucun nouveau gros contrat.",
  "Do not sign any new big contract.",
  [(156, "ne rentrer surtout aucun nouveau contrat jusqu'à votre départ.")], "Ordered contract freeze"),
 ("gabriel", "Je vais faire traîner les négociations.",
  "I will drag out the negotiations.",
  [(159, "faire traîner les négo.")], "Promised intentional delays"),
 ("lea", "La nouvelle agence ouvrira bientôt.",
  "The new agency will open soon.",
  [(137, "la nouvelle structure soit prête avant que j'accouche.")], "Envisioned near launch"),
 ("gabriel", "C'est notre grand avenir professionnel.",
  "It is our great professional future.",
  [(140, "monter une agence concurrente")], "Celebrated partnership"),
 ("lea", "Gardons ce grand secret pour nous.",
  "Let us keep this great secret to ourselves.",
  [(142, "Vous n'avez parlé à personne ?"), (143, "Non, bien sûr que non.")], "Sealed pact of secrecy"),
]

OPENER = "Let's observe as Andrea and Gabriel plan their secret new agency."

WALK = [
 (0, None,
  "'The lawyer confirmed our secret meeting.' A confidential declaration confirming an essential legal appointment."),
 (1, None,
  "'Perfect, we must remain very discreet.' An imperative warning emphasizing extreme professional secrecy."),
 (2, None,
  "'Hicham must suspect nothing.' A protective modal phrase guarding against agency executive suspicion."),
 (3, None,
  "'We want to create our own agency.' A bold declaration stating collective entrepreneurial independence."),
 (4, None,
  "'What are the legal risks?' A direct interrogative inquiring into commercial compliance constraints."),
 (5, None,
  "'We must avoid asset stripping ASK.' A serious legal caution preventing illegal corporate dismantling."),
 (6, None,
  "'What does the law say exactly?' A precise inquiry demanding exact statutory boundaries."),
 (7, None,
  "'Our combined figures remain under fifty percent.' A reassuring statistical compliance statement."),
 (8, None,
  "'We respect this essential rule.' A confident confirmation adhering strictly to statutory norms."),
 (9, None,
  "'Do not sign any new big contract.' A strategic negative imperative freezing new business acquisition."),
 (10, None,
  "'I will drag out the negotiations.' A pragmatic near-future promise to delay impending deals."),
 (11, None,
  "'The new agency will open soon.' An optimistic temporal anticipation looking forward to launch day."),
 (12, None,
  "'It is our great professional future.' An inspiring summary expressing long-term career ambition."),
 (13, None,
  "'Let us keep this great secret to ourselves.' A mutual imperative pact pledging total discretion."),
]

TRANSITION = "Now let's listen to Andrea and Gabriel again at full speed."

OUTRO = ("Andrea and Gabriel solidify their alliance, carefully measuring each business step to safeguard their independent agency. "
         "With strict confidentiality maintained, their transition plan moves ahead toward realization.")

CLOSING = ("lea", "Notre liberté commence maintenant.")
