# Authoring module for dvorik-u-mosta-s02e06-scene-03.
ID = 'dvorik-u-mosta-s02e06-scene-03'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 6
SCENE = 3
TITLE = 'Всё-таки двадцать четыре стула  (Twenty-Four Chairs After All)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'yaroslav': 'Ярослав', 'roman': 'Роман'}
INTRO = 'At a quarter to six under the warm courtyard lanterns, Kira and Roman are setting out teacups when Yaroslav rushes back from the open street gate, wide-eyed. Listen first.'
OPENER = "Now let's greet the early guests at the gate, one line at a time."
TRANSITION = "Now listen to the whole rush of early guests again without stopping."
OUTRO = "Every single one of Yaroslav's twenty-four bargain chairs fills with smiling neighbours under the courtyard lanterns! See you next time."
CLOSING = ('yaroslav', 'Всего доброго!')
STORY = [
    ('yaroslav', 'Кира! Роман! Идите посмотрите на тротуар у наших ворот!', 'Kira! Roman! Come and look at the pavement by our gate!'),
    ('kira', 'Ещё только без четверти шесть — люди уже идут?!', 'It is only a quarter to six, are people coming already?!'),
    ('yaroslav', 'Хозяин книжного магазина, девушка из аптеки, брат пекаря и двенадцать соседей!', "The bookshop owner, the girl from the pharmacy, the baker's brother and twelve neighbours!"),
    ('roman', 'Все двенадцать стульев в девятом номере заняли за три минуты!', 'All twelve chairs in room nine were taken in three minutes!'),
    ('kira', 'Подождите, а двенадцать складных стульев под аркой во дворе?!', 'Wait, what about the twelve folding chairs under the arch in the courtyard?!'),
    ('yaroslav', 'Те, что я по ошибке заказал в субботу?!', 'The ones I ordered by mistake on Saturday?!'),
    ('roman', 'Раскладываем все двенадцать вокруг четырёх столов во дворе, прямо сейчас!', "Let's unfold all twelve around the four tables in the courtyard, right now!"),
    ('kira', 'На каждом из ваших двадцати четырёх стульев сидит гость, Ярослав Ильич!', 'A guest is sitting on every one of your twenty-four chairs, Yaroslav Ilyich!'),
    ('yaroslav', 'Вы слышали, Кира?! Моя ошибка была гениальным планом!', 'Did you hear that, Kira?! My mistake was a brilliant plan!'),
    ('kira', 'Поклонитесь, Ярослав Ильич, и раздайте меню с улыбкой!', 'Take a bow, Yaroslav Ilyich, and hand out the menus with a smile!'),
    ('roman', 'Откройте окна пошире, чтобы все под деревом слышали пианино!', 'Open the windows wider so that everyone under the tree hears the piano!'),
    ('yaroslav', 'Добро пожаловать, друзья! Горячий мятный чай уже несут!', 'Welcome, friends! Hot mint tea is on its way!'),
]
WALK = [
    (0, None, ["'Kira! Roman! Come and look at the pavement by our gate!' Yaroslav glues two commands together with no 'and': ", (None, 'Идите посмотрите'), " is 'go look', very natural in speech."]),
    (1, None, ["'It is only a quarter to six, are people coming already?!' Russians count back from the hour: ", (None, 'без четверти шесть'), " is literally 'six without a quarter'."]),
    (2, None, ["'The bookshop owner, the girl from the pharmacy, the baker's brother and twelve neighbours!' Someone who works somewhere comes 'from' it: ", (None, 'девушка из аптеки,'), " is 'the girl from the pharmacy'."]),
    (3, None, ["'All twelve chairs in room nine were taken in three minutes!' Roman uses ", (None, 'заняли'), " with no subject, 'they took', which Russian uses where English says 'were taken'."]),
    (4, None, ["'Wait, what about the twelve folding chairs under the arch in the courtyard?!' Something that folds is ", (None, 'складных'), ", the same family as folding up a letter or a map."]),
    (5, None, ["'The ones I ordered by mistake on Saturday?!' Keep ", (None, 'по ошибке'), " for any accident: it means 'by mistake'."]),
    (6, None, ["'Let's unfold all twelve around the four tables in the courtyard, right now!' Laying things out in a circle is ", (None, 'вокруг'), ", the word for 'around'."]),
    (7, None, ["'A guest is sitting on every one of your twenty-four chairs, Yaroslav Ilyich!' Kira says ", (None, 'На каждом из'), ", 'on each of', a handy start for 'every one of them'."]),
    (8, None, ["'Did you hear that, Kira?! My mistake was a brilliant plan!' A clever idea is ", (None, 'гениальным планом!'), " close to English 'genius' and 'plan'."]),
    (9, None, ["'Take a bow, Yaroslav Ilyich, and hand out the menus with a smile!' Handing something to everyone is ", (None, 'раздайте'), ", 'give' with a front part meaning 'out, in all directions'."]),
    (10, None, ["'Open the windows wider so that everyone under the tree hears the piano!' Add the front part to ", (None, 'пошире,'), " and 'wide' becomes 'a bit wider'."]),
    (11, None, ["'Welcome, friends! Hot mint tea is on its way!' Greet any guest with ", (None, 'Добро пожаловать,'), " Russian for 'welcome', literally 'kindly come in'."]),
]
