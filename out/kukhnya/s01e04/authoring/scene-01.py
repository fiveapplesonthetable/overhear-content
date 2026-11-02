# Authoring module for kukhnya-s01e04-scene-01.
ID = 'kukhnya-s01e04-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = 'Собеседование у конкурентов  (An Interview with the Competitor)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'elena': 'Елена', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "This is the Russian comedy about a hot-tempered chef and the staff of a smart Moscow restaurant called Claude Monet. In this fourth episode, Max is fed up with peeling vegetables, so he sneaks off to apply for a job at a rival restaurant, Arcobaleno, whose head chef is a woman called Elena Sokolova. Here is the interview in Russian first, and don't worry about catching every word."
OPENER = "Now let's listen to the interview again, slowly."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max leaves with a promise of a phone call and a head full of dreams. If you remember one thing, make it the phrase for just in case, which literally translates to for any occasion."
CLOSING = ('elena', 'Пока!')
STORY = [
    ('elena', 'Максим, я внимательно прочла ваше резюме.', 'Maksim, I carefully read your résumé.', [(1, 'Я прочла резюме')], ''),
    ('max', 'Надеюсь, вам понравился мой опыт.', 'I hope you liked my experience.', [], ''),
    ('elena', 'Вы очень способный и перспективный повар.', 'You are a very capable and promising cook.', [(2, 'такого перспективного работника')], ''),
    ('max', 'Спасибо, я действительно хочу многому научиться.', 'Thank you, I truly want to learn a lot.', [], ''),
    ('elena', 'Я с радостью возьму вас на кухню.', 'I will gladly take you into the kitchen.', [(2, 'могу взять к себе на кухню')], ''),
    ('max', 'В ресторане Клод Моне меня не ценят.', 'At the Claude Monet restaurant they do not appreciate me.', [(3, 'почему в Мане они ценят такие кадры')], ''),
    ('elena', 'Я не понимаю, почему они так поступают.', 'I do not understand why they act like that.', [(3, 'вообще не понимаю')], ''),
    ('max', 'Там мне дают только чистить овощи.', 'There they only give me vegetables to peel.', [], ''),
    ('elena', 'У нас вы будете готовить сложные блюда.', 'With us you will cook complex dishes.', [], ''),
    ('max', 'Это именно то, о чём я мечтал!', 'This is exactly what I dreamed about!', [], ''),
    ('elena', 'Вот мои контакты на всякий случай.', 'Here are my contacts just in case.', [(4, 'Это мои контакты на всякий случай')], ''),
    ('max', 'Когда мне ожидать вашего звонка?', 'When should I expect your call?', [], ''),
    ('elena', 'Я позвоню вам через пару дней.', 'I will call you in a couple of days.', [(5, 'я позвоню вам через пару дней')], ''),
]
WALK = [
    (0, None, ["'Maksim, I carefully read your résumé.' Elena uses the full name, as an interviewer would. The word for read, ", ('elena', 'прочла'), ", ends with an 'a' sound because Elena is a woman, and ", ('elena', 'ваше'), " marks the polite form of 'your'."]),
    (1, None, ["'I hope you liked my experience.' Russian turns it round, literally translating to ", ('max', 'вам понравился'), ", 'to you was pleasing'. The action word ends without an 'a' sound because the Russian term for experience, ", ('max', 'опыт.'), ", has a male form."]),
    (2, None, ["'You are a very capable and promising cook.' The translation for capable, ", ('elena', 'способный'), ", is built from the Russian expression for 'a way of doing something'. The word for promising, ", ('elena', 'перспективный'), ", sounds like 'perspective', and means a cook with a bright future."]),
    (3, None, ["'Thank you, I truly want to learn a lot.' The Russian expression for truly, ", ('max', 'действительно'), ", has the Russian expression for action inside it: true in deed. The phrase ", ('max', 'многому научиться.'), " literally translates to 'to learn to much', which is the way to say 'learn a lot'."]),
    (4, None, ["'I will gladly take you into the kitchen.' The phrase ", ('elena', 'с радостью'), " literally translates to 'with joy', which is how the language expresses 'gladly'. The action word for 'I will take', ", ('elena', 'возьму'), ", describes an action that will happen later."]),
    (5, None, ["'At the Claude Monet restaurant they do not appreciate me.' The translation for 'they do not appreciate', ", ('max', 'не ценят.'), ", leaves the people unnamed. This action word is built from the expression for 'price'."]),
    (6, None, ["'I do not understand why they act like that.' The Russian term for act, ", ('elena', 'поступают.'), ", is usually about how people treat someone. The little word ", ('elena', 'так'), " translates to 'like that'."]),
    (7, None, ["'There they only give me vegetables to peel.' The phrase ", ('max', 'мне дают'), " translates to 'to me they give', without naming who gives it. The expression for to peel, ", ('max', 'чистить'), ", is built from the describing word for 'clean', so peeling is thought of as cleaning."]),
    (8, None, ["'With us you will cook complex dishes.' The phrase ", ('elena', 'У нас'), " literally translates to 'at us', meaning 'at our place'. The action word ", ('elena', 'будете'), " means 'you will be', and is paired with 'to cook' to describe the future."]),
    (9, None, ["'This is exactly what I dreamed about!' The sentence literally translates to 'this is exactly that about which I dreamed'. After the little word meaning 'about', as in ", ('max', 'о чём'), ", the Russian expression for 'what' changes its form."]),
    (10, None, ["'Here are my contacts just in case.' The phrase ", ('elena', 'на всякий случай.'), " literally translates to 'for any occasion', and it is the standard way to say 'just in case'. The Russian term for contacts is borrowed directly from English."]),
    (11, None, ["'When should I expect your call?' The phrase ", ('max', 'мне ожидать'), " literally translates to 'to me to expect', creating the 'should I' question with no action word for 'should'. The Russian expression for a call, ", ('max', 'звонка?'), ", takes a special ending here because it follows the expectation."]),
    (12, None, ["'I will call you in a couple of days.' The Russian term for a pair is used here, so ", ('elena', 'пару дней.'), " means a couple of days. The word ", ('elena', 'через'), " translates to 'across', and marks time from now to mean 'in a couple of days'."]),
]
