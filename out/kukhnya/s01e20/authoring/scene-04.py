# Authoring module for kukhnya-s01e20-scene-04.
ID = 'kukhnya-s01e20-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 4
TITLE = 'Дорогой подарок  (Expensive Gift)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = "Max has rung Vika to ask about the ring she sent him. She says it was for a friend, and Max starts to realise he's misread the whole thing. We'll hear it in Russian first."
OPENER = "Let's go through it a line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Vika wants Max to give her the ring after all, and Max has to find a year's wages. The phrase 'dlya sebya', meaning 'for oneself', is useful, and it is the same for every person. See you next time!"
CLOSING = ('vika', 'До свидания!')
STORY = [
    ('max', 'Привет. Я хотел узнать насчёт подарка.', 'Hi. I wanted to find out about the gift.', [(114, 'Я хотел узнать')], ''),
    ('max', 'Тебе понравилось это красивое кольцо?', 'Did you like this beautiful ring?', [(115, 'Тебе понравилось')], ''),
    ('vika', 'Да, оно очень красивое.', 'Yes, it is very beautiful.', [(115, 'Да, красивое')], ''),
    ('max', 'А ты знаешь, сколько оно стоит?', 'And do you know how much it costs?', [(116, 'знаешь, сколько оно стоит')], ''),
    ('max', 'Ты считаешь, это нормально для подарка?', 'You consider this normal for a gift?', [(119, 'считаешь, для подарка это нормально')], ''),
    ('vika', 'Конечно. Таня выбирала подарок для себя.', 'Of course. Tanya was choosing a gift for herself.', [(123, 'выбирала подарок')], ''),
    ('vika', 'Она просто прислала мне фотографию.', 'She simply sent me a photograph.', [(123, 'прислала мне фотографию')], ''),
    ('max', 'А я сам хотел подарить тебе кольцо.', 'But I wanted to gift you a ring myself.', [(126, 'сам хотел тебе кольцо подарить')], ''),
    ('vika', 'Ты хотел подарить то же самое?', 'You wanted to give the same thing?', [(127, 'подрезала подарок мой')], ''),
    ('vika', 'Я скажу ей выбрать что-то другое.', 'I will tell her to choose something else.', [(129, 'Пусть она что-нибудь другое выберет')], ''),
    ('vika', 'А ты мне подаришь это кольцо.', 'And you will gift me this ring.', [(130, 'А ты мне подаришь кольцо')], ''),
    ('max', 'Зачем же? Она же уже купила.', 'Why then? She already bought it.', [(132, 'Зачем же? Она же уже купила')], ''),
    ('vika', 'Нет, она просто просила совета.', 'No, she was simply asking for advice.', [(133, 'она просто выбирала, советовала')], ''),
    ('vika', 'Я сейчас ей позвоню.', 'I will call her now.', [(134, 'Я сейчас ей позвоню')], ''),
]
WALK = [
    (0, None, "'Hi. I wanted to ask about the gift.' 'Wanted to find out' uses the plain 'find out'. 'About' is a one-word phrase."),
    (1, None, "'Did you like this lovely ring?' 'Liked' is neuter, because 'ring' is neuter. 'To you' sits next to it."),
    (2, None, "'Yes, it's very pretty.' 'It' is the neuter 'ono', since 'ring' is neuter. 'Beautiful' ends in 'oe'."),
    (3, None, "'And do you know how much it costs?' 'How much' is one word. 'Costs' means 'stands' in this sense."),
    (4, None, "'Do you think that's reasonable for a gift?' 'You consider' ends in 'sh'. 'For a gift' needs a small word and an 'a'."),
    (5, None, "'Of course. Tanya was choosing a present for herself.' 'Herself' is the same for everyone, 'sebya'. 'Was choosing' is the ongoing past."),
    (6, None, "'She just sent me a photo.' 'Sent' ends in 'a', and 'just' is a small word. 'Photograph' is a borrowed word."),
    (7, None, "'But I wanted to give you the ring myself.' 'Myself' is a short word, 'sam'. 'Give as a gift' is the same word from before."),
    (8, None, "'You wanted to give the same thing?' 'The same thing' is three words, and means 'that very same'. 'Wanted' ends in 'l'."),
    (9, None, "'I'll tell her to choose something else.' 'To her' is the short word 'ey'. 'Something else' ends in 'oe' since it is neuter."),
    (10, None, "'And you'll give me this ring.' 'You'll give' is a finished action, ending in 'sh'. 'Me' takes the 'to me' form."),
    (11, None, "'What for? She's already bought it.' 'What for' asks about purpose. 'Bought' ends in 'a' for a woman."),
    (12, None, "'No, she was just asking for advice.' 'Ask for' is followed by the 'of' form, so 'advice' ends in 'a'. 'Asked' ends in 'a' for a woman."),
    (13, None, "'I'll call her now.' 'Call' goes with 'to her', not 'her'. 'I'll call' is a finished action."),
]
