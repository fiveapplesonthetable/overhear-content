# Authoring module for kukhnya-s06e01-scene-10.
ID = 'kukhnya-s06e01-scene-10'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 10
TITLE = 'Неожиданная гостья и пианист  (The Unexpected Guest and the Pianist)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'eleonora': 'Элеонора', 'katya': 'Катя', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = "After the oligarch introduces his wife Kristina—Nagiyev's own ex-wife—Katya confronts Eleonora for firing Denis, forcing Mikhail to improvise an excuse on the spot."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Katya insists it is merely a matter of principle, while Mikhail scrambles to bring Denis back before the ceremony. See you next time!'
CLOSING = ('katya', 'Пока!')
STORY = [
    ('eleonora', 'Давайте я вам покажу ваш номер.', 'Let me show you to your suite.', [(175, 'Давайте я вам покажу ваш номер')], 'exact'),
    ('mikhail', 'Выручай, мне срочно нужен пианист на вечер.', 'Help me out, I urgently need a pianist for the evening.', [(177, 'Выручай, мне срочно нужен пианист на вечер')], 'exact'),
    ('katya', 'Это так ты не вмешиваешься в мою личную жизнь?', 'Is this how you do not interfere in my personal life?', [(179, 'Это так ты не вмешиваешься в мою личную жизнь?')], 'exact'),
    ('eleonora', 'Успокойся, Катя.', 'Calm down, Katya.', [(180, 'Успокойся')], 'adapted'),
    ('katya', 'Ты сама взяла и уволила Дениса.', 'You went ahead and fired Denis yourself.', [(181, 'а сама взяла и уволила Дениса')], 'adapted'),
    ('eleonora', 'Может быть, он сам ушел?', 'Maybe he left on his own?', [(183, 'может быть, он сам ушел?')], 'adapted'),
    ('eleonora', 'Миша, а где пианист?', 'Misha, where is the pianist?', [(185, 'Миша, а где пианист?')], 'exact'),
    ('mikhail', 'Какой пианист?', 'Which pianist?', [(186, 'Какой пианист?')], 'exact'),
    ('eleonora', 'Пианист, которого Дима привел, найди его.', 'The pianist whom Dima brought, find him.', [(186, 'Пианист, которого Дима привел'), (187, 'Найди его')], 'adapted'),
    ('mikhail', 'Я его отправил переодеваться, ужасный пиджак.', 'I sent him to change clothes, an awful jacket.', [(189, 'Я его отправил переодеваться. Ужасный пиджак')], 'adapted'),
    ('eleonora', 'Ну видишь, будет твой Денис.', 'Well you see, your Denis will be here.', [(190, 'Ну, видишь, будет твой Денис')], 'adapted'),
    ('katya', 'Ты прекрасно знаешь, что мы расстались.', 'You know very well that we broke up.', [(192, 'Ты прекрасно знаешь, что мы расстались')], 'exact'),
]
WALK = [
    (0, None, "'Let me show you to your suite.' By letting her show Katya to Katya's suite, Eleonora keeps her side of the story grounded."),
    (1, None, "'Help me out, I urgently need a pianist for the evening.' Adding that Eleonora should help him out he urgently need a pianist for the evening fills in the missing piece for Eleonora."),
    (2, None, '\'Is this how you do not interfere in my personal life?\' Checking whether this how Eleonora does not interfere in her personal life cuts straight through the tension between Katya and Eleonora. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (3, None, "'Calm down, Katya.' Pointing out that Katya should calm down gives Katya a sobering reality check."),
    (4, None, '\'You went ahead and fired Denis yourself.\' Adding that Eleonora went ahead and fired Denis themselves fills in the missing piece for Eleonora. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (5, None, '\'Maybe he left on his own?\' Questioning whether maybe he left on his own is how Eleonora tests Katya\'s story. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (6, None, "'Misha, where is the pianist?' Asking where the pianist is cuts straight through the tension between Eleonora and Katya."),
    (7, None, '\'Which pianist?\' Over the moment and the suit, Mikhail presses Eleonora for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (8, None, "'The pianist whom Dima brought, find him.' Eleonora reminds Katya that the pianist whom Dima brought find him before the moment passes."),
    (9, None, "'I sent him to change clothes, an awful jacket.' Because he sent him to change clothes an awful jacket, Mikhail treats the matter as settled."),
    (10, None, '\'Well you see, your Denis will be here.\' Explaining that Katya\'s Denis will be here lays the cards on the table for Katya. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (11, None, '\'You know very well that we broke up.\' With the truth and suit in play, Katya keeps this short reply brisk and direct. Speaking with the close, informal "you" strips away any polite distance between them.'),
]
