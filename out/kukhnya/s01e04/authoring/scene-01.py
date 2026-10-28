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
INTRO = "This is Kukhnya, the Russian comedy about a hot-tempered chef and the staff of a smart Moscow restaurant called Claude Monet. In this fourth episode, Max is fed up with peeling vegetables, so he sneaks off to apply for a job at a rival restaurant, Arcobaleno, whose head chef is a woman called Elena Sokolova. Here is the interview in Russian first, and don't worry about catching every word."
OPENER = "Now let's listen to the interview again, slowly."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max leaves with a promise of a phone call and a head full of dreams. If one phrase stays with you, make it "na vsyakiy sluchay", "just in case".'
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
    (0, None, '\'Maksim, I carefully read your résumé.\' Elena uses his full first name, the way you do in a formal interview. The -la on "read" shows she is a woman, and "vashe" means "your" in the polite form.'),
    (1, None, '\'I hope you liked my experience.\' Russian says "to you pleased my experience", the same "pleasing" pattern as "mne nravitsya". Here it\'s "vam ponravilsya", because "opyt", experience, is masculine.'),
    (2, None, '\'You are a very capable and promising cook.\' "Sposobnyy" comes from "sposob", a way or a means, so it\'s someone with the means. "Perspektivnyy" sounds like "perspective", and means promising.'),
    (3, None, '\'Thank you, I truly want to learn a lot.\' "Deystvitel\'no", "really", grows out of "action". "Mnogomu" is "to much", and with "learn" it means "to learn a lot".'),
    (4, None, '\'I will gladly take you into the kitchen.\' "S radost\'yu" is "with joy", Russian for "gladly". And "voz\'mu" is "I will take", one word.'),
    (5, None, '\'At the Claude Monet restaurant they do not appreciate me.\' Nobody is named: "they don\'t value me". "Value" grows from "tsena", price.'),
    (6, None, '\'I do not understand why they act like that.\' "Postupat\'" is to act or behave, and it often suggests how someone treats you. "Tak" is "so", "like that".'),
    (7, None, '\'There they only give me vegetables to peel.\' "To me they give" is how Max says "I\'m given", and "peel" is also "clean". "Ovoshchi", vegetables, is plural.'),
    (8, None, '\'With us you will cook complex dishes.\' "At us" is "with us" here, and "you will cook" is "budete gotovit\'", the future with "will be".'),
    (9, None, '\'This is exactly what I dreamed about!\' Russian stacks it up as "exactly that, about which I dreamed". The little "o", about, turns "chto", what, into "chyom". A man ends "dreamed" in -l.'),
    (10, None, '\'Here are my contacts just in case.\' "Na vsyakiy sluchay" is literally "for every chance", and it\'s what Russians say for "just in case".'),
    (11, None, '\'When should I expect your call?\' "Mne ozhidat\'", "to me to expect", makes "should I". "Zvonka" is "of the call", from "zvonok", a ring.'),
    (12, None, '\'I will call you in a couple of days.\' "Para" is a pair, so "paru dney" is "a couple of days". "Cherez" is "through", meaning "in" for future time.'),
]
