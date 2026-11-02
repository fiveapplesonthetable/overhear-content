# Authoring module for kukhnya-s01e05-scene-14.
ID = 'kukhnya-s01e05-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 14
TITLE = 'Разговор в кладовой  (Talk in the Pantry)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Back at the Claude Monet bar, Nastya goes ahead with Sasha's plan. She finds Kostya, the bartender, and asks him to come somewhere quiet so she can ask him something. Kostya has liked her for ages and can hardly believe his luck. Here it is in Russian."
OPENER = "Let's go back. They're both nervous, and you can hear it in the short questions."
TRANSITION = 'By now it should sound clearer.'
OUTRO = "Kostya finally gets to say that he likes her a lot. It's one of the most useful sentences in Russian, and now you've heard it in a happy moment."
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('nastya', 'Костя, привет, ты сейчас сильно занят?', 'Kostya, hi, are you very busy right now?', [(175, 'Костя, привет'), (177, 'Ты занят')], ""),
    ('kostya', 'Привет, Настя, нет, я совсем свободен.', 'Hi, Nastya, no, I am completely free.', [(176, 'Привет'), (177, 'Нет, да')], ""),
    ('nastya', 'Тогда пойдём со мной в тихую комнату.', 'Then come with me into the quiet room.', [(178, 'Тогда пойдем')], ""),
    ('kostya', 'Подожди секунду, куда именно мы идём?', 'Wait a second, where exactly are we going?', [(179, 'Подожди')], ""),
    ('nastya', 'Я давно хотела серьёзно спросить тебя.', 'I wanted to ask you seriously for a long time.', [(180, 'чтобы мы с тобой')], ""),
    ('kostya', 'Я с удовольствием выслушаю тебя сейчас.', 'I will listen to you with pleasure now.', [(182, 'Да, да')], ""),
    ('nastya', 'Ты хочешь, чтобы мы начали встречаться?', 'Do you want us to start dating?', [(180, 'Ты хочешь, чтобы мы с тобой')], ""),
    ('kostya', 'Настя, я просто немного растерялся.', 'Nastya, I just got a little confused.', [(182, 'В смысле')], ""),
    ('nastya', 'Или ты совсем не хочешь этого?', 'Or do you not want this at all?', [(181, 'Ты не хочешь')], ""),
    ('kostya', 'Конечно, хочу, ты мне очень нравишься!', 'Of course I want to, I like you very much!', [(182, 'В смысле, хочу')], ""),
    ('nastya', 'Я очень рада это услышать от тебя.', 'I am very glad to hear this from you.', [(184, 'На всякий случай')], ""),
    ('kostya', 'Теперь нам пора возвращаться к гостям.', 'Now it is time for us to return to the guests.', [(185, 'два блюда')], ""),
]
WALK = [
    (0, None, [
        "'Kostya, hi, are you very busy right now?' indicates 'busy' for a man; for ",
        ('nastya', 'занят?'),
        " a man; for a woman, you'd use a different ending. ",
        ('nastya', 'сильно'),
        ", literally 'strongly', often just is used for 'very'."
    ]),
    (1, None, [
        "'Hi, Nastya, no, I am completely free.' , 'completely', is the term that ",
        ('kostya', 'совсем'),
        " makes 'not at all' when paired with a negative. ",
        ('kostya', 'свободен.'),
        ", 'free', is the man's form."
    ]),
    (2, None, [
        "'Then come with me into the quiet room.' acts as 'let's go', taking a ",
        ('nastya', 'пойдём'),
        " cts as 'let's go', taking a 'we' ending. ",
        ('nastya', 'в'),
        ('nastya', 'тихую'),
        ('nastya', 'комнату.'),
        " represents a direction, causing both following terms to take matching endings."
    ]),
    (3, None, [
        "'Wait a second, where exactly are we going?' questions 'where to', expressing movement. If ",
        ('kostya', 'куда'),
        ' you simply need to know location, a different word is used.'
    ]),
    (4, None, [
        "'I wanted to ask you seriously for a long time.' The phrase ",
        ('nastya', 'давно'),
        ('nastya', 'хотела'),
        ", meaning 'long wanted', covers 'I've been wanting for a long time'. The second word carries a feminine ending."
    ]),
    (5, None, [
        "'I will listen to you with pleasure now.' The expression ",
        ('kostya', 'с'),
        ('kostya', 'удовольствием'),
        ", 'with pleasure', serves as a polite yes to any offer. ",
        ('kostya', 'выслушаю'),
        " is translated as 'hear out', meaning listening all the way through."
    ]),
    (6, None, [
        "'Do you want us to start dating?' Here, ",
        ('nastya', 'хочешь,'),
        ('nastya', 'чтобы'),
        ('nastya', 'мы'),
        ('nastya', 'начали'),
        " literally means 'you want so-that we started', with the action placed in the past following ",
        ('nastya', 'чтобы'),
        ". And ",
        ('nastya', 'встречаться?'),
        " appears as the dating verb once more."
    ]),
    (7, None, [
        "'Nastya, I just got a little confused.' The term ",
        ('kostya', 'растерялся.'),
        " contains the root for 'to lose' along with a reflexive ending, yielding roughly 'I lost myself'. The phrase ",
        ('kostya', 'просто'),
        ('kostya', 'немного'),
        ", meaning 'just a little', softens it."
    ]),
    (8, None, [
        "'Or do you not want this at all?' After the negation ",
        ('nastya', 'не'),
        ('nastya', 'хочешь'),
        ", the word for 'this' changes to ",
        ('nastya', 'этого?'),
        " It's the same structural shift seen when negating other direct objects."
    ]),
    (9, None, [
        "'Of course I want to, I like you very much!' on its own expresses 'I want ",
        ('kostya', 'хочу,'),
        " to'. Following that, ",
        ('kostya', 'ты'),
        ('kostya', 'мне'),
        ('kostya', 'очень'),
        ('kostya', 'нравишься!'),
        ", literally meaning 'you to me are very pleasing', gives a clear 'I like you very much'."
    ]),
    (10, None, [
        "'I am very glad to hear this from you.' shows the feminine version of 'glad'; ",
        ('nastya', 'рада'),
        ' a man would say it without the final vowel. The chunk ',
        ('nastya', 'от'),
        ('nastya', 'тебя.'),
        ", meaning 'from you', relies on ",
        ('nastya', 'от'),
        ", which requires the following word to take the 'of' form."
    ]),
    (11, None, [
        "'Now it is time for us to return to the guests.' , meaning 'it's time', is followed ",
        ('kostya', 'пора'),
        ' by an unconjugated verb. The destination ',
        ('kostya', 'к'),
        ('kostya', 'гостям.'),
        ", 'to the guests', pairs ",
        ('kostya', 'к'),
        " with a plural ending on the noun."
    ]),
]
