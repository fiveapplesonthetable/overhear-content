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
CLOSING = ('max', 'Пока!')
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
    (0, None, '\'Vika says that you started a fight.\' "Ustroil", set up, is how Russians say you started a fight. "Draka", fight, becomes "draku" as the thing set up.'),
    (1, None, '\'We were simply fooling around in the backyard.\' "Durachilis\'", fooled around, comes from "durak", a fool. "Na zadnem dvore" is "on the back yard".'),
    (2, None, '\'Show me the video of this fight of yours.\' "Pokazhite", show, has the formal "-te". "Etoy vashey draki" puts the same "of" ending on all three words.'),
    (3, None, '\'Is that really a fight? You did not even fight back!\' "Razve" opens a doubtful "really?". "Dralsya", fought, ends in "-sya", and "dazhe" is "even".'),
    (4, None, '\'So there is no reason to fire the cook yet.\' "Ne za chto" is "not for what", here meaning "no reason". "Poka", yet, is the same word as "bye".'),
    (5, None, '\'Dmitry, thank you for the fair decision.\' "Spasibo za" is "thanks for". "Spravedlivoye", fair, and "resheniye", decision, both end in -oye and -iye to match.'),
    (6, None, '\'Listen to me everyone: forget about this video!\' "Slushayte" and "zabud\'te" are commands to the whole room. "Ob etom", about this, uses "ob" before a vowel.'),
    (7, None, '\'Vika still has to work here as art director.\' There\'s no "has to" verb in it. Russian puts Vika in the "to" form, "Vike", adds a plain infinitive, "rabotat\'", and the job title ends in -om, the ending for working "as" something.'),
    (8, None, '\'Whoever dares laugh will immediately get out!\' "Posmeyet", dares, sounds like "smeyat\'sya", to laugh, but it comes from "smet\'", to dare. "Poydyot von" is "will go out".'),
    (9, None, '\'Every coin has two sides.\' Russian says "medal\'", medal, where English says "coin". "Dve", two, is feminine to match "storony", sides.'),
    (10, None, '\'One day everything around can change drastically.\' Russian packs "one day" into a single word, "odnazhdy". And "drastically" here is the same word as "sharply", as in a sharp turn.'),
    (11, None, '\'A former enemy unexpectedly becomes your friend.\' "Byvshiy", former, grows from "byl", was. "Stanovitsya", becomes, puts the next word in its "as" shape: "tvoim drugom".'),
    (12, None, '\'And a strict tyrant becomes a little bit kinder.\' "Dobreye", kinder, ends in "-eye", the same "more" ending as "bystreye", faster. "Nemnogo" is "a little".'),
    (13, None, '\'Life goes on, and tomorrow is a new day!\' "Prodolzhayetsya", goes on, ends in "-sya", as if life keeps itself going. "Zavtra" is "tomorrow".'),
]
