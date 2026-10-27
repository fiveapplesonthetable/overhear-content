# Authoring module for dix-pour-cent s04e04 scene 12 (cues 886-896).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e04/authoring/scene-12.py --out overhear-content/out/dix-pour-cent/s04e04/scene-12.json

ID = "dix-pour-cent-s04e04-scene-12"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 12
TITLE = "Le grand amour de Sandrine  (Sandrine's True Love)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sarah", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 886-896. Sarah tries to reassure a distracted Gabriel that Sandrine Kiberlain "
    "will quickly tire of stand-up comedy and return to her true love, cinema. Realizing Gabriel "
    "is not listening to a word she says, an exasperated Sarah walks out."
)

INTRO = (
    "In Gabriel's office, Sarah tries to calm his fears about Sandrine Kiberlain's sudden passion for stand-up comedy. "
    "However, Gabriel is completely absorbed in his phone and barely pays attention to her advice. "
    "Let's listen to their tense exchange in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Ne t'inquiète pas pour Sandrine.",
     "Do not worry about Sandrine.",
     [(886, "Ne t'inquiète pas pour Sandrine")], "Sarah reassures Gabriel"),
    ("lea", "Elle veut juste changer d'air.",
     "She just wants a change of air.",
     [(887, "Elle veut juste changer d'air")], "Sarah explains Sandrine's whim"),
    ("gabriel", "Mais elle veut quitter le cinéma!",
     "But she wants to quit cinema!",
     [(891, "Le cinéma")], "Gabriel worries about her career"),
    ("lea", "Elle va s'amuser cinq minutes.",
     "She is going to have fun for five minutes.",
     [(888, "Elle va s'amuser cinq minutes")], "Sarah predicts it is temporary"),
    ("lea", "Puis elle va vite revenir.",
     "Then she will quickly come back.",
     [(888, "très vite"), (889, "revenir")], "Sarah says she will return soon"),
    ("gabriel", "Revenir vers quoi, à ton avis?",
     "Come back to what, in your opinion?",
     [(890, "Son grand amour")], "Gabriel asks what she means"),
    ("lea", "Vers son grand amour, bien sûr!",
     "To her true love, of course!",
     [(889, "son grand amour")], "Sarah refers to her true passion"),
    ("gabriel", "Et c'est quoi son grand amour?",
     "And what is her true love?",
     [(890, "Son grand amour")], "Gabriel asks skeptically"),
    ("lea", "C'est le cinéma, mon cher Gabriel.",
     "It is cinema, my dear Gabriel.",
     [(891, "Le cinéma")], "Sarah answers simply"),
    ("lea", "Mais tu ne m'écoutes même pas!",
     "But you are not even listening to me!",
     [(892, "tu n'écoutes pas")], "Sarah notices Gabriel is distracted"),
    ("lea", "D'accord, je m'en vais maintenant.",
     "All right, I am leaving now.",
     [(892, "je m'en vais")], "Sarah decides to walk out"),
    ("gabriel", "Mais si, je t'écoute vraiment!",
     "Yes I am, I am truly listening to you!",
     [(893, "Si… j'écoute")], "Gabriel protests that he is listening"),
    ("gabriel", "Tu veux venir avec moi ce soir?",
     "Do you want to come with me tonight?",
     [(893, "venir avec moi ce soir")], "Gabriel invites her out tonight"),
    ("lea", "Non, tu penses seulement au travail.",
     "No, you only think about work.",
     [(894, "Sarah")], "Sarah refuses and walks away"),
]

WALK = [
    (0, None,
     "'Do not worry about Sandrine.' Sarah tries to soothe Gabriel's anxiety over his famous client. "
     "The negative imperative 'ne t'inquiete pas' means do not worry."),
    (1, None,
     "'She just wants a change of air.' Sarah believes the actress merely craves novelty. "
     "The idiom 'changer d'air' means to get a change of scenery."),
    (2, None,
     "'But she wants to quit cinema!' Gabriel fears losing his star client to the stage forever. "
     "The verb 'quitter' means to leave or abandon."),
    (3, None,
     "'She is going to have fun for five minutes.' Sarah predicts that the comedy experiment will be brief. "
     "The reflexive verb 's'amuser' means to have fun or enjoy oneself."),
    (4, None,
     "'Then she will quickly come back.' Sarah is confident that Sandrine will return to film. "
     "The conjunction 'puis' means then or next."),
    (5, None,
     "'Come back to what, in your opinion?' Gabriel half-heartedly follows her train of thought. "
     "The phrase 'a ton avis' means in your opinion."),
    (6, None,
     "'To her true love, of course!' Sarah speaks poetically about the actress's lifelong vocation. "
     "The expression 'grand amour' translates as great love or true love."),
    (7, None,
     "'And what is her true love?' Gabriel stares at his screen while asking the question. "
     "The informal question 'c'est quoi' asks what something is."),
    (8, None,
     "'It is cinema, my dear Gabriel.' Sarah states the obvious answer with gentle irony. "
     "The adjective 'cher' means dear."),
    (9, None,
     "'But you are not even listening to me!' Sarah realizes that Gabriel is ignoring her completely. "
     "The adverb 'meme' adds the emphasis even."),
    (10, None,
     "'All right, I am leaving now.' Fed up with his inattention, Sarah turns toward the door. "
     "The idiomatic verb 's'en aller' means to go away or leave."),
    (11, None,
     "'Yes I am, I am truly listening to you!' Gabriel looks up in a panic and denies ignoring her. "
     "In French, 'si' is used instead of 'oui' to contradict a negative statement."),
    (12, None,
     "'Do you want to come with me tonight?' Gabriel tries to make amends by inviting her out. "
     "The preposition 'avec' means with."),
    (13, None,
     "'No, you only think about work.' Sarah rejects his offer and walks down the hallway. "
     "The adverb 'seulement' restricts the meaning to only."),
]

OUTRO = (
    "Sarah storms out of the office, leaving Gabriel calling her name in the corridor. "
    "Caught between his demanding clients and his relationship, Gabriel watches her leave in frustration. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("gabriel", "Hé, Sarah, attends-moi s'il te plaît!")
