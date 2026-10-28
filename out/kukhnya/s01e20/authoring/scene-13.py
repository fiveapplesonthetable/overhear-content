# Authoring module for kukhnya-s01e20-scene-13.
ID = 'kukhnya-s01e20-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 13
TITLE = 'Важный вопрос  (Important Question)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = 'Max and Kostya are talking in the kitchen about the beautiful rings they bought for their girlfriends. Senya overhears them and makes a stupid joke about them getting married to each other.'
OPENER = "Now let's examine this conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Kostya decides to go and give the ring to Nastya right away. Max wishes his friend good luck with his romantic proposal. Next time you watch the episode, listen for the Russian expressions for 'to buy' and 'ring' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Костя, ты купил кольцо для Насти?', 'Kostya, did you buy a ring for Nastya?', [(207, 'Ну что, купил кольцо? Да.')], ''),
    ('kostya', 'Да, я купил. А ты купил?', 'Yes, I bought it. And did you buy?', [], ''),
    ('max', 'Да, я тоже купил кольцо для Вики.', 'Yes, I also bought a ring for Vika.', [], ''),
    ('kostya', 'Покажи мне свое кольцо, пожалуйста.', 'Show me your ring, please.', [], ''),
    ('senya', 'Вы покупаете кольца друг для друга?', 'Are you buying rings for each other?', [], ''),
    ('max', 'Тебе какое дело, Сеня? Уйди.', 'What is it to you, Senya? Go away.', [], ''),
    ('senya', 'Просто интересно, когда будет ваша свадьба?', 'Just interesting, when will be your wedding?', [], ''),
    ('kostya', 'Это не твоя проблема. Замолчи.', 'This is not your problem. Shut up.', [], ''),
    ('senya', 'Ладно, ладно. Я просто пошутил.', 'Okay, okay. I just joked.', [], ''),
    ('max', 'Ты уже подарил кольцо Насте?', 'Did you already give the ring to Nastya?', [], ''),
    ('kostya', 'Еще нет. Я хочу сделать это сейчас.', 'Not yet. I want to do this now.', [], ''),
    ('max', 'Удачи тебе, Костя. Это важный момент.', 'Good luck to you, Kostya. This is an important moment.', [], ''),
    ('kostya', 'Спасибо, Макс. Тебе тоже удачи с Викой.', 'Thank you, Max. Good luck to you with Vika too.', [], ''),
    ('max', 'Да, мне нужна большая удача сегодня.', 'Yes, I need big luck today.', [], ''),
]
WALK = [
    (0, None, "'Kostya, did you buy a ring for Nastya?' Max asks his friend directly if he purchased the engagement ring."),
    (1, None, "'Yes, I bought it. And did you buy?' Kostya confirms his purchase and throws the question right back."),
    (2, None, "'Yes, I also bought a ring for Vika.' Max proudly announces he got one for Vika as well."),
    (3, None, "'Show me your ring, please.' Kostya asks to see the jewelry his friend picked out."),
    (4, None, "'Are you buying rings for each other?' Senya overhears and makes a sarcastic joke about their relationship."),
    (5, None, "'What is it to you, Senya? Go away.' Max angrily tells Senya to mind his own business and leave."),
    (6, None, "'Just interesting, when will be your wedding?' Senya continues teasing them about a hypothetical wedding."),
    (7, None, "'This is not your problem. Shut up.' Kostya aggressively shuts down the kitchen prankster."),
    (8, None, "'Okay, okay. I just joked.' Senya backs off, claiming he was only messing around."),
    (9, None, "'Did you already give the ring to Nastya?' Max refocuses and asks if the proposal happened yet."),
    (10, None, "'Not yet. I want to do this now.' Kostya admits he is still waiting for the right moment today."),
    (11, None, "'Good luck to you, Kostya. This is an important moment.' Max offers sincere encouragement for the big step."),
    (12, None, "'Thank you, Max. Good luck to you with Vika too.' Kostya returns the supportive wishes for Max's own proposal."),
    (13, None, "'Yes, I need big luck today.' Max admits he is going to need all the help he can get."),
]
