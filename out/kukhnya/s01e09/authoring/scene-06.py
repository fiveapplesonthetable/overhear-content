# Authoring module for kukhnya-s01e09-scene-06.
ID = 'kukhnya-s01e09-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 6
TITLE = 'Уроки кондитера  (Pastry Chef Lessons)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'louis': 'Луи', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = "Max has been given to Louis for the day, and Louis has an anniversary cake to make for a bank's banquet. In the pastry section the two of them work, and Louis can't stop giving orders. See what you can catch."
OPENER = "Here's what is going on, line by line."
TRANSITION = 'Now you can hear it all again.'
OUTRO = "The cake is coming along nicely, and then a knife goes missing. We'll find out where it went in the next scene. Until the next scene."
CLOSING = ('louis', 'Пока!')
STORY = [
    ('louis', 'Макс, быстрее! Уже пора добавлять яйца.', 'Max, faster! It is time to add the eggs.', [(160, 'Быстрее. Уже пора добавлять яйца.')], ''),
    ('max', 'Луи, я делаю всё по рецепту.', 'Louis, I am doing everything according to the recipe.', [], ''),
    ('louis', 'Обычно я делаю начинку сразу.', 'Usually I make the filling right away.', [(161, 'Обычно я делаю начинку сразу,')], ''),
    ('louis', 'Мешай равномерно, чтобы без комочков.', 'Stir evenly, so there are no lumps.', [(165, 'Равномерно, чтобы без комочков.')], ''),
    ('max', 'Сколько шоколада нужно разогреть?', 'How much chocolate needs to be melted?', [(169, 'Сколько чего?'), (168, 'И разогреть шоколад.')], ''),
    ('louis', 'И разогреть шоколад на водяной бане.', 'And melt the chocolate in a water bath.', [(168, 'И разогреть шоколад.')], ''),
    ('max', 'Хорошо, белый или темный шоколад?', 'All right, white or dark chocolate?', [], ''),
    ('louis', 'Только белый, для логотипа банка!', 'Only white, for the bank logo!', [], ''),
    ('louis', 'О, телефон звонит, одну секунду.', 'Oh, the phone is ringing, one second.', [(172, 'Телефон.')], ''),
    ('louis', 'Алло? Нет, сейчас я на кухне.', 'Hello? No, right now I am in the kitchen.', [], ''),
    ('max', 'Луи, я закончил взбивать крем.', 'Louis, I finished whipping the cream.', [], ''),
    ('louis', 'О, спасибо, отличная работа!', 'Oh, thank you, great job!', [(176, 'О, спасибо.')], ''),
    ('louis', 'Постой, а где мой любимый нож?', 'Wait, where is my favorite knife?', [(178, 'где')], ''),
    ('max', 'Я не трогал твой нож, Луи.', 'I did not touch your knife, Louis.', [], ''),
]
WALK = [
    (0, None, ["'Max, faster! It is time to add the eggs.' If you want someone to hurry, say ", ('louis', 'быстрее'), ' to tell them to go faster.']),
    (1, None, ["'Louis, I am doing everything according to the recipe.' When talking about following a recipe, the word becomes ", ('max', 'рецепту'), ' to show you are guided by it.']),
    (2, None, ["'Usually I make the filling right away.' This sweet filling for the pastry is called ", ('louis', 'начинку'), ', from the word for stuffing.']),
    (3, None, ["'Stir evenly, so there are no lumps.' Nobody wants any lumps in their bowl, so he warns against ", ('louis', 'комочков'), ' in the mixture.']),
    (4, None, ["'How much chocolate needs to be melted?' Asking about the required quantity starts with ", ('max', 'Сколько'), ', meaning how much or how many.']),
    (5, None, ["'And melt the chocolate in a water bath.' Making a gentle water bath uses the word ", ('louis', 'бане'), ', which is also a traditional steam bathhouse.']),
    (6, None, ["'All right, white or dark chocolate?' Dark chocolate is simply translated as ", ('max', 'темный'), ', which means dark rather than black.']),
    (7, None, ["'Only white, for the bank logo!' Because this logo belongs to a bank, it becomes ", ('louis', 'банка'), ' to show who owns it.']),
    (8, None, ["'Oh, the phone is ringing, one second.' Just like in many other languages, the word for phone is ", ('louis', 'телефон'), ' and it sounds almost identical.']),
    (9, None, ["'Hello? No, right now I am in the kitchen.' Answering an incoming call begins with ", ('louis', 'Алло'), ', a greeting reserved strictly for phones.']),
    (10, None, ["'Louis, I finished whipping the cream.' Whipping up the sweet mixture uses ", ('max', 'крем'), ', which sounds exactly like the English equivalent.']),
    (11, None, ["'Oh, thank you, great job!' Praising the completed work as excellent uses the word ", ('louis', 'отличная'), ' to show great approval.']),
    (12, None, ["'Wait, where is my favorite knife?' Any favourite tool or object is described as ", ('louis', 'любимый'), ', which is related to love.']),
    (13, None, ["'I did not touch your knife, Louis.' Denying that he touched the knife, Max uses ", ('max', 'трогал'), ' to say he kept his hands off.']),
]
