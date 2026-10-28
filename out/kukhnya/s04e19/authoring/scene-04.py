ID = 'kukhnya-s04e19-scene-04'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 19
SCENE = 4
TITLE = "Странный сон Дениса  (Denis's Strange Dream)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "kostya": "anja", "katya": "angelina"}
LABELS = {"kostya": "Костя", "katya": "Катя"}
SOURCE_NAME = 'Кухня (Kukhnya) S4.19'
SOURCE_FILE = 'sources/kukhnya/s04/e19.ru.srt'

INTRO = "In the middle of the night, Denis bolts upright in bed after having a bizarre nightmare about his own hands. Meanwhile, early the next morning, Nastya tries to wake a sleepy Kostya so he can drive their baby son to her parents' house. Let's listen to both bedroom scenes in Russian."

STORY = [
    ('kostya', 'Катя, посмотри на мои руки.', 'Katya, look at my hands.', [(48, 'Катя'), (48, 'посмотри на мои руки')], 'adapted'),
    ('kostya', 'Скажи, с ними всё хорошо?', 'Tell me, is everything all right with them?', [(48, 'с ними все хорошо')], 'adapted'),
    ('katya', 'Господи, их две у тебя.', 'Good grief, you have two of them.', [(49, 'Господи, их две у тебя')], ''),
    ('katya', 'Ложись обратно и спи давай.', 'Lie back down and go to sleep.', [(50, 'Спи давай')], 'adapted'),
    ('kostya', 'Мне просто приснился странный сон.', 'I just had a strange dream.', [], 'new'),
    ('katya', 'Утром всё расскажешь, спокойной ночи.', 'You will tell me everything in the morning, good night.', [], 'new'),
    ('katya', 'Костя, уже шесть часов, пора вставать.', "Kostya, it is six o'clock already, time to get up.", [(51, 'Костя, Костя'), (51, 'пора вставать')], 'adapted'),
    ('katya', 'Надо Стёпу к родителям отвезти.', "We need to take Styopa to my parents' place.", [(52, 'Надо Степу к родителям отвезти')], 'adapted'),
    ('kostya', 'Настя, может, он сам доедет?', 'Nastya, maybe he can get there by himself?', [(53, 'Настя, может он сам')], 'adapted'),
    ('kostya', 'Я ему всё подробно объясню.', 'I will explain everything to him in detail.', [(53, 'а я ему объясню')], 'adapted'),
    ('kostya', 'Там же совсем не сложно.', 'It is not complicated at all.', [(53, 'там не сложно же')], 'adapted'),
    ('kostya', 'Ладно, не злись, я уже встаю.', 'All right, do not be angry, I am getting up already.', [(54, 'Я встаю')], 'adapted'),
]

OPENER = "Now let's examine Denis's midnight scare and Kostya's early wake-up call line by line."

WALK = [
    (0, None, "'Katya, look at my hands.' Denis pairs 'look' with 'hands' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (1, None, "'Tell me, is everything all right with them?' In spoken Russian, the words stay in their normal statement order and Denis's rising voice at the end turns the line into a question."),
    (2, None, "'Good grief, you have two of them.' Russians say 'by me' or 'with us' where English says 'I have' or 'we have', without needing a separate word for 'have'."),
    (3, None, "'Lie back down and go to sleep.' Two singular imperatives urge Denis to lie back down and go back to sleep."),
    (4, None, "'I just had a strange dream.' Denis pairs 'simply, just' with 'dream' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (5, None, "'You will tell me everything in the morning, good night.' Notice how Russian puts 'in the morning' and 'night' together in a short, direct phrase where word endings show how the ideas connect."),
    (6, None, "'Kostya, it is six o'clock already, time to get up.' Here Katya anchors the thought on 'already' and finishes on 'to get up', keeping the spoken rhythm brisk and natural."),
    (7, None, "'We need to take Styopa to my parents' place.' In everyday Russian, 'need to, must' flows straight into 'to drive, to take' without extra linking words."),
    (8, None, "'Nastya, maybe he can get there by himself?' Half-asleep, Kostya jokes that their infant son can take himself to his grandparents' house."),
    (9, None, "'I will explain everything to him in detail.' Notice how Russian puts 'in detail' and 'will explain' together in a short, direct phrase where word endings show how the ideas connect."),
    (10, None, "'It is not complicated at all.' Here Kostya anchors the thought on 'at all' and finishes on 'difficultly, hard, complicated', keeping the spoken rhythm brisk and natural."),
    (11, None, "'All right, do not be angry, I am getting up already.' Seeing Nastya's glare, Kostya quickly uses a first-person singular present verb meaning getting up."),
]

TRANSITION = "Let's hear the night and morning bedroom exchanges again from start to finish."
OUTRO = 'Katya reassures Denis that he still has two normal hands, while reluctant Kostya finally drags himself out of bed. Listen for the plural noun meaning hands and the verbs meaning sleep and get up. See you next time!'
CLOSING = ("kostya", "До встречи!")
