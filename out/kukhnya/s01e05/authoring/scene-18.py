# Authoring module for kukhnya-s01e05-scene-18.
ID = 'kukhnya-s01e05-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 18
TITLE = 'Рыбный экзамен  (The Fish Exam)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Chef Viktor Barinov decides to test Max's culinary endurance during dinner service. He publicly puts Max in sole charge of the demanding fish station. Barinov then secretly orders the waiters to push cod dishes, flooding Max with overwhelming orders. Let's listen to their confrontation in Russian first."
OPENER = "Let's analyze this intense kitchen trial line by line. Notice how culinary hierarchy and restaurant pressure create high-stakes professional drama."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max faces a grueling test under Chef Barinov's watchful and demanding eye. Fantastic job practicing everyday culinary Russian! Next time you watch the episode, listen for the Russian expressions for 'dish' and 'fast' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Все заказы по рыбе выполняешь ты!', 'You are handling all the fish orders!', [(243, 'все заказы по рыбе')], ''),
    ('max', 'Есть, шеф, я готов к работе!', 'Yes, Chef, I am ready to work!', [(244, 'Есть, шеф')], ''),
    ('barinov', 'Посмотрим, какой из тебя рыбный мастер.', 'Let us see what kind of fish master you are.', [], ''),
    ('max', 'Я приготовлю все блюда очень быстро.', 'I will prepare all dishes very quickly.', [], ''),
    ('barinov', 'Максим, прими заказ: две трески по-флорентийски!', 'Maxim, take the order: two cod Florentines!', [(256, 'две трески')], ''),
    ('max', 'Да, шеф, уже начинаю готовить.', 'Yes, Chef, I am already starting to cook.', [(257, 'Да, шеф')], ''),
    ('barinov', 'И ещё две порции трески с миндалём!', 'And two more portions of cod with almonds!', [], ''),
    ('max', 'Я же уже взял два блюда!', 'But I already took two dishes!', [(260, 'Я же уже взял два блюда')], ''),
    ('barinov', 'Не спорь, Федя как-то справлялся!', 'Do not argue, Fedya managed somehow!', [(261, 'Федя как-то справлялся')], ''),
    ('max', 'Мне не хватает свежей рыбы здесь.', 'I do not have enough fresh fish here.', [], ''),
    ('barinov', 'Ищи на складе и быстрее крутись!', 'Search in the storage and hustle faster!', [], ''),
    ('max', 'Я справлюсь со всеми заказами сам.', 'I will handle all orders myself.', [], ''),
    ('barinov', 'Вот и докажи это делом, огузок!', 'Prove it with action then, rump!', [], ''),
]
WALK = [
    (0, None, "'You are handling all the fish orders!' Barinov intentionally overloads the rookie with responsibilities."),
    (1, None, "'Yes, Chef, I am ready to work!' Max confidently accepts the massive workload."),
    (2, None, "'Let us see what kind of fish master you are.' Barinov challenges the young cook to prove his worth."),
    (3, None, "'I will prepare all dishes very quickly.' Max boldly promises to deliver everything on time."),
    (4, None, "'Maxim, take the order: two cod Florentines!' Barinov calls out another challenging ticket."),
    (5, None, "'Yes, Chef, I am already starting to cook.' Max assures the boss he is already on it."),
    (6, None, "'And two more portions of cod with almonds!' Barinov piles on even more portions to test him."),
    (7, None, "'But I already took two dishes!' Max protests the sudden increase in volume."),
    (8, None, "'Do not argue, Fedya managed somehow!' Barinov shuts down the complaints by comparing him to a veteran."),
    (9, None, "'I do not have enough fresh fish here.' Max points out a critical shortage of ingredients."),
    (10, None, "'Search in the storage and hustle faster!' Barinov tells him to solve the problem himself and hurry up."),
    (11, None, "'I will handle all orders myself.' Max stubbornly insists he can handle the pressure."),
    (12, None, "'Prove it with action then, rump!' Barinov demands that he stop talking and start cooking."),
]
