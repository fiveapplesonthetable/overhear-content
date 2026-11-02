# Authoring module for kukhnya-s01e13-scene-01.
ID = 'kukhnya-s01e13-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 1
TITLE = 'Следующий шаг  (The Next Step)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "This is The Kitchen, a comedy set in the kitchen of Claude Monet, a smart restaurant in Moscow. In this episode, Max and Vika are keeping their romance secret, and the head chef picks a fight with the chef next door over a parking space. We start at the bar, where Nastya has a quiet proposal for Kostya. First the whole thing in the local language, and don't worry if you miss words."
OPENER = 'Now the slow version, with Nastya doing most of the talking.'
TRANSITION = 'And now all of it again, without the commentary.'
OUTRO = "Kostya runs off to buy candles, which tells you he understood exactly what she meant. Let's see how long the secret lasts. Until next time."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Костя, что ты сейчас делаешь?', 'Kostya, what are you doing right now?', [(1, 'Что делаешь?')], ''),
    ('kostya', 'Я стою и натираю бокалы.', 'I am standing and polishing glasses.', [(2, 'Стою, бокал натираю.')], ''),
    ('nastya', 'А я хочу остаться у тебя сегодня.', 'And I want to stay at your place today.', [(3, 'хочу остаться у тебя?')], ''),
    ('kostya', 'У меня? Тебя кто-то выгнал?', 'At my place? Did someone kick you out?', [(4, 'Тебя что, Саша выгнала?')], ''),
    ('nastya', 'Нет, нам пора сделать следующий шаг.', 'No, it is time for us to take the next step.', [(5, 'нам уже пора сделать следующий шаг.')], ''),
    ('kostya', 'Ты хочешь выйти замуж?', 'Do you want to get married?', [(6, 'Жениться, что ли?')], ''),
    ('nastya', 'Костик, ты такой смешной!', 'Kostik, you are so funny!', [(7, 'Костик такой смешной.')], ''),
    ('nastya', 'Мы просто проведём этот вечер вместе.', 'We will simply spend this evening together.', [(8, 'сегодня вечером мы с тобой...')], ''),
    ('kostya', 'И мы никому ничего не скажем?', 'And we will not tell anyone anything?', [(13, 'а мы никому ничего не скажем?')], ''),
    ('nastya', 'Это будет наш маленький секрет.', 'This will be our little secret.', [(12, 'будет')], ''),
    ('kostya', 'Отлично, это звучит очень логично.', 'Great, that sounds very logical.', [], ''),
    ('kostya', 'Я быстро куплю красивые свечи.', 'I will quickly buy beautiful candles.', [], ''),
    ('nastya', 'Хорошо, сделай этот вечер волшебным!', 'Good, make this evening magical!', [(13, 'этот')], ''),
]
WALK = [
    (0, None, ["'Kostya, what are you doing right now?' The language says 'what you now do', with the little ", ('nastya', 'ты'), " for 'you' tucked in the middle. There's one word for 'do' and it covers 'are doing' as well, because there is no need for a separate 'are ...ing'."]),
    (1, None, ["'I am standing and polishing glasses.' Same thing here. 'I stand and polish' means 'I am standing and polishing'. Notice he uses for polishing, ", ('kostya', 'натираю'), ", grows from 'rub', which is exactly what you do to a glass."]),
    (2, None, ["'And I want to stay at your place today.' 'At your place' is ", ('nastya', 'у'), ('nastya', 'тебя'), ", which means 'at you'. The locals use it for anyone's home."]),
    (3, None, ["'At my place? Did someone kick you out?' He answers with the same idea, now as a question. 'Someone kicked you out' puts 'you' first, ", ('kostya', 'Тебя'), ('kostya', 'кто'), '-', ('kostya', 'то'), ('kostya', 'выгнал'), ", and the little ending on the word for 'who' turns it into 'someone'."]),
    (4, None, ["'No, it is time for us to take the next step.' Word for word, 'to us time', which gives 'it is time for us'. Notice for 'next', ", ('nastya', 'следующий'), ", comes from a word meaning 'to follow'."]),
    (5, None, ["'Do you want to get married?' Careful with this one: ", ('kostya', 'выйти'), ('kostya', 'замуж'), " means 'to go out behind a husband', and only a woman can do it. A man would use a different word, so this is a question you can only put to a woman."]),
    (6, None, ["'Kostik, you are so funny!' 'Kostik' is a pet name made from Kostya with a small-making ending, the way English adds 'ie' to a name. The term for 'funny' is ", ('nastya', 'смешной'), ", and the word for 'such' is ", ('nastya', 'такой'), '.']),
    (7, None, ["'We will simply spend this evening together.' Spending time takes its own verb, ", ('nastya', 'проведём'), ', and it is never used for money. Notice for together, ', ('nastya', 'вместе'), ', is an early word that you can reuse everywhere.']),
    (8, None, ["'And we will not tell anyone anything?' Three negatives pile up: ", ('kostya', 'никому'), ('kostya', 'ничего'), ('kostya', 'не'), ". That is how the language makes it emphatic, and it isn't a mistake. Word for word, 'to no one nothing we won't say'."]),
    (9, None, ["'This will be our little secret.' Here ", ('nastya', 'будет'), " means 'will be' and is spoken out loud, and the term for 'little', ", ('nastya', 'маленький'), ", makes the secret sound cosy. The term for 'our', ", ('nastya', 'наш'), ', has no ending added because the term for secret is masculine.']),
    (10, None, ["'Great, that sounds very logical.' The word ", ('kostya', 'звучит'), " means 'it sounds', from the same root as the term for a sound. The word for logical, ", ('kostya', 'логично'), ", ends in an 'o', showing it is the 'how' form."]),
    (11, None, ["'I will quickly buy beautiful candles.' We can break down the sentence: ", ('kostya', 'куплю'), " means 'I will buy', and there's no helper word in it. Notice for candles, ", ('kostya', 'свечи'), ', is a plural, and the term for beautiful has a plural ending to match.']),
    (12, None, ["'Good, make this evening magical!' Nastya gives an order, then names what the evening should turn into. The term for magical, ", ('nastya', 'волшебным'), ", comes from the term for wizard, with the ending of 'made into'."]),
]
