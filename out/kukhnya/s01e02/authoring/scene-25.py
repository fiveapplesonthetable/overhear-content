# Authoring module for kukhnya-s01e02-scene-25.
ID = 'kukhnya-s01e02-scene-25'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 25
TITLE = 'Две стороны медали  (Two Sides of the Coin)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = 'Vika has shown the owner, Nagiyev, a video of Max in a scuffle in the courtyard, hoping to get him fired. Nagiyev watches, and it turns out to be less of a fight than she claimed. Here is the Russian first.'
OPENER = "Let's go back through the video and the verdict."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max keeps his job, and even a few friends. You've heard how Russian says that every medal has two sides, which is what English calls a coin."
STORY = [
    ('nagiyev', 'Вика говорит, что ты устроил драку.', 'Vika says that you started a fight.', [(310, 'Еще он сегодня устроил драку.')], ''),
    ('max', 'Мы просто дурачились на заднем дворе.', 'We were simply fooling around in the backyard.', [(313, 'Да мы так дурачились.')], ''),
    ('nagiyev', 'Покажите мне видео этой вашей драки.', 'Show me the video of this fight of yours.', [(315, 'Я все сняла.')], ''),
    ('nagiyev', 'Разве это драка? Ты даже не дрался!', 'Is that really a fight? You did not even fight back!', [(322, 'Ну какая же это драка, а?')], ''),
    ('nagiyev', 'Так что увольнять повара пока не за что.', 'So there is no reason to fire the cook yet.', [(324, 'Так что увольнять пока его не за что.')], ''),
    ('barinov', 'Дмитрий, спасибо вам за справедливое решение.', 'Dmitry, thank you for the fair decision.', [(325, 'Спасибо большое.')], ''),
    ('barinov', 'Слушайте меня все: забудьте об этом видео!', 'Listen to me everyone: forget about this video!', [(331, 'Чтобы об этом больше никто не знал.')], ''),
    ('barinov', 'Вике ещё работать здесь арт-директором.', 'Vika still has to work here as art director.', [(332, 'но арт-директор не самый плохой')], ''),
    ('barinov', 'Кто посмеет смеяться, сразу пойдёт вон!', 'Whoever dares laugh will immediately get out!', [(333, 'Ей еще здесь работать. Понятно?')], ''),
    ('max', 'У каждой медали есть две стороны.', 'Every coin has two sides.', [(335, 'У каждой медали есть две стороны,')], ''),
    ('max', 'Однажды всё вокруг может резко измениться.', 'One day everything around can change drastically.', [(335, 'и однажды все может перевернуться.')], ''),
    ('max', 'Бывший враг неожиданно становится твоим другом.', 'A former enemy unexpectedly becomes your friend.', [(337, 'становится твоим другом.')], ''),
    ('max', 'А строгий тиран становится немного добрее.', 'And a strict tyrant becomes a little bit kinder.', [(338, 'Ну а тот, кто казался злобным тираном,')], ''),
    ('max', 'Жизнь продолжается, и завтра новый день!', 'Life goes on, and tomorrow is a new day!', [(334, 'Вот как-то так.')], ''),
]
WALK = [
    (0, None, [
        '\'Vika says that you started a fight.\' ',
        ('nagiyev', 'устроил'),
        ', translates to set up, which is how Russians say you started a fight. The word for fight, ',
        ('nagiyev', 'драку.'),
        ', gets a special ending as the thing set up.'
    ]),
    (1, None, [
        '\'We were simply fooling around in the backyard.\' The action word ',
        ('max', 'дурачились'),
        ', meaning fooled around, is built from the word for a fool. And ',
        ('max', 'на заднем дворе.'),
        ' translates to on the back yard.'
    ]),
    (2, None, [
        '\'Show me the video of this fight of yours.\' The word for show, ',
        ('nagiyev', 'Покажите'),
        ', ends with a formal sign of respect. The phrase ',
        ('nagiyev', 'этой вашей драки.'),
        ', literally meaning of this fight of yours, puts a matching ending on all three words.'
    ]),
    (3, None, [
        '\'Is that really a fight? You did not even fight back!\' The little word ',
        ('nagiyev', 'Разве'),
        ' opens a doubtful really? The action word ',
        ('nagiyev', 'дрался!'),
        ' translates to fought, and the word for even is ',
        ('nagiyev', 'даже'),
        '.'
    ]),
    (4, None, [
        '\'So there is no reason to fire the cook yet.\' The phrase ',
        ('nagiyev', 'не за что.'),
        ' literally translates to not for what, here meaning no reason. The word for yet, ',
        ('nagiyev', 'пока'),
        ', is the exact same word used for bye.'
    ]),
    (5, None, [
        '\'Dmitry, thank you for the fair decision.\' The phrase ',
        ('barinov', 'спасибо вам за'),
        ' translates to thanks for. The describing word ',
        ('barinov', 'справедливое'),
        ', literally fair, and the word for decision, ',
        ('barinov', 'решение.'),
        ', have matching endings.'
    ]),
    (6, None, [
        '\'Listen to me everyone: forget about this video!\' The action words ',
        ('barinov', 'Слушайте'),
        ' and ',
        ('barinov', 'забудьте'),
        ' are commands to the whole room. The phrase ',
        ('barinov', 'об этом'),
        ', which translates to about this, uses a special little word for a smoother sound.'
    ]),
    (7, None, [
        '\'Vika still has to work here as art director.\' There is no has to action word here. Instead, Russian puts Vika in a special shape, ',
        ('barinov', 'Вике'),
        ', adds a base action word, ',
        ('barinov', 'работать'),
        ', and the word for art director ends with a special sound, ',
        ('barinov', 'арт-директором.'),
        ', representing working as something.'
    ]),
    (8, None, [
        '\'Whoever dares laugh will immediately get out!\' The word for dares, ',
        ('barinov', 'посмеет'),
        ', sounds like the action word to laugh, ',
        ('barinov', 'смеяться,'),
        ', but is built from a different word meaning to dare. And ',
        ('barinov', 'пойдёт вон!'),
        ' translates to will get out.'
    ]),
    (9, None, [
        '\'Every coin has two sides.\' Russian uses the word for medal, ',
        ('max', 'медали'),
        ', where English says coin. The number two, ',
        ('max', 'две'),
        ', is in a special shape to match the word for sides, ',
        ('max', 'стороны.'),
        '.'
    ]),
    (10, None, [
        '\'One day everything around can change drastically.\' Russian packs one day into a single word, ',
        ('max', 'Однажды'),
        '. The word for drastically here, ',
        ('max', 'резко'),
        ', literally translates to sharply, as in a sharp turn.'
    ]),
    (11, None, [
        '\'A former enemy unexpectedly becomes your friend.\' The word for former, ',
        ('max', 'Бывший'),
        ', is built from the word was. The action word ',
        ('max', 'становится'),
        ', meaning becomes, forces the phrase for your friend into a special shape, ',
        ('max', 'твоим другом.'),
        '.'
    ]),
    (12, None, [
        '\'And a strict tyrant becomes a little bit kinder.\' The word for kinder, ',
        ('max', 'добрее.'),
        ', ends with a sound that means more. The word for a little bit is ',
        ('max', 'немного'),
        '.'
    ]),
    (13, None, [
        '\'Life goes on, and tomorrow is a new day!\' The word for goes on, ',
        ('max', 'продолжается,'),
        ', has a special ending, literally as if life keeps itself going. And ',
        ('max', 'завтра'),
        ' translates to tomorrow.'
    ]),
]
CLOSING = ("max", "Пока!")
