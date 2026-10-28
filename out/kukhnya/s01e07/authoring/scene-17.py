# Authoring module for kukhnya-s01e07-scene-17.
ID = 'kukhnya-s01e07-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 17
TITLE = 'В гостях у Кости  (Visiting Kostya)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = "Kostya has persuaded Nastya to come back to his flat, and he has made an effort. Then she finds something on the floor, and the mood changes. It's in Russian first."
OPENER = "Slowly now. Kostya is proud of his home, and Nastya sees something he hasn't noticed."
TRANSITION = 'Once more from the top, at full speed.'
OUTRO = "Nastya's list of insults is long and worth hearing again: murderer, monster, cruel. Kostya's reply is simply that it's an ordinary trap. See you next time."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('kostya', 'Настя, добро пожаловать в мою квартиру.', 'Nastya, welcome to my apartment.', [], ''),
    ('nastya', 'У тебя здесь довольно уютно и чисто.', 'It is quite cozy and clean here with you.', [], ''),
    ('kostya', 'Ну, точнее, эта квартира съёмная.', 'Well, more precisely, this apartment is rented.', [(333, 'не моя съемная')], ''),
    ('kostya', 'Вот диван, стул, мягкая подушка.', 'Here is a couch, a chair, a soft pillow.', [(334, 'Диван, стул'), (335, 'Подушка')], ''),
    ('nastya', 'Костя, я всё это отлично вижу.', 'Kostya, I can see all this perfectly.', [(335, 'Кость, я вижу')], ''),
    ('kostya', 'Проходи скорее и садись на диван.', 'Come in quickly and sit on the couch.', [(336, 'Проходи, проходи. Садись')], ''),
    ('nastya', 'Ой, а что это там внизу?', 'Oh, and what is that down there?', [(337, 'Что это?')], ''),
    ('nastya', 'Боже мой, это же мёртвая мышь!', 'My God, that is a dead mouse!', [(338, 'Это…')], ''),
    ('nastya', 'Костя, ты самый настоящий жестокий убийца!', 'Kostya, you are a real cruel murderer!', [(338, 'Ты убийца')], ''),
    ('nastya', 'Ты погубил маленькую беззащитную мышь!', 'You destroyed a little defenseless mouse!', [(339, 'Убил маленькую ни в чем не повинную мышь')], ''),
    ('kostya', 'Настя, но это обычная мышеловка!', 'Nastya, but this is an ordinary mousetrap!', [], ''),
    ('nastya', 'Ты ещё сидишь и спокойно улыбаешься?!', 'You are still sitting and calmly smiling?!', [(340, 'Еще лыбится сидит')], ''),
    ('nastya', 'Ты поступил как настоящий монстр!', 'You acted like a real monster!', [(342, 'Ты вообще монстр')], ''),
]
WALK = [
    (0, None, "'Nastya, welcome to my apartment.' The opening phrase is the formal word for 'welcome', and it is literally close to 'good to come'. Kostya uses it to sound like a host."),
    (1, None, "'It is quite cozy and clean here with you.' 'At you here' is the Russian way to say 'in your place'. The term for 'cozy' is pieced together from the word for 'comfort'."),
    (2, None, "'Well, more precisely, this apartment is rented.' 'More precisely' is a handy phrase for correcting yourself. 'Rented' is made from 'take', as a tenant takes a flat."),
    (3, None, "'Here is a couch, a chair, a soft pillow.' A list with 'here is' needs no verbs. Each noun just follows the last."),
    (4, None, "'Kostya, I can see all this perfectly.' 'I see' is irregular, and a 'zh' sound appears. 'Perfectly' comes from 'excellent'."),
    (5, None, "'Come in quickly and sit on the couch.' The word for 'sit' ends in 'sya', so it is literally 'seat yourself'. 'Onto the couch' takes the ending that means movement."),
    (6, None, "'Oh, and what is that down there?' The little 'a' at the start means 'and' or 'but' and softens the question."),
    (7, None, "'My God, that is a dead mouse!' 'My God' is the usual exclamation. 'dead' agrees with 'mouse', which counts as a she-word."),
    (8, None, "'Kostya, you are a real cruel murderer!' 'The most real' is a way of saying 'a complete'. 'Murderer' comes from 'to kill'."),
    (9, None, "'You destroyed a little defenseless mouse!' 'Defenseless' is 'without' plus 'protection'. 'Destroyed' is a strong word, used for ruin."),
    (10, None, "'Nastya, but this is an ordinary mousetrap!' 'mousetrap' is a compound of 'mouse' and 'catching', so it literally means 'mouse-catcher'."),
    (11, None, "'You are still sitting and calmly smiling?!' 'Still' sits before 'sitting'. 'smiling' ends in 'sya', so it is literally 'smiling oneself'."),
    (12, None, "'You acted like a real monster!' 'Acted' is a word you can use for any behaviour. 'Like' introduces the comparison, and 'monster' is borrowed."),
]
