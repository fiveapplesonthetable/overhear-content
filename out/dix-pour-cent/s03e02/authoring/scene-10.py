# Authoring module for dix-pour-cent s03e02 scene 10 (cues 589-620).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-10.py --out out/dix-pour-cent/s03e02/scene-10.json

ID = "dix-pour-cent-s03e02-scene-10"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 10
TITLE = "L'invitation de Monica  (Monica's Invitation)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo", "hicham": "marcel"}
LABELS = {"lea": "Monica", "theo": "Gabriel", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 589-620. Star client Monica Bellucci calls the agency to discuss commercial ads, "
               "speaking first with Hicham before inviting Gabriel over to her home for homemade risotto. "
               "Adapted for A1 French.")

INTRO = ("At the agency, Italian screen icon Monica Bellucci calls to discuss advertising projects. "
         "After boss Hicham takes the initial call, Gabriel connects with Monica, who unexpectedly invites him to her home for dinner. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Bonjour, Gabriel est là?",
  "Hello, is Gabriel there?",
  [(589, "Bonjour, Monica.")], "Adapted greeting"),
 ("hicham", "Non, je suis son patron, Hicham Janowski.",
  "No, I am his boss, Hicham Janowski.",
  [(592, "Non, je suis son patron,"), (593, "Hicham Janowski.")], ""),
 ("lea", "Bonjour Hicham. Je voudrais parler à Gabriel.",
  "Hello Hicham. I would like to speak to Gabriel.",
  [(594, "Bonjour.")], "Adapted phone dialogue"),
 ("theo", "Allô, Monica! C'est moi, c'est Gabriel.",
  "Hello, Monica! It is me, it is Gabriel.",
  [(595, "Allô, Monica !"), (598, "C'est moi, c'est Gabriel.")], ""),
 ("lea", "Bonjour Gabriel, comment ça va?",
  "Hello Gabriel, how are you doing?",
  [(599, "Oui, ça va ?")], "Adapted greeting"),
 ("theo", "Très bien! J'ai réfléchi pour les contrats publicitaires.",
  "Very well! I thought about the advertising contracts.",
  [(601, "contrats publicitaires,"), (602, "j'ai réfléchi,")], "Adapted business update"),
 ("theo", "Ça pourrait vraiment nous intéresser.",
  "It could really interest us.",
  [(602, "ça pourrait m'intéresser, en fait.")], "Adapted business interest"),
 ("lea", "Super, j'en suis très ravie.",
  "Great, I am very delighted about it.",
  [(604, "Super, je suis ravi.")], "Adapted feminine agreement"),
 ("theo", "Tu veux passer au bureau pour en discuter?",
  "Do you want to come by the office to discuss it?",
  [(605, "Tu veux passer au bureau pour en discuter ?")], ""),
 ("lea", "Tu ne pourrais pas passer à la maison plutôt?",
  "Couldn't you come by my place instead?",
  [(606, "Tu pourrais pas passer à la maison, plutôt ?")], "Adapted negative"),
 ("lea", "Je voudrais te montrer des photos pour une pub.",
  "I would like to show you photos for an ad.",
  [(607, "Je voudrais te montrer des photos pour une pub,")], ""),
 ("theo", "Oui, c'est une excellente idée.",
  "Yes, that is an excellent idea.",
  [(611, "Oui, d'accord, super.")], "Adapted agreement"),
 ("lea", "Ce soir, tu peux venir chez moi?",
  "Tonight, can you come to my place?",
  [(610, "Ce soir, tu peux ?")], "Adapted invitation"),
 ("theo", "Oui d'accord, c'est parfait pour moi.",
  "Yes okay, that is perfect for me.",
  [(611, "Oui, d'accord, super.")], "Adapted confirmation"),
 ("lea", "Je te ferai ma recette secrète du risotto.",
  "I will make you my secret risotto recipe.",
  [(612, "Je te ferai ma recette secrète du risotto.")], ""),
 ("theo", "Rendez-vous chez toi à vingt heures trente!",
  "See you at your place at eight thirty!",
  [(614, "20h30 ?"), (616, "Au revoir.")], "Adapted closing"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Hello, is Gabriel there?' Monica calls the talent agency looking for her agent. "
  "The question 'est la' inquires about his presence."),
 (1, None,
  "'No, I am his boss, Hicham Janowski.' Hicham introduces himself with executive authority. "
  "The noun 'patron' denotes the head of the company."),
 (2, None,
  "'Hello Hicham. I would like to speak to Gabriel.' Monica maintains polite but focused intent. "
  "The conditional 'voudrais parler' expresses a courteous wish."),
 (3, None,
  "'Hello, Monica! It is me, it is Gabriel.' Gabriel snatches the telephone receiver. "
  "The emphatic phrase 'c'est moi' identifies the speaker warmly."),
 (4, None,
  "'Hello Gabriel, how are you doing?' Monica greets her agent warmly. "
  "The standard inquiry 'comment ca va' opens their exchange."),
 (5, None,
  "'Very well! I thought about the advertising contracts.' Gabriel shares his positive reflection. "
  "The past participle 'reflechi' denotes considered thought."),
 (6, None,
  "'It could really interest us.' Gabriel confirms the commercial opportunity. "
  "The conditional verb 'pourrait' frames a prospective business deal."),
 (7, None,
  "'Great, I am very delighted about it.' Monica welcomes his agreement. "
  "The feminine adjective 'ravie' expresses pleasure."),
 (8, None,
  "'Do you want to come by the office to discuss it?' Gabriel proposes a standard agency meeting. "
  "The infinitive 'passer' means to drop by."),
 (9, None,
  "'Couldn't you come by my place instead?' Monica shifts the venue to her private residence. "
  "The adverb 'plutot' suggests an intimate alternative."),
 (10, None,
  "'I would like to show you photos for an ad.' Monica provides a professional pretext. "
  "The noun 'pub' is common French shorthand for an advertisement."),
 (11, None,
  "'Yes, that is an excellent idea.' Gabriel enthusiastically agrees. "
  "The adjective 'excellente' modifies the feminine noun 'idee'."),
 (12, None,
  "'Tonight, can you come to my place?' Monica proposes dinner that very evening. "
  "The modal verb 'peux venir' asks about availability."),
 (13, None,
  "'Yes okay, that is perfect for me.' Gabriel confirms the evening plan without hesitation. "
  "The adjective 'parfait' conveys complete satisfaction."),
 (14, None,
  "'I will make you my secret risotto recipe.' Monica entices Gabriel with homemade cooking. "
  "The future tense 'ferai' promises a culinary treat."),
 (15, None,
  "'See you at your place at eight thirty!' Gabriel confirms the dinner appointment. "
  "The noun phrase 'rendez-vous' sets the meeting time."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Monica Bellucci calls ASK to discuss new promotional contracts with Gabriel. "
         "Instead of meeting at the office, she invites him to her apartment for a homemade risotto dinner.")
CLOSING = ("lea", "Je te ferai ma recette secrète du risotto.")
