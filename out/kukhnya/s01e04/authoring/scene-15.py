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
OUTRO = 'Max narrowly escapes, and sprints back to the stove. You\'ve heard "slushayus\'", the soldier\'s "yes, sir", which Max uses whenever the chef gives an order.'
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
    (0, None, '\'Lavrov, come here right now.\' "Podoydi" is "come up", with "pod-", up to. The surname, "Lavrov", marks a serious talk.'),
    (1, None, '\'Chef, can I already go to the kitchen?\' Just like English "can go", "mogu", I can, is followed by a plain infinitive, "idti", to go on foot. "Uzhe", already, slips in between them.'),
    (2, None, '\'Wait! Did you cook lunch for the cooks?\' "Podozhdi" is the familiar "wait". "Dlya povarov" is "for the cooks", with -ov.'),
    (3, None, '\'Yes, of course, I already made everything.\' "Sdelal" is "did" or "made", with the man\'s -l. "Uzhe" is "already".'),
    (4, None, '\'Is everything definitely ready? You aren\'t deceiving me?\' "Tochno" is "for sure". "Obmanyvayesh\'" is from "obman", a deception.'),
    (5, None, '\'Well, almost cooked, very little is left.\' "Pochti" is "almost". "Ostalos\'", is left, takes the neuter -o because nothing named is the subject.'),
    (6, None, '\'You are lying to my face again!\' "Vryosh\'" is the blunt everyday "you lie", from "vrat\'". "V litso" is "into the face".'),
    (7, None, '\'Chef, I never lie to you.\' "Nikogda ne vru" is "never not lie", the double negative. "Vam" is the polite "to you".'),
    (8, None, '\'The lie detector shows something completely different!\' Literally, "the detector of lie": "lozh\'", a lie, turns into "lzhi" in the "of" form. "Drugoye", other, is neuter because the thing it shows has no name.'),
    (9, None, '\'This stupid machine simply broke.\' "Slomalas\'" is "broke", with -s\' for breaking by itself and -a for "mashina".'),
    (10, None, '\'Chef, you are like my own father to me.\' "Rodnoy", one\'s own, is from "rod", kin. "Kak rodnoy otets" is "like a blood father".'),
    (11, None, '\'Quickly run to the kitchen and feed people!\' Two ty commands back to back, "begi", run, and "kormi", feed. After "kormi", "lyudi", people, becomes "lyudey".'),
    (12, None, '\'Understood, chef, I will do everything instantly.\' "Slushayus\'" is the soldier\'s "yes, sir", literally "I obey". "Momental\'no" is "instantly", from "moment".'),
]
