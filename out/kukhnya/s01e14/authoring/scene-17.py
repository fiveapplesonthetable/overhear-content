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
    (0, None, ["'What is this in my dessert?' Now let's consider the dialogue: ", ('guest', 'у'), ('guest', 'меня'), ' is how Russian says something is yours or happening to you.']),
    (1, None, ["'I almost broke a tooth because of you!' Now let's examine the words: ", ('guest', 'чуть'), " is 'nearly', literally 'a hair not'. ", ('guest', 'из'), '-', ('guest', 'за'), ('guest', 'вас'), " is 'because of you', and here it takes in the whole restaurant."]),
    (2, None, ["'Please forgive us.' We can focus on the dialogue: ", ('louis', 'Простите'), " gives the polite 'forgive', the one for strangers. Louis says 'us', ", ('louis', 'нас'), ', apologising for the kitchen.']),
    (3, None, ["'First, learn to speak Russian!' We can analyze this part: ", ('guest', 'научись'), " is the order form of 'learn', and using it with a stranger is the rude part. ", ('guest', 'по'), '-', ('guest', 'русски'), ' comes before the verbs.']),
    (4, None, ["'Why did you come here?' Now let's focus on the words: ", ('guest', 'приехал'), " is 'came', by car or train, not on foot. ", ('guest', 'сюда'), " is 'to here', the going partner of 'here'."]),
    (5, None, ["'So people would break their teeth?' After ", ('guest', 'Чтобы'), ", meaning 'so that', the verb goes into the past form: ", ('guest', 'ломали'), ", plural for people. That's a fixed rule, even about the future."]),
    (6, None, ["'I am the pastry chef, it is my fault.' Now let's analyze this part: ", ('louis', 'кондитер'), ' is a pastry chef. ', ('louis', 'вина'), " means blame, and it happens to look like the word for 'of wine', though that one has a different stress."]),
    (7, None, ["'Leave the pastry chef alone.' Let's examine the words: ", ('lyova', 'Оставьте'), " literally means 'leave', and the expression means 'leave in peace'. The pastry chef becomes ", ('lyova', 'кондитера'), " because he's the person being left alone."]),
    (8, None, ["'And who are you?' Now we can inspect the phrase: ", ('guest', 'ты'), ('guest', 'кто'), ('guest', 'такой'), " is pointed and a bit rude. People say it to ask what right someone has, and using the informal 'you' to a stranger makes it ruder still."]),
    (9, None, ["'I am the head chef of this restaurant.' Let us inspect the words: ", ('lyova', 'этого'), ('lyova', 'ресторана'), " is 'of this restaurant', where the endings of both words mark the 'of'."]),
    (10, None, ["'I am responsible for everything in the kitchen.' Lyova uses ", ('lyova', 'отвечаю'), " to mean he answers for it all. And it's ", ('lyova', 'на'), ('lyova', 'кухне'), ", 'on the kitchen', where English says 'in'."]),
    (11, None, ["'Do you have complaints against me?' We will examine the dialogue: ", ('lyova', 'У'), ('lyova', 'вас'), ('lyova', 'есть'), " is the way you say 'you have'. ", ('lyova', 'ко'), ('lyova', 'мне'), " has an extra 'o' to make it easier to say."]),
    (12, None, ["'Here is my complaint, take it.' We will analyze the sentence: ", ('guest', 'держи'), " literally says 'hold', and people say it when handing something over. It's an informal command, the same rudeness he showed Louis."]),
    (13, None, ["'Delicious dessert, thank you very much.' We will look at the sentence: ", ('louis', 'большое'), ('louis', 'спасибо'), " translates to 'big thanks', which is the equivalent of 'thank you very much'."]),
]
