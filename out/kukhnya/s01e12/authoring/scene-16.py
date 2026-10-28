# Authoring module for kukhnya-s01e12-scene-16.
ID = 'kukhnya-s01e12-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 16
TITLE = 'Ресторан напротив  (The Restaurant Across the Street)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'Barinov and Vika are standing outside the restaurant when somebody hands them a flyer for the new Italian place across the street. It makes big promises, and Barinov is not impressed. First, in Russian, what they say.'
OPENER = 'Line by line, to see how the two of them take the news.'
TRANSITION = 'Now it all again, in one go.'
OUTRO = "Barinov and Vika agree on one thing: the place across the street won't get their guests. Listen out for 'luchshe' and 'luchshiy', better and best. Bye for now."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Посмотри, что раздают прямо у нашей двери!', 'Look at what they hand out right at our door!', [(221, 'что я нашел под дверью ресторана')], ''),
    ('vika', 'Что это за странная яркая бумага?', 'What is this strange bright paper?', [], ''),
    ('barinov', 'Рядом новый ресторан открывается уже сегодня.', 'Nearby a new restaurant is opening today.', [(213, 'новый ресторан «Аркабалена»')], ''),
    ('vika', 'Они называют себя лучшим рестораном города.', 'They call themselves the best restaurant in town.', [(214, 'Современный ресторан класса «Люкс»')], ''),
    ('barinov', 'Они нагло раздают рекламу нашим гостям!', 'They brazenly hand out advertisements to our guests!', [(216, 'там бы раздал')], ''),
    ('vika', 'Неужели они обещают более вкусную еду?', 'Could they really be promising tastier food?', [(215, 'будет намного вкуснее')], ''),
    ('barinov', 'Они пишут, что у них намного лучше.', 'They write that with them it is much better.', [(215, 'и уютнее, чем тут')], ''),
    ('vika', 'Шеф, не надо так сильно нервничать.', 'Chef, you should not be so nervous.', [(226, 'Надо же, как вы нервничаете')], ''),
    ('barinov', 'Я пойду и прогоню этого наглого парня.', 'I will go and chase away this insolent fellow.', [(224, 'Еще одного клоуна найду')], ''),
    ('vika', 'Мы просто должны показать высший класс.', 'We simply must show top quality.', [], ''),
    ('barinov', 'Наш ресторан лучший во всей Москве!', 'Our restaurant is the best in all Moscow!', [], ''),
    ('vika', 'Ни один наш постоянный гость не уйдёт.', 'Not a single regular guest of ours will leave.', [(227, 'Боитесь, что к вам сегодня никто не придет?')], ''),
    ('barinov', 'Пусть сначала попробуют нормально открыться!', 'Let them try opening properly first!', [(229, 'Да вы откройтесь для начала')], ''),
]
WALK = [
    (0, None, "'Look at what they hand out right at our door!' 'Razdayut' is 'they hand out', and no 'they' is spoken. 'U nashey dveri' is 'at our door', and 'dver' takes a new ending after 'u'."),
    (1, None, "'What is this strange bright paper?' 'Chto za' asks 'what kind of'. 'Yarkaya' is 'bright', and 'bumaga' is simply 'paper'. Vika doesn't know yet that it's a flyer."),
    (2, None, "'Nearby a new restaurant is opening today.' 'Ryadom' means 'nearby' or 'right next door'. 'Otkryvaetsya' ends in 'sya', so it literally 'opens itself'."),
    (3, None, "'They call themselves the best restaurant in town.' 'Nazyvayut sebya' is literally 'they call themselves', in nearly the same shape as English. After 'call yourself', the name you take goes into the 'as' case, so it's 'luchshim restoranom', both words ending in 'm'. 'Goroda' means 'of the city'."),
    (4, None, "'They brazenly hand out advertisements to our guests!' 'Naglo' means 'cheekily' or 'brazenly', and it's a sharp word. 'Nashim gostyam' is 'to our guests', where the 'm' ending shows who gets them."),
    (5, None, "'Could they really be promising tastier food?' Surprise opens the question: 'could it really be that...'. 'Bolee vkusnuyu' is literally 'more tasty', with 'bolee', 'more', in front, the way English says 'more delicious'."),
    (6, None, "'They write that with them it is much better.' 'U nikh' is 'at them', so 'with them'. 'Namnogo luchshe' is 'much better'. 'Luchshe' is irregular, like 'better' itself: it doesn't come from 'khoroshiy', good."),
    (7, None, "'Chef, you should not be so nervous.' 'Ne nado' is 'no need'. 'Tak silno' is literally 'so strongly'. 'Nervnichat', to be nervous, is built on 'nerv', the same root as 'nerve'."),
    (8, None, "'I will go and chase away this insolent fellow.' 'Naglogo' comes from the same root as 'naglo', brazenly, two lines back. 'Parnya' is from 'paren', the everyday word for 'a guy', in the object form."),
    (9, None, "'We simply must show top quality.' 'Dolzhny' means 'must', and 'vysshy klass' is 'highest class'. 'Vysshy' is related to 'vysoky', high."),
    (10, None, "'Our restaurant is the best in all Moscow!' 'Luchshiy' is 'the best', built on the same stem as 'luchshe', better. 'Vo vsey Moskve' is 'in all Moscow': 'v' becomes 'vo' before a word starting with 'vs', which would be hard to say otherwise."),
    (11, None, "'Not a single regular guest of ours will leave.' 'Ni odin' is 'not even one', with 'ni' pushing the 'no' further. 'Postoyanny' is 'regular' and also 'constant', and 'ne uydyot' is 'will not leave', a future form, so it's a promise about what will happen."),
    (12, None, "'Let them try opening properly first!' 'Pust' is 'let', so 'pust poprobuyut' is 'let them try'. 'Snachala' means 'first', and 'normalno' is 'properly'."),
]
