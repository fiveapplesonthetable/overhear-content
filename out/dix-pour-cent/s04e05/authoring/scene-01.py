# Authoring module for dix-pour-cent s04e05 scene 01 (cues 1-18).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e05/authoring/scene-01.py --out out/dix-pour-cent/s04e05/scene-01.json

ID = "dix-pour-cent-s04e05-scene-01"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 1
TITLE = "Panique matinale  (Morning Panic)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "chauffeur": "theo"}
LABELS = {"lea": "Andréa", "chauffeur": "Chauffeur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-18. Andrea panics on the sidewalk with baby Flora after her nanny abruptly quits, "
               "struggling to find a taxi or ride to pick up Sigourney Weaver at Roissy.")

INTRO = ("Early in the morning on the Parisian streets, Andrea Martel faces an acute childcare crisis when her nanny abruptly resigns. "
         "Left stranded on the pavement with baby Flora, she struggles in vain to hail a taxi without a mandatory infant car seat. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("chauffeur", "Pas de siège bébé, pas de taxi!",
     "No baby seat, no taxi!",
     [(7, "Pas de siège bébé, pas de taxi")], "The taxi driver refuses to take Andrea with her infant"),
    ("lea", "Mais je suis vraiment très pressée!",
     "But I am truly in a great hurry!",
     [], "new: Andrea pleads with the stubborn driver"),
    ("chauffeur", "Ce n'est pas moi qui fais les règles.",
     "It is not me who makes the rules.",
     [(7, "Ce n'est pas moi qui fais les règles.")], "The driver reminds her of strict road safety laws"),
    ("lea", "Je vais commander une autre voiture.",
     "I am going to order another car.",
     [], "new: Andrea pulls out her phone to check ride apps"),
    ("chauffeur", "Ils vous diront exactement la même chose.",
     "They will tell you exactly the same thing.",
     [(9, "Ils vous diront la même chose.")], "The driver warns that private hire cars follow the same laws"),
    ("lea", "Ma nounou vient de me lâcher!",
     "My nanny just bailed on me!",
     [], "new: Andrea vents her acute domestic frustration"),
    ("lea", "Et la petite Flora est très triste.",
     "And little Flora is very sad.",
     [(4, "Et Flora est très triste.")], "Andrea comforts her restless daughter in the stroller"),
    ("lea", "Je dois aller chercher Sigourney Weaver!",
     "I must go pick up Sigourney Weaver!",
     [(10, "Sigourney Weaver")], "Andrea stresses the high-stakes Hollywood arrival at the airport"),
    ("chauffeur", "Prenez le métro avec votre poussette.",
     "Take the metro with your stroller.",
     [], "new: The driver suggests public transit as an alternative"),
    ("lea", "Flora, tu n'as jamais pris le métro.",
     "Flora, you have never taken the metro.",
     [(13, "T'as jamais pris le métro")], "Andrea speaks tenderly to her daughter"),
    ("lea", "Tu vas détester ce long voyage.",
     "You will hate this long trip.",
     [(14, "Tu vas détester ça.")], "Andrea dreads the noisy crowded underground corridors"),
    ("lea", "Le trajet dure plus d'une heure!",
     "The journey takes more than an hour!",
     [], "new: Andrea calculates the tedious suburban train transit"),
    ("lea", "Qu'est-ce que je fais maintenant?",
     "What do I do now?",
     [(16, "Qu'est-ce que je fais maintenant?")], "Andrea stands helpless on the pavement"),
    ("lea", "Je dois appeler Camille au secours.",
     "I must call Camille for help.",
     [], "new: Andrea decides to delegate the airport greeting to her assistant"),
]

OPENER = "Let's explore Andrea and the taxi driver's stressful morning exchange line by line."

WALK = [
    (0, None,
     "'No baby seat, no taxi!' The taxi driver firmly explains that safety regulations forbid transporting babies without proper seats."),
    (1, None,
     "'But I am truly in a great hurry!' Andrea begs the driver to overlook the restriction for an emergency."),
    (2, None,
     "'It is not me who makes the rules.' The driver shrugs off her pleas, pointing out municipal transport rules."),
    (3, None,
     "'I am going to order another car.' Andrea checks ride-hailing applications on her smartphone."),
    (4, None,
     "'They will tell you exactly the same thing.' The cabbie cautions that all commercial chauffeurs face heavy fines."),
    (5, None,
     "'My nanny just bailed on me!' Andrea laments that her sudden household emergency has thrown her schedule into chaos."),
    (6, None,
     "'And little Flora is very sad.' Andrea rocks the stroller gently as baby Flora whimpers on the sidewalk."),
    (7, None,
     "'I must go pick up Sigourney Weaver!' Andrea reveals that an international screen legend is landing at Charles de Gaulle."),
    (8, None,
     "'Take the metro with your stroller.' The driver gestures toward the nearby subterranean metro entrance."),
    (9, None,
     "'Flora, you have never taken the metro.' Andrea worries about navigating endless underground stairs with a pram."),
    (10, None,
     "'You will hate this long trip.' Andrea sighs at the prospect of subjecting an infant to the noisy morning rush."),
    (11, None,
     "'The journey takes more than an hour!' Andrea calculates that subway connections to the airport will take far too long."),
    (12, None,
     "'What do I do now?' Andrea experiences a moment of acute professional and parental despair."),
    (13, None,
     "'I must call Camille for help.' Andrea resolves to contact her junior agent Camille to greet the star on time."),
]

TRANSITION = "Now let's listen to Andrea's morning dilemma once more from start to finish."

OUTRO = ("Andrea navigates an unexpected childcare and logistical crisis on the streets of Paris. "
         "Let's review the key vocabulary of transit, childcare, and urgent scheduling from this opening scene.")

CLOSING = ("lea", "La journée commence très mal.")
