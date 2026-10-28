# Authoring module for kukhnya-s01e20-scene-23.
ID = 'kukhnya-s01e20-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 23
TITLE = 'Пробуждение  (Awakening)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = "This is the last scene of the season. Max sums up the morning after, in a few short sentences, and leaves one question hanging. Here's the Russian, start to finish."
OPENER = "Let's go over what we just heard."
TRANSITION = 'Now the whole conversation once more, from start to finish.'
OUTRO = "The season ends with a question and a line about moving on, which seems fitting. 'Idti tol'ko vperyod' means 'to go only forward', and you've now heard it twice. See you next time!"
CLOSING = ('max', 'До свидания!')
STORY = [
    ('max', 'Утро пришло.', 'Morning has come.', [], ''),
    ('max', 'Теперь все ясно.', 'Now everything is clear.', [], ''),
    ('max', 'Но уже поздно.', 'But it is already late.', [], ''),
    ('max', 'Время ушло.', 'Time has gone.', [], ''),
    ('max', 'Это наша общая ошибка.', 'This is our common mistake.', [], ''),
    ('max', 'Может быть, стоило проснуться?', 'Maybe we should have woken up?', [(339, 'Может быть, стоило проснуться')], ''),
    ('max', 'Проснуться раньше?', 'Woken up sooner?', [(339, 'проснуться раньше')], ''),
    ('max', 'Я не знаю ответ.', "I don't know the answer.", [], ''),
    ('max', 'Никто не знает.', 'Nobody knows.', [], ''),
    ('max', 'Жизнь продолжается.', 'Life goes on.', [], ''),
    ('max', 'Нужно идти.', 'Need to go.', [], ''),
    ('max', 'Идти только вперед.', 'Go only forward.', [], ''),
]
WALK = [
    (0, None, "'Morning has come.' 'Morning' is neuter, so 'came' finishes with 'o'. A short, quiet start."),
    (1, None, "'Now everything is clear.' 'Clear' is a word with an 'o' ending, used without a subject. There's no 'is'."),
    (2, None, "'But it's already late.' 'Late' is a word with an 'o' ending. 'But already' are two small words."),
    (3, None, "'Time has gone.' 'Time' is neuter, so 'went away' carries 'o'. A very short sentence."),
    (4, None, "'It's our common mistake.' 'Common' means 'shared'. 'Mistake' is feminine, so both words end in 'aya'."),
    (5, None, "'Maybe we should have woken up?' The word 'stoilo' means 'it was worth'. 'Wake up' finishes with 'sya'."),
    (6, None, "'Woken up sooner?' 'Earlier' is just one word. Max repeats the idea."),
    (7, None, "'I don't know the answer.' 'Answer' is a masculine word with no ending. 'I know' finishes with 'u'."),
    (8, None, "'Nobody knows.' 'Nobody' and 'not' appear together. Two words and a full stop."),
    (9, None, "'Life goes on.' 'Continues' carries 'sya', meaning it continues by itself. 'Life' ends in a soft sign."),
    (10, None, "'We need to go.' 'Necessary' plus the plain 'to go'. It is a short instruction."),
    (11, None, "'Only forward.' 'Only' sits in front of 'forward'. The episode ends on the plain word."),
]
