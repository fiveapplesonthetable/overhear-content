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
  "'Gabriel, we must keep Franck with us.' The clause hinges on the everyday verb meaning 'must'."),
 (1, None,
  "'He is shooting a fine arthouse film.' Notice how 'shoots' leads directly into the noun meaning 'movie'. Notice how 'shoots' leads directly into the noun meaning 'movie'."),
 (2, None,
  "'Hello Franck, I come to talk about your future.' Notice how 'come' leads directly into the noun meaning 'future'. Notice how 'come' leads directly into the noun meaning 'future'."),
 (3, None,
  "'It is the worst shoot of my life!' The verb meaning 'it is' pairs naturally with the noun for 'filming' in everyday conversation."),
 (4, None,
  "'The director constantly rewrites all the scenes.' Notice how 'rewrites' leads directly into the noun meaning 'film director'. Notice how 'rewrites' leads directly into the noun meaning 'film director'."),
 (5, None,
  "'She always asks me to act less.' A baffled protest against confusing minimalist acting directions. The reflexive pronoun sits right in front of the verb for 'to play', turning the action back onto the subject."),
 (6, None,
  "'She is simply seeking a very pure emotion.' The verb meaning 'seeks' pairs naturally with the noun for 'emotion' in everyday conversation."),
 (7, None,
  "'My young co-star makes fun of me.' The verb meaning 'makes fun of' pairs naturally with the noun for 'partner' in everyday conversation."),
 (8, None,
  "'This movie is your big dramatic turning point.' An encouraging perspective framing the struggle as a career breakthrough. The informal 'you' form around 'movie' marks a direct, personal relationship."),
 (9, None,
  "'This role will be your Tchao Pantin.' A flattering historical analogy recalling Coluche's legendary dramatic transition. Gabriel uses the casual singular 'you' with 'will be', showing close familiarity."),
 (10, None,
  "'I am not suited to this cinema.' Notice how 'am suited' leads directly into the noun meaning 'cinema'. Notice how 'am suited' leads directly into the noun meaning 'cinema'."),
 (11, None,
  "'I want to leave this shoot without waiting.' A reckless threat announcing an immediate walkout from the film. The verb meaning 'want' pairs naturally with the noun for 'filming' in everyday conversation."),
 (12, None,
  "'And I am also going to leave your agency.' A devastating escalation threatening to sever ties with ASK completely. French forms the near future by pairing the present tense of 'to go' directly with 'to leave'."),
 (13, None,
  "'Wait, let's talk calmly about all this.' A soothing intervention attempting to prevent an irreversible rupture. The clause hinges on the everyday verb meaning 'wait for'."),
]

TRANSITION = "Now let's listen to Andrea, Gabriel, and Franck talking again at full speed."

OUTRO = ("Confronted with Franck Dubosc's deep creative despair and threat to abandon ASK, Gabriel realizes he faces a major crisis. "
         "He must rapidly devise a plan to restore his actor's confidence before the entire production falls apart.")

CLOSING = ("lea", "Il faut sauver ce contrat.")
