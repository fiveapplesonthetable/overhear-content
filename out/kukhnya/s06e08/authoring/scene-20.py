# Authoring module for kukhnya-s06e08-scene-20.
ID = 'kukhnya-s06e08-scene-20'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 8
SCENE = 20
TITLE = 'Запоздавший перелом  (The Late Fracture)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'inspector': 'Инспектор', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.08'
SOURCE_FILE = 'sources/kukhnya/s06/e08.ru.srt'
INTRO = 'In the final scene of episode eight, Senya accidentally slams his finger right after midnight and marches into the insurance office expecting his sixty-thousand-ruble payout.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Missing his insurance deadline by just an hour and a half leaves Senya with a bandaged finger and an empty wallet. See you next time!'
CLOSING = ('senya', 'До завтра!')
STORY = [
    ('fedya', 'Что случилось, дайте сюда быстрее холодный лёд!', 'What happened, bring cold ice here quickly!', [(331, 'Что случилось? Сань, лед дай, лед')], 'adapted'),
    ('fedya', 'Смотрите, он всё-таки сломал себе палец!', 'Look, he broke his finger after all!', [(334, 'Сломал всё-таки')], 'adapted'),
    ('fedya', 'А ну-ка, покажи мне скорее свою руку.', 'Come on, show me your hand quickly.', [(335, 'А ну покажи, покажи')], 'adapted'),
    ('inspector', 'Ваш страховой полис действовал ровно до вчерашнего дня.', 'Your insurance policy was valid right until yesterday.', [(336, 'Ваш страховой полис действовал до')], 'adapted'),
    ('senya', 'Да, совершенно верно, я это прекрасно помню.', 'Yes, quite right, I remember that very well.', [(337, 'Да')], 'adapted'),
    ('inspector', 'А справку в больнице вы получили уже ночью.', 'And you received the hospital certificate late at night.', [(338, 'А справку в больнице вы получили полвторого ночи')], 'adapted'),
    ('inspector', 'То есть вы просто немного не успели вовремя.', 'That means you simply missed the deadline by a little.', [(339, 'То есть вы просто не успели')], 'adapted'),
    ('senya', 'Не понял, я что, денег теперь не получу?', 'I do not get it, will I not receive the money now?', [(340, 'я не понял? Чё, я денег не получил, что ли')], 'adapted'),
    ('inspector', 'Увы, выплата по этому полису уже невозможна.', 'Alas, a payout under this policy is no longer possible.', [(341, 'Увы')], 'adapted'),
    ('senya', 'Выходит, я совершенно зря свой палец ломал?', 'So it turns out I broke my finger completely in vain?', [(342, 'Я что, зря палец ломал')], 'adapted'),
    ('fedya', 'Не получилось у тебя сегодня хитро заработать, Сеня.', 'Your clever scheme to make money today did not work out, Senya.', [(343, 'Да, Сень, не получилось у тебя')], 'adapted'),
    ('inspector', 'Скажите, новый страховой полис оформлять будем?', 'Tell me, shall we sign you up for a new insurance policy?', [(344, 'Новый страховой полис оформлять будем')], 'adapted'),
]
WALK = [
    (0, None, '\'What happened, bring cold ice here quickly!\' Highlighting the ice at once, Fedya chooses "kholodnyy" ("cold") so the inspector gets the point right away.'),
    (1, None, "'Look, he broke his finger after all!' Fedya responds firmly toward the inspector, leaving no doubt about where he stands."),
    (2, None, '\'Come on, show me your hand quickly.\' Highlighting the hand right here, Fedya chooses "pokazhi" ("show", from the root "pokazat") so the inspector hears the exact meaning.'),
    (3, None, "'Your insurance policy was valid right until yesterday.' The inspector reacts firmly during the talk, steering the talk right where he wants it."),
    (4, None, "'Yes, quite right, I remember that very well.' Senya speaks steadily without any doubt, letting the remark speak for itself."),
    (5, None, '\'And you received the hospital certificate late at night.\' Focusing on the hospital in the exchange, the inspector lands on "bolnitse" ("the hospital", built on "bolnitsa") to keep the statement grounded.'),
    (6, None, '\'That means you simply missed the deadline by a little.\' Turning smoothly in front of Senya, the inspector uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (7, None, "'I do not get it, will I not receive the money now?' Senya quizzes frankly why things suddenly took this turn between them."),
    (8, None, '\'Alas, a payout under this policy is no longer possible.\' Pointing out how impossible things are before Senya, the inspector puts the weight on "nevozmozhna" ("impossible", from "nevozmozhnyy") as the exchange unfolds.'),
    (9, None, "'So it turns out I broke my finger completely in vain?' Mentioning his finger on the spot, Senya keeps normal statement word order here, turning the line into a question for Fedya purely through rising pitch."),
    (10, None, "'Your clever scheme to make money today did not work out, Senya.' Fedya replies honestly in this moment, keeping the focus on what actually matters here."),
    (11, None, '\'Tell me, shall we sign you up for a new insurance policy?\' Emphasizing the insurance policy in front of Fedya, the inspector leans on "strakhovoy" ("insurance") to give the whole sentence its punch.'),
]
