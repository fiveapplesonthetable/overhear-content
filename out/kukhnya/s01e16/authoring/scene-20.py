# Authoring module for kukhnya-s01e16-scene-20.
ID = 'kukhnya-s01e16-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 20
TITLE = 'Штраф и депортация  (Fine and Deportation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "The inspector brings Fedya into Barinov's office. He tells the chef he should have owned up from the start, and he turns down any deal. First comes the fine, and then something worse for the kitchen."
OPENER = 'Here it is again, one line at a time.'
TRANSITION = "Let's hear the whole thing again, start to finish."
OUTRO = "Barinov will pay, but he is about to lose his fish cook. 'Daleko ne vsyo', 'far from all', is worth keeping: it warns that the bad news isn't over yet. See you next time!"
CLOSING = ('inspector', 'Всего хорошего!')
STORY = [
    ('inspector', 'Вот я и нашёл вашего повара.', "Well, I've found your cook.", [(271, 'Вот.')], ''),
    ('barinov', 'Федя, почему ты не спрятался?', "Fedya, why didn't you hide?", [], ''),
    ('inspector', 'Зря вы меня обманывали, Виктор Петрович.', "You shouldn't have lied to me, Viktor Petrovich.", [(272, 'Зря вы, Виктор Петрович, упорствовали.')], ''),
    ('barinov', 'Я хотел защитить своего лучшего повара.', 'I wanted to protect my best cook.', [], ''),
    ('inspector', 'Нужно было сразу признаться во всём.', 'You should have owned up to everything right away.', [(273, 'Признались бы сразу во всем')], ''),
    ('inspector', 'Тогда вы получили бы простое предупреждение.', 'Then you would have got off with a simple warning.', [(273, 'и отделались бы простым предупреждением.')], ''),
    ('barinov', 'Может, договоримся?', 'Maybe we can work something out?', [], ''),
    ('inspector', 'Нет, теперь уже поздно.', "No, it's too late now.", [], ''),
    ('inspector', 'К сожалению, вам придётся платить штраф.', "Unfortunately, you'll have to pay a fine.", [(274, 'К моему огромному сожалению, придется платить штраф.')], ''),
    ('barinov', 'Ладно, мы заплатим.', "All right, we'll pay.", [], ''),
    ('inspector', 'Но это ещё далеко не всё.', "But that's far from all.", [], ''),
    ('inspector', 'Молодого человека придётся депортировать.', 'The young man will have to be deported.', [(275, 'А несчастного молодого человека'), (276, 'придется депортировать.')], ''),
    ('barinov', 'Как я буду работать без Феди?', 'How am I going to work without Fedya?', [], ''),
]
WALK = [
    (0, None, "'Well, I've found your cook.' 'Vot ya i nashyol' is literally 'here I have found', and 'vot... i' gives it the sense of 'there we are'. 'Vashego povara', 'your cook', takes '-ogo' and '-a' because he is the one found."),
    (1, None, "'Fedya, why didn't you hide?' Barinov says 'ty' to his cooks. 'Spryatalsya', 'hid', ends in '-sya', 'oneself', so it is literally 'hid himself'."),
    (2, None, "'You shouldn't have lied to me, Viktor Petrovich.' 'Zrya' means 'for nothing' or 'in vain', and 'zrya vy...' is the usual way to say 'you shouldn't have'. 'Obmanyvat' means 'to deceive'."),
    (3, None, "'I wanted to protect my best cook.' 'Zashchitit' means 'to protect', from 'shchit', 'shield'. 'Svoego' means 'my own' here, pointing back to Barinov."),
    (4, None, "'You should have owned up to everything right away.' 'Nuzhno bylo', literally 'it was needed', is the usual Russian 'should have'. 'Priznatsya vo vsyom' means 'to confess to everything'."),
    (5, None, "'Then you would have got off with a simple warning.' 'By' after a past verb turns it into 'would': 'poluchili by', 'would have got'. 'Preduprezhdenie', 'warning', comes from 'predupredit', 'to warn'."),
    (6, None, "'Maybe we can work something out?' 'Dogovorimsya' means 'we'll come to an agreement', and in a moment like this everyone hears it as a hint at a bribe. 'Mozhet' here is short for 'mozhet byt', 'maybe'."),
    (7, None, "'No, it's too late now.' 'Pozdno' means 'late', and 'uzhe' means 'already', so it is literally 'now already late'. Russian needs no 'it is' here."),
    (8, None, "'Unfortunately, you'll have to pay a fine.' 'K sozhaleniyu' is literally 'to regret', the everyday 'unfortunately'. 'Vam pridyotsya', literally 'to you it will come', means 'you'll have to'."),
    (9, None, "'All right, we'll pay.' 'Ladno' is the grudging 'all right', a step below 'khorosho'. 'Zaplatim', 'we'll pay', is the future of 'zaplatit', 'to pay up'."),
    (10, None, "'But that's far from all.' Russian says 'daleko ne vsyo', literally 'far not all'. 'Eshchyo', 'still' or 'yet', adds the feeling that more is coming."),
    (11, None, "'The young man will have to be deported.' 'Molodoy chelovek', 'young man', is also how you address a young stranger. 'Deportirovat' is a borrowed verb, and the '-irovat' ending turns many foreign words into Russian verbs."),
    (12, None, "'How am I going to work without Fedya?' 'Bez', 'without', changes 'Fedya' to 'Fedi'. 'Budu rabotat' means 'I will be working', the future of a verb that describes an ongoing activity."),
]
