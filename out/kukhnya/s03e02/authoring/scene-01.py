# Authoring module for kukhnya-s03e02-scene-01.
ID = 'kukhnya-s03e02-scene-01'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 2
SCENE = 1
TITLE = "Терпение официанта  (A Waiter's Patience)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.02'
SOURCE_FILE = 'sources/kukhnya/s03/e02.ru.srt'
INTRO = 'In Episode Two of Season Three, Max reflects on what quality matters most for a waiter at Claude Monet: not just manners or dramatic presentation, but endless patience with indecisive guests.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that finishes our opening scene. Listen for the contrast between the guest who orders a single coffee after ten minutes and the guest who leaves a generous tip. Until next time!'
CLOSING = ('max', 'До завтра!')
STORY = [
    ('max', 'Что самое важное в работе официанта?', "What is the most important thing in a waiter's job?", [(1, 'что самое важное в работе официанта')], ''),
    ('max', 'Манеры? Вежливость?', 'Manners? Politeness?', [(2, 'Манеры'), (3, 'Может быть')], 'adapted'),
    ('max', 'Эффектная подача блюд делает их вкуснее.', 'Spectacular presentation of dishes makes them tastier.', [(4, 'эффектная подача блюд'), (4, 'вкуснее')], 'adapted'),
    ('max', 'Индивидуальный подход?', 'An individual approach?', [(5, 'Индивидуальный подход')], ''),
    ('guest', 'Так, это мне нельзя. Это тоже.', 'Right, I am not allowed to have this. This either.', [(6, 'Так, это мне нельзя'), (7, 'Это тоже')], ''),
    ('max', 'По-моему, главное — это терпение.', 'In my opinion, the main thing is patience.', [(8, 'По-моему, главное в работе официанта – это терпение')], 'adapted'),
    ('guest', 'Знаете что, дайте мне кофе.', 'You know what, give me a coffee.', [(9, 'Знаете что, дайте мне кофе')], ''),
    ('guest', 'И всё.', 'And that is all.', [(10, 'И всё')], ''),
    ('max', 'Ты что делаешь? Заказал просто кофе!', 'What are you doing? He ordered just coffee!', [(11, 'Ты что делаешь'), (11, 'заказал просто кофе')], 'adapted'),
    ('guest', 'Кофе? Да, дайте мне кофе эспрессо.', 'Coffee? Yes, give me an espresso coffee.', [(13, 'Кофе? Да, дайте мне кофе эспрессо')], ''),
    ('guest', 'И вот, сдачи не надо.', 'And here, keep the change.', [(14, 'И вот, сдачи не надо')], ''),
    ('max', 'Порой терпение очень щедро вознаграждается.', 'Sometimes patience is very generously rewarded.', [(15, 'порой терпение в нашей работе очень щедро вознаграждается')], 'adapted'),
]
WALK = [
    (0, None, "'What is the most important thing in a waiter's job?' Here asking what the most important thing in a waiter job is shows Max looking for the real truth."),
    (1, None, '\'Manners? Politeness?\' Over the point and the menu, Max presses the guest for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, "'Spectacular presentation of dishes makes them tastier.' Even though spectacular presentation of dishes makes them tastier, Max keeps a steady face in front of the guest."),
    (3, None, "'An individual approach?' With the point and moment hanging in the air, Max puts the guest on the spot."),
    (4, None, '\'Right, I am not allowed to have this. This either.\' Saying that right he is not allowed to have this is how the guest sets the tone with Max. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (5, None, '\'In my opinion, the main thing is patience.\' Once in his opinion the main thing is patience, Max can finally tell the guest what he means. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (6, None, "'You know what, give me a coffee.' Around the moment and guest, the guest sets a calm, everyday tone with Max."),
    (7, None, "'And that is all.' The guest tells Max that that is all without dressing it up."),
    (8, None, '\'What are you doing? He ordered just coffee!\' Here asking what the guest doing is shows Max looking for the real truth. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (9, None, "'Coffee? Yes, give me an espresso coffee.' Around the guest and moment, the guest wants to know where Max really stands."),
    (10, None, '\'And here, keep the change.\' Around the moment and conversation, the guest sets a calm, everyday tone with Max. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (11, None, "'Sometimes patience is very generously rewarded.' Because sometimes patience is very generously rewarded, Max treats the matter as settled."),
]
