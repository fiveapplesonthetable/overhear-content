# Authoring module for kukhnya-s01e15-scene-15.
ID = 'kukhnya-s01e15-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 15
TITLE = 'Второй инфаркт  (A Second Heart Attack)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = 'Lyova has just poured out an apology to the sleeping Barinov. Now Barinov opens his eyes. The Russian comes first.'
OPENER = 'Gently, once more.'
TRANSITION = 'Now the whole scene again.'
OUTRO = "Barinov forgives Lyova and falls asleep again. Was he really listening the whole time? Bye for now."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('lyova', 'Виктор Петрович, вы не спите?', 'Viktor Petrovich, are you not sleeping?', [(329, 'Лёва, меня чуть не хватил удар от твоей пламенной речи второй за день.')], ''),
    ('barinov', 'Я всё слышал, Лёва.', 'I heard everything, Lyova.', [], ''),
    ('lyova', 'Вы слышали мои слова?', 'Did you hear my words?', [], ''),
    ('barinov', 'Меня чуть не хватил удар.', 'I almost had a stroke.', [], ''),
    ('barinov', 'Твоя речь была очень пламенной.', 'Your speech was very fiery.', [], ''),
    ('lyova', 'Я говорил от чистого сердца.', 'I spoke from a pure heart.', [], ''),
    ('barinov', 'Это уже второй инфаркт за день.', 'This is already the second heart attack today.', [], ''),
    ('lyova', 'Значит, вы на меня не злитесь?', 'So, you are not angry at me?', [], ''),
    ('barinov', 'Нет, я не злюсь на тебя.', 'No, I am not angry at you.', [], ''),
    ('lyova', 'Вы останетесь жить у нас?', 'Will you stay to live with us?', [], ''),
    ('barinov', 'Да, я останусь здесь.', 'Yes, I will stay here.', [], ''),
    ('lyova', 'Я очень рад это слышать.', 'I am very glad to hear this.', [], ''),
    ('barinov', 'А теперь дай мне поспать.', 'And now let me sleep.', [], ''),
]
WALK = [
    (0, None, ["'Viktor Petrovich, are you not sleeping?' A negative question using ", ('lyova', 'не'), ('lyova', 'спите'), " is how you ask 'are you awake?'. The verb has a formal ending."]),
    (1, None, ["'I heard everything, Lyova.' The verb ", ('barinov', 'слышал'), ' has the past tense ending for a man. The term ', ('barinov', 'всё'), " means 'everything'."]),
    (2, None, ["'Did you hear my words?' The noun ", ('lyova', 'слова'), " is the plural of 'word'. The verb ", ('lyova', 'слышали'), " has the ending that goes with the polite form of 'you'."]),
    (3, None, ["'I almost had a stroke.' The expression ", ('barinov', 'хватил'), ('barinov', 'удар'), " means 'a blow grabbed', which is an idiom for a stroke. The expression ", ('barinov', 'чуть'), ('barinov', 'не'), " means 'almost'."]),
    (4, None, ["'Your speech was very fiery.' The word ", ('barinov', 'пламенной'), ' comes from the noun meaning flame, so it means fiery. The word ', ('barinov', 'речь'), ' is feminine, so the adjective gets a feminine ending.']),
    (5, None, ["'I spoke from a pure heart.' We will look at the words: ", ('lyova', 'от'), ('lyova', 'чистого'), ('lyova', 'сердца'), " is fixed. English says 'from the bottom of my heart'."]),
    (6, None, ["'This is already the second heart attack today.' The term ", ('barinov', 'инфаркт'), ' is the medical term for a heart attack. The expression ', ('barinov', 'за'), ('barinov', 'день'), " means 'in one day'."]),
    (7, None, ["'So, you are not angry at me?' To say 'angry at' uses a word meaning 'on', so the phrasing is 'angry on me' using ", ('lyova', 'на'), ('lyova', 'меня'), '. The term ', ('lyova', 'Значит'), " opens the line to mean 'so'."]),
    (8, None, ["'No, I am not angry at you.' Barinov repeats the question as an answer. The same word comes before 'you' in ", ('barinov', 'на'), ('barinov', 'тебя'), '.']),
    (9, None, ["'Will you stay to live with us?' Let us look at this part: ", ('lyova', 'останетесь'), ('lyova', 'жить'), " means 'will you stay to live', two verbs together. Here we have ", ('lyova', 'у'), ('lyova', 'нас'), " means 'at our place'."]),
    (10, None, ["'Yes, I will stay here.' The verb ", ('barinov', 'останусь'), " has an ending meaning 'stay yourself'. Barinov agrees in four words."]),
    (11, None, ["'I am very glad to hear this.' The term ", ('lyova', 'рад'), " means 'glad'; a woman would add an 'a'. The verb ", ('lyova', 'слышать'), " means 'to hear', and it follows directly."]),
    (12, None, ["'And now let me sleep.' Now let's examine the speech: ", ('barinov', 'дай'), ('barinov', 'мне'), " means 'give me', common speech for 'let me'. The prefix on ", ('barinov', 'поспать'), ' makes it a short sleep, a nap.']),
]
