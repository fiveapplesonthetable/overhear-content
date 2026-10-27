ID = "dix-pour-cent-s01e03-scene-24"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 3
SCENE = 24
TITLE = "Une balle dans le pied  (Shooting Yourself in the Foot)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Solveig", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E03"
SOURCE_FILE = "sources/dix-pour-cent/s01/e03.fr.dual.srt"

INTRO = ("After learning that Solveig Akerfelt rejected Nathalie Baye, Andréa told Gabriel he made Laura Smet act "
         "like a diva for nothing: without her mother in the film, Laura could have played the role! Now Gabriel "
         "calls Solveig on the phone for a desperate piece of agent magic. Somehow, he has to convince the serious "
         "Scandinavian director that Laura's terrible behaviour at the audition was actually a sign of passion. "
         "Let's listen to the call in French first; don't worry if you don't catch every word.")

STORY = [
 ("lea", "Solveig à l'appareil.", "Solveig speaking.",
  [(598, "Solveig à l'appareil")], ""),
 ("gabriel", "Allô, Solveig? C'est Gabriel Sarda, l'agent de Laura Smet.",
  "Hello, Solveig? It's Gabriel Sarda, Laura Smet's agent.",
  [(599, "Allô, Solveig"), (600, "C'est Gabriel Sarda, l'agent de Laura Smet")], ""),
 ("lea", "Elle m'a donné envie de tout arrêter.", "She made me want to stop everything.",
  [(603, "Elle m'a donné envie de tout arrêter")], ""),
 ("gabriel", "C'était ma faute. Elle s'est tiré une balle dans le pied.",
  "It was my fault. She shot herself in the foot.",
  [(604, "C'était ma faute"), (606, "Elle s'est tiré une balle dans le pied")], ""),
 ("lea", "Une balle dans le pied?", "A bullet in the foot?",
  [(606, "une balle dans le pied")], "swearing in 606 dropped"),
 ("gabriel", "Oui, c'est une expression française, et une tradition chez les comédiens.",
  "Yes, it's a French expression, and a tradition among actors.",
  [(607, "Oui, c'est une expression française"), (608, "et une tradition chez les comédiens")], ""),
 ("gabriel", "Quand ils veulent un rôle, ils se comportent mal.",
  "When they want a part, they behave badly.",
  [(609, "Quand ils veulent un rôle, ils se comportent mal")], ""),
 ("gabriel", "Les Français sont de vrais romantiques. C'est une façon bizarre de faire.",
  "The French are true romantics. It's a strange way of doing things.",
  [(612, "les Français"), (612, "de vrais romantiques"), (614, "c'est une façon bizarre de faire")],
  "'Vous savez ce que sont' and 'Je sais que' simplified to A1"),
 ("gabriel", "Mais ils font tous comme ça.", "But they all do it like that.",
  [(615, "Ils font tous comme ça")], ""),
 ("gabriel", "Jean Dujardin, par exemple. Aux essais, il parlait, il parlait!",
  "Jean Dujardin, for example. At the screen tests, he talked and talked!",
  [(616, "Jean Dujardin, par exemple"), (617, "Aux essais, il parlait, il parlait")], ""),
 ("gabriel", "Et c'était pour un film muet! Complètement fou, non?",
  "And it was for a silent film! Completely crazy, right?",
  [(619, "et c'était pour un film muet ! Complètement fou, non")], ""),
 ("lea", "Un test!", "A test!",
  [(621, "Un test")], ""),
 ("gabriel", "Oui! Vous la voulez vraiment pour le rôle? Voilà la question.",
  "Yes! Do you really want her for the part? That's the question.",
  [(624, "Vous la voulez vraiment pour le rôle"), (624, "Voilà la question")], "guillemets removed"),
 ("gabriel", "Donnez-lui une autre chance. Solveig, je vous en supplie.",
  "Give her another chance. Solveig, I beg you.",
  [(625, "Donnez-lui une autre chance"), (626, "Solveig, je vous en supplie")], ""),
 ("lea", "D'accord.", "Okay.",
  [(627, "D'accord")], ""),
 ("gabriel", "Akerfelt veut revoir Laura Smet!", "Akerfelt wants to see Laura Smet again!",
  [(631, "Akerfelt veut revoir Laura Smet")], "Gabriel announces the news at the agency"),
 ("gabriel", "Elle veut voir Laura et Nathalie ensemble avant de prendre son avion.",
  "She wants to see Laura and Nathalie together before catching her flight.",
  [(636, "Elle veut voir Laura et Nathalie ensemble avant de prendre son avion")],
  "Hervé's line given to Gabriel (2-role limit)"),
 ("gabriel", "Les affaires reprennent!", "Business is picking up again!",
  [(639, "Les affaires reprennent")], "Mathias's line given to Gabriel (2-role limit)"),
]

OPENER = ("Let's go through it line by line. Solveig answers the phone in the standard formal way.")

WALK = [
 (0, None,
  "'Solveig speaking.' Literally 'Solveig at the device'. That's the classic French phrase when you answer the phone."),
 (1, None,
  "'Hello, Solveig? It's Gabriel Sarda, Laura Smet's agent.' On the phone, French uses 'it is' rather than 'I am' to introduce yourself."),
 (2, None,
  "'She made me want to stop everything.' Literally 'she gave me the desire to stop everything'. Solveig hated Laura's diva act."),
 (3, "C'était ma faute.",
  "'It was my fault.' Gabriel takes the blame to get Solveig listening."),
 (3, "Elle s'est tiré une balle dans le pied.",
  "'She shot herself in the foot.' Literally 'she fired a bullet into her foot'. Just like the English idiom."),
 (4, None,
  "'A bullet in the foot?' Solveig is Scandinavian, so the French idiom catches her completely by surprise."),
 (5, None,
  "'Yes, it's a French expression, and a tradition among actors.' Notice the preposition before 'actors', which means 'among' or 'at the home of'. Gabriel is inventing this tradition on the spot."),
 (6, None,
  "'When they want a part, they behave badly.' A reflexive verb at the end, 'they behave themselves badly'."),
 (7, "Les Français sont de vrais romantiques.",
  "'The French are true romantics.' Gabriel plays on every stereotype he can think of."),
 (7, "C'est une façon bizarre de faire.",
  "'It's a strange way of doing things.' Literally 'a strange way to do'."),
 (8, None,
  "'But they all do it like that.' The word for 'all' comes right after the verb 'do'."),
 (9, None,
  "'Jean Dujardin, for example. At the screen tests, he talked and talked!' The verb is in the past tense used for ongoing actions: 'he was talking, he was talking'."),
 (10, None,
  "'And it was for a silent film! Completely crazy, right?' Notice how 'silent film' puts the adjective after the noun, and 'right?' at the end is simply the word for 'no?'."),
 (11, None,
  "'A test!' Solveig is starting to buy the story."),
 (12, None,
  "'Yes! Do you really want her for the part? That's the question.' Notice the little word for 'her' placed right before 'want'."),
 (13, None,
  "'Give her another chance. Solveig, I beg you.' A polite command with 'to her' attached by a hyphen."),
 (14, None,
  "'Okay.' It worked! Solveig agrees."),
 (15, None,
  "'Akerfelt wants to see Laura Smet again!' Gabriel comes out of his office, proud of himself. Then Hervé runs up with an even bigger surprise from the director."),
 (16, None,
  "'She wants to see Laura and Nathalie together before catching her flight.' Solveig liked the idea of actors shooting themselves in the foot so much that now she wants both mother and daughter back!"),
 (17, None,
  "'Business is picking up again!' Literally 'business starts again'. Everything is back on track—or so the agents think."),
]

TRANSITION = "Let's listen to the whole scene again without stopping."

OUTRO = ("Gabriel's outrageous story about French actors shooting themselves in the foot worked a little too well: "
         "now Solveig Akerfelt wants to see both Nathalie Baye and Laura Smet together in the same room. "
         "See you next time.")
CLOSING = ("gabriel", "À tout à l'heure!")
