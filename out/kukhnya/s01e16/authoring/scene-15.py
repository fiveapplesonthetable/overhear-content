# Authoring module for kukhnya-s01e16-scene-15.
ID = 'kukhnya-s01e16-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 15
TITLE = "Освобождение Феди  (Fedya's Release)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'inspector': 'Инспектор', 'barinov': 'Шеф'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'Fedya is still in the fridge, and the inspector has finally got it open. He checks him, finds him clean, and apologises, while Barinov takes the credit. First the Russian.'
OPENER = "Let's replay it one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Fedya is out of the fridge, and nobody is any wiser. The chef's last line, 'let him think so', is one you can borrow whenever you want to let someone believe what they like. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('fedya', 'Шеф, мне очень холодно.', 'Chef, I am very cold.', [(180, 'Шеф, я понял. Вы в паштет базилик добавили, да?')], ''),
    ('fedya', 'Я тут замёрз.', 'I froze in here.', [(180, 'Шеф, я понял. Вы в паштет базилик добавили, да?')], ''),
    ('inspector', 'Чист.', 'Clear.', [(181, 'Чист. Проверили.')], ''),
    ('inspector', 'Проверили.', 'Checked.', [(181, 'Чист. Проверили.')], ''),
    ('barinov', 'Я так и знал.', 'I knew it.', [(182, 'Я так и знал.')], ''),
    ('inspector', 'Виктор Петрович, ошибочка вышла.', 'Viktor Petrovich, a mistake happened.', [(183, 'Ну что же, Виктор Петрович, ошибочка вышла.')], ''),
    ('inspector', 'Мои люди проверили этого человека.', 'My people checked this person.', [(184, 'Оказывается, мои люди уже проверили этого человечка.')], ''),
    ('inspector', 'Абсолютно чист.', 'Completely clean.', [], ''),
    ('barinov', 'А я всегда знал.', 'And I always knew.', [], ''),
    ('barinov', 'Федя, ты как?', 'Fedya, how are you?', [(187, 'Федь, ты как? Нормально.')], ''),
    ('fedya', 'Нормально.', 'Fine.', [(187, 'Федь, ты как? Нормально.')], ''),
    ('fedya', 'Как вы меня вытащили?', 'How did you get me out?', [(188, 'Ты как меня оттуда вытащил?')], ''),
    ('fedya', 'Ключ был только у вас.', 'Only you had the key.', [(189, 'Ключи же только у шефа были.')], ''),
    ('barinov', 'Пусть он так думает.', 'Let him think so.', [(190, 'Вот пусть он и дальше так думает.')], ''),
]
WALK = [
    (0, None, "'Chef, I'm very cold.' Russian says 'to me cold', as if the cold happens to you. 'Cold' ends in 'o' and is cousin to the word for the fridge he was stuck in."),
    (1, None, "'I froze in here.' The past form of 'freeze' ends in a bare consonant for a man, and a woman would add an 'a'. The little word for 'here' is the casual one."),
    (2, None, "'Clean.' The short form drops its ending, so what's left is a bare 'clean', as if reading from a form. It's the inspector's dry verdict."),
    (3, None, "'Checked.' There's no 'he' and no 'we', just the 'li' ending, which says somebody did it. Officials talk like this."),
    (4, None, "'I knew it.' The line is 'I so and knew', and 'so and' is a way of saying 'just as I thought'. The masculine 'l' ending is back."),
    (5, None, "'Viktor Petrovich, a little mistake happened.' 'Little mistake' is a diminutive, a gentler version of 'mistake'. Russian says the mistake 'came out', which also hides who made it."),
    (6, None, "'My people checked this man.' The plural of 'person' is 'lyudi', which looks nothing like the singular. 'This man' takes an 'ogo' ending because it's the thing that was checked."),
    (7, None, "'Completely clean.' The first word is a borrowed 'absolutely', and the second is the same short 'clean' as before. Two words, no sentence needed."),
    (8, None, "'And I always knew.' The small opening 'a' means 'and' with a bit of contrast. 'Always' is the same one you use for habits."),
    (9, None, "'Fedya, how are you?' Literally just 'you how', with no verb at all. The casual 'you' shows how close they are."),
    (10, None, "'Fine.' Literally 'normally', and it's the standard reply to 'how are you'. Russians don't say it with much more enthusiasm than this."),
    (11, None, "'How did you get me out?' Fedya uses the polite 'you' with his boss. 'Pull out' is the picture, as if he was dragged from the fridge."),
    (12, None, "'Only you had the key.' 'The key was only at you' is the literal order. It's the same 'at you' pattern that stands in for 'you have'."),
    (13, None, "'Let him think so.' It begins with 'let', the little word that goes in front of 'he thinks'. Barinov doesn't correct anybody, and the line is quiet and satisfied."),
]
