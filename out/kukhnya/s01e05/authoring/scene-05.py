# Authoring module for kukhnya-s01e05-scene-05.
ID = 'kukhnya-s01e05-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 5
TITLE = 'Кулинарный спор  (A Culinary Bet)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Back in the kitchen at Claude Monet, Max is late for work again, and Chef Barinov is waiting for him. Before the morning is over, the cook Fedya will pick a fight with him about who is the better cook. It comes first in Russian, and you can leave the odd word behind.'
OPENER = "Now slowly, from the chef's greeting. Notice how rarely anyone in this kitchen says anything nice."
TRANSITION = 'And now without interruptions.'
OUTRO = "A bet is easy to start in Russian: one word for 'let's bet', and you're in. The rest is a promise to win. See you next time."
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Доброе утро, шеф!', 'Good morning, Chef!', [(69, 'Доброе утро, шеф')], ''),
    ('barinov', 'Огузок, ты постоянно опаздываешь на работу.', 'Runt, you are constantly late for work.', [(69, 'Агузик'), (70, 'Ты постоянно'), (71, 'ты опять опоздал')], ''),
    ('max', 'Шеф, мне не выдали форму вовремя.', 'Chef, they did not issue my uniform on time.', [(72, 'мне'), (72, 'форму не выдало')], ''),
    ('barinov', 'Хватит оправданий, быстро иди работать!', 'Enough excuses, quickly go to work!', [(68, 'За работу')], ''),
    ('fedya', 'Ты так же плохо шутишь, как и готовишь.', 'You joke as badly as you cook.', [(78, 'Ты так же'), (78, 'шутишь, как и готовишь')], ''),
    ('max', 'Я не понял твоей шутки, Федя.', "I didn't understand your joke, Fedya.", [(79, 'Не понял')], ''),
    ('fedya', 'Это обычное состояние для твоего мозга.', 'This is a normal state for your brain.', [(79, 'привычное состояние для твоего мозга')], ''),
    ('max', 'Ты хочешь сказать, что я плохо готовлю?', 'Do you want to say that I cook badly?', [(80, 'он сказал, что я'), (82, 'ты хочешь сказать')], ''),
    ('fedya', 'Да, именно это я и говорю.', 'Yes, that is exactly what I say.', [], ''),
    ('max', 'А ты думаешь, ты готовишь лучше меня?', 'And do you think you cook better than me?', [(82, 'ты лучше готовишь')], ''),
    ('fedya', 'Уж точно намного лучше тебя!', 'Certainly much better than you!', [(83, 'уж не хуже')], ''),
    ('max', 'Тогда давай устроим кулинарный спор!', "Then let's make a culinary bet!", [(84, 'Спорим')], ''),
    ('fedya', 'Спорим, огузок! Я легко тебя выиграю!', 'Wanna bet, runt! I will easily beat you!', [(84, 'Спорим')], ''),
    ('max', 'Посмотрим, кто из нас лучший повар!', 'We will see which of us is the best cook!', [], ''),
]
WALK = [
    (0, None, "'Good morning, Chef!' Literally the greeting is 'kind morning', and the 'kind' takes the same ending as the morning does. 'chef' is borrowed from French, and in this kitchen it works as 'boss'."),
    (1, None, "'Runt, you are constantly late for work.' The chef's nickname for Max is back. The verb for 'be late' is in the present, which in Russian can mean 'you keep being late'."),
    (2, None, "'Chef, they did not issue my uniform on time.' Max says 'to me they didn't issue', with no one named, which is the standard way to blame nobody. The phrase for 'on time' is written as a single word."),
    (3, None, "'Enough excuses, quickly go to work!' The line opens with 'enough', and the thing you've had enough of comes after it. The last two words are 'go' and 'work', with no 'to' between them, which is how Russian says 'go and work'."),
    (4, None, "'You joke as badly as you cook.' The two halves are built to match: 'as badly' and then 'as you cook'. The verb for 'cook' is also the one for 'prepare', so Fedya uses it for any food."),
    (5, None, "'I didn't understand your joke, Fedya.' It's the polite way of saying 'I didn't get it'. 'Joke' changes its ending after 'your', because the joke is the thing that wasn't understood."),
    (6, None, "'This is a normal state for your brain.' 'normal' is closer to 'usual' or 'ordinary'. It is a good insult because it sounds almost calm."),
    (7, None, "'Do you want to say that I cook badly?' Russian builds it as 'you want to say' with no 'to' needed. The little word for 'that' is the same as 'what'."),
    (8, None, "'Yes, that is exactly what I say.' 'exactly' comes before 'this', and the 'and' in front of the verb adds weight. In English you'd stress 'that's exactly what I am saying'."),
    (9, None, "'And do you think you cook better than me?' Russian says 'better of me', putting 'me' in a different form instead of using a word for 'than'. That is the usual way to compare two people."),
    (10, None, "'Certainly much better than you!' It's the same comparison, with 'you' in the same changed form. 'much' is stuck on the front of 'better' to make 'far better'."),
    (11, None, "'Then let's make a culinary bet!' 'let's' is literally 'give', and it's how Russians propose something. The thing they propose is 'a dispute', and the same word also means 'bet' in this context."),
    (12, None, "'Wanna bet, runt! I will easily beat you!' Fedya's first word stems from 'dispute' from the line before. 'easily' comes from 'light', as in light weight."),
    (13, None, "'We will see which of us is the best cook!' The first word is the 'we'll see' you use when you want the last word. 'Of us' is a nice chunk: 'which of us' becomes 'who from us'."),
]
