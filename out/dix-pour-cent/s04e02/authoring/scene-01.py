# Authoring module for dix-pour-cent s04e02 scene 01 (cues 1-74).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-01.py --out out/dix-pour-cent/s04e02/scene-01.json

ID = "dix-pour-cent-s04e02-scene-01"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 1
TITLE = "Dubosc en plein doute  (Dubosc in Doubt)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "dubosc": "marcel"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel", "dubosc": "Franck Dubosc"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-74. Gabriel visits Franck Dubosc on a grueling arthouse film set. Dubosc feels ridiculed and threatens to quit. Adapted for A1 French.")

INTRO = ("With ASK struggling to hold onto its roster of stars, Andrea Martel orders Gabriel to check on popular actor Franck Dubosc. "
         "Arriving on the set of an avant-garde arthouse movie, Gabriel finds the famous comedian thoroughly demoralized by an eccentric director and an arrogant young co-star. "
         "Ready to abandon both the film and his agents, Dubosc pours out his grievances. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Gabriel, nous devons garder Franck chez nous.",
  "Gabriel, we must keep Franck with us.",
  [(6, "perdre Franck Dubosc")], "Instructed agent to retain star client"),
 ("lea", "Il tourne un beau film d'auteur.",
  "He is shooting a fine arthouse film.",
  [(10, "de super bonne humeur")], "Assumed client was thrilled by project"),
 ("gabriel", "Bonjour Franck, je viens parler de ton avenir.",
  "Hello Franck, I come to talk about your future.",
  [(31, "ton avenir chez ASK")], "Approached actor on movie set"),
 ("dubosc", "C'est le pire tournage de ma vie!",
  "It is the worst shoot of my life!",
  [(39, "le pire tournage de ma vie")], "Vented intense frustration with production"),
 ("dubosc", "La réalisatrice réécrit constamment toutes les scènes.",
  "The director constantly rewrites all the scenes.",
  [(42, "réécrit les scènes")], "Complained about unstable script directions"),
 ("dubosc", "Elle me demande toujours de jouer moins.",
  "She always asks me to act less.",
  [(50, "jouer... moins")], "Bemoaned confusing artistic direction"),
 ("gabriel", "Elle cherche simplement une émotion très pure.",
  "She is simply seeking a very pure emotion.",
  [(50, "jouer... moins")], "Interpreted director's minimalist acting request"),
 ("dubosc", "Mon jeune partenaire se moque de moi.",
  "My young co-star makes fun of me.",
  [(58, "l'avenir du cinéma français")], "Expressed humiliation over generational mockery"),
 ("gabriel", "Ce film est ton grand tournant dramatique.",
  "This movie is your big dramatic turning point.",
  [(67, "ton Tchao Pantin")], "Reminded client of breakthrough artistic opportunity"),
 ("gabriel", "Ce rôle sera ton Tchao Pantin.",
  "This role will be your Tchao Pantin.",
  [(67, "ton Tchao Pantin")], "Evoked iconic comedian dramatic transformation"),
 ("dubosc", "Je ne conviens pas à ce cinéma.",
  "I am not suited to this cinema.",
  [(69, "le cinéma d'auteur")], "Admitted fundamental mismatch with arthouse genre"),
 ("dubosc", "Je veux quitter ce tournage sans attendre.",
  "I want to leave this shoot without waiting.",
  [(73, "temps de me tirer")], "Threatened immediate walkout from production"),
 ("dubosc", "Et je vais aussi quitter votre agence.",
  "And I am also going to leave your agency.",
  [(73, "temps de me tirer")], "Announced intention to sever ties with ASK"),
 ("gabriel", "Attends, parlons calmement de tout cela.",
  "Wait, let's talk calmly about all this.",
  [(31, "ton avenir chez ASK")], "Urged client to reconsider rash departure"),
]

OPENER = "Let's observe as Gabriel tries to comfort a demoralized Franck Dubosc on set."

WALK = [
 (0, None,
  "'Gabriel, we must keep Franck with us.' An urgent executive order emphasizing the vital need to retain bankable talent."),
 (1, None,
  "'He is shooting a fine arthouse film.' An optimistic assumption about the prestigious creative project."),
 (2, None,
  "'Hello Franck, I come to talk about your future.' A diplomatic opening broaching representation and agency loyalty."),
 (3, None,
  "'It is the worst shoot of my life!' An explosive grievance revealing acute misery on the production."),
 (4, None,
  "'The director constantly rewrites all the scenes.' An exasperated complaint criticizing unpredictable artistic methods."),
 (5, None,
  "'She always asks me to act less.' A baffled protest against confusing minimalist acting directions."),
 (6, None,
  "'She is simply seeking a very pure emotion.' A tactful defense translating avant-garde intentions into positive craft goals."),
 (7, None,
  "'My young co-star makes fun of me.' A painful confession detailing disrespect from an arrogant newcomer."),
 (8, None,
  "'This movie is your big dramatic turning point.' An encouraging perspective framing the struggle as a career breakthrough."),
 (9, None,
  "'This role will be your Tchao Pantin.' A flattering historical analogy recalling Coluche's legendary dramatic transition."),
 (10, None,
  "'I am not suited to this cinema.' A frank admission recognizing an uncomfortable cultural misfit."),
 (11, None,
  "'I want to leave this shoot without waiting.' A reckless threat announcing an immediate walkout from the film."),
 (12, None,
  "'And I am also going to leave your agency.' A devastating escalation threatening to sever ties with ASK completely."),
 (13, None,
  "'Wait, let's talk calmly about all this.' A soothing intervention attempting to prevent an irreversible rupture."),
]

TRANSITION = "Now let's listen to Andrea, Gabriel, and Franck talking again at full speed."

OUTRO = ("Confronted with Franck Dubosc's deep creative despair and threat to abandon ASK, Gabriel realizes he faces a major crisis. "
         "He must rapidly devise a plan to restore his actor's confidence before the entire production falls apart.")

CLOSING = ("lea", "Il faut sauver ce contrat.")
