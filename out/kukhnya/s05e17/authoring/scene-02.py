# Authoring module for kukhnya-s05e17-scene-02.
ID = 'kukhnya-s05e17-scene-02'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 17
SCENE = 2
TITLE = 'Другая Гончарова  (The Other Goncharova)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'doctor': 'Врач', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.17'
SOURCE_FILE = 'sources/kukhnya/s05/e17.ru.srt'
INTRO = 'Max bursts into the delivery room without shoe covers expecting to see Vika, only to find another patient named Goncharova. When he finally reaches Vika by phone, she surprises him.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Baffled that Vika is back at the restaurant instead of the maternity ward, Max heads straight to the hotel. See you next time!'
CLOSING = ('vika', 'До завтра!')
STORY = [
    ('doctor', 'Эй, наденьте бахилы немедленно!', 'Hey, put on shoe covers immediately!', [(14, 'Эй')], 'adapted'),
    ('max', 'Вика, это ты здесь?', 'Vika, is that you here?', [(16, 'Вика')], 'adapted'),
    ('doctor', 'Нет, меня зовут Маша.', 'No, my name is Masha.', [(17, 'Нет, Маша')], 'adapted'),
    ('max', 'Подождите, а где Гончарова?', 'Wait, where is Goncharova?', [(18, 'Где Гончарова')], 'adapted'),
    ('doctor', 'Я тоже Гончарова.', 'I am Goncharova too.', [(18, 'Я Гончарова')], 'adapted'),
    ('max', 'А где другая Гончарова?', 'And where is the other Goncharova?', [(19, 'А другая Гончарова')], 'adapted'),
    ('doctor', 'Ребёнок никак рождаться не хочет.', 'The baby just does not want to be born yet.', [(21, 'никак рождаться не хочет')], 'adapted'),
    ('max', 'Алло, Вика, а ты где?', 'Hello, Vika, where are you?', [(22, 'Алло, Вика, а ты где')], 'adapted'),
    ('vika', 'Я сейчас на работе.', 'I am at work right now.', [(23, 'На работе')], 'adapted'),
    ('max', 'Ты разве ещё не рожаешь?', 'Are you not giving birth yet?', [(24, 'не рожаешь')], 'adapted'),
    ('vika', 'Нет, я очень занята.', 'No, I am very busy.', [(24, 'Я занята')], 'adapted'),
    ('max', 'Я сейчас приеду в отель.', 'I am coming to the hotel right now.', [(23, 'На работе')], 'adapted'),
]
WALK = [
    (0, None, "'Hey, put on shoe covers immediately!' The doctor aims the reply right away: spoken Russian trims this down to just 4 words, dropping the extra helper words that English has to spell out."),
    (1, None, "'Vika, is that you here?' Max inquires firmly whether Vika really thought this through."),
    (2, None, '\'No, my name is Masha.\' The doctor points to one loaded touch toward Max: "zovut" means "call" (from "zvat"), giving the line its exact edge.'),
    (3, None, '\'Wait, where is Goncharova?\' Max hands over the comeback beside Vika: putting the question word "gde" right at the front of the line lets Vika hear the point of the question on the very first beat.'),
    (4, None, "'I am Goncharova too.' The doctor fires back wryly on the spot, testing Max's reaction in the middle of the exchange."),
    (5, None, '\'And where is the other Goncharova?\' Max leans on this key element toward Vika: "drugaya" means "different, other" (from "drugoy"), giving the line its exact edge.'),
    (6, None, '\'The baby just does not want to be born yet.\' The doctor drops this warning frankly here: Russian happily doubles the negative here — pairing "never" or "nothing" with "ne" ("not") — which is the only natural way to say it.'),
    (7, None, "'Hello, Vika, where are you?' Max inquires earnestly what Vika is actually getting at here."),
    (8, None, '\'I am at work right now.\' Vika grounds this direct choice with the doctor: "rabote" means "work" (from "rabota"), giving the line its exact edge.'),
    (9, None, '\'Are you not giving birth yet?\' Max gives the remark without fuss: starting the question with "razve" ("really?, is it true that...?") shows Max is pushing back against what he just heard.'),
    (10, None, "'No, I am very busy.' Vika fires back evenly to be clear, letting the remark speak for itself."),
    (11, None, '\'I am coming to the hotel right now.\' Max highlights one colorful term in reply: "seychas" means "now", and it carries the main weight of what Max is saying.'),
]
