# Authoring module for kukhnya-s01e12-scene-07.
ID = 'kukhnya-s01e12-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 7
TITLE = "На кухне шефа  (In the Chef's Kitchen)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'It is a busy afternoon of prep in the kitchen, and Chef Barinov is on the warpath. He catches Senya, who cooks the meat, standing around. Russian first.'
OPENER = 'One barked order at a time.'
TRANSITION = 'Right, the kitchen at full speed again.'
OUTRO = "Senya promises to clean up and Barinov promises to check every plate. If you ever need to say 'a bit quieter, please' in Russian, you now have the words. Talk soon."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Сеня, почему ты стоишь без дела?', 'Senya, why are you standing doing nothing?', [], ''),
    ('senya', 'Я жду нужные специи для мяса.', 'I am waiting for the needed spices for the meat.', [], ''),
    ('barinov', 'Ты ждёшь, пока гном насыпет корицу?', 'Are you waiting until a gnome sprinkles cinnamon?', [(64, 'насыпет корицу')], ''),
    ('senya', 'Шеф, я всё делаю быстро.', 'Chef, I do everything quickly.', [(65, 'Ну, шеф')], ''),
    ('barinov', 'Тогда работай быстрее и не стой.', 'Then work faster and do not stand around.', [(66, 'Сам ты')], ''),
    ('barinov', 'И всегда убирай за собой стол.', 'And always clean up your table.', [(67, 'убирай за собой')], ''),
    ('senya', 'Шеф, говорите немного тише, пожалуйста.', 'Chef, please speak a bit quieter.', [(68, 'потише бы')], ''),
    ('barinov', 'Не надо учить меня дисциплине!', 'Do not teach me discipline!', [(69, 'Учи меня еще')], ''),
    ('senya', 'Мы просто очень стараемся для вас.', 'We are simply trying very hard for you.', [], ''),
    ('barinov', 'На моей кухне должен быть идеальный порядок.', 'There must be perfect order in my kitchen.', [], ''),
    ('senya', 'Мы сейчас же всё уберём, шеф.', 'We will clean everything up right now, chef.', [], ''),
    ('barinov', 'Спокойнее, я проверю каждое блюдо лично.', 'Calm down, I will check every dish personally.', [(71, 'Покойнее')], ''),
]
WALK = [
    (0, None, ["'Senya, why are you standing doing nothing?' To say 'idle', Russian says ", ('barinov', 'без'), ('barinov', 'дела'), ", which means 'without business'. Barinov uses an informal 'you' with his cook, seen in the verb ", ('barinov', 'стоишь'), '.']),
    (1, None, ["'I am waiting for the needed spices for the meat.' Russian says ", ('senya', 'жду'), ('senya', 'нужные'), ('senya', 'специи'), " without 'for' after 'wait'. The term for meat, ", ('senya', 'мяса'), ", takes a different ending after 'for'."]),
    (2, None, ["'Are you waiting until a gnome sprinkles cinnamon?' We will analyze the dialogue: ", ('barinov', 'Ты'), ('barinov', 'ждёшь'), " matches Senya's 'I wait'. The word ", ('barinov', 'пока'), " means 'until' here, and the gnome is Barinov's sarcastic picture of how slow Senya is."]),
    (3, None, ["'Chef, I do everything quickly.' We will focus on the dialogue: ", ('senya', 'всё'), " means 'everything' and is a very common small word. ", ('senya', 'быстро'), " means 'quickly'."]),
    (4, None, ["'Then work faster and do not stand around.' Change the ending of 'quickly' and it becomes ", ('barinov', 'быстрее'), ", meaning 'faster'. ", ('barinov', 'работай'), " is the command 'work!' and ", ('barinov', 'не'), ('barinov', 'стой'), " is 'do not stand'."]),
    (5, None, ["'And always clean up your table.' Let's look at the words: ", ('barinov', 'всегда'), " means 'always'. ", ('barinov', 'за'), ('barinov', 'собой'), " expresses cleaning up 'after yourself', phrased as 'behind yourself'."]),
    (6, None, ["'Chef, please speak a bit quieter.' Senya uses the polite 'you' form in ", ('senya', 'говорите'), ' because he is talking to the chef. ', ('senya', 'тише'), " is 'quieter'."]),
    (7, None, ["'Do not teach me discipline!' Let's focus on this line: ", ('barinov', 'Не'), ('barinov', 'надо'), " is 'no need', used as a strong 'do not'. The action ", ('barinov', 'учить'), ' takes the person as ', ('barinov', 'меня'), ", meaning 'me'."]),
    (8, None, ["'We are simply trying very hard for you.' The verb ", ('senya', 'стараемся'), ' ends with a part that shows the action reflects back on themselves. ', ('senya', 'для'), ('senya', 'вас'), " means 'for you' in the polite form."]),
    (9, None, ["'There must be perfect order in my kitchen.' The term ", ('barinov', 'должен'), ' takes this form because the thing that must be, the order, is masculine. Notice also ', ('barinov', 'На'), ('barinov', 'моей'), ('barinov', 'кухне'), ": Russians say 'on my kitchen' where English says 'in'."]),
    (10, None, ["'We will clean everything up right now, chef.' Let us analyze the dialogue: ", ('senya', 'сейчас'), ('senya', 'же'), " means 'this very second'. ", ('senya', 'уберём'), " means 'we will clear', related to the term Barinov used for 'clean up'."]),
    (11, None, ["'Calm down, I will check every dish personally.' We can look at the speech: ", ('barinov', 'Спокойнее'), " is 'calmer', using the same ending as 'faster'. ", ('barinov', 'блюдо'), ' is a dish, like a plate of food, and ', ('barinov', 'лично'), " means 'in person'."]),
]
