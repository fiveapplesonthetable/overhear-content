# Authoring module for dix-pour-cent s03e01 scene 01 (cues 1-20).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-01.py --out out/dix-pour-cent/s03e01/scene-01.json

ID = "dix-pour-cent-s03e01-scene-01"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 1
TITLE = "Le poste à New York  (The New York Position)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-20. Andréa discusses her legal dispute against UBA with Colette after the agency "
               "withdrew its New York offer, while celebrating their baby ultrasound. Adapted for A1 French.")

INTRO = ("In their Paris apartment, talent agent Andrea Martel discusses her legal battle with partner Colette Brecourt. "
         "American agency UBA withdrew its New York executive offer after learning Andrea is expecting a baby. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("lea", "Mon avocat dit que la situation est compliquée.",
  "My lawyer says the situation is complicated.",
  [(6, "Alors, il dit quoi, ton avocat ?"), (7, "Il dit que ça sent pas bon,")], "Reported lawyer advice"),
 ("colette", "Qu'est-ce que l'agence UBA essaie de prouver?",
  "What is agency UBA trying to prove?",
  [(7, "UBA est en train d'essayer de prouver")], "Inquired about legal dispute"),
 ("lea", "Ils disent que d'autres candidates voulaient le poste.",
  "They say other candidates wanted the position.",
  [(8, "que j'étais pas la seule candidate pour le poste à New York.")], "Explained rival candidate defense"),
 ("colette", "C'est faux, ils mentent complètement!",
  "That is false, they are lying completely!",
  [(2, "Oui, mais vous savez qu'ils mentent.")], "Denounced false claims"),
 ("lea", "Ils refusent une femme enceinte à New York.",
  "They refuse a pregnant woman in New York.",
  [(9, "c'est quand tu leur as dit que t'étais enceinte")], "Stated pregnancy reason"),
 ("colette", "C'est une vraie discrimination à l'embauche.",
  "That is real hiring discrimination.",
  [(11, "alors il n'y a plus de discrimination à l'embauche.")], "Framed discrimination issue"),
 ("lea", "Mais nous allons devoir nous battre en justice.",
  "But we will have to fight in court.",
  [(3, "je veux qu'ils paient pour ce qu'ils ont fait.")], "Declared resolve to litigate"),
 ("colette", "Ne t'inquiète pas, nous allons gagner.",
  "Do not worry, we are going to win.",
  [(13, "On va gagner.")], "Expressed confidence in victory"),
 ("lea", "Tu es vraiment très optimiste, Colette.",
  "You are really very optimistic, Colette.",
  [(14, "Tu sais pourquoi ?")], "Acknowledged supportive optimism"),
 ("colette", "Regarde plutôt cette belle échographie!",
  "Look instead at this lovely ultrasound!",
  [(14, "Regarde."), (16, "Laisse ta main, regarde.")], "Directed focus to ultrasound image"),
 ("lea", "Notre petite fille bouge déjà beaucoup.",
  "Our baby girl is already moving a lot.",
  [(19, "notre fille.")], "Remarked on baby movement"),
 ("colette", "Pose ta main ici sur ton ventre.",
  "Place your hand here on your belly.",
  [(16, "Laisse ta main, regarde.")], "Guided maternal touch"),
 ("lea", "Elle a déjà un fort caractère!",
  "She already has a strong personality!",
  [(18, "elle fait un doigt d'honneur.")], "Admired baby energy"),
 ("colette", "Elle ressemble beaucoup à sa maman.",
  "She looks a lot like her mother.",
  [(19, "notre fille.")], "Affirmed familial resemblance"),
]

OPENER = "Let's explore how Andrea and Colette discuss the legal dispute and celebrate their upcoming baby."

WALK = [
 (0, None,
  "'My lawyer says the situation is complicated.' The verb meaning 'says' pairs naturally with the noun for 'lawyer' in everyday conversation."),
 (1, None,
  "'What is agency UBA trying to prove?' Notice how 'is it' leads directly into the noun meaning 'talent firm'. Notice how 'is it' leads directly into the noun meaning 'talent firm'."),
 (2, None,
  "'They say other candidates wanted the position.' The descriptive adjective for 'other' agrees in gender and number with its noun. The descriptive adjective for 'other' agrees in gender and number with its noun."),
 (3, None,
  "'That is false, they are lying completely!' The descriptive adjective for 'false' agrees in gender and number with its noun. The descriptive adjective for 'false' agrees in gender and number with its noun."),
 (4, None,
  "'They refuse a pregnant woman in New York.' Notice how 'reject' leads directly into the noun meaning 'woman'. Notice how 'reject' leads directly into the noun meaning 'woman'."),
 (5, None,
  "'That is real hiring discrimination.' The adjective meaning 'genuine' takes its feminine form here to match the noun it describes."),
 (6, None,
  "'But we will have to fight in court.' The verb meaning 'are going' pairs naturally with the noun for 'court of law' in everyday conversation."),
 (7, None,
  "'Do not worry, we are going to win.' French forms the near future by pairing the present tense of 'to go' directly with 'win'. French forms the near future by pairing the present tense of 'to go' directly with 'win'."),
 (8, None,
  "'You are really very optimistic, Colette.' A heartfelt personal evaluation acknowledging morale support. The informal 'you' form around 'this line' marks a direct, personal relationship."),
 (9, None,
  "'Look instead at this lovely ultrasound!' Dropping the subject pronoun turns the verb for 'look' into a direct, punchy command. Dropping the subject pronoun turns the verb for 'look' into a direct, punchy command."),
 (10, None,
  "'Our baby girl is already moving a lot.' Notice how 'moves' leads directly into the noun meaning 'daughter'. Notice how 'moves' leads directly into the noun meaning 'daughter'."),
 (11, None,
  "'Place your hand here on your belly.' A gentle directive guiding physical maternal contact. The verb meaning 'place' pairs naturally with the noun for 'human hand' in everyday conversation."),
 (12, None,
  "'She already has a strong personality!' The verb meaning 'has' pairs naturally with the noun for 'personality' in everyday conversation."),
 (13, None,
  "'She looks a lot like her mother.' The verb meaning 'resembles' pairs naturally with the noun for 'mother' in everyday conversation."),
]

TRANSITION = "Now let's listen to Andrea and Colette again at full speed."

OUTRO = ("Andrea and Colette resolve to fight the unfair hiring discrimination, finding strength in their growing family. "
         "Their shared joy over the baby ultrasound balances the stress of corporate legal battles.")

CLOSING = ("colette", "Tout ira bien, mon amour.")
