ID = "dix-pour-cent-s01e05-scene-23"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 23
TITLE = "La scène de Sofia est coupée  (Sofia's Scene Is Cut)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "andrea": "emilie", "assistant": "theo"}
LABELS = {"lea": "Sofia", "andrea": "Andréa", "assistant": "L'assistant"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"

INTRO = ("After Andréa stormed out of Gabriel's car in the middle of the countryside, a friendly farmer named Loïc gave her a lift to the chateau on his tractor. "
         "Meanwhile, back in Paris, Camille's online petition to save Jonathan's character passed ten thousand signatures overnight and won Mathias's praise. "
         "Now at the chateau courtyard, Sofia is in costume waiting to shoot her big scene opposite JoeyStarr when the assistant director gathers the cast and crew. "
         "Listen to the scene in French first. Don't worry about catching every word.")

STORY = [
 ("andrea", "Merci, Loïc!", "Thank you, Loïc!",
  [(489, "Merci, Loïc")], "Andréa steps off the tractor"),
 ("assistant", "Votre attention, s'il vous plaît!", "Your attention, please!",
  [(490, "Votre attention, s'il vous plaît")], ""),
 ("assistant", "Tout le monde en place pour cet après-midi.", "Everyone in place for this afternoon.",
  [(491, "Tout le monde en place"), (492, "Cet après-midi")], ""),
 ("assistant", "La scène soixante est coupée.", "Scene sixty is cut.",
  [(494, "La scène"), (494, "coupée")], "'60' written out as 'soixante'"),
 ("lea", "Coupée?", "Cut?",
  [(495, "Coupée")], ""),
 ("assistant", "On veut les esclaves derrière le château, d'accord?", "We want the slaves behind the chateau, okay?",
  [(496, "On veut"), (496, "les esclaves"), (497, "derrière le château"), (497, "d'accord")], "simplified from 496-497"),
 ("lea", "Excusez-moi! Ma scène est coupée?", "Excuse me! My scene is cut?",
  [(498, "Excusez-moi"), (498, "scène"), (498, "coupée")], "simplified from 498"),
 ("assistant", "Oui, elle n'est pas utile.", "Yes, it isn't needed.",
  [(499, "Elle")], "'Elle n'apporte rien' -> 'Oui, elle n'est pas utile'"),
 ("lea", "Pourquoi? On ne peut pas couper une scène comme ça!", "Why? You can't cut a scene like that!",
  [(500, "Pourquoi"), (501, "On ne peut pas couper une scène comme ça")], ""),
 ("assistant", "On a déjà assez de problèmes aujourd'hui.", "We already have enough problems today.",
  [(502, "On a déjà assez de problèmes")], ""),
 ("lea", "C'est à cause de Joey?", "Is it because of Joey?",
  [(503, "C'est à cause de Joey")], ""),
 ("lea", "Il ne voulait pas jouer avec moi?", "He didn't want to act with me?",
  [(504, "Il ne voulait pas jouer avec moi")], ""),
 ("assistant", "Écoutez, j'ai quinze chevaux à préparer.", "Listen, I have fifteen horses to get ready.",
  [(505, "Écoutez"), (506, "J'ai"), (506, "chevaux")], "'15' written out as 'quinze'"),
 ("assistant", "Allez avec les autres, s'il vous plaît. Merci.", "Go with the others, please. Thank you.",
  [(507, "s'il vous plaît"), (507, "les autres"), (508, "Merci")], "simplified from 507"),
 ("lea", "Ce n'est pas juste!", "It's not fair!",
  [], "replaces 509-510 swearing"),
]

OPENER = ("Let's walk through it. Andréa arrives at the chateau gate just as the assistant director makes an announcement in the courtyard.")

WALK = [
 (0, None,
  "'Thank you, Loïc!' Andréa hops down from the farmer's tractor at the entrance to the set."),
 (1, None,
  "'Your attention, please!' In the courtyard, the assistant director calls everyone together."),
 (2, None,
  "'Everyone in place for this afternoon.' The word for 'this' takes a special form ending in a T sound before a masculine word that starts with a vowel."),
 (3, None,
  "'Scene sixty is cut.' Because Julie and JoeyStarr lost so much time arguing, the crew is behind schedule."),
 (4, None,
  "'Cut?' That is Sofia's scene, the one with her two lines opposite JoeyStarr."),
 (5, None,
  "'We want the slaves behind the chateau, okay?' Without her lines, Sofia is just a background extra again."),
 (6, None,
  "'Excuse me! My scene is cut?' Sofia runs up to the assistant director."),
 (7, None,
  "'Yes, it isn't needed.' Literally 'it is not useful'. He brushes her off."),
 (8, None,
  "'Why? You can't cut a scene like that!' Here the little word for 'we' or 'one' means 'you' or 'people'."),
 (9, None,
  "'We already have enough problems today.' After the word for 'enough', French uses the little word for 'of' with no article."),
 (10, None,
  "'Is it because of Joey?' The three-word phrase before his name means 'because of'."),
 (11, None,
  "'He didn't want to act with me?' Sofia remembers how nervous she was earlier when she rehearsed for him, and blames herself."),
 (12, None,
  "'Listen, I have fifteen horses to get ready.' The plural of 'horse' changes its ending from 'al' to 'aux'."),
 (13, None,
  "'Go with the others, please. Thank you.' He hurries away, leaving Sofia alone in the courtyard."),
 (14, None,
  "'It's not fair!' Sofia kicks a stone in frustration, heartbroken that her big moment is gone."),
]

TRANSITION = "Now let's listen to the whole scene again from the top."

OUTRO = ("Poor Sofia loses her speaking lines because the two stars delayed the shoot, and she thinks it's her own fault. "
         "Listen out for the phrase meaning 'because of' when you watch the episode. See you in the next scene.")
CLOSING = ("lea", "Ma scène est coupée?")
