ID = "domashniy-arest-s01e09-scene-06"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 6
TITLE = "Холостяцкая жизнь  (The Bachelor Life)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nina": "angelina"}
LABELS = {"anya": "Самсон", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 161-167. Nina mockingly packs Samsonov's flask for his new bachelor life. "
    "Samsonov attempts Arkady's ten-second masculine stare to intimidate her, but gets flustered and claims his stomach hurts."
)

INTRO = (
    "In this scene, Nina is packing Samsonov's small suitcase in their communal apartment. "
    "She mockingly puts in his metal flask for his upcoming bachelor life. "
    "Remembering Arkady's advice, Samsonov attempts an intense ten-second stare to intimidate her, "
    "but the psychological tactic fails completely. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("nina", "Фляжка, конечно!",
     "A flask, of course!",
     [(161, "Фляжка, конечно")], ""),
    ("nina", "Как же в холостяцкую жизнь без фляжки?",
     "How can you start bachelor life without a flask?",
     [(162, "в холостяцкую жизнь-то и без фляжки")], ""),
    ("anya", "Так, надо смотреть тяжело.",
     "Right, I need to stare intensely.",
     [], "internal monologue recalling Arkady's instruction"),
    ("anya", "По-мужски, ровно десять секунд.",
     "Like a real man, exactly ten seconds.",
     [], "counting seconds"),
    ("anya", "Один, два, три...",
     "One, two, three...",
     [], "counting seconds"),
    ("nina", "Чего ты уставился?",
     "What are you staring at?",
     [(163, "Чего уставился-то")], ""),
    ("anya", "Четыре, пять, шесть...",
     "Four, five, six...",
     [], "continuing the stare"),
    ("nina", "У тебя нервный тик?",
     "Do you have a nervous tic?",
     [(164, "У тебя что, нервный тик")], ""),
    ("anya", "Живот крутит.",
     "My stomach is acting up.",
     [(165, "Живот крутит")], ""),
    ("nina", "Так сходи в туалет!",
     "Then go to the bathroom!",
     [(166, "Так сходи в туалет")], ""),
    ("nina", "Не терпи, Самсон.",
     "Don't hold it in, Samson.",
     [(166, "не терпи")], ""),
    ("anya", "Я не в туалет иду!",
     "I am not going to the bathroom!",
     [], "angry defense"),
    ("anya", "Я ухожу навсегда!",
     "I am leaving forever!",
     [], "Samsonov announces departure"),
    ("nina", "Иди, скатертью дорожка!",
     "Go, and good riddance!",
     [], "dismissive retort"),
]

OPENER = (
    "Now let's examine Samsonov's failed intimidation tactic line by line. "
    "Nina packs his bag while Samsonov attempts an intense stare."
)

WALK = [
    (0, None,
     "'A flask, of course!' Nina sarcastically adds a drinking flask to Samsonov's bag."),
    (1, None,
     "'How can you start bachelor life without a flask?' The preposition takes the accusative case for destination."),
    (2, None,
     "'Right, I need to stare intensely.' The modal word combines with an infinitive to express necessity."),
    (3, None,
     "'Like a real man, exactly ten seconds.' Samsonov reminds himself of Arkady's psychological advice."),
    (4, None,
     "'One, two, three...' Samsonov counts the seconds mentally to reach ten."),
    (5, None,
     "'What are you staring at?' The colloquial verb expresses surprise at his strange facial expression."),
    (6, None,
     "'Four, five, six...' The husband continues counting under his breath despite her question."),
    (7, None,
     "'Do you have a nervous tic?' Nina mocks his twitching facial expression."),
    (8, None,
     "'My stomach is acting up.' The reflexive colloquial idiom describes an upset stomach."),
    (9, None,
     "'Then go to the bathroom!' The imperative verb directs him to the communal restroom."),
    (10, None,
     "'Don't hold it in, Samson.' The negative imperative advises him not to endure discomfort."),
    (11, None,
     "'I am not going to the bathroom!' Samsonov furiously rejects her domestic interpretation."),
    (12, None,
     "'I am leaving forever!' The present tense verb expresses definite future departure."),
    (13, None,
     "'Go, and good riddance!' Nina dismisses him with a traditional Russian parting idiom."),
]

TRANSITION = "Now let's listen to Nina and Samsonov's exchange one more time without pauses."
OUTRO = (
    "Samsonov's attempt at psychological intimidation backfires completely as Nina laughs at him. "
    "In the next scene, he reports back to Arkady in frustration."
)
CLOSING = ("anya", "Я ухожу навсегда!")
