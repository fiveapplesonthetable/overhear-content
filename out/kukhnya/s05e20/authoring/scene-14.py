# Authoring module for kukhnya-s05e20-scene-14.
ID = 'kukhnya-s05e20-scene-14'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 20
SCENE = 14
TITLE = 'Новый шеф-повар «Клод Моне»  (The New Head Chef of Claude Monet)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.20'
SOURCE_FILE = 'sources/kukhnya/s05/e20.ru.srt'
INTRO = 'In the hospital room, Chef Barinov tells Max that he is fired from Restaurant Victor—because Victor convinced Nagiyev that Max is a brilliant young talent who should become the new head chef of Claude Monet!'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Overwhelmed with gratitude, Max hugs Chef Barinov and races to Vika's apartment to share the news. See you next time!"
CLOSING = ('nagiyev', 'До свидания!')
STORY = [
    ('barinov', 'Кстати, формально ты ведь выиграл пари.', 'By the way, technically you won the bet.', [(221, 'Кстати, формально ты же выиграл')], 'adapted'),
    ('barinov', 'Поздравляю тебя, но есть и плохая новость.', 'Congratulations to you, but there is also bad news.', [(223, 'Поздравляю'), (225, 'плохая')], 'adapted'),
    ('barinov', 'С сегодняшнего дня ты у нас уволен.', 'As of today you are fired from our kitchen.', [(225, 'Ты уволен')], 'adapted'),
    ('max', 'Как уволен, почему, ведь это несправедливо!', 'What do you mean fired, why, that is unfair!', [(226, 'Как? Почему'), (227, 'Это несправедливо, шеф')], 'adapted'),
    ('barinov', 'Два крутых повара не могут ужиться на одной кухне.', 'Two great chefs cannot coexist in one kitchen.', [(228, 'Два крутых повара не могут ужиться на одной кухне')], 'adapted'),
    ('barinov', 'Поэтому завтра выходишь шеф-поваром в ресторан «Моне»!', 'So tomorrow you start as head chef at Restaurant Monet!', [(229, 'выходишь шеф-поваром')], 'adapted'),
    ('barinov', 'Через год за ним будут гоняться все рестораны Москвы.', 'In a year every restaurant in Moscow will be chasing after him.', [(234, 'будут гоняться все рестораны Москвы')], 'adapted'),
    ('barinov', 'Потому что он сейчас — это я в молодости.', 'Because right now he is me in my youth.', [(235, 'потому что он – это я в молодости')], 'adapted'),
    ('barinov', 'Подумай, сколько ты сэкономишь, если подпишешь его сейчас.', 'Think how much you will save if you sign him now.', [(237, 'Подумай, сколько ты сэкономишь, если подпишешь его сейчас')], 'adapted'),
    ('nagiyev', 'Так что, Максим, теперь ты новый шеф-повар «Моне».', 'So, Maxim, now you are the new head chef of Monet.', [(241, 'Так что, Максим, теперь ты новый шеф-повар Моне')], 'adapted'),
    ('max', 'Правда? Я новый шеф-повар ресторана «Моне»?', 'Really? I am the new head chef of Restaurant Monet?', [(243, 'Я шеф-повар Моне')], 'adapted'),
    ('barinov', 'Смотри не подведи меня там, Огузок!', 'Make sure you do not let me down there, Oguzok!', [(243, 'Не подведи')], 'adapted'),
    ('max', 'Спасибо вам огромное, шеф, можно вас обнять?', 'Thank you so much, Chef, may I hug you?', [(244, 'Спасибо, шеф, можно')], 'adapted'),
]
WALK = [
    (0, None, '\'By the way, technically you won the bet.\' Turning to the bet to Max, Barinov opens with "kstati" ("by the way") as if the thought just crossed his mind.'),
    (1, None, "'Congratulations to you, but there is also bad news.' Barinov weighs in briskly across the room, shifting the mood of the conversation in a single beat."),
    (2, None, '\'As of today you are fired from our kitchen.\' Barinov follows up decisively on the spot and leans on "segodnyashnego" ("of today\'s", a form of "segodnyashniy") to give the remark its edge.'),
    (3, None, '\'What do you mean fired, why, that is unfair!\' Max reacts sharply at once and uses "nespravedlivo" ("unfairly") to carry the main weight of the thought.'),
    (4, None, "'Two great chefs cannot coexist in one kitchen.' Barinov weighs in openly in this moment, making his position completely clear."),
    (5, None, '\'So tomorrow you start as head chef at Restaurant Monet!\' Touching on the head beside Max, Barinov uses "shef-povarom" ("head chef", from "shef-povar") to make the point stick.'),
    (6, None, '\'In a year every restaurant in Moscow will be chasing after him.\' Touching on the restaurant beside Max, Barinov chooses "restorany" ("restaurant", from the root "restoran") so Max hears the exact meaning.'),
    (7, None, "'Because right now he is me in my youth.' Barinov jumps in openly without any doubt, before Nagiyev can change the subject."),
    (8, None, '\'Think how much you will save if you sign him now.\' Barinov counters naturally right here and brings in "sekonomish" ("to save", from "sekonomit") as the key Russian word here.'),
    (9, None, '\'So, Maxim, now you are the new head chef of Monet.\' Bringing up the new head on the spot, Nagiyev links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (10, None, "'Really? I am the new head chef of Restaurant Monet?' Max checks eagerly about what Barinov just brought up."),
    (11, None, '\'Make sure you do not let me down there, Oguzok!\' Barinov continues earnestly with Max and uses "podvedi" ("to let down", from "podvesti") to make the point stick.'),
    (12, None, '\'Thank you so much, Chef, may I hug you?\' Pointing to the thank to Barinov, Max leans on "mozhno" ("it is possible, one may"), which carries the whole predicate in Russian without needing "it is".'),
]
