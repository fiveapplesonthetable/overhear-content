ID = "kukhnya-s04e04-scene-05"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 4
SCENE = 5
TITLE = 'Дудка из морковки  (The Carrot Flute)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'german': 'anja', 'lyova': 'angelina'}
LABELS = {'anya': 'Денис', 'german': 'Герман', 'lyova': 'Лёва'}
SOURCE_NAME = "Кухня (Kukhnya) S4.04"
SOURCE_FILE = 'sources/kukhnya/s04/e04.ru.srt'

INTRO = 'In the storage room of Claude Monet, German Mikhailovich hears music and finds Denis playing a handmade flute carved out of a carrot, leading to an immediate disciplinary task. Listen to their exchange in Russian.'

STORY = [
    ('german', 'Простите, пожалуйста, что такое?', 'Excuse me, please, what is this?', [(67, 'Простите, пожалуйста, что такое?')], ''),
    ('german', 'Поразительно. Это вы сами сделали? Из морковки?', 'Astonishing. Did you make this yourself? Out of a carrot?', [(68, 'Поразительно. Это вы сами сделали?'), (69, 'Из морковки?')], ''),
    ('anya', 'Да. Спасибо.', 'Yes. Thank you.', [(69, 'Да.'), (71, 'Спасибо.')], ''),
    ('german', 'Всю морковку почистили, ещё дудку сделали. Молодец.', 'You peeled all the carrots and even made a flute. Well done.', [(74, 'Всю морковку почистили, еще'), (74, 'сделали.'), (75, 'Молодец.')], ''),
    ('german', 'Вам не составит большого труда почистить мешок картошки.', 'It will not be much trouble for you to peel a sack of potatoes.', [(76, 'вам...'), (77, 'не составит большого труда почистить мешок картошки.')], ''),
    ('german', 'Вам лучше два. Два мешка. До вечера справитесь?', 'Better make it two for you. Two sacks. Will you manage by evening?', [(79, 'Вам лучше два.'), (80, 'Два мешка. До вечера справитесь?')], ''),
    ('anya', 'Шеф, я до вечера не успею.', "Chef, I won't finish in time by evening.", [(81, 'Шеф, я до вечера не успею.')], ''),
    ('german', 'Успеете. Вы очень талантливы.', 'You will finish in time. You are very talented.', [(81, 'Успеете.'), (82, 'Вы очень талантливы.')], ''),
    ('german', 'А не успеете — пойдёте вон.', "And if you don't finish in time, out you go.", [(83, 'А не успеете,'), (83, 'вон.')], ''),
    ('lyova', 'Герман Михайлович, а для чего нам нужно столько картошки?', 'German Mikhailovich, why do we need so many potatoes?', [(85, 'Герман Михайлович, а для чего нам нужно столько картошки?')], ''),
    ('german', 'В целях воспитания. Тунеядства я не потерплю.', 'For educational purposes. I will not tolerate slacking.', [(87, 'В целях воспитания.'), (88, 'я не потерплю.')], ''),
    ('lyova', 'Мне тоже не нравится.', 'I do not like this either.', [(89, 'Мне тоже не нравится.')], ''),
]

OPENER = "Let's break this conversation down line by line."

WALK = [
    (0, None, "'Excuse me, please, what is this?' German keeps the sentence short and direct, relying on Russian case endings to show how the words connect."),
    (1, None, "'Astonishing. Did you make this yourself? Out of a carrot?' German uses the polite plural form of address to maintain a respectful or ironic distance."),
    (2, None, "'Yes. Thank you.' In spoken Russian, Denis omits unnecessary linking verbs so the key idea lands immediately."),
    (3, None, "'You peeled all the carrots and even made a flute. Well done.' The past-tense verb ending marks the grammatical gender and number of the subject directly."),
    (4, None, "'It will not be much trouble for you to peel a sack of potatoes.' German keeps the sentence short and direct, relying on Russian case endings to show how the words connect."),
    (5, None, "'Better make it two for you. Two sacks. Will you manage by evening?' German uses the polite plural form of address to maintain a respectful or ironic distance."),
    (6, None, "'Chef, I won't finish in time by evening.' Denis uses the first-person pronoun in the case required by the Russian verb or preposition."),
    (7, None, "'You will finish in time. You are very talented.' German uses the polite plural form of address to maintain a respectful or ironic distance."),
    (8, None, "'And if you don't finish in time, out you go.' German keeps the sentence short and direct, relying on Russian case endings to show how the words connect."),
    (9, None, "'German Mikhailovich, why do we need so many potatoes?' In spoken Russian, Lyova omits unnecessary linking verbs so the key idea lands immediately."),
    (10, None, "'For educational purposes. I will not tolerate slacking.' German places the negative particle directly before the verb or predicate to negate the statement."),
    (11, None, "'I do not like this either.' Lyova uses the first-person pronoun in the case required by the Russian verb or preposition."),
]

TRANSITION = 'Now listen to the full Russian exchange again with everything in place.'

OUTRO = 'That completes German catching Denis with the carrot flute and assigning him two sacks of potatoes. Notice how Russian expresses deadlines with prepositions. See you in the next scene.'
CLOSING = ('anya', 'Шеф, я до вечера не успею.')
CLOSING_TRANS = "Chef, I won't finish in time by evening."
