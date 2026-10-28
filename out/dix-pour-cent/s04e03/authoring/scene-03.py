# Authoring module for dix-pour-cent s04e03 scene 03 (cue 49).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-03.py --out out/dix-pour-cent/s04e03/scene-03.json

ID = "dix-pour-cent-s04e03-scene-03"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 3
TITLE = "Le choc de José  (José's Shock)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jose": "theo"}
LABELS = {"lea": "Andréa", "jose": "José"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = ("Cue 49. Following Laurence's sudden appearance, "
               "Jose panics and develops sudden hiccups while Andrea tries to calm him down.")

INTRO = ("Left reeling after Laurence walks away, Jose Garcia freezes in complete shock on set. "
         "As sudden nervous hiccups overwhelm him, Andrea tries desperately to restore his composure "
         "before the director calls the actors to the soundstage. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("lea", "José? Tu m'entends?",
     "Jose? Do you hear me?",
     [(49, "José ?")], "Andrea tries to break through Jose's stunned silence"),
    ("jose", "Je ne peux pas y croire.",
     "I cannot believe it.",
     [], "new: Jose stares blankly in shock"),
    ("lea", "Qu'est-ce qui t'arrive tout à coup?",
     "What is happening to you all of a sudden?",
     [], "new: Andrea asks why he is paralyzed with fear"),
    ("jose", "Laurence est mon grand amour de jeunesse.",
     "Laurence is my great youth romance.",
     [], "new: Jose reveals his past history with Laurence"),
    ("jose", "Nous nous sommes quittés très fâchés.",
     "We parted on very angry terms.",
     [], "new: Jose explains how badly their relationship ended"),
    ("lea", "Cela remonte à vingt ans déjà!",
     "That goes back twenty years already!",
     [], "new: Andrea reminds him of how much time has passed"),
    ("jose", "Je ne peux pas jouer avec elle.",
     "I cannot act with her.",
     [], "new: Jose panics about performing romantic scenes"),
    ("jose", "Mon cœur bat beaucoup trop vite.",
     "My heart is beating much too fast.",
     [], "new: Jose feels acute physical anxiety"),
    ("lea", "Respire profondément et calme-toi.",
     "Breathe deeply and calm down.",
     [], "new: Andrea coaches him through relaxation techniques"),
    ("jose", "J'ai un terrible hoquet qui commence.",
     "I have terrible hiccups beginning.",
     [], "new: Jose starts hiccuping from intense stress"),
    ("jose", "Le réalisateur va bientôt nous appeler.",
     "The director will call us soon.",
     [], "new: Jose worries about impending call time"),
    ("lea", "Bois un grand verre d'eau fraîche.",
     "Drink a large glass of cool water.",
     [], "new: Andrea suggests a remedy for his hiccups"),
    ("jose", "Je ne serai jamais prêt à temps.",
     "I will never be ready on time.",
     [], "new: Jose despairs about his acting readiness"),
    ("lea", "Tu es un acteur formidable, José.",
     "You are a wonderful actor, Jose.",
     [], "new: Andrea offers strong encouragement"),
]

OPENER = "Let's explore Andrea and Jose's urgent conversation line by line."

WALK = [
    (0, None,
     "'Jose? Do you hear me?' Andrea snaps her fingers to regain Jose's attention. The clause hinges on the everyday verb meaning 'hear'."),
    (1, None,
     "'I cannot believe it.' Jose remains dumbfounded by Laurence's unexpected presence. Notice the classic French sandwich negation wrapping right around 'can'."),
    (2, None,
     "'What is happening to you all of a sudden?' Andrea inquiries about his sudden pallor and paralysis. The verb meaning 'am coming' pairs naturally with the noun for 'blow' in everyday conversation."),
    (3, None,
     "'Laurence is my great youth romance.' Jose confesses that Laurence was his deepest early love. The descriptive adjective for 'great' agrees in gender and number with its noun."),
    (4, None,
     "'We parted on very angry terms.' Jose recalls their stormy and painful separation years ago. The descriptive adjective for 'angry' agrees in gender and number with its noun."),
    (5, None,
     "'That goes back twenty years already!' Andrea emphasizes that decades have healed old wounds. Notice how 'dates back' leads directly into the noun meaning 'years'."),
    (6, None,
     "'I cannot act with her.' Jose expresses intense anxiety about shooting intimate scenes together. The two-part French negation brackets the verb for 'can' on both sides."),
    (7, None,
     "'My heart is beating much too fast.' Jose describes the physical symptoms of his panic attack. The verb meaning 'beats' pairs naturally with the noun for 'heart' in everyday conversation."),
    (8, None,
     "'Breathe deeply and calm down.' Andrea coaches him through relaxation techniques. The clause hinges on the everyday verb meaning 'breathe'."),
    (9, None,
     "'I have terrible hiccups beginning.' Jose reveals that his nervous spasm is triggering sudden hiccups. The descriptive adjective for 'terrible' agrees in gender and number with its noun."),
    (10, None,
     "'The director will call us soon.' Jose fears ruining the shooting schedule. The verb meaning 'is going' pairs naturally with the noun for 'film director' in everyday conversation."),
    (11, None,
     "'Drink a large glass of cool water.' Andrea recommends a quick remedy to stop the spasms. Notice how 'drink' leads directly into the noun meaning 'glass'."),
    (12, None,
     "'I will never be ready on time.' Jose doubts his ability to pull himself together before filming. Notice how 'will be' leads directly into the noun meaning 'time'."),
    (13, None,
     "'You are a wonderful actor, Jose.' Andrea boosts his professional confidence with sincere praise. The descriptive adjective for 'wonderful' agrees in gender and number with its noun."),
]

TRANSITION = "Now let's listen to Andrea and Jose's dialogue once more from start to finish."

OUTRO = ("Andrea fights to calm Jose's sudden panic and hiccups before the cameras roll. "
         "Let's review the key vocabulary of emotion, memory, and performance in this scene.")

CLOSING = ("lea", "Il faut vite retrouver son calme.")
