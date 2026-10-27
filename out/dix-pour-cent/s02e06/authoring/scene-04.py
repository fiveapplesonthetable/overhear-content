# Authoring module for dix-pour-cent s02e06 scene 04 (cues 84-93).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-04.py --out out/dix-pour-cent/s02e06/scene-04.json

ID = "dix-pour-cent-s02e06-scene-04"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 4
TITLE = "Montagnes russes  (An Emotional Rollercoaster)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "julien": "theo"}
LABELS = {"lea": "Gabriel", "julien": "Julien"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 84-93. Gabriel consoles an upset Julien Doré on the phone after his movie "
               "lacks financing, urging him to stop rereading the screenplay and move on. Adapted for A1 French.")

INTRO = ("In his office at ASK, talent agent Gabriel takes an urgent phone call from musician and filmmaker Julien Dore. "
         "Julien is spiraling in self-doubt after France 2 canceled his movie project, obsessively reading his rejected screenplay. "
         "Let's listen to their emotional exchange in French first.")

STORY = [
 ("julien", "Allô Gabriel, tu as une minute?",
  "Hello Gabriel, do you have a minute?",
  [(84, "Il y a quelqu'un ?")], "Opened phone call"),
 ("lea", "Oui Julien, je pensais justement à toi.",
  "Yes Julien, I was just thinking of you.",
  [(85, "Ah, te voilà ! Je te cherchais partout !")], "Expressed warm presence"),
 ("julien", "Je relis encore mon scénario rejeté.",
  "I am rereading my rejected screenplay again.",
  [(86, "arrête de lire le scénario de Julien,")], "Admitted obsessive reading"),
 ("lea", "Arrête de lire ce scénario, s'il te plaît.",
  "Stop reading this screenplay, please.",
  [(86, "Non, arrête de lire le scénario de Julien, tu ne fais qu'aggraver les choses.")], "Urged to stop reading"),
 ("julien", "Je veux comprendre notre échec commercial.",
  "I want to understand our commercial failure.",
  [(89, "Il m'associe à son échec.")], "Sought failure explanation"),
 ("lea", "Tu ne fais qu'aggraver ta tristesse.",
  "You are only making your sadness worse.",
  [(86, "tu ne fais qu'aggraver les choses.")], "Warned against worsening grief"),
 ("julien", "Aucun producteur ne veut de mon histoire.",
  "No producer wants my story.",
  [(88, "Beaucoup de films ne trouvent pas de financements.")], "Expressed feeling rejected"),
 ("lea", "Beaucoup de films manquent de financements.",
  "Many films lack financing.",
  [(88, "Beaucoup de films ne trouvent pas de financements.")], "Reminded of common film difficulties"),
 ("julien", "C'est un milieu artistique trop brutal.",
  "It is too brutal an artistic milieu.",
  [(90, "C'est un milieu difficile.")], "Critiqued cinema industry"),
 ("lea", "Le cinéma est de véritables montagnes russes.",
  "Cinema is a veritable rollercoaster.",
  [(91, "C'est des montagnes russes émotionnelles en permanence.")], "Shared rollercoaster metaphor"),
 ("julien", "Je ne sais plus quoi écrire maintenant.",
  "I no longer know what to write now.",
  [(87, "Il faut passer à autre chose.")], "Admitted creative disorientation"),
 ("lea", "Il faut simplement passer à autre chose.",
  "You simply must move on to something else.",
  [(87, "Il faut passer à autre chose.")], "Encouraged moving forward"),
 ("julien", "Tu crois qu'on trouvera un autre projet?",
  "Do you believe we will find another project?",
  [(92, "Je suis là, d'accord ?")], "Inquired about future project"),
 ("lea", "Oui, je suis toujours là avec toi.",
  "Yes, I am always here with you.",
  [(92, "Je suis là, d'accord ?")], "Affirmed enduring loyalty"),
]

OPENER = "Let's observe how Gabriel comforts Julien and encourages him to move forward."

WALK = [
 (0, None,
  "'Hello Gabriel, do you have a minute?' A telephone greeting checking conversational availability."),
 (1, None,
  "'Yes Julien, I was just thinking of you.' An affectionate imperfect tense expressing ongoing concern."),
 (2, None,
  "'I am rereading my rejected screenplay again.' An iterative present verb showing obsessive artistic doubt."),
 (3, None,
  "'Stop reading this screenplay, please.' A protective imperative urging a client to break negative habits."),
 (4, None,
  "'I want to understand our commercial failure.' A modal phrase seeking reasons for professional setback."),
 (5, None,
  "'You are only making your sadness worse.' A restrictive negative structure highlighting emotional harm."),
 (6, None,
  "'No producer wants my story.' A negative subject construction stating perceived total rejection."),
 (7, None,
  "'Many films lack financing.' A reassuring industry generalization contextualizing production challenges."),
 (8, None,
  "'It is too brutal an artistic milieu.' An intensified adjective describing harsh cinema realities."),
 (9, None,
  "'Cinema is a veritable rollercoaster.' A vivid metaphor illustrating unpredictable career fortunes."),
 (10, None,
  "'I no longer know what to write now.' A negative knowledge formula revealing creative disorientation."),
 (11, None,
  "'You simply must move on to something else.' An impersonal necessity idiom advising creative renewal."),
 (12, None,
  "'Do you believe we will find another project?' A tentative question seeking future collaborative hope."),
 (13, None,
  "'Yes, I am always here with you.' A steadfast affirmation guaranteeing personal and professional loyalty."),
]

TRANSITION = "Now let's listen to Gabriel and Julien again at full speed."

OUTRO = ("Gabriel helps Julien Dore process the pain of a canceled project, reminding him that setbacks are inevitable in filmmaking. "
         "With steadfast agent support, Julien prepares to turn the page toward new artistic endeavors.")

CLOSING = ("julien", "Merci pour ton soutien, Gabriel.")
