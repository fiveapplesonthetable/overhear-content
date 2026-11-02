# Authoring module for kukhnya-s01e15-scene-10.
ID = 'kukhnya-s01e15-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 10
TITLE = 'Высокое давление  (High Blood Pressure)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва', 'mama': 'Мама'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "Lyova takes Barinov's blood pressure and is shocked by the reading. Then his mother rings, and Lyova has bad news of his own. Russian first."
OPENER = "Once more, slowly."
TRANSITION = 'And the whole scene, start to finish.'
OUTRO = "Lyova has been demoted, and his mother has a lecture ready instead of sympathy. Talk soon."
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('lyova', 'Сто шестьдесят на девяносто.', 'One hundred sixty over ninety.', [(172, '160 на 90.')], ''),
    ('lyova', 'Виктор Петрович, это не шутки.', 'Viktor Petrovich, this is not a joke.', [(173, 'Виктор Петрович, это не шутки.')], ''),
    ('lyova', 'Такое давление — это очень опасно.', 'Such pressure is very dangerous.', [(174, 'Такое давление — это буревестник инфаркта.')], ''),
    ('barinov', 'Да, всё будет хорошо.', 'Yes, everything will be fine.', [], ''),
    ('lyova', 'Любой стресс и будет плохо.', 'Any stress and it will be bad.', [(175, 'Да, какой-нибудь стресс и…')], ''),
    ('lyova', 'Привет, мама.', 'Hi, Mom.', [(176, 'Привет, мам. Привет.')], ''),
    ('mama', 'Как прошёл твой рабочий день?', 'How was your workday?', [(177, 'Как прошел рабочий день?')], ''),
    ('lyova', 'Нормально, меня уволили.', 'Fine, they fired me.', [(178, 'Нормально. Меня уволили.')], ''),
    ('mama', 'Не уволили, а понизили.', 'Not fired, but demoted.', [(179, 'Не уволили, а понизили в воспитательных целях.')], ''),
    ('lyova', 'Мама, я ни в чём не виноват.', 'Mom, I am not guilty of anything.', [(181, 'За опоздание. Мама, я не виноват.')], ''),
    ('mama', 'Надо уметь отвечать за свои поступки.', 'You must know how to answer for your actions.', [(184, 'Нет-нет-нет. Надо уметь отвечать за свои поступки.')], ''),
    ('lyova', 'Спасибо тебе за поддержку, мама.', 'Thank you for the support, Mom.', [(186, 'Спасибо тебе, мама, за поддержку.')], ''),
]
WALK = [
    (0, None, ["'One hundred sixty over ninety.' We will break down the words: ", ('lyova', 'Сто'), ' is a hundred, ', ('lyova', 'шестьдесят'), " is 'six tens', and ", ('lyova', 'девяносто'), ' is the odd one out for ninety. ', ('lyova', 'на'), " here means 'over', as in a fraction."]),
    (1, None, ["'Viktor Petrovich, this is not a joke.' Russians say 'these are not jokes' in the plural, so ", ('lyova', 'не'), ('lyova', 'шутки'), " means 'not jokes'."]),
    (2, None, ["'Such pressure is very dangerous.' The dash stands for 'is'. ", ('lyova', 'давление'), " comes from the term for 'to press', so blood pressure is seen as a pressing."]),
    (3, None, ["'Yes, everything will be fine.' Barinov waves it off. ", ('barinov', 'всё'), ('barinov', 'будет'), ('barinov', 'хорошо'), ", meaning 'all will be well', is a stock reassurance, and Russian uses ", ('barinov', 'хорошо'), " for 'well', where English says 'fine'."]),
    (4, None, ["'Any stress and it will be bad.' Let's examine this part: ", ('lyova', 'Любой'), " means 'any'. The little ", ('lyova', 'и'), " means 'and then', so the sentence says 'any stress, and then it will be bad'."]),
    (5, None, ["'Hi, Mom.' Now we can analyze the phrase: ", ('lyova', 'Привет'), " supplies the casual 'hi' for family and friends, instead of the formal greeting."]),
    (6, None, ["'How was your workday?' Days 'pass', or ", ('mama', 'прошёл'), ', in Russian. Notice matches the masculine word for day, ', ('mama', 'рабочий'), ('mama', 'день'), ". This is the usual way to ask how someone's day went."]),
    (7, None, ["'Fine, they fired me.' Let us look at this line: ", ('lyova', 'меня'), ('lyova', 'уволили'), " is 'me they fired', without naming the one who did it. ", ('lyova', 'Нормально'), " means 'fine'."]),
    (8, None, ["'Not fired, but demoted.' Now let's break down this line: ", ('mama', 'Не'), ' and ', ('mama', 'а'), " pair up for 'not this, but that'. ", ('mama', 'понизили'), " means 'lowered', so a demotion is seen as a lowering."]),
    (9, None, ["'Mom, I am not guilty of anything.' Let us break down the dialogue: ", ('lyova', 'ни'), ('lyova', 'в'), ('lyova', 'чём'), ('lyova', 'не'), " gives the double negative for 'in nothing not'. ", ('lyova', 'виноват'), " is 'guilty', without an extra ending because Lyova is a man."]),
    (10, None, ["'You must know how to answer for your actions.' After ", ('mama', 'Надо'), " for 'one must', two actions follow in their basic form: ", ('mama', 'уметь'), ' to be able, and ', ('mama', 'отвечать'), ' to answer. ', ('mama', 'отвечать'), ('mama', 'за'), " something is everyday speech for 'take responsibility', and ", ('mama', 'поступки'), ' are deeds you chose to do.']),
    (11, None, ["'Thank you for the support, Mom.' It means 'thanks to you for support': after ", ('lyova', 'за'), ', the term for support takes a special ending in ', ('lyova', 'поддержку'), ". Lyova doesn't sound very grateful."]),
]
