# Authoring module for dix-pour-cent s04e02 scene 09 (cues 449-455).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e02/authoring/scene-09.py --out overhear-content/out/dix-pour-cent/s04e02/scene-09.json

ID = "dix-pour-cent-s04e02-scene-09"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 9
TITLE = "L'attente au café  (Waiting at the Café)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "serveur": "theo"}
LABELS = {"lea": "Andréa", "serveur": "Le serveur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 449-455. In a café near ASK, Andrea waits for star client Nathalie Baye, "
               "trading humorous banter with the waiter before discovering Mathias hijacked their appointment.")

INTRO = ("Sitting anxiously at a bistro table, Andrea waits for her important meeting with iconic actress Nathalie Baye. "
         "When she orders another coffee, a playful waiter teases her with celebrity lookalikes until an urgent phone call "
         "reveals that Mathias has diverted Nathalie to ASK. Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Pardon monsieur, excusez-moi.",
  "Pardon sir, excuse me.",
  [(449, "Pardon, excusez-moi.")], "Calling the waiter"),
 ("serveur", "Oui madame, que désirez-vous?",
  "Yes madam, what would you like?",
  [(450, "Bien sûr.")], "Offering polite service"),
 ("lea", "Je peux commander un autre café?",
  "Can I order another coffee?",
  [(450, "Je peux commander un autre café ?")], "Ordering second beverage"),
 ("serveur", "Bien sûr, je vous l'apporte immédiatement.",
  "Of course, I bring it to you immediately.",
  [(450, "Bien sûr.")], "Promising prompt delivery"),
 ("lea", "Vous avez vu Nathalie Baye aujourd'hui?",
  "Have you seen Nathalie Baye today?",
  [(451, "Vous avez vu Nathalie Baye ?")], "Inquiring about client"),
 ("serveur", "Nathalie Baye? Non, pas du tout.",
  "Nathalie Baye? No, not at all.",
  [(452, "Nathalie Baye ?"), (453, "Non, mais Catherine Deneuve est là-bas.")], "Denying sighting"),
 ("serveur", "Mais Catherine Deneuve est assise là-bas!",
  "But Catherine Deneuve is seated over there!",
  [(453, "Catherine Deneuve est là-bas.")], "Making playful celebrity joke"),
 ("lea", "Vraiment? Où ça dans la salle?",
  "Really? Where in the room?",
  [(453, "Vraiment ? Où ça ?")], "Looking around eagerly"),
 ("serveur", "Je plaisante, c'était une petite blague!",
  "I am joking, it was a little joke!",
  [(454, "Je plaisante !")], "Admitting prank"),
 ("lea", "Super, je n'ai pas le temps de rire.",
  "Great, I do not have time to laugh.",
  [(455, "Super.")], "Dismissing humor in stress"),
 ("lea", "Allô Gabriel? Où est passée Nathalie?",
  "Hello Gabriel? Where did Nathalie go?",
  [(464, "Vous n'êtes pas avec Andréa ?")], "Taking urgent mobile call"),
 ("lea", "Mathias l'a emmenée directement à l'agence!",
  "Mathias took her directly to the agency!",
  [(466, "la réunion ait lieu à l'agence.")], "Discovering client interception"),
 ("serveur", "Madame, voici votre nouveau café chaud!",
  "Madam, here is your hot fresh coffee!",
  [(474, "Votre café !")], "Delivering drink to departing guest"),
 ("lea", "Donnez-le plutôt à Catherine Deneuve!",
  "Give it instead to Catherine Deneuve!",
  [(475, "Donnez-le à Catherine Deneuve !")], "Delivering witty exit line"),
]

WALK = [
 (0, None,
  "'Pardon sir, excuse me.' Andrea calls the waiter to her table. "
  "The polite formulas 'pardon' and 'excusez-moi' request attention."),
 (1, None,
  "'Yes madam, what would you like?' The waiter responds with professional courtesy. "
  "The formal question 'que desirez-vous' asks for an order."),
 (2, None,
  "'Can I order another coffee?' Andrea asks for another drink while waiting. "
  "The modal verb 'peux' expresses permission to place an order."),
 (3, None,
  "'Of course, I bring it to you immediately.' The waiter confirms the second cup. "
  "The adverb 'immediatement' signals prompt service."),
 (4, None,
  "'Have you seen Nathalie Baye today?' Andrea checks whether her actress has arrived. "
  "The passe compose 'avez vu' asks about past visual sighting."),
 (5, None,
  "'Nathalie Baye? No, not at all.' The waiter clarifies that he has not spotted her. "
  "The negative phrase 'pas du tout' means not in the least."),
 (6, None,
  "'But Catherine Deneuve is seated over there!' The waiter points out a playful illusion. "
  "The past participle 'assise' functions here as a predicate adjective."),
 (7, None,
  "'Really? Where in the room?' Andrea takes the bait for a brief moment. "
  "The question 'ou ca' asks for a specific location."),
 (8, None,
  "'I am joking, it was a little joke!' The waiter laughs at his own jest. "
  "The verb 'plaisanter' means to joke or kid."),
 (9, None,
  "'Great, I do not have time to laugh.' Andrea shows her impatience under pressure. "
  "The noun phrase 'pas le temps' denotes lack of available time."),
 (10, None,
  "'Hello Gabriel? Where did Nathalie go?' Andrea checks in by phone. "
  "The interjection 'allo' begins French telephone calls."),
 (11, None,
  "'Mathias took her directly to the agency!' Andrea learns of Mathias's tactical maneuver. "
  "The compound passe compose 'a emmenee' describes accompanying someone somewhere."),
 (12, None,
  "'Madam, here is your hot fresh coffee!' The waiter delivers the cup as she rises. "
  "The presentation adverb 'voici' presents an item directly."),
 (13, None,
  "'Give it instead to Catherine Deneuve!' Andrea snaps back with dry sarcasm. "
  "The adverb 'plutot' means instead or rather."),
]

OUTRO = ("Andrea races out of the cafe after realizing Mathias has intercepted Nathalie Baye. "
         "Leaving the waiter with his coffee joke, she rushes to the agency to regain control of the situation. "
         "Now, let's review the scene one last time.")

CLOSING = ("lea", "Donnez-le plutôt à Catherine Deneuve!")
