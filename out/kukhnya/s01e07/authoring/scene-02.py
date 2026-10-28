# Authoring module for kukhnya-s01e07-scene-02.
ID = 'kukhnya-s01e07-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 2
TITLE = 'Секретный жилец  (The Secret Resident)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = "Arriving at Claude Monet well before his shift, Kostya finds Max wandering around in casual clothes instead of his chef uniform. Pressing him for answers, Kostya uncovers Max's shocking secret: to avoid Moscow's exorbitant rents, Max has been sleeping overnight in the restaurant dining room. Let's listen to their confrontation in Russian first."
OPENER = "Now let's examine Kostya and Max's confrontation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Terrified of what Chef Barinov would do if he caught a cook sleeping in the restaurant, Kostya considers how to help his friend out of this dangerous situation. Next time you watch the episode, listen for the Russian expressions for 'fast' and 'at all' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Костя, почему ты пришёл так рано?', 'Kostya, why did you arrive so early?', [(5, 'ты как так рано приперся')], ''),
    ('kostya', 'Сейчас уже восемь часов утра, Макс.', "It is already eight o'clock in the morning, Max.", [(6, 'Не рано')], ''),
    ('max', 'Я думал, что ресторан ещё закрыт.', 'I thought that the restaurant was still closed.', [], ''),
    ('kostya', 'Почему ты ещё не надел форму?', "Why haven't you put on your uniform yet?", [(6, 'Че не переоделся')], ''),
    ('max', 'Мой ключ от шкафа лежит здесь.', 'My locker key is lying here.', [(7, 'А у меня ключ здесь')], ''),
    ('kostya', 'Тогда иди быстрее в раздевалку персонала.', 'Then go faster to the staff locker room.', [(8, 'Ну и вали переодеваться')], ''),
    ('max', 'Не командуй мной, я всё успею.', 'Do not boss me around, I will manage everything in time.', [(9, 'Погоди, че ты меня строишь')], ''),
    ('kostya', 'Что ты вообще делал здесь ночью?', 'What were you doing here at night at all?', [(9, 'Че ты здесь делаешь')], ''),
    ('max', 'Честно говоря, я живу прямо здесь.', 'Honestly speaking, I live right here.', [(10, 'Живу я здесь')], ''),
    ('kostya', 'Ты ночуешь в ресторане шефа Баринова?!', "You spend the night in Chef Barinov's restaurant?!", [(10, 'Как так')], ''),
    ('max', 'Да, я сплю на диване в зале.', 'Yes, I sleep on the sofa in the dining room.', [(11, 'Так, так')], ''),
    ('kostya', 'Если шеф узнает, он тебя убьёт!', 'If the chef finds out, he will kill you!', [], ''),
    ('max', 'Пожалуйста, не рассказывай никому мой секрет.', 'Please do not tell anyone my secret.', [], ''),
]
WALK = [
    (0, None, "'Kostya, why did you arrive so early?' Max turns the question around, wondering why Kostya is here so soon."),
    (1, None, "'It is already eight o'clock in the morning, Max.' Kostya points out the actual time, showing it is morning already."),
    (2, None, "'I thought that the restaurant was still closed.' He genuinely believed he was safe from being caught before opening hours."),
    (3, None, "'Why haven't you put on your uniform yet?' The lack of kitchen attire immediately raises a red flag."),
    (4, None, "'My locker key is lying here.' Max tries to deflect by casually mentioning his locker key."),
    (5, None, "'Then go faster to the staff locker room.' Kostya urges his friend to get changed before anyone sees him."),
    (6, None, "'Do not boss me around, I will manage everything in time.' He gets defensive, claiming he has everything under control."),
    (7, None, "'What were you doing here at night at all?' Suspicion finally takes over as Kostya demands to know the truth."),
    (8, None, "'Honestly speaking, I live right here.' Max confesses his desperate housing situation with total honesty."),
    (9, None, "'You spend the night in Chef Barinov's restaurant?!' The idea of sleeping at work leaves Kostya utterly speechless."),
    (10, None, "'Yes, I sleep on the sofa in the dining room.' He confirms the crazy setup, specifically mentioning the dining room furniture."),
    (11, None, "'If the chef finds out, he will kill you!' The chef will be furious if he discovers a squatter in his establishment."),
    (12, None, "'Please do not tell anyone my secret.' Max begs for silence, knowing his job is on the line."),
]
