# Authoring module for kukhnya-s01e20-scene-17.
ID = 'kukhnya-s01e20-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 17
TITLE = 'Уход с праздника  (Leaving the Party)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = "The restaurant's party is in full swing, but Nastya has had enough and is heading for the door. Kostya catches up with her, because he has something to say. We'll hear it in Russian first."
OPENER = "Let's replay it step by step."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Nastya agrees to listen, and Kostya takes a deep breath. 'Pozhaluysta' can mean 'please' or 'you're welcome', but here it means 'please'. See you next time!"
CLOSING = ('kostya', 'До свидания!')
STORY = [
    ('kostya', 'Настя, подожди!', 'Nastya, wait!', [], ''),
    ('nastya', 'Пока.', 'Bye.', [(288, 'Пока')], ''),
    ('kostya', 'О, уже уходишь?', 'Oh, you are leaving already?', [(289, 'О, уже уходишь')], ''),
    ('nastya', 'Ага. Как-то здесь невесело.', 'Yeah. It is kind of a downer here.', [(290, 'Ага. Как-то здесь невесело')], ''),
    ('kostya', 'Не уходи так быстро.', 'Do not leave so fast.', [], ''),
    ('nastya', 'У меня много дел.', 'I have a lot of things to do.', [], ''),
    ('kostya', 'Я хочу поговорить с тобой.', 'I want to talk to you.', [], ''),
    ('nastya', 'О чем ты хочешь поговорить?', 'What do you want to talk about?', [], ''),
    ('kostya', 'Это очень важно.', 'This is very important.', [], ''),
    ('nastya', 'Говори быстрее.', 'Speak faster.', [], ''),
    ('kostya', 'Подойди поближе.', 'Come closer.', [], ''),
    ('nastya', 'Я слушаю.', 'I am listening.', [], ''),
    ('kostya', 'Я не могу молчать.', 'I cannot stay silent.', [(291, 'Я')], ''),
    ('kostya', 'Пожалуйста, выслушай меня.', 'Please, hear me out.', [], ''),
]
WALK = [
    (0, None, "'Nastya, wait!' The command is the casual one. Kostya calls out her name first."),
    (1, None, "'Bye.' The word 'poka' is the casual goodbye, which Nastya says without looking back."),
    (2, None, "'Oh, are you leaving already?' The word for 'leave' is the ongoing kind, for going away, and 'already' is a small word."),
    (3, None, "'Yeah. It's a bit of a downer here.' The word 'aga' is a casual 'yeah'. The word for 'dull' is made by putting 'ne' in front of 'cheerful'."),
    (4, None, "'Don't leave so fast.' The word for a negative command uses the ongoing kind, and 'so fast' is two small words."),
    (5, None, "'I've got a lot to do.' The word for 'matters' loses its ending after 'many', and 'at me' stands for 'I have'."),
    (6, None, "'I want to talk to you.' The word for 'with you' is the irregular 'toboy', and the word for 'I want' is irregular too."),
    (7, None, "'What do you want to talk about?' The words for 'about what' sound like one. The word for 'you want' ends in 'sh'."),
    (8, None, "'It's very important.' 'Important' ends in 'o', without a subject. 'Very' is placed in front."),
    (9, None, "'Speak faster.' The word for 'faster' is made from 'quickly' with 'ee', and the word for 'speak' is the casual command."),
    (10, None, "'Come a bit closer.' The 'po' prefix makes 'closer' into 'a bit closer'. 'Come up' has a prefix too."),
    (11, None, "'I'm listening.' The word for 'I listen' is a single word, and it ends in 'yu'."),
    (12, None, "'I can't keep quiet.' The word for 'I can't' is irregular, and 'keep quiet' is the plain form."),
    (13, None, "'Please hear me out.' 'Hear out' has the prefix 'vy', meaning 'to the end'. 'Please' is the longer word."),
]
