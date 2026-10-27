# Authoring module for dix-pour-cent s02e03 scene 08 (cues 202-224).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-08.py --out out/dix-pour-cent/s02e03/scene-08.json

ID = "dix-pour-cent-s02e03-scene-08"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 8
TITLE = "Rencontre dans le couloir  (Meeting in the Hallway)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "julien": "marcel"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel", "julien": "Julien"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 202-224. In the hallway, Sofia narrowly avoids blowing her cover when Mathias asks her to send a package. "
               "Hicham makes an energetic appearance, and Julien spots model Aymeline Val leaving Andrea's office. "
               "Adapted for A1 French.")

INTRO = ("Stepping out into the hallway of ASK, Sofia and Gabriel accompany Julien Dore. "
         "When Mathias hands Sofia an administrative errand in front of Julien, she quickly covers for herself, "
         "while the agency's new owner Hicham makes a lively impression. "
         "Let's listen to the scene in French first.")

STORY = [
 ("julien", "Il a une drôle de façon de traiter les acteurs.",
  "He has a strange way of treating actors.",
  [(205, "C'est votre agent ?"), (207, "Il a une drôle de façon de traiter les acteurs.")], "Julien is confused by Mathias's errand"),
 ("lea", "C'est juste une blague pour une pièce.",
  "It is just a joke for a play.",
  [(208, "Non, c'est juste..."), (209, "une blague, une réplique d'une pièce")], "Sofia covers for her receptionist duties"),
 ("julien", "Mathias rigole toujours avec tout le monde!",
  "Mathias is always joking around with everyone!",
  [(212, "Mathias rigole toujours !")], "Julien laughs it off"),
 ("gabriel", "Hicham Janowski arrive dans le couloir.",
  "Hicham Janowski arrives in the hallway.",
  [(218, "Hicham Janowski, le nouveau propriétaire d'ASK.")], "Gabriel spots Hicham"),
 ("julien", "C'est le nouveau propriétaire de l'agence?",
  "He is the new owner of the agency?",
  [(218, "le nouveau propriétaire d'ASK.")], "Julien asks about Hicham"),
 ("gabriel", "Oui, mais il s'occupe de la comptabilité.",
  "Yes, but he takes care of accounting.",
  [(221, "Non, il s'occupe de la comptabilité.")], "Gabriel downplays Hicham's role"),
 ("julien", "Qui est cette femme magnifique là-bas?",
  "Who is that gorgeous woman over there?",
  [(223, "-C'est qui ?")], "Julien spots Aymeline"),
 ("gabriel", "C'est le mannequin Aymeline Val.",
  "That is the model Aymeline Val.",
  [(223, "-Aymeline Val.")], "Gabriel identifies her"),
 ("julien", "Elle veut aussi devenir actrice?",
  "Does she also want to become an actress?",
  [(219, "c'est la meilleure."), (220, "Rien n'est décidé.")], "Julien asks about her career"),
 ("gabriel", "Oui, Andréa s'occupe de sa carrière.",
  "Yes, Andrea is managing her career.",
  [(219, "c'est la meilleure.")], "Gabriel confirms"),
 ("julien", "Vous avez une agence formidable!",
  "You have a wonderful agency!",
  [(219, "Vous avez fait le bon choix,")], "Julien praises ASK"),
 ("lea", "Merci pour cette belle rencontre, Julien.",
  "Thank you for this lovely meeting, Julien.",
  [(224, "Au revoir.")], "Sofia thanks Julien"),
 ("julien", "Au revoir, à très bientôt pour répéter!",
  "Goodbye, see you very soon to rehearse!",
  [(224, "Au revoir.")], "Julien says goodbye"),
]

OPENER = "Let's examine the conversation in the hallway line by line."

WALK = [
 (0, None,
  "'He has a strange way of treating actors.' Julien is surprised when Mathias treats Sofia like an office assistant."),
 (1, None,
  "'It is just a joke for a play.' Sofia quickly improvises to hide that she actually works as the receptionist."),
 (2, None,
  "'Mathias is always joking around with everyone!' Julien accepts her explanation with a smile."),
 (3, None,
  "'Hicham Janowski arrives in the hallway.' Gabriel spots the enthusiastic new majority shareholder."),
 (4, None,
  "'He is the new owner of the agency?' Julien asks about Hicham's role at ASK."),
 (5, None,
  "'Yes, but he takes care of accounting.' Gabriel downplays Hicham's involvement in artistic decisions."),
 (6, None,
  "'Who is that gorgeous woman over there?' Julien notices Aymeline Val walking out of Andrea's office."),
 (7, None,
  "'That is the model Aymeline Val.' Gabriel names the famous model."),
 (8, None,
  "'Does she also want to become an actress?' Julien asks if Aymeline is transitioning into cinema."),
 (9, None,
  "'Yes, Andrea is managing her career.' Gabriel confirms that Andrea is representing her."),
 (10, None,
  "'You have a wonderful agency!' Julien compliments the vibrant atmosphere at ASK."),
 (11, None,
  "'Thank you for this lovely meeting, Julien.' Sofia warmly bids farewell to the pop singer."),
 (12, None,
  "'Goodbye, see you very soon to rehearse!' Julien leaves on an upbeat note, promising to sing together soon."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Sofia skillfully manages the awkward encounter in the hallway, "
         "while Julien leaves with high spirits and an eagerness to collaborate on his musical soundtrack. "
         "Let's review the conversational phrases and vocabulary from this scene.")

CLOSING = ("julien", "Au revoir, à très bientôt pour répéter!")
