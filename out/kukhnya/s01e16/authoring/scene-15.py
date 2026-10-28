# Authoring module for kukhnya-s01e16-scene-15.
ID = 'kukhnya-s01e16-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 15
TITLE = "Освобождение Феди  (Fedya's Release)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'inspector': 'Инспектор', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "The inspector has opened the fridge with his own key, and someone is inside, just not the cook everyone was worried about. The man's papers are in order, and the inspector has to apologise. Meanwhile Fedya, who really was hiding, wants to know who got him out."
OPENER = 'Now we stop at the fridge and take it phrase by phrase.'
TRANSITION = 'And the fridge scene once more, all the way through.'
OUTRO = "Fedya is out of the fridge, and the chef has no idea how. Senya's last line, 'pust on tak dumaet', 'let him think so', is one you can borrow whenever you let someone believe what they like. See you next time!"
CLOSING = ('fedya', 'Всё, пока!')
STORY = [
    ('inspector', 'Чист. Мы его проверили.', "He's clean. We checked him.", [(181, 'Чист. Проверили.')], ''),
    ('inspector', 'Виктор Петрович, ошибочка вышла.', 'Viktor Petrovich, there has been a little mistake.', [(183, 'Ну что же, Виктор Петрович, ошибочка вышла.')], ''),
    ('inspector', 'Мои люди уже проверили этого человека.', 'My people have already checked this man.', [(184, 'Оказывается, мои люди уже проверили этого человечка.')], ''),
    ('inspector', 'Он абсолютно чист.', "He's completely clean.", [(185, 'Абсолютно чист.')], ''),
    ('senya', 'Федя, ты как?', 'Fedya, how are you?', [(187, 'Федь, ты как? Нормально.')], ''),
    ('fedya', 'Нормально. Как ты меня вытащил?', 'Fine. How did you get me out?', [(187, 'Нормально.'), (188, 'Ты как меня оттуда вытащил?')], ''),
    ('fedya', 'Ключ же был только у шефа.', 'Only the chef had the key.', [(189, 'Ключи же только у шефа были.')], ''),
    ('senya', 'Пусть он и дальше так думает.', 'Let him keep thinking that.', [(190, 'Вот пусть он и дальше так думает.')], ''),
]
WALK = [
    (0, None, "'He's clean. We checked him.' 'Chist', 'clean', is the short form of 'chisty', the kind used after 'he is'. It's the inspector's word for someone whose papers are in order."),
    (1, None, "'Viktor Petrovich, there has been a little mistake.' 'Oshibochka' is the softened form of 'oshibka', 'mistake'. Russian says the mistake 'vyshla', 'came out', which hides who made it."),
    (2, None, "'My people have already checked this man.' 'Lyudi', 'people', is the plural of 'chelovek', 'person', though the two look nothing alike. 'Etot chelovek' becomes 'etogo cheloveka' because he is the one checked."),
    (3, None, "'He's completely clean.' 'Absolyutno', 'absolutely', is borrowed and easy to spot. 'Chist' is the same short 'clean' as two lines back."),
    (4, None, "'Fedya, how are you?' 'Ty kak?' is literally 'you how?', a friendly check without any verb. Senya uses 'ty' because he and Fedya are mates."),
    (5, None, "'Fine. How did you get me out?' 'Normalno', literally 'normally', is the usual reply to 'how are you'. 'Vytashchil', 'pulled out', is built from 'vy-', 'out', and 'tashchit', 'to drag'."),
    (6, None, "'Only the chef had the key.' 'U shefa', 'at the chef', is the 'have' pattern: after 'u', 'shef' becomes 'shefa'. 'Zhe' means 'after all' here."),
    (7, None, "'Let him keep thinking that.' 'Pust' means 'let', and 'i dalshe' means 'from now on as well', so the line is 'let him go on thinking so'. Senya has a key of his own, and the chef doesn't need to know."),
]
