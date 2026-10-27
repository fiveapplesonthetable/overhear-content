# Authoring module for dix-pour-cent s04e01 scene 01 (cues 1-30).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-01.py --out out/dix-pour-cent/s04e01/scene-01.json

ID = "dix-pour-cent-s04e01-scene-01"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 1
TITLE = "Course contre la montre  (Race Against the Clock)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "camille": "emilie"}
LABELS = {"lea": "Andréa", "camille": "Camille"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-30. Andrea rushes in a taxi and asks Camille to devour Oscar Rondo's script before meeting Charlotte Gainsbourg. Adapted for A1 French.")

INTRO = ("Trapped in a Parisian taxi while juggling family calls and client emergencies, Andrea Martel rushes to meet Charlotte Gainsbourg at the airport. "
         "Having spent the night awake with her baby daughter Flora, Andrea has not had a moment to read director Oscar Rondo's urgent script. "
         "Spotting assistant Camille on the sidewalk, Andrea delegates the crucial task before time runs out. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Mon téléphone explose d'appels ce matin.",
  "My phone is exploding with calls this morning.",
  [(24, "mon téléphone explose")], "Complained about endless phone notifications"),
 ("lea", "Diane a besoin d'une robe rouge.",
  "Diane needs a red dress.",
  [(10, "a besoin d'une robe")], "Mentioned celebrity wardrobe request"),
 ("camille", "Tu avais l'air très pressée.",
  "You looked in a great hurry.",
  [(18, "Je t'appelais")], "Observed agent running breathless"),
 ("lea", "Je vais chercher Charlotte à l'aéroport.",
  "I am picking up Charlotte at the airport.",
  [(21, "Je vais chercher Charlotte")], "Stated urgent travel destination"),
 ("lea", "Tu dois lire le scénario d'Oscar.",
  "You must read Oscar's script.",
  [(19, "lire le scénario d'Oscar")], "Delegated urgent script reading"),
 ("camille", "Tu ne l'as pas lu cette nuit?",
  "You did not read it last night?",
  [(22, "Tu ne l'as pas lu")], "Asked about unread manuscript"),
 ("lea", "Non, le bébé a pleuré sans arrêt.",
  "No, the baby cried non-stop.",
  [(24, "mon téléphone explose")], "Explained sleepless night with infant"),
 ("lea", "Charlotte va me poser mille questions.",
  "Charlotte is going to ask me a thousand questions.",
  [(21, "Je vais chercher Charlotte")], "Anticipated client interrogation"),
 ("camille", "Quand veux-tu mon avis sur l'histoire?",
  "When do you want my opinion on the story?",
  [(19, "lire le scénario d'Oscar")], "Inquired about reading deadline"),
 ("lea", "J'ai besoin que tu le dévores immédiatement.",
  "I need you to devour it immediately.",
  [(25, "J'ai besoin que tu le dévores")], "Urged rapid reading pace"),
 ("lea", "Je dois gagner un peu de temps.",
  "I must buy a little time.",
  [(26, "pendant que je gagne du temps")], "Formulated delaying tactic"),
 ("camille", "Je t'envoie un message très vite.",
  "I will send you a text very quickly.",
  [(26, "pendant que je gagne du temps")], "Promised quick feedback via message"),
 ("lea", "Dépêche-toi, nous manquons vraiment de temps.",
  "Hurry up, we are really short on time.",
  [(28, "Dépêche-toi, on n'a pas le temps")], "Emphasized critical time crunch"),
 ("camille", "Je commence la lecture tout de suite.",
  "I am starting reading right away.",
  [(28, "Dépêche-toi, on n'a pas le temps")], "Committed to prompt execution"),
]

OPENER = "Let's observe as Andrea tasks Camille with an urgent emergency reading on the sidewalk."

WALK = [
 (0, None,
  "'My phone is exploding with calls this morning.' An overwhelmed remark describing intense morning communication pressure."),
 (1, None,
  "'Diane needs a red dress.' A concrete celebrity styling emergency illustrating demanding client requests."),
 (2, None,
  "'You looked in a great hurry.' An observant reaction noting the agent's breathless and frantic pace."),
 (3, None,
  "'I am picking up Charlotte at the airport.' A prompt clarification explaining the pressing travel deadline."),
 (4, None,
  "'You must read Oscar's script.' A direct delegation handing over an unread project under strict deadlines."),
 (5, None,
  "'You did not read it last night?' A surprised inquiry wondering why the senior agent did not review the text."),
 (6, None,
  "'No, the baby cried non-stop.' A relatable personal justification citing family obligations and sleep deprivation."),
 (7, None,
  "'Charlotte is going to ask me a thousand questions.' A realistic forecast predicting thorough questioning from the movie star."),
 (8, None,
  "'When do you want my opinion on the story?' A practical procedural question clarifying the expected delivery time."),
 (9, None,
  "'I need you to devour it immediately.' An emphatic imperative commanding rapid and thorough script analysis."),
 (10, None,
  "'I must buy a little time.' A candid admission of strategic stalling while awaiting feedback."),
 (11, None,
  "'I will send you a text very quickly.' A reassuring commitment promising prompt summary notes."),
 (12, None,
  "'Hurry up, we are really short on time.' An urgent warning highlighting the rapidly closing window of opportunity."),
 (13, None,
  "'I am starting reading right away.' A loyal agreement confirming immediate action on the script."),
]

TRANSITION = "Now let's listen to Andrea and Camille conversing again at full speed."

OUTRO = ("Leaving Camille to tackle the dense screenplay on the fly, Andrea speeds away toward Charles de Gaulle airport. "
         "She must now rely on her wits and quick texting to survive the upcoming ride with Charlotte.")

CLOSING = ("lea", "Je compte sur toi.")
