# Authoring module for kukhnya-s06e20-scene-04.
ID = 'kukhnya-s06e20-scene-04'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 20
SCENE = 4
TITLE = 'Тест на отцовство  (The Paternity Test)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.20'
SOURCE_FILE = 'sources/kukhnya/s06/e20.ru.srt'
INTRO = "At the apartment, Nastya points out how much little Styopa loves his grandfather, while her mother wants to throw the man out immediately. Nastya's father proposes doing a DNA paternity test, sparking an argument over whether they need saliva, blood, or hair."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Each family member secretly resolves to collect their own DNA sample, while back at the hotel Mikhail continues spinning his tale to Malouda. See you next time!'
CLOSING = ('guest', 'До свидания!')
STORY = [
    ('nastya', 'Ну какой же он маньяк?', 'Well, what kind of maniac is he?', [(49, 'какой маньяк')], 'adapted'),
    ('nastya', 'Посмотри, как ребёнок его любит.', 'Look how much the child loves him.', [(50, 'Ты посмотри, как'), (50, 'его любит')], 'adapted'),
    ('nastya', 'Маленькие дети всё сразу чувствуют.', 'Little children sense everything right away.', [(51, 'сразу чувствуют')], 'adapted'),
    ('guest', 'Лучше его выгнать на всякий случай.', 'Better to kick him out just in case.', [(52, 'Но лучше его выгнать. На всякий случай')], 'adapted'),
    ('nastya', 'Нет, лучше оставить его дома.', 'No, better to let him stay at home.', [(53, 'лучше оставить')], 'adapted'),
    ('guest', 'Надо сделать тест на отцовство.', 'We need to do a paternity test.', [(55, 'Надо сделать тест на отцовство')], 'adapted'),
    ('nastya', 'Это просто отличная идея, папа!', 'That is simply a great idea, Dad!', [(56, 'Отличная идея')], 'adapted'),
    ('nastya', 'Я об этом в кино видела.', 'I saw about that in the movies.', [(57, 'в кино видела')], 'adapted'),
    ('nastya', 'Для теста нужно взять слюну.', 'For the test we need to take saliva.', [(57, 'что для теста нужно слюну взять')], 'adapted'),
    ('guest', 'Там обязательно надо кровь брать.', 'They definitely need to take blood there.', [(58, 'Там кровь брать надо')], 'adapted'),
    ('nastya', 'А я читала, нужны волосы.', 'And I read that hair is needed.', [(59, 'читала, что волосы надо')], 'adapted'),
    ('guest', 'Нет, для анализа нужна слюна.', 'No, saliva is needed for the test.', [(60, 'Нет, там слюна')], 'adapted'),
]
WALK = [
    (0, None, "'Well, what kind of maniac is he?' Asking whether what kind of maniac is he puts the guest right on the defensive."),
    (1, None, "'Look how much the child loves him.' Explaining that how much the child loves him lays the cards on the table for the guest."),
    (2, None, "'Little children sense everything right away.' Between the test and the kitchen, Nastya gives the guest a quick, grounded response."),
    (3, None, "'Better to kick him out just in case.' With the test and moment in play, the guest keeps this short reply brisk and direct."),
    (4, None, "'No, better to let him stay at home.' Pointing out that better to let him stay at home gives the guest a sobering reality check."),
    (5, None, '\'We need to do a paternity test.\' Explaining that they need to do a paternity test lays the cards on the table for Nastya. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (6, None, "'That is simply a great idea, Dad!' Because that is simply a great idea dad, Nastya does not bother softening the blow for the guest."),
    (7, None, "'I saw about that in the movies.' Noting that she saw about that in the movies keeps Nastya's side of the story simple and clear."),
    (8, None, "'For the test we need to take saliva.' Around the secret and kitchen, Nastya sets a calm, everyday tone with the guest. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (9, None, "'They definitely need to take blood there.' Around the secret and shift, the guest sets a calm, everyday tone with Nastya."),
    (10, None, "'And I read that hair is needed.' Reading that hair is needed is how Nastya lays out the situation for the guest."),
    (11, None, "'No, saliva is needed for the test.' Once saliva is needed for the test, the guest can finally tell Nastya what he means."),
]
