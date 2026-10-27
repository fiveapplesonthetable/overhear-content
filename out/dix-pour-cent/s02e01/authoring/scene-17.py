# Authoring module for dix-pour-cent s02e01 scene 17 (cues 465-485).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-17.py --out out/dix-pour-cent/s02e01/scene-17.json

ID = "dix-pour-cent-s02e01-scene-17"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 17
TITLE = "Bréhier menace Arlette  (Bréhier Threatens Arlette)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "brehier": "theo"}
LABELS = {"lea": "Arlette", "brehier": "Bréhier"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 465-485. François Bréhier ambushes Arlette in the street while she walks her dog, "
    "threatening to leak past financial files if ASK attempts an aggressive buyout of StarMedia."
)

INTRO = (
    "On a quiet Parisian street, senior agent Arlette Azémar is walking her beloved Jack Russell "
    "terrier, Jean Gabin. Suddenly, rival agency head François Bréhier steps out from the shadows "
    "with a sinister warning. Listen to the conversation in French first."
)

STORY = [
    ("lea", "Allez, viens, Jean Gabin. Fais ta promenade.",
     "Come on, Jean Gabin. Take your walk.",
     [(465, "Allez, toutou"), (466, "Vas-y, Jean Gabin")], "Cleaned dog command for A1"),
    ("brehier", "Qu'est-ce que vous faites ici?",
     "What are you doing here?",
     [(469, "Mais qu'est-ce que vous foutez")], "Cleaned vulgar 'foutez' -> 'faites'"),
    ("lea", "Je promène mon chien.",
     "I am walking my dog.",
     [(470, "mon chien")], "Cleaned vulgar 'pisser' -> 'promène'"),
    ("brehier", "Vous êtes encore plus folle que prévu.",
     "You are even crazier than expected.",
     [(471, "que t'étais fou mais là c'est pire")], "Simplified idiom for A1"),
    ("brehier", "Vous allez bientôt finir à Pont-aux-Dames.",
     "You will soon end up at Pont-aux-Dames.",
     [(472, "Je vais bientôt finir à Pont-aux-Dames")], "'Je' -> 'Vous' for dramatic dialogue"),
    ("brehier", "Vous savez, la maison de retraite.",
     "You know, the retirement home.",
     [(474, "Vous savez, la maison de retraite")], ""),
    ("lea", "Tout le monde sait que j'y ai travaillé.",
     "Everyone knows that I worked there.",
     [(475, "Tout le monde sait que j'y ai travaillé")], ""),
    ("lea", "Et j'y ai rencontré beaucoup de gens.",
     "And I met a lot of people there.",
     [(476, "Et j'y ai rencontré beaucoup de gens")], ""),
    ("brehier", "Ils ne savent pas comment vous avez géré leur argent.",
     "They don't know how you managed their money.",
     [(477, "Ils ne savent pas comment vous avez géré l'argent")], "Cleaned offensive phrasing"),
    ("lea", "C'est de la diffamation!",
     "That is slander!",
     [(478, "C'est de la diffamation")], ""),
    ("brehier", "Non, c'est une menace. J'ai des preuves.",
     "No, it is a threat. I have proof.",
     [(479, "Non, c'est une menace"), (479, "La diffamation, c'est quand on n'a pas de preuves")], "Simplified for A1"),
    ("lea", "Qu'est-ce que vous voulez?",
     "What do you want?",
     [(480, "Qu'est-ce que vous voulez")], ""),
    ("brehier", "C'est la guerre entre ASK et StarMedia.",
     "It is war between ASK and StarMedia.",
     [(481, "C'est la guerre entre ASK et StarMedia")], ""),
    ("brehier", "Personne ne rachète personne.",
     "Nobody buys anyone out.",
     [(482, "mais chacun de son côté"), (483, "et personne ne rachète personne")], ""),
    ("brehier", "Sinon les vieux dossiers ressortent.",
     "Otherwise the old files come out.",
     [(484, "Sinon les vieux dossiers ressortent")], ""),
    ("lea", "Allez, Jean Gabin, on y va.",
     "Come on, Jean Gabin, let's go.",
     [(485, "Allez, on y va")], ""),
]

OPENER = "Let's walk through this tense confrontation line by line."

WALK = [
    (0, None,
     "'Come on, Jean Gabin. Take your walk.' Arlette encourages her dog on the sidewalk. "
     "Notice the imperative form of the verb to go."),
    (1, None,
     "'What are you doing here?' Bréhier steps out aggressively. "
     "The question uses the standard question phrase for what."),
    (2, None,
     "'I am walking my dog.' Arlette answers calmly. "
     "The verb to walk something uses a direct object."),
    (3, None,
     "'You are even crazier than expected.' Bréhier insults her mental state. "
     "The comparative structure uses more followed by than."),
    (4, None,
     "'You will soon end up at Pont-aux-Dames.' He threatens her with an elderly nursing home. "
     "The near future combines aller with the infinitive to end up."),
    (5, None,
     "'You know, the retirement home.' He spells out his threat clearly. "
     "The expression uses the formal second-person pronoun."),
    (6, None,
     "'Everyone knows that I worked there.' Arlette refuses to hide her past. "
     "The pronoun y replaces the place name."),
    (7, None,
     "'And I met a lot of people there.' She stands her ground firmly. "
     "The past tense combines to have with the past participle."),
    (8, None,
     "'They don't know how you managed their money.' Bréhier hints at past financial secrets. "
     "The question word how introduces the embedded clause."),
    (9, None,
     "'That is slander!' Arlette protests against the accusation. "
     "The partitive article indicates an abstract noun."),
    (10, None,
     "'No, it is a threat. I have proof.' Bréhier makes his blackmail explicit. "
     "The word for threat is a feminine noun."),
    (11, None,
     "'What do you want?' Arlette demands to know his real demand. "
     "Notice the verb to want in the second-person plural."),
    (12, None,
     "'It is war between ASK and StarMedia.' The rival agency head sets the stakes. "
     "The preposition between links the two rival agencies."),
    (13, None,
     "'Nobody buys anyone out.' He demands an end to the buyout talks. "
     "The double negative personne ne wraps the verb to buy out."),
    (14, None,
     "'Otherwise the old files come out.' He issues a final ultimatum. "
     "The conjunction otherwise warns of severe consequences."),
    (15, None,
     "'Come on, Jean Gabin, let's go.' Arlette walks away without yielding. "
     "The fixed expression on y va means let's go."),
]

TRANSITION = "Now let's listen to the entire dialogue once more without pauses."

OUTRO = (
    "Bréhier has laid his cards on the table, warning ASK to back off from StarMedia. "
    "Remember the key phrase for making a threat: faire une menace."
)

CLOSING = ("brehier", "Sinon les vieux dossiers ressortent.")
