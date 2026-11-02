# Authoring module for kukhnya-s01e06-scene-23.
ID = 'kukhnya-s01e06-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 23
TITLE = 'Неожиданный поворот  (An Unexpected Turn)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "At Claude Monet the inspection is behind them, and the bill for Rodion's dinner has landed on Max: a month of work for free. He takes it oddly calmly and ends the episode with a speech about life. It's in Russian first."
OPENER = "Let's go through the end of the day. Barinov has the practical lines, and Max has the philosophy."
TRANSITION = "And now Max's speech, all the way through."
OUTRO = 'Max\'s speech is all short Russian sentences about big ideas: "zhizn", life, "trudnosti", difficulties, "sudba", fate. They\'re a good way to practise long thoughts without long words. See you next time.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Огузок, ты оплатишь этот дорогой счёт!', 'Rump, you will pay this expensive bill!', [], ''),
    ('max', 'Шеф, но это очень большие деньги.', 'Chef, but this is very big money.', [(309, 'это')], ''),
    ('barinov', 'Будешь работать бесплатно целый месяц!', 'You will work for free a whole month!', [], ''),
    ('max', 'Жизнь постоянно испытывает нас на прочность.', 'Life is constantly putting us to the test.', [(309, 'жизнь')], ''),
    ('max', 'Кто-то легко справляется с трудностями.', 'Some people easily cope with difficulties.', [], ''),
    ('max', 'А кто-то сразу опускает руки.', 'And some people give up right away.', [(307, '-то нет.')], ''),
    ('max', 'Для одних жизнь — калейдоскоп приключений.', 'For some life is a kaleidoscope of adventures.', [(308, 'Для одних...'), (309, 'Жизнь — это калейдоскоп приключений.')], ''),
    ('max', 'Для других — череда горьких разочарований.', 'For others, a series of bitter disappointments.', [(310, 'Для других — череда разочарований.')], ''),
    ('barinov', 'Хватит мечтать, иди мыть сковородки!', 'Stop daydreaming, go wash the frying pans!', [], ''),
    ('max', 'В любом случае надо быть готовым ко всему.', 'In any case one must be ready for everything.', [(311, 'В'), (312, 'любом случае,')], ''),
    ('max', 'Жизнь учит нас неожиданным поворотам судьбы.', 'Life teaches us unexpected turns of fate.', [(313, 'жизнь учит всегда быть готовым к неожиданному повороту.')], ''),
    ('max', 'Я обязательно справлюсь с этой проблемой.', 'I will definitely deal with this problem.', [], ''),
    ('barinov', 'Вот это правильный настрой для повара!', 'Now that is the right attitude for a cook!', [], ''),
    ('max', 'Завтра меня ждут новые кулинарные победы!', 'Tomorrow new culinary victories await me!', [], ''),
]
WALK = [
    (0, None, ["'Rump, you will pay this expensive bill!' Notice how the chef says ", ('barinov', 'оплатишь'), ' to tell Max he will pay.']),
    (1, None, ["'Chef, but this is very big money.' Pay attention to the word ", ('max', 'деньги'), ' which Russians use for money.']),
    (2, None, ["'You will work for free a whole month!' You can hear the chef say ", ('barinov', 'бесплатно'), ' to mean working for free.']),
    (3, None, ["'Life is constantly putting us to the test.' It is interesting to note that ", ('max', 'прочность'), ' refers to strength or toughness here.']),
    (4, None, ["'Some people easily cope with difficulties.' In this part of the speech, ", ('max', 'справляется'), ' describes coping with a difficult situation.']),
    (5, None, ["'And some people give up right away.' Listen closely to the idiom using ", ('max', 'опускает'), ' which literally means lowering the hands.']),
    (6, None, ["'For some life is a kaleidoscope of adventures.' Max compares life to a colorful ", ('max', 'калейдоскоп'), ' full of unpredictable and exciting events.']),
    (7, None, ["'For others, a series of bitter disappointments.' The contrast continues as he uses ", ('max', 'череда'), ' to describe a long continuous series.']),
    (8, None, ["'Stop daydreaming, go wash the frying pans!' The chef interrupts the deep thoughts, and ", ('barinov', 'Хватит'), ' tells Max that enough is enough.']),
    (9, None, ["'In any case one must be ready for everything.' Moving on, we hear the word ", ('max', 'готовым'), ' expressing the need to be ready.']),
    (10, None, ["'Life teaches us unexpected turns of fate.' Let us look at the word ", ('max', 'поворотам'), ' meaning unexpected turns or life changes.']),
    (11, None, ["'I will definitely deal with this problem.' Max shows his determination by adding ", ('max', 'обязательно'), ' to say he will definitely succeed.']),
    (12, None, ["'Now that is the right attitude for a cook!' It is great to hear that ", ('barinov', 'настрой'), ' means a positive and right attitude.']),
    (13, None, ["'Tomorrow new culinary victories await me!' Finally, the scene ends confidently with ", ('max', 'победы'), ' meaning victories in his culinary journey.']),
]
