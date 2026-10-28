# Authoring module for kukhnya-s01e20-scene-16.
ID = 'kukhnya-s01e20-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 16
TITLE = 'Старые часы  (Old Watch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'old_man': 'Старик'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = 'Outside the restaurant, Max has met an old man on the street. He has decided to give away the watch he inherited from his grandfather, and the old man cannot quite believe it. Here it is in Russian.'
OPENER = "We'll go through it again, this time with the meaning."
TRANSITION = "Let's finish by hearing it all again."
OUTRO = "Max walks away lighter, and the old man now has a watch and a story. 'Proshchay' is the Russian for 'farewell', and it is the same word as 'forgive'. See you next time!"
CLOSING = ('max', 'До свидания!')
STORY = [
    ('max', 'Привет, старик.', 'Hello, old man.', [], ''),
    ('old_man', 'Здравствуй.', 'Hello.', [], ''),
    ('max', 'У меня есть часы.', 'I have a watch.', [], ''),
    ('old_man', 'Зачем они мне?', 'Why do I need them?', [], ''),
    ('max', 'Они мне больше не нужны.', 'I do not need them anymore.', [], ''),
    ('old_man', 'Они дорогие?', 'Are they expensive?', [], ''),
    ('max', 'Это старые дедовские часы.', "This is an old grandfather's watch.", [], ''),
    ('max', 'На, держись, старик.', 'Here, take it, old man.', [(286, 'На, держись, старик')], ''),
    ('old_man', 'Спасибо тебе большое.', 'Thank you very much.', [], ''),
    ('max', 'Тебе нужнее.', 'You need it more than I do.', [(287, 'Тебе нужнее')], ''),
    ('old_man', 'Я продам их и куплю еды.', 'I will sell it and buy food.', [], ''),
    ('max', 'Делай с ними что хочешь.', 'Do with them what you want.', [], ''),
    ('max', 'Прощай.', 'Goodbye.', [], ''),
    ('old_man', 'Ты очень добрый человек.', 'You are a very kind person.', [], ''),
]
WALK = [
    (0, None, "'Hello, old man.' 'Old man' is built from 'old'. 'Hello' is the casual 'privet'."),
    (1, None, "'Hello.' The old man replies with the singular, casual form of the long hello. It loses the 'te' at the end."),
    (2, None, "'I have a watch.' 'At me there is' stands for 'I have'. 'Watch' is plural in Russian."),
    (3, None, "'Why would I want them?' 'What for' asks about purpose. 'They' is plural because 'watch' is."),
    (4, None, "'I don't need them any more.' 'Needed' is plural. 'More not' means 'no longer'."),
    (5, None, "'Are they expensive?' 'Expensive' is plural, ending in 'ie'. The question lives in the voice."),
    (6, None, "'It's my grandfather's old watch.' 'Grandfather's' is made from 'granddad' with an ending. 'Old' is plural."),
    (7, None, "'Here, take it, old man.' 'Na' is a one-syllable word for 'here, take it'. 'Hold on' is a command with 'sya'."),
    (8, None, "'Thank you very much.' 'Thanks' is neuter, so 'big' finishes with 'oe'. 'To you' sits between them."),
    (9, None, "'You need them more than I do.' 'More needed' is one word, made with 'ee'. 'To you' sits in front."),
    (10, None, "'I'll sell them and buy food.' Both verbs are future, finished actions. 'Food' takes the 'of' form."),
    (11, None, "'Do what you like with them.' 'With them' picks up an 'n', so 'nimi'. 'Do' is the friendly command."),
    (12, None, "'Goodbye.' This word is the final goodbye, from the same family as 'forgive'. It means you may not meet again."),
    (13, None, "'You're a very kind person.' 'Kind' is the word from 'good day'. There's no 'are'."),
]
