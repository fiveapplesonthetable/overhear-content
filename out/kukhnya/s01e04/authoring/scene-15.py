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
OUTRO = 'Max narrowly escapes, and sprints back to the stove. You\'ve heard "slushayus\'", the soldier\'s "yes, sir", twice now.'
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
    (0, None, '\'Lavrov, come here right now.\' "Podoydi" is "walk up". The chef uses the surname for a serious talk.'),
    (1, None, '\'Chef, can I already go to the kitchen?\' "Mogu uzhe idti" is "I can already go". Max sounds hopeful.'),
    (2, None, '\'Wait! Did you cook lunch for the cooks?\' "Podozhdi" is a short, sharp "wait". "Obed" is the main midday meal.'),
    (3, None, '\'Yes, of course, I already made everything.\' "Sdelal" is "did" or "made", and a man ends it in -l.'),
    (4, None, '\'Is everything definitely ready? You aren\'t deceiving me?\' "Obmanyvayesh\'" comes from "obman", deceit. The chef asks the same thing twice.'),
    (5, None, '\'Well, almost cooked, very little is left.\' Max hedges with "almost" and "very little is left". The "left" word ends in "-o", because it agrees with a neuter idea: "it remained".'),
    (6, None, '\'You are lying to my face again!\' "Vryosh\'" is a rude, colloquial "you lie". "V litso" is "in the face", literally "to the face".'),
    (7, None, '\'Chef, I never lie to you.\' "Ne vru" is "I don\'t lie". Max says "never" and "not" together, as ever.'),
    (8, None, '\'The lie detector shows something completely different!\' The detector shows something "completely different", with the neuter "drugoye" for "other thing".'),
    (9, None, '\'This stupid machine simply broke.\' "Slomalas\'" is "broke", with "-s\'" for "broke by itself".'),
    (10, None, '\'Chef, you are like my own father to me.\' "Rodnoy" comes from "rod", kin, so it means "own by blood". Max is laying on flattery.'),
    (11, None, '\'Quickly run to the kitchen and feed people!\' "Begi" is the command "run", and "kormi" is "feed". The two commands are joined by "and".'),
    (12, None, '\'Understood, chef, I will do everything instantly.\' "Slushayus\'" is what a soldier says: "yes, sir". "Momental\'no" is "instantly", from "moment".'),
]
