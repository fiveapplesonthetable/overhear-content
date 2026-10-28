# Authoring module for kukhnya-s01e11-scene-10.
ID = 'kukhnya-s01e11-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 10
TITLE = 'Подозрительная гостья  (A Suspicious Guest)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "A woman at one of the tables has caught Barinov's attention. He thinks she may be the critic, and he asks Vika to help him decide. Listen for the names and the numbers."
OPENER = "Now we'll pick it apart."
TRANSITION = 'The full thing, one more time.'
OUTRO = 'Vika will find out the truth, whatever it takes. Whether the lady is a critic remains a mystery. Until the next one.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Вика, посмотри на ту даму.', 'Vika, look at that lady.', [], ''),
    ('vika', 'Ну как она себя ведёт?', 'Well, how is she behaving?', [(152, 'как она?')], ''),
    ('barinov', 'Вроде всё совершенно нормально.', 'Everything seems completely fine.', [(152, 'Вроде нормально')], ''),
    ('vika', 'Она долго говорит по телефону.', 'She is talking on the phone for a long time.', [], ''),
    ('barinov', 'Она просто обедает в нашем зале.', 'She is simply dining in our dining room.', [(154, 'Я в Клотмана обедаю')], ''),
    ('vika', 'Но она ничего не ест.', 'But she is not eating anything.', [], ''),
    ('barinov', 'Может быть, блюдо слишком горячее?', 'Maybe the dish is too hot?', [], ''),
    ('vika', 'Она только что попросила счёт.', 'She just asked for the bill.', [], ''),
    ('barinov', 'Она ресторанный критик или нет?', 'Is she a restaurant critic or not?', [(158, 'или нет?')], ''),
    ('vika', 'Мы до сих пор не уверены.', 'We are still not sure.', [], ''),
    ('barinov', 'Нужно срочно выяснить всю правду.', 'We need to urgently find out the whole truth.', [], ''),
    ('vika', 'Я сейчас же всё узнаю, шеф.', 'I will find out everything right now, chef.', [], ''),
]
WALK = [
    (0, None, '\'Vika, look at that lady.\' "Tu damu" is "that lady", both words ending in -u because she is the one being looked at. "Posmotri na" is "look at". Barinov wants a second opinion.'),
    (1, None, '\'Well, how is she behaving?\' "Kak ona sebya vedyot" is literally "how she leads herself". Vika used the same verb with Alisa: "vedi sebya prilichno", "behave decently".'),
    (2, None, '\'Everything seems completely fine.\' "Vrode", at the front, means "kind of" or "seemingly". "Sovershenno normalno" is "completely normal". Barinov is not sure.'),
    (3, None, '\'She is talking on the phone for a long time.\' Russians speak "po telefonu", "by phone". "Dolgo" is "for a long time", the word from the last scene\'s "dolgo govorili".'),
    (4, None, '\'She is simply dining in our dining room.\' "Obedaet", "has lunch", is built on "obed", the midday meal. "V nashem zale" is "in our hall". Barinov argues the other way.'),
    (5, None, '\'But she is not eating anything.\' "Est", "eats", is irregular in Russian. "Nichego ne est" is "nothing not eats", with both negatives. Vika makes a good point.'),
    (6, None, '\'Maybe the dish is too hot?\' "Goryachee", "hot", ends in -ee to match "blyudo", "dish". "Mozhet byt" is "maybe". For Barinov the food is always to blame.'),
    (7, None, '\'She just asked for the bill.\' "Poprosila", "asked for", is a different verb from "sprosit", "ask a question". "Schyot" is the bill, the same word as in "za schyot zavedeniya".'),
    (8, None, '\'Is she a restaurant critic or not?\' "Ili net", "or no", is the blunt Russian tail for "or not". "Restoranny kritik" is "restaurant critic". Barinov wants a yes or a no.'),
    (9, None, '\'We are still not sure.\' "Do sikh por", "up to these times", is the Russian for "still". "Uvereny", "sure", is plural to go with "my", "we".'),
    (10, None, '\'We need to urgently find out the whole truth.\' "Vyyasnit", "find out", grows from "yasny", "clear", so it means "make clear". "Vsyu pravdu" is "the whole truth".'),
    (11, None, '\'I will find out everything right now, chef.\' "Seychas zhe" is "right now", and the little "zhe" adds "this very minute". "Uznayu" is "I will find out".'),
]
