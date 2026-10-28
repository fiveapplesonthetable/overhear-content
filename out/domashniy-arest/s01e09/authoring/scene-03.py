# Authoring module for domashniy-arest-s01e09-scene-03.
ID = 'domashniy-arest-s01e09-scene-03'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 9
SCENE = 3
TITLE = 'Ты сам всё проиграл  (You Blew It All Yourself)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'governor': 'Губернатор', 'pasha': 'Паша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.09'
SOURCE_FILE = 'sources/domashniy-arest/s01/e09.ru.dual.srt'
INTRO = "In our last scene, the satirical opening theme song mocked the relentless greed and bribery of provincial politics. Now acting mayor Pasha Osipenko visits veteran party boss Viktor Stepanovich to plead for help against Ivan Samsonov, only to discover that political salvation carries a hefty price tag he can no longer afford. Let's listen in Russian first."
OPENER = "Now let's examine the tense negotiation between the two corrupt politicians line by line. Pasha leans forward anxiously over the senior official's mahogany desk."
TRANSITION = "Now let's listen to the political negotiation in the office again without interruption."
OUTRO = 'Refusing to help for free, Viktor Stepanovich leaves Pasha completely on his own. See you next time!'
CLOSING = ('governor', 'Пока!')
STORY = [
    ('governor', 'Ты же сам всё проиграл!', 'You lost everything yourself!', [(22, 'Ты же сам все')], 'crude просрал softened to проиграл'),
    ('governor', 'Что ты теперь от меня хочешь?', 'What do you want from me now?', [(23, 'теперь от меня-то хочешь')], ''),
    ('pasha', 'Виктор Степанович, помогите мне!', 'Viktor Stepanovich, please help me!', [(24, 'помогите')], 'ASR garble Сарсифов restored'),
    ('governor', 'Как я могу тебе помочь?', 'How can I help you?', [(25, 'как я тебе помогу')], ''),
    ('governor', 'Твой Самсонов прёт как танк!', 'Your Samsonov is charging ahead like a tank!', [(26, 'Твой Самсонов прет как танк')], ''),
    ('pasha', 'Вы же опытный политик.', 'You are an experienced politician, after all.', [(27, 'но вы же опытный политик')], ''),
    ('pasha', 'Вы придумайте что-нибудь, пожалуйста.', 'Think of something, please.', [(28, 'Вы придумайте что-нибудь')], ''),
    ('governor', 'А зачем мне это надо, Паша?', 'And why do I need this, Pasha?', [(29, 'мне все это надо, Паша')], 'crude нафига cleaned to зачем'),
    ('governor', 'В Москве считают, что Самсонов — хороший вариант.', 'In Moscow they think Samsonov is a good option.', [(30, 'В Москве'), (31, 'хороший вариант')], ''),
    ('pasha', 'Нет, он ужасный вариант! Помогите!', 'No, he is a terrible option! Help!', [(32, 'Нет, не хороший вариант'), (33, 'Ну пожалуйста')], ''),
    ('governor', 'Ладно. Три миллиона.', 'Alright. Three million.', [(34, 'Ну ладно'), (35, 'Три')], "'миллиона' added for clarity"),
    ('pasha', 'У меня сейчас нет таких денег.', "I don't have that kind of money right now.", [(38, 'У меня сейчас нету')], ''),
    ('governor', 'Паша, ты церковь или детский дом?', 'Pasha, are you a church or an orphanage?', [(40, 'Паша, ты церковь'), (42, 'Ты детский дом')], ''),
    ('governor', 'Почему я должен помогать бесплатно?', 'Why should I help you for free?', [(47, 'я тебе должен помогать бесплатно')], 'crude хрена omitted'),
]
WALK = [
    (0, None, "'You lost everything yourself!' Viktor Stepanovich puts the blame squarely on Pasha for blowing the election on his own."),
    (1, None, "'What do you want from me now?' He leans back and coldly asks what Pasha expects him to do about the mess now."),
    (2, None, "'Viktor Stepanovich, please help me!' Addressing his boss by name and patronymic, Pasha drops his pride and begs for a lifeline."),
    (3, None, "'How can I help you?' The veteran politician shrugs skeptically, acting as if his hands are tied."),
    (4, None, "'Your Samsonov is charging ahead like a tank!' Comparing Samsonov to a rolling tank captures his unstoppable momentum with the voters."),
    (5, None, "'You are an experienced politician, after all.' Pasha tries to flatter the older man's vanity by appealing to his years of political savvy."),
    (6, None, "'Think of something, please.' Desperate for a way out, he begs the boss to cook up some kind of clever scheme."),
    (7, None, "'And why do I need this, Pasha?' Viktor Stepanovich cuts straight to the point: what is in it for him personally?"),
    (8, None, "'In Moscow they think Samsonov is a good option.' Without naming names, he hints that the powers that be in the capital are already warming to Samsonov."),
    (9, None, "'No, he is a terrible option! Help!' Pasha urgently rejects the idea that his rival could be accepted."),
    (10, None, "'Alright. Three million.' The senior official names his price with blunt brevity."),
    (11, None, "'I don't have that kind of money right now.' Caught short, Pasha has to admit he doesn't have that kind of cash on hand."),
    (12, None, "'Pasha, are you a church or an orphanage?' Viktor Stepanovich sarcastically asks if Pasha is a registered charity."),
    (13, None, "'Why should I help you for free?' Nobody does favors for nothing in this office, and Viktor Stepanovich makes that crystal clear."),
]
