# Authoring module for kukhnya-s01e20-scene-08.
ID = 'kukhnya-s01e20-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 8
TITLE = 'Утренний сюрприз  (A Morning Surprise)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = "Kostya wakes up in a good mood and greets Nastya affectionately. She is not in the same mood at all, and it takes him a while to find out why. We'll hear it in Russian first."
OPENER = "Let's take it a line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Kostya tries to be charming and only makes things worse. Notice that 'moya dorogaya' means 'my dear', and that it's the feminine form of 'dear' used as a noun. See you next time!"
CLOSING = ('kostya', 'До свидания!')
STORY = [
    ('kostya', 'Доброе утро, моя дорогая.', 'Good morning, my dear.', [(141, 'проснулся и хочешь поиграть со мной?')], ''),
    ('nastya', 'Это не доброе утро.', 'It is not a good morning.', [], ''),
    ('kostya', 'Почему ты так на меня смотришь?', 'Why are you looking at me like that?', [], ''),
    ('nastya', 'Я ждала, когда ты проснешься.', 'I have been waiting for you to wake up.', [], ''),
    ('kostya', 'Ты уже проснулась? Хочешь кофе?', 'Are you awake already? Do you want coffee?', [], ''),
    ('nastya', 'Нет, Костя.', 'No, Kostya.', [], ''),
    ('kostya', 'А...', 'Ah...', [], ''),
    ('kostya', 'Я сделал что-то не так?', 'Did I do something wrong?', [], ''),
    ('nastya', 'Ты забыл, что мы обсуждали.', 'You forgot what we discussed.', [], ''),
    ('kostya', 'Я всё помню.', 'I remember everything.', [], ''),
    ('nastya', 'Тогда почему ты шутишь?', 'Then why are you joking?', [], ''),
    ('kostya', 'Я просто пытаюсь быть милым.', 'I am just trying to be nice.', [], ''),
]
WALK = [
    (0, None, "'Good morning, my dear.' 'Dear' is feminine, ending in 'aya', and is used as a noun. 'Morning' is neuter, so 'good' ends in 'oe'."),
    (1, None, "'It's not a good morning.' The 'not' sits in front of the whole phrase. There's no 'is'."),
    (2, None, "'Why are you looking at me like that?' 'Like that' is a small word. 'Look at' needs the little word 'on', followed by 'menya'."),
    (3, None, "'I was waiting for you to wake up.' Russian says 'waiting when you will wake up'. 'Wake up' ends in 'sya'."),
    (4, None, "'Are you awake already? Do you want coffee?' 'Woke up' ends in 'las', for a woman. 'You want' ends in 'sh'."),
    (5, None, "'No, Kostya.' Two words, and the name needs no change. The tone is flat."),
    (6, None, "'Ah...' A single sound that says he is about to be caught out. The dots show his uncertainty."),
    (7, None, "'Did I do something wrong?' 'Something not so' is the phrase for 'something wrong'. 'Did' is the finished kind."),
    (8, None, "'You forgot what we discussed.' 'Forgot' ends in 'l' for a man. 'We discussed' is the ongoing past, in the plural."),
    (9, None, "'I remember everything.' 'Everything' goes first, and 'I remember' follows. The word order puts the weight on 'everything'."),
    (10, None, "'Then why are you joking?' 'Joke' is made from 'a joke'. 'Then' is a small word at the front."),
    (11, None, "'I'm just trying to be nice.' 'Nice' takes an 'ym' ending after 'to be'. 'Try' ends in 'sya'."),
]
