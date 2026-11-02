# Authoring module for kukhnya-s01e12-scene-06.
ID = 'kukhnya-s01e12-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 6
TITLE = 'Визит к конкурентам  (A Visit to Competitors)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'Barinov is curious, and a bit nervous, so he walks next door to look at the new Italian restaurant. There he finds Elena, its head chef, and a delivery of palm trees. The duel comes first, in Russian.'
OPENER = 'Slowly now, to see who really wins.'
TRANSITION = "Now it's the whole duel again, start to finish."
OUTRO = 'Barinov leaves with a grumble about letting people finish. Notice how politely the two of them manage to insult each other.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('elena', 'Осторожно заносите эти пальмы в ресторан!', 'Carefully bring these palms into the restaurant!', [(59, 'И ты заноси.')], ''),
    ('elena', 'Ой, Виктор Петрович, захотели вкусно поесть?', 'Oh, Viktor Petrovich, did you want to eat well?', [(59, 'Ой, Виктор Петрович, захотели вкусно поесть.')], ''),
    ('elena', 'Мы откроемся только через шесть дней!', 'We open only in six days!', [(60, 'Извините, откроемся только через шесть дней.')], ''),
    ('barinov', 'Я просто гулял по этой улице.', 'I was simply taking a walk along this street.', [], ''),
    ('elena', 'Решили лично проверить своих главных конкурентов?', 'Decided to personally check your main competitors?', [], ''),
    ('barinov', 'Я совсем не боюсь вашего ресторана.', 'I am not at all afraid of your restaurant.', [], ''),
    ('elena', 'Тогда почему вы смотрите на нас?', 'Then why are you looking at us?', [], ''),
    ('barinov', 'Зачем вам в зале настоящие пальмы?', 'Why do you need real palm trees in the dining room?', [(61, 'Просто подумал, что если у вас пальмы')], ''),
    ('elena', 'Это создаёт уютную итальянскую атмосферу.', 'This creates a cozy Italian atmosphere.', [], ''),
    ('barinov', 'Пальмы не помогут готовить вкусную еду!', 'Palm trees will not help cook tasty food!', [], ''),
    ('elena', 'У нас будет самая вкусная кухня!', 'We will have the tastiest cuisine!', [], ''),
    ('elena', 'Пропустите рабочих, заносите деревья внутрь!', 'Let the workers through, bring the trees inside!', [(62, 'Заносим, заносим.')], ''),
    ('barinov', 'Дослушивать надо людей, когда они говорят!', 'One must listen to people when they speak!', [(63, 'Дослушивать надо.')], ''),
]
WALK = [
    (0, None, ["'Carefully bring these palms into the restaurant!' You might recognize ", ('elena', 'Осторожно'), ' from warning signs. The order is meant for several workers.']),
    (1, None, ["'Oh, Viktor Petrovich, did you want to eat well?' Using the first name and father's name is a respectful way to address someone. ", ('elena', 'захотели'), " uses the group past form to show a polite 'you'."]),
    (2, None, ["'We open only in six days!' Russians say ", ('elena', 'через'), ('elena', 'шесть'), ('elena', 'дней'), " to mean 'in six days', and the word for 'days' takes a special form after the number."]),
    (3, None, ["'I was simply taking a walk along this street.' The verb ", ('barinov', 'гулял'), ' shows the speaker is a man, and ', ('barinov', 'по'), ('barinov', 'этой'), ('barinov', 'улице'), ' describes walking along the street.']),
    (4, None, ["'Decided to personally check your main competitors?' We can focus on this part: ", ('elena', 'Решили'), " uses the group past form for a polite 'you', while ", ('elena', 'лично'), " means 'in person'."]),
    (5, None, ["'I am not at all afraid of your restaurant.' Let's analyze this line: ", ('barinov', 'совсем'), ('barinov', 'не'), " means 'not at all'. The thing you are afraid of changes its ending, making it ", ('barinov', 'ресторана'), '.']),
    (6, None, ["'Then why are you looking at us?' Now let's inspect the words: ", ('elena', 'Тогда'), ' picks up from what he just said. The verb ', ('elena', 'смотрите'), " is another polite 'you' form."]),
    (7, None, ["'Why do you need real palm trees in the dining room?' There is no verb here: ", ('barinov', 'Зачем'), ('barinov', 'вам'), " is how you ask why someone needs something, using a polite 'you'."]),
    (8, None, ["'This creates a cozy Italian atmosphere.' Both describing words change their endings to match the feminine word for atmosphere, giving us ", ('elena', 'уютную'), ('elena', 'итальянскую'), '.']),
    (9, None, ["'Palm trees will not help cook tasty food!' Let's look at this line: ", ('barinov', 'не'), ('barinov', 'помогут'), " goes with 'palms', while ", ('barinov', 'готовить'), " covers both 'cook' and 'prepare'."]),
    (10, None, ["'We will have the tastiest cuisine!' Russians say ", ('elena', 'У'), ('elena', 'нас'), ('elena', 'будет'), " to mean 'we will have'. ", ('elena', 'самая'), " adds 'the most' before 'tasty', and ", ('elena', 'кухня'), ' means both kitchen and cuisine.']),
    (11, None, ["'Let the workers through, bring the trees inside!' We will break down this line: ", ('elena', 'рабочих'), ' is a describing word used as a name for people. The word for trees, ', ('elena', 'деревья'), ', has an irregular plural form.']),
    (12, None, ["'One must listen to people when they speak!' Let us break down the speech: ", ('barinov', 'Дослушивать'), ' means to listen all the way to the end. Notice for people takes a different form as the object: ', ('barinov', 'людей'), '.']),
]
