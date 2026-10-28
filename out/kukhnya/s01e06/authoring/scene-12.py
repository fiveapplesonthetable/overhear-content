# Authoring module for kukhnya-s01e06-scene-12.
ID = 'kukhnya-s01e06-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 12
TITLE = 'Строгая проверка  (A Strict Inspection)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Inside the kitchen the inspector is looking at everything: the floor, the grill, a bottle that should not be open. Barinov follows him, trying to keep up a front. It's in Russian first."
OPENER = 'Slowly now. The inspector gives short, formal remarks, and Barinov is full of excuses.'
TRANSITION = 'And the whole inspection once more.'
OUTRO = "Barinov's favourite word here is 'personally', and the inspector's is 'violation'. Between them they've given you a handful of official words and a few good reactions. See you next time."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('inspector', 'Скользкий пол — это источник опасности.', 'A slippery floor is a source of danger.', [(160, 'Скользкий пол — это источник опасности для сотрудников')], ''),
    ('barinov', 'Мы сейчас же вытрем эту воду.', 'We will wipe up this water immediately.', [], ''),
    ('inspector', 'Почему у гриля открыта эта бутылка?', 'Why is this bottle open by the grill?', [(161, 'Почему у гриля открыта бутылка с алкоголем')], ''),
    ('barinov', 'Это вино нужно для мясного соуса.', 'This wine is needed for meat sauce.', [], ''),
    ('inspector', 'Понятно, но это всё равно нарушение.', 'Understood, but that is still a violation.', [(162, 'Понятно')], ''),
    ('barinov', 'Я лично уберу бутылку в шкаф.', 'I will personally put the bottle in the cupboard.', [], ''),
    ('inspector', 'Простым штрафом вы здесь не отделаетесь!', "You won't get off with a simple fine here!", [(163, 'простым штрафом вы здесь не отделаетесь')], ''),
    ('barinov', 'Поверьте, у нас образцовый ресторан!', 'Believe me, we have an exemplary restaurant!', [], ''),
    ('inspector', 'Пойдёмте дальше, я осмотрю склад.', "Let's move on, I will inspect the storage.", [(164, 'Пойдемте дальше')], ''),
    ('barinov', 'Прошу вас, идите прямо за мной.', 'Please, walk right behind me.', [], ''),
    ('inspector', 'А что находится за этой дверью?', 'And what is located behind this door?', [(165, 'А тут что')], ''),
    ('barinov', 'Там наш склад для закрытых бутылок.', 'There is our storage for unopened bottles.', [(166, 'Склад алкоголя')], ''),
    ('inspector', 'Откройте замок, я должен всё увидеть.', 'Open the lock, I must see everything.', [], ''),
]
WALK = [
    (0, None, "'A slippery floor is a source of danger.' The dash stands in for 'is'. 'Source' also means 'spring', as in water, and 'danger' is built from 'dangerous'."),
    (1, None, "'We will wipe up this water immediately.' 'Right now' has a tiny extra word that makes it 'this very minute'. 'We will wipe' ends in 'em', the 'we' ending."),
    (2, None, "'Why is this bottle open by the grill?' 'Open' ends in 'a' to agree with 'bottle'. 'By the grill' is the short 'at' word plus a changed ending."),
    (3, None, "'This wine is needed for meat sauce.' 'Wine' is neuter, so 'needed' ends in 'o'. 'Of meat' becomes a describing word, giving 'meaty sauce'."),
    (4, None, "'Understood, but that is still a violation.' 'Understood' is a handy one-word answer. 'Still' is literally 'all equal', which here means 'regardless'."),
    (5, None, "'I will personally put the bottle in the cupboard.' 'Put away' begins with the little piece 'u' that gives the sense of 'out of sight'. 'Into the cupboard' has no ending change on the cupboard."),
    (6, None, "'You won't get off with a simple fine here!' The long word at the end is the Russian for 'get off lightly'. It ends in 'sya', and the fine takes a 'with' ending."),
    (7, None, "'Believe me, we have an exemplary restaurant!' 'Believe' is the polite command. 'Exemplary' comes from 'a sample' or 'a model'."),
    (8, None, "'Let's move on, I will inspect the storage.' 'Let's go' has a polite 'te' on the end, which turns it into an invitation. 'Inspect' begins with a piece that means 'around'."),
    (9, None, "'Please, walk right behind me.' 'I ask you' is the formal way to say 'please'. 'Behind me' is 'behind' plus a changed form of 'me'."),
    (10, None, "'And what is located behind this door?' 'Is located' comes from 'to find', so it's literally 'finds itself'. 'Behind this door' uses the same 'behind' as before."),
    (11, None, "'There is our storage for unopened bottles.' 'Closed' is the opposite of 'open', and Barinov uses it for 'sealed'. 'Of bottles' has a changed ending."),
    (12, None, "'Open the lock, I must see everything.' 'lock' also means 'castle', and only the stress tells them apart. 'I must' is the man's form."),
]
