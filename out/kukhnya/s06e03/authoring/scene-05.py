# Authoring module for kukhnya-s06e03-scene-05.
ID = 'kukhnya-s06e03-scene-05'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 3
SCENE = 5
TITLE = "Травма актёра и поиск замены  (The Actor's Injury and Finding a Replacement)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'doctor': 'Врач', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.03'
SOURCE_FILE = 'sources/kukhnya/s06/e03.ru.srt'
INTRO = "On the film set, the actor playing Nagiyev's rival twists his ankle and has to be sent for an X-ray; refusing to pay for an extra shooting day, the director suggests casting the mustachioed chef instead."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Desperate to finish the shoot today without spending extra money, Nagiyev goes to recruit Chef Barinov as his co-star. Until next time!'
CLOSING = ('nagiyev', 'До встречи!')
STORY = [
    ('nagiyev', 'Как ты нас всех напугал!', 'How you scared us all!', [(72, 'Как ты нас всех напугал?')], 'adapted'),
    ('nagiyev', 'Как он, доктор?', 'How is he, doctor?', [(73, 'Как он, доктор?')], 'exact'),
    ('doctor', 'Возможно, перелом, но нужен рентген, чтобы убедиться.', 'Possibly a fracture, but an X-ray is needed to make sure.', [(73, 'перелом'), (73, 'но нужен рентген, чтобы убедиться')], 'adapted'),
    ('nagiyev', 'Завтра с утра иди на рентген.', 'Tomorrow first thing in the morning go for an X-ray.', [(74, 'Завтра с утра прямо встал, иди на рентген')], 'adapted'),
    ('doctor', 'Да вы что, его сейчас надо везти в больницу.', 'What do you mean, he needs to be taken to the hospital right now.', [(75, 'Да вы что? Его сейчас надо везти в больницу')], 'exact'),
    ('doctor', 'Давай завтра утром устроим кастинг.', "Let's hold a casting call tomorrow morning.", [(78, 'Давай завтра утром устроим кастинг')], 'exact'),
    ('doctor', 'И завтра же снимем с новым актером.', 'And tomorrow we will film with a new actor.', [(79, 'и завтра же снимем с новым актером')], 'exact'),
    ('nagiyev', 'У меня дома просто бассейн, не очень большой.', 'At home I just have a swimming pool, not a very big one.', [(81, 'У меня дома просто бассейн, не очень большой')], 'exact'),
    ('nagiyev', 'А что ты предлагаешь, ты же режиссер!', 'Well what do you suggest, you are the director!', [(82, 'А что ты предлагаешь'), (83, 'Ты режиссер')], 'adapted'),
    ('doctor', 'Слушай, а что если тот дядька с усами?', 'Listen, what about that guy with the mustache?', [(85, 'а что если тот дядька с усами')], 'adapted'),
    ('nagiyev', 'Ты же сказал, что ты с животными не любишь работать.', 'You said yourself that you do not like working with animals.', [(87, 'Ты же сказал, что ты с животными не любишь работать')], 'exact'),
    ('doctor', 'Между вами такая химия, давай попробуем.', "There is such chemistry between you two, let's try.", [(89, 'между вами такая химия'), (91, 'Давай попробуем')], 'adapted'),
]
WALK = [
    (0, None, "'How you scared us all!' Nagiyev replies calmly with the doctor, keeping the focus on what actually matters here."),
    (1, None, "'How is he, doctor?' Nagiyev questions firmly where this conversation is heading next."),
    (2, None, '\'Possibly a fracture, but an X-ray is needed to make sure.\' Focusing on a fracture during the talk, the doctor puts the emphasis on "perelom" ("fracture") in the middle of the talk.'),
    (3, None, '\'Tomorrow first thing in the morning go for an X-ray.\' Emphasizing the fine in the exchange, Nagiyev centers the remark on "rentgen" ("fine") without any extra fuss.'),
    (4, None, "'What do you mean, he needs to be taken to the hospital right now.' The doctor cuts in lightly during the talk, refusing to let the moment slip past."),
    (5, None, '\'Let\'s hold a casting call tomorrow morning.\' Focusing on a casting around Nagiyev, the doctor centers the remark on "kasting" ("casting, audition") without any extra fuss.'),
    (6, None, '\'And tomorrow we will film with a new actor.\' Talking about a new actor with Nagiyev, the doctor reaches for the Russian word "akterom" ("actor", built from "aktyor") right at the center of the line.'),
    (7, None, "'At home I just have a swimming pool, not a very big one.' Pointing to a swimming pool without holding back, Nagiyev keeps the doctor's attention locked on what matters."),
    (8, None, '\'Well what do you suggest, you are the director!\' Talking about the director at once, Nagiyev puts the weight on "predlagayesh" ("are suggesting", from "predlagat") as the exchange unfolds.'),
    (9, None, '\'Listen, what about that guy with the mustache?\' Addressing the moustache to Nagiyev, the doctor puts the question word "chto" right at the start so Nagiyev hears the focus immediately.'),
    (10, None, "'You said yourself that you do not like working with animals.' Nagiyev speaks at once in this moment, steering the talk right where he wants it."),
    (11, None, '\'There is such chemistry between you two, let\'s try.\' Turning to the chemicals right here, the doctor puts the emphasis on "khimiya" ("chemicals, chemistry") in the middle of the talk.'),
]
