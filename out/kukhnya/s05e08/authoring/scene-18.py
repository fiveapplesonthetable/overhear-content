# Authoring module for kukhnya-s05e08-scene-18.
ID = 'kukhnya-s05e08-scene-18'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 8
SCENE = 18
TITLE = 'Извинения перед шейхом  (Apologies to the Sheikh)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.08'
SOURCE_FILE = 'sources/kukhnya/s05/e08.ru.srt'
INTRO = "When the sheikh demands an explanation for the commotion in his suite, Max explains that the interpreter has been using His Highness's name to seduce the waitresses. The sheikh fires the interpreter on the spot."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'With the interpreter exposed and the sheikh appeased, the staff hurry back downstairs to the restaurant. See you next time!'
CLOSING = ('senya', 'Хорошего дня!')
STORY = [
    ('guest', 'Что здесь происходит?', 'What is happening here?', [(190, 'Что происходит')], 'adapted'),
    ('max', 'Извините нас, пожалуйста.', 'Excuse us, please.', [(191, 'Извините')], 'adapted'),
    ('max', 'Это ваш переводчик виноват.', "It is your interpreter's fault.", [(192, 'Ваш переводчик')], 'adapted'),
    ('max', 'Он использует ваше имя в своих целях.', 'He is using your name for his own purposes.', [(193, 'Использует ваше имя')], 'adapted'),
    ('guest', 'Прошу прощения, он будет уволен.', 'I beg your pardon, he will be fired.', [(194, 'Прошу прощения. Он будет уволен')], 'adapted'),
    ('senya', 'Что он сейчас сказал?', 'What did he just say?', [(195, 'Что он сказал')], 'adapted'),
    ('guest', 'Сказал, что если мы не извинимся, то нас уволят.', 'He said that if we do not apologize, we will be fired.', [(195, 'Сказал, что если мы не извинимся, то нас уволят')], 'adapted'),
    ('senya', 'Извините нас, пожалуйста!', 'Excuse us, please!', [(196, 'Извините')], 'adapted'),
    ('max', 'Извините, ребята, мы уже уходим.', 'Excuse us, guys, we are leaving already.', [(198, 'Извините, ребята')], 'adapted'),
    ('senya', 'Больше такого не повторится!', 'This will never happen again!', [(197, 'Извините. Извините')], 'adapted'),
    ('guest', 'Можете возвращаться к работе.', 'You may return to work.', [(194, 'Прошу прощения')], 'adapted'),
    ('max', 'Пошли отсюда скорее на кухню.', 'Let us get out of here to the kitchen quickly.', [(198, 'ребята. Извините')], 'adapted'),
]
WALK = [
    (0, None, '\'What is happening here?\' By asking what happening here is, the guest presses Max for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (1, None, "'Excuse us, please.' Claiming that the guest should excuse them please sounds confident, even if the guest has doubts."),
    (2, None, '\'It is your interpreter\'s fault.\' Once it is the guest\'s interpreter fault, Max can finally tell the guest what he means. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (3, None, '\'He is using your name for his own purposes.\' By being using the guest\'s name for his own purposes, Max keeps his side of the story grounded. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (4, None, "'I beg your pardon, he will be fired.' Because he begs Max's pardon he will be fired, the guest treats the matter as settled."),
    (5, None, '\'What did he just say?\' Asking what he just say cuts straight through the tension between Senya and the guest. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (6, None, "'He said that if we do not apologize, we will be fired.' Mentioning that he said that if they do not apologize they will be fired moves the talk in a new direction."),
    (7, None, "'Excuse us, please!' Here telling the guest to excuse them please lets Senya's real feelings break through."),
    (8, None, "'Excuse us, guys, we are leaving already.' Since the guest should excuse them guys they are leaving already, Max does not waste words on excuses."),
    (9, None, "'This will never happen again!' Senya insists that this will never happen again, leaving the guest no room to argue. Russian puts the key word right up front so his emotion lands on the first beat."),
    (10, None, "'You may return to work.' The guest mentions that Max may return to work so Max sees what is at stake."),
    (11, None, "'Let us get out of here to the kitchen quickly.' Proposing that they get out of here to the kitchen quickly moves the conversation forward without extra drama."),
]
