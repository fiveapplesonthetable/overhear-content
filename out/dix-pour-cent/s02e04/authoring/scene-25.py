# Authoring module for dix-pour-cent s02e04 scene 25 (cues 736-763).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-25.py --out out/dix-pour-cent/s02e04/scene-25.json

ID = "dix-pour-cent-s02e04-scene-25"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 25
TITLE = "L'entretien d'embauche  (The Job Interview)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Hervé", "hicham": "Hicham", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 736-763. Gabriel steps out with his dog, leaving Hicham to interview Herve "
               "one-on-one for the junior agent position. Herve makes an impassioned pitch for his abilities. "
               "Adapted for A1 French.")

INTRO = ("In Hicham's office, Gabriel steps out with his dog so Hicham can interview Herve privately. "
         "Herve pitches his unique talents, dedication, and keen sense of observation for the junior agent position. "
         "Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Jean Gabin, viens avec moi!",
  "Jean Gabin, come with me!",
  [(736, "Jean Gabin, viens ici !")], "Gabriel calls his dog"),
 ("hicham", "Maintenant, nous sommes entre hommes.",
  "Now, we are man-to-man.",
  [(737, "Maintenant, c'est entre hommes.")], "Hicham opens the interview"),
 ("hicham", "Comment tu envisages ce poste?",
  "How do you envisage this position?",
  [(738, "Comment tu envisages le poste ?")], "Hicham asks about the role"),
 ("lea", "Je ne veux pas quitter Gabriel.",
  "I do not want to leave Gabriel.",
  [(739, "-En quittant Gabriel ? -Oh non.")], "Herve states his loyalty"),
 ("lea", "Je continuerai à travailler avec lui.",
  "I will continue to work with him.",
  [(740, "Je continuerai à travailler avec lui")], "Herve explains his plan"),
 ("lea", "Je peux faire plusieurs choses ensemble.",
  "I can do several things together.",
  [(741, "Je suis très ouvert à faire plusieurs choses en même temps.")], "Herve touts multitasking"),
 ("lea", "Si vous m'engagez, je serai parfait.",
  "If you hire me, I will be perfect.",
  [(742, "Si vous m'engagez, je me donnerai à fond.")], "Herve promises commitment"),
 ("hicham", "Qu'est-ce que vous aimez dans ce métier?",
  "What do you like about this profession?",
  [(743, "Et... qu'est-ce que vous aimez le plus dans ce métier ?")], "Hicham asks about motivation"),
 ("lea", "J'aime l'excitation de la découverte.",
  "I like the excitement of discovery.",
  [(744, "L'excitation de la découverte.")], "Herve highlights discovery"),
 ("hicham", "Et quelle est votre plus grande qualité?",
  "And what is your greatest quality?",
  [(745, "Votre plus grande qualité ?")], "Hicham queries qualities"),
 ("lea", "J'ai un grand sens de l'observation.",
  "I have a great sense of observation.",
  [(746, "Mon sens de l'observation.")], "Herve praises his observation"),
 ("hicham", "Qu'allez-vous améliorer chez ASK?",
  "What will you improve at ASK?",
  [(747, "Qu'amélioreriez-vous chez ASK ?")], "Hicham asks about improvements"),
 ("lea", "La communication, sans aucune hésitation.",
  "Communication, without any hesitation.",
  [(748, "La communication, sans hésiter.")], "Herve answers communication"),
 ("hicham", "Merci, nous recommencerons les entretiens demain.",
  "Thank you, we will resume the interviews tomorrow.",
  [(763, "-À partir d'où ? -On recommence.")], "Hicham closes the session"),
]

OPENER = "Let's examine how Herve pitches his strengths during this one-on-one interview step by step."

WALK = [
 (0, None,
  "'Jean Gabin, come with me!' Gabriel calls his faithful dog as he steps out of the office."),
 (1, None,
  "'Now, we are man-to-man.' Hicham sets an informal tone for their private discussion."),
 (2, None,
  "'How do you envisage this position?' Hicham asks how Herve plans to handle the responsibilities."),
 (3, None,
  "'I do not want to leave Gabriel.' Herve immediately makes clear that he remains loyal to his mentor."),
 (4, None,
  "'I will continue to work with him.' Herve uses the simple future tense of the verb continuer."),
 (5, None,
  "'I can do several things together.' Herve highlights his ability to multitask across different agency tasks."),
 (6, None,
  "'If you hire me, I will be perfect.' Herve uses a conditional si clause followed by the future tense."),
 (7, None,
  "'What do you like about this profession?' Hicham probes Herve's passion for talent representation."),
 (8, None,
  "'I like the excitement of discovery.' Herve identifies scouting new talents as his main thrill."),
 (9, None,
  "'And what is your greatest quality?' Hicham asks a classic job interview question about personal virtues."),
 (10, None,
  "'I have a great sense of observation.' Herve emphasizes how attentively he watches everyone in the agency."),
 (11, None,
  "'What will you improve at ASK?' Hicham challenges him to identify internal agency weaknesses."),
 (12, None,
  "'Communication, without any hesitation.' Herve points directly to the lack of transparent communication."),
 (13, None,
  "'Thank you, we will resume the interviews tomorrow.' Hicham wraps up the meeting with polite reserve."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Herve presents his case with characteristic wit and passion, showing his ambition to become a full agent. "
         "Let's review the key vocabulary from this interview.")

CLOSING = ("lea", "J'ai un grand sens de l'observation.")
