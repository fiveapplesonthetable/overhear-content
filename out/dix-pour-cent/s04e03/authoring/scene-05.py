# Authoring module for dix-pour-cent s04e03 scene 05 (cues 112-194).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-05.py --out out/dix-pour-cent/s04e03/scene-05.json

ID = "dix-pour-cent-s04e03-scene-05"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 5
TITLE = "Le shooting de Tiffany's  (The Tiffany's Shoot)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "sophia": "emilie"}
LABELS = {"lea": "Camille", "sophia": "Sophia"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 112-194. Sophia struggles with a hangover before a Tiffany's photo shoot, "
               "confiding to Camille her mixed feelings about Gabriel and his new partner.")

INTRO = ("Before a major commercial photo shoot for Tiffany's, Sophia nurses an exhausting hangover. "
         "She confides to Camille that she drank too much after Gabriel left the agency party with his new girlfriend. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("lea", "Tu vas bien? Tu sembles très fatiguée.",
     "Are you well? You seem very tired.",
     [(112, "Tu vas bien ?")], "Camille notices Sophia looking visibly drained"),
    ("sophia", "Non, je ne me sens pas bien.",
     "No, I do not feel well.",
     [(113, "Je ne me sens pas bien.")], "Sophia admits her poor physical condition"),
    ("sophia", "Peut-on reporter ce rendez-vous photo important?",
     "Can we postpone this important photo shoot?",
     [(114, "reporter")], "Sophia asks if rescheduling is possible"),
    ("lea", "On ne reporte jamais un tel shooting!",
     "One never postpones such a shoot!",
     [(115, "On ne reporte pas un shooting pour Tiffany's.")], "Camille stresses the strict commercial deadline"),
    ("sophia", "J'ai une affreuse gueule de bois.",
     "I have an awful hangover.",
     [(116, "gueule de bois.")], "Sophia confesses the cause of her exhaustion"),
    ("lea", "Ils te voient comme l'ambassadrice parfaite.",
     "They see you as the perfect ambassador.",
     [(118, "ambassadrice parfaite.")], "Camille reminds her of the luxury brand's high expectations"),
    ("sophia", "Ma féminité est plutôt à plat aujourd'hui.",
     "My femininity is rather flat today.",
     [(121, "féminité")], "Sophia jokes dryly about feeling unglamorous"),
    ("lea", "Qu'est-ce qui ne va pas, Sophia?",
     "What is wrong, Sophia?",
     [(122, "Qu'est-ce qui ne va pas ?")], "Camille gently probes for the emotional root of the trouble"),
    ("sophia", "Hier soir, Gabriel m'a plantée là.",
     "Last night, Gabriel abandoned me there.",
     [(139, "Il m'a plantée là")], "Sophia reveals how Gabriel left her stranded at the bar"),
    ("sophia", "Il est parti avec sa petite amie.",
     "He left with his girlfriend.",
     [(126, "petite amie")], "Sophia mentions Gabriel's romantic departure with Sarah"),
    ("sophia", "J'ai bu deux verres toute seule!",
     "I drank two glasses all alone!",
     [(140, "les boire toutes les deux.")], "Sophia explains why she finished both cocktails"),
    ("lea", "Ne sois pas jalouse, pense au travail!",
     "Do not be jealous, think of work!",
     [(134, "je ne suis pas jalouse.")], "Camille encourages her friend to focus on career goals"),
    ("sophia", "D'accord, je vais assurer ce beau shooting.",
     "All right, I will deliver on this fine shoot.",
     [(152, "une belle journée.")], "Sophia rallies her spirits for the commercial session"),
]

OPENER = "Let's explore Camille and Sophia's heartfelt conversation line by line."

WALK = [
    (0, None,
     "'Are you well? You seem very tired.' Camille gently observes Sophia's obvious fatigue before the shoot."),
    (1, None,
     "'No, I do not feel well.' Sophia openly acknowledges that she feels physically unwell."),
    (2, None,
     "'Can we postpone this important photo shoot?' Sophia tentatively asks if the session could be delayed."),
    (3, None,
     "'One never postpones such a shoot!' Camille explains that prestigious fashion shoots cannot be moved."),
    (4, None,
     "'I have an awful hangover.' Sophia admits she is suffering from a heavy morning hangover."),
    (5, None,
     "'They see you as the perfect ambassador.' Camille reminds her that the jewelers consider her an ideal brand face."),
    (6, None,
     "'My femininity is rather flat today.' Sophia laments with irony that her energy feels totally depleted."),
    (7, None,
     "'What is wrong, Sophia?' Camille invites her friend to share the deeper cause of her distress."),
    (8, None,
     "'Last night, Gabriel abandoned me there.' Sophia admits that she felt stung when Gabriel deserted her."),
    (9, None,
     "'He left with his girlfriend.' Sophia explains that Gabriel walked out of the gathering with Sarah."),
    (10, None,
     "'I drank two glasses all alone!' Sophia explains how she ended up finishing both ordered drinks herself."),
    (11, None,
     "'Do not be jealous, think of work!' Camille urges Sophia not to let romantic jealousy derail her career."),
    (12, None,
     "'All right, I will deliver on this fine shoot.' Sophia resolves to put personal feelings aside and do her best."),
]

TRANSITION = "Now let's listen to Camille and Sophia's exchange once more from start to finish."

OUTRO = ("Sophia overcomes romantic disappointment to prepare professionally for a prestigious brand campaign. "
         "Let's review the key emotional and commercial vocabulary from this scene.")

CLOSING = ("sophia", "D'accord, je vais assurer ce beau shooting.")
