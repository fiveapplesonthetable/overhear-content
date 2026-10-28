# domashniy-arest/s01e01/scene-22.py
ID = "domashniy-arest-s01e01-scene-22"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 22
TITLE = "Мы с Пашей  (Pasha and I)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
VOICES = {"narrator": "sky", "vika": "angelina", "anya": "alisa", "pasha": "anja"}
LABELS = {"vika": "Вика", "anya": "Аркадий", "pasha": "Паша"}
INTRO = "Same little room, a moment later. Last time Pasha admitted that he set up Arkady's arrest himself, and reminded him that all his money is in his wife's name. Now Vika tells Arkady her own secret, and Pasha has the last word. We'll hear it in Russian first; don't worry about catching every word."
STORY = [
    ("vika", "Аркаша, я понимаю, тебе сейчас тяжело. Но…", "Arkasha, I understand, it's hard for you right now. But...", [(862, 'Аркаша, я понимаю, тебе сейчас'), (862, 'тяжело')], "'без этого' dropped"),
    ("vika", "Мы с Пашей вместе уже месяц.", "Pasha and I have been together for a month now.", [(863, 'Мы с Пашей')], "'в месяц как любовники' -> 'вместе уже месяц'"),
    ("anya", "Что? Как ты можешь, Вика?", "What? How could you, Vika?", [(865, 'Как ты можешь, Вика')], "'Что?' added"),
    ("vika", "Кто бы говорил.", "Look who's talking.", [(866, 'Кто бы говорил')], ""),
    ("anya", "Ты жена моя, Вика!", "You're my wife, Vika!", [(870, 'Ты жена моя'), (870, 'Вика')], "'Законная' dropped"),
    ("vika", "Вспомнил? Я давно тебя не интересую.", "Now you remember? You haven't been interested in me for a long time.", [(871, 'Вспомнил'), (872, 'Я давно тебя не интересую')], ""),
    ("vika", "А с Пашей я снова чувствую себя женщиной.", "And with Pasha I feel like a woman again.", [(873, 'А с Пашей я'), (874, 'Снова')], "past 'почувствовала' -> present 'чувствую'"),
    ("anya", "Вика, посмотри на него.", "Vika, look at him.", [(875, 'посмотри на него')], "'да ты' dropped"),
    ("anya", "Ему нужны только твои деньги.", "All he wants is your money.", [(877, 'только твои')], "'бабки' (slang) -> 'деньги'; word order made standard"),
    ("vika", "То есть меня можно любить только за деньги?", "So you mean I can only be loved for my money?", [(879, 'То есть'), (879, 'только за деньги')], "'полюбить' -> 'любить'; 'ты хочешь сказать, что' dropped"),
    ("anya", "Нет, Вика, я совсем не это хочу сказать.", "No, Vika, that's not what I mean at all.", [(880, 'Нет'), (880, 'я совсем не это')], "'Виктория' -> 'Вика'; 'тебе' dropped"),
    ("vika", "Какой ты ужасный человек!", "What a horrible person you are!", [(883, 'Какой ты')], "the insult 'козёл' retold cleanly as 'ужасный человек'"),
    ("anya", "Викуля, постой!", "Vikulya, wait!", [(885, 'Викуля, постой')], ""),
    ("pasha", "Ладно, Аркашенька. Мы поедем, пора.", "All right, Arkashenka. We'll be off, it's time.", [(887, 'Ладно, Аркашенька'), (888, 'пора')], "'поедем мы' -> 'Мы поедем'"),
    ("pasha", "У меня много дел. Выборы мэра…", "I've got a lot to do. The mayoral election...", [(890, 'Выборы мэра')], "'дел по горло' -> 'много дел'"),
    ("pasha", "Потом надо отдать москвичам твои деньги из подвала.", "Then I have to give your money from the basement to the Moscow people.", [(890, 'москвичам')], "'передать эти деньги твои из подвальчика' simplified"),
    ("pasha", "Ну и кластер, конечно. Пока!", "And the cluster, of course. Bye!", [(891, 'Ну и кластер'), (891, 'конечно'), (892, 'Пока')], "'устроить' dropped"),
]
OPENER = "Let's take it slowly. Vika starts gently, almost kindly."
WALK = [
    (0, None, "'Arkasha, I understand, it's hard for you right now. But...' Notice there's no 'it is' in the middle: Russians just say 'to you now hard'. And then the news."),
    (1, None, "'Pasha and I have been together for a month now.' Literally, 'we with Pasha'. That's how Russians say 'Pasha and I'. And the verb stays in the present: they still are together. Arkady is shocked."),
    (2, None, "'What? How could you, Vika?' Literally, 'how can you'. Vika has an answer ready."),
    (3, None, "'Look who's talking.' Word for word, 'who would talk'. She knows about his own affairs. So Arkady reminds her who she is."),
    (4, None, "'You're my wife, Vika!' Here 'my' comes after 'wife', which makes it louder, more emotional. Vika is not moved."),
    (5, 'Вспомнил?', "'Now you remember?' One word: 'remembered', in the masculine past, because she is talking to a man."),
    (5, 'Я давно тебя не интересую.', "'You haven't been interested in me for a long time.' Literally, 'I haven't interested you for long'. The first word in it means 'I', not 'you'. Then she explains."),
    (6, None, "'And with Pasha I feel like a woman again.' 'Like a woman' is just one word here, with an ending that means 'as'. Arkady tries to warn her."),
    (7, None, "'Vika, look at him.' A command in the casual form, the one you use with family."),
    (8, None, "'All he wants is your money.' Literally, 'to him only your money is needed'. A very useful pattern for saying what someone needs. Vika hears it differently."),
    (9, None, "'So you mean I can only be loved for my money?' The first two words mean 'that is', or 'so you mean'. Arkady backs off."),
    (10, None, "'No, Vika, that's not what I mean at all.' The word for 'at all' sits right before 'not'. Too late."),
    (11, None, "'What a horrible person you are!' The first word works like 'what a' in English. And she walks out."),
    (12, None, "'Vikulya, wait!' Vikulya is a tender form of Vika, the name he uses when he wants her back. Now Pasha is the one who speaks."),
    (13, None, "'All right, Arkashenka. We'll be off, it's time.' He uses the sweetest form of Arkady's name, and he doesn't mean it kindly. 'We' means him and Vika. Then he lists his plans."),
    (14, None, "'I've got a lot to do. The mayoral election...' To say 'I have', it's 'at me there is', like last time. Pasha is going to run for mayor himself."),
    (15, None, "'Then I have to give your money from the basement to the Moscow people.' Arkady's cash, hidden in the basement, is going to his Moscow partners. The people come first, with an ending that means 'to'."),
    (16, None, "'And the cluster, of course. Bye!' The project Arkady blocked, and then a cheerful goodbye. Pasha has taken everything."),
]
TRANSITION = "Let's hear the whole scene one more time."
OUTRO = "In a few minutes Arkady has lost his freedom, his wife and his money. Listen out for that short, cheerful goodbye when you watch, and. See you next time!"
CLOSING = ("vika", "Пока!")
