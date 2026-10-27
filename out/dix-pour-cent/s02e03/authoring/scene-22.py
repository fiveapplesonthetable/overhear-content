# Authoring module for dix-pour-cent s02e03 scene 22 (cues 562-594).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-22.py --out out/dix-pour-cent/s02e03/scene-22.json

ID = "dix-pour-cent-s02e03-scene-22"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 22
TITLE = "Le permis de conduire  (The Driving Test)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "examinateur": "theo"}
LABELS = {"lea": "Norman", "examinateur": "L'examinateur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 562-594. Norman takes his practical driving exam with a strict examiner. "
    "To his immense relief, the drive goes smoothly and the examiner discreetly hints that he has passed."
)

INTRO = (
    "Inside the test vehicle, nervous candidate Norman Thavaud embarks on his fourth attempt at the practical driving exam. "
    "Guiding the car through busy city streets, Norman manages to keep his cool and successfully impresses the strict examiner. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "J'adore vraiment conduire.",
     "I truly love driving.",
     [(562, "J'adore conduire")], ""),
    ("lea", "Je pourrais rouler indéfiniment.",
     "I could drive indefinitely.",
     [(563, "Je pourrais conduire indéfiniment")], ""),
    ("examinateur", "C'est bien, mais concentrez-vous.",
     "That is fine, but concentrate.",
     [(566, "L'horizon c'est bien, Norman, mais concentre-toi")], ""),
    ("examinateur", "Ici, on tourne à droite.",
     "Here, we turn right.",
     [(568, "Ici, on tourne à droite")], ""),
    ("lea", "N'oubliez pas le clignotant!",
     "Do not forget the turn signal!",
     [(570, "Le clignotant, bien sûr")], ""),
    ("examinateur", "Attention au passage pour piétons.",
     "Watch out for the pedestrian crossing.",
     [(574, "Allez, madame")], ""),
    ("examinateur", "Laissez passer cette dame d'abord.",
     "Let that lady cross first.",
     [(577, "Laissez-moi vous aider, madame")], ""),
    ("lea", "La route est totalement dégagée.",
     "The road is completely clear.",
     [(573, "Zone dégagée. Je répète, zone dégagée")], ""),
    ("examinateur", "Garez la voiture le long du trottoir.",
     "Park the car along the sidewalk.",
     [(581, "Messieurs, les résultats vous seront envoyés")], ""),
    ("examinateur", "Ça s'est plutôt bien passé.",
     "It went rather well.",
     [(583, "ça a l'air de s'être assez bien passé cette fois")], ""),
    ("lea", "Vous voulez dire que j'ai réussi?",
     "You mean that I passed?",
     [(585, "Vous voulez dire que j'ai réussi ?")], ""),
    ("examinateur", "Je n'ai absolument rien dit!",
     "I said absolutely nothing!",
     [(585, "Je n'ai rien dit")], ""),
    ("lea", "Merci beaucoup, c'est formidable!",
     "Thank you very much, that is wonderful!",
     [(586, "Oh ! Merci !"), (588, "Oui, oui. J'ai eu mon permis !")], ""),
    ("examinateur", "Maintenant, sortez du véhicule.",
     "Now, exit the vehicle.",
     [(587, "Maintenant partez !")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'I truly love driving.' Norman expresses his newfound enthusiasm behind the steering wheel. "
     "The verb adorer indicates strong personal enjoyment."),
    (1, None,
     "'I could drive indefinitely.' He feels surprisingly relaxed and confident on the road. "
     "The conditional form pourrais expresses hypothetical ability."),
    (2, None,
     "'That is fine, but concentrate.' The driving examiner sternly reminds him to stay focused on traffic. "
     "The reflexive imperative concentrez-vous demands full attention."),
    (3, None,
     "'Here, we turn right.' The official gives the next directional instruction. "
     "The prepositional phrase a droite indicates turning to the right."),
    (4, None,
     "'Do not forget the turn signal!' Norman reminds himself aloud to signal properly before turning. "
     "The noun clignotant refers to the vehicle flashing indicator."),
    (5, None,
     "'Watch out for the pedestrian crossing.' The examiner points out an approaching danger on the street. "
     "The prepositional phrase attention au gives a warning."),
    (6, None,
     "'Let that lady cross first.' The candidate must yield right of way to walking pedestrians. "
     "The causative structure laissez passer means allow someone to pass."),
    (7, None,
     "'The road is completely clear.' Norman checks his mirrors and assesses the traffic situation. "
     "The feminine adjective degagee means unobstructed."),
    (8, None,
     "'Park the car along the sidewalk.' The final maneuver test is requested by the examiner. "
     "The prepositional locution le long du means along the side of the street."),
    (9, None,
     "'It went rather well.' The official hints at a surprisingly positive assessment. "
     "The adverbial phrase plutot bien indicates a favorable impression."),
    (10, None,
     "'You mean that I passed?' Norman hopes for confirmation that he finally earned his license. "
     "The idiom vouloir dire asks for intended meaning."),
    (11, None,
     "'I said absolutely nothing!' The examiner refuses to break official confidentiality rules. "
     "The negative construction n'ai rien dit expresses strict silence."),
    (12, None,
     "'Thank you very much, that is wonderful!' Norman rejoices at having overcome his driving exam anxiety. "
     "The adjective formidable expresses intense relief."),
    (13, None,
     "'Now, exit the vehicle.' The official dismisses the candidate at the end of the test. "
     "The imperative sortez orders him to step out."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Norman celebrates a successful driving exam that opens the door to his new movie role. "
    "Remember the common conversational idiom for asking what someone means: vouloir dire."
)

CLOSING = ("examinateur", "Maintenant, sortez du véhicule.")
