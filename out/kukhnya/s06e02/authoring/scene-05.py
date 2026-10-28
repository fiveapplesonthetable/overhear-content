# Authoring module for kukhnya-s06e02-scene-05.
ID = 'kukhnya-s06e02-scene-05'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 5
TITLE = "Совет Айнуры про поцелуй  (Ainura's Advice About the Kiss)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ainura': 'Айнура', 'lyova': 'Лёва', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = 'In the storeroom, Ainura pulls sous-chef Lyova aside to ask how his romance with her niece Gulya is going, and scolds him for taking Gulya to the cinema five times without kissing her.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Embarrassed that Senya overheard his romantic dilemma, Lyova resolves to finally kiss Gulya on their next date. Until next time!'
CLOSING = ('senya', 'До встречи!')
STORY = [
    ('ainura', 'Важное сказать хочу.', 'I want to say something important.', [(64, 'Важное сказать хочу')], 'exact'),
    ('ainura', 'Ты целовал ее?', 'Did you kiss her?', [(68, 'Ты целовал ее?')], 'exact'),
    ('lyova', 'Нет, еще не целовал.', 'No, I have not kissed her yet.', [(68, 'Ты целовал ее?')], 'adapted'),
    ('ainura', 'Не переживай, Лёва.', 'Do not worry, Lyova.', [(69, 'Не переживай')], 'adapted'),
    ('ainura', 'Пять раз в кино водил и не целовал ее?', 'You took her to the movies five times and did not kiss her?', [(70, 'пять раз кино водил и не целовал ее?')], 'adapted'),
    ('ainura', 'Она приехала в Москву кино смотреть?', 'Did she come to Moscow to watch movies?', [(71, 'она приехала в Москву кино смотреть?')], 'adapted'),
    ('lyova', 'Я же не знаю, как у вас принято за девушками ухаживать.', 'I do not know how it is customary in your country to court girls.', [(72, 'принято за девушками ухаживать')], 'adapted'),
    ('lyova', 'У вас сначала у родителей разрешение просить надо.', 'In your country you first have to ask the parents for permission.', [(73, 'у родителей разрешение просить надо')], 'adapted'),
    ('ainura', 'Но это у нас, а тут другая страна.', 'But that is back home, and here is another country.', [(74, 'Но это у нас. А тут другая страна')], 'exact'),
    ('ainura', 'Тут у вас все можно.', 'Here with you anything is allowed.', [(76, 'Тут у вас все можно')], 'exact'),
    ('senya', 'Значит, да, я все слышал.', 'So, yes, I heard everything.', [(80, 'Значит, да, я все слышал')], 'exact'),
    ('senya', 'Прости, что-то я удержаться не смог.', 'Sorry, somehow I could not hold back.', [(85, 'прости, что-то я удержаться не смог')], 'adapted'),
]
WALK = [
    (0, None, "'I want to say something important.' Explaining that she wants to say something important lays the cards on the table for Lyova."),
    (1, None, '\'Did you kiss her?\' By checking whether Lyova kisses, Ainura presses Lyova for a straight answer. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (2, None, "'No, I have not kissed her yet.' Mentioning that he has not kissed her yet moves the talk in a new direction."),
    (3, None, "'Do not worry, Lyova.' Noting that do not worry keeps Ainura's side of the story simple and clear."),
    (4, None, '\'You took her to the movies five times and did not kiss her?\' Questioning whether Lyova took her to the movies five times and did not kiss is how Ainura tests Lyova\'s story. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, "'Did she come to Moscow to watch movies?' By asking whether she come to Moscow to watch movies, Ainura presses Lyova for a straight answer."),
    (6, None, '\'I do not know how it is customary in your country to court girls.\' Saying that he does not know how it is customary in Ainura\'s country to court girls is how Lyova sets the tone with Ainura. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (7, None, '\'In your country you first have to ask the parents for permission.\' Once in Ainura\'s country Ainura first have to ask the parents for permission, Lyova can finally tell Ainura what he means. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (8, None, "'But that is back home, and here is another country.' Adding that that is back home and here is another country fills in the missing piece for Lyova."),
    (9, None, '\'Here with you anything is allowed.\' Ainura tells Lyova that here with Lyova anything is allowed without dressing it up. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (10, None, "'So, yes, I heard everything.' Since he heard everything, Senya does not waste words on excuses."),
    (11, None, "'Sorry, somehow I could not hold back.' Mentioning that somehow he could not hold back moves the talk in a new direction."),
]
