# Authoring module for kukhnya-s01e05-scene-09.
ID = 'kukhnya-s01e05-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 9
TITLE = "Поддержка подруги  (A Friend's Support)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Back in the Claude Monet staff area, Nastya is still crying over Max, and her fellow waitress Sasha has come to sit with her. Sasha is the practical kind of friend who says exactly what she thinks. Listen to it in Russian first.'
OPENER = 'Now slowly. Sasha does most of the work here, with short, warm orders.'
TRANSITION = 'It comes round again, in order.'
OUTRO = 'Take one pattern away from this: phrasing \'I liked Max\' as \'Max was pleasing to me\'. That\'s how Russians say they like someone or something, and you\'ll hear it constantly.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('sasha', 'Настя, перестань так сильно расстраиваться!', 'Nastya, stop being so deeply upset!', [(137, 'Да не расстраивайся ты')], ""),
    ('nastya', 'Мне очень больно, он разбил мне сердце.', 'It hurts me very much, he broke my heart.', [], ""),
    ('sasha', 'Знаешь, сколько парней у тебя ещё будет?', 'Do you know how many more guys you will still have?', [(138, 'Знаешь, сколько мужиков тебя еще кинет')], ""),
    ('nastya', 'Мне не нужны другие, мне нравился Макс.', 'I do not need others, I liked Max.', [], ""),
    ('sasha', 'Неужели стоит так убиваться из-за каждого?', 'Is it really worth falling apart over every one?', [(139, 'Что, и за каждого убиваться, что ли')], ""),
    ('nastya', 'Я боюсь, что меня снова обманут.', 'I am afraid that they will deceive me again.', [(140, 'Меня опять кинут')], ""),
    ('sasha', 'Ты добрая, красивая и очень умная.', 'You are kind, beautiful, and very smart.', [], ""),
    ('nastya', 'Тогда почему он так быстро забыл меня?', 'Then why did he forget me so quickly?', [], ""),
    ('sasha', 'Потому что он глупый и ветреный парень.', 'Because he is a foolish and fickle guy.', [], ""),
    ('nastya', 'Я хочу, чтобы он понял свою ошибку.', 'I want him to understand his mistake.', [], ""),
    ('sasha', 'Вот это уже правильные мысли, подруга!', 'Now those are the right thoughts, my friend!', [], ""),
    ('nastya', 'Спасибо тебе огромное за тёплую поддержку.', 'Thank you so much for the warm support.', [], ""),
]
WALK = [
    (0, None, ["'Nastya, stop being so deeply upset!' , meaning 'stop', is followed by ", ('sasha', 'перестань'), " the 'to' form, here ", ('sasha', 'расстраиваться!'), ", which is used for 'to get upset'. Its reflexive ending makes it 'stop upsetting yourself'."]),
    (1, None, ["'It hurts me very much, he broke my heart.' translates literally as 'to me ", ('nastya', 'Мне'), ('nastya', 'больно,'), " painful'. ", ('nastya', 'разбил'), " is the action for smashing a glass, and here it is applied to ", ('nastya', 'мне'), ('nastya', 'сердце.'), ", giving us 'to me the heart'."]),
    (2, None, ["'Do you know how many more guys you will still have?' After ", ('sasha', 'сколько'), ", for 'how many', the word for guy becomes ", ('sasha', 'парней'), ". The phrase ", ('sasha', 'у'), ('sasha', 'тебя'), ('sasha', 'будет?'), " is used for 'at you will be', expressing the future of 'you have'."]),
    (3, None, ["'I do not need others, I liked Max.' Both halves start with ", ('nastya', 'Мне'), ", equivalent to 'to me'. The sequence ", ('nastya', 'мне'), ('nastya', 'нравился'), ('nastya', 'Макс.'), " literally expresses 'to me was pleasing Max', showing that in this phrasing, it's Max who does the pleasing."]),
    (4, None, ["'Is it really worth falling apart over every one?' indicates 'it is worth'. The ", ('sasha', 'стоит'), " word ", ('sasha', 'убиваться'), " is literally 'to kill yourself', but people use it for grieving too hard."]),
    (5, None, ["'I am afraid that they will deceive me again.' stands for 'I am afraid', and ", ('nastya', 'боюсь,'), " s for 'I am afraid', and it ends in a short reflexive sound. ", ('nastya', 'обманут.'), " has no named subject, creating the sense of 'people will lie to me'."]),
    (6, None, ["'You are kind, beautiful, and very smart.' All three describing words end in an 'aya' sound, as they apply to a woman. For instance, ", ('sasha', 'умная.'), ", signifying 'smart', comes from the root for 'mind'."]),
    (7, None, ["'Then why did he forget me so quickly?' The combination ", ('nastya', 'так'), ('nastya', 'быстро'), " gives us 'so quickly'. The action ", ('nastya', 'забыл'), " ends in a consonant because Max did the forgetting."]),
    (8, None, ["'Because he is a foolish and fickle guy.' The phrase ", ('sasha', 'Потому'), ('sasha', 'что'), " answers 'because', sounding similar to the previous question's 'why'. The describing word ", ('sasha', 'ветреный'), ", used for 'fickle', comes from the word for 'wind'."]),
    (9, None, ["'I want him to understand his mistake.' Russian structures this as 'I want so-that he understood', seen in ", ('nastya', 'хочу,'), ('nastya', 'чтобы'), ('nastya', 'он'), ('nastya', 'понял'), ". After the connector for 'so-that', the action shifts into its past form."]),
    (10, None, ["'Now those are the right thoughts, my friend!' The start ", ('sasha', 'Вот'), ('sasha', 'это'), ('sasha', 'уже'), " works like 'now that's more like it'. The final word ", ('sasha', 'подруга!'), " refers to a female friend, while a male friend would use a shorter version."]),
    (11, None, ["'Thank you so much for the warm support.' Using ", ('nastya', 'Спасибо'), ('nastya', 'тебе'), ", meaning 'thanks to you', makes it personal. Adding ", ('nastya', 'огромное'), ", which is the word for 'huge', is how you turn a simple thanks into 'thanks so much'."]),
]
