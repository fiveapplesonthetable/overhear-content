# Authoring module for dix-pour-cent s04e03 scene 02 (cues 13-48).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-02.py --out out/dix-pour-cent/s04e03/scene-02.json

ID = "dix-pour-cent-s04e03-scene-02"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 2
TITLE = "Le retour du passé  (The Return of the Past)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jose": "theo", "laurence": "emilie"}
LABELS = {"lea": "Andréa", "jose": "José", "laurence": "Laurence"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 13-48. Andrea discovers Colette has left, "
               "then joins Jose Garcia on set where his ex-lover Laurence unexpectedly appears.")

INTRO = ("Devastated to find a farewell note from Colette, Andrea heads straight to the film studio. "
         "On set, an enthusiastic Jose Garcia describes his passionate new role, "
         "before a sudden encounter with his former partner Laurence completely throws him off balance. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("lea", "Colette m'a laissé un mot terrible.",
     "Colette left me a terrible note.",
     [(13, "On n'a plus de couches")], "Andrea recalls the parting message left at home"),
    ("lea", "Ce que tu fais est irresponsable!",
     "What you are doing is irresponsible!",
     [(17, "Ce que tu fais est irresponsable.")], "Andrea vents her frustration into Colette's voicemail"),
    ("jose", "Ça va être une bonne journée!",
     "It is going to be a good day!",
     [(26, "ça va être une bonne journée.")], "Jose greets Andrea warmly on the film set"),
    ("jose", "Ce nouveau rôle m'emballe vraiment.",
     "This new role truly excites me.",
     [(28, "Ce rôle m'emballe vraiment.")], "Jose explains how thrilled he feels about the character"),
    ("jose", "Je vais donner envie de manger.",
     "I will make people want to eat.",
     [(29, "donner envie de manger.")], "Jose talks enthusiastically about his culinary scenes"),
    ("jose", "Tu as l'air bizarre ce matin.",
     "You look strange this morning.",
     [(36, "T'as l'air bizarre.")], "Jose notices Andrea's worried expression"),
    ("lea", "C'est un peu tendu avec Colette.",
     "It is a bit tense with Colette.",
     [(37, "C'est un peu tendu")], "Andrea admits that her domestic life is troubled"),
    ("lea", "Sans Colette, tu veux dire.",
     "Without Colette, you mean.",
     [(39, "tu veux dire.")], "Andrea corrects herself sadly"),
    ("laurence", "José? Comment tu vas?",
     "Jose? How are you?",
     [(41, "Comment tu vas ?")], "Laurence suddenly approaches and greets her former lover"),
    ("laurence", "Ça fait vraiment une éternité!",
     "It has truly been ages!",
     [(41, "Ça fait une éternité.")], "Laurence remarks warmly on how many years have passed"),
    ("laurence", "Je suis ravie d'être sur ce tournage.",
     "I am delighted to be on this shoot.",
     [(44, "sur ce tournage.")], "Laurence shares her excitement about the project"),
    ("laurence", "À tout à l'heure sur le plateau.",
     "See you shortly on the movie set.",
     [(47, "sur le plateau.")], "Laurence waves goodbye as she heads off to makeup"),
    ("jose", "Laurence... Que fait-elle ici?",
     "Laurence... What is she doing here?",
     [(40, "Laurence.")], "Jose stares in stunned shock after Laurence walks away"),
    ("lea", "Tu la connais depuis longtemps?",
     "Have you known her for a long time?",
     [], "new: Andrea notices Jose's pale face and inquires"),
]

OPENER = "Let's explore this dramatic encounter line by line."

WALK = [
    (0, None,
     "'Colette left me a terrible note.' Andrea struggles to accept that Colette packed her bags and left."),
    (1, None,
     "'What you are doing is irresponsible!' Andrea leaves an exasperated message on Colette's phone."),
    (2, None,
     "'It is going to be a good day!' Jose welcomes his agent with cheerful optimism."),
    (3, None,
     "'This new role truly excites me.' Jose expresses deep enthusiasm for his creative performance."),
    (4, None,
     "'I will make people want to eat.' Jose describes how vibrant food preparation will bring the scene alive."),
    (5, None,
     "'You look strange this morning.' Jose perceives Andrea's visible distress and lack of focus."),
    (6, None,
     "'It is a bit tense with Colette.' Andrea confides that things are difficult at home."),
    (7, None,
     "'Without Colette, you mean.' Andrea acknowledges with bitter irony that Colette has walked out."),
    (8, None,
     "'Jose? How are you?' Laurence suddenly interrupts the agents with an affectionate greeting."),
    (9, None,
     "'It has truly been ages!' Laurence highlights how many years have elapsed since their last encounter."),
    (10, None,
     "'I am delighted to be on this shoot.' Laurence expresses genuine joy at joining the film cast."),
    (11, None,
     "'See you shortly on the movie set.' Laurence smiles politely before heading to the dressing rooms."),
    (12, None,
     "'Laurence... What is she doing here?' Jose remains petrified by the unexpected arrival of his ex-partner."),
    (13, None,
     "'Have you known her for a long time?' Andrea asks Jose about the history behind his shock."),
]

TRANSITION = "Now let's listen to the full exchange once more from start to finish."

OUTRO = ("Andrea's domestic crisis collides with Jose's sudden emotional turmoil on the movie set. "
         "Let's review the key theatrical and emotional vocabulary from this encounter.")

CLOSING = ("lea", "Le passé refait surface.")
