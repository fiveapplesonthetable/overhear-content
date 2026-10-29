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
    (0, None, "'Senya, why are you standing doing nothing?' To say 'idle', Russian says 'bez dela', 'without business', from 'delo', a job or matter. Barinov uses 'ty' with his cook, and 'stoish' is the ty form of 'stoyat', 'to stand'."),
    (1, None, "'I am waiting for the needed spices for the meat.' Russian says 'I wait the spices', with no word for 'for' after 'wait'. 'Myasa' is 'of meat', and it picks up an 'a' after 'for'."),
    (2, None, "'Are you waiting until a gnome sprinkles cinnamon?' 'Zhdyosh' is 'you wait', the same word as Senya's 'I wait'. 'Poka' here means 'until', and the gnome is Barinov's sarcastic picture of how slow Senya is."),
    (3, None, "'Chef, I do everything quickly.' 'Vsyo' means 'everything', and it's one of the most common little words in Russian. 'Bystro' is 'quickly', and you'll hear it again in a moment."),
    (4, None, "'Then work faster and do not stand around.' Swap the 'o' of bystro for 'ee' and 'quickly' becomes bystree, 'faster'. 'Rabotay' is the order 'work!' and 'ne stoy' is 'don't stand', the same 'stoy' as above."),
    (5, None, "'And always clean up your table.' 'Vsegda' means 'always'. 'Za soboy' is literally 'behind yourself', which is how Russians say 'after yourself'."),
    (6, None, "'Chef, please speak a bit quieter.' Senya uses the polite 'you' form of 'speak', because the person is the chef. 'Tishe' is 'quieter', the 'sh-e' ending made from 'tikho', 'quiet'."),
    (7, None, "'Do not teach me discipline!' 'Ne nado' is 'no need', and it's used as a strong 'don't'. 'Uchit' takes the person as menya, 'me', and the subject with an 'e' ending, distsipline, literally 'teach me to discipline'."),
    (8, None, "'We are simply trying very hard for you.' 'Starayemsya' ends in 'sya', so it's literally 'we try ourselves'. 'Dlya vas' is 'for you', in the polite form."),
    (9, None, "'There must be perfect order in my kitchen.' Barinov's 'dolzhen' has no vowel after the 'n' because the thing that must be, 'order', is masculine. Also note 'on my kitchen': Russians stand 'on' a kitchen where English stands 'in' it."),
    (10, None, "'We will clean everything up right now, chef.' 'Seychas zhe' is 'this very second', where the little 'zhe' pushes the 'now'. 'Uberyom' is 'we will clear', from the same word as Barinov's 'clean up!'."),
    (11, None, "'Calm down, I will check every dish personally.' 'Spokoynee' is 'calmer', made with the same 'ee' ending as 'faster'. 'Blyudo' is a dish, in the sense of a plate of food, and 'lichno' is 'in person'."),
]
