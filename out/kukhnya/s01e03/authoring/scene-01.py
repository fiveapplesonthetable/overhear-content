# Authoring module for kukhnya-s01e03-scene-01.
ID = 'kukhnya-s01e03-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = 'Живой гусь  (The Live Goose)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "This is The Kitchen, the Russian comedy about a hot-tempered chef and the staff of a smart Moscow restaurant called Claude Monet. In this third episode, Max, the young cook, has spent a week unloading deliveries and is longing to be allowed near a stove. Instead, Chef Barinov hands him something very different: a live goose. Here is their conversation in Russian first, so don't worry about catching every word."
OPENER = "Let's go back and watch Max's face."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "So Max has been given a goose and an ultimatum. If the word for alive sticks in your head after this, good: you'll meet it again."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Доброе утро, шеф!', 'Good morning, chef!', [(46, 'Доброе утро, шеф')], ''),
    ('barinov', 'Здравствуй, огузок. Вот твоя работа.', 'Hello, oguzok. Here is your work.', [(48, 'Иди разгружай продукты')], ''),
    ('max', 'Шеф, это живой гусь!', 'Chef, this is a live goose!', [(36, 'Это чего? Гусь'), (40, 'живой гусь')], ''),
    ('barinov', 'У нас сегодня очень важный банкет.', 'We have a very important banquet today.', [(38, 'у нас же сегодня банкет')], ''),
    ('max', 'Зачем нам живой гусь на кухне?', 'Why do we need a live goose in the kitchen?', [(40, 'На хрена мне на кухне живой гусь')], ''),
    ('barinov', 'Гостям нужен самый свежий продукт!', 'The guests need the freshest product!', [(41, 'вы просили самого свежего')], ''),
    ('max', 'Но я повар, а не мясник.', 'But I am a cook, not a butcher.', [(49, 'ну я же не грузчик, я повар')], ''),
    ('barinov', 'Каждый повар обязан уметь разделывать мясо.', 'Every chef is obliged to know how to butcher meat.', [(59, 'Каждый повар должен быть готов')], ''),
    ('max', 'Что, мне нужно убить его?', 'What, do I need to kill it?', [(56, 'Что, прям насмерть')], ''),
    ('barinov', 'А ты думал, мясо растёт на деревьях?', 'Did you think meat grows on trees?', [(58, 'ты думаешь, что мясо кусочком на деревьях растет')], ''),
    ('max', 'Я никогда в жизни этого не делал.', 'I have never done this in my life.', [], ''),
    ('barinov', 'Убей гуся, или ты уволен!', 'Kill the goose, or you are fired!', [(53, 'Убей гуся'), (60, 'Убей, гуся')], ''),
    ('max', 'Хорошо, я попробую сделать это.', 'Fine, I will try to do it.', [], ''),
]
WALK = [
    (0, None, [
        "'Good morning, chef!' Here we see ",
        ('max', 'Доброе утро,'),
        " translates to 'good morning', and it puts a special ending on 'good' because the word for morning, ",
        ('max', 'утро,'),
        " uses a middle shape."
    ]),
    (1, None, [
        "'Hello, oguzok. Here is your work.' Looking closely, ",
        ('barinov', 'Здравствуй,'),
        " translates to the hello for one person you know well. Add an extra sound at the end and you get the polite version. ",
        ('barinov', 'огузок.'),
        " is the word for the rump cut in a cow, and ",
        ('barinov', 'Вот твоя работа.'),
        " literally means 'here your work'."
    ]),
    (2, None, [
        "'Chef, this is a live goose!' Looking closely, ",
        ('max', 'это живой гусь!'),
        " literally says 'this live goose', with no action word for 'is'. ",
        ('max', 'живой'),
        " translates to 'alive', and ",
        ('max', 'гусь!'),
        " is the word for a goose."
    ]),
    (3, None, [
        "'We have a very important banquet today.' Pay attention to ",
        ('barinov', 'У нас'),
        " literally means 'at us', which is how they say 'we have'. ",
        ('barinov', 'важный'),
        " translates to 'important', and ",
        ('barinov', 'банкет.'),
        " is the word for the banquet."
    ]),
    (4, None, [
        "'Why do we need a live goose in the kitchen?' Focusing here, ",
        ('max', 'Зачем нам'),
        " translates to 'what for, to us', and that second word carries the feeling of 'we need'. Note ",
        ('max', 'на кухне?'),
        " — they literally say they are 'on' the kitchen, not 'in' it."
    ]),
    (5, None, [
        "'The guests need the freshest product!' The word for the guests, ",
        ('barinov', 'Гостям'),
        ", gets a 'to' ending, because the thing needed is the main focus. So the needed word matches with ",
        ('barinov', 'продукт!'),
        ", which has a guy shape, and ",
        ('barinov', 'самый свежий'),
        " is built from 'most fresh'."
    ]),
    (6, None, [
        "'But I am a cook, not a butcher.' In ",
        ('max', 'я повар, а не мясник.'),
        ", the little phrase ",
        ('max', 'а не'),
        " translates to 'and not', setting one job against the other. The word for butcher, ",
        ('max', 'мясник.'),
        ", is built from the word for meat."
    ]),
    (7, None, [
        "'Every chef is obliged to know how to butcher meat.' Looking closely, ",
        ('barinov', 'обязан'),
        " translates to 'obliged', and has a man's ending. ",
        ('barinov', 'уметь'),
        " is the word for 'know how' when talking about skills, and ",
        ('barinov', 'разделывать'),
        " means to cut an animal into pieces."
    ]),
    (8, None, [
        "'What, do I need to kill it?' Observe how ",
        ('max', 'мне нужно'),
        " literally says 'to me necessary', which is the standard way to say 'I need to'. ",
        ('max', 'убить'),
        " is the word for 'to kill', and ",
        ('max', 'его?'),
        ", meaning 'him', refers to the goose."
    ]),
    (9, None, [
        "'Did you think meat grows on trees?' Listen carefully, ",
        ('barinov', 'думал,'),
        " ends in a specific sound because Barinov is talking to a man. The word for tree changes into a strange shape for more than one, making 'on trees' look like ",
        ('barinov', 'на деревьях?'),
        "."
    ]),
    (10, None, [
        "'I have never done this in my life.' In Russian, ",
        ('max', 'никогда'),
        " and ",
        ('max', 'не делал.'),
        " literally pair up to say 'never not did', which is their way of saying 'not' twice. The word for 'this', ",
        ('max', 'этого'),
        ", takes an 'of' shape because of the negative, and ",
        ('max', 'в жизни'),
        " translates to 'in life'."
    ]),
    (11, None, [
        "'Kill the goose, or you are fired!' Let us review ",
        ('barinov', 'Убей'),
        " translates to the action word 'kill!'. The word for the goose becomes ",
        ('barinov', 'гуся,'),
        " because it is the living creature receiving the action. ",
        ('barinov', 'ты уволен!'),
        " literally means 'you are fired'."
    ]),
    (12, None, [
        "'Fine, I will try to do it.' Focusing here, ",
        ('max', 'попробую'),
        " translates to 'I will try', which is the finished-action partner shape of the base action word. ",
        ('max', 'сделать это.'),
        " is built from the words for 'to do it'."
    ]),
]
