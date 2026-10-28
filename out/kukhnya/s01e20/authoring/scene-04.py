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
INTRO = "Max calls Vika to discuss the expensive ring she sent him. He tries to subtly figure out if she really expects him to buy it. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around Expensive Gift line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max accidentally traps himself into buying the ring when his attempt to look generous backfires. Next time you watch the episode, listen for the Russian expressions for 'to want' and 'to recognise' — you will catch every word right away. See you next time!"
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Привет. Я хотел узнать насчёт подарка.', 'Hi. I wanted to find out about the gift.', [(114, 'Я хотел узнать')], ''),
    ('max', 'Тебе понравилось это красивое кольцо?', 'Did you like this beautiful ring?', [(115, 'Тебе понравилось')], ''),
    ('vika', 'Да, оно очень красивое.', 'Yes, it is very beautiful.', [(115, 'Да, красивое')], ''),
    ('max', 'А ты знаешь, сколько оно стоит?', 'And do you know how much it costs?', [(116, 'знаешь, сколько оно стоит')], ''),
    ('max', 'Ты считаешь, это нормально для подарка?', 'You consider this normal for a gift?', [(119, 'считаешь, для подарка это нормально')], ''),
    ('vika', 'Конечно. Таня выбирала подарок для себя.', 'Of course. Tanya was choosing a gift for herself.', [(123, 'выбирала подарок')], ''),
    ('vika', 'Она просто прислала мне фотографию.', 'She simply sent me a photograph.', [(123, 'прислала мне фотографию')], ''),
    ('max', 'А я сам хотел подарить тебе кольцо.', 'But I wanted to gift you a ring myself.', [(126, 'сам хотел тебе кольцо подарить')], ''),
    ('vika', 'Она подрезала твой подарок?', 'She undercut your gift?', [(127, 'подрезала подарок мой')], ''),
    ('vika', 'Я скажу ей выбрать что-то другое.', 'I will tell her to choose something else.', [(129, 'Пусть она что-нибудь другое выберет')], ''),
    ('vika', 'А ты мне подаришь это кольцо.', 'And you will gift me this ring.', [(130, 'А ты мне подаришь кольцо')], ''),
    ('max', 'Зачем же? Она же уже купила.', 'Why then? She already bought it.', [(132, 'Зачем же? Она же уже купила')], ''),
    ('vika', 'Нет, она просто просила совета.', 'No, she was simply asking for advice.', [(133, 'она просто выбирала, советовала')], ''),
    ('vika', 'Я сейчас ей позвоню.', 'I will call her now.', [(134, 'Я сейчас ей позвоню')], ''),
]
WALK = [
    (0, None, "'Hi. I wanted to find out about the gift.' Max starts the conversation with a clear purpose."),
    (1, None, "'Did you like this beautiful ring?' Max checks if she liked the item in the picture."),
    (2, None, "'Yes, it is very beautiful.' Vika enthusiastically confirms her approval."),
    (3, None, "'And do you know how much it costs?' The question opens with the everyday word for 'how much' and builds toward 'is parked'."),
    (4, None, "'You consider this normal for a gift?' Max questions the appropriateness of such an item."),
    (5, None, "'Of course. Tanya was choosing a gift for herself.' Vika explains that her friend was shopping for herself."),
    (6, None, "'She simply sent me a photograph.' Vika clarifies it was just a casual message."),
    (7, None, "'But I wanted to gift you a ring myself.' Max reveals his original intention to buy it for her."),
    (8, None, "'She undercut your gift?' Vika realizes the conflict of interest."),
    (9, None, "'I will tell her to choose something else.' Vika offers to resolve the situation with her friend."),
    (10, None, "'And you will gift me this ring.' Vika smoothly transitions to expecting it from him instead."),
    (11, None, "'Why then? She already bought it.' Max points out the logistical problem with her plan."),
    (12, None, "'No, she was simply asking for advice.' Vika insists it was merely a consultation."),
    (13, None, "'I will call her now.' Vika takes immediate action to secure her present."),
]
