# Authoring module for dix-pour-cent s03e01 scene 22 (cues 916-954).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-22.py --out out/dix-pour-cent/s03e01/scene-22.json

ID = "dix-pour-cent-s03e01-scene-22"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 22
TITLE = "Les confidences de Noémie  (Noémie's Confidences)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "marcel", "camille": "emilie"}
LABELS = {"lea": "Noémie", "herve": "Hervé", "camille": "Camille"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 916-954. At ASK after hours, Noemie confides in Herve and Camille "
               "about her complicated romantic history with her married neighbour Philippe. "
               "Adapted for A1 French.")

INTRO = ("At the ASK agency after hours, assistants Herve, Camille, and Noemie chat about their evening plans. "
         "Noemie reveals the ongoing romantic drama with her married neighbour Philippe. "
         "Let's listen to the scene in French first.")

STORY = [
 ("herve", "Que faites-vous ce soir, les filles?",
  "What are you doing tonight, girls?",
  [(924, "ce soir, les filles ?")], "Herve asks about evening plans"),
 ("camille", "Moi, je vais au théâtre ce soir.",
  "Me, I am going to the theater tonight.",
  [(925, "Moi, je vais au théâtre")], "Camille shares her plan"),
 ("herve", "Et toi Noémie, tu vois Philippe?",
  "And you Noemie, are you seeing Philippe?",
  [(927, "Avec qui ? Avec Philippe ?")], "Herve teases Noemie"),
 ("camille", "C'est qui exactement, ce Philippe?",
  "Who exactly is this Philippe?",
  [(930, "C'est qui, Philippe ?")], "Camille inquires"),
 ("herve", "Mais attends, c'est son cher voisin!",
  "Well wait, he is her dear neighbour!",
  [(938, "Philippe, c'est son voisin.")], "Herve explains who Philippe is"),
 ("lea", "En fait, Philippe est un homme marié.",
  "In fact, Philippe is a married man.",
  [(940, "il est marié,")], "Noemie reveals his status"),
 ("lea", "Nous avons eu une petite histoire secrète.",
  "We had a little secret affair.",
  [(940, "on a eu une liaison")], "Noemie admits the affair"),
 ("herve", "Ils vivent dans le même immeuble!",
  "They live in the same building!",
  [(943, "dans le même immeuble.")], "Herve highlights the proximity"),
 ("camille", "Tu devrais peut-être changer d'appartement.",
  "You should perhaps change apartments.",
  [(947, "je déménage rien.")], "Camille suggests moving"),
 ("lea", "Ah non, moi je reste ici!",
  "Oh no, I am staying here!",
  [(948, "Alors là, non.")], "Noemie refuses to leave"),
 ("lea", "C'est à lui de déménager, franchement.",
  "It is up to him to move, honestly.",
  [(949, "C'est plutôt à lui de déménager")], "Noemie stands her ground"),
 ("lea", "Je vois bien ses regards discrets.",
  "I clearly see his discreet glances.",
  [(952, "Je vois bien comment il me regarde.")], "Noemie notices his looks"),
 ("lea", "Je sais qu'il pense encore à moi!",
  "I know he still thinks of me!",
  [(952, "Je sais qu'il pense à moi.")], "Noemie remains confident"),
 ("herve", "Tu aimes les situations très compliquées!",
  "You love very complicated situations!",
  [(946, "comment tu fais")], "Herve comments on the drama"),
]

OPENER = "Let's examine how Noemie confides in Herve and Camille step by step."

WALK = [
 (0, None,
  "'What are you doing tonight, girls?' Herve asks his fellow assistants about their evening plans."),
 (1, None,
  "'Me, I am going to the theater tonight.' Camille shares her cultural plan after work."),
 (2, None,
  "'And you Noemie, are you seeing Philippe?' Herve teases Noemie about her romantic interest."),
 (3, None,
  "'Who exactly is this Philippe?' Camille asks for background on the mysterious man."),
 (4, None,
  "'Well wait, he is her dear neighbour!' Herve reveals that Philippe lives right next door."),
 (5, None,
  "'In fact, Philippe is a married man.' Noemie explains the complicated marital status of her lover."),
 (6, None,
  "'We had a little secret affair.' Noemie admits they shared a discreet past relationship."),
 (7, None,
  "'They live in the same building!' Herve points out the awkward proximity of the living situation."),
 (8, None,
  "'You should perhaps change apartments.' Camille suggests moving away to avoid daily run-ins."),
 (9, None,
  "'Oh no, I am staying here!' Noemie firmly refuses to leave her home because of him."),
 (10, None,
  "'It is up to him to move, honestly.' Noemie insists that Philippe should be the one to relocate."),
 (11, None,
  "'I clearly see his discreet glances.' Noemie notices lingering signs of mutual attraction in the hallways."),
 (12, None,
  "'I know he still thinks of me!' Noemie remains convinced of his ongoing feelings."),
 (13, None,
  "'You love very complicated situations!' Herve humorously highlights Noemie's taste for drama."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Noemie stands her ground in an awkward apartment building romance while Herve and Camille listen with amusement. "
         "Let's review the key expressions and vocabulary from this scene.")

CLOSING = ("herve", "Tu aimes les situations très compliquées!")
