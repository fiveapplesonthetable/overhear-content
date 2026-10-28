# Authoring module for kukhnya-s06e12-scene-16.
ID = 'kukhnya-s06e12-scene-16'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 12
SCENE = 16
TITLE = 'Приступ откровенности в отеле  (An Outbreak of Honesty in the Hotel)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'eleonora': 'Элеонора', 'sveta': 'Света'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.12'
SOURCE_FILE = 'sources/kukhnya/s06/e12.ru.srt'
INTRO = 'Having eaten the spiked navy-style pasta, the hotel staff loses all ability to lie: a waiter tells Eleonora to her face that she looks terrible with dark circles under her eyes, and the receptionist warns guests away from a smelly room. Meanwhile, Sveta asks Denis for his apartment keys.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Forgetting that Kostya's anniversary ring for Nastya is sitting in that exact jacket pocket, Denis sends Sveta straight to the locker room. See you next time!"
CLOSING = ('denis', 'Всего хорошего!')
STORY = [
    ('denis', 'Здравствуйте, Элеонора Андреевна, выглядите вы сегодня не очень.', 'Hello, Eleonora Andreevna, you do not look very good today.', [(256, 'Здравствуйте'), (258, 'Ну, выглядите не очень')], 'adapted'),
    ('denis', 'У вас синяки под глазами, вчера опять пили?', 'You have dark circles under your eyes, were you drinking again yesterday?', [(259, 'Синяки под глазами. Опять пили, да')], 'adapted'),
    ('eleonora', 'Что ты говоришь, ты что себе вообще позволяешь?', 'What are you saying, what do you think you are doing?', [(260, 'Что? Ты что себе позволяешь')], 'adapted'),
    ('denis', 'Уважаемые гости, лучше не берите этот дорогой номер.', 'Dear guests, you had better not take this expensive room.', [(261, 'Лучше не берите этот номер')], 'adapted'),
    ('eleonora', 'Егор, что ты такое говоришь, я тебя уволю!', 'Egor, what are you saying, I will fire you!', [(264, 'Егор, ты что несешь? Я тебя уволю')], 'adapted'),
    ('denis', 'Элеонора Андреевна, с такой маленькой зарплатой я сам уволюсь.', 'Eleonora Andreevna, with such a small salary I will quit myself.', [(265, 'с такой зарплатой я сам уволюсь')], 'adapted'),
    ('eleonora', 'Так, что здесь происходит, где вообще Михаил Джекович?', 'Alright, what is going on here, where on earth is Mikhail Dzhekovich?', [(266, 'Так, что происходит'), (267, 'Где Михаил')], 'adapted'),
    ('denis', 'Он отдыхает в номере и просил никому не говорить.', 'He is resting in a room and asked not to tell anyone.', [(269, 'Просил никому не говорить')], 'adapted'),
    ('sveta', 'Денис, ты сейчас идёшь домой после работы?', 'Denis, are you going home after work right now?', [(270, 'идешь')], 'adapted'),
    ('denis', 'Сейчас доиграю песню и пойду, а ты куда?', 'I will finish playing the song now and go, and where are you going?', [(271, 'Сейчас доиграю, пойду. А ты')], 'adapted'),
    ('sveta', 'Я очень устала с ночи, поеду домой к нам, дашь ключи?', 'I am very tired from the night shift, I will go home to our place, will you give me the keys?', [(272, 'Нет, я устала с ночи'), (273, 'Я домой поеду. К нам'), (274, 'Дашь ключи')], 'adapted'),
    ('denis', 'Конечно, возьми сама, они лежат в куртке в раздевалке.', 'Of course, take them yourself, they are in my jacket in the locker room.', [(275, 'Они в куртке, в раздевалке')], 'adapted'),
]
WALK = [
    (0, None, "'Hello, Eleonora Andreevna, you do not look very good today.' Mentioning that Eleonora does not look very good today moves the talk in a new direction."),
    (1, None, '\'You have dark circles under your eyes, were you drinking again yesterday?\' Wondering if Eleonora has dark circles under Eleonora\'s eyes were Eleonora drinking again yesterday shows Denis caught off guard. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (2, None, '\'What are you saying, what do you think you are doing?\' By wondering what Denis saying what do Denis thinks Denis is doing is, Eleonora presses Denis for a straight answer. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (3, None, "'Dear guests, you had better not take this expensive room.' Explaining that dear guests Eleonora had better not take this expensive room lays the cards on the table for Eleonora."),
    (4, None, '\'Egor, what are you saying, I will fire you!\' Once someone what are Denis saying she will fire Denis, Eleonora makes sure Denis hears every word. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (5, None, "'Eleonora Andreevna, with such a small salary I will quit myself.' Claiming that with such a small salary he will quit himself sounds confident, even if Eleonora has doubts."),
    (6, None, "'Alright, what is going on here, where on earth is Mikhail Dzhekovich?' Wondering if Alright what is going on here where on earth is Mikhail Dzhekovich shows Eleonora caught off guard."),
    (7, None, "'He is resting in a room and asked not to tell anyone.' Adding that he is resting in a room and asked not to tell anyone fills in the missing piece for Eleonora."),
    (8, None, '\'Denis, are you going home after work right now?\' Asking whether Denis going home after work right now is how Sveta puts Denis on the spot. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (9, None, "'I will finish playing the song now and go, and where are you going?' Denis asks whether he will finish playing the song now and go and where are Eleonora going, refusing to let the point slide."),
    (10, None, '\'I am very tired from the night shift, I will go home to our place, will you give me the keys?\' Here being very tired from the night shift she will go home to their place will Denis gives her the keys shows Sveta looking for the real truth. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (11, None, "'Of course, take them yourself, they are in my jacket in the locker room.' Taking them themselves they are in his jacket in the locker room moves the conversation forward without extra drama."),
]
