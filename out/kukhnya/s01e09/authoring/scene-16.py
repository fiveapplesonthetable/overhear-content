# Authoring module for kukhnya-s01e09-scene-16.
ID = 'kukhnya-s01e09-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 16
TITLE = 'Торт для банкета  (The Banquet Cake)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = "The banquet cake is almost ready in the pastry section, and Louis is proud of it. Barinov comes by to check. Then he spots something in the cream that shouldn't be there. Hear it first, then we'll pick it apart."
OPENER = "We'll go slowly this time."
TRANSITION = "This time you'll hear more."
OUTRO = "Louis will fix it, and he promises the cake will be perfect. What the guests don't know won't hurt them. Carry on listening, and see you soon."
CLOSING = ('louis', 'Пока!')
STORY = [
    ('louis', 'Шеф, я почти закончил этот торт.', 'Chef, I have almost finished this cake.', [], ''),
    ('barinov', 'Покажи мне его, Луи.', 'Show it to me, Louis.', [], ''),
    ('louis', 'Я думаю, торт скоро можно подавать.', 'I think the cake can be served soon.', [(309, 'Я думаю, торт через пять минут уже можно подавать.')], ''),
    ('barinov', 'Подожди, это ещё что такое?', 'Wait, what on earth is this?', [(310, 'Это еще что такое?')], ''),
    ('louis', 'Ой, это же железная струбцина!', 'Oh, this is an iron clamp!', [(311, 'Это струб.')], ''),
    ('barinov', 'Откуда она взялась в креме?', 'Where did it come from in the cream?', [], ''),
    ('barinov', 'Это же праздничный торт для гостей!', 'This is a celebration cake for the guests!', [], ''),
    ('louis', 'Наверное, маленькая девочка играла здесь.', 'Probably the little girl was playing here.', [], ''),
    ('barinov', 'Алиса трогала твой торт?', 'Did Alisa touch your cake?', [], ''),
    ('louis', 'Шеф, спокойно, не нужно кричать.', 'Chef, calm down, no need to shout.', [(312, 'Спокойно.')], ''),
    ('louis', 'Я сейчас быстро всё исправлю.', 'I will quickly fix everything right now.', [(313, 'Я все исправлю.')], ''),
    ('barinov', 'Сделай красиво, чтобы гости ничего не заметили.', 'Make it pretty so the guests notice nothing.', [], ''),
    ('louis', 'Обещаю, торт будет идеальным.', 'I promise, the cake will be perfect.', [], ''),
]
WALK = [
    (0, None, ["'Chef, I have almost finished this cake.' The word ", ('louis', 'почти'), ' translates to almost, indicating that the pastry chef is nearly done with his long task.']),
    (1, None, ["'Show it to me, Louis.' The word ", ('barinov', 'Покажи'), ' means to show, which is used here as a direct request for the baker to reveal the dessert.']),
    (2, None, ["'I think the cake can be served soon.' In this sentence, the expression ", ('louis', 'скоро'), ' stands for soon, suggesting the dessert is nearly ready to be given to the guests.']),
    (3, None, ["'Wait, what on earth is this?' The head chef uses the specific command ", ('barinov', 'Подожди'), ' to tell his colleague to hold on a moment while he examines the strange object.']),
    (4, None, ["'Oh, this is an iron clamp!' Here we can clearly hear ", ('louis', 'железная'), ' which describes the iron material of the heavy tool that ended up inside the cake by mistake.']),
    (5, None, ["'Where did it come from in the cream?' Asking about the mysterious origin, ", ('barinov', 'Откуда'), ' questions where the strange object came from before ending up in the sweet dessert.']),
    (6, None, ["'This is a celebration cake for the guests!' To express his massive shock, the boss highlights ", ('barinov', 'праздничный'), ' to emphasize that this is a special celebration cake meant for very important visitors.']),
    (7, None, ["'Probably the little girl was playing here.' Trying to guess what happened, the baker says ", ('louis', 'Наверное'), ' meaning probably, as he suspects a little girl was playing around the kitchen area.']),
    (8, None, ["'Did Alisa touch your cake?' The boss asks if she ", ('barinov', 'трогала'), ' the cake, meaning touched, showing his growing concern about the ruined dessert.']),
    (9, None, ["'Chef, calm down, no need to shout.' Hoping to defuse the stressful situation, the baker uses ", ('louis', 'спокойно'), ' to tell his boss to remain calm and not raise his voice in anger.']),
    (10, None, ["'I will quickly fix everything right now.' Promising to resolve the issue entirely, he says ", ('louis', 'всё'), ' to assure the boss that he will fix absolutely everything about the ruined dessert immediately.']),
    (11, None, ["'Make it pretty so the guests notice nothing.' Instructing him to do a proper job, the head chef says ", ('barinov', 'красиво'), ' so that the final result looks pretty and the guests will not suspect a thing.']),
    (12, None, ["'I promise, the cake will be perfect.' With absolute and complete confidence, the baker states ", ('louis', 'Обещаю'), ' which means I promise, giving his word that the final dessert will be perfect.']),
]
