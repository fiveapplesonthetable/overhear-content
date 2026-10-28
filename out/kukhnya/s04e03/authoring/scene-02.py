# Authoring module for kukhnya-s04e03-scene-02.
ID = 'kukhnya-s04e03-scene-02'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 3
SCENE = 2
TITLE = 'Мастер-класс на складе  (Master Class in the Storage Room)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'lyova': 'Лёва', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.03'
SOURCE_FILE = 'sources/kukhnya/s04/e03.ru.srt'
INTRO = "In the storage room of Claude Monet, Max shows Denis how to peel potatoes without giving away that he is not a trained cook, until sous-chef Lyova walks in. Let's hear the dialogue in Russian first."
OPENER = "Now let's walk through the Russian dialogue together."
TRANSITION = "Let's hear the entire conversation one more time from start to finish."
OUTRO = "That covers Max coaching Denis in the storage room before Nagiyev's staff meeting. See you next time!"
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('max', 'Кто так чистит, салага?', 'Who peels like that, rookie?', [(26, 'Кто так чистит, салага?')], ''),
    ('denis', 'Мне кажется, все уже догадались.', 'I think everyone has already guessed.', [(27, 'Мне кажется, все уже догадались')], ''),
    ('denis', 'Что я вообще совсем не повар.', 'That I am not a cook at all.', [(27, 'что я'), (27, 'не повар.')], 'adapted'),
    ('max', 'Да пока ты на складе, никто ничего не поймёт.', 'As long as you are in the storage room, nobody will figure anything out.', [(28, 'на складе никто ничего не поймет.')], ''),
    ('max', 'А заготовщиком можно и полгода пробыть.', 'And you can stay a prep cook for half a year.', [(29, 'А заготовщиком можно и полгода пробыть.')], ''),
    ('max', 'Поверь моему опыту.', 'Trust my experience.', [(30, 'моему опыту.')], ''),
    ('lyova', 'Ты и картошку за него чистить будешь, да?', 'Are you going to peel potatoes for him too, huh?', [(31, 'Ты и картошку за него'), (31, 'будешь, да?')], ''),
    ('lyova', 'Заканчивай мастер-класс.', 'Wrap up the master class.', [(32, 'Заканчивай мастер-класс.')], ''),
    ('lyova', 'Нагиев весь персонал собирает.', 'Nagiyev is gathering the entire staff.', [(33, 'Нагиев весь персонал собирает.')], ''),
    ('denis', 'Пойдём скорее.', "Let's go quickly.", [(33, 'собирает')], ''),
    ('max', 'Сейчас идём, Лёв.', 'We are coming right now, Lyova.', [(32, 'мастер-класс')], ''),
    ('lyova', 'Быстрее давайте.', 'Come on, hurry up.', [(31, 'будешь, да?')], ''),
]
WALK = [
    (0, None, '\'Who peels like that, rookie?\' With the room and plan hanging in the air, Max puts Denis on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (1, None, "'I think everyone has already guessed.' Pointing out that he thinks everyone has already guessed gives Lyova a sobering reality check."),
    (2, None, "'That I am not a cook at all.' Admitting that that he is not a cook at all shows Denis being honest for a change."),
    (3, None, '\'As long as you are in the storage room, nobody will figure anything out.\' Saying that as long as Denis is in the storage room nobody will figure anything out is how Max sets the tone with Denis. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
    (4, None, "'And you can stay a prep cook for half a year.' Once Denis can stay a prep cook for half a year, Max can finally tell Denis what he means. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (5, None, "'Trust my experience.' Adding that Denis should trust his experience fills in the missing piece for Denis."),
    (6, None, '\'Are you going to peel potatoes for him too, huh?\' Here asking whether Denis going to peel potatoes for him too huh shows Lyova looking for the real truth. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (7, None, "'Wrap up the master class.' Between the moment and the truth, Lyova gives Denis a quick, grounded response."),
    (8, None, "'Nagiyev is gathering the entire staff.' Mentioning that Nagiyev is gathering the entire staff moves the talk in a new direction."),
    (9, None, "'Let's go quickly.' Here going quickly together sets up the next turn in their exchange."),
    (10, None, "'We are coming right now, Lyova.' Because they are coming right now, Max treats the matter as settled."),
    (11, None, "'Come on, hurry up.' Telling Denis to come on hurry up is how Lyova lays out the situation for Denis."),
]
