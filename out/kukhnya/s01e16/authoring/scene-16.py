# Authoring module for kukhnya-s01e16-scene-16.
ID = 'kukhnya-s01e16-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 16
TITLE = 'Пряность Айнура  (Aynura Spice)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'One more cook without papers needs hiding, and the kitchen is running out of places to put people. Max has a plan, Barinov has a better one, and then the inspector comes back from the fridge with news. Listen to how differently Barinov speaks to Max and to the inspector.'
OPENER = "Now the hiding plan and the inspector's verdict, line by line."
TRANSITION = 'And the whole scramble once more, at full speed.'
OUTRO = "The inspector declares the kitchen clean, but he still wonders how so few people do so much work. Listen for 'na vkhode', 'at the entrance', where Russian uses 'na', 'on', and English uses 'at'. See you next time!"
CLOSING = ('barinov', 'Всего доброго!')
STORY = [
    ('max', 'Шеф, тут ещё один.', "Chef, here's another one.", [(192, 'Еще один.')], ''),
    ('barinov', 'Господи, куда вас всех девать?', 'Good Lord, where am I supposed to put you all?', [(192, 'Господи, куда вас всех девать?')], ''),
    ('max', 'Пусть пока посидит в туалете.', 'Let him sit in the bathroom for now.', [(193, 'Да сейчас вы в туалете отсидитесь,')], ''),
    ('max', 'Потом выйдет через главный вход.', 'Then he can go out through the main entrance.', [(193, 'потом через главный день.')], ''),
    ('barinov', 'Самый умный, да? Они на входе дежурят.', 'Think you are so clever? They are guarding the entrance.', [(194, 'Ты самоумный, да? Они на входе дежурят.')], ''),
    ('barinov', 'Пусть сядет в зале, как Айнура.', 'Let him sit in the dining room, like Ainura.', [(195, 'Боже мой, сядет в зал, как и Анюра.')], ''),
    ('barinov', 'Сходи к Косте на бар, возьми для него одежду.', 'Go over to Kostya at the bar and get him some clothes.', [(196, 'Пойди, сходи в Костя на бар, возьми для него одежду.')], ''),
    ('inspector', 'Виктор Петрович, поздравляю вас.', 'Viktor Petrovich, congratulations.', [(202, 'Виктор Петрович.'), (203, 'Все ж, поздравляю вас.')], ''),
    ('inspector', 'У вас всё чисто.', "You're in the clear.", [(203, 'У вас все чисто.')], ''),
    ('barinov', 'Ну, я же вам сразу сказал.', 'Well, I told you that right away.', [(204, 'Ну, я же вам сразу сказал.')], ''),
    ('inspector', 'Простите, но я не имею права верить на слово.', "Forgive me, but I can't just take your word for it.", [(205, 'Ну, вы простите меня, конечно, но я не имею права верить на слово.')], ''),
    ('inspector', 'У вас ведь так мало сотрудников.', 'You have so few employees.', [(207, 'У вас ведь так мало сотрудников.')], ''),
    ('barinov', 'Мы профессионалы.', "We're professionals.", [(208, 'Мы профессионалы.')], ''),
]
WALK = [
    (0, None, "'Chef, here's another one.' 'Eshchyo odin' means 'one more', the usual Russian 'another'. 'Tut', 'here', is the casual partner of 'zdes'."),
    (1, None, "'Good Lord, where am I supposed to put you all?' 'Devat' means 'to put away' or 'to get rid of', and 'kuda vas devat' is a set groan when there are too many of something."),
    (2, None, "'Let him sit in the bathroom for now.' 'Posidit' is 'sidit', 'to sit', with 'po-', which makes it 'sit for a while'. 'Poka' here means 'for now', not 'bye'."),
    (3, None, "'Then he can go out through the main entrance.' 'Vykhod', 'exit', and 'vkhod', 'entrance', are built on the same root: 'vy-' is 'out', 'v-' is 'in'. 'Vyydet', 'he'll go out', comes from 'vyyti'."),
    (4, None, "'Think you are so clever? They are guarding the entrance.' Russian says 'na vkhode', literally 'on the entrance', where English says 'at'. 'Samy umny', 'the cleverest', is a sarcastic way to say 'smart guy'."),
    (5, None, "'Let him sit in the dining room, like Ainura.' 'Pust syadet' means 'let him sit down', the moment of sitting, and 'pust posidit' means 'let him sit a while'. 'Kak', 'how', also means 'like'."),
    (6, None, "'Go over to Kostya at the bar and get him some clothes.' 'Skhodi' means 'go and come back', a quick errand. 'Odezhda', 'clothes', is singular in Russian, so it is literally 'take clothing'."),
    (7, None, "'Viktor Petrovich, congratulations.' 'Pozdravlyayu vas' is literally 'I congratulate you', and the '-yu' ending says 'I'. It's also how you say 'happy birthday': 'pozdravlyayu!'."),
    (8, None, "'You're in the clear.' 'U vas vsyo chisto' is literally 'at you everything clean'. 'Chisto', 'clean', ends in '-o' to match 'vsyo', 'everything'."),
    (9, None, "'Well, I told you that right away.' 'Zhe' adds 'didn't I?' to 'ya vam skazal', 'I told you'. 'Vam', 'to you', is the polite 'vy' in its 'to' form."),
    (10, None, "'Forgive me, but I can't just take your word for it.' 'Ne imeyu prava' means 'I have no right', a formal phrase from officials. 'Verit na slovo', literally 'to believe on the word', is 'to take someone's word'."),
    (11, None, "'You have so few employees.' After 'malo', 'few', the word changes ending: 'sotrudniki' becomes 'sotrudnikov'. 'Ved' means 'after all', and it makes the remark sound like a little trap."),
    (12, None, "'We're professionals.' Russian needs no 'are': 'my professionaly', 'we professionals'. The word is borrowed, so it sounds almost like the English."),
]
