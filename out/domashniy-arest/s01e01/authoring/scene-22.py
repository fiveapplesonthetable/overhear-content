# Authoring module for domashniy-arest-s01e01-scene-22.
ID = 'domashniy-arest-s01e01-scene-22'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 22
TITLE = 'Мы с Пашей  (Pasha and I)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'pasha': 'Паша', 'vika': 'Вика'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "Same little room, a moment later. Last time Pasha admitted that he set up Arkady's arrest himself, and reminded him that all his money is in his wife's name. Now Vika tells Arkady her own secret, and Pasha has the last word. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's take it slowly. Vika starts gently, almost kindly."
TRANSITION = "Let's hear the whole scene one more time."
OUTRO = "In a few minutes Arkady has lost his freedom, his wife and his money. Listen out for that short, cheerful goodbye when you watch, and that's it. See you next time!"
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Аркаша, я понимаю, тебе сейчас тяжело. Но…', "Arkasha, I understand, it's hard for you right now. But...", [(862, 'Аркаша, я понимаю, тебе сейчас'), (862, 'тяжело')], "'без этого' dropped"),
    ('vika', 'Мы с Пашей вместе уже месяц.', 'Pasha and I have been together for a month now.', [(863, 'Мы с Пашей')], "'в месяц как любовники' -> 'вместе уже месяц'"),
    ('arkady', 'Что? Как ты можешь, Вика?', 'What? How could you, Vika?', [(865, 'Как ты можешь, Вика')], "'Что?' added"),
    ('vika', 'Кто бы говорил.', "Look who's talking.", [(866, 'Кто бы говорил')], ''),
    ('arkady', 'Ты жена моя, Вика!', "You're my wife, Vika!", [(870, 'Ты жена моя'), (870, 'Вика')], "'Законная' dropped"),
    ('vika', 'Вспомнил? Я давно тебя не интересую.', "Now you remember? You haven't been interested in me for a long time.", [(871, 'Вспомнил'), (872, 'Я давно тебя не интересую')], ''),
    ('vika', 'А с Пашей я снова чувствую себя женщиной.', 'And with Pasha I feel like a woman again.', [(873, 'А с Пашей я'), (874, 'Снова')], "past 'почувствовала' -> present 'чувствую'"),
    ('arkady', 'Вика, посмотри на него.', 'Vika, look at him.', [(875, 'посмотри на него')], "'да ты' dropped"),
    ('arkady', 'Ему нужны только твои деньги.', 'All he wants is your money.', [(877, 'только твои')], "'бабки' (slang) -> 'деньги'; word order made standard"),
    ('vika', 'То есть меня можно любить только за деньги?', 'So you mean I can only be loved for my money?', [(879, 'То есть'), (879, 'только за деньги')], "'полюбить' -> 'любить'; 'ты хочешь сказать, что' dropped"),
    ('arkady', 'Нет, Вика, я совсем не это хочу сказать.', "No, Vika, that's not what I mean at all.", [(880, 'Нет'), (880, 'я совсем не это')], "'Виктория' -> 'Вика'; 'тебе' dropped"),
    ('vika', 'Какой ты ужасный человек!', 'What a horrible person you are!', [(883, 'Какой ты')], "the insult 'козёл' retold cleanly as 'ужасный человек'"),
    ('arkady', 'Викуля, постой!', 'Vikulya, wait!', [(885, 'Викуля, постой')], ''),
    ('pasha', 'Ладно, Аркашенька. Мы поедем, пора.', "All right, Arkashenka. We'll be off, it's time.", [(887, 'Ладно, Аркашенька'), (888, 'пора')], "'поедем мы' -> 'Мы поедем'"),
    ('pasha', 'У меня много дел. Выборы мэра…', "I've got a lot to do. The mayoral election...", [(890, 'Выборы мэра')], "'дел по горло' -> 'много дел'"),
    ('pasha', 'Потом надо отдать москвичам твои деньги из подвала.', 'Then I have to give your money from the basement to the Moscow people.', [(890, 'москвичам')], "'передать эти деньги твои из подвальчика' simplified"),
    ('pasha', 'Ну и кластер, конечно. Пока!', 'And the cluster, of course. Bye!', [(891, 'Ну и кластер'), (891, 'конечно'), (892, 'Пока')], "'устроить' dropped"),
]
WALK = [
    (0, None, [
        "'Arkasha, I understand, it's hard for you right now. But...' Notice there's no 'it is' in the middle: literally, it translates to ",
        ('vika', 'тебе сейчас тяжело.'),
        " 'to you now hard'. And then the news."
    ]),
    (1, None, [
        "'Pasha and I have been together for a month now.' Literally, the phrase for 'Pasha and I' translates to ",
        ('vika', 'Мы с Пашей'),
        ", 'we with Pasha'. And the action word stays in the present time: they still are together. Arkady is shocked."
    ]),
    (2, None, [
        "'What? How could you, Vika?' Literally, ",
        ('arkady', 'Как ты можешь,'),
        " translates to 'how can you'. Vika has an answer ready."
    ]),
    (3, None, [
        "'Look who's talking.' Word for word, it translates to ",
        ('vika', 'Кто бы говорил.'),
        " 'who would talk'. She knows about his own affairs. So Arkady reminds her who she is."
    ]),
    (4, None, [
        "'You're my wife, Vika!' Here the translation for 'my', ",
        ('arkady', 'моя,'),
        " comes after 'wife', which makes it louder, more emotional. Vika is not moved."
    ]),
    (5, 'Вспомнил?', [
        "'Now you remember?' the expression for 'remembered' is ",
        ('vika', 'Вспомнил?'),
        " which is used for a man, because she is talking to a man."
    ]),
    (5, 'Я давно тебя не интересую.', [
        "'You haven't been interested in me for a long time.' Literally, it translates to ",
        ('vika', 'Я давно тебя не интересую.'),
        " 'I haven't interested you for long'. The first word in it means 'I', not 'you'. Then she explains."
    ]),
    (6, None, [
        "'And with Pasha I feel like a woman again.' which translates to 'like a woman', ",
        ('vika', 'женщиной.'),
        " is just one word here, built from the translation for woman, with an ending that translates to 'as'. Arkady tries to warn her."
    ]),
    (7, None, [
        "'Vika, look at him.' the expression for 'look' is ",
        ('arkady', 'посмотри'),
        " which is a command in the casual style, the one you use with family."
    ]),
    (8, None, [
        "'All he wants is your money.' Literally, it translates to ",
        ('arkady', 'Ему нужны только твои деньги.'),
        " 'to him only your money is needed'. A very useful pattern for saying what someone needs. Vika hears it differently."
    ]),
    (9, None, [
        "'So you mean I can only be loved for my money?' The phrase built from the first two words, ",
        ('vika', 'То есть'),
        " translates to 'that is', or 'so you mean'. Arkady backs off."
    ]),
    (10, None, [
        "'No, Vika, that's not what I mean at all.' the Russian for 'at all', ",
        ('arkady', 'совсем'),
        " sits right before 'not'. Too late."
    ]),
    (11, None, [
        "'What a horrible person you are!' meaning 'what a', ",
        ('vika', 'Какой'),
        " works like 'what a' in English. And she walks out."
    ]),
    (12, None, [
        "'Vikulya, wait!' The name ",
        ('arkady', 'Викуля,'),
        " is built from a tender version of Vika, the name he uses when he wants her back. Now Pasha is the one who speaks."
    ]),
    (13, None, [
        "'All right, Arkashenka. We'll be off, it's time.' The name ",
        ('pasha', 'Аркашенька.'),
        " is built from the sweetest version of Arkady's name, and he doesn't mean it kindly. 'We' means him and Vika. Then he lists his plans."
    ]),
    (14, None, [
        "'I've got a lot to do. The mayoral election...' Literally, the phrase for 'I have' translates to ",
        ('pasha', 'У меня'),
        " 'at me there is', like last time. Pasha is going to run for mayor himself."
    ]),
    (15, None, [
        "'Then I have to give your money from the basement to the Moscow people.' Right then, Arkady's cash, hidden in the basement, is going to his Moscow partners. the translation for the people, ",
        ('pasha', 'москвичам'),
        " comes first, with an ending that translates to 'to'."
    ]),
    (16, None, [
        "'And the cluster, of course. Bye!' The project Arkady blocked, and then the translation for a cheerful goodbye, ",
        ('pasha', 'Пока!'),
        " Pasha has taken everything."
    ]),
]
