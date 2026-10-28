# Authoring module for kukhnya-s06e18-scene-01.
ID = 'kukhnya-s06e18-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 18
SCENE = 1
TITLE = 'Операция в Германии  (Surgery in Germany)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'doctor': 'Врач', 'eleonora': 'Элеонора', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.18'
SOURCE_FILE = 'sources/kukhnya/s06/e18.ru.srt'
INTRO = 'At the start of this episode, the hospital doctor tells Katya, Elena, and Eleonora that Chef Barinov needs an urgent operation in Germany costing two hundred and fifty thousand euros. With her own assets tied up in a loan, Eleonora promises to ask a wealthy friend for help.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'While Eleonora reaches out to her philanthropist friend Alyokhin, the kitchen staff at the hotel learn they must work without their chef. Until next time!'
CLOSING = ('eleonora', 'Хорошего дня!')
STORY = [
    ('doctor', 'Его состояние стабильно тяжёлое.', 'His condition is stable but serious.', [(1, 'Состояние стабильно тяжелое')], 'adapted'),
    ('doctor', 'Слава богу, такое сейчас лечится.', 'Thank goodness, this is treatable now.', [(2, 'слава богу, такое лечится')], 'adapted'),
    ('doctor', 'Нужна срочная операция в Германии.', 'An urgent operation in Germany is needed.', [(4, 'Нужна срочная операция в Германии')], 'adapted'),
    ('doctor', 'По подсчётам это стоит дорого.', 'By estimates this costs a lot.', [(5, 'По предварительным подсчетам')], 'adapted'),
    ('katya', 'У меня нет таких денег.', 'I do not have that kind of money.', [(7, 'У меня нет таких денег')], 'adapted'),
    ('katya', 'Деньги не проблема, да, мама?', 'Money is not a problem, right, Mom?', [(8, 'Деньги не проблема. Да, мам')], 'adapted'),
    ('eleonora', 'Вообще-то это большая проблема.', 'Actually, it is a big problem.', [(9, 'Вообще-то проблема')], 'adapted'),
    ('katya', 'Но ведь он мой отец.', 'But after all, he is my father.', [(10, 'Вообще-то он мой отец')], 'adapted'),
    ('eleonora', 'Я отель в Питере построила.', 'I built a hotel in Saint Petersburg.', [(15, 'я отель в Питере на что построила')], 'adapted'),
    ('eleonora', 'Я большой кредит под залог взяла.', 'I took out a big loan against collateral.', [(16, 'Я кредит взяла. Под залог')], 'adapted'),
    ('katya', 'Я могу свою квартиру продать.', 'I can sell my apartment.', [(17, 'Я могу квартиру свою продать')], 'adapted'),
    ('eleonora', 'Не надо ничего сейчас продавать.', 'There is no need to sell anything right now.', [(19, 'не надо'), (19, 'продавать')], 'adapted'),
]
WALK = [
    (0, None, "'His condition is stable but serious.' Even though his condition is stable but serious, the doctor keeps a steady face in front of Eleonora."),
    (1, None, "'Thank goodness, this is treatable now.' Here telling Eleonora to thank goodness this is treatable now sets up the next turn in their exchange."),
    (2, None, "'An urgent operation in Germany is needed.' Saying that an urgent operation in Germany is needed is how the doctor sets the tone with Eleonora."),
    (3, None, "'By estimates this costs a lot.' Once by estimates this costs a lot, the doctor can finally tell Eleonora what he means."),
    (4, None, '\'I do not have that kind of money.\' Adding that she does not have that kind of money fills in the missing piece for the doctor. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (5, None, '\'Money is not a problem, right, Mom?\' Wondering if money is not a problem right Mom shows Katya caught off guard. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (6, None, "'Actually, it is a big problem.' Since it is a big problem, Eleonora does not waste words on excuses."),
    (7, None, "'But after all, he is my father.' Mentioning that after all he is her father moves the talk in a new direction."),
    (8, None, "'I built a hotel in Saint Petersburg.' Between the point and the friend, Eleonora gives the doctor a quick, grounded response."),
    (9, None, "'I took out a big loan against collateral.' Because she took out a big loan against collateral, Eleonora treats the matter as settled."),
    (10, None, "'I can sell my apartment.' Explaining that she can sell her apartment lays the cards on the table for the doctor."),
    (11, None, "'There is no need to sell anything right now.' Eleonora reminds the doctor that there is no need to sell anything right now before the moment passes. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
]
