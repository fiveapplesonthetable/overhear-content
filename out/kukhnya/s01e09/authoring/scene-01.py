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
INTRO = "This is Kukhnya, a Russian comedy set in the kitchen of Claude Monet, a smart French restaurant in Moscow. Chef Barinov rules it with a loud voice, and young Max is the newest cook. In this episode a huge banquet lands on the pastry section, and the chef's small daughter ends up spending the whole day in the kitchen. First, Louis, the French pastry chef, goes to the chef for help. You'll hear it in Russian first, and you don't need to catch every word."
OPENER = "Now we'll pick it apart."
TRANSITION = 'The full thing, one more time.'
OUTRO = "Barinov already has someone in mind, and Louis isn't delighted. You'll see why when you watch. Until the next one."
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
    (0, None, ["'Chef, I have big problems.' Louis starts the conversation by saying ", ('louis', 'проблемы'), ', which means problems, letting the chef know something is wrong.']),
    (1, None, ["'What happened in the kitchen again?' The chef is clearly annoyed and uses ", ('barinov', 'опять'), ' to point out that this is happening again.']),
    (2, None, ["'I urgently need a good assistant.' This situation cannot wait, so Louis adds ", ('louis', 'срочно'), ' to express that he needs help urgently.']),
    (3, None, ["'Why are you not working alone?' Asking why he cannot manage by himself, the chef says ", ('barinov', 'один'), ' meaning alone.']),
    (4, None, ["'I alone will not manage today.' Louis admits that he will not manage by saying ", ('louis', 'справлюсь'), ' to show his inability to cope today.']),
    (5, None, ["'Do you have too much work?' Wondering about the amount of tasks, Barinov says ", ('barinov', 'слишком'), ' for too much.']),
    (6, None, ["'A very big banquet order arrived.' A huge event is coming up, as Louis mentions an order, ", ('louis', 'заказ'), ', that is very big.']),
    (7, None, ["'What exactly needs to be prepared?' Wanting to know the exact details, the chef asks ", ('barinov', 'именно'), ' to specify what is needed.']),
    (8, None, ["'Fresh croissants and a big cake.' The pastry chef describes the baked goods with ", ('louis', 'Свежие'), ' meaning fresh.']),
    (9, None, ["'Max will work with you.' Making a quick decision, the boss tells him Max will help with the work, using ", ('barinov', 'работать'), ' for this.']),
    (10, None, ["'But he does not know how to do anything.' Complaining about the new guy, Louis uses ", ('louis', 'ничего'), ' to point out that he knows absolutely nothing.']),
    (11, None, ["'He will peel and cut.' Assigning simple tasks, Barinov says the new guy will peel, ", ('barinov', 'чистить'), ', as part of his job.']),
    (12, None, ["'Fine, let him wash the dishes.' Giving in eventually, the French chef suggests he should just wash the dishes, or ", ('louis', 'посуду'), ', instead.']),
]
