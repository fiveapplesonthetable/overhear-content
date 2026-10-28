# Authoring module for kukhnya-s06e20-scene-01.
ID = 'kukhnya-s06e20-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 20
SCENE = 1
TITLE = 'Болт в чечевичном супе  (A Bolt in the Lentil Soup)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.20'
SOURCE_FILE = 'sources/kukhnya/s06/e20.ru.srt'
INTRO = 'At the start of the series finale, Chef Barinov has convinced Elena Pavlovna to let him work in the kitchen for two hours a day. Suddenly, word arrives that a guest found a metal bolt in his lentil soup, and Barinov assumes the guest is a scammer.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Chef Barinov marches into the dining room and makes the foreigner pay for the soup—before seeing the man's business card. Until next time!"
CLOSING = ('barinov', 'Хорошего дня!')
STORY = [
    ('barinov', 'Без меня вы звезду не получите.', 'Without me you will never get a star.', [(2, 'Никогда звезду не получите')], 'adapted'),
    ('senya', 'А Елена Павловна разве не против?', 'And is Elena Pavlovna not against it?', [(3, 'А Елена Павловна не против')], 'adapted'),
    ('barinov', 'Нет, она совсем не против.', 'No, she is not against it at all.', [(4, 'Не против')], 'adapted'),
    ('barinov', 'На два часа я её уговорил.', 'I talked her into two hours a day.', [(4, 'На два часа в день я ее уговорил')], 'adapted'),
    ('fedya', 'Гость нашёл в супе железяку.', 'A guest found a piece of metal in the soup.', [(6, 'нашел какую-то железяку')], 'adapted'),
    ('fedya', 'Гость в супе из чечевицы нашёл.', 'The guest found it in the lentil soup.', [(6, 'Там гость в супе из чечевицы')], 'adapted'),
    ('fedya', 'Теперь он хочет видеть шефа.', 'Now he wants to see the chef.', [(6, 'и хочет видеть шефа')], 'adapted'),
    ('senya', 'Шеф, это же обычный болт.', 'Chef, this is just an ordinary bolt.', [(7, 'Шеф, это болт')], 'adapted'),
    ('barinov', 'Скажите мне, кто это готовил?', 'Tell me, who cooked this?', [(8, 'Кто готовил')], 'adapted'),
    ('barinov', 'Не важно, кто именно готовил.', 'It does not matter who exactly cooked it.', [(9, 'не важно, кто готовил')], 'adapted'),
    ('barinov', 'Очевидно, что это хитрый мошенник.', 'Obviously, this is a clever con artist.', [(10, 'очевидно, что это'), (10, 'мошенник')], 'adapted'),
    ('barinov', 'Сейчас я сам пойду разберусь.', 'Right now I will go sort it out myself.', [(13, 'Сейчас пойду разберусь')], 'adapted'),
]
WALK = [
    (0, None, "'Without me you will never get a star.' Because without him Fedya will never get a star, Barinov treats the matter as settled."),
    (1, None, '\'And is Elena Pavlovna not against it?\' Checking whether Elena Pavlovna not against it is how Senya puts Barinov on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, "'No, she is not against it at all.' Barinov mentions that she is not against it at all so Fedya sees what is at stake."),
    (3, None, "'I talked her into two hours a day.' Claiming that he talked her into two hours a day sounds confident, even if Fedya has doubts."),
    (4, None, "'A guest found a piece of metal in the soup.' Pointing out that a guest found a piece of metal in the soup gives Barinov a sobering reality check."),
    (5, None, "'The guest found it in the lentil soup.' Fedya explains that the guest found it in the lentil soup, keeping his voice calm and direct."),
    (6, None, "'Now he wants to see the chef.' Realizing that he wants to see changes how Fedya handles the situation."),
    (7, None, '\'Chef, this is just an ordinary bolt.\' Noting that this is just an ordinary bolt keeps Senya\'s side of the story simple and clear. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (8, None, '\'Tell me, who cooked this?\' With the soup and conversation hanging in the air, Barinov puts Fedya on the spot. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (9, None, "'It does not matter who exactly cooked it.' Because it does not matter who exactly cooked it, Barinov treats the matter as settled."),
    (10, None, '\'Obviously, this is a clever con artist.\' Saying that obviously this is a clever con artist is how Barinov sets the tone with Fedya. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (11, None, "'Right now I will go sort it out myself.' Once right now he will go sort it out himself, Barinov can finally tell Fedya what he means."),
]
