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
    (0, None, '\'Maksim, I carefully read your résumé.\' Elena uses the full "Maksim", as an interviewer would. "Prochla", read, ends in -la because she is a woman, and "vashe" is the polite "your".'),
    (1, None, '\'I hope you liked my experience.\' Russian turns it round: "vam ponravilsya moy opyt", to you was pleasing my experience. "Ponravilsya" ends in -sya with no -a, because "opyt" is masculine.'),
    (2, None, '\'You are a very capable and promising cook.\' "Sposobnyy", capable, grows out of "sposob", a way of doing something. "Perspektivnyy" sounds like "perspective", and means a cook with a future.'),
    (3, None, '\'Thank you, I truly want to learn a lot.\' "Deystvitel\'no", truly, has "deystviye", action, inside it: true in deed. "Mnogomu nauchit\'sya" is "to learn to much", the way Russian says "learn a lot".'),
    (4, None, '\'I will gladly take you into the kitchen.\' "S radost\'yu" is "with joy", which is how Russian says "gladly". "Voz\'mu", I will take, is the future of "vzyat\'".'),
    (5, None, '\'At the Claude Monet restaurant they do not appreciate me.\' "Ne tsenyat" is "they don\'t value", with nobody named. The verb has "tsena", price, at its root.'),
    (6, None, '\'I do not understand why they act like that.\' "Postupat\'" is to act or behave, usually about how people treat someone. "Tak" is "like that".'),
    (7, None, '\'There they only give me vegetables to peel.\' "Mne dayut", to me they give, has no named subject. "Chistit\'", to peel, comes from "chistyy", clean, so peeling is cleaning.'),
    (8, None, '\'With us you will cook complex dishes.\' "U nas", at us, is "at our place". "Budete gotovit\'" builds the future from "budete", you will be, plus "to cook".'),
    (9, None, '\'This is exactly what I dreamed about!\' The Russian runs "eto imenno to, o chyom ya mechtal", this is exactly that about which I dreamed. After "o", "chto" turns into "chyom".'),
    (10, None, '\'Here are my contacts just in case.\' "Na vsyakiy sluchay" is "for any occasion", and it is the fixed phrase for "just in case". "Kontakty" is borrowed.'),
    (11, None, '\'When should I expect your call?\' "Mne ozhidat\'", to me to expect, makes the "should I" question with no verb for "should". "Zvonka" is "zvonok", a call, in the "of" form after "ozhidat\'".'),
    (12, None, '\'I will call you in a couple of days.\' "Para" is a pair, so "paru dney" is a couple of days. "Cherez", across, marks time from now: "cherez paru dney", in a couple of days.'),
]
