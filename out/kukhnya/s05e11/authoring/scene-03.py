# Authoring module for kukhnya-s05e11-scene-03.
ID = 'kukhnya-s05e11-scene-03'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 11
SCENE = 3
TITLE = 'Новый повар Артём  (The New Cook Artyom)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'denis': 'Денис', 'eleonora': 'Элеонора'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.11'
SOURCE_FILE = 'sources/kukhnya/s05/e11.ru.srt'
INTRO = "In the hotel lobby, job applicant Artyom spills coffee on Eleonora Andreyevna's trousers. When Eleonora declares that he will never work at her hotel, Chef Barinov immediately hires the young cook out of spite, prompting Eleonora to order three difficult French dishes."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that finishes the clash in the lobby. Listen for how Chef Barinov asserts his authority over the kitchen and hires Artyom on the spot. Until next time!'
CLOSING = ('barinov', 'Увидимся!')
STORY = [
    ('eleonora', 'А можно поаккуратнее?', 'Could you be more careful?', [(38, 'А можно поаккуратнее')], 'adapted'),
    ('eleonora', 'Что простите? Вы мне брюки будете стирать?', 'What do you mean forgive me? Are you going to wash my trousers?', [(41, 'Что простите? Вы мне брюки будете стирать')], 'adapted'),
    ('denis', 'Ну, хотите, постираю. Снимайте!', 'Well, if you want, I will wash them. Take them off!', [(42, 'Ну, хотите, постираю. Снимайте')], 'adapted'),
    ('denis', 'Здравствуйте, я бы хотел у вас работать в ресторане.', 'Hello, I would like to work in your restaurant.', [(44, 'Здравствуйте'), (45, 'Я бы хотел у вас'), (45, 'в ресторане')], 'adapted'),
    ('denis', 'Вот моё резюме.', 'Here is my resume.', [(46, 'Вот мое резюме')], 'adapted'),
    ('eleonora', 'Мне очень жаль, но вы нам не подходите.', 'I am very sorry, but you do not suit us.', [(47, 'мне очень жаль'), (48, 'Но вы нам не подходите')], 'adapted'),
    ('barinov', 'Только я решаю, кто работает на моей кухне!', 'Only I decide who works in my kitchen!', [(49, 'только я решаю, кто работает на моей кухне')], 'adapted'),
    ('barinov', 'Резюме у парня приличное.', "The guy's resume is decent.", [(50, 'Резюме у парня приличное')], 'adapted'),
    ('eleonora', 'Ты его даже не читал! Он не будет здесь работать.', 'You did not even read it! He will not work here.', [(51, 'Ты его даже не читал'), (52, 'Он не будет здесь работать')], 'adapted'),
    ('barinov', 'Ты принят! Поздравляю, пойдём.', 'You are hired! Congratulations, let us go.', [(53, 'Ты принят. Поздравляю. Пойдем')], 'adapted'),
    ('eleonora', 'Ладно, тогда пусть он приготовит мне гратен и перепёлку.', 'Fine, then let him cook gratin and quail for me.', [(54, 'Ладно'), (55, 'Тогда пусть он приготовит мне'), (56, 'перепелку')], 'adapted'),
    ('eleonora', 'И лично мне принесёт! Посмотрим, какой он повар.', 'And bring it to me personally! We will see what kind of cook he is.', [(57, 'И лично мне принесет'), (58, 'Посмотрим, какой он повар')], 'adapted'),
]
WALK = [
    (0, None, '\'Could you be more careful?\' Eleonora questions openly to Barinov here, joining "mozhno" ("may, can") to "poakkuratneye" ("more carefully") so every word pulls its weight.'),
    (1, None, '\'What do you mean forgive me? Are you going to wash my trousers?\' Eleonora probes warmly for Denis\'s benefit, putting "prostite" ("excuse me") alongside "bryuki" ("trousers, pants") in a tight, everyday turn of phrase.'),
    (2, None, '\'Well, if you want, I will wash them. Take them off!\' Denis picks a calm angle in this beat, pairing "khotite" ("want") with "postirayu" ("will wash") to get the point across in plain spoken Russian.'),
    (3, None, '\'Hello, I would like to work in your restaurant.\' Denis favors a playful view on the spot, linking "zdravstvuyte" ("hello"), "khotel" ("wanted"), and "rabotat" ("to work") in one brisk exchange.'),
    (4, None, '\'Here is my resume.\' Denis brings a calm style for Barinov, placing "rezyume" ("résumé") straight beside "vot" ("there, here") with no word for "to be" needed.'),
    (5, None, '\'I am very sorry, but you do not suit us.\' Eleonora offers a sharp tone in the scene, combining "ochen" ("very much") and "zhal" ("it is a pity") so the key meaning lands right away.'),
    (6, None, '\'Only I decide who works in my kitchen!\' Barinov shows a candid tack as they talk, joining "tolko" ("only") to "reshayu" ("decide") so every word pulls its weight.'),
    (7, None, '\'The guy\'s resume is decent.\' Barinov shows a pointed stance during the exchange, weaving "rezyume" ("résumé") together with "parnya" ("boyfriend") just the way native speakers do.'),
    (8, None, '\'You did not even read it! He will not work here.\' Eleonora shares an honest tempo in this beat, combining "chital" ("read") and "budet" ("will be") so the key meaning lands right away.'),
    (9, None, '\'You are hired! Congratulations, let us go.\' Barinov chooses a steady view straight away, leaning on "prinyat" ("accepted") before closing the thought with "pozdravlyayu" ("congratulations").'),
    (10, None, '\'Fine, then let him cook gratin and quail for me.\' Eleonora strikes a calm note beside Barinov, leaning on "togda" ("back then") before closing the thought with "prigotovit" ("makes, cooks").'),
    (11, None, '\'And bring it to me personally! We will see what kind of cook he is.\' Eleonora establishes a warm style in this beat, leaning on "lichno" ("personally") before closing the thought with "prinesyot" ("will bring").'),
]
