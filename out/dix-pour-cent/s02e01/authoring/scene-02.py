# Authoring module for dix-pour-cent s02e01 scene 02 (cues 27-63).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-02.py --out out/dix-pour-cent/s02e01/scene-02.json

ID = "dix-pour-cent-s02e01-scene-02"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 2
TITLE = "L'appel nocturne de Virginie  (Virginie's Night Call)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Virginie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 27-63. Mathias's late-night meditation is interrupted by a frantic call from Virginie, "
               "who reveals she was photographed kissing another man. "
               "Adapted for A1 French.")

INTRO = ("At home late at night, agent Mathias Barneville tries to relax with a guided meditation session. "
         "Suddenly his phone rings. It is his star client Virginie Efira in a state of absolute panic after a night out. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("mathias", "Allô? Virginie, que s'est-il passé?",
  "Hello? Virginie, what happened?",
  [(31, "Allô ?"), (33, "Que s'est-il passé ?")], ""),
 ("lea", "Mathias, c'est terrible!",
  "Mathias, it is terrible!",
  [(32, "Mathias, c'est terrible.")], ""),
 ("lea", "J'étais dans la rue avec un ami.",
  "I was in the street with a friend.",
  [(34, "J'étais dans la rue, avec un ami.")], ""),
 ("mathias", "Un ami? Tu étais avec Ramzy?",
  "A friend? Were you with Ramzy?",
  [(37, "Un ami ? Tu étais avec Ramzy ?")], ""),
 ("lea", "Non, Ramzy est rentré chez lui.",
  "No, Ramzy went home.",
  [(38, "Non, il est rentré chez lui.")], "Replaced pronoun 'il' with 'Ramzy' for clarity"),
 ("lea", "J'ai vu un flash dans la nuit.",
  "I saw a flash in the night.",
  [(36, "il y a eu un flash")], "Adapted to first-person view"),
 ("mathias", "Vous avez été pris en photo par un paparazzi?",
  "Were you photographed by a paparazzo?",
  [(45, "vous avez été pris en photo par un paparazzi ?")], ""),
 ("lea", "Il faut que tu fasses quelque chose!",
  "You have to do something!",
  [(47, "il faut que tu fasses quelque chose")], ""),
 ("lea", "Appelle les magazines, ils ne doivent pas publier!",
  "Call the magazines, they must not publish!",
  [(48, "Appelle les magazines people"), (49, "ils ne doivent pas le publier !")], ""),
 ("mathias", "Mes menaces ne vont pas les arrêter.",
  "My threats are not going to stop them.",
  [(50, "Mes menaces ne les"), (51, "arrêter.")], "Adapted modal structure"),
 ("lea", "Alors qu'est-ce que je fais?",
  "So what do I do?",
  [(52, "Alors qu'est-ce que je fais ?")], ""),
 ("mathias", "Parle à Ramzy immédiatement.",
  "Talk to Ramzy immediately.",
  [(53, "Parle à Ramzy.")], "Added adverb 'immédiatement'"),
 ("lea", "Non, je ne peux pas, il ne comprendra pas.",
  "No, I cannot, he will not understand.",
  [(54, "Non, je ne peux pas, il ne comprendra pas.")], ""),
 ("mathias", "Virginie, crois-moi, c'est la meilleure chose à faire.",
  "Virginie, believe me, it is the best thing to do.",
  [(55, "Crois-moi"), (56, "c'est la meilleure chose à faire.")], ""),
]

OPENER = "Let's examine how Mathias handles a sudden emergency call from his actress."

WALK = [
 (0, None,
  "'Hello? Virginie, what happened?' The classic telephone greeting followed by a formal inverted past question."),
 (1, None,
  "'Mathias, it is terrible!' A demonstrative pronoun followed by an expressive emotional adjective."),
 (2, None,
  "'I was in the street with a friend.' An imperfect tense verb setting the scene with a preposition of company."),
 (3, None,
  "'A friend? Were you with Ramzy?' Mathias asks a pointed question using the imperfect tense."),
 (4, None,
  "'No, Ramzy went home.' A compound past verb constructed with the auxiliary to be for movement."),
 (5, None,
  "'I saw a flash in the night.' A direct perception in the compound past with a temporal noun phrase."),
 (6, None,
  "'Were you photographed by a paparazzo?' A passive voice construction expressing an unwanted media intrusion."),
 (7, None,
  "'You have to do something!' The impersonal expression of obligation governing a present subjunctive verb."),
 (8, None,
  "'Call the magazines, they must not publish!' An imperative followed by a modal verb expressing strong prohibition."),
 (9, None,
  "'My threats are not going to stop them.' The near-future tense with a plural subject noun."),
 (10, None,
  "'So what do I do?' A conversational connector followed by an interrogative locution."),
 (11, None,
  "'Talk to Ramzy immediately.' An imperative verb form addressing someone with the informal pronoun."),
 (12, None,
  "'No, I cannot, he will not understand.' A modal verb in the present tense followed by a simple future verb."),
 (13, None,
  "'Virginie, believe me, it is the best thing to do.' An imperative followed by a superlative adjective phrase."),
]

TRANSITION = "Now let's listen to the late-night phone call again at full speed."

OUTRO = ("Virginie is terrified of losing both her partner and her career over the scandal. "
         "Mathias urges honesty, but in the morning the press will already have the story.")

CLOSING = ("mathias", "Parle-lui.")
