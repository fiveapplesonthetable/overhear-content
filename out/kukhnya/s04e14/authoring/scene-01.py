# Authoring module for kukhnya-s04e14-scene-01.
ID = 'kukhnya-s04e14-scene-01'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 14
SCENE = 1
TITLE = 'Утро дня рождения  (Birthday Morning)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'katya': 'Катя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.14'
SOURCE_FILE = 'sources/kukhnya/s04/e14.ru.srt'
INTRO = "Before Claude Monet opens at eleven in the morning, Senya and Fedya relax in the kitchen thinking the new management does not know their schedule. Newly rehired sous-chef Katya proves them wrong with a flying kitchen knife, while next door at Arcobaleno everyone celebrates Chef Barinov's birthday."
OPENER = "Let's step through the morning banter in the kitchen and the birthday greetings."
TRANSITION = 'Now listen to the complete morning scene from start to finish at natural speed.'
OUTRO = 'While Katya keeps the Claude Monet cooks on their toes, Chef Barinov prepares for his big birthday evening. Next, Barinov gets an unpleasant surprise about the dining room schedule. Until next time!'
CLOSING = ('katya', 'Всего хорошего!')
STORY = [
    ('senya', 'Заказов пока нет, ресторан ещё закрыт.', 'There are no orders yet, the restaurant is still closed.', [(1, 'Ну что такого? Заказов')], 'adapted'),
    ('senya', 'Наше новое начальство не знает расписания.', 'Our new management does not know the schedule.', [(2, 'У нас новое начальство')], 'adapted'),
    ('fedya', 'Расслабься, друг, время ещё есть.', 'Relax, friend, there is still time.', [(3, 'Расслабься, пусик.')], 'adapted'),
    ('katya', 'В следующий раз нож будет выше!', 'Next time the knife will be higher!', [(4, 'Следующий раз будет на')], 'adapted'),
    ('katya', 'Давайте быстро за работу, без разговоров!', 'Get to work quickly, without chatter!', [(5, 'Работаем?')], 'adapted'),
    ('fedya', 'Нельзя же быть такой злой утром!', 'One must not be so mean in the morning!', [(6, 'Ну, нельзя же быть')], 'adapted'),
    ('senya', 'Тем более сегодня праздник у твоего папы.', "Especially since today is your dad's holiday.", [(7, 'Тем более, день рождения')], 'adapted'),
    ('senya', 'Тихо, ребята, наш именинник сюда идёт!', 'Quiet, guys, our birthday boy is coming here!', [(8, 'Идет, идет, идет.')], 'adapted'),
    ('fedya', 'Виктор Петрович, поздравляем с днём рождения!', 'Viktor Petrovich, happy birthday to you!', [(9, 'С днем рождения!')], 'adapted'),
    ('senya', 'Ура, желаем вам здоровья и счастья!', 'Hurray, we wish you health and happiness!', [(10, 'Ура!')], 'adapted'),
    ('fedya', 'Спасибо большое, друзья, мне очень приятно.', 'Thank you very much, friends, I am very pleased.', [(11, 'Спасибо, господин.')], 'adapted'),
    ('senya', 'Лёва, подержи, пожалуйста, мои подарки.', 'Lyova, hold my presents, please.', [(15, 'О, Леха, подержи.')], 'adapted'),
]
WALK = [
    (0, None, "'There are no orders yet, the restaurant is still closed.' Since there are no orders yet the restaurant is still closed, Senya does not waste words on excuses."),
    (1, None, "'Our new management does not know the schedule.' Mentioning that their new management does not know the schedule moves the talk in a new direction."),
    (2, None, "'Relax, friend, there is still time.' Admitting that Katya should relax friend there is still time shows Fedya being honest for a change."),
    (3, None, "'Next time the knife will be higher!' Insisting that next time the knife will be higher shows Katya is not backing down."),
    (4, None, '\'Get to work quickly, without chatter!\' Because Fedya should get to work quickly without chatter, Katya does not bother softening the blow for Fedya. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
    (5, None, "'One must not be so mean in the morning!' Declaring that one must not be so mean in the morning brings Fedya's temper right to the surface. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (6, None, "'Especially since today is your dad's holiday.' Claiming that especially since today is Fedya's dad holiday sounds confident, even if Fedya has doubts."),
    (7, None, "'Quiet, guys, our birthday boy is coming here!' Saying that quiet guys their birthday boy is coming here is how Senya takes charge of the moment. Russian puts the key word right up front so his emotion lands on the first beat."),
    (8, None, "'Viktor Petrovich, happy birthday to you!' With the conversation and morning at stake, Fedya reacts without holding back. Russian puts the key word right up front so his emotion lands on the first beat."),
    (9, None, "'Hurray, we wish you health and happiness!' With the work and morning at stake, Senya reacts without holding back."),
    (10, None, "'Thank you very much, friends, I am very pleased.' Noting that very much friends he is very pleased keeps Fedya's side of the story simple and clear."),
    (11, None, "'Lyova, hold my presents, please.' Adding that Fedya should hold his presents please fills in the missing piece for Fedya."),
]
