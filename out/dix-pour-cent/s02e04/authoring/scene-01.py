# Authoring module for dix-pour-cent s02e04 scene 01 (cues 1-21).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-01.py --out out/dix-pour-cent/s02e04/scene-01.json

ID = "dix-pour-cent-s02e04-scene-01"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 1
TITLE = "Arlette regarde une série  (Game of Thrones)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Arlette", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-21. Arlette enthusiastically describes a TV series to Mathias, "
               "who reminds her of serious agency business. Adapted for A1 French.")

INTRO = ("At the ASK agency, senior agent Arlette Azemar is engrossed in watching television episodes on her computer. "
         "When Mathias walks in, she passionately recounts plot twists from Game of Thrones and asks for his help, "
         "while Mathias tries to focus on serious agency business. Let's listen to the scene in French first.")

STORY = [
 ("lea", "Cette actrice est tellement magnétique et élégante.",
  "That actress is so magnetic and elegant.",
  [(2, "Elle est tellement... magnétique."), (3, "Tellement élégante.")], "Combined short descriptive reactions"),
 ("lea", "Elle est vraiment poétique aussi.",
  "She is truly poetic as well.",
  [(4, "Poétique aussi.")], "Added full subject and verb"),
 ("lea", "Ensuite, la petite femme devient aveugle.",
  "Then, the small woman becomes blind.",
  [(5, "Ensuite la petite femme devient aveugle.")], "Kept exact plot description"),
 ("lea", "Et la grande fille stupide meurt!",
  "And the stupid tall girl dies!",
  [(6, "La grande fille stupide"), (7, "meurt...")], "Combined subject and verb"),
 ("mathias", "Arlette, tu regardes encore cette série?",
  "Arlette, are you still watching this series?",
  [(13, "-Oui.")], "Added context question"),
 ("lea", "Oui, la fin m'énerve beaucoup.",
  "Yes, the ending annoys me a lot.",
  [(12, "Ça m'énerve.")], "Added specific reference to ending"),
 ("lea", "Peux-tu trouver la prochaine saison?",
  "Can you find the next season?",
  [(13, "Alors tu peux trouver"), (14, "la prochaine saison pour moi ?")], "Simplified request"),
 ("lea", "Un an, c'est trop long d'attendre.",
  "One year is too long to wait.",
  [(15, "Un an, c'est long à attendre.")], "Added intensity with trop"),
 ("mathias", "C'est quoi le titre déjà?",
  "What is the title again?",
  [(16, "Bien sûr. C'est quoi le titre déjà ?")], "Kept exact question"),
 ("lea", "Tu vis dans une grotte, Mathias?",
  "Do you live in a cave, Mathias?",
  [(18, "Tu vis dans une grotte, Mathias ?")], "Kept cultural idiom"),
 ("lea", "C'est la célèbre série Game of Thrones.",
  "It is the famous series Game of Thrones.",
  [(17, "Game of Thrones.")], "Expanded title with description"),
 ("mathias", "Je verrai Louis Garrel au théâtre jeudi.",
  "I will see Louis Garrel at the theater Thursday.",
  [(19, "Je verrai Louis Garrel au théâtre, jeudi.")], "Kept professional schedule"),
 ("mathias", "Dis à Berléand que ses contrats sont prêts.",
  "Tell Berleand that his contracts are ready.",
  [(20, "Dis à Berléand que les contrats sont prêts.")], "Kept agency instruction"),
 ("mathias", "Au fait, ton haut sent la friture.",
  "By the way, your top smells like frying.",
  [(21, "Au fait, ton haut sent la friture.")], "Kept playful tease"),
]

OPENER = "Let's examine how Arlette shares her passion for television with Mathias."

WALK = [
 (0, None,
  "'That actress is so magnetic and elegant.' Two coordinated descriptive adjectives highlighting screen presence."),
 (1, None,
  "'She is truly poetic as well.' An adverb of degree modifying an aesthetic quality."),
 (2, None,
  "'Then, the small woman becomes blind.' A temporal adverb followed by a state transition verb."),
 (3, None,
  "'And the stupid tall girl dies!' An emotional plot spoiler with an irregular present tense verb."),
 (4, None,
  "'Arlette, are you still watching this series?' A direct question inquiring about a workplace distraction."),
 (5, None,
  "'Yes, the ending annoys me a lot.' A pronominal emotion verb governing an adverb of quantity."),
 (6, None,
  "'Can you find the next season?' An inverted modal question asking for pirated episodes."),
 (7, None,
  "'One year is too long to wait.' An expression of impatience regarding TV release schedules."),
 (8, None,
  "'What is the title again?' A familiar interrogative seeking clarification."),
 (9, None,
  "'Do you live in a cave, Mathias?' A sarcastic cultural idiom teasing his lack of television awareness."),
 (10, None,
  "'It is the famous series Game of Thrones.' A demonstrative statement introducing the global hit series."),
 (11, None,
  "'I will see Louis Garrel at the theater Thursday.' A simple future tense verb outlining his evening schedule."),
 (12, None,
  "'Tell Berleand that his contracts are ready.' An imperative command delivering professional instructions."),
 (13, None,
  "'By the way, your top smells like frying.' An informal critique pointing out a kitchen odor."),
]

TRANSITION = "Now let's listen to Arlette and Mathias's humorous banter again at full speed."

OUTRO = ("Arlette's obsession with fantasy television amuses the office, but Mathias remains strictly focused on client contracts. "
         "Their teasing dynamic highlights the lighthearted atmosphere at ASK before new challenges arrive.")

CLOSING = ("lea", "Merci pour ton aide, Mathias.")
