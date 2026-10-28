# Authoring module for domashniy-arest-s01e12-scene-01.
ID = 'domashniy-arest-s01e12-scene-01'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 12
SCENE = 1
TITLE = 'Монастырская летопись  (Monastery Chronicle)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'grigory': 'Отец Григорий', 'kostik': 'Костик'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.12'
SOURCE_FILE = 'sources/domashniy-arest/s01/e12.ru.dual.srt'
INTRO = "Eight hundred years ago, inside the quiet scriptorium of Sineozersk monastery, monk Konstantin is busy copying an ancient book. His mentor, Father Grigory, watches over him strictly and criticizes his slow and messy handwriting. Konstantin complains that his hand is going numb and that he feels deep dread in his soul. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine Father Grigory and Konstantin's medieval dialogue line by line."
TRANSITION = "Now let's listen to the monastery scriptorium scene again without interruption."
OUTRO = 'Father Grigory takes the manuscript away from Konstantin to finish the work himself. See you next time!'
CLOSING = ('grigory', 'Пока!')
STORY = [
    ('kostik', 'Ух ты, похвала от настоятеля!', 'Oh wow, praise from the abbot!', [(1, 'Ух ты, плюс')], ''),
    ('grigory', 'За что тебе похвала, Константин?', 'What praise do you deserve, Konstantin?', [(2, 'За что, отец Григорий')], ''),
    ('grigory', 'Ты пишешь слишком медленно и грязно.', 'You write too slowly and messily.', [(3, 'пишешь ты медленно и грязнишь')], ''),
    ('kostik', 'Я очень стараюсь писать красиво.', 'I try very hard to write nicely.', [(4, 'Возюкаешь ты и рад')], 'adapted'),
    ('grigory', 'Посмотри, какая кривая буква получилась!', 'Look what a crooked letter turned out!', [(5, 'куды хвост пошел')], 'adapted'),
    ('grigory', 'Исправляй эту ошибку прямо сейчас.', 'Correct this mistake right now.', [(6, 'Подчищай')], 'adapted'),
    ('kostik', 'Господи, прости меня грешного.', 'Lord, forgive me a sinner.', [(7, 'Прости, господи')], ''),
    ('grigory', 'У нас осталось очень мало времени.', 'We have very little time left.', [(8, 'Времени мало')], ''),
    ('grigory', 'Скоро эту летопись повезут назад.', 'Soon this chronicle will be taken back.', [(8, 'рукопись обратно в Киев поедет')], 'adapted'),
    ('kostik', 'Мне очень боязно на душе.', 'I feel very frightened in my soul.', [(11, 'боязно мне отец Григорий. Тревога')], ''),
    ('grigory', 'Ты боишься из-за своих грехов!', 'You are afraid because of your sins!', [(12, 'Тебе боязно, потому что ты')], 'adapted'),
    ('kostik', 'Моя рука уже совсем немеет.', 'My hand is going completely numb.', [(15, 'длань уж не имеет')], 'adapted'),
    ('grigory', 'Тогда молись и кайся усердно!', 'Then pray and repent diligently!', [(19, 'Молись и кайся')], ''),
    ('grigory', 'Я сам закончу эту страницу!', 'I will finish this page myself!', [(27, 'Сам буду писать')], 'adapted'),
]
WALK = [
    (0, None, '\'Oh wow, praise from the abbot!\' "Oh wow" is "ukh ty", the go-to Russian exclamation when something catches you happily by surprise. Konstantin thinks he has finally earned a compliment.'),
    (1, None, '\'What praise do you deserve, Konstantin?\' Father Grigory bursts that bubble immediately. Literally he asks "For what to you praise?", challenging the young monk to name one thing he did right.'),
    (2, None, "'You write too slowly and messily.' No gentle feedback in this scriptorium: the elder calls the work both slow and dirty."),
    (3, None, "'I try very hard to write nicely.' Konstantin pleads his case like a schoolboy who knows his handwriting is a mess."),
    (4, None, "'Look what a crooked letter turned out!' Hovering over the parchment, Grigory points right at a lopsided character that ruined the line."),
    (5, None, "'Correct this mistake right now.' To fix ink on parchment takes a knife, and the mentor wants it done on the spot."),
    (6, None, "'Lord, forgive me a sinner.' Instead of arguing back, the monk mutters the classic monastery sigh of a weary scribe."),
    (7, None, "'We have very little time left.' Here is why Grigory is so tense: the deadline is breathing down their necks."),
    (8, None, '\'Soon this chronicle will be taken back.\' In Russian they simply say "they will take this chronicle back", leaving the messengers unnamed because only the book matters.'),
    (9, None, '\'I feel very frightened in my soul.\' Something heavier than bad penmanship is bothering him: a dark foreboding has settled "on the soul", where Russians place deep feelings.'),
    (10, None, "'You are afraid because of your sins!' Grigory has one explanation for every bad feeling, and it is always the young monk's own conscience."),
    (11, None, "'My hand is going completely numb.' After hours hunched over the desk with a quill, his fingers can barely move anymore."),
    (12, None, "'Then pray and repent diligently!' Sore hand or troubled soul, the elder's cure is the same: more prayer and harder repentance."),
    (13, None, "'I will finish this page myself!' Out of patience at last, Grigory snatches the quill to do the job with his own hand."),
]
