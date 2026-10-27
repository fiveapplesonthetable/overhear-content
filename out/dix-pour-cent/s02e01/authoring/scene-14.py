# Authoring module for dix-pour-cent s02e01 scene 14 (cues 376-421).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-14.py --out out/dix-pour-cent/s02e01/scene-14.json

ID = "dix-pour-cent-s02e01-scene-14"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 14
TITLE = "Retrouvailles à Couchey  (Reunion in Couchey)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "maire": "theo", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "maire": "Le maire", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 376-421. Andréa visits the town hall in Couchey, where the mayor introduces a surprise guest: "
               "Hicham Janowski, a former schoolmate who sold his tech company for two hundred million euros. "
               "Adapted for A1 French.")

INTRO = ("Andrea arrives at the village town hall of Couchey for her mother's medal ceremony. "
         "The mayor introduces a special guest from London, young tech millionaire Hicham Janowski, "
         "who turns out to be an old classmate from Andrea's school days. Let's listen to the scene in French first.")

STORY = [
 ("lea", "Monsieur le maire.",
  "Mr. Mayor.",
  [(376, "Monsieur le maire")], ""),
 ("maire", "Andréa, je suis ravi de vous voir ici.",
  "Andréa, I am delighted to see you here.",
  [(377, "Andréa, je suis ravi de vous voir ici")], ""),
 ("lea", "Ravie d'être là.",
  "Delighted to be here.",
  [(378, "Ravie d'être là")], ""),
 ("maire", "Nous avons un léger changement de programme.",
  "We have a slight change of schedule.",
  [(380, "Nous avons un léger changement de programme")], ""),
 ("maire", "Nous avons un invité surprise: Hicham Janowski!",
  "We have a surprise guest: Hicham Janowski!",
  [(383, "nous avons un invité surprise"), (386, "Hicham Janowski")], ""),
 ("lea", "Le gars du site de rencontres?",
  "The guy from the dating site?",
  [(387, "Le gars du site de rencontres")], ""),
 ("maire", "Ça ne vous dérange pas de partager la vedette?",
  "You do not mind sharing the spotlight?",
  [(389, "Ça ne vous dérange pas de partager la vedette")], ""),
 ("lea", "Bien sûr que non.",
  "Of course not.",
  [(390, "Bien sûr que non")], ""),
 ("maire", "Le voilà! Hicham, bienvenue à Couchey.",
  "Here he is! Hicham, welcome to Couchey.",
  [(391, "Le voilà")], "Added welcome"),
 ("hicham", "Je vous connais, non?",
  "I know you, right?",
  [(400, "Je vous connais, non")], ""),
 ("lea", "On était à l'école ensemble.",
  "We were at school together.",
  [(401, "On était à l'école ensemble")], ""),
 ("hicham", "C'est ça! Andréa Marteau.",
  "That's it! Andréa Marteau.",
  [(402, "C'est ça"), (403, "Andréa Marteau")], ""),
 ("lea", "Martel. Mon nom de scène.",
  "Martel. My stage name.",
  [(405, "Martel. Mon nom de scène")], ""),
 ("hicham", "Vous avez donc changé de nom.",
  "So you changed your name.",
  [(406, "Vous avez donc changé de nom")], ""),
 ("maire", "Hicham a vendu son site pour deux cents millions d'euros!",
  "Hicham sold his site for two hundred million euros!",
  [(415, "Vous avez vendu votre site pour la coquette somme de 200 millions d'euros")], "Written out numbers"),
 ("hicham", "Très bien. L'humour de Couchey!",
  "Very well. Couchey humor!",
  [(420, "Très bien"), (421, "L'humour Couchey")], ""),
]

OPENER = "Andrea reconnects with her roots. Let us examine the lines with English notes."

WALK = [
 (0, None, "'Mr. Mayor.' Andrea addresses the village official politely. Monsieur le maire is the formal title."),
 (1, None, "'Andrea, I am delighted to see you here.' Ravi is an adjective meaning thrilled or delighted."),
 (2, None, "'Delighted to be here.' Andrea responds with the feminine agreement ravie."),
 (3, None, "'We have a slight change of schedule.' Leger means slight, and le programme means schedule."),
 (4, None, "'We have a surprise guest: Hicham Janowski!' Un invite surprise means a surprise guest."),
 (5, None, "'The guy from the dating site?' Un site de rencontres is the French phrase for a dating website."),
 (6, None, "'You do not mind sharing the spotlight?' Partager la vedette is an idiom meaning to share the spotlight."),
 (7, None, "'Of course not.' Bien sur que non is an emphatic expression meaning of course not."),
 (8, None, "'Here he is! Hicham, welcome to Couchey.' Le voila means here he is, introducing his arrival."),
 (9, None, "'I know you, right?' Hicham recognizes Andrea from their childhood in the village."),
 (10, None, "'We were at school together.' Ensemble is an adverb meaning together."),
 (11, None, "'That is it! Andrea Marteau.' C'est ca is a conversational expression meaning that's right."),
 (12, None, "'Martel. My stage name.' Un nom de scene is a professional or stage pseudonym."),
 (13, None, "'So you changed your name.' Donc means so, noting her professional identity change."),
 (14, None, "'Hicham sold his site for two hundred million euros!' Vendre means to sell, followed by a huge sum."),
 (15, None, "'Very well. Couchey humor!' L'humour is a masculine noun meaning humor or joking."),
]

TRANSITION = "Now listen to Andrea and Hicham's conversation once more at a natural pace."
OUTRO = ("Andrea is stunned to discover that her nerdy former classmate is now enormously wealthy. "
         "Back in Paris, Mathias faces an enraged film producer. "
         "Here is our closing phrase.")
CLOSING = ("hicham", "Très bien. L'humour de Couchey!")
