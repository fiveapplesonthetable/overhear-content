ID = 'kukhnya-s06e18-scene-01'
SHOW = "kukhnya"
SEASON = 6
EPISODE = 18
SCENE = 1
TITLE = 'Операция в Германии  (Surgery in Germany)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'eleonora': 'anja', 'doctor': 'angelina'}
LABELS = {'anya': 'Катя', 'eleonora': 'Элеонора', 'doctor': 'Врач'}
SOURCE_NAME = "Кухня (Kukhnya) S6.18"
SOURCE_FILE = 'sources/kukhnya/s06/e18.ru.srt'

INTRO = 'At the start of this episode, the hospital doctor tells Katya, Elena, and Eleonora that Chef Barinov needs an urgent operation in Germany costing two hundred and fifty thousand euros. With her own assets tied up in a loan, Eleonora promises to ask a wealthy friend for help.'

STORY = [
    ('doctor', 'Его состояние стабильно тяжёлое.', 'His condition is stable but serious.', [(1, 'Состояние стабильно тяжелое')], 'adapted'),
    ('doctor', 'Слава богу, такое сейчас лечится.', 'Thank goodness, this is treatable now.', [(2, 'слава богу, такое лечится')], 'adapted'),
    ('doctor', 'Нужна срочная операция в Германии.', 'An urgent operation in Germany is needed.', [(4, 'Нужна срочная операция в Германии')], 'adapted'),
    ('doctor', 'По подсчётам это стоит дорого.', 'By estimates this costs a lot.', [(5, 'По предварительным подсчетам')], 'adapted'),
    ('anya', 'У меня нет таких денег.', 'I do not have that kind of money.', [(7, 'У меня нет таких денег')], 'adapted'),
    ('anya', 'Деньги не проблема, да, мама?', 'Money is not a problem, right, Mom?', [(8, 'Деньги не проблема. Да, мам')], 'adapted'),
    ('eleonora', 'Вообще-то это большая проблема.', 'Actually, it is a big problem.', [(9, 'Вообще-то проблема')], 'adapted'),
    ('anya', 'Но ведь он мой отец.', 'But after all, he is my father.', [(10, 'Вообще-то он мой отец')], 'adapted'),
    ('eleonora', 'Я отель в Питере построила.', 'I built a hotel in Saint Petersburg.', [(15, 'я отель в Питере на что построила')], 'adapted'),
    ('eleonora', 'Я большой кредит под залог взяла.', 'I took out a big loan against collateral.', [(16, 'Я кредит взяла. Под залог')], 'adapted'),
    ('anya', 'Я могу свою квартиру продать.', 'I can sell my apartment.', [(17, 'Я могу квартиру свою продать')], 'adapted'),
    ('eleonora', 'Не надо ничего сейчас продавать.', 'There is no need to sell anything right now.', [(19, 'не надо'), (19, 'продавать')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'His condition is stable but serious.' the doctor anchors the line on 'his', while 'heavy' completes the thought."),
    (1, None, "'Thank goodness, this is treatable now.' The meaning hinges on 'glory' working together with 'is treatable' in spoken Russian."),
    (2, None, "'An urgent operation in Germany is needed.' The meaning hinges on 'needed' working together with 'Germany' in spoken Russian."),
    (3, None, "'By estimates this costs a lot.' In Russian, the idea of 'according to' flows naturally into 'expensive' without extra filler words."),
    (4, None, "'I do not have that kind of money.' In Russian, the idea of 'at' flows naturally into 'money' without extra filler words."),
    (5, None, "'Money is not a problem, right, Mom?' Spoken Russian keeps this brisk, leaning on 'money' and finishing on 'mom'. Eleonora answers right away."),
    (6, None, "'Actually, it is a big problem.' Here the Russian phrasing highlights 'actually' before landing on 'problem'."),
    (7, None, "'But after all, he is my father.' Katya brings out the contrast between 'but' and 'after all' in a few short words."),
    (8, None, "'I built a hotel in Saint Petersburg.' Notice how Russian expresses 'I' and 'built' with crisp inflection rather than helper words."),
    (9, None, "'I took out a big loan against collateral.' Here the Russian phrasing highlights 'I' before landing on 'picked up'."),
    (10, None, "'I can sell my apartment.' The meaning hinges on 'I' working together with 'to sell' in spoken Russian."),
    (11, None, "'There is no need to sell anything right now.' The negative particle sits right before the verb meaning 'to sell' to negate the statement."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'While Eleonora reaches out to her philanthropist friend Alyokhin, the kitchen staff at the hotel learn they must work without their chef. See you in the next scene.'
CLOSING = ('eleonora', 'Он нам точно поможет.')
