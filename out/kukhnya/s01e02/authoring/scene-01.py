# Authoring module for kukhnya-s01e02-scene-01.
ID = 'kukhnya-s01e02-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = "Две стороны ресторана  (Two Sides of a Restaurant)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
LABELS = {"max": "Макс", "kostya": "Костя"}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "Before Claude Monet opens for the day, the new cook Maksim Lavrov, whom everyone calls Max, jokes with bartender Kostya about the restaurant. Everything is \"on the one hand\" glamorous and \"on the other hand\" not quite. Max ends with a promise to show the chef what he can do. First, the whole conversation in Russian."
OPENER = "Now let's take it slowly, one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "That's how the episode opens. When you watch, keep an ear out for \"on the one hand, on the other hand\": it comes back a minute later in this very episode. See you next time!"
CLOSING = ("max", "Пока!")
STORY = [
    ('max', 'С одной стороны, я работаю в крутом ресторане.', 'On the one hand, I work in a cool restaurant.', [(1, 'С одной стороны, ты устроился в самый крутой')], ''),
    ('kostya', 'А с другой стороны, ты ешь обычные сосиски.', 'And on the other hand, you eat ordinary sausages.', [(2, 'не повлияло на качество твоего питания')], ''),
    ('max', 'Наш шеф готовит самую вкусную еду.', 'Our chef cooks the most delicious food.', [(1, 'самый крутой и вкусный ресторан')], ''),
    ('kostya', 'Но на кухне всегда царит полный хаос.', 'But total chaos always reigns in the kitchen.', [], ''),
    ('max', 'Гости думают, что это самое спокойное место.', 'Guests think this is the most peaceful place.', [(5, 'в самом красивом и спокойном месте')], ''),
    ('kostya', 'Они никогда не узнают правду о нас.', 'They will never know the truth about us.', [(4, 'вы никогда не узнаете, как на самом деле')], ''),
    ('max', 'Каждый клиент считает себя важным человеком.', 'Every customer considers themselves an important person.', [(3, 'вы уважаемые гости элитного ресторана')], ''),
    ('kostya', 'А мы просто наливаем им вино.', 'And we simply pour them wine.', [], ''),
    ('max', 'Работа на кухне очень трудная и нервная.', 'Work in the kitchen is very hard and nerve-wracking.', [], ''),
    ('kostya', 'Зато здесь никогда не бывает скучно!', "On the other hand, it's never boring here!", [], ''),
    ('max', 'Скоро начинается наша утренняя смена.', 'Our morning shift is starting soon.', [], ''),
    ('kostya', 'Тогда готовься к новому рабочему дню!', 'Then prepare for a new workday!', [], ''),
    ('max', 'Я докажу шефу, что умею готовить.', 'I will prove to the chef that I know how to cook.', [], ''),
]
WALK = [
    (0, None, [ "'On the one hand, I work in a cool restaurant.' The term for cool here is ", ("max", "крутом"), ", which literally translates to steep or tough, but they use it to mean awesome just like we do." ]),
    (1, None, [ "'And on the other hand, you eat ordinary sausages.' Here is the other hand, and it's a joke: cool restaurant, cheap sausages. The action word, ", ("kostya", "ешь"), ", translates to you eat in an informal way, said here with a grin." ]),
    (2, None, [ "'Our chef cooks the most delicious food.' Max sounds proud. The describing word, ", ("max", "самую"), ", literally translates to the very, emphasizing how delicious the food is." ]),
    (3, None, [ "'But total chaos always reigns in the kitchen.' Kostya goes straight for the deflating comment. The action word for reigns, ", ("kostya", "царит"), ", is built from the term for emperor, so chaos is literally on the throne." ]),
    (4, None, [ "'Guests think this is the most peaceful place.' These are the guests' illusions. The describing word for peaceful, ", ("max", "спокойное"), ", literally translates to calm or quiet, which is exactly how the dining room looks." ]),
    (5, None, [ "'They will never know the truth about us.' Kostya lets the secret out. The phrase for never know, ", ("kostya", "никогда не узнают"), ", literally translates to never not will know, because the language happily doubles the no." ]),
    (6, None, [ "'Every customer considers themselves an important person.' A small dig at vanity. The action word for considers, ", ("max", "считает"), ", is built from the term for to count, meaning they count themselves as important." ]),
    (7, None, [ "'And we simply pour them wine.' That is Kostya's job in one line. The tiny word for simply, ", ("kostya", "просто"), ", translates to just, and serves as the shrug in the sentence." ]),
    (8, None, [ "'Work in the kitchen is very hard and nerve-wracking.' No joke this time. The term for hard, ", ("max", "трудная"), ", is built from the term for labor, showing plainly how tough the work really is." ]),
    (9, None, [ "'On the other hand, it's never boring here!' Kostya's little word, ", ("kostya", "Зато"), ", literally translates to but on the plus side, and they reach for it all the time to turn a complaint around." ]),
    (10, None, [ "'Our morning shift is starting soon.' The mood shifts here. The action word for is starting, ", ("max", "начинается"), ", literally translates to begins itself." ]),
    (11, None, [ "'Then prepare for a new workday!' A friendly pep talk. The action word, ", ("kostya", "готовься"), ", translates to prepare yourself." ]),
    (12, None, [ "'I will prove to the chef that I know how to cook.' This sets up his first morning. The action word for I will prove, ", ("max", "докажу"), ", is built from the term for to show, framing his promise to the chef." ]),
]
