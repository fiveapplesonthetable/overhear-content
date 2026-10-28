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
    (0, None, '\'By the way, technically you won the bet.\' Adding that technically Max won the bet fills in the missing piece for Max. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (1, None, '\'Congratulations to you, but there is also bad news.\' Barinov tells Max that congratulations to Max but there is also bad news without dressing it up. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (2, None, "'As of today you are fired from our kitchen.' Since as of today Max is fired from their kitchen, Barinov does not waste words on excuses."),
    (3, None, '\'What do you mean fired, why, that is unfair!\' Max declares that what do Barinov means fired why that is unfair as the tension in the room peaks. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (4, None, "'Two great chefs cannot coexist in one kitchen.' Barinov reminds Max that two great chefs cannot coexist in one kitchen before the moment passes."),
    (5, None, "'So tomorrow you start as head chef at Restaurant Monet!' Insisting that tomorrow Max starts as head at restaurant Monet shows Barinov is not backing down."),
    (6, None, "'In a year every restaurant in Moscow will be chasing after him.' Explaining that in a year every restaurant in Moscow will be chasing after him lays the cards on the table for Max."),
    (7, None, '\'Because right now he is me in my youth.\' Barinov mentions that because right now he is him in his youth so Max sees what is at stake. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (8, None, "'Think how much you will save if you sign him now.' Because Max should think how much Max will save if Max signs him now, Barinov treats the matter as settled."),
    (9, None, '\'So, Maxim, now you are the new head chef of Monet.\' Pointing out that Maxim now Barinov is the new head of Monet gives Barinov a sobering reality check. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (10, None, '\'Really? I am the new head chef of Restaurant Monet?\' Max asks whether he is the new head of restaurant Monet, refusing to let the point slide. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (11, None, "'Make sure you do not let me down there, Oguzok!' Saying that Max should make sure Max does not let him down there Oguzok is how Barinov takes charge of the moment."),
    (12, None, "'Thank you so much, Chef, may I hug you?' Wondering if much Chef may he hug Barinov shows Max caught off guard. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
]
