# Authoring module for kukhnya-s01e20-scene-13.
ID = 'kukhnya-s01e20-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 13
TITLE = "Важный вопрос  (Important Question)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja", "senya": "angelina"}
LABELS = {"anya": "Макс", "kostya": "Костя", "senya": "Сеня"}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = 'Max and Kostya are talking in the kitchen about the beautiful rings they bought for their girlfriends. Senya overhears them and makes a stupid joke about them getting married to each other.'
OPENER = "Now let's examine this conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Kostya decides to go and give the ring to Nastya right away. Max wishes his friend good luck with his romantic proposal. Next time you watch the episode, listen for the Russian expressions for 'to buy' and 'ring' — you will catch every word right away. See you next time!"
CLOSING = ("anya", "Пока!")
STORY = [
    ('anya', 'Костя, ты купил кольцо для Насти?', 'Kostya, did you buy a ring for Nastya?', [(207, 'Ну что, купил кольцо? Да.')], ''),
    ('kostya', 'Да, я купил. А ты купил?', 'Yes, I bought it. And did you buy?', [], ''),
    ('anya', 'Да, я тоже купил кольцо для Вики.', 'Yes, I also bought a ring for Vika.', [], ''),
    ('kostya', 'Покажи мне свое кольцо, пожалуйста.', 'Show me your ring, please.', [], ''),
    ('senya', 'Вы покупаете кольца друг для друга?', 'Are you buying rings for each other?', [], ''),
    ('anya', 'Тебе какое дело, Сеня? Уйди.', 'What is it to you, Senya? Go away.', [], ''),
    ('senya', 'Просто интересно, когда будет ваша свадьба?', 'Just interesting, when will be your wedding?', [], ''),
    ('kostya', 'Это не твоя проблема. Замолчи.', 'This is not your problem. Shut up.', [], ''),
    ('senya', 'Ладно, ладно. Я просто пошутил.', 'Okay, okay. I just joked.', [], ''),
    ('anya', 'Ты уже подарил кольцо Насте?', 'Did you already give the ring to Nastya?', [], ''),
    ('kostya', 'Еще нет. Я хочу сделать это сейчас.', 'Not yet. I want to do this now.', [], ''),
    ('anya', 'Удачи тебе, Костя. Это важный момент.', 'Good luck to you, Kostya. This is an important moment.', [], ''),
    ('kostya', 'Спасибо, Макс. Тебе тоже удачи с Викой.', 'Thank you, Max. Good luck to you with Vika too.', [], ''),
    ('anya', 'Да, мне нужна большая удача сегодня.', 'Yes, I need big luck today.', [], ''),
]
WALK = [
    (0, None, "'Kostya, did you buy a ring for Nastya?' Max turns a statement into a question purely through rising intonation on the word meaning 'bought', followed by 'ring'."),
    (1, None, "'Yes, I bought it. And did you buy?' Kostya turns a statement into a question purely through rising intonation on the word meaning 'bought' to make the point directly in conversation."),
    (2, None, "'Yes, I also bought a ring for Vika.' The phrasing opens with 'too' before bringing in 'bought' and 'ring' to make the point clear."),
    (3, None, "'Show me your ring, please.' Kostya leads with the direct command form meaning 'show', followed by 'ring'."),
    (4, None, "'Are you buying rings for each other?' Senya turns a statement into a question purely through rising intonation on the word meaning 'are buying', pairing it with 'ring' and 'friend'."),
    (5, None, "'What is it to you, Senya? Go away.' Max leads with the direct command form meaning 'go away', pairing it with 'what a' and 'matter'."),
    (6, None, "'Just interesting, when will be your wedding?' The phrasing opens with 'just' before bringing in 'interesting' and 'when' to make the point clear."),
    (7, None, "'This is not your problem. Shut up.' The little negative word sits right in front of the verb for 'to fall silent', just like 'not' in English. Then Senya replies."),
    (8, None, "'Okay, okay. I just joked.' Senya puts the word for 'just' together with 'to joke' in a crisp, natural spoken turn of phrase."),
    (9, None, "'Did you already give the ring to Nastya?' Max turns a statement into a question purely through rising intonation on the word meaning 'already', pairing it with 'donated' and 'ring'."),
    (10, None, "'Not yet. I want to do this now.' The phrasing opens with 'still' before bringing in 'want' and 'to do' to make the point clear."),
    (11, None, "'Good luck to you, Kostya. This is an important moment.' Russian omits the present-tense verb 'to be' here, linking 'luck' directly with 'important', combining 'luck' with 'important' and 'moment'."),
    (12, None, "'Thank you, Max. Good luck to you with Vika too.' Russian omits the present-tense verb 'to be' here, linking 'thank you' directly with 'too', combining 'thank you' with 'too' and 'luck'."),
    (13, None, "'Yes, I need big luck today.' Russian omits the present-tense verb 'to be' here, linking 'needed' directly with 'large', combining 'needed' with 'large' and 'good luck'."),
]
