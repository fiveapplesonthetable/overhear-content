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
INTRO = "In the Claude Monet kitchen, Chef Viktor Barinov tastes Max's freshly prepared dish and admits it is delicious. Max cheekily remarks on the chef's rare smile, prompting Barinov to declare the day of brutal truth officially over before quietly thanking him. Listen to their conversation in Russian first, then we will break down each line in English."
OPENER = 'Now let us go through each phrase to see how it works in Russian.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "In a rare moment of tenderness, Chef Barinov genuinely compliments Max before returning to kitchen discipline. Until then! Next time you watch the episode, listen for the Russian expressions for 'dish' and 'big' — you will catch every word right away. See you next time!"
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
    (0, None, "'Chef, please taste this hot dish.' Max nervously presents his work. He hopes the boss will actually like it."),
    (1, None, "'Give the plate here, I will taste it now.' Barinov grabs it without hesitation. He is ready to find flaws in the young cook's attempt."),
    (2, None, "'Very tasty, we can serve it to the guests.' Barinov is pleasantly surprised. He gives a straightforward approval, which is incredibly rare for him."),
    (3, None, "'Are you really telling me the pure truth?' Max is shocked by the compliment. He wonders if the chef is just playing a trick on him."),
    (4, None, '\'Yes, the dish turned out truly magnificent.\' Barinov doubles down on the praise. He uses a strong word like "magnificent" to show his genuine appreciation.'),
    (5, None, "'Chef, you are smiling so joyfully now!' Max pushes his luck by pointing out the chef's good mood. He is amazed to see his boss actually look happy."),
    (6, None, "'Why, can a cook no longer smile?' Barinov defensively questions the observation. He tries to act like his smile is perfectly normal."),
    (7, None, "'Do not smile like that, you look like a clown.' Max immediately regrets his cheeky comment. He teases the boss about his unnatural expression."),
    (8, None, "'Be quiet right now, insolent rump!' Barinov instantly reverts to his angry self. He uses his favorite nickname to put Max back in his place."),
    (9, None, "'From this moment on, all truth is canceled!' Barinov officially ends his experiment with brutal honesty. He decides the truth is just too annoying."),
    (10, None, "'I understood you, we return to work.' Max wisely backs down. He gets the message and drops the joke."),
    (11, None, "'And one more important word, Maxim.' Barinov pauses to say something serious. He even uses Max's real name instead of an insult."),
    (12, None, "'Thank you for the excellent work in the kitchen.' Barinov expresses sincere gratitude for the help. It is a rare moment of humility from the proud chef."),
    (13, None, "'Thank you very much, chef!' Max warmly accepts the thanks. He is touched by the master's acknowledgement."),
]
