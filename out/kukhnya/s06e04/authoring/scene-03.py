# Authoring module for kukhnya-s06e04-scene-03.
ID = 'kukhnya-s06e04-scene-03'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 3
TITLE = "Утро у Лёвы дома  (Morning at Lyova's Home)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = 'On his day off, sous-chef Lyova reassures Gulya on the phone before she comes over to meet his mother Vera Ivanovna, who complains that she has already washed all the floors herself.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'When his mother sighs that she needs a female helper in the apartment, Lyova smiles and says one will arrive very soon. Until next time!'
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('lyova', 'Нет, мы договаривались именно на сегодня.', 'No, we agreed specifically on today.', [(38, 'мы договаривались именно на сегодня')], 'adapted'),
    ('lyova', 'Гуля, да не съест она тебя.', 'Gulya, she is not going to eat you up.', [(39, 'да не съест она тебя')], 'adapted'),
    ('lyova', 'Да, до встречи.', 'Yes, see you soon.', [(40, 'Да. До встречи')], 'exact'),
    ('lyova', 'Я тоже тебя очень люблю.', 'I love you very much too.', [(41, 'Да, и я тебя')], 'adapted'),
    ('lyova', 'Все, пока, жду тебя.', 'Alright, bye, I am waiting for you.', [(43, 'Все, пока')], 'adapted'),
    ('guest', 'О, доброе утро!', 'Oh, good morning!', [(44, 'О, доброе утро')], 'exact'),
    ('guest', 'Проснулся наконец, сынок.', 'You finally woke up, son.', [(45, 'Проснулся наконец')], 'adapted'),
    ('guest', 'Хоть у тебя и выходной, мог бы маме помочь.', 'Even though you have a day off, you could have helped your mom.', [(46, 'Хоть у тебя и выходной мог бы маме помочь')], 'exact'),
    ('guest', 'Я уже все полы вымыла.', 'I have already washed all the floors.', [(47, 'Я уже все полы вымыла')], 'exact'),
    ('lyova', 'Ну и зачем, мама?', 'Well and why did you do that, Mom?', [(48, 'Ну и зачем, мам?')], 'adapted'),
    ('lyova', 'Я бы потом все сам сделал.', 'I would have done everything myself later.', [(49, 'Я бы потом все сам сделал')], 'exact'),
    ('guest', 'Да, у тебя все потом.', 'Yes, with you everything is later.', [(50, 'Да, у тебя все потом')], 'exact'),
]
WALK = [
    (0, None, "'No, we agreed specifically on today.' Over the work and the visit, Lyova answers the guest without a second thought."),
    (1, None, "'Gulya, she is not going to eat you up.' Since she is not going to eat the guest up, Lyova does not waste words on excuses."),
    (2, None, "'Yes, see you soon.' Here seeing the guest soon sets up the next turn in their exchange."),
    (3, None, '\'I love you very much too.\' Saying that he loves the guest very much is how Lyova sets the tone with the guest. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (4, None, "'Alright, bye, I am waiting for you.' Because Alright bye he is waiting for the guest, Lyova treats the matter as settled."),
    (5, None, "'Oh, good morning!' Around the shift and conversation, the guest makes his point loud and clear. Russian puts the key word right up front so his emotion lands on the first beat."),
    (6, None, "'You finally woke up, son.' The guest mentions that Lyova finally woke up son so Lyova sees what is at stake."),
    (7, None, "'Even though you have a day off, you could have helped your mom.' Claiming that even though Lyova has a day off Lyova could have helped sounds confident, even if Lyova has doubts."),
    (8, None, "'I have already washed all the floors.' The guest mentions that he has already washed all the floors so Lyova sees what is at stake."),
    (9, None, '\'Well and why did you do that, Mom?\' By wondering why the guest does that Mom, Lyova presses the guest for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (10, None, "'I would have done everything myself later.' Realizing that he would have done everything himself later changes how Lyova handles the situation."),
    (11, None, '\'Yes, with you everything is later.\' Noting that with Lyova everything is later keeps the guest\'s side of the story simple and clear. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
]
