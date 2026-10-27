# Authoring module for dix-pour-cent s02e04 scene 19 (cues 516-560).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-19.py --out out/dix-pour-cent/s02e04/scene-19.json

ID = "dix-pour-cent-s02e04-scene-19"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 19
TITLE = "Le premier rôle  (The Lead Role)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 516-560. Julien Doré sends a text message about Sofia's songs. After an initial shock, Gabriel and Sofia "
    "discover that Julien wants Sofia to star as the female lead in his musical film and compose the soundtrack."
)

INTRO = (
    "In Gabriel's office, Sofia waits anxiously for news about her audition songs for Julien Doré's upcoming movie. "
    "A text message arrives from the famous singer, bringing an unexpected and life-changing opportunity. "
    "Listen to the scene in French first."
)

STORY = [
    ("gabriel", "J'ai reçu un message de Julien Doré.",
     "I received a message from Julien Doré.",
     [(516, "C'est Julien")], ""),
    ("lea", "Qu'est-ce qu'il dit dans son message?",
     "What does he say in his message?",
     [(519, "Un SMS ? Il est sérieux ?")], ""),
    ("gabriel", "Il pense que les chansons ne conviennent pas.",
     "He thinks that the songs are not suitable.",
     [(517, "J'ai réfléchi, ces chansons ne sont pas une bonne idée.")], ""),
    ("lea", "C'est dommage, j'aimais beaucoup ce projet.",
     "That is a pity, I really liked this project.",
     [(518, "Merde !"), (523, "Oui, mais quand même... C'est juste...")], ""),
    ("gabriel", "Attends, il y a une deuxième phrase!",
     "Wait, there is a second sentence!",
     [(524, "Je vous propose plutôt de m'accompagner")], ""),
    ("gabriel", "Il veut que tu joues dans son film.",
     "He wants you to act in his movie.",
     [(525, "dans le film et de faire la bande originale")], ""),
    ("lea", "Il veut que je sois l'actrice principale?",
     "He wants me to be the lead actress?",
     [(526, "Attendez, il veut que je joue dedans ? Et que je chante ?")], ""),
    ("gabriel", "Oui, et que tu composes la musique aussi.",
     "Yes, and that you compose the music too.",
     [(525, "et de faire la bande originale")], ""),
    ("lea", "Mais Charlotte Le Bon devait avoir ce rôle!",
     "But Charlotte Le Bon was supposed to have this role!",
     [(528, "Charlotte Le Bon est censée être au casting.")], ""),
    ("gabriel", "Je vais l'appeler pour vérifier cette proposition.",
     "I will call him to check this proposal.",
     [(529, "Je vais l'appeler.")], ""),
    ("gabriel", "Julien me confirme que le rôle est pour toi.",
     "Julien confirms to me that the role is for you.",
     [(536, "Grâce à toi, j'ai rencontré Sofia."), (537, "Je la veux.")], ""),
    ("gabriel", "Il dit que tu as un talent immense.",
     "He says that you have immense talent.",
     [(539, "Je l'ai vue, elle est parfaite !"), (541, "Elle a tout.")], ""),
    ("lea", "C'est une opportunité incroyable pour ma carrière.",
     "It is an incredible opportunity for my career.",
     [(527, "Le grand jeu !")], ""),
    ("gabriel", "Tu as travaillé dur pour arriver ici.",
     "You worked hard to get here.",
     [(545, "Elle s'est vraiment confiée à moi.")], ""),
    ("gabriel", "Tu mérites pleinement ce premier rôle.",
     "You fully deserve this lead role.",
     [(551, "Elle est parfaite.")], ""),
    ("lea", "Gabriel, nous devons fêter cette nouvelle!",
     "Gabriel, we must celebrate this news!",
     [(560, "Tu sais qu'il veut que tu joues le rôle principal dans son film ?")], "")
]

OPENER = "Let's examine how Gabriel shares the big news with Sofia."

WALK = [
    (0, None,
     "'I received a message from Julien Doré.' Gabriel announces the unexpected text. "
     "The past tense ai reçu comes from the irregular verb recevoir."),
    (1, None,
     "'What does he say in his message?' Sofia inquires eagerly. "
     "The question phrase qu'est-ce qu'il dit asks what he is saying."),
    (2, None,
     "'He thinks that the songs are not suitable.' Gabriel shares the initial disappointment. "
     "The verb conviennent expresses appropriateness."),
    (3, None,
     "'That is a pity, I really liked this project.' Sofia expresses her regret. "
     "The expression c'est dommage means that is a pity."),
    (4, None,
     "'Wait, there is a second sentence!' Gabriel reads further with surprise. "
     "The ordinal number deuxième precedes the noun phrase."),
    (5, None,
     "'He wants you to act in his movie.' Gabriel announces the sudden proposal. "
     "The subjunctive form joues follows the expression of will."),
    (6, None,
     "'He wants me to be the lead actress?' Sofia is astonished by the opportunity. "
     "The subjunctive sois comes from the irregular verb être."),
    (7, None,
     "'Yes, and that you compose the music too.' Gabriel mentions the soundtrack request. "
     "The adverb aussi adds supplementary information."),
    (8, None,
     "'But Charlotte Le Bon was supposed to have this role!' Sofia remembers the original casting choice. "
     "The imperfect devait indicates prior intention."),
    (9, None,
     "'I will call him to check this proposal.' Gabriel seeks immediate clarification. "
     "The preposition pour expresses purpose before an infinitive."),
    (10, None,
     "'Julien confirms to me that the role is for you.' Gabriel delivers the definitive confirmation. "
     "The present tense me confirme shows direct affirmation."),
    (11, None,
     "'He says that you have immense talent.' Julien's praise is relayed enthusiastically. "
     "The adjective immense emphasizes great artistic skill."),
    (12, None,
     "'It is an incredible opportunity for my career.' Sofia realizes the significance of this break. "
     "The feminine noun opportunité takes the adjective incroyable."),
    (13, None,
     "'You worked hard to get here.' Gabriel acknowledges her dedication and perseverance. "
     "The compound past as travaillé indicates completed effort."),
    (14, None,
     "'You fully deserve this lead role.' Gabriel offers heartfelt encouragement. "
     "The adverb pleinement reinforces the verb mériter."),
    (15, None,
     "'Gabriel, we must celebrate this news!' Sofia is ready to celebrate the achievement. "
     "The verb fêter means to celebrate a happy event.")
]

TRANSITION = "Now let's listen to the joyful conversation once more at full speed."

OUTRO = (
    "Sofia's musical audition turns into the role of a lifetime in Julien Doré's upcoming movie. "
    "Listen to the wonderful conversation once more in French."
)

CLOSING = ("lea", "Gabriel, nous devons fêter cette nouvelle!")
