# Authoring module for dix-pour-cent s04e03 scene 01 (cues 1-12).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-01.py --out out/dix-pour-cent/s04e03/scene-01.json

ID = "dix-pour-cent-s04e03-scene-01"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 1
TITLE = "Réveil matinal  (Early Wake-Up)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-12. Andrea wakes up early to care for baby Flora, "
               "then Gabriel calls about Jose Garcia's film shoot.")

INTRO = ("At five in the morning, Andrea wakes up to soothe her baby daughter Flora. "
         "She tenderly notes that the restless infant takes after her own night-owl habits, "
         "just before Gabriel calls to coordinate an early start on the movie set. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("lea", "J'arrive, mon petit bébé, j'arrive!",
     "I am coming, my little baby, I am coming!",
     [(1, "J'arrive, mon bébé !")], "Andrea rushes into the nursery to comfort Flora"),
    ("lea", "Te voilà enfin réveillée si tôt.",
     "There you are finally awake so early.",
     [(2, "Te voilà !"), (3, "Te voilà.")], "Andrea picks up her smiling daughter from her crib"),
    ("lea", "Qu'est-ce que tu fais debout à cette heure?",
     "What are you doing up at this hour?",
     [(6, "debout à cette heure-ci ?")], "Andrea asks her baby why she woke before dawn"),
    ("lea", "Cinq heures du matin, ce n'est pas l'heure.",
     "Five in the morning is no time to wake up.",
     [(7, "Cinq heures du mat")], "Andrea playfully explains normal sleeping hours"),
    ("lea", "Tu es bien réveillée, dis-moi.",
     "You are wide awake, tell me.",
     [(9, "T'es bien réveillée")], "Andrea smiles at Flora's lively energy"),
    ("lea", "À cette heure, maman était en boîte.",
     "At this hour, mommy was in nightclubs.",
     [(10, "en boîte de nuit.")], "Andrea remembers her past party life"),
    ("lea", "Tu tiens vraiment de maman Andréa!",
     "You truly take after mommy Andrea!",
     [(11, "Tu tiens de maman Andréa.")], "Andrea notes the striking nocturnal resemblance"),
    ("lea", "On va aller voir maman Colette?",
     "Shall we go see mommy Colette?",
     [(12, "On va voir maman Colette ?")], "Andrea suggests greeting Colette in the bedroom"),
    ("lea", "Allô Gabriel? Pourquoi m'appelles-tu si tôt?",
     "Hello Gabriel? Why are you calling me so early?",
     [], "new: Andrea answers a sudden early phone call"),
    ("gabriel", "José Garcia t'attend déjà sur le plateau.",
     "Jose Garcia is already waiting for you on the movie set.",
     [], "new: Gabriel reminds Andrea of the filming schedule"),
    ("lea", "Je sais, je prépare ma fille Flora.",
     "I know, I am getting my daughter Flora ready.",
     [], "new: Andrea explains she is dressing the baby"),
    ("gabriel", "Ne sois pas en retard ce matin.",
     "Do not be late this morning.",
     [], "new: Gabriel urges punctuality for the star actor"),
    ("lea", "J'arrive tout de suite au tournage.",
     "I am coming right away to the film shoot.",
     [], "new: Andrea promises to arrive quickly"),
    ("gabriel", "Parfait, je compte sur toi, Andréa.",
     "Perfect, I count on you, Andrea.",
     [], "new: Gabriel expresses confidence in Andrea"),
]

OPENER = "Let's explore Andrea and Gabriel's early conversation line by line."

WALK = [
    (0, None,
     "'I am coming, my little baby, I am coming!' Andrea reassures Flora as she hurries into her nursery."),
    (1, None,
     "'There you are finally awake so early.' Andrea greets her infant daughter with gentle affection."),
    (2, None,
     "'What are you doing up at this hour?' Andrea asks why the baby has woken up so long before dawn."),
    (3, None,
     "'Five in the morning is no time to wake up.' Andrea explains that early dawn is far too early for breakfast."),
    (4, None,
     "'You are wide awake, tell me.' Andrea observes her child's alert eyes and active movements."),
    (5, None,
     "'At this hour, mommy was in nightclubs.' Andrea fondly reminisces about her youthful Parisian nights."),
    (6, None,
     "'You truly take after mommy Andrea!' Andrea acknowledges that her daughter shares her energetic nocturnal nature."),
    (7, None,
     "'Shall we go see mommy Colette?' Andrea suggests going together to wake up her partner."),
    (8, None,
     "'Hello Gabriel? Why are you calling me so early?' Andrea wonders why her business partner rings at daybreak."),
    (9, None,
     "'Jose Garcia is already waiting for you on the movie set.' Gabriel warns her that the lead actor has arrived."),
    (10, None,
     "'I know, I am getting my daughter Flora ready.' Andrea explains that she must dress and pack for the baby."),
    (11, None,
     "'Do not be late this morning.' Gabriel insists on total professionalism on the production set."),
    (12, None,
     "'I am coming right away to the film shoot.' Andrea reassures him that she will leave the apartment immediately."),
    (13, None,
     "'Perfect, I count on you, Andrea.' Gabriel trusts his partner to handle the demanding actor smoothly."),
]

TRANSITION = "Now let's listen to Andrea and Gabriel's exchange once more from start to finish."

OUTRO = ("Andrea balances motherhood with agency duties as she rushes to support her star client on set. "
         "Let's review the key family and scheduling terms introduced in this opening scene.")

CLOSING = ("lea", "Une longue journée nous attend.")
