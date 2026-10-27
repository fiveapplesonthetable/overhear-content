# Authoring module for dix-pour-cent s04e03 scene 21 (cues 994-995).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-21.py --out out/dix-pour-cent/s04e03/scene-21.json

ID = "dix-pour-cent-s04e03-scene-21"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 21
TITLE = "Le service d'étage  (Room Service)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jose": "theo"}
LABELS = {"lea": "Andréa", "jose": "José"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 994-995. Sitting down at the table in the hotel room, Jose and Andrea inspect the ordered dishes. "
    "Famished from the chaotic day on set, Jose delights in the food and urges Andrea to take a well-deserved break."
)

INTRO = (
    "Sitting down at the table in the hotel room, Jose and Andrea inspect the ordered dishes. "
    "Famished from the chaotic day on set, Jose delights in the food and urges Andrea to take a well-deserved break. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("jose", "Alors, ce service en chambre arrive?",
     "So, is this room service coming?",
     [(994, "Alors…"), (995, "Il y a un service en chambre ?")], "Inquired eagerly about the food arrival"),
    ("lea", "Le dîner est déjà bien servi.",
     "Dinner is already nicely served.",
     [(995, "service en chambre")], "Pointed out the arranged dishes"),
    ("jose", "J'ai une faim absolument terrible.",
     "I have an absolutely terrible hunger.",
     [(995, "service en chambre")], "Expressed his enormous appetite"),
    ("lea", "Tu as à peine déjeuné aujourd'hui.",
     "You barely had lunch today.",
     [(995, "service en chambre")], "Noted his busy filming schedule"),
    ("jose", "Le réalisateur me rendait totalement fou.",
     "The director was driving me totally crazy.",
     [(995, "service en chambre")], "Complained about the difficult director"),
    ("lea", "Tu as sauvé la scène finale.",
     "You saved the final scene.",
     [(995, "service en chambre")], "Praised his screen resilience"),
    ("jose", "Grâce à ton énergie débordante, Andréa.",
     "Thanks to your overflowing energy, Andrea.",
     [(995, "service en chambre")], "Toasted her tireless agency dedication"),
    ("lea", "Mange un peu avant que ça refroidisse.",
     "Eat a little before it gets cold.",
     [(995, "service en chambre")], "Encouraged him to enjoy the warm meal"),
    ("jose", "Prends une assiette avec moi.",
     "Take a plate with me.",
     [(995, "service en chambre")], "Offered to share the hotel dinner"),
    ("lea", "Je n'ai pas très faim ce soir.",
     "I am not very hungry tonight.",
     [(995, "service en chambre")], "Declined food quietly"),
    ("jose", "Tu dois penser à toi parfois.",
     "You must think of yourself sometimes.",
     [(995, "service en chambre")], "Urged her to look after her health"),
    ("lea", "Je n'arrive jamais à décrocher.",
     "I never manage to switch off.",
     [(995, "service en chambre")], "Confessed her chronic workaholic habits"),
    ("jose", "Cette nuit, oublie un peu l'agence.",
     "Tonight, forget the agency for a bit.",
     [(995, "service en chambre")], "Advised her to take a mental break"),
    ("lea", "C'est plus facile à dire qu'à faire.",
     "It is easier said than done.",
     [(995, "service en chambre")], "Acknowledged the difficulty of resting")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'So, is this room service coming?' Jose looks eagerly at the covered dishes. "
     "The interrogative phrase anticipates a hearty meal."),
    (1, None,
     "'Dinner is already nicely served.' Andrea uncovers the hot plates. "
     "The adverb bien emphasizes the appealing presentation."),
    (2, None,
     "'I have an absolutely terrible hunger.' Jose rubs his hands together with enthusiasm. "
     "The strong adjective exaggerates his appetite."),
    (3, None,
     "'You barely had lunch today.' Andrea notes his hectic schedule on set. "
     "The adverbial phrase expressing barely recalls his missed break."),
    (4, None,
     "'The director was driving me totally crazy.' Jose recounts the tense friction with the crew. "
     "The imperfect verb recalls the artistic pressure."),
    (5, None,
     "'You saved the final scene.' Andrea reassures him of his great acting. "
     "The compound past celebrates his screen performance."),
    (6, None,
     "'Thanks to your overflowing energy, Andrea.' Jose toasts her with his water glass. "
     "The descriptive adjective praises her tireless drive."),
    (7, None,
     "'Eat a little before it gets cold.' Andrea gestures toward his warm plate. "
     "The subjunctive clause urges him to eat promptly."),
    (8, None,
     "'Take a plate with me.' Jose invites her to share the feast. "
     "The imperative verb offers warm companionship."),
    (9, None,
     "'I am not very hungry tonight.' Andrea declines gently with a quiet sigh. "
     "The negative expression reflects her inner preoccupation."),
    (10, None,
     "'You must think of yourself sometimes.' Jose advises her with genuine care. "
     "The modal verb construction urges healthy boundaries."),
    (11, None,
     "'I never manage to switch off.' Andrea admits her constant workaholic habits. "
     "The colloquial verb decrocher describes letting go."),
    (12, None,
     "'Tonight, forget the agency for a bit.' Jose encourages her to let down her guard. "
     "The temporal phrase defines an oasis of rest."),
    (13, None,
     "'It is easier said than done.' Andrea smiles faintly at the advice. "
     "The common proverb recognizes the difficulty of resting.")
]

TRANSITION = "Now, listen to the complete dialogue again at normal conversational pace."
OUTRO = "Sharing late-night room service allows Jose and Andrea to open up about life beyond the screen."
CLOSING = ("lea", "C'est plus facile à dire qu'à faire.")
