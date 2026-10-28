# Authoring module for kukhnya-s01e17-scene-23.
ID = 'kukhnya-s01e17-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 23
TITLE = 'Тайна паспорта  (The Secret of the Passport)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "The toast is interrupted. Barinov asks Max to show him his passport, and the date of birth in it is not what Max has been telling everyone. Here's the Russian, start to finish."
OPENER = "We'll go through it again, this time with the meaning."
TRANSITION = "Let's finish by hearing it all again."
OUTRO = "Max has been caught out, and everyone has something to say about it. As you listen again, notice that months are not capitalised in Russian, and that 'v fevrale' means 'in February'. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Покажи мне свой паспорт, Макс.', 'Show me your passport, Max.', [(327, 'Паспорте!')], ''),
    ('max', 'Вот мой паспорт, шеф.', 'Here is my passport, chef.', [(327, 'Паспорте!')], ''),
    ('barinov', 'А почему день рождения в феврале?', 'And why is the birthday in February?', [(327, 'А что это тебе день рождения в феврале, а?')], ''),
    ('senya', 'Твой день рождения не сегодня?', 'Your birthday is not today?', [(327, 'день рождения в феврале')], ''),
    ('max', 'Я хотел сделать вам приятное.', 'I wanted to please you.', [(329, 'чтобы сделать тебе приятное')], ''),
    ('barinov', 'Ты соврал нам про праздник?', 'Did you lie to us about the holiday?', [(330, 'немножко соврать')], ''),
    ('max', 'Я хотел забыть все обиды.', 'I wanted to forget all grudges.', [(328, 'забыть свои обиды')], ''),
    ('senya', 'Но врать друзьям нельзя.', 'But one must not lie to friends.', [(330, 'соврать')], ''),
    ('barinov', 'Любая ложь — это плохо.', 'Any lie is bad.', [(331, 'за любое вранье')], ''),
    ('max', 'Я очень виноват перед вами.', 'I am very guilty before you.', [(331, 'приходится платить')], ''),
    ('barinov', 'За любой обман надо отвечать.', 'For any deceit one must answer.', [(331, 'за любое вранье рано или поздно приходится платить.')], ''),
    ('senya', 'Правда всегда открывается.', 'The truth always reveals itself.', [(331, 'Правда')], ''),
    ('max', 'За любой обман приходится платить.', 'For any deceit one has to pay.', [(331, 'за любое вранье рано или поздно приходится платить.')], ''),
]
WALK = [
    (0, None, "'Show me your passport, Max.' The command is casual. 'Your own' is a special word that always points back to the person asked."),
    (1, None, "'Here's my passport, Chef.' 'Here' points at it. 'My' is masculine to match 'passport'."),
    (2, None, "'And why is your birthday in February?' Months start with a small letter in Russian, and this one takes an 'e' after 'in'. 'Birthday' is 'day of birth'."),
    (3, None, "'Isn't your birthday today?' The 'not' goes right before 'today', so only that word is denied. It sounds suspicious, which it should."),
    (4, None, "'I wanted to do something nice for you.' 'Nice' is used as a noun, so it means 'something nice'. 'Do to you' is the usual pattern."),
    (5, None, "'Did you lie to us about the holiday?' 'Lied' is the kind that means a small lie. 'About' is a tiny word."),
    (6, None, "'I wanted to forget all the grudges.' 'Grudges' is plural. 'Forget' is an action seen as complete."),
    (7, None, "'But you mustn't lie to friends.' The 'not allowed' word is followed by the plain 'to lie'. 'To friends' has a plural ending."),
    (8, None, "'Any lie is bad.' 'Any' is a single word. The dash stands in for 'is'."),
    (9, None, "'I'm very much in the wrong before you.' 'Guilty' is a short form with a masculine ending. 'Before you' picks up an 'ami' ending."),
    (10, None, "'You have to answer for any deceit.' 'Answer' is the word you use for being responsible. 'For' brings the next word into its object form."),
    (11, None, "'The truth always comes out.' 'Comes out' means 'opens itself', with a 'sya' ending. It's a neat way to say that truths emerge."),
    (12, None, "'You end up paying for any deception.' 'It comes to paying' is the structure. 'Any' is the same as before."),
]
