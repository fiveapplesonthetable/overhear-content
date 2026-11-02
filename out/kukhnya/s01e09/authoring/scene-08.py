# Authoring module for kukhnya-s01e09-scene-08.
ID = 'kukhnya-s01e09-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 8
TITLE = 'Неожиданное родство  (An Unexpected Kinship)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = "The restaurant's floor is calm, and Vika is looking after Alisa between her duties. Max comes over to ask for water and notices a little girl at her side. Here's the Russian, from the top."
OPENER = "Let's go back to the beginning."
TRANSITION = 'Here is the full story once more.'
OUTRO = 'Max now knows who the girl is, and Vika is not pleased that he knows. Everyone in this kitchen is related to someone. Keep listening.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Вика, налей немного воды, пожалуйста.', 'Vika, pour a little water, please.', [(193, 'Костя, налей водички, пожалуйста')], ''),
    ('vika', 'Костя тебе нальёт, а мне некогда.', 'Kostya will pour for you, and I have no time.', [(187, 'Но мне сейчас встречать гостей, видите')], ''),
    ('max', 'Ого, я не знал о твоих детях!', 'Wow, I did not know about your children!', [(194, 'Ой, я не знал, что у тебя есть дети')], ''),
    ('vika', 'Это не моя дочка, а моя племянница.', 'This is not my daughter, but my niece.', [(196, 'Это дочь моей сестры Алиса')], ''),
    ('max', 'Она очень похожа на тебя внешне.', 'She looks very much like you externally.', [], ''),
    ('vika', 'Её зовут Алиса, и она хорошая девочка.', 'Her name is Alisa, and she is a good girl.', [(196, 'дочь моей сестры Алиса')], ''),
    ('max', 'А почему она говорит про нашего шефа?', 'And why is she talking about our chef?', [(203, 'Мой папа тут главный')], ''),
    ('vika', 'Потому что наш шеф — её родной папа!', 'Because our chef is her own dad!', [(204, 'Ты что, дочка шефа')], ''),
    ('max', 'Неужели шеф — твой близкий родственник?', 'Can it be that the chef is your close relative?', [(206, 'Получается, ты и родственница шефа')], ''),
    ('vika', 'Это совершенно не твоё дело, Макс!', 'That is completely none of your business, Max!', [(207, 'Не твое дело')], ''),
    ('max', 'Теперь я понимаю многие странные вещи.', 'Now I understand many strange things.', [], ''),
    ('vika', 'Иди на кухню и работай молча!', 'Go to the kitchen and work quietly!', [(208, 'Ладно, я пошел')], ''),
]
WALK = [
    (0, None, ["'Vika, pour a little water, please.' Max politely requests a drink using ", ('max', 'пожалуйста'), ' at the end.']),
    (1, None, ["'Kostya will pour for you, and I have no time.' Vika dismisses him completely since she has ", ('vika', 'некогда'), ', meaning she has no time for him.']),
    (2, None, ["'Wow, I did not know about your children!' The bartender expresses clear surprise with ", ('max', 'Ого'), ', a natural exclamation like wow.']),
    (3, None, ["'This is not my daughter, but my niece.' She clarifies the family relationship saying the child is her ", ('vika', 'племянница'), ', or niece.']),
    (4, None, ["'She looks very much like you externally.' He then comments on their striking resemblance ", ('max', 'внешне'), ', meaning on the outside or externally.']),
    (5, None, ["'Her name is Alisa, and she is a good girl.' The busy manager introduces the little ", ('vika', 'девочка'), ', or girl, as a good person.']),
    (6, None, ["'And why is she talking about our chef?' Trying to understand the situation he asks why the kid mentions the ", ('max', 'шефа'), ', referring to their chef.']),
    (7, None, ["'Because our chef is her own dad!' Because of this unexpected answer we hear the word ", ('vika', 'родной'), ', which means her own real dad.']),
    (8, None, ["'Can it be that the chef is your close relative?' Unable to believe his ears he starts with ", ('max', 'Неужели'), ', a word used to express strong disbelief.']),
    (9, None, ["'That is completely none of your business, Max!' Closing the conversation firmly she says this is not his ", ('vika', 'дело'), ', meaning his business.']),
    (10, None, ["'Now I understand many strange things.' Putting all the puzzle pieces together he says ", ('max', 'Теперь'), ', which means now.']),
    (11, None, ["'Go to the kitchen and work quietly!' Sending him back to work she tells him to do it ", ('vika', 'молча'), ', which means silently or without a word.']),
]
