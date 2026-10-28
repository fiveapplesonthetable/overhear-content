# domashniy-arest/s01e02/scene-01.py
ID = "domashniy-arest-s01e02-scene-01"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = "Всё ради нас  (All for Us)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "angelina", "pasha": "anja"}
LABELS = {"anya": "Аркадий", "vika": "Вика", "pasha": "Паша"}
INTRO = "This series is called House Arrest. But it opens with a flashback to New Year's Eve, before the arrest: Arkady comes home late, and he has brought Pasha with him. Let's listen in Russian first."
STORY = [
    ("anya", "Викуля! Прости, милая, я опоздал.", "Vikulya! Sorry, darling, I'm late.", [(12, 'Викуля'), (15, 'прости, милая')], "'за опоздание' (for being late) -> 'я опоздал' (I'm late)"),
    ("vika", "Привет.", "Hi.", [(18, 'Привет')], "speaker not marked in the subtitles; given to Vika"),
    ("anya", "Дела, дела. Всё ради нас.", "Work, work. It's all for us.", [(16, 'дела, дела'), (16, 'Все ради нас')], "'Ну, все' dropped"),
    ("vika", "Ты же обещал: Новый год только вдвоём.", "But you promised: New Year just the two of us.", [(20, 'Ты же обещал')], "adapted: 'что мы будем Новый год отмечать вдвоем' shortened to 'Новый год только вдвоём'"),
    ("anya", "Вика, ну он одинокий. Я же не оставлю его одного.", "Vika, come on, he's all alone. I can't just leave him on his own.", [(21, 'Вика, ну он одинокий'), (21, 'Я же не оставлю его')], "the cue's ungrammatical second 'одинокий' -> 'одного'"),
    ("pasha", "Добрый вечер, Вика. С Новым годом!", "Good evening, Vika. Happy New Year!", [(26, 'С Новым годом')], "'Добрый вечер, Вика' new; speaker of cue 26 not marked, given to Pasha"),
    ("anya", "Пашуля, проходи, проходи!", "Pashulya, come in, come in!", [(34, 'Пашуля'), (23, 'Проходи, проходи')], "'любимая' (said to Vika) -> 'Пашуля' (cue 22 garbles the nickname)"),
    ("vika", "Подождите, а вы куда?", "Wait, where are you two going?", [(27, 'Подождите, а вы куда')], ""),
    ("anya", "Мы сейчас. Пойдём, Паша.", "We'll be right back. Come on, Pasha.", [(24, 'Мы сейчас'), (25, 'Пойдем')], "'пойдём' (cue 24) shortened to 'Мы сейчас'; 'Паша' added"),
    ("vika", "Там же президент выступает! Надо открыть шампанское.", "But the president is on TV! We have to open the champagne.", [(28, 'выступает'), (28, 'шампанское')], "the president's name -> 'президент'; 'надо шампанское успеть открыть' simplified"),
    ("anya", "Успеем! Президент долго выступает.", "We'll make it! The president always talks for a long time.", [(29, 'Успеем'), (29, 'долго выступает')], "the president's name -> 'Президент'"),
    ("anya", "Это семейный праздник. Как в детстве, с подарками!", "It's a family holiday. Like when we were kids, with presents!", [(30, 'Семейный праздник'), (30, 'в детстве'), (31, 'С подарками')], "'Мы отмечаем его, как было в детстве' shortened; 'и с красотой теплотой' dropped"),
    ("anya", "Паша, давай, не отставай!", "Pasha, come on, keep up!", [(32, 'не отставай')], "'Паша' added"),
    ("pasha", "Иду, Аркаша, иду!", "Coming, Arkasha, coming!", [], "new: Pasha follows Arkady"),
]
OPENER = "Let's go back through it slowly. It's nearly midnight, Arkady is late, and he starts with an apology and a pet name."
WALK = [
    (0, 'Викуля!', "His wife is Vika, and this is a soft, affectionate form of her name. Russians love these little endings on names."),
    (0, 'Прости, милая, я опоздал.', "'Sorry, darling, I'm late.' The first word is a casual 'sorry' between people who say 'you' informally. And notice the last word: it's past tense, literally 'I came late', and because Arkady is a man it has no ending. Vika is not impressed."),
    (1, None, "'Hi.' Just one short word, and rather cool. Arkady explains himself."),
    (2, None, "'Work, work. It's all for us.' The first word means business, things to do, and he says it twice, as if he had no choice. Vika reminds him of a promise."),
    (3, None, "'But you promised: New Year just the two of us.' The little word after 'you' adds 'but, after all'. The last word means 'the two of us together'. The problem is the guest standing behind Arkady."),
    (4, 'Вика, ну он одинокий.', "'Vika, come on, he's all alone.' The small word in the middle is a soft 'come on', 'well'. And who is so lonely?"),
    (4, 'Я же не оставлю его одного.', "'I can't just leave him on his own.' The verb looks like a present but means the future: 'I won't leave'. The guest, of course, is Pasha, his deputy, and he greets Vika politely."),
    (5, None, "'Good evening, Vika. Happy New Year!' The greeting literally says 'with the new year'. You'll hear it everywhere on the last night of December. Arkady waves him inside."),
    (6, None, "'Pashulya, come in, come in!' Another pet name, this time for Pasha, with the same kind of affectionate ending. And then the two men head somewhere else in the house."),
    (7, None, "'Wait, where are you two going?' The word for 'you' is plural here, because she is speaking to both of them. The last word means 'where to', for movement."),
    (8, None, "'We'll be right back. Come on, Pasha.' The first sentence is literally 'we, now', short and casual. Vika points at the television."),
    (9, 'Там же президент выступает!', "'But the president is on TV!' Literally, 'the president is speaking there'. Every New Year's Eve, just before midnight, the president gives a speech on television."),
    (9, 'Надо открыть шампанское.', "'We have to open the champagne.' The first word means 'it's necessary', and the verb after it stays in its basic form. Arkady is not worried."),
    (10, None, "'We'll make it! The president always talks for a long time.' The first word is one verb, 'we'll be in time'. Then he tells her what this night means to him."),
    (11, 'Это семейный праздник.', "'It's a family holiday.' The first word is the handy 'this is', 'it's'."),
    (11, 'Как в детстве, с подарками!', "'Like when we were kids, with presents!' Literally, 'as in childhood'. The little word for 'with' makes the word after it change its ending. A family holiday, says the man who brought his deputy instead of staying home with his wife. He calls Pasha along."),
    (12, None, "'Pasha, come on, keep up!' The middle word is a friendly 'come on', and the command means 'don't fall behind'. Pasha hurries after him."),
    (13, None, "'Coming, Arkasha, coming!' The verb means 'I'm going', and here it's how you say 'I'm coming'. Arkasha is a friendly form of Arkady's name."),
]
TRANSITION = "Now let's hear the whole scene once more, from the front door."
OUTRO = "So Vika is left alone with the champagne while her husband and his deputy disappear into the house. Next we find out where they went; see you then. See you next time!"
CLOSING = ("anya", "Пока!")
