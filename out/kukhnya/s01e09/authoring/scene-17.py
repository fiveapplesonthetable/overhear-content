# Authoring module for kukhnya-s01e09-scene-17.
ID = 'kukhnya-s01e09-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 17
TITLE = 'Где Алиса?  (Where Is Alisa?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'tanya': 'Таня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = "The banquet is winding down, and Alisa's mother Tanya arrives at the restaurant to pick her up. Barinov has some explaining to do, and he does not want to do it. Here is how they put it."
OPENER = 'First line first.'
TRANSITION = 'Time to hear it all again.'
OUTRO = "Tanya has seen through him in a second, and Barinov is running after her. It's a family argument, in a restaurant. Catch you next time."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('tanya', 'Виктор, добрый вечер. Где Алиса?', 'Viktor, good evening. Where is Alisa?', [(314, 'Где Алиса?')], ''),
    ('barinov', 'А мы с ней решили остаться.', 'And she and I decided to stay.', [(314, 'А мы с ней решили, что она еще со мной на денек останется.')], ''),
    ('barinov', 'Она побудет со мной ещё денёк.', 'She will stay with me one more day.', [(314, 'на денек останется.')], ''),
    ('barinov', 'Ты же не возражаешь, Таня?', 'You do not mind, Tanya?', [(315, 'Ты же не возражаешь.')], ''),
    ('tanya', 'Ну, если она сама так решила.', 'Well, if she decided so herself.', [(316, 'Ну, если она так решила сама.')], ''),
    ('tanya', 'Пойдём, я быстро с ней попрощаюсь.', 'Let us go, I will quickly say goodbye to her.', [(317, 'Ладно, пойдем, я с ней попрощаюсь.')], ''),
    ('barinov', 'Зачем? Я сам всё передам!', 'What for? I will pass on everything myself!', [(317, 'Ну, зачем?'), (318, 'Я передам.')], ''),
    ('barinov', 'Она там на кухне развлекается.', 'She is having fun there in the kitchen.', [(318, 'Она там на кухне развлекается.')], ''),
    ('barinov', 'Она просила передать тебе пока.', 'She asked me to say goodbye to you.', [(319, 'Кстати, она просила передать тебе пока.')], ''),
    ('tanya', 'Так, что с ней случилось?', 'Wait, what happened to her?', [(320, 'Что с ней случилось?')], ''),
    ('barinov', 'Всё нормально, она просто играет.', 'Everything is fine, she is just playing.', [(320, 'Все нормально.'), (321, 'На кухне играется.')], ''),
    ('tanya', 'А врать ты так и не научился.', 'And you still have not learned how to lie.', [(322, 'А вот врать ты до сих пор не научился.')], ''),
    ('barinov', 'Таня, подожди, я всё объясню!', 'Tanya, wait, I will explain everything!', [], ''),
]
WALK = [
    (0, None, ["'Viktor, good evening. Where is Alisa?' Pay attention to ", ('tanya', 'вечер'), ' is the word for evening, making this a standard formal greeting to start the conversation.']),
    (1, None, ["'And she and I decided to stay.' This uses the word ", ('barinov', 'решили'), ' translates to decided, showing how quickly he invents an excuse on the spot.']),
    (2, None, ["'She will stay with me one more day.' Let's look at ", ('barinov', 'денёк'), ' represents a cute and friendly way to say day, softening his unexpected news.']),
    (3, None, ["'You do not mind, Tanya?' They use the expression ", ('barinov', 'возражаешь'), ' means object or mind, framing his sudden plan as if it is already approved.']),
    (4, None, ["'Well, if she decided so herself.' The word ", ('tanya', 'сама'), ' stands for herself, placing the responsibility entirely on the supposed choice of the child.']),
    (5, None, ["'Let us go, I will quickly say goodbye to her.' Here we have ", ('tanya', 'быстро'), ' acts as the word for quickly, proving she has no time to waste here.']),
    (6, None, ["'What for? I will pass on everything myself!' Pay attention to ", ('barinov', 'Зачем'), ' asks for what purpose, revealing his rising panic as he tries to stop her.']),
    (7, None, ["'She is having fun there in the kitchen.' The target word is ", ('barinov', 'кухне'), ' means kitchen, which is the place he claims the little girl is having fun.']),
    (8, None, ["'She asked me to say goodbye to you.' You can hear ", ('barinov', 'пока'), ' serves as a casual bye, completing the fake message he is delivering right now.']),
    (9, None, ["'Wait, what happened to her?' The character says ", ('tanya', 'случилось'), ' questions what happened, proving that she can see right through his terrible acting.']),
    (10, None, ["'Everything is fine, she is just playing.' Let's look at ", ('barinov', 'нормально'), ' insists that everything is normal, even though his calm tone is completely fake.']),
    (11, None, ["'And you still have not learned how to lie.' We hear the word ", ('tanya', 'врать'), ' directly means to lie, summing up her weary reaction to his constant nonsense.']),
    (12, None, ["'Tanya, wait, I will explain everything!' In this sentence, we have ", ('barinov', 'подожди'), ' pleads with her to wait, ending the scene right in the middle of a chase.']),
]
