# Authoring module for kukhnya-s01e11-scene-12.
ID = 'kukhnya-s01e11-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 12
TITLE = 'Второй критик  (The Second Critic)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "Barinov wants to know about the mystery man at table five, and he asks Nastya, who has been serving him. The answer makes him think of a second critic. Take it in once, and don't worry about the details."
OPENER = 'Now the same thing, but slowly.'
TRANSITION = 'Now put it all together.'
OUTRO = 'The chef now has two possible critics, and a lot to feed them. He sends the menu to the man. The next scene looks at this from another side. Bye for now.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Настя, давно у тебя этот гость?', 'Nastya, how long have you had this guest?', [(160, 'Давно у тебя этот гость?')], ''),
    ('nastya', 'Какой именно гость, шеф?', 'Which guest exactly, chef?', [(160, 'Какой гость?')], ''),
    ('barinov', 'Тот странный мужчина в тёмном пиджаке.', 'That strange man in the dark jacket.', [], ''),
    ('nastya', 'Можно сказать, довольно давно.', 'You could say, quite a long time.', [(161, 'Можно сказать, давно')], ''),
    ('barinov', 'Что он уже успел заказать?', 'What has he already managed to order?', [(162, 'Что он заказал?')], ''),
    ('nastya', 'Пока совершенно ничего, только воду.', 'Nothing at all so far, only water.', [(162, 'Пока ничего')], ''),
    ('nastya', 'Он всё время что-то пишет.', 'He is writing something the whole time.', [(162, 'он все время что-то пишет')], ''),
    ('barinov', 'Он что, известный писатель?', 'Is he some famous writer?', [(162, 'что')], ''),
    ('nastya', 'Вы же говорили про ту девушку!', 'But you were talking about that girl!', [], ''),
    ('barinov', 'Получается, у меня теперь два критика?', 'It turns out I have two critics now?', [], ''),
    ('nastya', 'Что мне теперь делать, шеф?', 'What should I do now, chef?', [], ''),
    ('barinov', 'Немедленно отнеси ему наше фирменное меню.', 'Immediately take him our signature menu.', [], ''),
    ('nastya', 'Я всё сделаю в лучшем виде.', 'I will do everything in the best way.', [], ''),
]
WALK = [
    (0, None, '\'Nastya, how long have you had this guest?\' Russian has two words for "long". "Davno" looks back from now, "since long ago", and "dolgo" measures a stretch of time. Barinov asks "davno u tebya".'),
    (1, None, '\'Which guest exactly, chef?\' "Kakoy imenno" is "which exactly". "Imenno" is the word Barinov used in "chto imenno ey ne ponravilos". Nastya is not sure which guest he means.'),
    (2, None, '\'That strange man in the dark jacket.\' "Tyomny", "dark", is the dark of Max\'s "tyomny shokolad". "V tyomnom pidzhake" is "in a dark jacket", with -e on "pidzhake" after "v".'),
    (3, None, '\'You could say, quite a long time.\' "Mozhno skazat", "it is possible to say", is "you could say". "Mozhno" is the opposite of "nelzya". "Dovolno davno" is "rather long ago".'),
    (4, None, '\'What has he already managed to order?\' "Uspel", "managed", means "had time to". It is the verb Lyova used in "my uspeem vsyo sdelat vovremya", "we will manage everything in time".'),
    (5, None, '\'Nothing at all so far, only water.\' "Poka", "so far", is the word that also means "bye". "Sovershenno nichego" is "completely nothing". "Vodu" is "voda", "water", as the thing he ordered.'),
    (6, None, '\'He is writing something the whole time.\' Add -to to a question word and it goes vague: "chto", "what", becomes "chto-to", "something", just as "gde" becomes "gde-to", "somewhere". "Vsyo vremya", "all the time", is the everyday "constantly".'),
    (7, None, '\'Is he some famous writer?\' "Izvestny", "famous", literally means "known". "Pisatel", "writer", is "one who writes", from "pisat", "to write". "On chto" is "what, is he".'),
    (8, None, '\'But you were talking about that girl!\' The little "zhe" is "but you know". "Pro tu devushku" is "about that girl". Nastya points out what the chef said earlier.'),
    (9, None, '\'It turns out I have two critics now?\' "Poluchaetsya", "it comes out", is the usual Russian for "it turns out". After "dva", "two", the word is "kritika", not "kritiki".'),
    (10, None, '\'What should I do now, chef?\' "Chto mne delat" is "what to me to do", with no word for "should". The plain form "delat" carries it. Nastya asks for orders.'),
    (11, None, '\'Immediately take him our signature menu.\' "Otnesi" is "take away to", the carrying "nesti" with ot-. "Firmennoe", "signature", is the word in Lyova\'s "firmennoe myaso".'),
    (12, None, '\'I will do everything in the best way.\' "V luchshem vide", "in the best form", is the promise Lyova made to Barinov: "sdelayu vsyo v luchshem vide". Nastya says it the same way.'),
]
