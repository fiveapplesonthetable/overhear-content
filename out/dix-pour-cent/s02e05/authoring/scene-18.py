# Authoring module for dix-pour-cent s02e05 scene 18 (cues 550-588).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-18.py --out out/dix-pour-cent/s02e05/scene-18.json

ID = "dix-pour-cent-s02e05-scene-18"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 18
TITLE = "Le coup du beurre  (The Butter Trick)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "guy": "theo"}
LABELS = {"lea": "Arlette", "guy": "Guy"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 550-588. At the film set canteen, veteran actor Guy Marchand worries about his recent memory blanks. "
    "Arlette arrives with her dog Jean Gabin, playfully teasing him about his famous butter trick and boosting his confidence."
)

INTRO = (
    "At the studio canteen, veteran actor Guy Marchand eats lunch while feeling anxious about recent memory blanks on set. "
    "Arlette arrives with her faithful dog Jean Gabin to comfort her old friend before his afternoon scenes. "
    "Listen to the scene in French first."
)

STORY = [
    ("guy", "Il y a un grand choix de fromages ici.",
     "There is a wide selection of cheeses here.",
     [(552, "Il y a du camembert, du saint-nectaire,"), (554, "Une bien belle cantine.")], ""),
    ("lea", "Bonjour Guy! Comment se passe ton tournage?",
     "Hello Guy! How is your filming going?",
     [(578, "Je suis une très vieille amie."), (579, "Arlette Azémar.")], ""),
    ("guy", "Je confonds le poivre et le sel aujourd'hui.",
     "I confuse the pepper and the salt today.",
     [(558, "Merci. Non, le poivre."), (560, "Pardon, je me suis trompé.")], ""),
    ("lea", "Ce n'est pas grave, cela arrive à tout le monde.",
     "That is not serious, that happens to everyone.",
     [(561, "C'est pas grave, ça arrive.")], ""),
    ("guy", "Les gens me posent des questions sur ma mémoire.",
     "People are asking me questions about my memory.",
     [(562, "Vos trous de mémoire, c'est du passé ?"), (566, "Vous voulez que je me souvienne d'un trou.")], ""),
    ("guy", "Ils ont peur que j'oublie mon texte.",
     "They are afraid that I forget my lines.",
     [(563, "C'était une petite frayeur sans conséquence."), (567, "C'est un piège.")], ""),
    ("lea", "Tu as cinquante ans de carrière derrière toi.",
     "You have fifty years of career behind you.",
     [(576, "Ça fait 50 ans qu'il fait son coup du beurre.")], ""),
    ("guy", "Regarde, Jean Gabin adore le beurre!",
     "Look, Jean Gabin loves the butter!",
     [(572, "Jean Gabin !"), (574, "Tu aimes le beurre, hein ?")], ""),
    ("lea", "Jean Gabin, tiens-toi bien à table!",
     "Jean Gabin, behave yourself at the table!",
     [(573, "Tiens-toi bien !")], ""),
    ("lea", "Guy, tu fais toujours ton fameux coup du beurre?",
     "Guy, are you still doing your famous butter trick?",
     [(576, "Ça fait 50 ans qu'il fait son coup du beurre.")], ""),
    ("guy", "C'est une vieille habitude pour séduire la crémière.",
     "It is an old habit to charm the dairywoman.",
     [(577, "En espérant mettre la main sur la crémière !")], ""),
    ("lea", "Ne t'énerve pas pour quelques trous de mémoire.",
     "Do not get upset over a few memory blanks.",
     [(585, "Il ne fallait pas s'énerver comme ça.")], ""),
    ("guy", "Je veux réussir ma scène cet après-midi.",
     "I want to succeed in my scene this afternoon.",
     [(586, "Ouais, mais quand même !"), (588, "La prochaine scène !")], ""),
    ("lea", "Tu es un acteur formidable, aie confiance.",
     "You are a wonderful actor, have confidence.",
     [(580, "J'accompagne Guy sur ses tournages.")], ""),
    ("guy", "Merci d'être venue me voir sur le plateau.",
     "Thanks for coming to see me on the set.",
     [(587, "Bon, je retourne.")], ""),
    ("lea", "Je serai toujours là pour veiller sur toi.",
     "I will always be there to watch over you.",
     [(581, "Arlette Davidson."), (582, "C'est mon surnom.")], "")
]

OPENER = "Let's examine how Arlette comforts an anxious veteran actor."

WALK = [
    (0, None,
     "'There is a wide selection of cheeses here.' Guy admires the canteen buffet. "
     "The noun phrase grand choix means wide selection."),
    (1, None,
     "'Hello Guy! How is your filming going?' Arlette greets her long-time client warmly. "
     "The pronominal verb se passe asks how things are progressing."),
    (2, None,
     "'I confuse the pepper and the salt today.' Guy admits his momentary confusion. "
     "The verb confonds means to mix up or confuse."),
    (3, None,
     "'That is not serious, that happens to everyone.' Arlette reassures him immediately. "
     "The phrase tout le monde means everyone."),
    (4, None,
     "'People are asking me questions about my memory.' Guy expresses his frustration with inquiries. "
     "The feminine noun mémoire refers to memory recall."),
    (5, None,
     "'They are afraid that I forget my lines.' Guy senses the crew's anxiety. "
     "The subjunctive j'oublie follows avoir peur que."),
    (6, None,
     "'You have fifty years of career behind you.' Arlette reminds him of his vast experience. "
     "The numeral cinquante indicates fifty."),
    (7, None,
     "'Look, Jean Gabin loves the butter!' Guy feeds a treat to the dog. "
     "The masculine noun beurre refers to butter."),
    (8, None,
     "'Jean Gabin, behave yourself at the table!' Arlette scolds her pampered dog gently. "
     "The reflexive imperative tiens-toi bien means behave yourself."),
    (9, None,
     "'Guy, are you still doing your famous butter trick?' Arlette playfully brings up his signature habit. "
     "The adjective fameux means famous or well-known."),
    (10, None,
     "'It is an old habit to charm the dairywoman.' Guy chuckles at the recurring joke. "
     "The feminine noun habitude means habit or custom."),
    (11, None,
     "'Do not get upset over a few memory blanks.' Arlette urges him to stay calm and poised. "
     "The negative imperative ne t'énerve pas advises against anger."),
    (12, None,
     "'I want to succeed in my scene this afternoon.' Guy focuses on his acting performance. "
     "The verb réussir expresses successful execution."),
    (13, None,
     "'You are a wonderful actor, have confidence.' Arlette bolsters his self-assurance. "
     "The imperative aie comes from the verb avoir."),
    (14, None,
     "'Thanks for coming to see me on the set.' Guy appreciates her physical presence. "
     "The prepositional infinitive d'être venue expresses gratitude."),
    (15, None,
     "'I will always be there to watch over you.' Arlette pledges her unwavering loyalty. "
     "The simple future serai expresses an enduring commitment.")
]

TRANSITION = "Now let's listen to the warm conversation once more at normal pace."

OUTRO = (
    "With affection and humor, Arlette restores Guy's confidence before his next scene on set. "
    "Listen to the touching dialogue once more in French."
)

CLOSING = ("lea", "Je serai toujours là pour veiller sur toi.")
