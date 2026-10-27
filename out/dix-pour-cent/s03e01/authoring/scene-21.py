# Authoring module for dix-pour-cent s03e01 scene 21 (cues 695-915).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-21.py --out out/dix-pour-cent/s03e01/scene-21.json

ID = "dix-pour-cent-s03e01-scene-21"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 21
TITLE = "Un jeune talent prometteur  (A Promising Young Talent)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "brian": "theo", "mathias": "marcel"}
LABELS = {"lea": "Camille", "brian": "Brian", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 695-745. At the ASK agency, Camille meets with young actor Brian Valles. "
               "Mathias walks in and mentions a casting call with Jacques Audiard. "
               "Adapted for A1 French.")

INTRO = ("At the ASK agency, Camille meets with promising young actor Brian Valles to discuss potential representation. "
         "When senior partner Mathias walks in talking about director Jacques Audiard, Brian's interest is piqued. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Bonjour Brian, bienvenue dans mon bureau.",
  "Hello Brian, welcome to my office.",
  [(700, "Bonjour, Brian."), (706, "dans mon bureau.")], "Camille welcomes Brian"),
 ("brian", "Merci Camille, c'est un bel endroit.",
  "Thank you Camille, it is a nice place.",
  [(707, "Beau bureau."), (708, "Merci.")], "Brian compliments the office"),
 ("lea", "Parlons un peu de votre carrière.",
  "Let us talk a bit about your career.",
  [(712, "Parlons un peu")], "Camille starts the discussion"),
 ("brian", "J'ai déjà un agent artistique.",
  "I already have a talent agent.",
  [(713, "j'ai déjà un agent.")], "Brian mentions his agent"),
 ("brian", "Mais ASK est une grande agence.",
  "But ASK is a major agency.",
  [(716, "c'est quand même une grande agence.")], "Brian praises ASK"),
 ("lea", "Nous voulons vous accompagner avec soin.",
  "We want to support you with care.",
  [(717, "comment vous travaillez.")], "Camille explains ASK's approach"),
 ("mathias", "Pardon Camille, tu as une minute?",
  "Sorry Camille, do you have a minute?",
  [(722, "T'as besoin de quelque chose ?")], "Mathias drops in"),
 ("lea", "Je suis en rendez-vous, Mathias.",
  "I am in a meeting, Mathias.",
  [(725, "tu es occupé.")], "Camille notes she is busy"),
 ("mathias", "Jacques Audiard m'a appelé ce matin.",
  "Jacques Audiard called me this morning.",
  [(726, "Jacques m'a appelé."), (727, "Jacques Audiard.")], "Mathias mentions Audiard"),
 ("mathias", "Il cherche de nouveaux jeunes talents.",
  "He is looking for new young talent.",
  [(728, "je lui présente des jeunes.")], "Mathias explains Audiard's search"),
 ("brian", "Jacques Audiard prépare un nouveau film?",
  "Jacques Audiard is preparing a new movie?",
  [(729, "Audiard.")], "Brian is excited"),
 ("mathias", "Oui, un projet absolument formidable!",
  "Yes, an absolutely wonderful project!",
  [(730, "Il m'appelle")], "Mathias praises the project"),
 ("brian", "Mathias, auriez-vous juste une minute?",
  "Mathias, would you have just a minute?",
  [(739, "auriez juste une minute ?")], "Brian pitches Mathias directly"),
 ("lea", "Chaque jeune acteur cherche sa chance!",
  "Every young actor seeks his chance!",
  [(715, "On sait jamais.")], "Camille notes industry ambition"),
]

OPENER = "Let's examine how Camille conducts her meeting with Brian step by step."

WALK = [
 (0, None,
  "'Hello Brian, welcome to my office.' Camille greets the promising young actor warmly."),
 (1, None,
  "'Thank you Camille, it is a nice place.' Brian admires Camille's professional workplace."),
 (2, None,
  "'Let us talk a bit about your career.' Camille begins their exploratory representation meeting."),
 (3, None,
  "'I already have a talent agent.' Brian clarifies his current professional representation."),
 (4, None,
  "'But ASK is a major agency.' Brian recognizes the agency's prestige and market power."),
 (5, None,
  "'We want to support you with care.' Camille emphasizes ASK's personalized guidance for actors."),
 (6, None,
  "'Sorry Camille, do you have a minute?' Mathias interrupts the meeting without knocking."),
 (7, None,
  "'I am in a meeting, Mathias.' Camille reminds her senior colleague that she is busy."),
 (8, None,
  "'Jacques Audiard called me this morning.' Mathias casually drops the prominent director's name."),
 (9, None,
  "'He is looking for new young talent.' Mathias mentions a prestigious casting opportunity."),
 (10, None,
  "'Jacques Audiard is preparing a new movie?' Brian immediately reacts to the filmmaker's name."),
 (11, None,
  "'Yes, an absolutely wonderful project!' Mathias hypes the upcoming high-profile feature film."),
 (12, None,
  "'Mathias, would you have just a minute?' Brian eagerly tries to pitch himself to the senior agent."),
 (13, None,
  "'Every young actor seeks his chance!' Camille observes the intense competition in the industry."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("An exploratory meeting turns into an unexpected audition opportunity as Brian pitches himself to Mathias. "
         "Let's review the key expressions and vocabulary from this scene.")

CLOSING = ("lea", "Chaque jeune acteur cherche sa chance!")
