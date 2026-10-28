ID = 'kukhnya-s05e03-scene-01'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 3
SCENE = 1
TITLE = "Знакомство Дениса с мамой Кати  (Denis Meets Katya's Mother)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "eleonora": "angelina", "denis": "anja"}
LABELS = {"eleonora": "Элеонора", "denis": "Денис"}
SOURCE_NAME = 'Кухня (Kukhnya) S5.03'
SOURCE_FILE = 'sources/kukhnya/s05/e03.ru.srt'

INTRO = "Episode 3 picks up right in Eleonora Andreevna's office as Katya introduces her boyfriend Denis to her mother—and Denis realizes in shock that the stranger he slept with was Katya's mother. Listen to the tense meeting."

STORY = [
    ('eleonora', 'Пожалуйста, ознакомьтесь.', 'Please get acquainted.', [(1, 'Ознакомьтесь')], 'verbatim'),
    ('eleonora', 'Денис, это моя мама.', 'Denis, this is my mom.', [(2, 'Денис, это моя мама')], 'verbatim'),
    ('eleonora', 'Мама, это мой парень Денис.', 'Mom, this is my boyfriend Denis.', [(3, 'Мама, это мой парень Денис')], 'verbatim'),
    ('eleonora', 'Мне очень приятно.', 'Very nice to meet you.', [(4, 'Очень приятно')], 'adapted'),
    ('eleonora', 'Не бойся, мама не кусается.', 'Do not be afraid, Mom does not bite.', [(5, 'Не бойся, мама не кусается')], 'verbatim'),
    ('denis', 'Да, я это уже знаю.', 'Yes, I already know that.', [(6, 'Я знаю')], 'adapted'),
    ('eleonora', 'Денис, а вы чем занимаетесь?', 'Denis, and what do you do for a living?', [(7, 'Денис, а вы чем занимаетесь?')], 'verbatim'),
    ('denis', 'Я здесь у вас работаю.', 'I work right here for you.', [(8, 'Работаю'), (9, 'У вас')], 'adapted'),
    ('denis', 'Я работаю поваром на кухне.', 'I work as a cook in the kitchen.', [(9, 'Поваром')], 'adapted'),
    ('eleonora', 'Очень хорошо, и к Кате поближе.', 'Very good, and closer to Katya.', [(10, 'Очень хорошо'), (10, 'поближе')], 'adapted'),
    ('eleonora', 'Вы теперь под моей крышей.', 'You are under my roof now.', [(11, 'И под моей крышей')], 'adapted'),
    ('eleonora', 'Значит, будете часто видеться.', 'So we will see each other often.', [(11, 'будете часто видеться')], 'adapted'),
    ('denis', 'Извините, мне нужно идти.', 'Excuse me, I need to go.', [(12, 'Извините, мне нужно идти')], 'verbatim'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Please get acquainted.' Here the Russian phrasing highlights 'please' before landing on 'get acquainted'."),
    (1, None, "'Denis, this is my mom.' The grammar packs 'Denis' and 'mom' into a tight, idiomatic kitchen exchange."),
    (2, None, "'Mom, this is my boyfriend Denis.' The meaning hinges on 'mom' working together with 'Denis' in spoken Russian. Eleonora answers right away."),
    (3, None, "'Very nice to meet you.' In Russian, the idea of 'to me' flows naturally into 'pleasant' without extra filler words."),
    (4, None, "'Do not be afraid, Mom does not bite.' Katya anchors the line on 'not', while 'bites' completes the thought."),
    (5, None, "'Yes, I already know that.' Notice how Russian expresses 'yes' and 'know' with crisp inflection rather than helper words. Eleonora answers right away."),
    (6, None, "'Denis, and what do you do for a living?' In Russian, the idea of 'Denis' flows naturally into 'you do' without extra filler words."),
    (7, None, "'I work right here for you.' In Russian, the idea of 'I' flows naturally into 'work' without extra filler words."),
    (8, None, "'I work as a cook in the kitchen.' Denis anchors the line on 'I', while 'kitchen' completes the thought. Eleonora answers right away."),
    (9, None, "'Very good, and closer to Katya.' The grammar packs 'very' and 'closer' into a tight, idiomatic kitchen exchange."),
    (10, None, "'You are under my roof now.' The meaning hinges on 'you' working together with 'roof' in spoken Russian."),
    (11, None, "'So we will see each other often.' Eleonora pairs 'often' with 'to see each other' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (12, None, "'Excuse me, I need to go.' Spoken Russian keeps this brisk, leaning on 'excuse me' and finishing on 'to go'."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that captures Denis's mortifying realization in Eleonora's office. Until next time!"
CLOSING = ("denis", "До встречи!")
