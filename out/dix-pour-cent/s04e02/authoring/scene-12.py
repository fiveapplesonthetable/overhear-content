# Authoring module for dix-pour-cent s04e02 scene 12 (cues 677-700).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e02/authoring/scene-12.py --out overhear-content/out/dix-pour-cent/s04e02/scene-12.json

ID = "dix-pour-cent-s04e02-scene-12"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 12
TITLE = "Coincée à Bergues  (Stuck in Bergues)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 677-700. After a hearty meal in Bergues, Andrea calls Colette "
               "to confess she cannot make their dinner date in Paris.")

INTRO = ("After enduring a colossal homemade feast with Dany Boon's mother, Andrea steps into the quiet street to call Colette. "
         "Expected home in Paris for date night, Andrea must break the difficult news of her whereabouts. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Ce repas du nord était délicieux!",
  "This northern meal was delicious!",
  [(677, "Ça ne vous plaît pas")], "Complimenting meal"),
 ("colette", "Allô Andréa, la baby-sitter est là.",
  "Hello Andrea, the babysitter is here.",
  [(689, "La baby-sitter est là")], "Announcing sitter"),
 ("lea", "Bonsoir mon amour, comment vas-tu?",
  "Good evening my love, how are you?",
  [(687, "Au revoir")], "Greeting warmly"),
 ("colette", "On se retrouve bientôt au restaurant?",
  "Are we meeting soon at the restaurant?",
  [(690, "au restaurant")], "Asking dinner"),
 ("lea", "Le restaurant, ça va être compliqué.",
  "The restaurant, that will be complicated.",
  [(691, "ça va être compliqué")], "Breaking news"),
 ("colette", "Tu es encore coincée au bureau?",
  "Are you still stuck at the office?",
  [(691, "ça va être compliqué")], "Suspecting work"),
 ("lea", "Non, pas cette fois-ci, justement.",
  "No, not this time, actually.",
  [(694, "Tu es où")], "Clarifying situation"),
 ("colette", "Mais où es-tu en ce moment?",
  "Where are you right now?",
  [(694, "Tu es où")], "Demanding location"),
 ("lea", "Je suis actuellement à Bergues.",
  "I am currently in Bergues.",
  [(695, "Bergues")], "Revealing town"),
 ("colette", "Bergues? C'est quelle ligne de métro?",
  "Bergues? Which metro line is that?",
  [(695, "Bergues")], "Confusing geography"),
 ("lea", "C'est loin, dans les Hauts-de-France!",
  "It is far, in Hauts-de-France!",
  [(697, "dans les Hauts-de-France")], "Explaining province"),
 ("colette", "Tu plaisantes? J'en peux plus!",
  "Are you joking? I can't take it!",
  [(699, "j'en peux plus")], "Exploding in anger"),
 ("lea", "Je devais sauver un gros contrat.",
  "I had to save a major contract.",
  [(699, "j'en peux plus")], "Defending trip"),
 ("colette", "Rentre à Paris le plus vite!",
  "Return to Paris as fast as possible!",
  [(687, "Au revoir")], "Demanding return"),
]

WALK = [
 (0, None,
  "'This northern meal was delicious!' Andrea appreciates the hearty hospitality. "
  "The adjective 'delicieux' describes wonderful food."),
 (1, None,
  "'Hello Andrea, the babysitter is here.' Colette calls to coordinate the evening. "
  "The interjection 'allo' is used specifically when answering the phone."),
 (2, None,
  "'Good evening my love, how are you?' Andrea tries to soothe her partner gently. "
  "The affectionate phrase 'mon amour' shows tenderness."),
 (3, None,
  "'Are we meeting soon at the restaurant?' Colette anticipates their date night. "
  "The reflexive verb 'se retrouver' means to meet up."),
 (4, None,
  "'The restaurant, that will be complicated.' Andrea delivers the disappointing news. "
  "The adjective 'complique' indicates difficulties."),
 (5, None,
  "'Are you still stuck at the office?' Colette assumes standard agency delays. "
  "The past participle 'coincee' functions here as an adjective."),
 (6, None,
  "'No, not this time, actually.' Andrea prepares to reveal the surprise. "
  "The adverb 'justement' means precisely or actually."),
 (7, None,
  "'Where are you right now?' Colette asks with mounting suspicion. "
  "The phrase 'en ce moment' means right now."),
 (8, None,
  "'I am currently in Bergues.' Andrea confesses her unexpected location. "
  "The adverb 'actuellement' means currently in modern French."),
 (9, None,
  "'Bergues? Which metro line is that?' Colette mistakes the distant town for a Parisian station. "
  "The noun 'metro' designates the Paris subway network."),
 (10, None,
  "'It is far, in Hauts-de-France!' Andrea clarifies the geography. "
  "The regional name 'Hauts-de-France' refers to northern France."),
 (11, None,
  "'Are you joking? I can't take it!' Colette vents her frustration at the broken promise. "
  "The idiom 'en avoir marre' or 'n'en pouvoir plus' expresses exhaustion."),
 (12, None,
  "'I had to save a major contract.' Andrea justifies the emergency business trip. "
  "The verb 'sauver' means to save or rescue."),
 (13, None,
  "'Return to Paris as fast as possible!' Colette demands her immediate return home. "
  "The adverbial locution 'le plus vite' means as quickly as possible."),
]

OUTRO = ("Andrea faces Colette's frustration over her sudden trip to northern France. "
         "The constant demands of the agency continue to put pressure on her personal life. "
         "Now, let's review the scene one last time.")

CLOSING = ("colette", "Rentre à Paris le plus vite!")
