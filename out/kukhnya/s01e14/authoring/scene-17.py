# Authoring module for kukhnya-s01e14-scene-17.
ID = 'kukhnya-s01e14-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 17
TITLE = 'Защитник Лёва  (Defender Lyova)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'louis': 'Луи', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = "A guest has bitten on something hard in his dessert, and he's furious. He turns on Louis until Lyova steps in. Here's the argument in Russian."
OPENER = 'Back through the argument, slowly.'
TRANSITION = 'Now the argument, all in one go.'
OUTRO = 'Lyova takes responsibility, and the guest hands over the evidence. Who has the loudest voice? Until next time.'
CLOSING = ('louis', 'Пока!')
STORY = [
    ('guest', 'Что это у меня в десерте?', 'What is this in my dessert?', [(253, 'Че за хрень у меня в десерте?')], ''),
    ('guest', 'Я из-за вас чуть зуб не сломал!', 'I almost broke a tooth because of you!', [(254, 'А? Из-за тебя?'), (255, 'Я еще зуба не лишился.')], ''),
    ('louis', 'Простите нас, пожалуйста.', 'Please forgive us.', [(256, 'Простите меня, пожалуйста.')], ''),
    ('guest', 'Ты сначала по-русски говорить научись!', 'First, learn to speak Russian!', [(256, 'Ты сначала научись по-русски разговаривать.')], ''),
    ('guest', 'Зачем ты сюда приехал?', 'Why did you come here?', [(257, 'Ты чего сюда приехал, а?')], ''),
    ('guest', 'Чтобы люди ломали зубы?', 'So people would break their teeth?', [(258, 'Чтобы народ зубы ломал?')], ''),
    ('louis', 'Я кондитер, это моя вина.', 'I am the pastry chef, it is my fault.', [], ''),
    ('lyova', 'Оставьте кондитера в покое.', 'Leave the pastry chef alone.', [(264, 'Оставьте в покое кондитера.')], ''),
    ('guest', 'А ты кто такой?', 'And who are you?', [(265, 'А ты кто такой?')], ''),
    ('lyova', 'Я шеф-повар этого ресторана.', 'I am the head chef of this restaurant.', [(265, 'Я шеф-повар.')], ''),
    ('lyova', 'Я отвечаю за всё на кухне.', 'I am responsible for everything in the kitchen.', [(266, 'И я несу ответственность за все, что происходит на кухне.')], ''),
    ('lyova', 'У вас есть претензии ко мне?', 'Do you have complaints against me?', [(267, 'И если у вас есть какие-то претензии...')], ''),
    ('guest', 'Вот моя претензия, держи.', 'Here is my complaint, take it.', [(269, 'Вот.')], ''),
    ('louis', 'Вкусный десерт, большое спасибо.', 'Delicious dessert, thank you very much.', [(272, 'Вкусный десерт с коньяком.')], ''),
]
WALK = [
    (0, None, "'What is this in my dessert?' Literally 'what is this at me in the dessert'. U menya, 'at me', is how Russian says something is yours or happening to you."),
    (1, None, "'I almost broke a tooth because of you!' 'Chut ne' is 'nearly', literally 'a hair not'. 'Iz-za vas' is 'because of you', and vas here takes in the whole restaurant."),
    (2, None, "'Please forgive us.' 'Prostite' is the polite 'forgive', the one for strangers; with friends it's prosti. Louis says 'us', nas, apologising for the kitchen."),
    (3, None, "'First, learn to speak Russian!' 'Nauchis' is the 'ty' order form of 'learn', and using ty with a stranger is the rude part. 'Po-russki', in Russian, comes before the verbs."),
    (4, None, "'Why did you come here?' 'Priekhal' is 'came', by car or train, not on foot, and the 'l' ending fits a man. 'Syuda' is 'to here', the going partner of zdes."),
    (5, None, "'So people would break their teeth?' After chtoby, 'so that', the verb goes into the past form: lomali, plural for lyudi, people. That's a fixed rule, even about the future."),
    (6, None, "'I am the pastry chef, it is my fault.' 'Konditer' is a pastry chef. 'Vina' means blame, and it happens to look like vina, 'of wine', though that one's stressed on the 'i'."),
    (7, None, "'Leave the pastry chef alone.' 'Ostavte v pokoe' is literally 'leave in peace'. 'Konditer' becomes konditera because he's the person being left."),
    (8, None, "'And who are you?' 'Kto takoy' is literally 'who such', and it's pointed. You say it when you want to know what right someone has."),
    (9, None, "'I am the head chef of this restaurant.' 'Etogo restorana' is 'of this restaurant': the 'ogo' and the 'a' both mark the 'of'."),
    (10, None, "'I am responsible for everything in the kitchen.' 'Otvechayu za vse' is literally 'I answer for everything'. And it's na kukhne, 'on the kitchen', where English says 'in'."),
    (11, None, "'Do you have complaints against me?' U vas est is 'at you there is', the Russian 'you have'. Ko mne is k mne with an extra 'o' to make it easier to say."),
    (12, None, "'Here is my complaint, take it.' 'Derzhi' is literally 'hold', and Russians say it when handing something over. It's the ty form, the same rudeness he showed Louis."),
    (13, None, "'Delicious dessert, thank you very much.' Russians say bolshoe spasibo, 'big thanks', where English says 'thank you very much'."),
]
