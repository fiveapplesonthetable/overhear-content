# Authoring module for kukhnya-s01e05-scene-10.
ID = 'kukhnya-s01e05-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 10
TITLE = 'Тайное поручение  (A Secret Errand)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "During a hectic evening service at Claude Monet, Chef Viktor Barinov pulls junior cook Max aside. Desperate for a drink during his demanding shift, Barinov orders Max to secretly fetch a bottle of cognac from the bar. Let's listen to their conspiratorial dialogue in Russian first."
OPENER = "Let's examine how Chef Barinov issues disguised commands to his cook."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Now you know how Barinov disguises his drinking habits as culinary tasks. Listen for these phrases next time you watch the episode. Next time you watch the episode, listen for the Russian expressions for 'bartender' and 'to run' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Слушай, Огузок, подойди ко мне.', 'Listen, Oguzok, come here to me.', [(141, 'Слушай, Агузик')], ''),
    ('max', 'Да, шеф! Что нужно сделать?', 'Yes, chef! What needs to be done?', [], ''),
    ('barinov', 'Сходи в бар и принеси коньяк.', 'Go to the bar and bring cognac.', [(141, 'ходи в бар, принеси коньяк')], ''),
    ('max', 'Какой именно коньяк вам нужен?', 'Which cognac exactly do you need?', [], ''),
    ('barinov', 'Я написал название на этой бумажке.', 'I wrote the name on this piece of paper.', [(142, 'Я для идиотов тут название написал')], ''),
    ('max', 'А если кто-то заметит меня?', 'And what if someone notices me?', [], ''),
    ('barinov', 'В бар сходи для отвода глаз.', 'Go to the bar to keep up appearances.', [(141, 'бар')], ''),
    ('max', 'А что сказать бармену Косте?', 'And what should I say to bartender Kostya?', [], ''),
    ('barinov', 'Скажи, что это для мясного соуса.', 'Say that this is for meat sauce.', [], ''),
    ('max', 'Понял, сделаю всё быстро и тихо.', 'Understood, I will do everything quickly and quietly.', [], ''),
    ('barinov', 'И фаршируй рыбу жюльеном с лимоном.', 'And stuff the fish with julienne and lemon.', [], ''),
    ('barinov', 'Потом ставь её в горячую духовку.', 'Then put it into the hot oven.', [], ''),
    ('max', 'Слушаюсь, шеф, уже бегу!', "Right away, chef, I'm already running!", [], ''),
]
WALK = [
    (0, None, "'Go to the bar and bring cognac.' Barinov quietly assigns a covert mission to his subordinate."),
    (1, None, "'I wrote the name on this piece of paper.' Barinov provides written instructions to avoid mistakes."),
    (2, None, "'Go to the bar to keep up appearances.' Barinov reminds him to act naturally so nobody suspects anything."),
    (3, None, "'And stuff the fish with julienne and lemon.' Barinov throws in a legitimate cooking task as a cover story."),
]
