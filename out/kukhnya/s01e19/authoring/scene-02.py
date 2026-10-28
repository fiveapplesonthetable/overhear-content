# Authoring module for kukhnya-s01e19-scene-02.
ID = 'kukhnya-s01e19-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 2
TITLE = 'Новые имена  (New names)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'artyom': 'Артём', 'barinov': 'Шеф', 'fedya': 'Федя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = 'In the kitchen, Senya and Fedya are gone, and Barinov refuses to accept it. He calls the cooks who are left by the old names, whether they like it or not. Russian first, no need to catch it all.'
OPENER = "We'll take the lines one by one."
TRANSITION = "Let's finish by hearing it all again."
OUTRO = "Names are something you have to earn in this kitchen. When you hear a Russian say 'ya' and then a name, with no 'am' in between, that is the plain way to introduce yourself. See you next time!"
CLOSING = ('fedya', 'До свидания!')
STORY = [
    ('barinov', 'Сеня, соус готов?', 'Senya, is the sauce ready?', [(16, 'Сеня, соус готов?')], ''),
    ('artyom', 'А я не Сеня.', 'I am not Senya.', [(17, 'А я не Сеня, я Артем.')], ''),
    ('artyom', 'Я Артем.', 'I am Artyom.', [(17, 'А я не Сеня, я Артем.')], ''),
    ('barinov', 'Сеню уволили.', 'Senya got fired.', [(18, 'Сеню же уволили. А мне плевать, кто ты.')], ''),
    ('barinov', 'Мне плевать, кто ты.', 'I do not care who you are.', [(18, 'Сеню же уволили. А мне плевать, кто ты.')], ''),
    ('barinov', 'Сегодня ты Сеня.', 'Today you are Senya.', [(19, 'Сегодня ты Сеня.')], ''),
    ('barinov', 'Федя бы это быстро сделал.', 'Fedya would have done it fast.', [(21, 'Федя бы это за 10 секунд сделал.')], ''),
    ('fedya', 'Я тоже Федя, шеф.', 'I am Fedya too, Chef.', [(22, 'Я, кстати, тоже Федя, шеф.')], ''),
    ('barinov', 'Нет, ты не Федя.', 'No, you are not Fedya.', [(23, 'Нет, ты не Федя.')], ''),
    ('barinov', 'Имя Федя заслужить надо.', 'You have to earn the name Fedya.', [(24, 'Имя Федя заслужить надо.')], ''),
    ('barinov', 'Теперь ты Артем.', 'Now you are Artyom.', [(25, 'Теперь ты Артем.')], ''),
    ('fedya', 'Да, шеф.', 'Yes, Chef.', [(26, 'Да, шеф.')], ''),
]
WALK = [
    (0, None, "'Senya, is the sauce ready?' 'Ready' is a short masculine form, since the word for sauce is masculine. 'Sauce' is borrowed from French."),
    (1, None, "'But I'm not Senya.' The small 'a' means 'but' and contrasts the two ideas. There's no 'am', only 'I not Senya'."),
    (2, None, "'I'm Artyom.' Just 'I Artyom', with no word for 'am'. It's the plain way to say your name."),
    (3, None, "'Senya was fired.' The name changes its ending to 'yu' because Senya is the one affected. 'Fired' has the plural 'li', for an unnamed 'they'."),
    (4, None, "'I don't care who you are.' The phrase is literally 'to me, to spit'. It's a rude, informal way to say you don't care."),
    (5, None, "'Today you're Senya.' No 'are' again. 'Today' sits in front of 'you', and the name stays as it is."),
    (6, None, "'Fedya would have done that quickly.' The small word 'by' after the name is what makes it 'would'. 'Did' treats the action as done, ending in 'l'."),
    (7, None, "'I'm Fedya too, Chef.' 'Too' goes after 'I'. Again there's no 'am', just a name."),
    (8, None, "'No, you're not Fedya.' The 'not' stands right before the name. It's as blunt as it sounds."),
    (9, None, "'You have to earn the name Fedya.' The Russian puts the verb first, 'earn', and 'necessary' at the end, which gives the line weight. 'Name' ends in 'ya', and is neuter."),
    (10, None, "'Now you're Artyom.' 'Now' stands at the start. The line is just 'now you Artyom'."),
    (11, None, "'Yes, Chef.' Two words, and no more is needed. It's the classic reply of a cook to a chef."),
]
