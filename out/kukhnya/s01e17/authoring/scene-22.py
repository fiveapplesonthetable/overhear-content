# Authoring module for kukhnya-s01e17-scene-22.
ID = 'kukhnya-s01e17-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 22
TITLE = 'Бокал для шефа  (A Glass for the Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "Standing by the kitchen counter after the conflict is resolved, Chef Viktor decides it is time to properly celebrate with his staff. He asks Nastya to bring a clean glass so he can pour a celebratory drink and raise a toast with Max. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine this kitchen conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "With glasses in hand, Chef Viktor and the kitchen crew prepare to drink together, enjoying a rare moment of camaraderie in Claude Monet. Next time you watch the episode, listen for the Russian expressions for 'to bring' and 'clean' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Настя, принеси мне чистый бокал.', 'Nastya, bring me a clean glass.', [(326, 'принеси бокал.')], ''),
    ('nastya', 'Сейчас принесу, шеф.', 'I will bring it right away, chef.', [], ''),
    ('barinov', 'Мы должны выпить за праздник.', 'We must drink to the holiday.', [], ''),
    ('max', 'Шеф, это очень приятно.', 'Chef, this is very pleasant.', [], ''),
    ('barinov', 'Наливай всем хорошее вино.', 'Pour good wine for everyone.', [], ''),
    ('nastya', 'Вот ваш бокал, шеф.', 'Here is your glass, chef.', [], ''),
    ('barinov', 'Спасибо, Настя, молодец.', 'Thank you, Nastya, well done.', [], ''),
    ('max', 'Какой красивый бокал!', 'What a beautiful glass!', [], ''),
    ('barinov', 'Для хорошего вина нужен красивый бокал.', 'For good wine one needs a beautiful glass.', [], ''),
    ('nastya', 'Я принесла бокалы для всех.', 'I brought glasses for everyone.', [], ''),
    ('max', 'Теперь у всех есть бокалы.', 'Now everyone has glasses.', [], ''),
    ('barinov', 'Поднимите ваши бокалы.', 'Raise your glasses.', [], ''),
    ('barinov', 'Давайте выпьем за дружбу!', 'Let us drink to friendship!', [], ''),
]
WALK = [
    (0, None, "'Nastya, bring me a clean glass.' Barinov barks an order, requiring specific equipment for the toast."),
    (1, None, "'I will bring it right away, chef.' Nastya responds with immediate compliance."),
    (2, None, "'We must drink to the holiday.' Barinov declares the necessity of marking the occasion with a drink."),
    (3, None, "'Chef, this is very pleasant.' Max expresses genuine delight at the unexpected gesture."),
    (4, None, "'Pour good wine for everyone.' Barinov gives a broader command to ensure everyone is included."),
    (5, None, "'Here is your glass, chef.' Nastya returns quickly, delivering the requested item."),
    (6, None, "'Thank you, Nastya, well done.' Barinov offers a brief word of thanks and approval."),
    (7, None, "'What a beautiful glass!' Max compliments the aesthetic quality of the item."),
    (8, None, "'For good wine one needs a beautiful glass.' Barinov philosophizes slightly, linking the quality of the drink to its presentation."),
    (9, None, "'I brought glasses for everyone.' Nastya confirms that she has supplied everyone with what they need."),
    (10, None, "'Now everyone has glasses.' Max points out that the group is now fully prepared."),
    (11, None, "'Raise your glasses.' Barinov commands the room to prepare for the toast."),
    (12, None, "'Let us drink to friendship!' He delivers the final dedication, focusing on camaraderie."),
]
