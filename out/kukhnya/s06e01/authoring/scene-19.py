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
    (0, None, "'Come on, I do not even know such illnesses.' Telling the doctor to come on he does not even know such illnesses moves the conversation forward without extra drama."),
    (1, None, '\'Your body is very weak.\' Admitting that Barinov\'s body is very weak shows the doctor being honest for a change. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (2, None, "'And your heart is weak.' Saying that Barinov's heart is weak is how the doctor sets the tone with Barinov."),
    (3, None, "'A stroke does not pass without consequences.' Once a stroke does not pass without consequences, the doctor can finally tell Barinov what he means."),
    (4, None, "'And hallucinations do not appear out of nowhere.' Adding that hallucinations do not appear out of nowhere fills in the missing piece for Barinov."),
    (5, None, '\'And how much time do I have left?\' Asking whether how much time do he has left puts the doctor right on the defensive. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (6, None, "'Maybe five years, or maybe a year.' With the doctor and restaurant in play, the doctor keeps this short reply brisk and direct."),
    (7, None, "'You need to quit your job.' Mentioning that Barinov needs to quit Barinov's job moves the talk in a new direction. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (8, None, '\'Quit completely?\' With the conversation and doctor hanging in the air, Barinov puts the doctor on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (9, None, "'Cook calmly at home in your own kitchen.' Telling Barinov to cook calmly at home in Barinov's own kitchen is how the doctor lays out the situation for Barinov."),
    (10, None, "'But no stresses at work.' Over the doctor and the test, the doctor answers Barinov without a second thought."),
    (11, None, '\'I heard you.\' Barinov mentions that he heard the doctor so the doctor sees what is at stake. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
]
