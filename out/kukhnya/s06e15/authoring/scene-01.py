# Authoring module for kukhnya-s06e15-scene-01.
ID = 'kukhnya-s06e15-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 15
SCENE = 1
TITLE = 'Пора всё рассказать  (Time to Tell Everything)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'katya': 'Катя', 'sveta': 'Света'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.15'
SOURCE_FILE = 'sources/kukhnya/s06/e15.ru.srt'
INTRO = "Welcome to Episode Fifteen of Kukhnya Season Six. Denis and Katya are secretly meeting behind Sveta's and Nikita's backs, and they agree that they must tell the truth to their partners tomorrow so they can stop hiding."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Denis and Katya postpone their difficult confession until the next day so they do not ruin the movie night. Until next time!'
CLOSING = ('denis', 'Хорошего дня!')
STORY = [
    ('denis', 'Спокойной тебе ночи и сладких снов.', 'Good night to you and sweet dreams.', [(1, 'Спокойной ночи')], 'adapted'),
    ('katya', 'Сейчас всё выглядит очень некрасиво.', 'Right now everything looks very bad.', [(2, 'Все сейчас выглядит именно так')], 'adapted'),
    ('katya', 'Поэтому мы должны всё честно рассказать.', 'Therefore we must tell everything honestly.', [(3, 'мы все должны рассказать')], 'adapted'),
    ('katya', 'Ты скажешь Свете, а я Никите.', 'You will tell Sveta, and I will tell Nikita.', [(4, 'Свете, а я Никите')], 'adapted'),
    ('katya', 'Нам пора наконец перестать так прятаться.', 'It is time for us to finally stop hiding like this.', [(4, 'перестать прятаться')], 'adapted'),
    ('denis', 'Я только за такое хорошее решение.', 'I am all for such a good decision.', [(5, 'Я только за')], 'adapted'),
    ('sveta', 'Денис, скорее, мы в кино опаздываем!', 'Denis, hurry, we are running late for the cinema!', [(6, 'мы в кино опаздываем')], 'adapted'),
    ('sveta', 'Катя, а ты уже совсем готова?', 'Katya, are you completely ready already?', [(8, 'ты готова')], 'adapted'),
    ('sveta', 'А вы не пойдёте с нами?', 'Are you not coming with us?', [(9, 'с нами в кино')], 'adapted'),
    ('katya', 'Ну, в принципе, можно и пойти.', 'Well, in principle, we can go.', [(10, 'Ну, можно')], 'adapted'),
    ('sveta', 'Пойдём, мы вас на улице подождём.', 'Let us go, we will wait for you outside.', [(11, 'Мы вас на улице подождем')], 'adapted'),
    ('denis', 'Ладно, тогда уже завтра всё расскажем.', 'Alright, then we will tell everything tomorrow.', [(13, 'тогда уже завтра расскажем')], 'adapted'),
    ('katya', 'Конечно, ведь сегодня мы идём в кино.', 'Of course, since today we are going to the cinema.', [(14, 'Сегодня же кино')], 'adapted'),
]
WALK = [
    (0, None, '\'Good night to you and sweet dreams.\' Addressing the night on the spot, Denis chooses "spokoynoy" ("good", from the root "spokoynyy") so Katya hears the exact meaning.'),
    (1, None, '\'Right now everything looks very bad.\' Katya speaks up pointedly before Denis and chooses "nekrasivo" ("impolite, not nice") so Denis gets the point right away.'),
    (2, None, "'Therefore we must tell everything honestly.' Katya reacts frankly in this moment, making her position completely clear."),
    (3, None, '\'You will tell Sveta, and I will tell Nikita.\' Katya jumps in pointedly during the talk and lands on "skazhesh" ("will you say", built on "skazat") to keep the statement grounded.'),
    (4, None, '\'It is time for us to finally stop hiding like this.\' Turning quietly right here, Katya leans on "pora" ("it is time to"), which carries the whole predicate in Russian without needing "it is".'),
    (5, None, "'I am all for such a good decision.' Denis follows up plainly with a sigh, testing Katya's reaction in the middle of the exchange."),
    (6, None, '\'Denis, hurry, we are running late for the cinema!\' Talking about the cinema before Denis, Sveta reaches for the Russian word "opazdyvayem" ("are late", built from "opazdyvat") right at the center of the line.'),
    (7, None, '\'Katya, are you completely ready already?\' Emphasizing how ready things are during the talk, Sveta adds "sovsem" ("completely, at all") so the statement leaves zero room for doubt.'),
    (8, None, "'Are you not coming with us?' Sveta quizzes earnestly while looking straight at Katya here."),
    (9, None, '\'Well, in principle, we can go.\' Talking about the principle on the spot, Katya brings in "printsipe" ("principle", from "printsip") as the key Russian word here.'),
    (10, None, "'Let us go, we will wait for you outside.' Sveta speaks up bluntly watching Katya, testing Katya's reaction in the middle of the exchange."),
    (11, None, "'Alright, then we will tell everything tomorrow.' Denis answers briskly in their talk, to clear the air between them once and for all."),
    (12, None, '\'Of course, since today we are going to the cinema.\' Talking about the cinema in this beat, Katya chooses "konechno" ("of course") so Denis gets the point right away.'),
]
