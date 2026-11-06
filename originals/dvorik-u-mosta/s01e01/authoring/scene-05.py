# Authoring module for dvorik-u-mosta-s01e01-scene-05.
ID = 'dvorik-u-mosta-s01e01-scene-05'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = 'Это не мои вещи!  (Not My Clothes!)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'larisa': 'Лариса', 'kira': 'Кира', 'matvey': 'Матвей'}
INTRO = "Two minutes after going upstairs, Room 4's buzzer rings at the desk four times in a row. Kira hurries up to find Larisa Borisovna and Matvey staring into the open suitcase. Listen first."
OPENER = "Now let's take each line slowly and look closely at the words."
TRANSITION = "Now let's hear the whole scene again without stopping."
OUTRO = "Instead of dresses and sheet music, the blue suitcase holds big brown shoes and a wooden toy train. Let's see what is written on that tag next time."
CLOSING = ('kira', 'До скорого!')
STORY = [
    ('kira', 'Лариса Борисовна, всё в порядке? Вы звонили!', 'Larisa Borisovna, is everything alright? You rang!'),
    ('larisa', 'Посмотрите в этот чемодан, Кира! Это не моя сумка!', 'Look inside this suitcase, Kira! This is not my bag!'),
    ('kira', 'Подождите — снаружи он тёмно-синий, совсем как ваш!', 'Wait — outside it is dark blue, just like yours!'),
    ('larisa', 'Снаружи одинаковый, да! Но посмотрите внутрь!', 'Identical on the outside, yes! But look inside!'),
    ('matvey', 'Тут мужские коричневые ботинки и серые свитеры, а не платья.', "Here are men's brown shoes and grey sweaters, not dresses."),
    ('kira', 'А что это в белой бумаге? Маленький поезд из дерева!', 'And what is this in white paper? A little train made of wood!'),
    ('larisa', 'Я точно не ношу сорок четвёртый размер обуви!', 'I certainly do not wear size forty-four shoes!'),
    ('matvey', 'Понятно, почему он такой тяжёлый. Дерево и кожа!', 'No wonder it is so heavy. Wood and leather!'),
    ('larisa', 'На вокзале кто-то по ошибке забрал мой синий чемодан!', 'Someone at the station took my blue suitcase by mistake!'),
    ('kira', 'Садитесь, пожалуйста. Не волнуйтесь, сейчас мы проверим бирку.', 'Please sit down. Do not worry, we will check the tag right now.'),
    ('matvey', 'Сбоку на ручке висит маленькая бумажная карточка.', 'A small paper card is hanging on the side handle.'),
    ('larisa', 'Ох, давайте спустим чемодан вниз, к свету!', 'Oh, let us bring the suitcase downstairs to the light!'),
]
WALK = [
    (0, None, ["'Larisa Borisovna, is everything alright? You rang!' Checking on someone in a hurry uses ", (None, 'всё в порядке?'), " — literally 'everything in order?'."]),
    (1, None, ["'Look inside this suitcase, Kira! This is not my bag!' Placing ", (None, 'не моя'), " right in front of 'my' negates ownership cleanly without needing any 'is'."]),
    (2, None, ["'Wait — outside it is dark blue, just like yours!' Compound colours link with a hyphen: ", (None, 'тёмно-синий,'), " blends 'dark' with Russian's distinct word for deep navy blue."]),
    (3, None, ["'Identical on the outside, yes! But look inside!' Hear the pair: ", (None, 'Снаружи'), " means 'on the outside', contrasted right away with ", (None, 'внутрь!'), " meaning 'to the inside'."]),
    (4, None, ["'Here are men's brown shoes and grey sweaters, not dresses.' Matvey sharpens the contrast using ", (None, 'а не'), " — Russian's crisp formula for 'and not', correcting a wrong expectation."]),
    (5, None, ["'And what is this in white paper? A little train made of wood!' The little word for 'from' also names materials, so ", (None, 'из дерева!'), " means 'out of wood'."]),
    (6, None, ["'I certainly do not wear size forty-four shoes!' Here ", (None, 'точно'), " means 'definitely' or 'for sure', adding dry humour to her protest."]),
    (7, None, "'No wonder it is so heavy. Wood and leather!' Matvey opens with a single word meaning 'understandable', connecting the mystery weight from scene four to the heavy boots inside."),
    (8, None, ["'Someone at the station took my blue suitcase by mistake!' Remember the handy chunk ", (None, 'по ошибке'), " whenever something happens accidentally, 'by mistake'."]),
    (9, None, ["'Please sit down. Do not worry, we will check the tag right now.' Reassuring a worried guest starts naturally with ", (None, 'Не волнуйтесь,'), " — literally 'do not agitate yourself like waves'."]),
    (10, None, ["'A small paper card is hanging on the side handle.' Objects attached to a bag or wall 'hang' in Russian: ", (None, 'висит'), " gives a clear visual picture rather than flat 'is'."]),
    (11, None, ["'Oh, let us bring the suitcase downstairs to the light!' Inviting everyone to act together begins with ", (None, 'давайте'), " — the everyday Russian way to say 'let us'."]),
]
