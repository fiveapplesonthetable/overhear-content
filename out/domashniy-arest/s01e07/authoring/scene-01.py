# domashniy-arest/s01e07/scene-01.py
ID = "domashniy-arest-s01e07-scene-01"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 1
TITLE = "Положительная динамика  (Positive Dynamics)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "marina": "angelina", "samson": "anja"}
LABELS = {"anya": "Аркадий", "marina": "Марина", "samson": "Самсон"}
INTRO = "Today the neighbors are gathered around the communal kitchen table for a small party celebrating Ivan Samsonov's official registration as a candidate for city mayor. While Nina politely says goodbye to her lawyer friend Danya and Ilona reports that the campaign posters will be printed tomorrow, Arkady raises a glass and flirts shamelessly with his neighbor Marina Sergeyevna. Let's listen in Russian first."
STORY = [
    ("samson", "У нас сегодня праздник! Меня официально зарегистрировали кандидатом в мэры.", "We have a celebration today! They officially registered me as a candidate for mayor.", [(4, 'У нас сегодня'), (4, 'официально зарегистрировали')], "Nina's announcement in cues 4-5 folded into Samson's role; 'фуршет по случаю того' -> 'праздник'"),
    ("samson", "А мне вообще всё равно! Нет, я кандидат, я чай!", "I don't care at all! No, I am a candidate, I'm having tea!", [(10, 'А мне вообще все равно'), (20, 'Нет, я кандидат, я чай')], "cues 7-9 (Danya leaving) narrated"),
    ("anya", "Друзья, я предлагаю выпить за успех! Все вместе, как одна большая семья.", "Dear friends, I propose we drink to success! All together, like one big family.", [(30, 'друзья'), (31, 'я предлагаю выпить за успех'), (37, 'Все вместе, как одна'), (38, 'большая семья')], "cues 22-29 (Klavdia's dream and Ilona's print shop news) narrated"),
    ("marina", "Вы что делаете? Вы прекрасно знаете, что вы делаете!", "What are you doing? You know perfectly well what you are doing!", [(42, 'Вы что делаете'), (44, 'Вы прекрасно знаете, что вы делаете')], ""),
    ("marina", "Вы ведёте себя как подросток! Вы приударяете за мной.", "You are behaving like a teenager! You are flirting with me.", [(45, 'Вы ведете себя, как подросток, вы приударяете за мной')], ""),
    ("anya", "Что за слово такое глупое — приударяете?", "What kind of silly word is that — flirting?", [(46, 'Что за слово такое глупое'), (47, 'Приударяете')], ""),
    ("anya", "Да, я оказываю вам знаки внимания. Потому что вы мне нравитесь!", "Yes, I am showing you signs of attention. Because I like you!", [(48, 'Да, я оказываю вам знаки внимания, потому что'), (49, 'потому что вы мне нравитесь')], ""),
    ("marina", "Как интересно! Но между нами ничего быть не может.", "How interesting! But nothing can happen between us.", [(50, 'Как интересно'), (52, 'между нами'), (52, 'быть не может')], "cue 52 garbled 'чего' -> 'ничего'"),
    ("anya", "Да, конечно, понимаю. А почему? Из-за Эдуарда Валентиновича?", "Yes, of course, I understand. But why? Because of Eduard Valentinovich?", [(53, 'Да, конечно, понимаю'), (54, 'А почему'), (55, 'Эдуардом Валентиновичем')], "cue 55 'порочной связи с' simplified"),
    ("marina", "При чём здесь Эдуард Валентинович? Я ничего к вам не чувствую.", "What does Eduard Valentinovich have to do with it? I feel nothing toward you.", [(56, 'при чем здесь Эдуард Валентинович'), (58, 'ничего'), (58, 'к вам не чувствую')], ""),
    ("anya", "Так это замечательно! Раньше вы чувствовали ко мне отвращение.", "Well, that is wonderful! Before, you felt disgust toward me.", [(59, 'Так это замечательно'), (60, 'Раньше вы чувствовали ко мне отвращение')], ""),
    ("anya", "А теперь ничего не чувствуете! Значит, скоро влюбитесь.", "And now you feel nothing! That means you will fall in love soon.", [(60, 'а теперь ничего не чувствуете'), (61, 'Значит, скоро влюбитесь')], ""),
    ("anya", "Динамика положительная!", "The trend is positive!", [], "cue 61 garbled 'Динамик-то положительный' -> 'Динамика положительная!'"),
    ("marina", "Ой, разговор окончен! Фу на вас!", "Oh, the conversation is over! Shame on you!", [(62, 'Ой, разговор окончен'), (64, 'Фу на вас')], ""),
    ("anya", "Я всё равно вас добьюсь, Марина!", "I will win you over anyway, Marina!", [(63, 'Я все равно вас добьюсь, Марина')], ""),
]
OPENER = "Now let's walk through the kitchen celebration and Arkady's conversation with Marina line by line. Nina invites the neighbors into the kitchen to celebrate."
WALK = [
    (0, 'У нас сегодня праздник!', "'We have a celebration today!' Literally 'by us today is a holiday'."),
    (0, 'Меня официально зарегистрировали кандидатом в мэры.', "'They officially registered me as a candidate for mayor.' Notice the 'with/as' form on 'candidate' after the registration verb."),
    (1, 'А мне вообще всё равно!', "'I don't care at all!' When Nina's polite lawyer friend Danya excuses himself and leaves, jealous Samson pretends not to care."),
    (1, 'Нет, я кандидат, я чай!', "'No, I am a candidate, I'm having tea!' Samson refuses champagne while Klavdia Viktorovna mutters about a bad dream and Ilona announces that the campaign posters will be printed tomorrow."),
    (2, 'Друзья, я предлагаю выпить за успех!', "'Friends, I propose we drink to success!' Arkady rises to offer a toast."),
    (2, 'Все вместе, как одна большая семья.', "'All together, like one big family.' Meanwhile, Arkady keeps handing Marina clean forks and glasses until she confronts him."),
    (3, None, "'What are you doing? You know perfectly well what you are doing!' Marina addresses him with the polite plural pronoun."),
    (4, 'Вы ведёте себя как подросток!', "'You are behaving like a teenager!' Literally 'you lead yourself like a teenager'."),
    (4, 'Вы приударяете за мной.', "'You are flirting with me.' This old-fashioned colloquial verb takes the preposition for 'behind' plus the 'with/as' form."),
    (5, None, "'What kind of silly word is that — flirting?' Arkady is amused by her old-fashioned phrasing."),
    (6, 'Да, я оказываю вам знаки внимания.', "'Yes, I am showing you signs of attention.' Literally 'I render to you signs of attention'."),
    (6, 'Потому что вы мне нравитесь!', "'Because I like you!' In Russian, the person you like is the grammatical subject and 'to me' is in the 'to/for' form."),
    (7, None, "'How interesting! But nothing can happen between us.' Literally 'between us nothing to be cannot'."),
    (8, None, "'Yes, of course, I understand. But why? Because of Eduard Valentinovich?' Arkady brings up her former university dean."),
    (9, 'При чём здесь Эдуард Валентинович?', "'What does Eduard Valentinovich have to do with it?' A useful idiom for asking how someone is relevant."),
    (9, 'Я ничего к вам не чувствую.', "'I feel nothing toward you.' Notice the double negative with 'nothing' and 'not'."),
    (10, None, "'Well, that is wonderful! Before, you felt disgust toward me.' Arkady treats her answer as fantastic news."),
    (11, None, "'And now you feel nothing! That means you will fall in love soon.' The self-action verb form verb means 'you will fall in love'."),
    (12, None, "'The trend is positive!' Literally 'positive dynamics', like a rising chart in an economics report."),
    (13, None, "'Oh, the conversation is over! Shame on you!' The short passive form marks the discussion as finished."),
    (14, None, "'I will win you over anyway, Marina!' This phrase means 'I will achieve my goal' or 'win you over'."),
]
TRANSITION = "Now let's listen to the full kitchen scene again from start to finish."
OUTRO = "From disgust to indifference — in Arkady's mind, that is unmistakable progress toward true love. See you next time!"
CLOSING = ("anya", "Пока!")
