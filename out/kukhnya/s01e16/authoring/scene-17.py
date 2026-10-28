# Authoring module for kukhnya-s01e16-scene-17.
ID = 'kukhnya-s01e16-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 17
TITLE = 'Яблочный штрудель  (Apple Strudel)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ainura': 'Айнура', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "To hide cleaner Aynura from the migration inspection, the staff dress her up as a wealthy guest in the dining room. However, the sharp-eyed inspector sits right at her table, orders apple strudel, and reveals that he knows every trick restaurants use to hide workers. Let's listen to their tense conversation in Russian."
OPENER = "Let's see how the migration inspector toys with Aynura before pardoning her over dessert."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Now you know how to order food at a table, talk about years of work experience, and express gratitude in Russian. See who the inspector catches next in the following scene. Next time you watch the episode, listen for the Russian expressions for 'kind' and 'evening' — you will catch every word right away. See you next time!"
CLOSING = ('inspector', 'Пока!')
STORY = [
    ('inspector', 'Добрый вечер, можно сесть за столик?', 'Good evening, may I sit at the table?', [(224, 'Добрый вечер')], ''),
    ('ainura', 'Да, пожалуйста, садитесь сюда.', 'Yes, please, sit down here.', [], ''),
    ('inspector', 'Вы уже готовы сделать заказ?', 'Are you ready to place an order already?', [(225, 'Готовы сделать заказ?')], ''),
    ('ainura', 'Я хочу заказать этот дорогой коньяк.', 'I want to order this expensive cognac.', [(229, 'Этот коньяк очень дорогой')], ''),
    ('inspector', 'А я закажу вкусный яблочный штрудель.', 'And I will order the delicious apple strudel.', [(234, 'яблочный штрудель')], ''),
    ('inspector', 'Я всегда везде нахожу нелегальных работников.', 'I always find illegal workers everywhere.', [(239, 'я их всегда везде нахожу')], ''),
    ('ainura', 'Вам очень нравится ваша работа?', 'Do you like your job very much?', [], ''),
    ('inspector', 'Да, я занимаюсь этим пять лет.', 'Yes, I have been doing this for five years.', [(248, 'этим я уже занимаюсь пять лет')], ''),
    ('inspector', 'Обычно работников прячут на складе.', 'Usually they hide workers in the storeroom.', [(250, 'прячут их в туалете, на складе')], ''),
    ('inspector', 'А умные люди сажают их в зале.', 'And smart people seat them in the dining room.', [(251, 'А те, кто поумнее')], ''),
    ('inspector', 'Но этот яблочный штрудель просто прекрасный!', 'But this apple strudel is simply wonderful!', [(255, 'самый прекрасный яблочный штрудель')], ''),
    ('inspector', 'Сегодня вкусный десерт спас вас.', 'Today the delicious dessert saved you.', [(257, 'сегодня кое-кого спас')], ''),
    ('ainura', 'Хорошо, спасибо вам большое!', 'All right, thank you very much!', [(259, 'Хорошо. Спасибо')], ''),
]
WALK = [
    (0, None, "'Are you ready to place an order already?' inspector drops a standard dining room question to find out if the supposed customer is prepared to eat."),
    (1, None, "'And I will order the delicious apple strudel.' Pointing out his choice, the official decides on a sweet dessert for himself."),
    (2, None, "'Yes, I have been doing this for five years.' A casual remark follows, confirming his long experience dealing with these exact situations."),
    (3, None, "'Today the delicious dessert saved you.' Playfully admitting that the high quality of the food earned them a temporary pardon, the officer finishes his thought."),
]
