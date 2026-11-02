# Authoring module for domashniy-arest-s01e01-scene-19.
ID = 'domashniy-arest-s01e01-scene-19'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 19
TITLE = 'Список желаний  (The Wish List)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "Now we're in the Samsonovs' room. Last time, Arkady refused to fix the leaking toilet pipe and promised the family everything they want once he's free, and Nina demanded it in writing. So with a pen and paper on the table, Nina starts the list, and Arkady promises everything. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go through the list item by item. Nina knows exactly what she wants, and the flat comes first."
TRANSITION = "Here's the list scene again, from the top."
OUTRO = "A flat, a car, a spa and a university place, all on one sheet of paper. Next time we meet Arkady's guests; see you then. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('nina', 'Квартира. Три комнаты.', 'A flat. Three rooms.', [(736, 'Квартира'), (745, 'три комнаты')], "736 'трёхкомнатная' simplified to 'три комнаты'"),
    ('arkady', 'Квартира будет отличная. На Симашко есть новый дом.', "It'll be an excellent flat. There's a new building on Simashko Street.", [(737, 'будет отличная'), (738, 'на Симашко')], "'квартирка' -> 'квартира'; 'новостроечка' -> 'новый дом'"),
    ('arkady', 'Хороший район. Там три комнаты и балкон.', "It's a good area. There are three rooms and a balcony.", [(740, 'хороший район'), (745, 'три комнаты')], "746 'балкончик' -> 'балкон'"),
    ('nina', 'С мебелью?', 'With furniture?', [(747, 'С мебелью')], ''),
    ('arkady', 'Конечно, с мебелью.', 'Of course, with furniture.', [(747, 'с мебелью')], "748 'Разумеется' -> the simpler 'Конечно'"),
    ('samson', 'Машина. Немецкая.', 'A car. A German one.', [(749, 'Машина')], "749 slang 'Немец' -> 'Немецкая'"),
    ('nina', 'Мне ещё работа нужна.', 'I need a job too.', [(752, 'Мне еще работа нужна')], ''),
    ('arkady', 'Для вас можно открыть салон красоты.', 'We could open a beauty salon for you.', [(754, 'для вас'), (755, 'салон красоты')], "754-755 simplified: 'мы можем ... открыть' -> 'можно открыть'"),
    ('arkady', 'Или ещё лучше: спа!', 'Or even better: a spa!', [(756, 'Или еще лучше'), (757, 'Спа')], ''),
    ('nina', 'Спа. Давайте!', "A spa. Let's do it!", [(758, 'Спа'), (759, 'Давайте')], ''),
    ('nina', 'Юле надо поступить в институт.', 'Yulia needs to get into university.', [(761, 'в институт поступить надо')], "'Юльке' -> 'Юле'; word order made neutral"),
    ('arkady', 'Это вообще без проблем.', "That's no problem at all.", [(764, 'Это вообще без проблем')], ''),
    ('samson', 'Слушай, обманешь — будут проблемы. Понял?', "Listen, if you cheat us, there'll be trouble. Got it?", [(766, 'обманешь'), (766, 'понял')], "766 retold cleanly: the threat to tear his head off -> 'будут проблемы'"),
    ('arkady', 'Ваня, расслабься. В этот раз без обмана.', "Vanya, relax. This time there's no trick.", [(769, 'Ваня, ну расслабься'), (770, 'без обмана')], "'ну' and 'вообще' dropped"),
    ('arkady', 'Почему он меня всё время за горло хватает?', 'Why does he keep grabbing me by the throat?', [(772, 'все время за горло хватает')], "772 'мне' (transcription slip) -> 'меня'"),
    ('samson', 'А мне что?', 'And what about me?', [(774, 'А мне что')], ''),
    ('arkady', 'О, а вот и мой заместитель! Пойдёмте, я вас познакомлю.', "Oh, and here's my deputy! Come on, I'll introduce you.", [(776, 'мой заместитель'), (777, 'Пойдемте, я вас')], "'с ним' dropped from 777"),
]
WALK = [
    (0, None, ["'A flat. Three rooms.' After the number three, the translation for 'room', ", ('nina', 'комнаты.'), ", takes a special ending, as it does after two and four. Arkady has just the thing."]),
    (1, 'Квартира будет отличная.', ["'It'll be an excellent flat.' the term that translates to 'will be', ", ('arkady', 'будет.'), ", turns a simple description into a promise. And he knows where."]),
    (1, 'На Симашко есть новый дом.', ["'There's a new building on Simashko Street.' The little word in the middle that literally translates to 'there is', ", ('arkady', 'есть.'), ", is how you say something exists. In the show he admits he kept three of those flats for himself."]),
    (2, None, ["'It's a good area. There are three rooms and a balcony.' the translation for 'there', ", ('arkady', 'Там.'), ", plus a list: simple and useful. Nina has a practical question."]),
    (3, None, ["'With furniture?' The little word for 'with', ", ('nina', 'С.'), ", makes the next word change its ending. Arkady doesn't hesitate."]),
    (4, None, ["'Of course, with furniture.' The opening word that translates to 'of course', ", ('arkady', 'Конечно.'), ", is one of the most useful words you can learn. Samson adds his wish."]),
    (5, None, ["'A car. A German one.' The describing word takes a matching ending, because the expression for 'car', ", ('samson', 'Машина.'), ", needs it. Nina hasn't finished."]),
    (6, None, ["'I need a job too.' Literally 'to me also a job is needed'. The person who needs something comes first, using the term meaning 'to me', ", ('nina', 'Мне.'), ". Arkady thinks fast."]),
    (7, None, ["'We could open a beauty salon for you.' the term after 'for you' that translates to 'it's possible', ", ('arkady', 'можно.'), ", is followed by the basic form of an action word. Then he has a better idea."]),
    (8, None, ["'Or even better: a spa!' the expression for 'spa', ", ('arkady', 'спа.'), ", is exactly the same as in English. Nina loves it."]),
    (9, None, ["'A spa. Let's do it!' the Russian for the polite or plural 'let's', ", ('nina', 'Давайте.'), ", comes second. Then she thinks of her daughter."]),
    (10, None, ["'Yulia needs to get into university.' Her name comes first, in the 'to Yulia' form, and then the Russian word that translates to 'it's necessary', ", ('nina', 'надо.'), ". Same pattern as 'I need' a moment ago. Arkady is generous."]),
    (11, None, ["'That's no problem at all.' The little word for 'without', ", ('arkady', 'без.'), ", changes the ending of the next word. Samson wants to make one thing clear."]),
    (12, None, ["'Listen, if you cheat us, there'll be trouble. Got it?' In Russian you don't even need the expression 'if': the action word for 'cheat', ", ('samson', 'обманешь.'), ", sets the condition all by itself. In the show his threat is far more colourful. Arkady tries to calm him down."]),
    (13, None, ["'Vanya, relax. This time there's no trick.' He calls Samson by his first name, the term for 'Vanya', ", ('arkady', 'Ваня.'), ", which is the short and friendly form of Ivan. Then he complains to Nina."]),
    (14, None, ["'Why does he keep grabbing me by the throat?' The phrase in the middle that translates to 'all the time', ", ('arkady', 'всё время.'), ", is very common. Samson has a complaint of his own."]),
    (15, None, ["'And what about me?' Three little words, featuring the term for 'to me', ", ('samson', 'мне.'), ", again. Everyone got something except him. But just then Arkady's deputy arrives, and the question is forgotten."]),
    (16, 'О, а вот и мой заместитель!', ["'Oh, and here's my deputy!' The little word for 'here', ", ('arkady', 'вот.'), ", plus 'and' means 'here comes'. Perfect timing."]),
    (16, 'Пойдёмте, я вас познакомлю.', ["'Come on, I'll introduce you.' He uses the Russian for the plural 'come on', ", ('arkady', 'Пойдёмте.'), ", because he's taking the whole family to meet the guest."])
]
