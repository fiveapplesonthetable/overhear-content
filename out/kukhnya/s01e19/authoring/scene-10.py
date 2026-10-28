# Authoring module for kukhnya-s01e19-scene-10.
ID = 'kukhnya-s01e19-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 10
TITLE = 'Подозрительный гость  (A Suspicious Guest)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "Max has spotted Vika in the dining room talking to a stranger who gave her flowers. He can't stand not knowing what they're saying, so he sends Kostya to find out. We'll hear it in Russian first."
OPENER = "Let's go through it a line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Kostya agrees, though not happily, and goes to eavesdrop. 'Drug drugu' means 'each other', and is literally 'friend to friend', which is a pleasing little idiom. See you next time!"
CLOSING = ('kostya', 'До свидания!')
STORY = [
    ('max', 'Костя, посмотри скорее туда.', 'Kostya, look over there quickly.', [(210, 'Ой, Костян')], ''),
    ('kostya', 'Что случилось, Макс?', 'What happened, Max?', [], ''),
    ('max', 'О чём Вика говорит с этим человеком?', 'What is Vika talking about with that person?', [(210, 'а о чем Вика с этим кренделем разговаривает?')], ''),
    ('kostya', 'Макс, я вообще без понятия.', 'Max, I have no idea at all.', [(211, 'Макс, я вообще без понятия.')], ''),
    ('max', 'Этот мужчина подарил ей огромный букет.', 'This man gave her a huge bouquet.', [], ''),
    ('kostya', 'Может быть, это просто постоянный гость.', 'Maybe it is just a regular guest.', [], ''),
    ('max', 'Они слишком мило улыбаются друг другу.', 'They are smiling too sweetly at each other.', [], ''),
    ('kostya', 'Тебе не стоит так сильно переживать.', 'You should not worry so much.', [], ''),
    ('max', 'Костя, подойди поближе к ним.', 'Kostya, get closer to them.', [(212, 'Ну, подойди поближе.')], ''),
    ('kostya', 'Зачем мне подходить к их столику?', 'Why should I approach their table?', [], ''),
    ('max', 'Послушай, что они сейчас обсуждают.', 'Listen to what they are discussing right now.', [], ''),
    ('kostya', 'Ладно, я пойду и узнаю всё.', 'Fine, I will go and find out everything.', [], ''),
    ('max', 'Спасибо, друг, я жду новостей.', 'Thank you, friend, I await the news.', [], ''),
]
WALK = [
    (0, None, "'Kostya, look over there quickly.' The command is casual. 'There' means 'to there', as Max is pointing."),
    (1, None, "'What happened, Max?' 'Happened' ends in 'sya' and is neuter. 'What' sits at the front."),
    (2, None, "'What is Vika talking about with that man?' 'About what' is two words. 'With this man' takes 'im' and 'om' endings."),
    (3, None, "'Max, I have no idea at all.' The phrase is 'without an idea', and it is a set idiom. 'Anyway' is the long word you've already heard."),
    (4, None, "'This man gave her a huge bouquet.' 'Gave as a gift' is one word. 'To her' is the short word 'ey'."),
    (5, None, "'Maybe he's just a regular guest.' A regular guest is a 'constant' guest in Russian. 'Maybe' is built from 'can be'."),
    (6, None, "'They're smiling at each other too sweetly.' 'Each other' is literally 'friend to friend'. 'Too' goes in front of 'sweetly'."),
    (7, None, "'You shouldn't worry so much.' 'It's not worth to you' is the pattern. 'So much' is two small words."),
    (8, None, "'Kostya, go a bit closer to them.' The prefix 'po' makes 'closer' into 'a bit closer'. 'Go up' also has a prefix."),
    (9, None, "'Why should I go up to their table?' 'What for' asks about purpose, not cause. 'To their little table' has a 'u' ending."),
    (10, None, "'Listen to what they're discussing now.' 'Listen' is the finished kind of command. 'They discuss' is plural."),
    (11, None, "'Fine, I'll go and find out everything.' Two verbs side by side with 'and'. 'Find out' is a finished action."),
    (12, None, "'Thanks, friend, I'm waiting for news.' 'News' is plural and takes an 'ey' ending after 'wait for'. 'Friend' is the casual form of address."),
]
