ID = "dix-pour-cent-s04e05-scene-13"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 13
TITLE = "La virée en ville  (The Night Out)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "arlette": "emilie"}
LABELS = {"lea": "Sigourney", "arlette": "Arlette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"

INTRO = "Sigourney Weaver and Arlette realize that Bernard will not be joining them for their highly anticipated night out. Let's listen to their conversation."

STORY = [
    ("lea", "Bernard est parti?", "Did Bernard leave?", [(633, "Bernard est parti")], ""),
    ("arlette", "Oui, je crois.", "Yes, I think so.", [], "Padding for short scene"),
    ("lea", "Zut alors!", "Darn it!", [(634, "Zut alors")], ""),
    ("arlette", "Il est déjà tard.", "It is already late.", [], "Padding"),
    ("lea", "Arlette, il ne sera pas là.", "Arlette, he won't be there.", [(635, "Arlette, il ne sera pas là")], ""),
    ("lea", "Pour notre virée en ville.", "For our night out.", [(635, "pour notre virée en ville")], ""),
    ("arlette", "Ce n'est pas grave.", "It does not matter.", [], "Padding"),
    ("arlette", "On va s'amuser.", "We will have fun.", [], "Padding"),
    ("lea", "Bien sûr, mon amie.", "Of course, my friend.", [], "Padding"),
    ("arlette", "On y va?", "Shall we go?", [], "Padding"),
    ("lea", "Oui, on y va.", "Yes, let's go.", [], "Padding"),
    ("arlette", "Paris nous attend.", "Paris is waiting for us.", [], "Padding")
]

WALK = [
    (0, "Bernard est parti?", "'Did Bernard leave?' Sigourney asks, looking around for him."),
    (1, "Oui, je crois.", "'Yes, I think so.' Arlette replies calmly."),
    (2, "Zut alors!", "'Darn it!' Sigourney exclaims in frustration."),
    (3, "Il est déjà tard.", "'It is already late.' Arlette points out."),
    (4, "Arlette, il ne sera pas là.", "'Arlette, he won't be there.' Sigourney realizes with disappointment."),
    (5, "Pour notre virée en ville.", "'For our night out.' Sigourney refers to their planned evening."),
    (6, "Ce n'est pas grave.", "'It does not matter.' Arlette reassures her gently."),
    (7, "On va s'amuser.", "'We will have fun.' Arlette promises an exciting evening."),
    (8, "Bien sûr, mon amie.", "'Of course, my friend.' Sigourney agrees with a smile."),
    (9, "On y va?", "'Shall we go?' Arlette asks, ready to depart."),
    (10, "Oui, on y va.", "'Yes, let's go.' Sigourney confirms with enthusiasm."),
    (11, "Paris nous attend.", "'Paris is waiting for us.' Arlette concludes joyfully.")
]
OPENER = "Let's walk through it."
TRANSITION = "Now let's hear the whole thing."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around the night out, and for the words meaning 'left' and 'think'. You'll catch them now. See you next time."
CLOSING = ("lea", "Au revoir.")
