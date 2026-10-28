# Authoring module for kukhnya-s05e19-scene-14.
ID = 'kukhnya-s05e19-scene-14'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 19
SCENE = 14
TITLE = 'Проверка ФМС и французский блокнот  (The Immigration Raid and the French Notebook)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'inspector': 'Инспектор', 'katya': 'Катя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.19'
SOURCE_FILE = 'sources/kukhnya/s05/e19.ru.srt'
INTRO = 'Just as Katya arrives at the botanical garden expecting her hat back, immigration officers raid the park and detain her by mistake. Back in the kitchen, Fedya and Senya puzzle over the French notebook.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Excited that a guest ordered the chef's signature dish, Max decides to cook his own creation instead of Victor's recipe. See you next time!"
CLOSING = ('katya', 'До свидания!')
STORY = [
    ('katya', 'Здравствуйте, и что мне делать дальше?', 'Hello, and what am I supposed to do next?', [(245, 'Здравствуйте. Ну и что мне делать дальше')], 'adapted'),
    ('katya', 'Скажите, у кого следующая подсказка?', 'Tell me, who has the next clue?', [(246, 'У кого подсказка')], 'adapted'),
    ('inspector', 'ФМС, всем оставаться на своих местах!', 'Migration Service, everyone stay in your places!', [(248, 'ФМС! Всем оставаться на своих местах')], 'adapted'),
    ('katya', 'Ничего себе, как у вас всё продумано.', 'Wow, how thoroughly you have thought everything through.', [(250, 'Ничего себе у вас всё продумано')], 'adapted'),
    ('inspector', 'Дальше будет суд за нелегалов.', 'Next there will be a court hearing for illegal workers.', [(251, 'Дальше суд'), (252, 'для нелегалов')], 'adapted'),
    ('katya', 'Вы сейчас шутите, вам это смешно?', 'Are you joking right now, is this funny to you?', [(253, 'Шутите? Вам смешно')], 'adapted'),
    ('katya', 'Алло, Никита, что здесь вообще происходит?', 'Hello, Nikita, what on earth is going on here?', [(254, 'Алло, Никита, а что происходит')], 'adapted'),
    ('senya', 'Что ты там хочешь прочитать в блокноте?', 'What are you trying to read in that notebook?', [(255, 'Что ты там хочешь')], 'adapted'),
    ('senya', 'Там же всё написано по-французски.', 'Everything in there is written in French.', [(255, 'Там все по-французски')], 'adapted'),
    ('senya', 'А вдруг этот гость — иностранный шпион?', 'And what if this guest is a foreign spy?', [(256, 'А вдруг он')], 'adapted'),
    ('katya', 'Ребята, в зале блюдо от шефа заказали!', "Guys, someone in the dining room ordered the chef's special!", [(258, 'блюдо от шефа заказали')], 'adapted'),
    ('senya', 'Класс, посмотрим, что приготовит наш новый шеф.', "Great, let's see what our new chef will cook.", [(259, 'Класс')], 'adapted'),
]
WALK = [
    (0, None, '\'Hello, and what am I supposed to do next?\' Replying directly in the exchange, Katya puts the question word "chto" right at the start so the inspector hears the focus immediately.'),
    (1, None, "'Tell me, who has the next clue?' Katya checks frankly before the inspector can change the subject."),
    (2, None, '\'Migration Service, everyone stay in your places!\' Emphasizing the migration service at once, the inspector leans on "ostavatsya" ("to stay, to remain") to give the whole sentence its punch.'),
    (3, None, "'Wow, how thoroughly you have thought everything through.' Katya replies decisively with a sigh, leaving no doubt about where she stands."),
    (4, None, "'Next there will be a court hearing for illegal workers.' The inspector jumps in honestly with a sigh, bringing things back to earth after the buildup."),
    (5, None, '\'Are you joking right now, is this funny to you?\' Katya fires back warmly before the inspector and centers the thought on "shutite" ("are joking", from "shutit") without wasting a word.'),
    (6, None, '\'Hello, Nikita, what on earth is going on here?\' Answering earnestly in the exchange, Katya drops in "voobshche" ("in general, altogether") to sum up the whole situation at once.'),
    (7, None, "'What are you trying to read in that notebook?' Senya wonders openly how Katya expects that to work in practice."),
    (8, None, '\'Everything in there is written in French.\' Senya steps in openly before Katya and lands on "po-frantsuzski" ("in French") as the key everyday word here.'),
    (9, None, '\'And what if this guest is a foreign spy?\' Pointing out how foreign things are to Katya, Senya links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (10, None, "'Guys, someone in the dining room ordered the chef's special!' Katya counters calmly facing Senya, watching Senya's face to see how the news lands."),
    (11, None, '\'Great, let\'s see what our new chef will cook.\' Addressing the cool before Katya, Senya chooses "prigotovit" ("makes, cooks") so Katya gets the point right away.'),
]
