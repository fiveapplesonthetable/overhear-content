# Authoring module for dix-pour-cent s04e04 scene 26 (cues 1215-1238).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e04/authoring/scene-26.py --out out/dix-pour-cent/s04e04/scene-26.json

ID = "dix-pour-cent-s04e04-scene-26"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 26
TITLE = "Les limites de la gentillesse  (The Limits of Kindness)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1215-1238. After driving across Paris to rescue Sofia from a cloakroom mishap, Gabriel sets firm boundaries "
    "and refuses to be her chauffeur to an afterparty in Chatou, reminding her that he must stop being overly accommodating."
)

INTRO = (
    "Outside a nightclub late at night, Gabriel arrives after driving across Paris to rescue Sofia, who claimed to be stranded without money. "
    "When Sofia reveals it was merely a coat check misunderstanding and asks for a ride to an afterparty, Gabriel finally decides to stand his ground. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine Gabriel and Sofia's late night encounter line by line."

STORY = [
    ("gabriel", "Sofia, comment ça va maintenant?",
     "Sofia, how are you doing now?",
     [(1216, "Ça va ?")], "Gabriel checks on her after rushing across town"),
    ("lea", "Oh, voilà enfin mon sauveur adoré!",
     "Oh, here is finally my beloved savior!",
     [(1217, "mon sauveur")], "Sofia greets him with dramatic relief"),
    ("gabriel", "Tu étais sans pièce d'identité?",
     "You were without ID?",
     [(1220, "sans pièce d'identité")], "Gabriel questions her urgent distress call"),
    ("lea", "La vestiaire a déplacé nos affaires.",
     "The coat check girl moved our things.",
     [(1222, "la vestiaire a pris nos affaires")], "Explains the petty cloakroom mix-up"),
    ("gabriel", "J'ai dû traverser tout Paris!",
     "I had to cross all of Paris!",
     [(1224, "traverser Paris")], "Gabriel expresses his growing annoyance"),
    ("lea", "Ne sois pas en colère, Gabriel.",
     "Do not be angry, Gabriel.",
     [(1225, "Ne sois pas en colère")], "Sofia tries to soothe his frustration"),
    ("lea", "Il y a une fête magnifique.",
     "There is a magnificent party.",
     [(1226, "Il y a une fête")], "Invites him to drive her to the suburbs"),
    ("gabriel", "Super, je te souhaite bonne nuit.",
     "Great, I wish you good night.",
     [(1227, "Bonne nuit")], "Gabriel curtly turns down her invitation"),
    ("lea", "Attends, s'il te plaît, Gabriel!",
     "Wait, please, Gabriel!",
     [(1228, "Gabriel, s'il te plaît")], "Sofia pleads with him to stay"),
    ("lea", "Je suis désolée pour ce retard.",
     "I am sorry for this delay.",
     [(1229, "Je suis désolée")], "Apologizes for inconveniencing him"),
    ("lea", "Tu es toujours si gentil, Gabriel.",
     "You are always so kind, Gabriel.",
     [(1230, "toujours si gentil")], "Appeals to his generous nature"),
    ("gabriel", "Je dois arrêter d'être aussi gentil.",
     "I must stop being so kind.",
     [(1231, "arrêter d'être aussi gentil")], "Gabriel sets a firm personal boundary"),
    ("lea", "Non, tu es parfait avec moi.",
     "No, you are perfect with me.",
     [(1232, "Tu es parfait")], "Sofia protests his sudden change in attitude"),
    ("gabriel", "Cette fois je dois vraiment partir.",
     "This time I really must leave.",
     [(1237, "Cette fois je dois vraiment y aller")], "Gabriel walks away into the night"),
]

WALK = [
    (0, None,
     "'Sofia, how are you doing now?' Gabriel asks how she is doing after his frantic drive across town. In everyday spoken French, rising intonation on 'goes' at the end is enough to turn the sentence into a question."),
    (1, None,
     "'Oh, here is finally my beloved savior!' Sofia welcomes him with theatrical affection. The key noun here means 'savior', anchored by its matching French article."),
    (2, None,
     "'You were without ID?' Gabriel asks whether she was truly stranded without identity papers. In everyday spoken French, rising intonation on 'were' at the end is enough to turn the sentence into a question."),
    (3, None,
     "'The coat check girl moved our things.' Sofia explains the trivial mix-up at the venue cloakroom. Notice how 'has' leads directly into the noun meaning 'coat check attendant'."),
    (4, None,
     "'I had to cross all of Paris!' Gabriel points out the trouble he took on her behalf. This conversational past tense combines a helper verb with the past participle for 'had to'."),
    (5, None,
     "'Do not be angry, Gabriel.' Sofia begs him not to lose his temper. Notice the classic French sandwich negation wrapping right around 'be'."),
    (6, None,
     "'There is a magnificent party.' Sofia pitches the suburban party in hopes of securing a ride. The descriptive adjective for 'magnificent' agrees in gender and number with its noun."),
    (7, None,
     "'Great, I wish you good night.' Gabriel dryly rejects the offer and prepares to leave. The descriptive adjective for 'super' agrees in gender and number with its noun."),
    (8, None,
     "'Wait, please, Gabriel!' Sofia calls after him to reconsider his sudden departure. The clause hinges on the everyday verb meaning 'wait'."),
    (9, None,
     "'I am sorry for this delay.' Sofia apologizes for making him come out so late. The key noun here means 'delay', anchored by its matching French article."),
    (10, None,
     "'You are always so kind, Gabriel.' Sofia flatters his usual accommodating personality. Sofia uses the casual singular 'you' with 'this line', showing close familiarity."),
    (11, None,
     "'I must stop being so kind.' Gabriel decides that he can no longer let people exploit his generosity. The clause hinges on the everyday verb meaning 'must'."),
    (12, None,
     "'No, you are perfect with me.' Sofia tries to reassure him of her appreciation. The descriptive adjective for 'perfect' agrees in gender and number with its noun."),
    (13, None,
     "'This time I really must leave.' Gabriel stands firm on his decision and steps away."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Tired of being taken for granted, Gabriel refuses to chauffeur Sofia and her friend to a late-night party, drawing a clear line and asserting his independence. When you watch the episode, listen out for the expressions meaning 'goes' and 'savior'. You'll catch them now. See you next time."
CLOSING = ("gabriel", "Je dois arrêter d'être aussi gentil.")
