# Authoring module for dix-pour-cent s02e06 scene 05 (cues 94-105).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-05.py --out out/dix-pour-cent/s02e06/scene-05.json

ID = "dix-pour-cent-s02e06-scene-05"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 5
TITLE = "Un planning très serré  (A Tight Schedule)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "herve": "marcel"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 94-105. At the ASK agency, Andréa panics over Juliette Binoche's schedule for Cannes "
               "and demands an immediate appointment with luxury jeweler Chopard. "
               "Adapted for A1 French.")

INTRO = ("In the ASK offices on the eve of the Cannes film festival, Andrea scrambles to organize Juliette Binoche's high-stakes schedule. "
         "Gabriel and Herve struggle to keep up as office tension reaches a boiling point. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Prenez rendez-vous avec Chopard pour Juliette Binoche.",
  "Make an appointment with Chopard for Juliette Binoche.",
  [(94, "Prenez rendez-vous avec Chopard pour Juliette Binoche immédiatement.")], "Andrea demands an appointment"),
 ("herve", "Mon emploi du temps est trop chargé.",
  "My schedule is much too tight.",
  [(95, "Mon emploi du temps est vraiment trop chargé.")], "Herve explains his lack of time"),
 ("gabriel", "C'est qui exactement, cette maison Chopard?",
  "Who exactly is this fashion house Chopard?",
  [(96, "C'est qui, Chopard ?")], "Gabriel asks for clarification"),
 ("lea", "C'est le partenaire officiel du festival!",
  "It is the official partner of the festival!",
  [(97, "Chopard, le partenaire du festival.")], "Andrea highlights the sponsor"),
 ("lea", "Ils fabriquent la célèbre Palme d'or.",
  "They manufacture the famous Palme d'Or.",
  [(98, "Ils fabriquent la Palme d'Or !")], "Andrea stresses prestige"),
 ("gabriel", "Andréa, nous n'avons pas le temps.",
  "Andrea, we do not have the time.",
  [(99, "Non, Andréa, on n'a vraiment pas le temps.")], "Gabriel resists"),
 ("herve", "Pas juste avant notre départ pour Cannes!",
  "Not right before our departure for Cannes!",
  [(100, "Non, pas juste avant Cannes.")], "Herve backs Gabriel up"),
 ("lea", "Je pars demain matin pour le festival.",
  "I am leaving tomorrow morning for the festival.",
  [(101, "Exactement ! Je pars à Cannes demain")], "Andrea emphasizes the deadline"),
 ("lea", "J'ai mille choses urgentes à faire.",
  "I have a thousand urgent things to do.",
  [(101, "j'ai mille choses à faire !")], "Andrea vents her stress"),
 ("gabriel", "Et sans Camille, tu n'y arrives pas.",
  "And without Camille, you cannot cope.",
  [(103, "Et sans Camille, je n'y arrive pas, donc...")], "Gabriel mentions Camille's absence"),
 ("lea", "Ne prononcez plus ce nom ici!",
  "Do not utter that name here anymore!",
  [(104, "Ne prononcez pas ce nom dans ce bureau !")], "Andrea shuts down the mention"),
 ("herve", "On fait tout le boulot nous-mêmes.",
  "We are doing all the work ourselves.",
  [(105, "On fait tout le boulot pendant que Mme...")], "Herve vents frustration"),
 ("gabriel", "Calmons-nous avant de monter les marches.",
  "Let us calm down before climbing the red carpet stairs.",
  [(102, "Je monte déjà ces marches !")], "Gabriel urges composure"),
]

OPENER = "Let's examine how Andrea and her colleagues handle the extreme pressure step by step to explore festival preparations."

WALK = [
 (0, None,
  "'Make an appointment with Chopard for Juliette Binoche.' Andrea gives urgent orders to prepare jewelry for the star."),
 (1, None,
  "'My schedule is much too tight.' Herve protests that he is already overwhelmed with logistics."),
 (2, None,
  "'Who exactly is this fashion house Chopard?' Gabriel wonders about the prestige of the luxury brand."),
 (3, None,
  "'It is the official partner of the festival!' Andrea reminds Gabriel of the luxury brand's major role."),
 (4, None,
  "'They manufacture the famous Palme d'Or.' Andrea points out that Chopard creates the highest award in cinema."),
 (5, None,
  "'Andrea, we do not have the time.' Gabriel tries to set realistic boundaries before their trip."),
 (6, None,
  "'Not right before our departure for Cannes!' Herve stresses how impossible last-minute requests are."),
 (7, None,
  "'I am leaving tomorrow morning for the festival.' Andrea insists that time is running out quickly."),
 (8, None,
  "'I have a thousand urgent things to do.' Andrea describes her overwhelming pre-festival workload."),
 (9, None,
  "'And without Camille, you cannot cope.' Gabriel notes how hard it is to work without their best assistant."),
 (10, None,
  "'Do not utter that name here anymore!' Andrea refuses to hear Camille mentioned after her departure."),
 (11, None,
  "'We are doing all the work ourselves.' Herve complains about taking on extra duties without help."),
 (12, None,
  "'Let us calm down before climbing the red carpet stairs.' Gabriel urges the team to stay focused."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("The pre-festival rush tests everyone's patience as Andrea tries to secure top-tier luxury support for Juliette Binoche. "
         "Let's review the key expressions and vocabulary from this scene.")

CLOSING = ("gabriel", "Calmons-nous avant de monter les marches.")
