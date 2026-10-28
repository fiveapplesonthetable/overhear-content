ID = 'kukhnya-s06e04-scene-19'
SHOW = "kukhnya"
SEASON = 6
EPISODE = 4
SCENE = 19
TITLE = 'Обвинение в краже  (Accusation of Theft)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'gulya': 'angelina', 'guest': 'anja'}
LABELS = {'anya': 'Шеф', 'gulya': 'Гуля', 'guest': 'Гость'}
SOURCE_NAME = "Кухня (Kukhnya) S6.04"
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'

INTRO = "After the kitchen brigade visits Barinov in the hospital, Lyova's mother and her friend block Gulya at the apartment door and demand that she open her handbag to prove she did not steal the five thousand rubles."

STORY = [
    ('guest', 'Здравствуйте, шеф, вам лучше уже?', 'Hello, Chef, are you feeling better already?', [(298, 'Здрасте'), (299, 'Ну что, шеф, вам лучше уже?')], 'adapted'),
    ('anya', 'Да, спасибо, ребята, уже лучше.', 'Yes, thank you, guys, already better.', [(299, 'Да, спасибо'), (302, 'Да, ребят, уже лучше')], 'adapted'),
    ('guest', 'А когда мне десять тысяч вернете?', 'And when will you pay me back my ten thousand?', [(300, 'А когда мне'), (300, 'тысяч вернете')], 'adapted'),
    ('anya', 'Пошел вон отсюда, все понял?', 'Get out of here, understood?', [(301, 'Пошел вон. Все понял?')], 'adapted'),
    ('guest', 'А ты куда собралась?', 'And where are you going?', [(303, 'а ты куда')], 'adapted'),
    ('gulya', 'Я к чаю хочу чего-нибудь купить.', 'I want to buy something to go with tea.', [(304, 'Я к чаю хочу чего-нибудь купить')], 'exact'),
    ('guest', 'Ты нам сумочку свою сначала покажи.', 'Show us your handbag first.', [(305, 'Ты нам сумочку свою покажи')], 'adapted'),
    ('gulya', 'Что вы говорите?', 'What are you saying?', [(307, 'Что?')], 'adapted'),
    ('guest', 'Гуля, мы тебя ни в чем не обвиняем.', 'Gulya, we are not accusing you of anything.', [(307, 'мы тебя ни в чем не обвиняем')], 'adapted'),
    ('guest', 'Взяла пять тысяч, думаешь, никто не заметил?', 'You took five thousand, do you think nobody noticed?', [(308, 'пять тысяч, думаешь, никто не заметил?')], 'adapted'),
    ('guest', 'Ну, дай сюда, покажи сумку!', 'Come on, give it here, show the bag!', [(309, 'Ну, дай сюда, покажи сумку')], 'exact'),
    ('gulya', 'Что вы такое делаете, пустите!', 'What are you doing, let go!', [(311, 'Что вы такое делаете?')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Hello, Chef, are you feeling better already?' the guest anchors the line on 'hello', while 'already' completes the thought."),
    (1, None, "'Yes, thank you, guys, already better.' In Russian, the idea of 'yes' flows naturally into 'better' without extra filler words."),
    (2, None, "'And when will you pay me back my ten thousand?' the guest raises the pitch on 'will return' to turn the phrase into a direct spoken question. Chef Barinov answers right away."),
    (3, None, "'Get out of here, understood?' Spoken Russian keeps this brisk, leaning on 'went' and finishing on 'understood'."),
    (4, None, "'And where are you going?' The meaning hinges on 'and' working together with 'to get ready' in spoken Russian."),
    (5, None, "'I want to buy something to go with tea.' Gulya brings out the contrast between 'I' and 'tea' in a few short words. the guest answers right away."),
    (6, None, "'Show us your handbag first.' the guest anchors the line on 'you', while 'show' completes the thought."),
    (7, None, "'What are you saying?' The grammar packs 'what' and 'speak' into a tight, idiomatic kitchen exchange."),
    (8, None, "'Gulya, we are not accusing you of anything.' the guest anchors the line on 'Gulya', while 'accuse' completes the thought."),
    (9, None, "'You took five thousand, do you think nobody noticed?' the guest brings out the contrast between 'picked up' and 'five' in a few short words."),
    (10, None, "'Come on, give it here, show the bag!' The meaning hinges on 'come on' working together with 'bag' in spoken Russian."),
    (11, None, "'What are you doing, let go!' The grammar packs 'what' and 'let' into a tight, idiomatic kitchen exchange."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Right as the two women wrestle for Gulya's purse in the hallway, Lyova opens the front door and freezes at the sight. See you in the next scene."
CLOSING = ('guest', 'Поймали тебя с поличным!')
