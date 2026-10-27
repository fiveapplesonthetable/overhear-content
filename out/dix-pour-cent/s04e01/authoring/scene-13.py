# Authoring module for dix-pour-cent s04e01 scene 13 (cues 661-670).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e01/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s04e01/scene-13.json

ID = "dix-pour-cent-s04e01-scene-13"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 13
TITLE = "Les pleurs de décharge  (Release Crying)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 661-670. In their apartment, Colette and Andréa discuss "
               "baby Flora's crying habits.")

INTRO = ("In the quiet living room, Colette notices that baby Flora immediately stops crying when held. "
         "Andrea explains the pediatric concept of release crying, leading to a thoughtful exchange between the exhausted mothers. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("colette", "Tu as vu ça, Andréa?",
  "Did you see that, Andrea?",
  [(661, "Tu as vu ça")], "Noting miracle"),
 ("lea", "Elle arrête de pleurer dans tes bras.",
  "She stops crying in your arms.",
  [(662, "Elle arrête de pleurer")], "Observing child"),
 ("colette", "Elle a besoin de notre présence.",
  "She needs our presence.",
  [(663, "en sécurité")], "Reflecting on care"),
 ("lea", "Ce sont des pleurs de décharge.",
  "These are release crying episodes.",
  [(664, "Les pleurs de décharge")], "Explaining concept"),
 ("colette", "Qu'est-ce que cela veut dire?",
  "What does that mean?",
  [(664, "Les pleurs de décharge")], "Asking explanation"),
 ("lea", "Le bébé évacue tout son stress.",
  "The baby releases all its stress.",
  [(665, "se sentir en sécurité")], "Clarifying mechanism"),
 ("colette", "C'est donc un très bon signe?",
  "Is that a very good sign?",
  [(666, "Bien au contraire")], "Seeking confirmation"),
 ("lea", "Bien au contraire, c'est de l'angoisse.",
  "Quite the opposite, it is anxiety.",
  [(666, "Bien au contraire")], "Correcting assumption"),
 ("colette", "Où as-tu appris toutes ces théories?",
  "Where did you learn all these theories?",
  [(667, "sur ton bureau")], "Inquiring about source"),
 ("lea", "Le livre est sur ton bureau.",
  "The book is on your desk.",
  [(667, "sur ton bureau")], "Indicating guide"),
 ("colette", "Oui, il est super ce livre!",
  "Yes, it is great, this book!",
  [(668, "Il est super")], "Acknowledging guide"),
 ("lea", "Il faut le lire très attentivement.",
  "One must read it very attentively.",
  [(668, "Il est super")], "Advising diligence"),
 ("colette", "Je vais me coucher maintenant.",
  "I am going to bed now.",
  [(669, "Je vais me coucher")], "Heading to sleep"),
 ("lea", "Bonne nuit, dors bien cette nuit.",
  "Good night, sleep well tonight.",
  [(669, "Je vais me coucher")], "Wishing good night"),
]

WALK = [
 (0, None,
  "'Did you see that, Andrea?' Colette points out the sudden change in Flora's behavior. "
  "The passe compose 'as vu' indicates an immediate observation."),
 (1, None,
  "'She stops crying in your arms.' Andrea confirms the soothing effect of physical contact. "
  "The verb 'arreter de' is followed by an infinitive."),
 (2, None,
  "'She needs our presence.' Colette emphasizes parental comfort. "
  "The verbal idiom 'avoir besoin de' expresses a necessity."),
 (3, None,
  "'These are release crying episodes.' Andrea introduces a pediatric concept. "
  "The noun 'decharge' refers to emotional release."),
 (4, None,
  "'What does that mean?' Colette asks for clarification. "
  "The idiom 'vouloir dire' signifies to mean."),
 (5, None,
  "'The baby releases all its stress.' Andrea explains the physiological process. "
  "The verb 'evacuer' means to discharge or release."),
 (6, None,
  "'Is that a very good sign?' Colette wonders if it indicates healthy development. "
  "The adverb 'donc' introduces a logical conclusion."),
 (7, None,
  "'Quite the opposite, it is anxiety.' Andrea corrects the misunderstanding. "
  "The locution 'bien au contraire' means quite the reverse."),
 (8, None,
  "'Where did you learn all these theories?' Colette asks about the source of knowledge. "
  "The interrogative adverb 'ou' asks about location or origin."),
 (9, None,
  "'The book is on your desk.' Andrea mentions the parenting guide. "
  "The preposition 'sur' indicates physical placement upon a surface."),
 (10, None,
  "'Yes, it is great, this book!' Colette confirms having seen the volume. "
  "The informal adjective 'super' means fantastic or great."),
 (11, None,
  "'One must read it very attentively.' Andrea encourages careful study. "
  "The impersonal expression 'il faut' indicates necessity."),
 (12, None,
  "'I am going to bed now.' Colette heads to the bedroom to rest. "
  "The reflexive verb 'se coucher' means to go to sleep."),
 (13, None,
  "'Good night, sleep well tonight.' Andrea offers loving parting wishes. "
  "The imperative 'dors' wishes restful sleep."),
]

OUTRO = ("Andrea and Colette navigate the emotional intricacies of new parenthood together. "
         "Sharing moments of guidance and tenderness strengthens their partnership despite the exhaustion. "
         "Now, let's review the scene one last time.")

CLOSING = ("lea", "Bonne nuit, dors bien cette nuit.")
