# Authoring module for kukhnya-s01e03-scene-04.
ID = 'kukhnya-s01e03-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = 'Опасный разговор  (A Dangerous Conversation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vadim': 'Вадим'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "A rough-looking man stops Max outside Claude Monet. His name is Vadim, he is a prosecutor, and he wants to know who Vika is seeing these days. Max is not enjoying this. Here's the conversation in Russian first."
OPENER = "Let's go through the threat."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max promises that Vika is seeing nobody, and Vadim does not look convinced. Take away "ni s kem ne", the double negative with a word wedged in the middle.'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('vadim', 'Слышь, малой, есть разговор.', 'Listen, kid, I want to talk.', [(132, 'разговор есть')], ''),
    ('max', 'Что вам нужно?', 'What do you need?', [], ''),
    ('vadim', 'Тут у вас работает Вика.', 'Vika works here with you.', [(133, 'Тут у вас работает Вика')], ''),
    ('vadim', 'Виктория Сергеевна.', 'Viktoria Sergeyevna.', [(133, 'Виктория Сергеевна')], ''),
    ('vadim', 'С кем она тут встречается?', 'Who is she seeing here?', [(134, 'с кем она у вас тут встречается')], ''),
    ('vadim', 'Ну, почему молчим?', 'Well, why are we silent?', [], ''),
    ('max', 'Почему я должен отвечать?', 'Why should I answer?', [(136, 'я тебе должен отвечать')], ''),
    ('vadim', 'Не хочешь отвечать здесь?', "Don't want to answer here?", [(137, 'Не хочешь отвечать здесь')], ''),
    ('vadim', 'Ответишь у меня в прокуратуре.', "You'll answer in my prosecutor's office.", [(138, 'у меня в прокуратуре')], ''),
    ('vadim', 'Ты меня понял?', 'Did you understand me?', [(139, 'Понял')], ''),
    ('max', 'Понял, всё понял.', 'Understood, understood everything.', [(140, 'Понял, понял')], ''),
    ('max', 'Она ни с кем не встречается.', 'She is not seeing anyone.', [(141, 'она здесь ни с кем не встречается')], ''),
    ('vadim', 'Ну, смотри у меня.', 'Well, you watch yourself.', [(142, 'Ну, смотри')], ''),
    ('max', 'Надо срочно предупредить всех.', 'Must urgently warn everyone.', [(160, 'Надо предупредить')], ''),
]
WALK = [
    (0, None, '\'Listen, kid, I want to talk.\' This is street Russian. The first word is a clipped "hey, listen", and "maloy", kid, comes from "small". "There is a conversation" is how he says he wants a word.'),
    (1, None, '\'What do you need?\' Max uses the polite "you" with a stranger, and he is wary. The shape is "what to you needed".'),
    (2, None, '\'Vika works here with you.\' "Here at you" is Russian for "where you work". Vadim talks like a policeman, short and flat.'),
    (3, None, "'Viktoria Sergeyevna.' He uses her full name and father's name, which makes it sound like a police file."),
    (4, None, '\'Who is she seeing here?\' The word for "meet" turns into "date" when it has "with" after it, so it\'s the normal way to say you\'re seeing someone.'),
    (5, None, '\'Well, why are we silent?\' Vadim says "we are silent" when he means "you". It\'s the patronising "we" Russians use for scolding children and suspects.'),
    (6, None, '\'Why should I answer?\' The word for "should" has a masculine ending, because Max is a man. "Answer" is from "otvet", an answer.'),
    (7, None, '\'Don\'t want to answer here?\' Vadim switches to the friendly "you", which sounds rude from a stranger. It\'s a way of putting Max in his place.'),
    (8, None, '\'You\'ll answer in my prosecutor\'s office.\' "At me in the prosecutor\'s office" is how he says "my office". The future is a threat dressed as a statement.'),
    (9, None, '\'Did you understand me?\' The answer will end in "-l", because Max is a man. Vadim keeps using the friendly "you", which is rude here.'),
    (10, None, '\'Understood, understood everything.\' Max repeats "understood" and adds "everything". Fear makes him say it twice.'),
    (11, None, '\'She is not seeing anyone.\' The pieces of "nobody" come apart here: "ni" and "kem" have "with" wedged between them. "Not" follows, so it\'s a double negative with a preposition in the middle.'),
    (12, None, '\'Well, you watch yourself.\' Literally "look at me", but with that tone it\'s a threat meaning "watch your step".'),
    (13, None, '\'Must urgently warn everyone.\' "Nado" is the one-word "must", and "everyone" takes the object ending. Max plans to spread the news.'),
]
