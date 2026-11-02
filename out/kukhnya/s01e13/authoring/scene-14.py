# Authoring module for kukhnya-s01e13-scene-14.
ID = 'kukhnya-s01e13-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 14
TITLE = 'Честный разговор  (An Honest Conversation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Kostya has come to Nastya's flat expecting a romantic evening. Nastya, though, has something honest to say. Hear how she says it in Russian first."
OPENER = 'Back through it slowly.'
TRANSITION = 'Here is the whole conversation again.'
OUTRO = "Kostya takes it well, and the two of them settle for a calm night. Notice how Nastya says she is grateful. Keep that in mind for the next time someone helps you. Until next time."
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('nastya', 'Костя, подожди секунду, не спеши.', 'Kostya, wait a second, do not rush.', [], ''),
    ('kostya', 'Настя, что случилось, почему ты грустная?', 'Nastya, what happened, why are you sad?', [(192, 'Что')], ''),
    ('nastya', 'Сегодня у нас ничего не получится.', 'Nothing will work out between us today.', [(193, 'сегодня')], ''),
    ('kostya', 'Давай выпьем ещё немного сока!', 'Let us drink a little more juice!', [], ''),
    ('nastya', 'Нет, Костя, дело совсем не в этом.', 'No, Kostya, that is not the point.', [(195, 'Нет.')], ''),
    ('nastya', 'Я не хочу поступать не по любви.', 'I do not want to act without love.', [], ''),
    ('nastya', 'Я просто очень благодарна за твою помощь.', 'I am simply very grateful for your help.', [], ''),
    ('kostya', 'Ты думаешь, что ты обязана мне?', 'Do you think that you owe me?', [], ''),
    ('nastya', 'Да, я чувствую себя нечестным человеком.', 'Yes, I feel like a dishonest person.', [], ''),
    ('nastya', 'Давай сегодня просто спокойно поспим.', 'Let us just sleep quietly tonight.', [(196, 'Сегодня')], ''),
    ('kostya', 'Хорошо, давай сегодня просто поспим.', 'All right, let us just sleep tonight.', [], ''),
    ('nastya', 'Костя, ты правда понимаешь мои чувства?', 'Kostya, do you really understand my feelings?', [], ''),
    ('kostya', 'Да, Настя, всё совершенно нормально.', 'Yes, Nastya, everything is completely fine.', [], ''),
]
WALK = [
    (0, None, ["'Kostya, wait a second, do not rush.' These are two orders to a friend, ", ('nastya', 'подожди'), ' and ', ('nastya', 'не'), ('nastya', 'спеши'), '. Notice ', ('nastya', 'секунду'), " takes a different ending to mean 'for a second'."]),
    (1, None, ["'Nastya, what happened, why are you sad?' The verb ", ('kostya', 'случилось'), " has a neuter ending because 'what' counts as neuter. Notice ", ('kostya', 'грустная'), " has a woman's ending because Nastya is a woman."]),
    (2, None, ["'Nothing will work out between us today.' Russian says 'at us nothing will turn out', ", ('nastya', 'у'), ('nastya', 'нас'), ('nastya', 'ничего'), ('nastya', 'не'), ('nastya', 'получится'), ", not 'between us'. The 'not' after 'nothing' is required."]),
    (3, None, ["'Let us drink a little more juice!' The verb ", ('kostya', 'выпьем'), " means 'drink up'. The word ", ('kostya', 'сока'), " has an ending because it is 'some juice'."]),
    (4, None, ["'No, Kostya, that is not the point.' Let us consider the sentence: ", ('nastya', 'дело'), ('nastya', 'совсем'), ('nastya', 'не'), ('nastya', 'в'), ('nastya', 'этом'), " is the usual Russian chunk for 'that is not the point'."]),
    (5, None, ["'I do not want to act without love.' Two 'not' words sit in the sentence, one for ", ('nastya', 'не'), ('nastya', 'хочу'), ' and one for ', ('nastya', 'не'), ('nastya', 'по'), ('nastya', 'любви'), ', and they do not cancel each other. Russian marks the love with ', ('nastya', 'по'), ('nastya', 'любви'), ", 'out of love'."]),
    (6, None, ["'I am simply very grateful for your help.' We can focus on this part: ", ('nastya', 'благодарна'), " is 'grateful', in a woman's form. It is built from good, and to give. Also, ", ('nastya', 'за'), " is 'for'."]),
    (7, None, ["'Do you think that you owe me?' The term ", ('kostya', 'обязана'), " is a woman's 'obliged'. After ", ('kostya', 'думаешь'), ' comes ', ('kostya', 'что'), ', and the comma in front of it is mandatory in Russian.']),
    (8, None, ["'Yes, I feel like a dishonest person.' Let's break down this line: ", ('nastya', 'чувствую'), ('nastya', 'себя'), " means 'I feel myself'. The term ", ('nastya', 'нечестным'), " is made by adding 'not' to the front, which is how Russians make opposites."]),
    (9, None, ["'Let us just sleep quietly tonight.' The verb ", ('nastya', 'поспим'), ' is a short sleep. Notice ', ('nastya', 'спокойно'), ', calmly, sits just in front of it.']),
    (10, None, ["'All right, let us just sleep tonight.' Kostya repeats her words, minus 'calmly'. The term ", ('kostya', 'давай'), " with a 'we' verb is the same 'let us' form as before."]),
    (11, None, ["'Kostya, do you really understand my feelings?' Now we can break down the dialogue: ", ('nastya', 'чувства'), " means 'feelings' and belongs to the family of 'I feel'. Notice ", ('nastya', 'правда'), " means 'truth', but here it means 'really'."]),
    (12, None, ["'Yes, Nastya, everything is completely fine.' Let us consider the sentence: ", ('kostya', 'нормально'), " is the English 'normal' with a Russian adverb ending. Notice ", ('kostya', 'совершенно'), ", completely, is the word Max used in the car for 'absolutely right'."]),
]
