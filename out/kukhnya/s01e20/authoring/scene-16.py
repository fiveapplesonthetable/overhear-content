# Authoring module for kukhnya-s01e20-scene-16.
ID = 'kukhnya-s01e20-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 16
TITLE = 'Старые часы  (Old Watch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'old_man': 'Старик'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = "At Claude Monet, max decides to give his grandfather's watch to a homeless man on the street. Max finds an old homeless man on the street. He decides to give away his grandfather's antique watch because he feels it is time to move on and let go of the past. Let's listen closely to the conversation in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around Old Watch line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The old man gratefully accepts the unexpected gift, leaving Max feeling a sense of relief. Next time you watch the episode, listen for the Russian expressions for 'old man' and 'to be' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Привет, старик.', 'Hello, old man.', [], ''),
    ('old_man', 'Здравствуй.', 'Hello.', [], ''),
    ('max', 'У меня есть часы.', 'I have a watch.', [], ''),
    ('old_man', 'Зачем они мне?', 'Why do I need them?', [], ''),
    ('max', 'Они мне больше не нужны.', 'I do not need them anymore.', [], ''),
    ('old_man', 'Они дорогие?', 'Are they expensive?', [], ''),
    ('max', 'Это старые дедовские часы.', "This is an old grandfather's watch.", [], ''),
    ('max', 'На, держись, старик.', 'Here, take it, old man.', [(286, 'На, держись, старик')], ''),
    ('old_man', 'Спасибо тебе большое.', 'Thank you very much.', [], ''),
    ('max', 'Тебе нужнее.', 'You need it more than I do.', [(287, 'Тебе нужнее')], ''),
    ('old_man', 'Я продам их и куплю еды.', 'I will sell it and buy food.', [], ''),
    ('max', 'Делай с ними что хочешь.', 'Do with them what you want.', [], ''),
    ('max', 'Прощай.', 'Goodbye.', [], ''),
    ('old_man', 'Ты очень добрый человек.', 'You are a very kind person.', [], ''),
]
WALK = [
    (0, None, "'I do not need them anymore.' Max drunkenly decides he has no use for his possessions now."),
    (1, None, "'Here, take it, old man.' Max hands his expensive ring over to a random homeless man."),
    (2, None, "'You need it more than I do.' Max insists the stranger will get more value out of it."),
    (3, None, "'You are a very kind person.' old man sincerely thanks him for the incredible generosity."),
]
