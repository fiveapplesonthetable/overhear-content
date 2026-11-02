# Authoring module for kukhnya-s01e15-scene-02.
ID = 'kukhnya-s01e15-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 2
TITLE = 'Лишний сосед  (An Extra Roommate)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "It's late, and Nastya and Kostya are in bed. Then Max walks in and suggests a trip to the cinema. Russian first."
OPENER = "Now we take it apart, slowly."
TRANSITION = 'Now the bedroom scene, in full.'
OUTRO = "Nastya has finally run out of patience with the third roommate, and she wants him gone. Talk soon."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Это моя мочалка, а это Костина.', "This is my loofah, and this one is Kostya's.", [(6, 'Это моя мочалка, а это Костина.')], ''),
    ('max', 'Слышь, народ, давай в кино сходим?', 'Hey, guys, let us go to the cinema?', [(7, 'Слышь, народ, давай в кино сходим')], ''),
    ('kostya', 'Макс, мы спим уже давно.', 'Max, we have been sleeping for a long time.', [(8, 'Макс, мы спим')], ''),
    ('nastya', 'Да. Точнее, мы спали.', 'Yes. More precisely, we were sleeping.', [(9, 'Да. Точнее, спали')], ''),
    ('max', 'Ну, давай попозже сходим вместе.', 'Well, let us go later together.', [(10, 'Ну, давай попозже сходим')], ''),
    ('kostya', 'Ты же видишь, что мы отдыхаем.', 'You see that we are resting.', [], ''),
    ('nastya', 'Иди спать, пожалуйста, Макс!', 'Go to sleep, please, Max!', [(11, 'Спать')], ''),
    ('max', 'Ну, понятно, я ухожу к себе.', 'Well, understood, I am going to my room.', [(12, 'Ну, понятно')], ''),
    ('nastya', 'Всё, я так больше не могу!', 'That is it, I cannot take this anymore!', [(13, 'Все. Я так больше не могу.')], ''),
    ('kostya', 'Настя, успокойся, он просто наш друг.', 'Nastya, calm down, he is just our friend.', [], ''),
    ('nastya', 'Он постоянно заходит в нашу комнату!', 'He constantly walks into our room!', [], ''),
    ('nastya', 'Я хочу, чтобы Макс съехал отсюда!', 'I want Max to move out of here!', [(14, 'Я хочу, чтоб Макс съехал')], ''),
]
WALK = [
    (0, None, ["'This is my loofah, and this one is Kostya's.' The scrubby bath sponge is ", ('nastya', 'мочалка'), ". Kostya's is made by turning the name into a describing word, ", ('nastya', 'Костина'), '.']),
    (1, None, ["'Hey, guys, let us go to the cinema?' Now we can inspect this line: ", ('max', 'Слышь'), ' is clipped from do you hear, and it is a rough, matey hey. ', ('max', 'народ'), ' means people, used here like folks. ', ('max', 'сходим'), ' means going somewhere and coming back.']),
    (2, None, ["'Max, we have been sleeping for a long time.' Russian uses the plain present, ", ('kostya', 'спим'), ', along with already for a long time. English needs have been, and Russian does not.']),
    (3, None, ["'Yes. More precisely, we were sleeping.' We can analyze the words: ", ('nastya', 'Точнее'), ' is precisely, with the ending for more, the same one in faster. ', ('nastya', 'спали'), ' is the plural past, we slept.']),
    (4, None, ["'Well, let us go later together.' We can break down the words: ", ('max', 'попозже'), ' is later, with a prefix to make it a bit later. The action word, ', ('max', 'сходим'), ', waits until the end of the line.']),
    (5, None, ["'You see that we are resting.' The short term ", ('kostya', 'же'), ' makes it sound like come on, you can see. We rest also means we are resting.']),
    (6, None, ["'Go to sleep, please, Max!' We will examine this line: ", ('nastya', 'Иди'), ('nastya', 'спать'), ' is go sleep, two actions side by side, with no to. Nastya says it with a polite please squeezed in the middle.']),
    (7, None, ["'Well, understood, I am going to my room.' Let's inspect this part: ", ('max', 'понятно'), ' means it is clear, and Russians say it to mean I get it. ', ('max', 'к'), ('max', 'себе'), ' is to oneself, so to my own place.']),
    (8, None, ["'That is it, I cannot take this anymore!' Let's analyze the phrase: ", ('nastya', 'Всё'), ' at the start works like a full stop: that is it. The rest reads as I so more not can, with ', ('nastya', 'не'), ' right before the action it cancels.']),
    (9, None, ["'Nastya, calm down, he is just our friend.' We can analyze the words: ", ('kostya', 'успокойся'), ' ends in a bit that means calm yourself. Notice for friend is ', ('kostya', 'друг'), ', and ', ('kostya', 'просто'), ' means just, playing it down.']),
    (10, None, ["'He constantly walks into our room!' The prefix on the front of ", ('nastya', 'заходит'), ' gives drop in. The term for room becomes ', ('nastya', 'комнату'), ' after the term for into.']),
    (11, None, ["'I want Max to move out of here!' Russian says I want that Max moved out, with the past form after ", ('nastya', 'чтобы'), '. The moving word ', ('nastya', 'съехал'), ' is built from ride off.']),
]
