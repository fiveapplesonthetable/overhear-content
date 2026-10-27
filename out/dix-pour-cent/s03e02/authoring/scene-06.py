# Authoring module for dix-pour-cent s03e02 scene 06 (cues 430-520).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-06.py --out out/dix-pour-cent/s03e02/scene-06.json

ID = "dix-pour-cent-s03e02-scene-06"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 6
TITLE = "Le choix des prénoms  (Choosing Baby Names)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 430-520. In bed, Andréa and Colette try to choose a baby name from their lists, "
               "sparking disagreements over past girlfriends and Andréa's commitment to the pregnancy. Adapted for A1 French.")

INTRO = ("In their apartment bedroom, talent agent Andrea Martel and her partner Colette discuss baby names for their future child. "
         "When Andrea's suggestions trigger memories of old relationships, Colette questions Andrea's readiness for parenthood. "
         "Let's listen to the scene in French first.")

STORY = [
 ("colette", "Nous devions comparer nos listes de prénoms.",
  "We were supposed to compare our lists of first names.",
  [(435, "On avait dit qu'on se montrait nos listes, ce soir."), (436, "Les prénoms.")], "Colette reminds Andrea of their agreement"),
 ("lea", "J'ai oublié ma liste écrite au bureau.",
  "I forgot my written list at the office.",
  [(437, "t'as oublié la liste au bureau.")], "Andrea confesses the oversight"),
 ("lea", "Mais j'ai tous les noms en tête.",
  "But I have all the names in my head.",
  [(438, "parce que je l'ai bien en tête.")], "Andrea insists she remembers them all"),
 ("lea", "Que penses-tu du joli prénom Clélia?",
  "What do you think of the pretty first name Clelia?",
  [(443, "Alors, Clélia."), (444, "C'est joli.")], "Andrea proposes a first choice"),
 ("colette", "Je suis déjà sortie avec une Clélia.",
  "I have already dated a Clelia.",
  [(446, "Mais je suis sortie avec une Clélia")], "Colette dismisses the name"),
 ("lea", "Et que dis-tu de Natacha alors?",
  "And what do you say about Natacha then?",
  [(450, "Natacha ? La Russie, Tolstoy...")], "Andrea suggests another option"),
 ("colette", "C'est encore une de tes anciennes amoureuses?",
  "Is that another one of your former lovers?",
  [(451, "C'est aussi une fille avec qui t'as couché, c'est ça ?")], "Colette suspects another ex"),
 ("lea", "Non, c'était juste une camarade d'école!",
  "No, she was just a school classmate!",
  [(453, "y avait une Natacha dans notre classe en prépa.")], "Andrea defends her suggestion"),
 ("colette", "Nous n'avons toujours aucun prénom choisi.",
  "We still do not have any name chosen.",
  [(464, "On est près de sur rien."), (466, "Pas de chambre d'enfant, pas de prénom, rien.")], "Colette laments the lack of progress"),
 ("colette", "Tu n'es pas investie dans cette grossesse.",
  "You are not invested in this pregnancy.",
  [(467, "c'était pas du tout investi dans cette grossesse.")], "Colette expresses deep frustration"),
 ("lea", "Et mes rendez-vous médicaux tous les quinze jours?",
  "And my medical appointments every two weeks?",
  [(472, "Et les rendez-vous médicaux, là, tous les quinze jours,")], "Andrea highlights her medical efforts"),
 ("lea", "Notre petite fille n'est pas encore née!",
  "Our little girl is not born yet!",
  [(477, "Non, mais elle est pas encore née, la petite.")], "Andrea emphasizes there is still time"),
 ("lea", "Je veux profiter un peu de notre liberté.",
  "I want to enjoy our freedom a little bit.",
  [(478, "on peut pas profiter encore un tout petit peu de notre liberté.")], "Andrea asks for more couple time"),
]

OPENER = "Let's examine how Andrea and Colette discuss their future child step by step."

WALK = [
 (0, None,
  "'We were supposed to compare our lists of first names.' Colette reminds Andrea that they planned to choose baby names tonight."),
 (1, None,
  "'I forgot my written list at the office.' Andrea admits that she left her paper notepad at work."),
 (2, None,
  "'But I have all the names in my head.' Andrea reassures Colette that she remembers each of her favorite suggestions."),
 (3, None,
  "'What do you think of the pretty first name Clelia?' Andrea offers her first idea for their baby daughter."),
 (4, None,
  "'I have already dated a Clelia.' Colette quickly vetoes the name because of an unpleasant past relationship."),
 (5, None,
  "'And what do you say about Natacha then?' Andrea puts forward an alternative literary-inspired name."),
 (6, None,
  "'Is that another one of your former lovers?' Colette playfully suspects another romantic history behind the name."),
 (7, None,
  "'No, she was just a school classmate!' Andrea defends herself by explaining that Natacha was simply an old schoolmate."),
 (8, None,
  "'We still do not have any name chosen.' Colette sighs that they have prepared neither a nursery nor a baby name."),
 (9, None,
  "'You are not invested in this pregnancy.' Colette shares her growing worry that Andrea is avoiding parenting responsibilities."),
 (10, None,
  "'And my medical appointments every two weeks?' Andrea reminds Colette of the frequent medical examinations she endures."),
 (11, None,
  "'Our little girl is not born yet!' Andrea points out that they still have time before the baby arrives."),
 (12, None,
  "'I want to enjoy our freedom a little bit.' Andrea expresses her desire to cherish their time together as a couple."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("A playful discussion about baby names turns into an honest conversation about the changes that parenthood will bring. "
         "Let's review the key family and emotional vocabulary from this scene.")

CLOSING = ("lea", "Je veux profiter un peu de notre liberté.")
