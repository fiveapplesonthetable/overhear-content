# Authoring module for kukhnya-s01e05-scene-04.
ID = 'kukhnya-s01e05-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 4
TITLE = 'Неловкое расставание  (An Awkward Breakup)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Max meets waitress Nastya in the vegetable storeroom to clear up a huge misunderstanding. Nastya thinks they are on a romantic date and talking about their future, while Max frantically tries to explain they were never together. Listen to their comical conversation in Russian first, and then we will examine every line.'
OPENER = "Let's examine this hilarious breakup conversation step by step."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'That concludes our fourth scene. In Kukhnya, clarifying relationship boundaries in the vegetable storeroom never goes quite as planned. See you next time!'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Настя, что ты сейчас делаешь?', 'Nastya, what are you doing now?', [(50, 'Что ты делаешь')], ''),
    ('nastya', 'Ну, у нас же настоящее свидание!', 'Well, we are on a real date!', [(50, 'Ну, у нас же свидание')], ''),
    ('max', 'Нет, Настя, у нас не свидание.', 'No, Nastya, we are not on a date.', [(51, 'Нет, Настя, у нас не свидание')], ''),
    ('max', 'Ты вчера всё не так поняла.', 'You understood everything wrong yesterday.', [(52, 'Ты вчера все не так поняла')], ''),
    ('max', 'Мы с тобой совсем не встречаемся.', 'You and I are not dating at all.', [(53, 'Мы с тобой не встречаемся')], ''),
    ('max', 'Я не твой парень.', 'I am not your boyfriend.', [(53, 'Я не твой парень')], ''),
    ('max', 'А ты не моя девушка.', 'And you are not my girlfriend.', [(53, 'а ты не моя девушка')], ''),
    ('nastya', 'Ты что, меня сейчас бросаешь?', 'Are you dumping me right now?', [(54, 'Ты что, меня бросаешь')], ''),
    ('max', 'Это вовсе не глупые шутки.', 'These are not silly jokes at all.', [(55, 'шуточки'), (56, 'Это не шутки, Настя')], ''),
    ('max', 'Между нами никогда ничего не было.', 'Nothing ever happened between us.', [(58, 'Между нами ничего не было')], ''),
    ('nastya', 'А как же наш поцелуй?', 'And what about our kiss?', [(60, 'А поцелуй')], ''),
    ('nastya', 'А наши будущие дети?', 'And what about our future children?', [(61, 'А наши дети')], ''),
    ('max', 'Какие ещё дети, Настя?', 'What children, Nastya?', [(62, 'Какие дети')], ''),
    ('max', 'Да, если хочешь, я тебя бросаю!', 'Yes, if you want, I am dumping you!', [(63, 'да, я тебя бросаю')], ''),
]
WALK = [
    (0, None, "'Nastya, what are you doing now?' Max cautiously approaches to figure out what is happening."),
    (1, None, "'Well, we are on a real date!' Nastya assumes they are on an official romantic outing."),
    (2, None, "'No, Nastya, we are not on a date.' Max explicitly denies that this is a romantic occasion."),
    (3, None, "'You understood everything wrong yesterday.' Max tells her she completely misinterpreted yesterday's events."),
    (4, None, "'You and I are not dating at all.' Max firmly clarifies their actual relationship status."),
    (5, None, "'I am not your boyfriend.' Max delivers a blunt reality check about his role."),
    (6, None, "'And you are not my girlfriend.' Max finishes shutting down the fantasy completely."),
    (7, None, "'Are you dumping me right now?' Nastya is shocked and feels like she is being dumped."),
    (8, None, "'These are not silly jokes at all.' Max insists he is being completely serious."),
    (9, None, "'Nothing ever happened between us.' Max reminds her that they were never actually together."),
    (10, None, "'And what about our kiss?' Nastya desperately brings up their intimate moment."),
    (11, None, "'And what about our future children?' Nastya dramatically jumps far ahead into her imagined future."),
    (12, None, "'What children, Nastya?' Max is completely flabbergasted by her wild assumption."),
    (13, None, "'Yes, if you want, I am dumping you!' Max gives up trying to reason and just accepts the breakup narrative."),
]
