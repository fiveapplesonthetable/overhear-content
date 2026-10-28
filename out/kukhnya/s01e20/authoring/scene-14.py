# Authoring module for kukhnya-s01e20-scene-14.
ID = 'kukhnya-s01e20-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 14
TITLE = 'Новый план  (The New Plan)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = 'Max wins a drinking competition in the kitchen and gets very drunk. He walks into the dining room and interrupts Victoria, who is receiving an expensive birthday gift from an important guest.'
OPENER = "Now let's examine this conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Victoria is very embarrassed in front of the important guest. Drunk Max tries to give Victoria the ring he bought for her, but she is very angry. Next time you watch the episode, listen for the Russian expressions for 'to hear' and 'day' — you will catch every word right away. See you next time!"
CLOSING = ('vika', 'Пока!')
STORY = [
    ('guest', 'Вика, я слышал, у вас день рождения.', 'Vika, I heard it is your birthday.', [(243, 'Итак, приветствуем нового чемпиона.')], ''),
    ('guest', 'У меня есть красивый подарок для вас.', 'I have a beautiful gift for you.', [], ''),
    ('vika', 'Боже мой! Это очень дорогая картина.', 'Oh my God! This is a very expensive painting.', [], ''),
    ('guest', 'Главное, что она вам очень нравится.', 'The main thing is that you like it very much.', [], ''),
    ('vika', 'Спасибо большое, это мой любимый художник.', 'Thank you very much, this is my favorite artist.', [], ''),
    ('max', 'А я смотрю, вы тут хорошо развлекаетесь.', 'And I see you are having good fun here.', [], ''),
    ('vika', 'Макс, что ты делаешь? Иди отсюда.', 'Max, what are you doing? Go from here.', [], ''),
    ('max', 'Я хочу выпить за удивительную девушку.', 'I want to drink to an amazing girl.', [], ''),
    ('vika', 'Макс, ты пьян. Пойдем, выйдем, пожалуйста.', "Max, you are drunk. Let's go out, please.", [], ''),
    ('max', 'Подожди, я еще не подарил свой подарок.', 'Wait, I did not give my gift yet.', [], ''),
    ('vika', 'Мне не нужны твои глупые подарки сейчас.', 'I do not need your stupid gifts now.', [], ''),
    ('max', 'Смотри, это красивое кольцо для тебя.', 'Look, this is a beautiful ring for you.', [], ''),
    ('guest', 'Извините, я, наверное, пойду сейчас.', 'Excuse me, I will probably go now.', [], ''),
    ('vika', 'Нет, останьтесь. Макс, ты сошел с ума!', 'No, stay. Max, you have gone crazy!', [], ''),
]
WALK = [
    (0, None, "'Vika, I heard it is your birthday.' , combining 'heard' with 'day' and 'of birth'."),
    (1, None, "'I have a beautiful gift for you.' , combining 'there is' with 'beautiful' and 'gift'."),
    (2, None, "'Oh my God! This is a very expensive painting.' Russian omits the present-tense verb 'to be' here, linking 'good lord!' directly with 'very much', combining 'good lord!' with 'very much' and 'expensive'."),
    (3, None, "'The main thing is that you like it very much.' the guest expresses this naturally by combining the word for 'important' with 'very much' and 'is pleasing'."),
    (4, None, "'Thank you very much, this is my favorite artist.' Russian omits the present-tense verb 'to be' here, linking 'thank you' directly with 'big', combining 'thank you' with 'big' and 'favourite'."),
    (5, None, "'And I see you are having good fun here.' Max leads with the direct command form meaning 'to have fun', combining 'look' with 'here' and 'good'."),
    (6, None, "'Max, what are you doing? Go from here.' Vika leads with the direct command form meaning 'go', pairing it with 'are you doing' and 'from here'."),
    (7, None, "'I want to drink to an amazing girl.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (8, None, "'Max, you are drunk. Let's go out, please.' Vika puts the word for 'drunk' together with 'let's go' and 'to go out' in a crisp, natural spoken turn of phrase."),
    (9, None, "'Wait, I did not give my gift yet.' Max leads with the direct command form meaning 'wait', pairing it with 'still' and 'donated'."),
    (10, None, "'I do not need your stupid gifts now.' Russian omits the present-tense verb 'to be' here, linking 'needed' directly with 'silly', combining 'needed' with 'silly' and 'presents'."),
    (11, None, "'Look, this is a beautiful ring for you.' Max leads with the direct command form meaning 'look', pairing it with 'beautiful' and 'ring'."),
    (12, None, "'Excuse me, I will probably go now.' , combining 'sorry' with 'probably' and 'go'."),
    (13, None, "'No, stay. Max, you have gone crazy!' Vika uses the action verb meaning 'to remain' to focus on the single completed result, pairing it with 'go mad' and 'mind'."),
]
