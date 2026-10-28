# Authoring module for kukhnya-s01e10-scene-43.
ID = 'kukhnya-s01e10-scene-43'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 43
TITLE = 'Икра и футбол  (Caviar and Football)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = "In the main restaurant room, a VIP guest lavishly praises the special caviar, believing Barinov's tale about private planes from Astrakhan. Meanwhile, Barinov anxiously tracks the football broadcast, his mood swinging wildly with every update from the pitch."
OPENER = "Let's listen to the VIP guest savoring the fraudulent caviar while Barinov agonizes over a live football match."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Between fraudulent caviar compliments and a painful match result, Barinov barely keeps his anger under control. Next time you watch the episode, listen for the Russian expressions for 'idler' and 'fast' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('guest', 'Шеф, налейте мне ещё немного вина.', 'Chef, pour me some more wine.', [(314, 'мне')], ''),
    ('guest', 'Какая невероятно вкусная у вас чёрная икра!', 'What an incredibly delicious black caviar you have!', [], ''),
    ('barinov', 'Конечно, это лучшая икра прямо из Астрахани.', 'Of course, this is the best caviar straight from Astrakhan.', [(312, 'Из Астрахани.')], ''),
    ('barinov', 'Мы возим её сюда специальными боингами.', 'We fly it here on special Boeings.', [(313, 'Возим. Боингами.')], ''),
    ('guest', 'Ну что, по вкусу всё просто отлично!', 'Well, in taste everything is simply excellent!', [(314, 'Ну что? Мне бы все хорошо.')], ''),
    ('barinov', 'В нашем ресторане иначе и быть не может.', 'In our restaurant it cannot be any other way.', [(315, 'Ну и иначе быть не может.')], ''),
    ('barinov', 'Официант, какой сейчас счёт в матче?', 'Waiter, what is the score in the match now?', [], ''),
    ('guest', 'Там сейчас счёт три-три, наши отыгрались!', 'The score there is three-three now, our guys tied it up!', [(316, 'Что? Три-три.'), (317, 'Наши молодцы отыгрались.')], ''),
    ('guest', 'Они двадцать лет подряд так не отыгрывались.', 'They had not tied it up like that for twenty years in a row.', [(318, '20 лет не отыгрывались.')], ''),
    ('guest', 'А сегодня вдруг забили три быстрых гола!', 'And today they suddenly scored three quick goals!', [(319, 'А сегодня отыгрались.')], ''),
    ('barinov', 'Неужели Спартак опять упустил победу в конце?!', 'Did Spartak really let victory slip away in the end again?!', [], ''),
    ('guest', 'Футбол сегодня получился очень нервный и странный.', 'Football today turned out very nervous and strange.', [], ''),
    ('barinov', 'Да уж, играют как настоящие бездельники!', 'Indeed, they play like real slackers!', [(321, 'Уроды.')], ''),
]
WALK = [
    (0, None, "'Chef, pour me some more wine.' The relaxed guest enjoys his lavish meal at the table."),
    (1, None, "'What an incredibly delicious black caviar you have!' To Viktor's relief, the VIP guest raves about how delicious the black caviar is."),
    (2, None, "'Of course, this is the best caviar straight from Astrakhan.' Playing along smoothly, Barinov boasts that the caviar came straight from Astrakhan."),
    (3, None, "'We fly it here on special Boeings.' The chef adds ridiculous claims about luxury transport."),
    (4, None, "'Well, in taste everything is simply excellent!' The guest remains totally unaware of the deception."),
    (5, None, "'In our restaurant it cannot be any other way.' When the guest praises the flavor, Viktor replies proudly that Claude Monet accepts nothing less."),
    (6, None, "'Waiter, what is the score in the match now?' Turning anxiously to a passing waiter, Viktor whispers to ask the current score of the football match."),
    (7, None, "'The score there is three-three now, our guys tied it up!' Watching the live broadcast on his phone, the guest excitedly announces that Spartak just tied the match three to three."),
    (8, None, "'They had not tied it up like that for twenty years in a row.' Amazed by the comeback, the guest marvels that the team has not pulled off a rally like that in twenty years."),
    (9, None, "'And today they suddenly scored three quick goals!' He adds in disbelief that the players suddenly scored three quick goals in a row today."),
    (10, None, "'Did Spartak really let victory slip away in the end again?!' Hearing that Spartak just scored three goals to tie the game at three-all — ruining his huge bet on CSKA — Viktor gasps in disbelief."),
    (11, None, "'Football today turned out very nervous and strange.' Shaking his head with a grin, the guest remarks that today's football match turned out wild and nerve-wracking."),
    (12, None, "'Indeed, they play like real slackers!' Barinov vents his deep sports frustration under his breath."),
]
