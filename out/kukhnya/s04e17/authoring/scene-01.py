ID = 'kukhnya-s04e17-scene-01'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 17
SCENE = 1
TITLE = "Новость о беременности  (Pregnancy News)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "eva": "angelina", "chef": "anja"}
LABELS = {"eva": "Ева", "chef": "Шеф"}
SOURCE_NAME = 'Кухня (Kukhnya) S4.17'
SOURCE_FILE = 'sources/kukhnya/s04/e17.ru.srt'

INTRO = "Waitress Eva pulls Chef Viktor Barinov, sous-chef Lyova, and young cook Denis aside one by one at Claude Monet. With a calm, serious expression, she tells each man in secret that she is expecting a baby. Let's listen to their stunned reactions in Russian."

STORY = [
    ('eva', 'Виктор Петрович, вы тоже должны знать.', 'Viktor Petrovich, you should know too.', [(1, 'Виктор Петрович, думаю, вы тоже должны знать')], 'adapted'),
    ('eva', 'Я сейчас жду ребёнка.', 'I am expecting a child right now.', [], 'new'),
    ('eva', 'Я беременна от тебя.', 'I am pregnant by you.', [(5, 'я беременна от тебя')], 'adapted'),
    ('chef', 'Что ты такое говоришь, Ева?', 'What on earth are you saying, Eva?', [], 'new'),
    ('eva', 'Срок пока ещё очень небольшой.', 'It is still very early.', [(3, 'Срок пока небольшой')], 'adapted'),
    ('eva', 'Но скоро всё будет заметно.', 'But soon everything will be noticeable.', [(3, 'но скоро будет заметно')], 'adapted'),
    ('eva', 'Витя, я правда беременна.', 'Vitya, I really am pregnant.', [(4, 'Витя, я беременна')], 'adapted'),
    ('eva', 'Виктор Петрович, у вас всё хорошо?', 'Viktor Petrovich, is everything all right with you?', [(7, 'Виктор Петрович, у вас все в порядке')], 'adapted'),
    ('chef', 'Да, Лёва, всё в порядке.', 'Yes, Lyova, everything is fine.', [(7, 'в порядке'), (8, 'Да')], 'adapted'),
    ('eva', 'А у меня большая проблема.', 'Well, I have a big problem.', [], 'new'),
    ('eva', 'Лёва, я тоже беременна.', 'Lyova, I am pregnant too.', [(10, 'Я беременна')], 'adapted'),
    ('chef', 'Нам нужно срочно всё проверить.', 'We need to check everything urgently.', [], 'new'),
]

OPENER = "Now let's break down Eva's unexpected announcement and the chefs' reactions line by line."

WALK = [
    (0, None, "'Viktor Petrovich, you should know too.' Eva addresses the head chef politely by name and patronymic while using a plural modal adjective of obligation."),
    (1, None, "'I am expecting a child right now.' Here Eva anchors the thought on 'right now' and finishes on 'child', keeping the spoken rhythm brisk and natural."),
    (2, None, "'I am pregnant by you.' Spoken Russian keeps this brief and expressive, built right around 'pregnant' without extra helper words."),
    (3, None, "'What on earth are you saying, Eva?' Chef Barinov reacts with incredulity using an emphatic neuter pronoun alongside a second-person singular verb."),
    (4, None, "'It is still very early.' She reassures him about the timing with temporal particles and a prefixed adjective meaning small."),
    (5, None, "'But soon everything will be noticeable.' Here Eva anchors the thought on 'soon' and finishes on 'noticeable', keeping the spoken rhythm brisk and natural."),
    (6, None, "'Vitya, I really am pregnant.' Switching to his affectionate diminutive name, she reinforces her claim with a conversational truth particle."),
    (7, None, "'Viktor Petrovich, is everything all right with you?' Russians say 'by me' or 'with us' where English says 'I have' or 'we have', without needing a separate word for 'have'."),
    (8, None, "'Yes, Lyova, everything is fine.' Spoken Russian keeps this brief and expressive, built right around 'order' without extra helper words."),
    (9, None, "'Well, I have a big problem.' Lyova contrasts their situations with an adversative conjunction and a feminine singular noun phrase."),
    (10, None, "'Lyova, I am pregnant too.' In Lyova's memory, Eva repeats the exact same short feminine adjective with an additive adverb."),
    (11, None, "'We need to check everything urgently.' Russian expresses feelings and needs by saying 'to me it is needed' or 'to me it seems', putting the person in the 'to me' form."),
]

TRANSITION = "Let's hear the entire conversation from start to finish without interruption."
OUTRO = "Eva's sudden revelation leaves Viktor Petrovich, Lyova, and Denis completely bewildered in the kitchen. Listen for the adjective meaning pregnant and the adverb meaning soon when you watch. Until next time!"
CLOSING = ("eva", "Всего хорошего!")
