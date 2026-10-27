# Authoring module for dix-pour-cent s02e06 scene 22 (cues 599-621).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-22.py --out out/dix-pour-cent/s02e06/scene-22.json

ID = "dix-pour-cent-s02e06-scene-22"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 22
TITLE = "Perdus dans les couloirs  (Lost in the Corridors)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "juliette": "emilie", "hicham": "theo"}
LABELS = {"lea": "Andréa", "juliette": "Juliette", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 599-621. Andrea, Juliette Binoche, and Hicham get lost in the backstage service corridors "
               "of the Palais des Festivals while searching for a restroom just minutes before the ceremony. "
               "Adapted for A1 French.")

INTRO = ("Lost behind the scenes of the Palais des Festivals, Andrea, Juliette Binoche, and Hicham rush frantically through service hallways. "
         "Time is running out before the opening ceremony as panic escalates. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Par ici, dépêchons-nous un peu!",
  "This way, let us hurry up a bit!",
  [(604, "Par ici.")], "Andrea hurries the group along"),
 ("juliette", "Je dois monter sur scène bientôt.",
  "I have to go on stage soon.",
  [(600, "Tu montes")], "Juliette notes the pressing deadline"),
 ("juliette", "C'est un véritable cauchemar!",
  "It is a true nightmare!",
  [(603, "un cauchemar")], "Juliette laments the confusion"),
 ("hicham", "Où mènent tous ces longs couloirs?",
  "Where do all these long corridors lead?",
  [(614, "Un couloir")], "Hicham wonders about the hallway maze"),
 ("lea", "Il y a des toilettes par là.",
  "There are bathrooms over there.",
  [(604, "Il y a des toilettes par là.")], "Andrea thinks she sees restrooms"),
 ("juliette", "Fais attention à ma robe!",
  "Be careful with my dress!",
  [(605, "fais attention.")], "Juliette watches her gown"),
 ("hicham", "Regardez, cette porte est fermée!",
  "Look, this door is locked!",
  [(615, "portes")], "Hicham finds a closed door"),
 ("lea", "Ce n'est pas possible, nous tournons!",
  "It is not possible, we are turning!",
  [(611, "C'est pas possible !")], "Andrea realizes they are circling"),
 ("juliette", "Je ne vois que des portes.",
  "I only see doors.",
  [(615, "portes marron.")], "Juliette sees endless identical doors"),
 ("hicham", "On est complètement perdus ici!",
  "We are completely lost here!",
  [(613, "On est perdus !")], "Hicham acknowledges they are lost"),
 ("lea", "Prenons ce couloir par ici.",
  "Let us take this corridor this way.",
  [(606, "Par ici.")], "Andrea points toward another passage"),
 ("juliette", "Attention, ma belle robe se déchire!",
  "Watch out, my beautiful dress is tearing!",
  [(617, "Non !")], "Juliette feels her dress rip"),
 ("lea", "Oh non, un accroc en bas!",
  "Oh no, a tear at the bottom!",
  [(607, "c'est pas ça !")], "Andrea notices the damage to the gown"),
 ("juliette", "La cérémonie va bientôt commencer!",
  "The ceremony will begin soon!",
  [(600, "Tu montes")], "Juliette panics as showtime approaches"),
]

OPENER = "Let's examine how Andrea, Juliette, and Hicham navigate the backstage maze step by step."

WALK = [
 (0, None,
  "'This way, let us hurry up a bit!' Andrea urges everyone to move quickly through the building."),
 (1, None,
  "'I have to go on stage soon.' Juliette reminds them that the clock is ticking down."),
 (2, None,
  "'It is a true nightmare!' Juliette laments their chaotic predicament."),
 (3, None,
  "'Where do all these long corridors lead?' Hicham asks as they wander through unfamiliar hallways."),
 (4, None,
  "'There are bathrooms over there.' Andrea thinks she has found the right direction."),
 (5, None,
  "'Be careful with my dress!' Juliette warns them to mind her delicate designer outfit."),
 (6, None,
  "'Look, this door is locked!' Hicham points out that their path is blocked."),
 (7, None,
  "'It is not possible, we are turning!' Andrea realizes they are running in circles."),
 (8, None,
  "'I only see doors.' Juliette despairs at the maze of unmarked doors."),
 (9, None,
  "'We are completely lost here!' Hicham states the obvious truth about their situation."),
 (10, None,
  "'Let us take this corridor this way.' Andrea tries another turn to escape the maze."),
 (11, None,
  "'Watch out, my beautiful dress is tearing!' Juliette gasps as her garment snags on an obstacle."),
 (12, None,
  "'Oh no, a tear at the bottom!' Andrea spots the damage to the gown with dismay."),
 (13, None,
  "'The ceremony will begin soon!' Juliette worries that she must go on stage in damaged clothes."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("A frantic search for a restroom turns into a backstage labyrinth as Juliette's dress suffers unexpected damage moments before the show. "
         "Let's review the key expressions and vocabulary from this scene.")

CLOSING = ("juliette", "La cérémonie va bientôt commencer!")
