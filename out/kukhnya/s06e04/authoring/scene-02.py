ID = 'kukhnya-s06e04-scene-02'
SHOW = "kukhnya"
SEASON = 6
EPISODE = 4
SCENE = 2
TITLE = 'Старый друг из Парижа  (An Old Friend from Paris)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'guest': 'anja', 'eleonora': 'angelina'}
LABELS = {'anya': 'Катя', 'guest': 'Гость', 'eleonora': 'Элеонора'}
SOURCE_NAME = "Кухня (Kukhnya) S6.04"
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'

INTRO = 'At the reception desk, Katya is surprised by her old French classmate Olivier from the Paris culinary academy—and when Barinov and Eleonora hear the words Paris and culinary academy, they jump to conclusions.'

STORY = [
    ('guest', 'Мне показалось, что вы мне подмигнули.', 'It seemed to me that you winked at me.', [(14, 'мне показалось, что вы мне подмигнули')], 'exact'),
    ('anya', 'Нет, вам показалось.', 'No, you imagined it.', [(15, 'Нет, вам показалось')], 'exact'),
    ('anya', 'Столько лет прошло, а ты все пользуешься этим!', 'So many years have passed, and you still use that line!', [(17, 'Столько лет прошло, а ты все пользуешься этим')], 'adapted'),
    ('guest', 'Катя, сколько мы не виделись?', 'Katya, how long has it been since we saw each other?', [(18, 'Катя, сколько мы не виделись?')], 'exact'),
    ('anya', 'Мы не виделись с тех пор, как меня отчислили.', 'We have not seen each other since they expelled me.', [(20, 'с тех пор, как меня отчислили')], 'adapted'),
    ('anya', 'А ты что здесь делаешь?', 'And what are you doing here?', [(21, 'А ты что здесь делаешь?')], 'exact'),
    ('guest', 'Это небольшой бизнес, а ты как?', 'It is a small business trip, and how about you?', [(21, 'Это небольшой бизнес'), (22, 'А ты как?')], 'adapted'),
    ('anya', 'Я отлично работаю здесь в ресторане.', 'I am doing great working here in the restaurant.', [(22, 'Я отлично работаю здесь в ресторане')], 'exact'),
    ('guest', 'Ты помнишь нашего старого профессора?', 'Do you remember our old professor?', [(24, 'Ты помнишь профессора')], 'adapted'),
    ('guest', 'Когда он заснул на занятии, я проучился на месяц больше, чем ты.', 'When he fell asleep in class, I studied a month longer than you.', [(25, 'заснул на занятии'), (27, 'я проучился на месяц больше, чем ты')], 'adapted'),
    ('eleonora', 'А кто это такой, Катя?', 'And who is that, Katya?', [(34, 'А кто это?')], 'adapted'),
    ('anya', 'Это Оливье, мы с ним учились в Париже в кулинарной академии.', 'That is Olivier, he and I studied together in Paris at the culinary academy.', [(34, 'Это Оливье'), (35, 'Мы с ним учились в Париже, в кулинарной академии')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'It seemed to me that you winked at me.' The plural past ending '-li' on the verb for 'winked' covers a group or the polite 'you'."),
    (1, None, "'No, you imagined it.' Here the Russian phrasing highlights 'no' before landing on 'seemed'."),
    (2, None, "'So many years have passed, and you still use that line!' Notice the reflexive suffix on the verb meaning 'use', turning the action back on the subject."),
    (3, None, "'Katya, how long has it been since we saw each other?' Notice the reflexive suffix on the verb meaning 'saw each other', turning the action back on the subject."),
    (4, None, "'We have not seen each other since they expelled me.' Notice how Russian expresses 'we' and 'expelled' with crisp inflection rather than helper words."),
    (5, None, "'And what are you doing here?' Here the Russian phrasing highlights 'and' before landing on 'are doing'."),
    (6, None, "'It is a small business trip, and how about you?' Notice how Russian expresses 'this' and 'how' with crisp inflection rather than helper words."),
    (7, None, "'I am doing great working here in the restaurant.' Spoken Russian keeps this brisk, leaning on 'I' and finishing on 'restaurant'. the guest answers right away."),
    (8, None, "'Do you remember our old professor?' Notice how Russian expresses 'you' and 'professor' with crisp inflection rather than helper words."),
    (9, None, "'When he fell asleep in class, I studied a month longer than you.' The meaning hinges on 'when' working together with 'you' in spoken Russian."),
    (10, None, "'And who is that, Katya?' Notice how Russian expresses 'and' and 'Katya' with crisp inflection rather than helper words. Katya answers right away."),
    (11, None, "'That is Olivier, he and I studied together in Paris at the culinary academy.' Here the Russian phrasing highlights 'this' before landing on 'academy'."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Hearing that Olivier is a French chef on a mysterious business trip, Barinov and Eleonora exchange a knowing look. See you in the next scene.'
CLOSING = ('eleonora', 'Париж, кулинарная академия?')
