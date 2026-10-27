# Authoring module for dix-pour-cent s04e03 scene 15 (cues 666-709).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e03/authoring/scene-15.py --out overhear-content/out/dix-pour-cent/s04e03/scene-15.json

ID = "dix-pour-cent-s04e03-scene-15"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 15
TITLE = "À la crèche  (At the Daycare)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jose": "theo"}
LABELS = {"lea": "Andréa", "jose": "José"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 666-709. Frantic after finding her apartment empty, Andréa rushes to the daycare "
    "center and finds José Garcia happily holding baby Flora. While Andréa frantically accuses "
    "him of child abduction, José playfully urges her to breathe and stay zen before leaving for his set."
)

INTRO = (
    "Andrea rushes into the daycare center in absolute terror after finding her apartment empty. "
    "She discovers Jose Garcia happily cradling baby Flora, completely unbothered by her panic. "
    "Let's listen to their chaotic encounter in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Flora! Oh, mon bébé adoré!",
     "Flora! Oh, my beloved baby!",
     [(667, "mon bébé")], "Andréa rushes to her baby"),
    ("jose", "Andréa, tout va très bien ici.",
     "Andrea, everything is going very well here.",
     [(666, "Andréa, ça va ?"), (669, "tout va bien")], "José welcomes her calmly"),
    ("lea", "C'est un enlèvement d'enfant!",
     "It is a child abduction!",
     [(681, "enlèvement d'enfant")], "Andréa accuses José"),
    ("jose", "Mais non, j'ai laissé un mot!",
     "Of course not, I left a note!",
     [(670, "J'ai laissé un mot")], "José defends his actions"),
    ("lea", "Tu es complètement fou, José!",
     "You are completely crazy, Jose!",
     [(668, "T'es folle")], "Andréa vents her shock"),
    ("jose", "Regarde, elle est très heureuse.",
     "Look, she is very happy.",
     [(672, "Regarde")], "José shows baby Flora"),
    ("jose", "Bonjour Princesse Joues-rebondies!",
     "Hello Princess Chubby-cheeks!",
     [(673, "Princesse Joues-rebondies")], "José teases baby Flora"),
    ("lea", "Elle est où, la directrice?",
     "Where is the director?",
     [(675, "Elle est où")], "Andréa searches for the staff"),
    ("jose", "Capucine s'occupe des autres enfants.",
     "Capucine takes care of the other children.",
     [(678, "s'appelle Capucine")], "José explains the situation"),
    ("jose", "Allez, calme-toi et respire un peu.",
     "Come on, calm down and breathe a bit.",
     [(683, "calme-toi"), (684, "respire")], "José urges Andréa to relax"),
    ("jose", "Regarde, nous sommes totalement zen.",
     "Look, we are totally zen.",
     [(688, "Regarde, on est zen")], "José models calm behavior"),
    ("lea", "Une voiture t'attend pour le tournage.",
     "A car is waiting for you for the shoot.",
     [(692, "Une voiture t'attend")], "Andréa refocuses on work"),
    ("jose", "D'accord, je pars immédiatement.",
     "All right, I am leaving immediately.",
     [(703, "José. On y va")], "José agrees to leave"),
    ("lea", "Ne touche plus jamais à mon bébé!",
     "Never touch my baby again!",
     [(667, "mon bébé")], "Andréa gives a final warning"),
]

WALK = [
    (0, None,
     "'Flora! Oh, my beloved baby!' Andrea bursts into tears of relief upon spotting her child. "
     "The possessive adjective 'mon' introduces the masculine noun 'bebe'."),
    (1, None,
     "'Andrea, everything is going very well here.' Jose is startled by Andrea's frantic entrance. "
     "The phrase 'tout va bien' indicates that all is fine."),
    (2, None,
     "'It is a child abduction!' Andrea furiously accuses Jose of taking her daughter without consent. "
     "The compound noun 'enlevement d'enfant' means kidnapping."),
    (3, None,
     "'Of course not, I left a note!' Jose defends himself by pointing to the note he wrote. "
     "The past tense 'ai laisse' comes from 'laisser'."),
    (4, None,
     "'You are completely crazy, Jose!' Andrea vents her fury at his reckless behavior. "
     "The adjective 'fou' describes someone out of their mind."),
    (5, None,
     "'Look, she is very happy.' Jose points out that baby Flora is cooing and smiling peacefully. "
     "The feminine adjective 'heureuse' describes joy."),
    (6, None,
     "'Hello Princess Chubby-cheeks!' Jose affectionately nicknames the baby after her round face. "
     "The compound term 'joues-rebondies' refers to plump cheeks."),
    (7, None,
     "'Where is the director?' Andrea demands to know who authorized Jose to bring Flora in. "
     "The question 'elle est ou' is colloquial for where is she."),
    (8, None,
     "'Capucine takes care of the other children.' Jose explains that the daycare supervisor is in the next room. "
     "The verb phrase 's'occuper de' means to look after."),
    (9, None,
     "'Come on, calm down and breathe a bit.' Jose coaches his stressed agent through breathing exercises. "
     "The imperative 'calme-toi' urges relaxation."),
    (10, None,
     "'Look, we are totally zen.' Jose demonstrates how peaceful the nursery atmosphere is. "
     "The adjective 'zen' means relaxed and calm."),
    (11, None,
     "'A car is waiting for you for the shoot.' Andrea reminds Jose of his strict filming schedule. "
     "The noun 'tournage' denotes a film shoot."),
    (12, None,
     "'All right, I am leaving immediately.' Jose hands Flora over and prepares for his work day. "
     "The adverb 'immediatement' indicates promptness."),
    (13, None,
     "'Never touch my baby again!' Andrea sets a firm boundary with her unpredictable star client. "
     "The negative structure 'ne ... plus jamais' means never again."),
]

OUTRO = (
    "Andrea recovers her baby daughter safely from Jose Garcia at the daycare center. "
    "Relieved yet exhausted by the scare, she sends Jose off to his film set while hugging Flora tightly. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("jose", "À plus tard, maman stressée!")
