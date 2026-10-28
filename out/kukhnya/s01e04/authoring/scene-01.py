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
INTRO = "Feeling unappreciated at Claude Monet, Max secretly visits the rival restaurant Arcobaleno across the street. Head chef Elena Sokolova reviews his résumé and expresses keen interest in taking him onto her kitchen staff. Encouraged by her praise, Max eagerly awaits her follow-up call. Let's listen to their interview in Russian first."
OPENER = "Now let's examine Elena Sokolova and Max's interview line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'That wraps up this scene from Kukhnya. Listen for these everyday Russian expressions when you watch the episode. See you next time!'
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
    (0, None, "'Maksim, I carefully read your résumé.' Elena tells Maksim she carefully read his resume."),
    (1, None, "'I hope you liked my experience.' Max hopes she liked his experience."),
    (2, None, "'You are a very capable and promising cook.' She calls him a very capable and promising cook."),
    (3, None, "'Thank you, I truly want to learn a lot.' Max thanks her and says he truly wants to learn a lot."),
    (4, None, "'I will gladly take you into the kitchen.' Elena says she will gladly take him into the kitchen."),
    (5, None, "'At the Claude Monet restaurant they do not appreciate me.' He complains they do not appreciate him at the Claude Monet restaurant."),
    (6, None, "'I do not understand why they act like that.' Elena does not understand why they act that way."),
    (7, None, "'There they only give me vegetables to peel.' Max says they only let him peel vegetables there."),
    (8, None, "'With us you will cook complex dishes.' She promises he will cook complex dishes with them."),
    (9, None, "'This is exactly what I dreamed about!' Max says this is exactly what he dreamed about."),
    (10, None, "'Here are my contacts just in case.' Elena gives him her contact information just in case."),
    (11, None, "'When should I expect your call?' He asks when he should expect her call."),
    (12, None, "'I will call you in a couple of days.' Elena promises to call him in a couple of days."),
]
