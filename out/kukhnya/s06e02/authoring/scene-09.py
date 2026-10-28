# Authoring module for kukhnya-s06e02-scene-09.
ID = 'kukhnya-s06e02-scene-09'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 9
TITLE = 'Тост за новое меню  (A Toast to the New Menu)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'katya': 'Катя', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = "After closing time, the staff gathers at the bar to celebrate the new menu. Barinov apologizes to Mikhail for covering up Nagiyev's wedding-night indiscretion, while Denis and Nikita eye Katya's wine glass."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "With liquid courage in hand, Nikita heads over to Katya's table first, followed closely by Denis. Until next time!"
CLOSING = ('barinov', 'Всего хорошего!')
STORY = [
    ('mikhail', 'Что случилось, Витя?', 'What happened, Vitya?', [(145, 'Что случилось?')], 'adapted'),
    ('barinov', 'Префект не наелся.', 'The prefect did not eat his fill.', [(145, 'не наелся')], 'adapted'),
    ('barinov', 'Миша, ты меня прости, что я тогда Элеоноре ничего не сказал.', 'Misha, forgive me for not saying anything to Eleonora back then.', [(146, 'Миша, ты меня прости, что я тогда Элеоноре ничего не сказал')], 'exact'),
    ('barinov', 'Ты пойми, для нее это важно.', 'Understand, for her it is important.', [(147, 'Ты пойми, для нее это')], 'adapted'),
    ('mikhail', 'Никаких проблем, Витя.', 'No problem at all, Vitya.', [(148, 'Никаких проблем')], 'adapted'),
    ('barinov', 'За новое меню и за звезду!', 'To the new menu and to the star!', [(149, 'За новое меню и за звезду')], 'adapted'),
    ('mikhail', 'Катя уже третий бокал пьет.', 'Katya is already drinking her third glass.', [(150, 'Катя уже третий бокал пьет')], 'exact'),
    ('katya', 'По-моему, пора идти.', 'In my opinion, it is time to go.', [(151, 'По-моему, пора')], 'adapted'),
    ('mikhail', 'Давай, удачи.', 'Go ahead, good luck.', [(152, 'Давай')], 'adapted'),
    ('katya', 'Ну что, думаешь, пора уже с Катей поговорить?', 'Well, do you think it is time to talk to Katya already?', [(154, 'Ну что, думаешь, пора уж с Катей поговорить?')], 'adapted'),
    ('mikhail', 'Да, а вино где?', 'Yes, and where is the wine?', [(155, 'Да. А вино где?')], 'exact'),
    ('katya', 'Не вопрос, сейчас налью.', 'No question, I will pour right now.', [(158, 'Не вопрос')], 'adapted'),
]
WALK = [
    (0, None, "'What happened, Vitya?' Mikhail inquires point-blank what Barinov is actually getting at here."),
    (1, None, '\'The prefect did not eat his fill.\' Emphasizing the prefect around Mikhail, Barinov chooses "prefekt" ("district prefect") so Mikhail gets the point right away.'),
    (2, None, '\'Misha, forgive me for not saying anything to Eleonora back then.\' Holding firm openly on the spot, Barinov pairs the negative word with "ne" ("not"), since Russian naturally doubles its negatives for emphasis.'),
    (3, None, "'Understand, for her it is important.' Barinov steps in at once watching Mikhail, refusing to let the moment slip past."),
    (4, None, '\'No problem at all, Vitya.\' Emphasizing the problems right here, Mikhail puts the weight on "problem" ("problems", from "problema") as the exchange unfolds.'),
    (5, None, '\'To the new menu and to the star!\' Pointing to the new menu before Mikhail, Barinov leans on "novoye" ("new", a form of "novyy") to give the remark its edge.'),
    (6, None, "'Katya is already drinking her third glass.' Mikhail speaks plainly in this moment, bringing things back to earth after the buildup."),
    (7, None, '\'In my opinion, it is time to go.\' Katya steps in quietly during the talk and uses "po-moyemu" ("in my opinion") to carry the main weight of the thought.'),
    (8, None, '\'Go ahead, good luck.\' Pointing to the luck before Katya, Mikhail starts with "davay" ("come on, let\'s") to invite Katya right into the action.'),
    (9, None, "'Well, do you think it is time to talk to Katya already?' Katya probes plainly if there is more going on behind the scenes."),
    (10, None, '\'Yes, and where is the wine?\' Discussing the wine around Katya, Mikhail centers the remark on "vino" ("wine") without any extra fuss.'),
    (11, None, '\'No question, I will pour right now.\' Dwelling on the question on the spot, the "-sya" ending on "vopros" ("question, matter") marks an action that unfolds mutually or turns back on the speaker.'),
]
