# Authoring module for kukhnya-s01e13-scene-20.
ID = 'kukhnya-s01e13-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 20
TITLE = 'Разоблачение  (The Exposure)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = 'Vika told the restaurant owner that her trip was cancelled, and Nagiyev has checked. She comes into his office, and he is smiling. Hear the scene in Russian first.'
OPENER = "Nagiyev's questions, one at a time."
TRANSITION = 'And now the whole interview, uninterrupted.'
OUTRO = 'Nagiyev has caught her, politely. He never raises his voice. Speak soon.'
CLOSING = ('nagiyev', 'Пока!')
STORY = [
    ('vika', 'Доброе утро, Дмитрий Владимирович.', 'Good morning, Dmitry heovich.', [(280, 'дмитрий')], ''),
    ('nagiyev', 'Пожалуй, добрый день, Вика.', 'I would say it is afternoon, Vika.', [], ''),
    ('nagiyev', 'Почему, Вик, на выставку не улетели?', "Why didn't you fly out to the exhibition?", [(280, 'вик')], ''),
    ('vika', 'Так ее же отменили.', 'It was cancelled.', [(283, 'так')], ''),
    ('vika', 'Я звонила своим друзьям.', 'I called my contacts.', [(273, 'звонила')], ''),
    ('nagiyev', 'Вам же звонил там какой-то предприниматель.', 'Some businessman called you, right?', [(274, 'вам')], ''),
    ('vika', 'Какой?', 'Who?', [(274, 'какой')], ''),
    ('vika', 'Да, звонил.', 'Yeah, he called.', [(274, 'звонил')], ''),
    ('nagiyev', 'Сейчас скажем.', "Let's see.", [(276, 'сейчас')], ''),
    ('nagiyev', 'Александр Дель Пьеро.', 'Alexander Del Piero.', [(276, 'александр')], ''),
    ('nagiyev', 'Сказал, что выставка отменяется.', 'He said the exhibition was cancelled.', [(277, 'сказал')], ''),
    ('nagiyev', 'С московского телефона звонят?', 'Was it a call from a Moscow number?', [(278, 'московского')], ''),
    ('nagiyev', 'Да, вот номер.', 'Yeah, here is the number.', [(279, 'вот')], ''),
    ('nagiyev', 'Набирайте.', 'Call it.', [(279, 'набирайте')], ''),
    ('nagiyev', 'Я бы вас уволил.', 'I would have fired you.', [(281, 'вас')], ''),
    ('nagiyev', 'А так вы просто летите на выставку.', 'As it is, you are going to the exhibition.', [(283, 'так')], ''),
    ('nagiyev', 'И за свой счет.', 'And at your own expense.', [(283, 'свой')], ''),
]
WALK = [
    (0, None, ["'Good morning, Dmitry heovich.' First name plus father's name, as always for the boss. ", ('vika', 'Владимирович'), ' means son of he.']),
    (1, None, ["'I would say it is afternoon, Vika.' Let us analyze the speech: ", ('nagiyev', 'добрый'), ('nagiyev', 'день'), ' is good day, in a masculine ending, since day is masculine. ', ('nagiyev', 'Пожалуй'), ' is perhaps or I would say, a soft way to correct her.']),
    (2, None, ["'Why didn't you fly out to the exhibition?' We will consider the words: ", ('nagiyev', 'Вик'), ' is Vika with the last vowel dropped, the casual way to call someone. ', ('nagiyev', 'улетели'), ' is flew off, and ', ('nagiyev', 'на'), ('nagiyev', 'выставку'), ' is to the exhibition.']),
    (3, None, ["'It was cancelled.' Let's look at the speech: ", ('vika', 'Так'), ' starts it like well. ', ('vika', 'ее'), ' is it, but a feminine one, because exhibition is. ', ('vika', 'отменили'), ' means they cancelled, with nobody named.']),
    (4, None, ["'I called my contacts.' Now we can examine the words: ", ('vika', 'звонила'), ' has the ending of a woman. To my friends is ', ('vika', 'своим'), ('vika', 'друзьям'), '.']),
    (5, None, ["'Some businessman called you, right?' To you, ", ('nagiyev', 'Вам'), ', carries a polite plural. ', ('nagiyev', 'предприниматель'), ' comes from to undertake, much as entrepreneur does in French.']),
    (6, None, ["'Who?' It is just ", ('vika', 'Какой'), ', which one, in the masculine because it asks about a man. A short question that buys time.']),
    (7, None, ["'Yeah, he called.' We can inspect the speech: ", ('vika', 'звонил'), " is phoned, in a man's form. Vika is cornered and confirms it."]),
    (8, None, ["'Let's see.' Let us inspect the words: ", ('nagiyev', 'Сейчас'), ('nagiyev', 'скажем'), ' means now we will say. Nagiyev uses we, as bosses often do.']),
    (9, None, ["'Alexander Del Piero.' The surname belongs to a famous Italian footballer. Russians spell foreign names the way they sound, so on the page it is in Russian letters, ", ('nagiyev', 'Александр'), ('nagiyev', 'Дель'), ('nagiyev', 'Пьеро'), '.']),
    (10, None, ["'He said the exhibition was cancelled.' A man's past tense gets a masculine ending, so ", ('nagiyev', 'Сказал'), '. The exhibition cancels itself, which is why the action ends in a self ending.']),
    (11, None, ["'Was it a call from a Moscow number?' From a Moscow phone is ", ('nagiyev', 'С'), ('nagiyev', 'московского'), ('nagiyev', 'телефона'), ': of Moscow takes a special ending after from. ', ('nagiyev', 'звонят'), ' is they call, with nobody specified.']),
    (12, None, ["'Yeah, here is the number.' Let's consider the phrase: ", ('nagiyev', 'вот'), ' is here is, what you say when you hand something over.']),
    (13, None, ["'Call it.' Now let's consider the words: ", ('nagiyev', 'Набирайте'), ' is dial, for a number. It is the polite plural.']),
    (14, None, ["'I would have fired you.' The small word ", ('nagiyev', 'бы'), ' turns I fired into I would fire. ', ('nagiyev', 'вас'), ' is you, polite.']),
    (15, None, ["'As it is, you are going to the exhibition.' Let us inspect this part: ", ('nagiyev', 'А'), ('nagiyev', 'так'), ' is but as it is, so otherwise. ', ('nagiyev', 'летите'), ' is you fly, and Russians use the present for you are going.']),
    (16, None, ["'And at your own expense.' We will look at this part: ", ('nagiyev', 'за'), ('nagiyev', 'свой'), ('nagiyev', 'счет'), ", saying for one's own account, is familiar Russian for at your own expense."]),
]
