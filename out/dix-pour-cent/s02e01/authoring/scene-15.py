# Authoring module for dix-pour-cent s02e01 scene 15 (cues 422-435).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-15.py --out out/dix-pour-cent/s02e01/scene-15.json

ID = "dix-pour-cent-s02e01-scene-15"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 15
TITLE = "L'ultimatum du producteur  (The Producer's Ultimatum)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "marcel", "michel": "theo"}
LABELS = {"lea": "Camille", "mathias": "Mathias", "michel": "Michel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 422-435. Film producer Michel calls Mathias in a fury because Ramzy has gone missing "
               "and Virginie is giving depressed interviews right before their film release. "
               "Adapted for A1 French.")

INTRO = ("In Mathias's office, the telephone rings with an explosive call from movie producer Michel. "
         "Ramzy Bedia has vanished just one week before the premiere, and Michel delivers an uncompromising threat. "
         "Let's listen to the scene in French first.")

STORY = [
 ("michel", "Mathias, tu as l'air d'avoir mal compris.",
  "Mathias, you seem to have misunderstood.",
  [(422, "tu as l'air d'avoir mal compris")], ""),
 ("michel", "Ramzy ne répond plus à mes appels et je suis le producteur du film!",
  "Ramzy no longer answers my calls and I am the producer of the film!",
  [(423, "Ramzy ne répond plus à mes appels et je suis le producteur du film")], ""),
 ("michel", "Il a disparu une semaine avant la sortie.",
  "He has disappeared a week before the release.",
  [(424, "Il a disparu une semaine avant la sortie")], ""),
 ("mathias", "Virginie fait la promotion, non?",
  "Virginie is doing the promotion, right?",
  [(426, "Virginie fait la promotion, non")], ""),
 ("michel", "Tu plaisantes? Elle est comme un zombie!",
  "Are you kidding? She is like a zombie!",
  [(427, "Tu plaisantes ? Elle est comme un zombie")], ""),
 ("michel", "Pas une seule photo utilisable!",
  "Not a single usable photo!",
  [(428, "Pas une seule photo utilisable")], ""),
 ("michel", "On sort une comédie la semaine prochaine!",
  "We are releasing a comedy next week!",
  [(430, "On sort une comédie, la semaine prochaine")], ""),
 ("michel", "Agissez de manière responsable!",
  "Act in a responsible manner!",
  [(431, "Agissez de manière responsable")], ""),
 ("mathias", "Michel, tu as tout à fait raison.",
  "Michel, you are completely right.",
  [(432, "Michel, tu as tout à fait raison")], ""),
 ("mathias", "Je raccroche et je trouve Ramzy.",
  "I hang up and I find Ramzy.",
  [(432, "Je raccroche")], "Softened colloquial expression"),
 ("michel", "S'il ne fait pas l'émission de Drucker cette semaine, je l'attaque!",
  "If he does not do Drucker's show this week, I will sue him!",
  [(434, "S'il ne fait pas l'émission de Drucker cette semaine"), (435, "je l'attaque pour rupture de contrat")], ""),
 ("mathias", "Ne t'inquiète pas, il sera là.",
  "Do not worry, he will be there.",
  [], "Reassuring promise"),
 ("lea", "C'est une catastrophe, Mathias!",
  "It is a disaster, Mathias!",
  [], "Camille's reaction in the office"),
 ("mathias", "Je dois régler ce problème immédiatement.",
  "I must settle this problem immediately.",
  [], "Closing resolution"),
]

OPENER = "The producer loses his temper. Let us examine the lines with English notes."

WALK = [
 (0, None, "'Mathias, you seem to have misunderstood.' Avoir l'air de means to seem or look like."),
 (1, None, "'Ramzy no longer answers my calls and I am the producer of the film!' Repondre a means to answer."),
 (2, None, "'He has disappeared a week before the release.' Disparaitre means to disappear, and la sortie means release."),
 (3, None, "'Virginie is doing the promotion, right?' La promotion refers to publicity for a film or book."),
 (4, None, "'Are you kidding? She is like a zombie!' Tu plaisantes is a frequent question meaning are you joking."),
 (5, None, "'Not a single usable photo!' Utilisable is an adjective meaning usable or suitable for print."),
 (6, None, "'We are releasing a comedy next week!' Sortir can mean to release a movie in theatres."),
 (7, None, "'Act in a responsible manner!' Agir means to act, and de maniere responsable means responsibly."),
 (8, None, "'Michel, you are completely right.' Avoir raison means to be right, intensified by tout a fait."),
 (9, None, "'I hang up and I find Ramzy.' Raccrocher means to hang up the telephone."),
 (10, None, "'If he does not do Drucker's show this week, I will sue him!' Attaquer means to sue or take legal action."),
 (11, None, "'Do not worry, he will be there.' Ne t'inquiete pas is a standard phrase meaning do not worry."),
 (12, None, "'It is a disaster, Mathias!' Camille reacts with alarm to the legal threat."),
 (13, None, "'I must settle this problem immediately.' Regler un probleme means to solve or settle a problem."),
]

TRANSITION = "Now listen to the heated exchange once more from beginning to end."
OUTRO = ("With a lawsuit looming over ASK, Mathias urgently needs to track down Ramzy and calm the producer. "
         "Soon after, Gabriel approaches Mathias to propose a truce. "
         "Here is our closing line.")
CLOSING = ("mathias", "Je dois régler ce problème immédiatement.")
