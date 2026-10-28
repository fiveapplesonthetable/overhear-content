# Authoring module for kukhnya-s04e19-scene-04.
ID = 'kukhnya-s04e19-scene-04'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 19
SCENE = 4
TITLE = "Странный сон Дениса  (Denis's Strange Dream)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'katya': 'Катя', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.19'
SOURCE_FILE = 'sources/kukhnya/s04/e19.ru.srt'
INTRO = "In the middle of the night, Denis bolts upright in bed after having a bizarre nightmare about his own hands. Meanwhile, early the next morning, Nastya tries to wake a sleepy Kostya so he can drive their baby son to her parents' house. Let's listen to both bedroom scenes in Russian."
OPENER = "Now let's examine Denis's midnight scare and Kostya's early wake-up call line by line."
TRANSITION = "Let's hear the night and morning bedroom exchanges again from start to finish."
OUTRO = 'Katya reassures Denis that he still has two normal hands, while reluctant Kostya finally drags himself out of bed. Listen for the plural noun meaning hands and the verbs meaning sleep and get up. See you next time!'
CLOSING = ('denis', 'До встречи!')
STORY = [
    ('denis', 'Катя, посмотри на мои руки.', 'Katya, look at my hands.', [(48, 'Катя'), (48, 'посмотри на мои руки')], 'adapted'),
    ('denis', 'Скажи, с ними всё хорошо?', 'Tell me, is everything all right with them?', [(48, 'с ними все хорошо')], 'adapted'),
    ('katya', 'Господи, их две у тебя.', 'Good grief, you have two of them.', [(49, 'Господи, их две у тебя')], ''),
    ('katya', 'Ложись обратно и спи давай.', 'Lie back down and go to sleep.', [(50, 'Спи давай')], 'adapted'),
    ('denis', 'Мне просто приснился странный сон.', 'I just had a strange dream.', [], 'new'),
    ('katya', 'Утром всё расскажешь, спокойной ночи.', 'You will tell me everything in the morning, good night.', [], 'new'),
    ('katya', 'Костя, уже шесть часов, пора вставать.', "Kostya, it is six o'clock already, time to get up.", [(51, 'Костя, Костя'), (51, 'пора вставать')], 'adapted'),
    ('katya', 'Надо Стёпу к родителям отвезти.', "We need to take Styopa to my parents' place.", [(52, 'Надо Степу к родителям отвезти')], 'adapted'),
    ('kostya', 'Настя, может, он сам доедет?', 'Nastya, maybe he can get there by himself?', [(53, 'Настя, может он сам')], 'adapted'),
    ('kostya', 'Я ему всё подробно объясню.', 'I will explain everything to him in detail.', [(53, 'а я ему объясню')], 'adapted'),
    ('kostya', 'Там же совсем не сложно.', 'It is not complicated at all.', [(53, 'там не сложно же')], 'adapted'),
    ('kostya', 'Ладно, не злись, я уже встаю.', 'All right, do not be angry, I am getting up already.', [(54, 'Я встаю')], 'adapted'),
]
WALK = [
    (0, None, "'Katya, look at my hands.' Once at his hands, Denis can finally tell Katya what he means."),
    (1, None, '\'Tell me, is everything all right with them?\' Asking whether tell him is everything all right with them puts Katya right on the defensive. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, '\'Good grief, you have two of them.\' Katya tells Denis that good grief Denis has two of them without dressing it up. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (3, None, "'Lie back down and go to sleep.' By telling Denis to lie back down and go to sleep, Katya keeps her side of the story grounded."),
    (4, None, "'I just had a strange dream.' Mentioning that he just had a strange dream moves the talk in a new direction."),
    (5, None, "'You will tell me everything in the morning, good night.' Saying that Denis will tell her everything in the morning good night is how Katya sets the tone with Denis."),
    (6, None, "'Kostya, it is six o'clock already, time to get up.' Because it is six o'clock already time to get up, Katya treats the matter as settled."),
    (7, None, '\'We need to take Styopa to my parents\' Needing to take Styopa to her parents is how Katya lays out the situation for Denis. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (8, None, '\'Nastya, maybe he can get there by himself?\' Wondering if maybe he can get there by himself shows Kostya caught off guard. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (9, None, "'I will explain everything to him in detail.' Claiming that he will explain everything to him in detail sounds confident, even if Denis has doubts."),
    (10, None, "'It is not complicated at all.' Explaining that it is not complicated at all lays the cards on the table for Denis."),
    (11, None, "'All right, do not be angry, I am getting up already.' Kostya explains that all right do not be angry he is getting up already, keeping his voice calm and direct."),
]
