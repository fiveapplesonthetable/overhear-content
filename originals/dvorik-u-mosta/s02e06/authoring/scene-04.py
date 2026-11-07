# Authoring module for dvorik-u-mosta-s02e06-scene-04.
ID = 'dvorik-u-mosta-s02e06-scene-04'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 6
SCENE = 4
TITLE = 'Всё продано за пятнадцать минут  (Sold Out in Fifteen Minutes)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'zoya': 'Зоя', 'kira': 'Кира', 'gleb': 'Глеб'}
INTRO = 'At the bustling café counter, Zoya slices golden tarts onto white plates as fast as Kira and Gleb can carry trays out to the tables. Listen to the whole scene first.'
OPENER = "Now let's run between the kitchen and the tables, one order at a time."
TRANSITION = "Let's hear the whole busy café rush again from beginning to end."
OUTRO = 'All but three slices of tart vanish in fifteen minutes, and the whole courtyard falls quiet as six o\'clock arrives. See you inside Room 9 next time.'
CLOSING = ('kira', 'До скорого!')
STORY = [
    ('kira', 'Два мятных чая и три лимонных пирога на четвёртый стол под деревом!', 'Two mint teas and three lemon tarts for table four under the tree!'),
    ('zoya', 'Сейчас будет! Глеб, отнесите горячий чайник на угловой стол у окна!', 'Coming right up! Gleb, take the hot teapot to the corner table by the window!'),
    ('gleb', 'Второй стол говорит, что это лучшее тесто на Липовом переулке!', 'Table two says this is the best pastry on Lipovy Lane!'),
    ('zoya', 'Скажите им, что секрет — мои два помощника на кухне в среду!', 'Tell them the secret was my two kitchen helpers on Wednesday!'),
    ('kira', 'Зоя, сколько кусков лимонного пирога осталось на четвёртом противне?', 'Zoya, how many slices of lemon tart are left on the fourth tray?'),
    ('zoya', 'Считай: один, два, три — из сорока кусков за пятнадцать минут!', 'Count them: one, two, three, out of forty slices in fifteen minutes!'),
    ('gleb', 'Хорошо, что вы испекли ещё два противня тёплых булочек с корицей!', 'Good thing you baked two more trays of warm cinnamon rolls!'),
    ('kira', 'Слушайте, в комнате стало тихо! Кто-то стучит по подставке для нот!', 'Listen, the room went quiet! Someone is tapping on the music stand!'),
    ('zoya', 'Наш сосед из десятого дома принёс скрипку в девятый номер!', 'Our neighbour from number ten brought his violin into room nine!'),
    ('gleb', 'Оставьте чистые тарелки на пять минут — идёмте слушать у двери!', "Leave the clean plates for five minutes, let's go listen at the door!"),
    ('zoya', 'Последние три куска — для Ларисы Борисовны, Матвея и Ярослава Ильича!', 'The last three slices are for Larisa Borisovna, Matvey and Yaroslav Ilyich!'),
    ('kira', 'Снимаем фартуки — уже шесть часов, пятница!', "Aprons off, it is already six o'clock on Friday!"),
]
WALK = [
    (0, None, ["'Two mint teas and three lemon tarts for table four under the tree!' Orders go 'onto' a table in Russian: ", (None, 'на четвёртый стол'), " means 'for table four'."]),
    (1, None, ["'Coming right up! Gleb, take the hot teapot to the corner table by the window!' Waiters answer an order with ", (None, 'Сейчас будет!'), " literally 'it will be now'."]),
    (2, None, ["'Table two says this is the best pastry on Lipovy Lane!' Gleb lets the table speak: ", (None, 'Второй стол говорит,'), " just like English waiters say 'table two wants'."]),
    (3, None, ["'Tell them the secret was my two kitchen helpers on Wednesday!' Someone who helps is ", (None, 'помощника'), ", built on the verb 'to help' plus a person ending."]),
    (4, None, ["'Zoya, how many slices of lemon tart are left on the fourth tray?' A slice or a piece of anything is ", (None, 'кусков'), ", here after 'how many', which changes its ending."]),
    (5, None, ["'Count them: one, two, three, out of forty slices in fifteen minutes!' Time it took to finish is ", (None, 'за пятнадцать минут!'), " with a little word that means 'within'."]),
    (6, None, ["'Good thing you baked two more trays of warm cinnamon rolls!' Gleb starts with ", (None, 'Хорошо, что'), ", 'it is good that', the Russian way to say 'good thing'."]),
    (7, None, ["'Listen, the room went quiet! Someone is tapping on the music stand!' A music stand is just ", (None, 'подставке для нот!'), " literally 'a stand for notes'."]),
    (8, None, ["'Our neighbour from number ten brought his violin into room nine!' House numbers are said as ordinals: ", (None, 'из десятого дома'), " is 'from the tenth house'."]),
    (9, None, ["'Leave the clean plates for five minutes, let's go listen at the door!' Gleb's ", (None, 'идёмте слушать'), " is 'let's go and listen', polite because he says it to two people."]),
    (10, None, ["'The last three slices are for Larisa Borisovna, Matvey and Yaroslav Ilyich!' Saving something for someone uses ", (None, 'для'), ", the word for 'for'."]),
    (11, None, ["'Aprons off, it is already six o'clock on Friday!' Kira's ", (None, 'Снимаем фартуки'), " is 'we take off our aprons', a team command in the present tense."]),
]
