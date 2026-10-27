# Authoring module for dix-pour-cent s01e04 scene 06 (cues 160-192).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-06.py --out out/dix-pour-cent/s01e04/scene-06.json

ID = "dix-pour-cent-s01e04-scene-06"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 6
TITLE = "Une strip-teaseuse écolo  (An Ecologist Stripper)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Audrey", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"

INTRO = ("At the agency, Noémie has just scolded Camille for saying 'kiss-kiss' to a star on the phone. "
         "Now we're at a cafe with Mathias and his client Audrey Fleurot, who has brought her two small children "
         "along. Mathias is trying to pitch her Augustin's film between spoonfuls of baby food. "
         "We'll hear it in French first; just follow the story and don't worry about every word.")

STORY = [
 ("lea", "Chérie, fais-le pour maman.", "Sweetheart, do it for Mummy.",
  [(162, "Chérie, fais-le pour maman.")], ""),
 ("lea", "Parle-moi de cet Augustin. Quel est son nom de famille?",
  "Tell me about this Augustin. What's his surname?",
  [(165, "Parle-moi de cet Augustin."), (166, "Quel est son nom de famille ?")], ""),
 ("mathias", "Il s'appelle juste Augustin. C'est une star du web.",
  "He's just called Augustin. He's a web star.",
  [(168, "il s'appelle juste Augustin."), (169, "stars du web")], ""),
 ("lea", "Je ne connais rien à tout ça. J'ai même coupé le Wi-Fi!",
  "I don't know anything about all that. I even turned off the Wi-Fi!",
  [(170, "rien"), (170, "tout ça"), (171, "J'ai même coupé le Wi-Fi.")],
  "'Je ne suis au courant de rien de tout ça' -> 'Je ne connais rien à tout ça'"),
 ("lea", "C'est mauvais pour les jeunes cerveaux.", "It's bad for young brains.",
  [(172, "C'est mauvais pour les jeunes cerveaux.")], ""),
 ("mathias", "Regarde, c'est la meilleure de ses vidéos.", "Look, this is the best of his videos.",
  [(175, "C'est la meilleure de ses vidéos.")], ""),
 ("lea", "Mathias, il a douze ans!", "Mathias, he's twelve years old!",
  [(177, "Mathias, il a"), (177, "ans !")], "'12' written out as 'douze'"),
 ("mathias", "Il est jeune, mais très talentueux. Comme Xavier Dolan.",
  "He's young, but very talented. Like Xavier Dolan.",
  [(178, "Il est jeune"), (178, "mais très talentueux."), (179, "Comme Xavier Dolan.")], ""),
 ("lea", "Vraiment? Chérie, tu veux une compote de fruits?",
  "Really? Sweetheart, do you want a fruit compote?",
  [(180, "Vraiment ?"), (181, "Chérie, une compote de fruits ?")], ""),
 ("mathias", "C'est l'histoire d'une strip-teaseuse écolo. Très drôle, très moderne.",
  "It's the story of an ecologist stripper. Very funny, very modern.",
  [(184, "C'est l'histoire d'une strip-teaseuse écolo"), (184, "Très drôle, très moderne.")], ""),
 ("mathias", "C'est le film parfait pour ton retour.", "It's the perfect film for your comeback.",
  [(185, "c'est le film parfait pour ton retour.")], ""),
 ("lea", "J'adore le sujet. Mais quel est mon rôle?", "I love the subject. But what's my part?",
  [(186, "J'adore le sujet."), (187, "quel est mon rôle ?")], ""),
 ("mathias", "La strip-teaseuse écolo.", "The ecologist stripper.",
  [(188, "La strip-teaseuse écolo")], ""),
 ("lea", "Quoi? Mais il sait que j'ai eu deux enfants récemment?",
  "What? But does he know I had two children recently?",
  [(190, "il sait que j'ai"), (190, "eu deux enfants ?")], ""),
 ("mathias", "Ça n'a aucune importance!", "That doesn't matter at all!",
  [(191, "Ça n'a aucune importance.")], ""),
]

OPENER = ("Let's go back through their cafe meeting. Audrey is trying to get her little girl to eat first.")

WALK = [
 (0, None,
  "'Sweetheart, do it for Mummy.' Notice the hyphenated command at the start: 'do it'. Then she turns back to Mathias."),
 (1, None,
  "'Tell me about this Augustin. What's his surname?' Literally 'his name of family'."),
 (2, None,
  "'He's just called Augustin. He's a web star.' Like a lot of young online comedians in France, he only uses his first name."),
 (3, None,
  "'I don't know anything about all that. I even turned off the Wi-Fi!' Literally 'I have even cut the Wi-Fi'."),
 (4, None,
  "'It's bad for young brains.' Audrey is a very protective new mother. Mathias holds up his phone."),
 (5, None,
  "'Look, this is the best of his videos.' The word for 'the best' has a feminine ending here to match 'video'."),
 (6, None,
  "'Mathias, he's twelve years old!' Augustin is actually twenty-four, but to Audrey he looks like a schoolboy."),
 (7, None,
  "'He's young, but very talented. Like Xavier Dolan.' Mathias compares him to the famous young Canadian director."),
 (8, None,
  "'Really? Sweetheart, do you want a fruit compote?' Audrey is only half listening as she feeds her daughter."),
 (9, None,
  "'It's the story of an ecologist stripper. Very funny, very modern.' Notice the short casual word for 'ecologist' or 'green'."),
 (10, None,
  "'It's the perfect film for your comeback.' The word for 'return' also means an actor's comeback."),
 (11, None,
  "'I love the subject. But what's my part?' Audrey likes the sound of the comedy, assuming she plays a sensible supporting role."),
 (12, None,
  "'The ecologist stripper.' Mathias says it without blinking."),
 (13, None,
  "'What? But does he know I had two children recently?' Audrey has just had two babies in two years, and the idea of pole dancing makes her eyes widen."),
 (14, None,
  "'That doesn't matter at all!' Literally 'that has no importance'. For Mathias, nothing stands in the way of a contract."),
]

TRANSITION = "Let's hear the whole conversation again."

OUTRO = ("Audrey has a lot of tax bills to pay, and now Mathias wants her to play a stripper. "
         "Listen out for how French says 'surname' and 'that doesn't matter'. See you next time.")
CLOSING = ("lea", "Une strip-teaseuse écolo, vraiment?")
