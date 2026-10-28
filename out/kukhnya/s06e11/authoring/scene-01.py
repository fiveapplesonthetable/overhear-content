# Authoring module for kukhnya-s06e11-scene-01.
ID = 'kukhnya-s06e11-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 11
SCENE = 1
TITLE = 'Утро после праздника  (The Morning After the Party)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'fedya': 'Федя', 'sveta': 'Света'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.11'
SOURCE_FILE = 'sources/kukhnya/s06/e11.ru.srt'
INTRO = "Welcome to Episode Eleven of Kukhnya Season Six. The morning after Senya's wild birthday party, Fedya teases Denis about his tequila-fueled kiss with Sveta, and seconds later Sveta announces that she just broke up with her boyfriend Misha because of Denis."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Denis is horrified to learn Sveta dumped her boyfriend over a staged kiss, while in the dining room Barinov spots his arch-rival at Eleonora's table. Until next time!"
CLOSING = ('denis', 'Хорошего дня!')
STORY = [
    ('fedya', 'Там сейчас свежее мясо должны привезти, проконтролируй.', 'They are supposed to deliver fresh meat there right now, go check it.', [(3, 'Там все мясо должны привезти')], 'adapted'),
    ('denis', 'Сеня, вчера вечеринка у тебя получилась отличная.', 'Senya, your party yesterday turned out great.', [(4, 'вчера получилась')], 'adapted'),
    ('fedya', 'Денис, расскажи, как у тебя со Светой?', 'Denis, tell me, how are things with you and Sveta?', [(6, 'как у тебя со Светкой')], 'adapted'),
    ('denis', 'Никак, это было просто чтобы Катя поревновала.', 'Nothing at all, that was just to make Katya jealous.', [(7, 'Никак'), (10, 'Это просто, чтобы Катя')], 'adapted'),
    ('fedya', 'Видел я вчера, как у вас после текилы было.', 'I saw yesterday how it was with you two after tequila.', [(8, 'Видел я, как у вас после текилы было никак')], 'adapted'),
    ('denis', 'Да правда ничего у нас с ней нет.', 'Honestly there is nothing going on between her and me.', [(11, 'Ничего у нас нет')], 'adapted'),
    ('sveta', 'Всё, Миша, пока, не звони мне больше.', 'That is it, Misha, bye, do not call me anymore.', [(11, 'Все, Миша, пока'), (12, 'Не звони мне больше')], 'adapted'),
    ('denis', 'Привет, Света, с кем ты сейчас говорила?', 'Hi, Sveta, who were you talking to just now?', [(13, 'Привет'), (14, 'С кем болтала')], 'adapted'),
    ('sveta', 'Со своим парнем, точнее его уже нет.', 'With my boyfriend, or rather he is gone now.', [(15, 'С парнем'), (17, 'Уже нет')], 'adapted'),
    ('sveta', 'Вчера я пришла домой и не смогла врать.', 'Yesterday I came home and could not lie to him.', [(18, 'Вчера я пришла домой, поняла, что не могу ему врать')], 'adapted'),
    ('sveta', 'Я рассказала о нашем поцелуе, и мы расстались.', 'I told him about our kiss, and we broke up.', [(19, 'Рассказала о нашем поцелуи, и мы расстались')], 'adapted'),
    ('sveta', 'Но я думаю, это даже к лучшему.', 'But I think that is even for the best.', [(20, 'Ну, это даже к лучшему')], 'adapted'),
    ('fedya', 'Слушай, а Света знает, что у вас ничего нет?', 'Listen, does Sveta know that there is nothing between you two?', [(22, 'Светка-то знает, что у вас ничего нет')], 'adapted'),
]
WALK = [
    (0, None, "'They are supposed to deliver fresh meat there right now, go check it.' Fedya mentions that they are supposed to deliver fresh meat there right now go check it so Denis sees what is at stake."),
    (1, None, '\'Senya, your party yesterday turned out great.\' Claiming that Fedya\'s party yesterday turned out great sounds confident, even if Fedya has doubts. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (2, None, '\'Denis, tell me, how are things with you and Sveta?\' Questioning whether tell him how are things with Denis and Sveta is how Fedya tests Denis\'s story. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (3, None, "'Nothing at all, that was just to make Katya jealous.' Denis explains that nothing at all that was just to make Katya jealous, keeping his voice calm and direct."),
    (4, None, '\'I saw yesterday how it was with you two after tequila.\' Realizing that he saw yesterday how it was with Denis two after tequila changes how Fedya handles the situation. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (5, None, '\'Honestly there is nothing going on between her and me.\' Noting that there is nothing going on between her and him keeps Denis\'s side of the story simple and clear. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (6, None, "'That is it, Misha, bye, do not call me anymore.' Saying that that is it Misha bye do not call her anymore is how Sveta sets the tone with Denis."),
    (7, None, '\'Hi, Sveta, who were you talking to just now?\' Wondering who Fedya talking to just now was cuts straight through the tension between Denis and Fedya. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (8, None, "'With my boyfriend, or rather he is gone now.' Saying that with her boyfriend or rather he is gone now is how Sveta sets the tone with Denis."),
    (9, None, "'Yesterday I came home and could not lie to him.' Once yesterday she came home and could not lie to him, Sveta can finally tell Denis what she means."),
    (10, None, "'I told him about our kiss, and we broke up.' Adding that she told him about their kiss and they broke up fills in the missing piece for Denis."),
    (11, None, '\'But I think that is even for the best.\' Adding that she thinks that is even for the best fills in the missing piece for Denis. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (12, None, "'Listen, does Sveta know that there is nothing between you two?' Checking whether Sveta know that there is nothing between Denis two is how Fedya puts Denis on the spot."),
]
