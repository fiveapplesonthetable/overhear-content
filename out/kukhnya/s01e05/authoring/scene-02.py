# Authoring module for kukhnya-s01e05-scene-02.
ID = 'kukhnya-s01e05-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 2
TITLE = 'Мечты о будущем  (Dreams of the Future)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Meanwhile, in the staff locker room at Claude Monet, the waitress Nastya is floating. She thinks yesterday's kiss with Max was the start of a love story, which is not what Max just told Kostya. Her friend Sasha, another waitress, is trying to keep up. Here it is in Russian."
OPENER = 'Now slowly. Nastya races ahead, and Sasha keeps asking questions to pull her back.'
TRANSITION = 'And now the chat in one piece.'
OUTRO = 'Sasha\'s little questions are worth stealing. They keep any conversation going. Max, of course, has no idea about the children.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('sasha', 'Настя, у вас с Максом всё серьёзно?', 'Nastya, is everything serious between you and Max?', [], ""),
    ('nastya', 'Да, мы вчера даже поцеловались.', 'Yes, yesterday we even kissed.', [], ""),
    ('sasha', 'Правда? И как это произошло?', 'Really? And how did that happen?', [], ""),
    ('nastya', 'Это было невероятно романтично!', 'It was incredibly romantic!', [], ""),
    ('sasha', 'Неужели ты влюбилась в него?', 'Did you really fall in love with him?', [], ""),
    ('nastya', 'Он такой добрый и внимательный парень.', 'He is such a kind and attentive guy.', [], ""),
    ('sasha', 'Вы ведь знакомы всего одну неделю.', 'After all, you have only known each other one week.', [], ""),
    ('nastya', 'Настоящая любовь не знает времени.', 'True love knows no time.', [], ""),
    ('nastya', 'Представляешь, какие у нас будут красивые дети!', 'Imagine what beautiful children we will have!', [(22, 'Представляешь, какие у нас дети красивые будут')], ""),
    ('sasha', 'Ты уже думаешь о детях?!', 'Are you already thinking about children?!', [], ""),
    ('nastya', 'Конечно, мы создадим прекрасную семью.', 'Of course, we will create a wonderful family.', [], ""),
    ('sasha', 'А Макс знает о твоих планах?', 'And does Max know about your plans?', [], ""),
    ('nastya', 'Скоро мы обязательно всё обсудим.', 'Soon we will definitely discuss everything.', [], ""),
]
WALK = [
    (0, None, [
        "'Nastya, is everything serious between you and Max?' Russian says 'at you with Max everything serious', with no 'is' at all. ",
        ('sasha', 'у'), ('sasha', 'вас'),
        " is plural here, because Sasha literally translates to the two of them."
    ]),
    (1, None, [
        "'Yes, yesterday we even kissed.' The same kissing verb, but now we see ",
        ('nastya', 'поцеловались.'),
        " That makes it one kiss, done and finished, where the imperfective verb sounded more like an ongoing activity."
    ]),
    (2, None, [
        "'Really? And how did that happen?' literally translates to 'truth', and said ",
        ('sasha', 'Правда?'),
        " with a rising voice it expresses 'really?'. The verb ",
        ('sasha', 'произошло?'),
        " ends in an O to agree with ",
        ('sasha', 'это'),
        ", 'it'."
    ]),
    (3, None, [
        "'It was incredibly romantic!' expresses 'not' in front of 'probably', ",
        ('nastya', 'невероятно'),
        " so it expresses 'improbably' or 'unbelievably'. As for ",
        ('nastya', 'романтично!'),
        ", you can probably guess what that means."
    ]),
    (4, None, [
        "'Did you really fall in love with him?' is a surprised 'can it really ",
        ('sasha', 'Неужели'),
        " be?'. In Russian you fall in love 'into' someone: ",
        ('sasha', 'влюбилась'), ('sasha', 'в'), ('sasha', 'него?'),
        " The ending on the verb tells you it's a woman who fell."
    ]),
    (5, None, [
        "'He is such a kind and attentive guy.' before a description signifies 'such a'. ",
        ('nastya', 'такой'),
        ' Both ',
        ('nastya', 'добрый'),
        " and ",
        ('nastya', 'внимательный'),
        " share the same ending, which is standard when the adjective describes a man, here ",
        ('nastya', 'парень.')
    ]),
    (6, None, [
        "'After all, you have only known each other one week.' , tucked in the middle, expresses ",
        ('sasha', 'ведь'),
        " 'after all', a gentle 'come on'. The word for 'week' becomes ",
        ('sasha', 'одну'), ('sasha', 'неделю.'),
        " when it says how long."
    ]),
    (7, None, [
        "'True love knows no time.' It sounds like a song lyric, and Nastya expresses it. After ",
        ('nastya', 'не'), ('nastya', 'знает'),
        " (which expresses 'doesn't know'), the word for 'time' shifts to ",
        ('nastya', 'времени.')
    ]),
    (8, None, [
        "'Imagine what beautiful children we will have!' literally literally translates to 'do you ",
        ('nastya', 'Представляешь,'),
        " imagine?', used like 'just imagine!'. 'We will have' is expressed by ",
        ('nastya', 'у'), ('nastya', 'нас'), ('nastya', 'будут'),
        ", which equates to 'at us will be'."
    ]),
    (9, None, [
        "'Are you already thinking about children?!' The word ",
        ('sasha', 'уже'),
        " ('already') carries all of Sasha's shock. After ",
        ('sasha', 'о'),
        " ('about'), the term for 'children' turns into ",
        ('sasha', 'детях?!')
    ]),
    (10, None, [
        "'Of course, we will create a wonderful family.' is spelled with a 'ch' sound ",
        ('nastya', 'Конечно,'),
        " in Cyrillic but spoken differently. The word for 'family' becomes ",
        ('nastya', 'семью.'),
        " because it's the thing they will create."
    ]),
    (11, None, [
        "'And does Max know about your plans?' The one question Nastya has dodged. Following ",
        ('sasha', 'о'),
        " ('about'), both words take plural endings: ",
        ('sasha', 'твоих'), ('sasha', 'планах?')
    ]),
    (12, None, [
        "'Soon we will definitely discuss everything.' literally translates to 'we will discuss', ",
        ('nastya', 'обсудим.'),
        " with the same ending as the verb she used for 'we will create' in her last line. The word ",
        ('nastya', 'обязательно'),
        " literally translates to 'definitely', and is something Russian speakers say all the time to promise something."
    ]),
]
