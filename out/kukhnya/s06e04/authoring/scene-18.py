# Authoring module for kukhnya-s06e04-scene-18.
ID = 'kukhnya-s06e04-scene-18'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 18
TITLE = 'В больнице у Шефа  (At the Hospital with the Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'doctor': 'Врач', 'eleonora': 'Элеонора'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = 'At the hospital, Barinov regains consciousness as Katya tearfully apologizes for her prank, and Eleonora brings surprising news: sous-chef Lyova fed the real Michelin inspector, who left delighted!'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Even from a hospital bed, Barinov cannot bear the thought that Lyova cooked for the Michelin inspector instead of him. See you next time!'
CLOSING = ('doctor', 'До свидания!')
STORY = [
    ('eleonora', 'С утра здесь было пятнадцать тысяч.', 'This morning there were fifteen thousand here.', [(282, 'С утра здесь было')], 'adapted'),
    ('eleonora', 'Папа, извини, я не хотела, это был глупый розыгрыш.', 'Dad, forgive me, I did not mean to, it was a silly prank.', [(284, 'Папа, извини, я не хотела'), (285, 'розыгрыш')], 'adapted'),
    ('barinov', 'Хорошо, я все запомнил.', 'Alright, I remembered everything.', [(286, 'Хорошо, я все запомнил')], 'exact'),
    ('doctor', 'По поводу лекарств я вам подробно все напишу.', 'Regarding the medicines, I will write everything down for you in detail.', [(287, 'По поводу лекарств я вам подробно все напишу')], 'exact'),
    ('doctor', 'Проследите за ним, я вас очень прошу.', 'Keep an eye on him, I beg you.', [(288, 'Проследите за ним. Я вас очень прошу')], 'exact'),
    ('doctor', 'Боюсь, один он не справится.', 'I am afraid he will not manage on his own.', [(289, 'Боюсь, один он не справится')], 'exact'),
    ('barinov', 'Что там с инспектором?', 'What happened with the inspector?', [(290, 'Что с инспектором?')], 'adapted'),
    ('eleonora', 'Все хорошо, твой повар его накормил.', 'Everything is fine, your chef fed him.', [(290, 'Все хорошо'), (291, 'его накормил')], 'adapted'),
    ('eleonora', 'И просили передать, что инспектор был очень доволен.', 'And they asked to pass along that the inspector was very pleased.', [(292, 'И просили передать, что инспектор был очень доволен')], 'exact'),
    ('barinov', 'Это даже уже не смешно!', 'This is not even funny anymore!', [(293, 'Это даже уже не смешно')], 'exact'),
    ('barinov', 'Когда он придет в третий раз, его что, Айнура будет кормить?', 'When he comes for the third time, is Ainura going to feed him?', [(294, 'Когда он придет в третий раз, его что, Айнура будет кормить?')], 'exact'),
    ('barinov', 'Я все понимаю, но мне надо еще немного поработать.', 'I understand everything, but I need to work a little longer.', [(296, 'я все понимаю. Но мне надо еще немного поработать')], 'adapted'),
]
WALK = [
    (0, None, "'This morning there were fifteen thousand here.' Eleonora tells Barinov that this morning there were fifteen thousand here without dressing it up."),
    (1, None, "'Dad, forgive me, I did not mean to, it was a silly prank.' Since dad forgive her she did not mean to it was a silly prank, Eleonora does not waste words on excuses."),
    (2, None, "'Alright, I remembered everything.' Mentioning that Alright he remembered everything moves the talk in a new direction."),
    (3, None, '\'Regarding the medicines, I will write everything down for you in detail.\' The doctor reminds Barinov that regarding the medicines he will write everything down for Barinov in detail before the moment passes. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (4, None, "'Keep an eye on him, I beg you.' Telling Barinov to keep an eye on him he begs Barinov moves the conversation forward without extra drama."),
    (5, None, "'I am afraid he will not manage on his own.' Mentioning that he is afraid he will not manage on his own moves the talk in a new direction."),
    (6, None, '\'What happened with the inspector?\' Over the hospital and the doctor, Barinov presses the doctor for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (7, None, "'Everything is fine, your chef fed him.' Claiming that everything is fine Barinov's fed him sounds confident, even if Barinov has doubts."),
    (8, None, "'And they asked to pass along that the inspector was very pleased.' Pointing out that they asked to pass along that the inspector was very pleased gives Barinov a sobering reality check."),
    (9, None, '\'This is not even funny anymore!\' Because this is not even funny anymore, Barinov does not bother softening the blow for the doctor. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (10, None, "'When he comes for the third time, is Ainura going to feed him?' Wondering if when he comes for the third time is Ainura going to feed him shows Barinov caught off guard."),
    (11, None, '\'I understand everything, but I need to work a little longer.\' Realizing that he understands everything but he needs to work a little longer changes how Barinov handles the situation. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
]
