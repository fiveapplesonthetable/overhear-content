ID = 'kukhnya-s06e02-scene-05'
SHOW = "kukhnya"
SEASON = 6
EPISODE = 2
SCENE = 5
TITLE = "Совет Айнуры про поцелуй  (Ainura's Advice About the Kiss)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'ainura': 'angelina', 'senya': 'anja'}
LABELS = {'anya': 'Лёва', 'ainura': 'Айнура', 'senya': 'Сеня'}
SOURCE_NAME = "Кухня (Kukhnya) S6.02"
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'

INTRO = 'In the storeroom, Ainura pulls sous-chef Lyova aside to ask how his romance with her niece Gulya is going, and scolds him for taking Gulya to the cinema five times without kissing her.'

STORY = [
    ('ainura', 'Важное сказать хочу.', 'I want to say something important.', [(64, 'Важное сказать хочу')], 'exact'),
    ('ainura', 'Ты целовал ее?', 'Did you kiss her?', [(68, 'Ты целовал ее?')], 'exact'),
    ('anya', 'Нет, еще не целовал.', 'No, I have not kissed her yet.', [(68, 'Ты целовал ее?')], 'adapted'),
    ('ainura', 'Не переживай, Лёва.', 'Do not worry, Lyova.', [(69, 'Не переживай')], 'adapted'),
    ('ainura', 'Пять раз в кино водил и не целовал ее?', 'You took her to the movies five times and did not kiss her?', [(70, 'пять раз кино водил и не целовал ее?')], 'adapted'),
    ('ainura', 'Она приехала в Москву кино смотреть?', 'Did she come to Moscow to watch movies?', [(71, 'она приехала в Москву кино смотреть?')], 'adapted'),
    ('anya', 'Я же не знаю, как у вас принято за девушками ухаживать.', 'I do not know how it is customary in your country to court girls.', [(72, 'принято за девушками ухаживать')], 'adapted'),
    ('anya', 'У вас сначала у родителей разрешение просить надо.', 'In your country you first have to ask the parents for permission.', [(73, 'у родителей разрешение просить надо')], 'adapted'),
    ('ainura', 'Но это у нас, а тут другая страна.', 'But that is back home, and here is another country.', [(74, 'Но это у нас. А тут другая страна')], 'exact'),
    ('ainura', 'Тут у вас все можно.', 'Here with you anything is allowed.', [(76, 'Тут у вас все можно')], 'exact'),
    ('senya', 'Значит, да, я все слышал.', 'So, yes, I heard everything.', [(80, 'Значит, да, я все слышал')], 'exact'),
    ('senya', 'Прости, что-то я удержаться не смог.', 'Sorry, somehow I could not hold back.', [(85, 'прости, что-то я удержаться не смог')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'I want to say something important.' Spoken Russian keeps this brisk, leaning on 'important' and finishing on 'want'."),
    (1, None, "'Did you kiss her?' Ainura raises the pitch on 'she' to turn the phrase into a direct spoken question. Lyova answers right away."),
    (2, None, "'No, I have not kissed her yet.' The meaning hinges on 'no' working together with 'kissed' in spoken Russian."),
    (3, None, "'Do not worry, Lyova.' In Russian, the idea of 'not' flows naturally into 'Lyova' without extra filler words."),
    (4, None, "'You took her to the movies five times and did not kiss her?' Spoken Russian keeps this brisk, leaning on 'five' and finishing on 'she'."),
    (5, None, "'Did she come to Moscow to watch movies?' The '-a' ending on the past-tense verb for 'came' marks a female speaker or subject."),
    (6, None, "'I do not know how it is customary in your country to court girls.' Notice how Russian expresses 'I' and 'to court' with crisp inflection rather than helper words."),
    (7, None, "'In your country you first have to ask the parents for permission.' Lyova chooses the respectful plural 'you' alongside 'need' to keep a polite distance. Ainura answers right away."),
    (8, None, "'But that is back home, and here is another country.' Here the Russian phrasing highlights 'but' before landing on 'country'."),
    (9, None, "'Here with you anything is allowed.' Ainura chooses the respectful plural 'you' alongside 'may' to keep a polite distance."),
    (10, None, "'So, yes, I heard everything.' The '-l' ending on the verb meaning 'heard' places the action in the masculine past tense."),
    (11, None, "'Sorry, somehow I could not hold back.' Notice the reflexive suffix on the verb meaning 'to hold back', turning the action back on the subject."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Embarrassed that Senya overheard his romantic dilemma, Lyova resolves to finally kiss Gulya on their next date. See you in the next scene.'
CLOSING = ('senya', 'Ты же меня знаешь!')
