# Authoring module for dix-pour-cent s04e02 scene 08 (cues 409-448).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e02/authoring/scene-08.py --out overhear-content/out/dix-pour-cent/s04e02/scene-08.json

ID = "dix-pour-cent-s04e02-scene-08"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 8
TITLE = "L'héritière de Barneville  (The Barneville Heiress)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo"}
LABELS = {"lea": "Camille", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 409-448. In their new apartment, Camille reviews Mathias's official paternity papers "
               "while Herve humorously calculates the immense Barneville family fortune.")

INTRO = ("In their newly shared apartment, Camille and Herve organize details for their housewarming celebration. "
         "While posting polite invitations for the neighbors, Herve notices Camille studying legal documents from Mathias "
         "regarding formal paternity recognition. Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("herve", "J'ai prévenu tous les voisins de l'immeuble.",
  "I warned all the building's neighbors.",
  [(427, "J'ai prévenu les voisins.")], "Reporting party announcement"),
 ("lea", "Pour notre pendaison de crémaillère demain soir?",
  "For our housewarming party tomorrow evening?",
  [(429, "pour la pendaison de crémaillère.")], "Clarifying the occasion"),
 ("herve", "Oui, avec un mot très cordial.",
  "Yes, with a very cordial note.",
  [(431, "Un mot dans la cage d'escalier.")], "Describing stairwell invitation"),
 ("herve", "Et toi, que regardes-tu sur cette feuille?",
  "And you, what are you looking at?",
  [(435, "Tu fais quoi là ?")], "Noticing official paperwork"),
 ("lea", "La procédure de reconnaissance de paternité de Mathias.",
  "Mathias's paternity recognition procedure.",
  [(436, "Je vérifie la procédure de reconnaissance de paternité.")], "Explaining legal document"),
 ("herve", "Tu vas accepter de signer ce papier?",
  "Are you going to agree to sign?",
  [(437, "Tu vas dire oui ?")], "Asking about her decision"),
 ("lea", "Je ne sais pas encore quoi décider.",
  "I do not know what to decide yet.",
  [(437, "Je sais pas.")], "Expressing personal hesitation"),
 ("herve", "Mais c'est une opportunité absolument incroyable, Camille!",
  "But it is an amazing opportunity, Camille!",
  [(444, "C'est pas rien.")], "Reacting with excitement"),
 ("lea", "C'est un choix familial très intime.",
  "It is a very intimate family choice.",
  [(439, "je dois décider s'il devient mon père ?")], "Emphasizing personal emotional weight"),
 ("herve", "Tu oublies une chose essentielle ici.",
  "You are forgetting one essential thing here.",
  [(441, "Mais tu oublies quelque chose.")], "Teasing upcoming financial point"),
 ("lea", "Quoi encore? Dis-moi la vérité.",
  "What now? Tell me the truth.",
  [(443, "Non, vraiment, je te jure.")], "Asking him to elaborate"),
 ("herve", "Tu deviendras l'héritière de l'empire Barneville!",
  "You will become the Barneville empire heiress!",
  [(442, "Tu vas devenir héritière de l'empire Barneville.")], "Proclaiming future inheritance"),
 ("lea", "Tu penses toujours à l'argent, Hervé!",
  "You always think about money, Herve!",
  [(445, "Oui, au moins !")], "Chiding his mercenary reaction"),
 ("herve", "Imagine le magnifique appartement immense pour nous!",
  "Imagine the huge magnificent apartment for us!",
  [(447, "Imagine, on pourrait se prendre un appartement immense.")], "Dreaming of luxury housing"),
]

WALK = [
 (0, None,
  "'I warned all the building's neighbors.' Herve shares his courteous neighborly update. "
  "The verb 'prevenir' means to notify or warn in advance."),
 (1, None,
  "'For our housewarming party tomorrow evening?' Camille verifies the event purpose. "
  "The noun phrase 'pendaison de cremaillere' refers to a housewarming party."),
 (2, None,
  "'Yes, with a very cordial note.' Herve describes his polite hallway notice. "
  "The adjective 'cordial' means friendly or courteous."),
 (3, None,
  "'And you, what are you looking at?' Herve observes Camille absorbed in a form. "
  "The inverted question 'que regardes-tu' inquires directly about an activity."),
 (4, None,
  "'Mathias's paternity recognition procedure.' Camille identifies the formal registry form. "
  "The compound noun phrase 'reconnaissance de paternite' denotes legal acknowledgement of fatherhood."),
 (5, None,
  "'Are you going to agree to sign?' Herve asks whether she will make it official. "
  "The near future 'vas accepter' explores her forthcoming choice."),
 (6, None,
  "'I do not know what to decide yet.' Camille feels torn about acknowledging Mathias. "
  "The verb 'decider' means to decide or settle on an option."),
 (7, None,
  "'But it is an amazing opportunity, Camille!' Herve sees only positive prestige. "
  "The adjective 'incroyable' expresses remarkable magnitude."),
 (8, None,
  "'It is a very intimate family choice.' Camille focuses on the delicate personal bond. "
  "The adjective 'intime' describes deep private matters."),
 (9, None,
  "'You are forgetting one essential thing here.' Herve prepares his humorous argument. "
  "The adjective 'essentielle' underlines crucial significance."),
 (10, None,
  "'What now? Tell me the truth.' Camille waits for Herve's punchline. "
  "The imperative 'dis-moi' directly requests clarification."),
 (11, None,
  "'You will become the Barneville empire heiress!' Herve envisions massive financial prestige. "
  "The future 'deviendras' marks her potential status as 'heritiere'."),
 (12, None,
  "'You always think about money, Herve!' Camille laughs at his relentless materialism. "
  "The noun 'argent' denotes money or wealth."),
 (13, None,
  "'Imagine the huge magnificent apartment for us!' Herve pictures their upgraded living quarters. "
  "The imperative 'imagine' encourages playful visualization."),
]

OUTRO = ("Camille weighs the emotional complexity of officially recognizing Mathias as her father. "
         "While Herve dreams of grand apartments and inherited millions, Camille knows family bonds run deeper than paperwork. "
         "Now, let's review the scene one last time.")

CLOSING = ("herve", "Imagine le magnifique appartement immense pour nous!")
