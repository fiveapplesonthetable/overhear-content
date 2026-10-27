# Authoring module for dix-pour-cent s02e04 scene 04 (cues 97-118).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-04.py --out out/dix-pour-cent/s02e04/scene-04.json

ID = "dix-pour-cent-s02e04-scene-04"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 4
TITLE = "Dispute au sujet d'Isabelle  (Arguing Over Adjani)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "noemie": "emilie"}
LABELS = {"lea": "Andréa", "noemie": "Noémie"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 97-118. Andréa and Noémie dispute whether Isabelle should apologize "
               "to Sacha Hartman, but Andréa fiercely protects her star. Adapted for A1 French.")

INTRO = ("Inside Andrea's office, tensions rise as Andrea and Noemie argue over how to salvage the situation. "
         "While Noemie suggests asking Isabelle to apologize, Andrea adamantly refuses to let her star client humiliate herself. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Noémie, prends-moi un rendez-vous avec Mathias.",
  "Noemie, get me an appointment with Mathias.",
  [(97, "Noémie, prenez-moi un rendez-vous avec Mathias Barneville.")], "Familiar imperative to assistant"),
 ("noemie", "Pourquoi Mathias? C'est votre client le problème.",
  "Why Mathias? Your client is the problem.",
  [(100, "C'est votre client qui fait des difficultés ici.")], "Clarified assistant objection"),
 ("noemie", "Vous avez entraîné Isabelle dans cette histoire.",
  "You dragged Isabelle into this story.",
  [(101, "C'est vous qui avez entraîné Isabelle dans tout ça.")], "Simplified blame clause"),
 ("lea", "Arrêtez! Elle voulait absolument travailler avec lui.",
  "Stop! She absolutely wanted to work with him.",
  [(102, "Arrêtez. Vous l'avez vue ?"), (103, "Elle mourait d'envie de travailler avec lui !")], "Combined defense"),
 ("noemie", "Isabelle pourrait peut-être l'appeler pour s'excuser.",
  "Maybe Isabelle could call him to apologize.",
  [(104, "Elle pourrait peut-être l'appeler."), (105, "-Pour s'excuser. -Hors de question !")], "Formulated compromise proposal"),
 ("lea", "Hors de question, elle ne s'excusera pas!",
  "Out of the question, she will not apologize!",
  [(105, "-Hors de question !")], "Added full refusal clause"),
 ("lea", "Je refuse de la laisser s'humilier.",
  "I refuse to let her humiliate herself.",
  [(106, "Je ne la laisserai pas s'humilier devant un type")], "Expressed protective stance"),
 ("lea", "Sacha se prend pour un génie.",
  "Sacha thinks he is a genius.",
  [(107, "qui se prend pour un grand du cinéma !")], "Simplified idiom"),
 ("noemie", "Alors, qu'est-ce que nous faisons maintenant?",
  "So, what do we do now?",
  [(108, "Bien..."), (109, "Non, je comprends.")], "Formulated operational question"),
 ("noemie", "Voulez-vous que j'appelle Isabelle au téléphone?",
  "Do you want me to call Isabelle on the phone?",
  [(110, "Bon, j'appellerai Isabelle.")], "Framed as offer"),
 ("lea", "Non, c'est ma cliente, je m'en charge.",
  "No, that is my client, I will handle it.",
  [(112, "C'est ma cliente, je m'en charge.")], "Kept exact dialogue"),
 ("noemie", "Très bien, faites comme vous voulez!",
  "Very well, do as you wish!",
  [(113, "Ah, très bien !"), (114, "Merci, monseigneur. Merci !")], "Simplified sarcastic concession"),
 ("lea", "Fermez la porte et laissez-moi réfléchir.",
  "Close the door and let me think.",
  [(118, "Andréa, fermez la porte.")], "Reversed command to request quiet"),
 ("noemie", "D'accord, mais trouvez vite une solution.",
  "All right, but find a solution quickly.",
  [(115, "-Elle est tellement impolie ! -Bref...")], "Added assistant warning"),
]

OPENER = "Let's examine how Andrea and Noemie debate the best strategy for Isabelle Adjani."

WALK = [
 (0, None,
  "'Noemie, get me an appointment with Mathias.' An imperative request demanding high-level mediation."),
 (1, None,
  "'Why Mathias? Your client is the problem.' A defiant retort assigning blame to the director."),
 (2, None,
  "'You dragged Isabelle into this story.' An accusation pointing out premature agent enthusiasm."),
 (3, None,
  "'Stop! She absolutely wanted to work with him.' A fierce defense of client motivation."),
 (4, None,
  "'Maybe Isabelle could call him to apologize.' A pragmatic compromise suggesting an apology."),
 (5, None,
  "'Out of the question, she will not apologize!' An emphatic refusal protecting client status."),
 (6, None,
  "'I refuse to let her humiliate herself.' A fierce protective instinct shielding an iconic star."),
 (7, None,
  "'Sacha thinks he is a genius.' A dismissive critique of young director arrogance."),
 (8, None,
  "'So, what do we do now?' A practical question seeking immediate direction."),
 (9, None,
  "'Do you want me to call Isabelle on the phone?' An offer from an assistant to break bad news."),
 (10, None,
  "'No, that is my client, I will handle it.' A firm territorial declaration asserting agent responsibility."),
 (11, None,
  "'Very well, do as you wish!' A sarcastic surrender conceding control."),
 (12, None,
  "'Close the door and let me think.' An imperative command requesting privacy to strategize."),
 (13, None,
  "'All right, but find a solution quickly.' An urgent closing reminder of looming consequences."),
]

TRANSITION = "Now let's listen to Andrea and Noemie's heated dispute again at full speed."

OUTRO = ("Andrea refuses to let an iconic actress apologize to an arrogant young director, taking full charge of the crisis. "
         "She must now find a creative way to bring the two together without damaging Isabelle's reputation.")

CLOSING = ("lea", "Merci, Noémie.")
