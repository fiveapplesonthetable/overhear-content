# Authoring module for dvorik-u-mosta-s02e03-scene-02.
ID = 'dvorik-u-mosta-s02e03-scene-02'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 3
SCENE = 2
TITLE = 'Зелёная гостевая книга  (The Green Guest Book)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'larisa': 'Лариса', 'yaroslav': 'Ярослав'}
INTRO = 'At the sunny corner table, Larisa puts on her reading glasses beside Kira and Yaroslav and opens the cloth-bound green ledger to May thirty years ago. Let\'s listen in first.'
OPENER = "Let's turn the old pages again, one line at a time."
TRANSITION = 'Now listen to the whole guest book reading again without stopping.'
OUTRO = "The mystery of the locked sunroom and the unfinished page is solved, and Larisa offers to complete the waltz for Friday's opening night. See you next time."
CLOSING = ('larisa', 'Всего доброго!')
STORY = [
    ('larisa', 'Посмотрите, какие аккуратные страницы: дата, номер, имя гостя и погода.', 'Look how neat the pages are: date, room, guest name, and weather.'),
    ('kira', 'Откройте десятое мая, Лариса Борисовна, ту пятницу с нашей открытки!', 'Open it to the tenth of May, Larisa Borisovna, that Friday from our postcard!'),
    ('yaroslav', 'Вот! Тут написано: всю ночь сильный дождь, вода капала на пианино.', 'Here! It says: heavy rain all night, water dripped onto the piano.'),
    ('larisa', 'Дальше: пианино поставили в сухой угол, средняя клавиша застряла.', 'Next: the piano was moved to the dry corner, the middle key got stuck.'),
    ('kira', 'Ой! Одна дождливая ночь сломала и крышу, и клавишу сразу!', 'Oh! One rainy night broke both the roof and the key at once!'),
    ('yaroslav', 'А внизу записка тёти: девятый номер закрыт, пока крыша не высохнет.', "And below is my aunt's note: room nine is closed until the roof dries."),
    ('larisa', 'И свой вальс без конца она положила под крышку ждать солнца!', 'And she put her waltz with no ending under the lid to wait for the sun!'),
    ('kira', 'Потом летние гости, годы, и перед дверью встал шкаф.', 'Then summer guests, years, and a bookcase went up in front of the door.'),
    ('yaroslav', 'Она так и не услышала вторую половину своего пятничного вальса.', 'She never got to hear the second half of her Friday waltz.'),
    ('larisa', 'Ярослав Ильич, можно я допишу шестнадцать тактов к пятнице?', 'Yaroslav Ilyich, may I write the missing sixteen bars by Friday?'),
    ('yaroslav', 'Вы закончите песню моей тёти к нашему открытию, Лариса Борисовна?!', "You would finish my aunt's song for our opening, Larisa Borisovna?!"),
    ('larisa', 'В том же стиле, и её первая мелодия приведёт нас домой.', 'In the same style, and her first melody will lead us home.'),
]
WALK = [
    (0, None, ["'Look how neat the pages are: date, room, guest name, and weather.' To gush about something, start with ", (None, 'какие аккуратные'), ", 'what neat ones', where English would say 'how neat'."]),
    (1, None, ["'Open it to the tenth of May, Larisa Borisovna, that Friday from our postcard!' Russian dates use an ordinal number before the month: ", (None, 'десятое мая,'), " is literally 'the tenth of May'."]),
    (2, None, ["'Here! It says: heavy rain all night, water dripped onto the piano.' When reading out a note, Russians say ", (None, 'Тут написано:'), " 'here it is written', where English says 'it says'."]),
    (3, None, ["'Next: the piano was moved to the dry corner, the middle key got stuck.' Nobody is named as the mover: ", (None, 'пианино поставили'), " is simply 'they put the piano', a neat way to skip the who."]),
    (4, None, ["'Oh! One rainy night broke both the roof and the key at once!' Doubling the 'and' gives 'both... and': ", (None, 'и крышу, и клавишу'), ". Then ", (None, 'сразу!'), " adds 'at once'."]),
    (5, None, ["'And below is my aunt's note: room nine is closed until the roof dries.' Yaroslav points to the bottom of the page with ", (None, 'А внизу'), ", 'and down below', a word worth pairing with 'up above'."]),
    (6, None, ["'And she put her waltz with no ending under the lid to wait for the sun!' A waltz ", (None, 'без конца'), " is 'without an end', and the same chunk can also mean 'endlessly'."]),
    (7, None, ["'Then summer guests, years, and a bookcase went up in front of the door.' Kira tells thirty years in one breath, starting with ", (None, 'Потом'), ", the everyday 'then, after that' for any story."]),
    (8, None, ["'She never got to hear the second half of her Friday waltz.' The sad chunk ", (None, 'так и не услышала'), " means 'never did get to hear', after waiting a long time."]),
    (9, None, ["'Yaroslav Ilyich, may I write the missing sixteen bars by Friday?' A small prefix meaning 'to the end' turns 'I will write' into ", (None, 'допишу'), ", 'I will finish writing'. Asking ", (None, 'можно я'), " is a polite 'may I'."]),
    (10, None, ["'You would finish my aunt's song for our opening, Larisa Borisovna?!' Built from 'to open', the word ", (None, 'открытию,'), " here is the opening of the inn itself."]),
    (11, None, ["'In the same style, and her first melody will lead us home.' A reusable chunk: ", (None, 'В том же'), " means 'in the same', so swap in your own word after it."]),
]
