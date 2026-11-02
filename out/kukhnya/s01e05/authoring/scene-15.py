# Authoring module for kukhnya-s01e05-scene-15.
ID = 'kukhnya-s01e05-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 15
TITLE = 'Кулинарный вердикт  (The Culinary Verdict)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Still in the Claude Monet kitchen, the fish duel is over. Vika, the art director, has tasted both dishes, and Chef Barinov is passing her verdict on to Max, who expects the worst. Listen in Russian first; you don't need every word."
OPENER = 'Now line by line. Barinov is enjoying every second of this.'
TRANSITION = "Here's the verdict again, start to finish."
OUTRO = 'Two things to keep: the expression for when you think you\'re done for, and the polite way to ask for a taste. Both will come in handy in any kitchen.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('max', 'Шеф, кажется, мне сейчас конец.', "Chef, it looks like I'm done for.", [(187, 'Мне конец')], ""),
    ('barinov', 'Молчи и слушай строгий вердикт жюри.', "Keep quiet and listen to the jury's strict verdict.", [(188, 'Мне понравилось')], ""),
    ('barinov', 'Виктория выбрала именно это первое блюдо.', 'Victoria chose this first dish in particular.', [(189, 'Мне понравилось вот это')], ""),
    ('max', 'А вторую рыбу она назвала ужасной?', 'And the second fish she called awful?', [(190, 'А эту рыбу я бы')], ""),
    ('barinov', 'Она не посоветовала её никому в зале.', "She didn't recommend it to anyone in the hall.", [(190, 'никому не посоветовала')], ""),
    ('barinov', 'Поздравляю, наш повар честно победил сегодня!', 'Congratulations, our cook won fairly today!', [(191, 'Поздравляю')], ""),
    ('max', 'Спасибо большое за отличную справедливую оценку.', 'Thank you very much for the great, fair evaluation.', [(194, 'Спасибо, Виктория Сергеевна')], ""),
    ('barinov', 'Господи, как же это невероятно вкусно!', 'Lord, how incredibly delicious this is!', [(196, 'как же вкусно')], ""),
    ('max', 'Шеф, дайте мне тоже немного попробовать.', 'Chef, let me taste a little too.', [(197, 'дайте попробовать')], ""),
    ('barinov', 'Подожди, я сам ещё не распробовал.', "Wait, I haven't properly tasted it myself yet.", [(198, 'еще сам не распробовал')], ""),
    ('barinov', 'А проигравший повар обязан доесть всё сам.', 'And the losing cook must finish eating everything himself.', [(203, 'доесть самому')], ""),
    ('max', 'Надеюсь, наши гости останутся очень довольны.', 'I hope our guests will remain very pleased.', [(202, 'Вкусно, да')], ""),
]
WALK = [
    (0, None, ['\'Chef, it looks like I\'m done for.\' which expresses \'it seems\', softens a ', ('max', 'кажется,'), " guess. ", ('max', 'мне'), " and ", ('max', 'конец.'), " literally mean 'to me the end', the everyday way to say you're finished."]),
    (1, None, ['\'Keep quiet and listen to the jury\'s strict verdict.\' and ', ('barinov', 'Молчи'), ('barinov', 'слушай'), " are short informal commands, one straight after the other. ", ('barinov', 'вердикт'), " and ", ('barinov', 'жюри.'), " are borrowed words, so you can almost hear the English and French in them."]),
    (2, None, ['\'Victoria chose this first dish in particular.\' Barinov uses her full name, ', ('barinov', 'Виктория'), ", which sounds more formal than the short version. ", ('barinov', 'блюдо.'), " stands for 'dish' and is neuter, so ", ('barinov', 'это'), " and ", ('barinov', 'первое'), " end in -o and -oe to match it."]),
    (3, None, ['\'And the second fish she called awful?\' originates from the Russian word for ', ('max', 'ужасной?'), " 'horror'. After ", ('max', 'назвала'), ", meaning 'called', the description changes endings, so 'awful' ends in -oy."]),
    (4, None, ['\'She didn\'t recommend it to anyone in the hall.\' comes from the root for \'advice\', ', ('barinov', 'посоветовала'), " making it close to 'advised'. ", ('barinov', 'никому'), ", expressing 'to nobody', still needs ", ('barinov', 'не'), " before the verb."]),
    (5, None, ['\'Congratulations, our cook won fairly today!\' represents \'I congratulate\', and the ending ', ('barinov', 'Поздравляю,'), " already indicates 'I'. ", ('barinov', 'честно'), ", expressing 'fairly' or 'honestly', is related to the noun for 'honour'."]),
    (6, None, ['\'Thank you very much for the great, fair evaluation.\' is literally \'big ', ('max', 'Спасибо'), ('max', 'большое'), " thanks'. ", ('max', 'оценку.'), " is used for 'evaluation' but also translates to a mark at school, and it takes this form after ", ('max', 'за'), "."]),
    (7, None, ['\'Lord, how incredibly delicious this is!\' is what people exclaim when something ', ('barinov', 'Господи,'), " amazes them. ", ('barinov', 'вкусно!'), ", translating to 'delicious', comes straight from the noun for 'taste'."]),
    (8, None, ['\'Chef, let me taste a little too.\' , the verb for \'give\', has ', ('max', 'дайте'), " a polite ending because Max is speaking to his boss. Together, ", ('max', 'дайте'), " and ", ('max', 'попробовать.'), " ask for a taste."]),
    (9, None, ['\'Wait, I haven\'t properly tasted it myself yet.\' puts the weight on \'myself\', ', ('barinov', 'сам'), " while ", ('barinov', 'ещё'), ('barinov', 'не'), " indicates 'not yet'. ", ('barinov', 'распробовал.'), " translates to to taste something properly and get the flavour."]),
    (10, None, ['\'And the losing cook must finish eating everything himself.\' Notice the prefixes. ', ('barinov', 'проигравший'), ", the one who lost, is built on the verb for losing a game, and the prefix in ", ('barinov', 'доесть'), " signifies eating right to the end. ", ('barinov', 'обязан'), ", expressing obligation, is the masculine form; for a woman it would take a different ending."]),
    (11, None, ['\'I hope our guests will remain very pleased.\' , meaning \'I hope\', has an ', ('max', 'Надеюсь,'), " ing 'I hope', has an ending that shows it is about the speaker. ", ('max', 'довольны.'), ", indicating 'pleased', takes a plural form because it describes the ", ('max', 'гости'), ", or 'guests'."]),
]
