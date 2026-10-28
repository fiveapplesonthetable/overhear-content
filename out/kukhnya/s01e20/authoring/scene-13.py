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
INTRO = "Max and Kostya are both nervous: each has bought a ring for his girlfriend, and each wants to see the other's. Senya overhears and makes a joke at their expense. Russian first, no need to catch it all."
OPENER = 'Now for a closer look.'
TRANSITION = 'Once more, all the way through.'
OUTRO = "Both friends are about to find out whether they've chosen the right moment. 'Drug dlya druga' means 'for each other' and is literally 'friend for friend'. See you next time!"
CLOSING = ('kostya', 'До свидания!')
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
    (0, None, "'Kostya, did you buy a ring for Nastya?' The name changes its ending after 'for', with the final 'ya' turning into 'i'. 'Bought' ends in the masculine 'l'."),
    (1, None, "'Yes, I bought one. Did you?' Kostya repeats 'bought' as his answer. That is how Russians say yes."),
    (2, None, "'Yes, I bought a ring for Vika too.' The girl's name takes the same 'i' ending after 'for'. 'Too' sits in front of 'bought'."),
    (3, None, "'Show me your ring, please.' 'Show' is the friendly command. 'Own' is a special word, here in the neuter, as 'ring' is neuter."),
    (4, None, "'Are you buying rings for each other?' 'Friend for friend' is the Russian for 'for each other'. 'You buy' is plural."),
    (5, None, "'What's it to you, Senya? Go away.' 'To you what business' is the rude 'mind your own'. 'Go away' is a once-and-done action."),
    (6, None, "'I'm just curious, when's your wedding?' 'Interesting' on its own means 'I wonder'. 'Wedding' is a word you'll learn quickly."),
    (7, None, "'It's not your problem. Shut up.' 'Shut up' has a prefix 'za' on 'be silent'. It is a rude command."),
    (8, None, "'Okay, okay. I was only joking.' 'Joked' has the prefix 'po', for 'cracked a joke'. Doubling 'okay' sounds soothing."),
    (9, None, "'Have you already given the ring to Nastya?' The name takes an 'e' ending when someone is given something. 'Gave as a gift' is a once-and-done action."),
    (10, None, "'Not yet. I want to do it now.' 'Not yet' is literally 'still no'. 'Now' closes the line."),
    (11, None, "'Good luck, Kostya. It's an important moment.' 'Of luck to you' is the wish. 'Important' agrees with the masculine 'moment'."),
    (12, None, "'Thanks, Max. Good luck with Vika too.' The girl's name takes an 'oy' ending after 'with'. 'Too' sits before 'luck'."),
    (13, None, "'Yes, I need lots of luck today.' 'Needed' finishes with 'a' to match the feminine 'luck'. 'Big' finishes with 'aya' for the same reason."),
]
