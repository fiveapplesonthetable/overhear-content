# Authoring module for kukhnya-s06e01-scene-19.
ID = 'kukhnya-s06e01-scene-19'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 19
TITLE = "Диагноз врача  (The Doctor's Diagnosis)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'doctor': 'Врач'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = 'Troubled by his hallucinations of his late mother-in-law, Chef Barinov visits his doctor friend, who examines his test results and delivers a grim warning about his heart.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Ordered to give up professional cooking for the sake of his life, Barinov protests that his lifelong dream is finally within reach. Until next time!'
CLOSING = ('doctor', 'До встречи!')
STORY = [
    ('barinov', 'Ладно тебе, я даже болезней таких не знаю.', 'Come on, I do not even know such illnesses.', [(337, 'Ладно тебе, я даже болезней таких не знаю')], 'exact'),
    ('doctor', 'У тебя очень слабый организм.', 'Your body is very weak.', [(338, 'У тебя крайне истощен организм')], 'adapted'),
    ('doctor', 'И сердце слабое.', 'And your heart is weak.', [(339, 'Сердце слабое')], 'adapted'),
    ('doctor', 'Инсульт даром не проходит.', 'A stroke does not pass without consequences.', [(339, 'Инсульт даром не проходит')], 'exact'),
    ('doctor', 'И галлюцинации просто так не появляются.', 'And hallucinations do not appear out of nowhere.', [(340, 'Да и галлюцинации на пустом месте не появляются')], 'adapted'),
    ('barinov', 'И сколько мне осталось?', 'And how much time do I have left?', [(342, 'Чего?')], 'adapted'),
    ('doctor', 'Может пять лет, а может и год.', 'Maybe five years, or maybe a year.', [(343, 'Нет, может пять, а может и год')], 'adapted'),
    ('doctor', 'Тебе надо бросить работу.', 'You need to quit your job.', [(344, 'Тебе надо бросить работу')], 'exact'),
    ('barinov', 'Бросить совсем?', 'Quit completely?', [(345, 'Совсем?')], 'adapted'),
    ('doctor', 'Готовь спокойно у себя дома на кухне.', 'Cook calmly at home in your own kitchen.', [(346, 'пожалуйста, у себя на кухне')], 'adapted'),
    ('doctor', 'Но никаких стрессов на работе.', 'But no stresses at work.', [(347, 'стрессов')], 'adapted'),
    ('barinov', 'Я тебя услышал.', 'I heard you.', [(345, 'Совсем?')], 'adapted'),
]
WALK = [
    (0, None, '\'Come on, I do not even know such illnesses.\' Discussing the illnesses right here, Barinov lands on "bolezney" ("illnesses, diseases", built on "bolezn") to keep the statement grounded.'),
    (1, None, '\'Your body is very weak.\' Bringing up the organism in the exchange, the doctor uses "u tebya" (literally "by you") where English says "you have" or "your".'),
    (2, None, "'And your heart is weak.' The doctor proceeds firmly without any doubt, watching Barinov's face to see how the news lands."),
    (3, None, '\'A stroke does not pass without consequences.\' Emphasizing a stroke on the spot, the doctor uses "insult" ("stroke") to carry the main weight of the thought.'),
    (4, None, '\'And hallucinations do not appear out of nowhere.\' Pointing to the hallucinations during the talk, the doctor uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (5, None, "'And how much time do I have left?' Barinov wonders eagerly to see how the doctor will answer on the spot."),
    (6, None, "'Maybe five years, or maybe a year.' The doctor continues dryly in this moment, leaving no doubt about where he stands."),
    (7, None, '\'You need to quit your job.\' Talking about the job with Barinov, the doctor leans on "nado" ("it is necessary, one needs to"), which carries the whole predicate in Russian without needing "it is".'),
    (8, None, "'Quit completely?' Barinov presses wryly while looking straight at the doctor here."),
    (9, None, '\'Cook calmly at home in your own kitchen.\' Highlighting the kitchen to Barinov, the doctor centers the thought on "kukhne" ("kitchen", from "kukhnya") without wasting a word.'),
    (10, None, '\'But no stresses at work.\' Pointing to the stresses in the exchange, the doctor reaches for the Russian word "stressov" ("stresses", built from "stress") right at the center of the line.'),
    (11, None, "'I heard you.' Barinov reacts evenly with a smile, steering the talk right where he wants it."),
]
