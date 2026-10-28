# Authoring module for kukhnya-s02e01-scene-04.
ID = 'kukhnya-s02e01-scene-04'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 1
SCENE = 4
TITLE = 'Плохие новости  (Bad News)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'kristina': 'Кристина', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.01'
SOURCE_FILE = 'sources/kukhnya/s02/e01.ru.dual.srt'
INTRO = "Near the bar at Claude Monet, waitress Sasha runs into Kristina and begs her to ask her husband Dmitry Nagiyev to overturn Victoria's firing. Kristina reveals shocking news of her own and orders a drink from Kostya. Let us listen to their conversation in Russian first."
OPENER = "Now let us examine Sasha and Kristina's conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Hoping for help after losing her job, Sasha learns that Kristina is divorcing Dmitry Nagiyev and can no longer pull strings at Claude Monet. Next time you watch the episode, listen for the Russian expressions for 'to want' and 'to call' — you will catch every word right away. See you next time!"
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('sasha', 'Кристина, привет, я хотела позвонить тебе сегодня.', 'Kristina, hi, I wanted to call you today.', [(96, 'Крис, привет. Я уже собралась тебе звонить.')], ''),
    ('kristina', 'Привет, Саша, что у тебя сейчас случилось?', 'Hi, Sasha, what happened with you right now?', [], ''),
    ('sasha', 'Представляешь, Виктория только что меня зло уволила!', 'Can you imagine, Victoria just angrily fired me!', [(97, 'Слушай, эта сучка меня уволила, представляешь?')], ''),
    ('kristina', 'Почему она вдруг решила уволить тебя сегодня?', 'Why did she suddenly decide to fire you today?', [], ''),
    ('sasha', 'Она очень злится из-за глупой ошибки вчера.', 'She is very angry because of a foolish mistake yesterday.', [], ''),
    ('sasha', 'Ты можешь поговорить со своим мужем Димой?', 'Can you talk with your husband Dima?', [(98, 'Ты это, не могла бы там, ну, как-то поговорить с Димой?')], ''),
    ('sasha', 'Пусть он поможет мне вернуться в ресторан.', 'Let him help me return to the restaurant.', [], ''),
    ('kristina', 'Саша, извини, но у меня не получится.', 'Sasha, sorry, however I will not be able to.', [(99, 'Сашуль, извини, не получится.')], ''),
    ('sasha', 'Но почему ты не можешь попросить Диму?', 'But why can you not ask Dima?', [], ''),
    ('kristina', 'Потому что мы с Димой скоро разводимся.', 'Because Dima and I are getting divorced soon.', [(100, 'Мы с Димой разводимся.')], ''),
    ('sasha', 'Какой ужас, я совсем не знала этого!', 'How terrible, I did not know that at all!', [], ''),
    ('kristina', 'Костя, налей мне быстро бокал хорошего вина!', 'Kostya, quickly pour me a glass of good wine!', [(101, 'Костя.'), (102, 'Налей мне быстро. Момент.')], ''),
    ('kostya', 'Один момент, сейчас я налью вам вино.', 'One moment, right now I will pour you wine.', [(102, 'Налей мне быстро. Момент.')], ''),
]
WALK = [
    (0, None, "'Kristina, hi, I wanted to call you today.' Sasha catches Kristina near the bar and says she was just about to call her."),
    (1, None, "'Hi, Sasha, what happened with you right now?' Kristina asks what happened to make Sasha look so upset."),
    (2, None, "'Can you imagine, Victoria just angrily fired me!' Sasha vents that Victoria just fired her in a fit of anger."),
    (3, None, "'Why did she suddenly decide to fire you today?' Kristina is surprised and asks why Vika suddenly decided to let her go."),
    (4, None, "'She is very angry because of a foolish mistake yesterday.' Sasha admits that Vika is furious over a foolish mistake from yesterday."),
    (5, None, "'Can you talk with your husband Dima?' She asks if Kristina can put in a word with her husband Dima."),
    (6, None, "'Let him help me return to the restaurant.' Sasha hopes Nagiyev can overrule Vika and bring her back to the restaurant."),
    (7, None, "'Sasha, sorry, however I will not be able to.' Kristina apologizes and says she will not be able to help."),
    (8, None, "'But why can you not ask Dima?' Sasha is confused about why Kristina cannot simply ask her own husband."),
    (9, None, "'Because Dima and I are getting divorced soon.' Kristina reveals the real reason: she and Dima are getting divorced soon."),
    (10, None, "'How terrible, I did not know that at all!' Sasha gasps, saying she had no idea their marriage was ending."),
    (11, None, "'Kostya, quickly pour me a glass of good wine!' Needing a drink after sharing the news, Kristina asks Kostya for a glass of good wine."),
    (12, None, "'One moment, right now I will pour you wine.' Kostya promises to pour her wine right away."),
]
