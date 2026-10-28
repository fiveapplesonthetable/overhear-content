# Authoring module for kukhnya-s01e08-scene-01.
ID = 'kukhnya-s01e08-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 1
TITLE = 'Лицо ресторана  (The Face of the Restaurant)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Backstage at the television studio of a morning culinary program, restaurant owner Dmitry Nagiev corners Chef Viktor Barinov. Barinov grumbles that he is a professional cook rather than a television star, but Nagiev insists that as the face of Claude Monet, he must represent the establishment on air. Let's listen to their backstage argument in Russian first."
OPENER = "Now let's examine Barinov and Nagiev's backstage argument line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "With seconds to spare before the live broadcast begins, Chef Barinov steps out under the studio lights ready to defend his restaurant's prestige against rival chef Elena Sokolova. Next time you watch the episode, listen for the Russian expressions for 'actor' and 'to be' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Дима, зачем ты позвал меня сюда?', 'Dima, why did you call me here?', [(1, 'Дим, ну в каком хрен я здесь')], ''),
    ('nagiyev', 'Ты будешь выступать на телевидении, Виктор.', 'You will perform on television, Viktor.', [(3, 'Ты не только повар, ты лицо нашего ресторана')], ''),
    ('barinov', 'Я шеф-повар, а не известный актёр!', 'I am a head chef, not a famous actor!', [(2, 'Я же не актер, я повар')], ''),
    ('nagiyev', 'Ты главное лицо нашего дорогого ресторана.', 'You are the main face of our expensive restaurant.', [(3, 'ты лицо нашего ресторана')], ''),
    ('barinov', 'Моё место на кухне у плиты.', 'My place is in the kitchen at the stove.', [], ''),
    ('nagiyev', 'Зрители хотят видеть настоящего шефа.', 'The viewers want to see a real chef.', [(4, 'этим лицом светить')], ''),
    ('barinov', 'Отпусти меня обратно в Клод Моне.', 'Let me go back to Claude Monet.', [(5, 'Давай в ресторан поеду')], ''),
    ('nagiyev', 'Перестань спорить и иди вперёд.', 'Stop arguing and go forward.', [(10, 'Все, в тени живот и вперед')], ''),
    ('barinov', 'Там будет выступать эта Соколова?', 'Will that Sokolova perform there?', [(17, 'Елена Соколова')], ''),
    ('nagiyev', 'Да, Елена Соколова из ресторана Аркабалено.', 'Yes, Elena Sokolova from Arcobaleno restaurant.', [(16, 'шеф-повар ресторана Арка Баляна'), (17, 'Елена Соколова')], ''),
    ('barinov', 'Я докажу всем свой высокий класс.', 'I will prove my high caliber to everyone.', [], ''),
    ('nagiyev', 'Вот это отличный настрой, шеф!', 'Now that is a great attitude, chef!', [], ''),
    ('barinov', 'Прямой эфир начинается прямо сейчас.', 'Live broadcast begins right now.', [(19, 'Итак, мы начинаем')], ''),
]
WALK = [
    (0, None, "'Dima, why did you call me here?' Barinov uses the owner's informal nickname. He is annoyed to be dragged out of his kitchen."),
    (1, None, "'You will perform on television, Viktor.' Nagiyev drops the big news casually. He expects the chef to be thrilled about the exposure."),
    (2, None, "'I am a head chef, not a famous actor!' Barinov immediately rejects the idea. He hates the thought of performing for a camera."),
    (3, None, "'You are the main face of our expensive restaurant.' Nagiyev tries to flatter him into compliance. He reminds Viktor that he represents their luxury brand."),
    (4, None, "'My place is in the kitchen at the stove.' Barinov stubbornly defends his professional territory. He believes a cook belongs behind the scenes."),
    (5, None, "'The viewers want to see a real chef.' Nagiyev explains the marketing strategy. He needs Viktor's authentic grumpy persona for the show."),
    (6, None, "'Let me go back to Claude Monet.' Barinov begs to be released from this PR stunt. He just wants to return to his comfortable domain."),
    (7, None, "'Stop arguing and go forward.' Nagiyev physically pushes him toward the stage. He leaves the chef no room for debate."),
    (8, None, "'Will that Sokolova perform there?' Barinov suddenly stops when he hears his rival's name. His competitive instincts flare up instantly."),
    (9, None, "'Yes, Elena Sokolova from Arcobaleno restaurant.' Nagiyev confirms the presence of the other head chef. He knows this will motivate Viktor better than anything else."),
    (10, None, "'I will prove my high caliber to everyone.' Barinov changes his tune completely. He is now determined to crush his competitor on live television."),
    (11, None, "'Now that is a great attitude, chef!' Nagiyev celebrates his successful manipulation. He is pleased to see the chef finally fired up."),
    (12, None, "'Live broadcast begins right now.' Barinov prepares himself for the cameras. He marches onto the stage ready for a fight."),
]
