# Authoring module for kukhnya-s01e01-scene-12.
ID = 'kukhnya-s01e01-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 12
TITLE = 'Спасительный литр воды  (A Lifesaving Liter of Water)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "Slumping onto a stool at the Claude Monet bar, Max attempts to recover from a sleepless night of drinking at the nightclub. Bartender Kostya immediately detects the painful signs of a hangover and pours a lifesaving jug of cold water for the young newcomer. Let's listen to their conversation in Russian first."
OPENER = "Let's replay a few lines to examine key phrases and grammar."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Kostya slides a large carafe of water across the bar. Next time you watch the episode, listen for the Russian expressions for 'appetite' and 'pale' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('kostya', 'Бухал вчера?', 'Been drinking yesterday?', [(75, 'Бухал вчера')], ''),
    ('max', 'Заметно?', 'Is it noticeable?', [(76, 'Заметно')], ''),
    ('kostya', 'Лицо бледное, руки немного дрожат.', 'Your face is pale, your hands are shaking a bit.', [], ''),
    ('max', 'Да, ночь была очень бурной.', 'Yes, the night was very wild.', [], ''),
    ('kostya', 'Приятного аппетита.', 'Enjoy your meal.', [(77, 'Приятного аппетита')], ''),
    ('max', 'Кому ты сейчас это сказал?', 'Who did you just say that to?', [], ''),
    ('kostya', 'Гостю за соседним столиком.', 'To a guest at the next table.', [], ''),
    ('kostya', 'Что-нибудь желаете?', 'Would you like anything?', [(78, 'Что-нибудь желаете')], ''),
    ('max', 'Воды.', 'Water.', [(78, 'Воды')], ''),
    ('kostya', 'С газом или без газа?', 'Sparkling or still?', [(79, 'без газа')], ''),
    ('max', 'Литр! Без всякого газа!', 'A liter! Without any gas at all!', [(79, 'Литр')], ''),
    ('kostya', 'Всё, я уже несу.', 'Right away, I am already bringing it.', [(80, 'я несу')], ''),
    ('max', 'Спасибо, друг, ты спасаешь мне жизнь.', 'Thank you, my friend, you are saving my life.', [], ''),
]
WALK = [
    (0, None, "'Been drinking yesterday?' Kostya asks casually, using the colloquial verb for drinking alcohol."),
    (1, None, "'Is it noticeable?' Max replies ruefully, realizing his rough night shows on his face."),
    (2, None, "'Would you like anything?' Kostya asks politely, switching into professional hospitality mode behind the bar."),
    (3, None, "'Water.' Max croaks, as he is in need of cold water before his interview."),
    (4, None, "'A liter! Without any gas at all!' Max exclaims, emphasizing the urgent quantity of cold still water he requires. Now listen to the full bar dialogue once more."),
]
