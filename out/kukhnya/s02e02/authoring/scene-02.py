# Authoring module for kukhnya-s02e02-scene-02.
ID = 'kukhnya-s02e02-scene-02'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 2
SCENE = 2
TITLE = 'Новый сушист  (The New Sushi Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ainura': 'Айнура', 'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.02'
SOURCE_FILE = 'sources/kukhnya/s02/e02.ru.dual.srt'
INTRO = "Focused on the new sushi chef, The Chef discovers a strange new person in the kitchen who doesn't speak Russian well. He asks Aynura about him. Let's listen closely to Ainura and Chef Viktor's exchange in Russian first, and then walk through each line together."
OPENER = 'Now let us examine the conversation line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The Chef discovers a strange new person in the kitchen who doesn't speak Russian well. He asks Aynura about him. Next time you watch the episode, listen for the Russian expressions for 'to smile' and 'to give' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Ты кто такой?', 'Who are you?', [(32, 'Ты кто такой?')], ''),
    ('barinov', 'Что ты улыбаешься?', 'What are you smiling at?', [(33, 'Что ты улыбаешься?')], ''),
    ('barinov', 'Давай, отвечай.', 'Come on, answer.', [(33, 'Давай, отвечай.')], ''),
    ('barinov', 'Айнура, это японец?', 'Aynura, is this a Japanese person?', [(34, 'Айнура, это что, реальные японецы')], ''),
    ('ainura', 'Нет.', 'No.', [(35, 'Не,')], ''),
    ('ainura', 'Он не наш.', 'He is not ours.', [(36, 'не наш.')], ''),
    ('barinov', 'Слушай, ты перепутал.', 'Listen, you made a mistake.', [(37, 'Слышь, Бехада, ты перепутал.')], ''),
    ('barinov', 'Суши делают рядом.', 'They make sushi next door.', [(38, 'Суши делают в соседнем ресторане.')], ''),
    ('senya', 'Шеф, это новый повар.', 'Chef, this is the new cook.', [], ''),
    ('barinov', 'Какой повар?', 'What cook?', [], ''),
    ('senya', 'Он будет делать суши.', 'He will make sushi.', [], ''),
    ('barinov', 'Иди отсюда.', 'Get out of here.', [(39, 'Давай, дуй отсюда.')], ''),
]
WALK = [
    (0, None, "'Who are you?' Spotting a stranger in a chef's coat, Barinov demands to know who he is."),
    (1, None, "'What are you smiling at?' The man only smiles silently, making Viktor ask what he is grinning at."),
    (2, None, "'Come on, answer.' Impatient, the chef tells the newcomer to speak up and answer."),
    (3, None, "'Aynura, is this a Japanese person?' Turning to Ainura, Viktor asks if the silent man is Japanese."),
    (4, None, "'No.' Ainura shakes her head and says no."),
    (5, None, "'He is not ours.' She clarifies that he is not one of her relatives or countrymen."),
    (6, None, "'Listen, you made a mistake.' Thinking the man walked into the wrong kitchen, Viktor says he made a mistake."),
    (7, None, "'They make sushi next door.' Barinov points out that the sushi bar is next door, not here."),
    (8, None, "'Chef, this is the new cook.' Senya steps in to explain that the man actually is their new cook."),
    (9, None, "'What cook?' Baffled, Viktor asks what kind of cook Senya means."),
    (10, None, "'He will make sushi.' Senya reveals that the new owner hired him to roll sushi in their French kitchen."),
    (11, None, "'Get out of here.' Outraged by the idea of sushi in his restaurant, Barinov orders the man out."),
]
