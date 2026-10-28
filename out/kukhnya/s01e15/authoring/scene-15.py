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
INTRO = 'Lyova has just poured out an apology to the sleeping Barinov. Now Barinov opens his eyes. Here is the scene in Russian first.'
OPENER = "Let's go back through this one gently."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Barinov forgives Lyova and falls asleep again. When you watch, see whether he really has been listening the whole time. Talk soon.'
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
    (0, None, "'Viktor Petrovich, are you not sleeping?' A negative question, 'vy ne spite', is how Russians ask 'are you awake?'. 'Vy' is the polite you, and the verb ends in 'ite'."),
    (1, None, "'I heard everything, Lyova.' 'Slyshal' means 'heard', and it's a man's form. 'Vsyo' is 'everything'."),
    (2, None, "'Did you hear my words?' 'Slova' is the plural of 'slovo', 'word'. Lyova is nervous."),
    (3, None, "'I almost had a stroke.' 'Menya khvatil udar' is literally 'a blow grabbed me', which is the Russian idiom for a stroke. 'Chut ne' is 'almost'."),
    (4, None, "'Your speech was very fiery.' 'Plamenny' comes from 'plamya', flame, so a fiery speech is a flamy one. 'Rech' is feminine, so the word ends in 'oy'."),
    (5, None, "'I spoke from a pure heart.' 'Ot chistogo serdtsa' is 'from a pure heart', and it's a fixed phrase. English says 'from the bottom of my heart'."),
    (6, None, "'This is already the second heart attack today.' 'Vtoroy' is 'second', and 'za den' is 'in a day'. The joke is that his heart is behaving worse than it ever did."),
    (7, None, "'So, you are not angry at me?' 'Zlitsya na' is 'to be angry at', and it takes 'na', 'on'. 'Znachit' at the start means 'so'."),
    (8, None, "'No, I am not angry at you.' Barinov repeats the question as an answer. The same 'na' comes before 'tebya'."),
    (9, None, "'Will you stay to live with us?' 'Ostanetes zhit' is 'will you stay to live', two verbs together. 'U nas' is 'at our place'."),
    (10, None, "'Yes, I will stay here.' 'Ostanus'' is 'I will stay', and it has the 'sya' of 'stay yourself'. Barinov agrees in four words."),
    (11, None, "'I am very glad to hear this.' 'Rad' is 'glad', in the man's form. 'Slyshat' is 'to hear', and it follows directly."),
    (12, None, "'And now let me sleep.' 'Day pospat' is again 'give me to sleep'. The 'po' keeps the sleep short and sweet."),
]
