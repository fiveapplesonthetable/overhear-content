# Authoring module for dix-pour-cent s03e02 scene 04 (cues 230-357).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-04.py --out out/dix-pour-cent/s03e02/scene-04.json

ID = "dix-pour-cent-s03e02-scene-04"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 4
TITLE = "La vie ordinaire  (Ordinary Life)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Monica", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 230-357. Monica browses quirky Paris dating guidebooks and convinces Gabriel "
               "to accompany her to an ordinary neighborhood party. Adapted for A1 French.")

INTRO = ("Inside a quiet Paris bookstore, Monica Bellucci browses quirky guides describing local romantic strolls. "
         "Craving genuine human connection away from the spotlight, she hatches a plan to attend a neighborhood apartment gathering with Gabriel. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("gabriel", "As-tu trouvé un guide intéressant, Monica?",
  "Did you find an interesting guide, Monica?",
  [(225, "Vous avez des guides pour célibataires à Paris ?")], "Asked about guidebook findings"),
 ("lea", "Ce livre propose des promenades très coquines!",
  "This book suggests very playful strolls!",
  [(231, "Mais si vous êtes plus hardi, il y a aussi le Paris coquin.")], "Shared quirky guidebook topic"),
 ("gabriel", "C'est un guide original pour visiter Paris.",
  "It is an original guide for visiting Paris.",
  [(232, "Et là, on sort de l'ordinaire.")], "Evaluated book novelty"),
 ("lea", "Le vendeur était tellement timide et troublé!",
  "The clerk was so shy and flustered!",
  [(234, "Pardon ? Je suis désolé, je l'ai pas vu."), (244, "Quel imbécile, je le fais.")], "Noted clerk's flustered shyness"),
 ("gabriel", "N'importe quel homme serait troublé devant toi.",
  "Any man would be flustered in front of you.",
  [(237, "je sais pas ce qui m'a pris.")], "Explained natural intimidation"),
 ("lea", "Je veux vivre une soirée parfaitement normale.",
  "I want to experience a perfectly normal evening.",
  [(239, "Non, mais ça m'intéresse, moi, Paris coquin.")], "Expressed longing for ordinary night"),
 ("gabriel", "Que veux-tu faire exactement ce soir?",
  "What do you want to do tonight exactly?",
  [(239, "ça m'intéresse")], "Asked about evening plans"),
 ("lea", "Aller à une petite fête entre voisins.",
  "Go to a small party among neighbors.",
  [(209, "on baisserait ensemble les rideaux.")], "Proposed neighborhood gathering"),
 ("gabriel", "Une fête d'immeuble avec des inconnus?",
  "A building party with strangers?",
  [(209, "ensemble")], "Clarified casual setting"),
 ("lea", "Oui, pour discuter sans protocole ni caméras.",
  "Oui, to chat without protocol or cameras.",
  [(202, "normal")], "Yearned for unscripted conversation"),
 ("gabriel", "Les gens vont immédiatement te reconnaître, Monica.",
  "People are going to recognize you immediately, Monica.",
  [(204, "célèbre")], "Warned of instant recognition"),
 ("lea", "Je porterai des vêtements simples et discrets.",
  "I will wear simple and discreet clothes.",
  [(209, "ensemble")], "Promised understated attire"),
 ("gabriel", "Tu es vraiment incorrigible et pleine d'énergie!",
  "You are truly incorrigible and full of energy!",
  [(232, "sort de l'ordinaire")], "Admired spontaneous spirit"),
 ("lea", "Tu viens avec moi, mon cher Gabriel?",
  "Are you coming with me, my dear Gabriel?",
  [(209, "ensemble")], "Invited agent to join"),
]

OPENER = "Let's see how Monica convinces Gabriel to accompany her on an ordinary Parisian evening."

WALK = [
 (0, None,
  "'Did you find an interesting guide, Monica?' An inverted question inquiring about guidebook discoveries."),
 (1, None,
  "'This book suggests very playful strolls!' An appreciative statement detailing quirky Parisian walking routes."),
 (2, None,
  "'It is an original guide for visiting Paris.' An agreeable evaluation describing alternative sightseeing."),
 (3, None,
  "'The clerk was so shy and flustered!' An amused observation noting the seller's visible shyness."),
 (4, None,
  "'Any man would be flustered in front of you.' An empathetic compliment contextualizing masculine intimidation."),
 (5, None,
  "'I want to experience a perfectly normal evening.' A decisive modal assertion stating a desire for ordinary life."),
 (6, None,
  "'What do you want to do tonight exactly?' An interrogative phrase seeking practical evening plans."),
 (7, None,
  "'Go to a small party among neighbors.' An infinitive proposal outlining a casual domestic gathering."),
 (8, None,
  "'A building party with strangers?' An incredulous clarifying question questioning the informal venue."),
 (9, None,
  "'Oui, to chat without protocol or cameras.' A purposeful prepositional phrase seeking genuine, unmediated conversation."),
 (10, None,
  "'People are going to recognize you immediately, Monica.' A cautionary near-future warning anticipating public recognition."),
 (11, None,
  "'I will wear simple and discreet clothes.' A reassuring future commitment to an understated outfit."),
 (12, None,
  "'You are truly incorrigible and full of energy!' An affectionate exclamation admiring adventurous spirit."),
 (13, None,
  "'Are you coming with me, my dear Gabriel?' A warm invitation asking an agent to join the adventure."),
]

TRANSITION = "Now let's listen to Gabriel and Monica again at full speed."

OUTRO = ("Monica Bellucci embraces the adventure of ordinary Parisian life, stepping away from the red carpet toward a neighborhood gathering. "
         "Accompanied by a protective Gabriel, she pursues her wish for sincere, unpretentious companionship.")

CLOSING = ("gabriel", "D'accord Monica, je t'accompagne ce soir.")
