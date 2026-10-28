# Authoring module for kukhnya-s01e07-scene-15.
ID = 'kukhnya-s01e07-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 15
TITLE = 'Правда отменяется  (The Truth Is Canceled)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = "The lying is over, and Max has cooked a dish for Barinov's judgement. For once the chef likes it, and Max can't resist a joke about his smile. It's in Russian first."
OPENER = 'Slowly now. Notice how Barinov swings from praise to a shout in the space of a line.'
TRANSITION = 'Now the story in one go.'
OUTRO = "'Thank you very much, chef' is a good last line. After all the shouting, it's the sentence that ends the scene. See you next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Шеф, попробуйте, пожалуйста, это горячее блюдо.', 'Chef, please taste this hot dish.', [], ''),
    ('barinov', 'Давай сюда тарелку, я сейчас попробую.', 'Give the plate here, I will taste it now.', [], ''),
    ('barinov', 'Очень вкусно, можно подавать гостям.', 'Very tasty, we can serve it to the guests.', [(313, 'Очень вкусно. Можно подавать')], ''),
    ('max', 'Неужели вы говорите мне чистую правду?', 'Are you really telling me the pure truth?', [(312, 'Правда')], ''),
    ('barinov', 'Да, блюдо получилось действительно великолепным.', 'Yes, the dish turned out truly magnificent.', [], ''),
    ('max', 'Шеф, вы сейчас так радостно улыбаетесь!', 'Chef, you are smiling so joyfully now!', [(314, 'Не улыбайтесь так')], ''),
    ('barinov', 'А что, повар уже не может улыбнуться?', 'Why, can a cook no longer smile?', [], ''),
    ('max', 'Не улыбайтесь так, вы похожи на клоуна.', 'Do not smile like that, you look like a clown.', [(314, 'вы похожи на бесеного класса')], ''),
    ('barinov', 'Замолчи сейчас же, наглый огузок!', 'Be quiet right now, insolent rump!', [(315, 'Заткнись')], ''),
    ('barinov', 'С этого момента вся правда отменяется!', 'From this moment on, all truth is canceled!', [(316, 'с этого момента правда отменяется')], ''),
    ('max', 'Я вас понял, возвращаемся к работе.', 'I understood you, we return to work.', [], ''),
    ('barinov', 'И ещё одно важное слово, Максим.', 'And one more important word, Maxim.', [(317, 'И еще')], ''),
    ('barinov', 'Спасибо за отличную работу на кухне.', 'Thank you for the excellent work in the kitchen.', [(318, 'Спасибо')], ''),
    ('max', 'Спасибо вам большое, шеф!', 'Thank you very much, chef!', [], ''),
]
WALK = [
    (0, None, "'Chef, please taste this hot dish.' The expression for 'taste' is the polite command, so Max is using the proper form for a boss. 'Hot' ends in 'oe' to match 'dish', which is a neuter word."),
    (1, None, "'Give the plate here, I will taste it now.' The Russian word for 'give' is a casual command, and Barinov uses it as 'hand it over'. 'here' is the 'to here' kind, since the plate has to move."),
    (2, None, "'Very tasty, we can serve it to the guests.' The Russian for 'it's allowed' is one short word that covers 'we can' and 'we may'. 'To the guests' puts an 'am' ending on 'guests'."),
    (3, None, "'Are you really telling me the pure truth?' The line begins with the surprised 'really'. 'Pure truth' is how Russians say 'honest truth'."),
    (4, None, "'Yes, the dish turned out truly magnificent.' 'Turned out' ends in 'o', since 'dish' is neuter. 'Magnificent' ends in 'ym'."),
    (5, None, "'Chef, you are smiling so joyfully now!' 'Joyfully' starts from 'joy'. 'Smile' ends in 'sya'."),
    (6, None, "'Why, can a cook no longer smile?' The term for 'why' here is a sarcastic 'what, then?'. The expression for 'smile' is the one-time kind, so it means 'give a smile' rather than 'be smiling'."),
    (7, None, "'Do not smile like that, you look like a clown.' 'Similar to' is the Russian for 'look like'. 'Clown' takes an 'a' ending, since it's the thing resembled."),
    (8, None, "'Be quiet right now, insolent rump!' 'Fall silent' starts with a prefix that means 'begin to'. 'Right now' is made of 'now' and 'already'."),
    (9, None, "'From this moment on, all truth is canceled!' The Russian for 'is canceled' ends in 'sya', so it means 'cancels itself'. 'From this moment' is a nice formal phrase that you can use for any announcement."),
    (10, None, "'I understood you, we return to work.' 'I understood you' uses the polite 'you'. 'To work' is 'to' plus a changed word."),
    (11, None, "'And one more important word, Maxim.' Barinov uses Max's full name here to sound serious. 'One more' is made of 'still' and 'one', and the Russian for 'word' sits at the end."),
    (12, None, "'Thank you for the excellent work in the kitchen.' 'Thank you for' takes the thing in the plain object form. 'Excellent' is a word for top marks."),
    (13, None, "'Thank you very much, chef!' The expression for 'you' is added after 'thank you' to make it more personal. 'big' is the usual way of saying 'very much'."),
]
