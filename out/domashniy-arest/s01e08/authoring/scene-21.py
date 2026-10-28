# domashniy-arest/s01e08/scene-21.py
ID = "domashniy-arest-s01e08-scene-21"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 21
TITLE = "Яблоко от яблони  (The Apple Doesn't Fall Far)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 8"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"
VOICES = {"narrator": "sky", "nina": "angelina", "samson": "anja"}
LABELS = {"nina": "Нина", "samson": "Самсон"}
INTRO = "Previously, back at the communal apartment, Arkady and young Lyosha gathered wooden clothespins to make a toy shooter while neighbor Klavdia Viktorovna shouted warnings from her doorway. Meanwhile, at Ivan Samsonov's flat, Nina finds her depressed husband drinking cold vodka alone, having completely given up on his mayoral campaign."
STORY = [
    ("samson", "Вот хорошая ты баба. Холодная.", "You are a good woman. Cold.", [(305, 'Вот хорошая ты баба'), (306, 'Холодная')], "combined cues 305-306"),
    ("samson", "В смысле, водка хорошая.", "I mean, the vodka is good.", [(307, 'В смысле, водка')], "added хорошая"),
    ("nina", "Какие у тебя планы?", "What are your plans?", [(308, 'Какие планы')], "added у тебя"),
    ("samson", "Пить буду. Дома сидеть.", "I'll be drinking. Sitting at home.", [(310, 'Сбухиваться буду')], "cleaned slang cue 310"),
    ("nina", "Гениальные планы! Очень полезные.", "Brilliant plans! Very useful.", [(311, 'Гениальные планы')], "added sarcastic remark"),
    ("samson", "А у тебя другие предложения есть?", "Do you have other suggestions?", [(312, 'У тебя есть другие предложения')], "added А and word order"),
    ("nina", "Успокоить жену! Подготовиться и поехать на дебаты.", "Calm your wife down! Get ready and go to the debate.", [(313, 'успокоить жену'), (315, 'подготовиться и поехать на дебаты')], "combined cues 313 and 315"),
    ("nina", "Не зря в народе говорят.", "Not for nothing people say it.", [(318, 'Не зря, конечно, говорят')], "adapted cue 318"),
    ("nina", "Яблоко от яблони недалеко падает!", "The apple doesn't fall far from the tree!", [(319, 'Яблоко от яблони')], "completed proverb"),
    ("samson", "Что ты такое говоришь?", "What are you talking about?", [(320, 'Чего?')], "expanded cue 320"),
    ("nina", "Твой дед в войну родину предал.", "Your grandfather betrayed his country in the war.", [(321, 'Твой дед родину предал')], "added в войну"),
    ("nina", "А ты сейчас свою семью предаёшь!", "And you are betraying your family right now!", [(322, 'Ты сейчас свою семью предаешь')], "added А and punctuation"),
    ("samson", "Не надо мне мораль читать!", "Don't lecture me on morals!", [(324, 'не надо мне только мораль читать')], "shortened cue 324"),
    ("nina", "Твой дед полицаем стал из страха.", "Your grandfather became a collaborator out of fear.", [(326, 'Твой дед'), (326, 'полицаем стал')], "adapted cue 326"),
    ("nina", "А ты алкоголиком становишься. Счастливо!", "And you are becoming an alcoholic. Goodbye!", [(327, 'алкоголиком становишься'), (332, 'Счастливо')], "combined cues 327 and 332"),
]
OPENER = "Let's unpack the bitter confrontation between Nina and her defeated husband."
WALK = [
    (0, 'Холодная.', "'Cold.' Samsonov makes a drunken joke, comparing the chilled vodka to a woman."),
    (1, None, "'I mean, the vodka is good.' He clarifies his clumsy words with a sigh."),
    (2, None, "'What are your plans?' Nina demands to know if he has any intention of fighting back."),
    (3, None, "'I will be drinking. Sitting at home.' He admits his total defeat and surrender."),
    (4, None, "'Brilliant plans! Very useful.' Nina uses biting sarcasm to shake him awake."),
    (6, None, "'Calm your wife down! Get ready and go to the debate.' She lays out a clear path forward."),
    (8, None, "'The apple does not fall far from the tree!' Nina invokes the famous proverb about family flaws."),
    (10, None, "'Your grandfather betrayed his country in the war.' The historical rumor stings Samsonov deeply."),
    (11, None, "'And you are betraying your family right now!' She links the grandfather's failure to his drinking."),
    (12, None, "'Do not lecture me on morals!' The colloquial phrase means to preach or scold."),
    (14, None, "'And you are becoming an alcoholic. Goodbye!' Nina turns on her heel and leaves the room."),
]
TRANSITION = "Now listen to the argument between Nina and Ivan again."
OUTRO = "Disgusted by Ivan's self-pity and drinking, Nina storms out into the chilly night. See you next time!"
CLOSING = ("nina", "Пока!")
