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
INTRO = "Earlier that morning, in the Claude Monet kitchen, Max turns up late again and Chef Barinov is waiting for him. Then Fedya, another cook, starts needling Max about his cooking, and it ends in a bet. Listen in Russian first; the odd missed word doesn't matter."
OPENER = "Now line by line, from Max's greeting. Notice that nobody in this kitchen says anything nice."
TRANSITION = 'And now the whole morning without stopping.'
OUTRO = "Starting a bet in Russian takes just one word, and an imperative form of 'to give' placed before a verb is how you suggest anything at all. Max and Fedya now have something to prove."
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Доброе утро, шеф!', 'Good morning, Chef!', [(69, 'Доброе утро, шеф')], ""),
    ('barinov', 'Огузок, ты постоянно опаздываешь на работу.', 'Runt, you are constantly late for work.', [(69, 'Агузик'), (70, 'Ты постоянно'), (71, 'ты опять опоздал')], ""),
    ('max', 'Шеф, мне не выдали форму вовремя.', 'Chef, they did not issue my uniform on time.', [(72, 'мне'), (72, 'форму не выдало')], ""),
    ('barinov', 'Хватит оправданий, быстро иди работать!', 'Enough excuses, quickly go to work!', [(68, 'За работу')], ""),
    ('fedya', 'Ты так же плохо шутишь, как и готовишь.', 'You joke as badly as you cook.', [(78, 'Ты так же'), (78, 'шутишь, как и готовишь')], ""),
    ('max', 'Я не понял твоей шутки, Федя.', "I didn't understand your joke, Fedya.", [(79, 'Не понял')], ""),
    ('fedya', 'Это обычное состояние для твоего мозга.', 'This is a normal state for your brain.', [(79, 'привычное состояние для твоего мозга')], ""),
    ('max', 'Ты хочешь сказать, что я плохо готовлю?', 'Do you want to say that I cook badly?', [(80, 'он сказал, что я'), (82, 'ты хочешь сказать')], ""),
    ('fedya', 'Да, именно это я и говорю.', 'Yes, that is exactly what I say.', [], ""),
    ('max', 'А ты думаешь, ты готовишь лучше меня?', 'And do you think you cook better than me?', [(82, 'ты лучше готовишь')], ""),
    ('fedya', 'Уж точно намного лучше тебя!', 'Certainly much better than you!', [(83, 'уж не хуже')], ""),
    ('max', 'Тогда давай устроим кулинарный спор!', "Then let's make a culinary bet!", [(84, 'Спорим')], ""),
    ('fedya', 'Спорим, огузок! Я легко тебя обыграю!', 'Wanna bet, runt! I will easily beat you!', [(84, 'Спорим')], ""),
    ('max', 'Посмотрим, кто из нас лучший повар!', 'We will see which of us is the best cook!', [], ""),
]
WALK = [
    (0, None, [
        "'Good morning, Chef!' Literally 'kind morning'. ",
        ('max', 'Доброе'),
        " ends in -oe to match ",
        ('max', 'утро'),
        ", a noun ending in -o. ",
        ('max', 'шеф'),
        " is borrowed from French, and in this kitchen it simply literally translates to 'boss'."
    ]),
    (1, None, [
        "'Runt, you are constantly late for work.' , Barinov's name for Max, is ",
        ('barinov', 'Огузок'),
        ' really the rump cut of beef. ',
        ('barinov', 'опаздываешь'),
        " is a present-tense verb, and paired with ",
        ('barinov', 'постоянно'),
        ", meaning 'constantly', it describes a habit of being late."
    ]),
    (2, None, [
        "'Chef, they did not issue my uniform on time.' Max says ",
        ('max', 'мне'),
        ('max', 'не'),
        ('max', 'выдали'),
        ", a phrase conveying 'to me they didn't issue', so nobody in particular gets the blame. The adverb ",
        ('max', 'вовремя'),
        ", for 'on time', is written as one word."
    ]),
    (3, None, [
        "'Enough excuses, quickly go to work!' Following ",
        ('barinov', 'Хватит'),
        ", indicating 'enough', the thing you've had enough of takes a genitive ending, as seen in ",
        ('barinov', 'оправданий'),
        ", meaning 'excuses'. The command ",
        ('barinov', 'иди'),
        ('barinov', 'работать'),
        " simply equates to 'go work', placing two verbs side by side."
    ]),
    (4, None, [
        "'You joke as badly as you cook.' The two halves match: ",
        ('fedya', 'так'),
        ('fedya', 'же'),
        ('fedya', 'плохо'),
        " acts as 'just as badly', while ",
        ('fedya', 'как'),
        ('fedya', 'и'),
        " represents 'as also'. The verb ",
        ('fedya', 'готовишь'),
        ", which expresses 'you cook', also carries the sense of 'you prepare'."
    ]),
    (5, None, [
        "'I didn't understand your joke, Fedya.' After ",
        ('max', 'не'),
        ('max', 'понял'),
        ", the negative for 'understood', the joke becomes ",
        ('max', 'шутки'),
        ", and the feminine pronoun for 'your' turns into ",
        ('max', 'твоей'),
        ". Notice that ",
        ('max', 'понял'),
        ", lacking an -a ending, tells you a man is speaking."
    ]),
    (6, None, [
        "'This is a normal state for your brain.' The preposition ",
        ('fedya', 'для'),
        ", expressing 'for', changes the case of what follows it: the base forms for 'your brain' become ",
        ('fedya', 'твоего'),
        ('fedya', 'мозга'),
        ". It's an insult delivered almost calmly."
    ]),
    (7, None, [
        "'Do you want to say that I cook badly?' The phrase ",
        ('max', 'хочешь'),
        ('max', 'сказать'),
        " pairs 'you want' and 'to say', combining two verbs without a linking 'to'. The conjunction ",
        ('max', 'что'),
        " functions here as 'that', though it also serves as the question word for 'what'."
    ]),
    (8, None, [
        "'Yes, that is exactly what I say.' The adverb ",
        ('fedya', 'именно'),
        " carries the weight of 'exactly' or 'precisely'. The small ",
        ('fedya', 'и'),
        " before ",
        ('fedya', 'говорю'),
        " does not act as 'and' here: it just leans on the verb for emphasis."
    ]),
    (9, None, [
        "'And do you think you cook better than me?' There is no direct equivalent for 'than'. Russian shifts 'me' into the form ",
        ('max', 'меня'),
        " and says ",
        ('max', 'лучше'),
        ('max', 'меня'),
        " to convey 'better of me'."
    ]),
    (10, None, [
        "'Certainly much better than you!' The same pattern applies with ",
        ('fedya', 'лучше'),
        ('fedya', 'тебя'),
        ". Adding ",
        ('fedya', 'намного'),
        " in front amplifies it to 'much better', while ",
        ('fedya', 'Уж'),
        ('fedya', 'точно'),
        " provides a cocky sense of 'that's for sure'."
    ]),
    (11, None, [
        "'Then let's make a culinary bet!' The imperative ",
        ('max', 'давай'),
        " originates from the verb for 'to give', and placing it before another verb creates a 'let's' proposal. While ",
        ('max', 'спор'),
        " refers to an argument or dispute, the phrase ",
        ('max', 'кулинарный'),
        ('max', 'спор'),
        " turns it into a cook-off on a bet."
    ]),
    (12, None, [
        "'Wanna bet, runt! I will easily beat you!' Built from the verb for 'to argue', ",
        ('fedya', 'Спорим'),
        ", is how people here challenge someone with 'wanna bet?'. The verb ",
        ('fedya', 'обыграю'),
        " promises 'I'll beat you at it', framing the loser as the direct object, ",
        ('fedya', 'тебя'),
        "."
    ]),
    (13, None, [
        "'We will see which of us is the best cook!' Here is ",
        ('max', 'Посмотрим'),
        " again, the familiar 'we'll see' that Kostya used earlier. The expression ",
        ('max', 'кто'),
        ('max', 'из'),
        ('max', 'нас'),
        " functions as 'who out of us', a handy chunk for comparing people."
    ]),
]
