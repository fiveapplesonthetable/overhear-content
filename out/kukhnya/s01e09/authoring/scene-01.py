# Authoring module for kukhnya-s01e09-scene-01.
ID = 'kukhnya-s01e09-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 1
TITLE = 'Заказ на банкет  (The Banquet Order)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = "In the bustling kitchen of Claude Monet, French pastry chef Louis is overwhelmed by an enormous banquet order. Desperate for assistance, he appeals to Chef Viktor Barinov, who decides that novice cook Max will be his helper for the day. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine Louis and Chef Barinov's kitchen exchange line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "With a skeptical Louis reluctantly accepting Max's assistance, the kitchen prepares to tackle the demanding banquet pastry order under Chef Barinov's watchful eye. Next time you watch the episode, listen for the Russian expressions for 'banquet' and 'big' — you will catch every word right away. See you next time!"
CLOSING = ('louis', 'Пока!')
STORY = [
    ('louis', 'Шеф, у меня большие проблемы.', 'Chef, I have big problems.', [(1, 'У меня проблемы.')], ''),
    ('barinov', 'Что опять случилось на кухне?', 'What happened in the kitchen again?', [], ''),
    ('louis', 'Мне срочно нужен хороший помощник.', 'I urgently need a good assistant.', [(1, 'Мне очень срочно нужен'), (7, 'тебе нужен помощник.')], ''),
    ('barinov', 'Почему ты не работаешь один?', 'Why are you not working alone?', [], ''),
    ('louis', 'Я один сегодня не справлюсь.', 'I alone will not manage today.', [(4, 'Я один не справлюсь.')], ''),
    ('barinov', 'У тебя слишком много работы?', 'Do you have too much work?', [], ''),
    ('louis', 'Пришёл очень большой заказ на банкет.', 'A very big banquet order arrived.', [(5, 'Очень большой заказ на банкет.')], ''),
    ('barinov', 'Что именно нужно приготовить?', 'What exactly needs to be prepared?', [], ''),
    ('louis', 'Свежие круассаны и большой торт.', 'Fresh croissants and a big cake.', [(6, 'Круассаны')], ''),
    ('barinov', 'Макс будет работать с тобой.', 'Max will work with you.', [(16, 'Макс сегодня твой')], ''),
    ('louis', 'Но он ничего не умеет.', 'But he does not know how to do anything.', [], ''),
    ('barinov', 'Он будет чистить и резать.', 'He will peel and cut.', [], ''),
    ('louis', 'Ладно, пусть моет посуду.', 'Fine, let him wash the dishes.', [], ''),
]
WALK = [
    (0, None, "'Chef, I have big problems.' Overwhelmed at the pastry station, Louis runs to the chef and says he is in big trouble."),
    (1, None, "'What happened in the kitchen again?' Barinov sighs and asks what crisis has hit his kitchen this time."),
    (2, None, "'I urgently need a good assistant.' Louis insists that he urgently needs a capable assistant today."),
    (3, None, "'Why are you not working alone?' Viktor asks why the pastry chef cannot handle his section on his own as usual."),
    (4, None, "'I alone will not manage today.' Louis explains that there is simply too much baking for one person today."),
    (5, None, "'Do you have too much work?' Barinov asks if the workload has really piled up that high."),
    (6, None, "'A very big banquet order arrived.' Louis points to a massive banquet order that just came in."),
    (7, None, "'What exactly needs to be prepared?' Viktor asks what items the banquet menu requires from the pastry station."),
    (8, None, "'Fresh croissants and a big cake.' Louis lists fresh croissants along with an enormous celebration cake."),
    (9, None, "'Max will work with you.' To get Louis off his back, Barinov assigns rookie cook Max to help him."),
    (10, None, "'But he does not know how to do anything.' Louis protests that Max has no idea how to bake fine French pastries."),
    (11, None, "'He will peel and cut.' Viktor shrugs and says Max can peel fruit and chop ingredients."),
    (12, None, "'Fine, let him wash the dishes.' Giving in, Louis decides he will at least put Max on dishwashing duty."),
]
