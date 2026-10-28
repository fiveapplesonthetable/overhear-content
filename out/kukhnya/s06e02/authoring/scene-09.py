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
    (0, None, "'What happened, Vitya?' Mikhail inquires point-blank while looking straight at Barinov here."),
    (1, None, '\'The prefect did not eat his fill.\' Barinov picks one direct element in earnest: "prefekt" means "district prefect", and it carries the main weight of what Barinov is saying.'),
    (2, None, '\'Misha, forgive me for not saying anything to Eleonora back then.\' Barinov makes this line right away: the word "prosti" ("forgive me") is a warmer, more personal apology than a routine "excuse me".'),
    (3, None, "'Understand, for her it is important.' Barinov proceeds at once hearing Mikhail, to clear the air between them once and for all."),
    (4, None, '\'No problem at all, Vitya.\' Mikhail underscores one concrete piece right here: "problem" means "problems" (from "problema"), giving the line its exact edge.'),
    (5, None, "'To the new menu and to the star!' Barinov answers quietly as they talk, making his position completely clear."),
    (6, None, "'Katya is already drinking her third glass.' Mikhail speaks up plainly across the room, so Barinov knows he is not just making small talk."),
    (7, None, '\'In my opinion, it is time to go.\' Katya favors this direct piece right here: "po-moyemu" means "in my opinion", and it carries the main weight of what Katya is saying.'),
    (8, None, '\'Go ahead, good luck.\' Mikhail brings this warning beside Barinov: starting with "davay" is the classic everyday Russian way to say "come on, let\'s do this" between people on close terms.'),
    (9, None, "'Well, do you think it is time to talk to Katya already?' Katya probes plainly what Mikhail is actually getting at here."),
    (10, None, '\'Yes, and where is the wine?\' Mikhail favors one direct term on cue: "vino" means "wine", and it carries the main weight of what Mikhail is saying.'),
    (11, None, '\'No question, I will pour right now.\' Katya sends this warning toward Mikhail: the "-sya" ending on "vopros" ("question, matter") turns the action inward or makes it happen between people naturally.'),
]
