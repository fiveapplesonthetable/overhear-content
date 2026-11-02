# Authoring module for kukhnya-s01e09-scene-12.
ID = 'kukhnya-s01e09-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 12
TITLE = 'Поиски Алисы  (Searching for Alisa)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = 'The cake game ended with a lost child. Alisa has vanished from the restaurant, and Barinov and Fedya, the fish cook, are going through every room. Then the phone rings. Let the Russian wash over you first.'
OPENER = 'Time to look at it properly.'
TRANSITION = 'Now, from the top, in one go.'
OUTRO = "Barinov has lied to Tanya, Fedya has been told to get lost, and Alisa is still missing. It gets quieter in the next scene. That's all for now."
CLOSING = ('fedya', 'Пока!')
STORY = [
    ('fedya', 'Шеф, в туалете девочки тоже нет.', 'Chef, the girl is not in the bathroom either.', [(264, 'в туалете тоже нет')], ''),
    ('barinov', 'Где она вообще может быть сейчас?', 'Where can she possibly be right now?', [(267, 'Где она может быть')], ''),
    ('fedya', 'Она точно не выходила из здания ресторана.', 'She definitely did not leave the restaurant building.', [(265, 'она не выходила из здания')], ''),
    ('barinov', 'Ты проверил записи со всех внутренних камер?', 'Did you check recordings from all interior cameras?', [(266, 'на внутренних смотреть')], ''),
    ('fedya', 'Внутренние камеры было приказано отключить утром.', 'The interior cameras were ordered to be turned off this morning.', [(267, 'Внутренние было сказано отключить')], ''),
    ('barinov', 'Какой глупый человек догадался это сделать?', 'What foolish person thought of doing that?', [(268, 'догадался это сказать')], ''),
    ('fedya', 'Вы сами дали такой странный приказ, шеф.', 'You gave such a strange order yourself, Chef.', [(269, 'Вы, шеф')], ''),
    ('barinov', 'Теперь хуже уже точно быть не может.', 'Now it definitely cannot get any worse.', [(270, 'хуже уже быть не может')], ''),
    ('fedya', 'Вам звонит её мама на телефон, шеф.', 'Her mother is calling you on the phone, Chef.', [(271, 'Да нет, может')], ''),
    ('barinov', 'Алло, Таня, у нас с дочкой всё хорошо.', 'Hello, Tanya, everything is fine with our daughter.', [(272, 'да все хорошо'), (273, 'С Алисой хорошо')], ''),
    ('fedya', 'Мы перевернём всю кухню и найдём её!', 'We will turn the whole kitchen upside down and find her!', [(278, 'мы всю каюту вернем, перевернем')], ''),
    ('barinov', 'Пошёл вон отсюда со своими глупыми советами!', 'Get out of here with your foolish advice!', [(280, 'пошел вон отсюда')], ''),
]
WALK = [
    (0, None, ["'Chef, the girl is not in the bathroom either.' Notice how Fedya clarifies the situation using ", ('fedya', 'тоже'), ' to tell us that she is missing from the bathroom in addition to everywhere else.']),
    (1, None, ["'Where can she possibly be right now?' Wondering where she could be right now, Barinov uses ", ('barinov', 'сейчас'), ' for the current moment in time.']),
    (2, None, ["'She definitely did not leave the restaurant building.' Being absolutely certain about her remaining inside, Fedya adds ", ('fedya', 'точно'), ' to mean definitely or for sure.']),
    (3, None, ["'Did you check recordings from all interior cameras?' Making sure no spot was missed, the chef asks about ", ('barinov', 'всех'), ' cameras, meaning all of them.']),
    (4, None, ["'The interior cameras were ordered to be turned off this morning.' Earlier in the day they were disabled, which is why Fedya mentions ", ('fedya', 'утром'), ' to indicate it happened this morning.']),
    (5, None, ["'What foolish person thought of doing that?' Frustrated by the situation, Barinov calls the unknown person ", ('barinov', 'глупый'), ', meaning foolish or incredibly stupid.']),
    (6, None, ["'You gave such a strange order yourself, Chef.' Pointing out the unusual nature of the request, Fedya describes it as ", ('fedya', 'странный'), ' since it was quite bizarre.']),
    (7, None, ["'Now it definitely cannot get any worse.' Thinking things have hit rock bottom, the word ", ('barinov', 'хуже'), ' is used to say that it cannot get any worse.']),
    (8, None, ["'Her mother is calling you on the phone, Chef.' Right on cue, the mother is calling, and ", ('fedya', 'звонит'), ' describes the phone ringing loudly.']),
    (9, None, ["'Hello, Tanya, everything is fine with our daughter.' Picking up the incoming call, Barinov greets the mother with ", ('barinov', 'Алло'), ', a word only used for answering phones.']),
    (10, None, ["'We will turn the whole kitchen upside down and find her!' Promising to search high and low, Fedya vows they will find her, using ", ('fedya', 'найдём'), ' for their future success.']),
    (11, None, ["'Get out of here with your foolish advice!' Furious at his cook, the head chef screams at him to get away from here, using ", ('barinov', 'отсюда'), ' to demand his immediate departure.']),
]
