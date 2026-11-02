
# Authoring module for kukhnya-s01e04-scene-15.
ID = 'kukhnya-s01e04-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 15
TITLE = 'Обед для персонала  (Staff Lunch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "The chef catches Max in his office and asks whether the staff lunch is cooked. Max says it is nearly done, the lie detector says otherwise, and Max tries flattery. Here's the Russian first."
OPENER = "Let's listen to the chef catch him out."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max narrowly escapes, and sprints back to the stove. You've heard the soldier's 'yes, sir', which Max uses whenever the chef gives an order."
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Лавров, подойди сюда прямо сейчас.', 'Lavrov, come here right now.', [(180, 'соседний ресторан')], ''),
    ('max', 'Шеф, я могу уже идти на кухню?', 'Chef, can I already go to the kitchen?', [(188, 'я могу идти')], ''),
    ('barinov', 'Подожди! Ты приготовил обед для поваров?', 'Wait! Did you cook lunch for the cooks?', [(190, 'ты обед приготовил')], ''),
    ('max', 'Да, конечно, я всё уже сделал.', 'Yes, of course, I already made everything.', [(191, 'Да')], ''),
    ('barinov', 'Точно всё готово? Ты не обманываешь меня?', "Is everything definitely ready? You aren't deceiving me?", [(193, 'мне врешь')], ''),
    ('max', 'Ну, почти приготовил, осталось совсем немного.', 'Well, almost cooked, very little is left.', [(192, 'Почти приготовил')], ''),
    ('barinov', 'Ты опять врёшь мне в лицо!', 'You are lying to my face again!', [(193, 'мне врешь')], ''),
    ('max', 'Шеф, я никогда не вру вам.', 'Chef, I never lie to you.', [(195, 'никогда не обману')], ''),
    ('barinov', 'Детектор лжи показывает совсем другое!', 'The lie detector shows something completely different!', [(196, 'полюбуйтесь')], ''),
    ('max', 'Эта глупая машина просто сломалась.', 'This stupid machine simply broke.', [(194, 'да что')], ''),
    ('max', 'Шеф, вы для меня как родной отец.', 'Chef, you are like my own father to me.', [(197, 'вы для меня'), (198, 'Как отец')], ''),
    ('barinov', 'Быстро беги на кухню и корми людей!', 'Quickly run to the kitchen and feed people!', [(189, 'Вали отсюда')], ''),
    ('max', 'Слушаюсь, шеф, я сделаю всё моментально.', 'Understood, chef, I will do everything instantly.', [(195, 'не обману')], ''),
]
WALK = [
    (0, None, ["'Lavrov, come here right now.' The Russian expression for 'come up' is ", ("barinov", "подойди"), " built from a prefix meaning 'up to'. Using the surname, ", ("barinov", "Лавров,"), " marks a serious talk."]),
    (1, None, ["'Chef, can I already go to the kitchen?' Just like English 'can go', the Russian term for 'I can', ", ("max", "могу"), " is followed by a plain action word, ", ("max", "идти"), " to go on foot. The translation for 'already', ", ("max", "уже"), " slips in between them."]),
    (2, None, ["'Wait! Did you cook lunch for the cooks?' The expression for the familiar 'wait' is ", ("barinov", "Подожди!"), " 'For the cooks' translates to ", ("barinov", "для поваров?")]),
    (3, None, ["'Yes, of course, I already made everything.' The Russian term for 'did' or 'made' is ", ("max", "сделал."), " ending with the man's action sound. The term for 'already' translates to ", ("max", "уже")]),
    (4, None, ["'Is everything definitely ready? You aren't deceiving me?' The translation for 'for sure' is ", ("barinov", "Точно"), " 'You are deceiving' translates to ", ("barinov", "обманываешь"), " built from a word meaning a deception."]),
    (5, None, ["'Well, almost cooked, very little is left.' The word for 'almost' is ", ("max", "почти"), " The Russian term for 'is left' is ", ("max", "осталось"), " which has an ending used when the thing it refers to has no name."]),
    (6, None, ["'You are lying to my face again!' The Russian term for the blunt everyday 'you lie' translates to ", ("barinov", "врёшь"), " from the action word for lying. 'To my face' translates literally to ", ("barinov", "в лицо!"), " or 'into the face'."]),
    (7, None, ["'Chef, I never lie to you.' The phrase for 'never lie' translates literally to ", ("max", "никогда не вру"), " meaning 'never not lie', a double negative. The expression for the polite 'to you' is ", ("max", "вам.")]),
    (8, None, ["'The lie detector shows something completely different!' Translates literally to 'the detector of lie'. The phrase for a lie changes to ", ("barinov", "лжи"), " in this form. The translation for 'other', ", ("barinov", "другое!"), " takes an ending used when the thing it shows has no name."]),
    (9, None, ["'This stupid machine simply broke.' The expression for 'broke' translates to ", ("max", "сломалась."), " with a sound at the end meaning it broke by itself, and an ending that matches the describing word for the machine, ", ("max", "машина")]),
    (10, None, ["'Chef, you are like my own father to me.' The phrase for 'one's own', ", ("max", "родной"), " is built from a word meaning kin. The phrase for 'like my own father' translates literally to ", ("max", "как родной отец."), " meaning 'like a blood father'."]),
    (11, None, ["'Quickly run to the kitchen and feed people!' Two familiar commands back to back: the Russian term for 'run' is ", ("barinov", "беги"), " and the translation for 'feed' is ", ("barinov", "корми"), " After 'feed', the translation for people changes to ", ("barinov", "людей!")]),
    (12, None, ["'Understood, chef, I will do everything instantly.' The Russian expression for the soldier's 'yes, sir' translates to ", ("max", "Слушаюсь,"), " which translates literally to 'I obey'. The term for 'instantly' is ", ("max", "моментально."), " built from the term for 'moment'."]),
]
