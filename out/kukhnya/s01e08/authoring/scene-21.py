# Authoring module for kukhnya-s01e08-scene-21.
ID = 'kukhnya-s01e08-scene-21'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 21
TITLE = 'Строгие порядки  (Strict Orders)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'elena': 'Елена', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Back in the kitchen at Claude Monet, Elena Pavlovna, borrowed from a rival restaurant, is in charge while Barinov sulks. The cooks want a smoke break, the way they had under Barinov. Lyova, the sous-chef, asks for one, and Elena says no. Here it is in Russian first."
OPENER = "Let's go through the standoff. Lyova stays polite, and Elena doesn't give an inch."
TRANSITION = "Now the full exchange without stopping."
OUTRO = "Lyova gets the last word in spirit: \"ya su-shef, a ne kurer\", I'm a sous-chef, not a courier. Then he goes to fetch the arugula anyway. See you next time."
CLOSING = ('elena', 'Пока!')
STORY = [
    ('lyova', 'Шеф, можно поварам выйти перекурить?', 'Chef, can the cooks go smoke?', [(241, 'Шеф, мы перекурить')], ''),
    ('elena', 'Вы в своём уме? Заказов полно!', 'Are you mad? Plenty of orders!', [(242, 'Вы в своем уме')], ''),
    ('lyova', 'Но по мясу сейчас чеков нет.', 'But there are no meat orders now.', [(244, 'По мясу ни одного чека нет')], ''),
    ('elena', 'Значит, быстро переходите на курицу!', 'Then quickly switch over to poultry!', [(245, 'Значит, переходи на курицу')], ''),
    ('lyova', 'Повара очень устали от этой работы.', 'The cooks are very tired from this work.', [], ''),
    ('elena', 'Никаких перекуров, все остаются на кухне!', 'No smoke breaks, everyone stays in the kitchen!', [(246, 'никаких перекурок')], ''),
    ('lyova', 'Вы слишком строги с нашей командой.', 'You are too strict with our team.', [], ''),
    ('elena', 'Мне нужно, чтобы вы отлично работали!', 'I need you to work excellently!', [(249, 'А мне нужно, чтобы вы работали')], ''),
    ('lyova', 'На кухне закончилась свежая рукола.', 'The kitchen has run out of fresh arugula.', [(251, 'Так, у нас закончилась рукола')], ''),
    ('elena', 'Лёва, быстро принесите руколу со склада!', 'Lyova, quickly bring arugula from the storeroom!', [(252, 'Лев, принесите, пожалуйста, руколу со склада')], ''),
    ('lyova', 'Я су-шеф, а не курьер!', 'I am a sous-chef, not a courier!', [(255, 'А вообще-то я здесь суша')], ''),
    ('elena', 'Я сама решаю, кто пойдёт туда!', 'I decide myself who will go there!', [(257, 'я буду решать, кто пойдет')], ''),
    ('lyova', 'Хорошо, шеф, я принесу эту зелень.', 'Fine, Chef, I will bring this greenery.', [], ''),
]
WALK = [
    (0, None, "'Chef, can the cooks go smoke?' Permission with \"mozhno\" is asked 'to' someone, so \"povara\", cooks, becomes \"povaram\". Inside \"perekurit\" sits \"kurit\", to smoke, with \"pere-\" added: a quick smoke break."),
    (1, None, "'Are you mad? Plenty of orders!' Elena's question, \"vy v svoyom ume\", is literally 'are you in your own mind?' After \"polno\", plenty, orders come out as \"zakazov\", 'of orders'."),
    (2, None, "'But there are no meat orders now.' In kitchen talk, \"po myasu\" means 'on the meat side'. A \"chek\" is the printed order ticket, and after \"net\", there are no, it becomes \"chekov\"."),
    (3, None, "'Then quickly switch over to poultry!' Literally 'it means', \"znachit\" is the everyday 'so' or 'then'. To switch to something is \"perekhodit na\": the chicken, \"kuritsa\", becomes \"na kuritsu\"."),
    (4, None, "'The cooks are very tired from this work.' Lyova says \"ustali\", which looks past: Russians say they 'got tired' and still are. Tired of something is \"ustat ot\", so the work becomes \"etoy raboty\"."),
    (5, None, "'No smoke breaks, everyone stays in the kitchen!' The phrase \"nikakikh perekurov\", no smoke breaks of any kind, is how Russian makes a flat ban. Kitchens take \"na\", on, so it's \"na kukhne\"."),
    (6, None, "'You are too strict with our team.' Lyova says \"strogi\", a shortened \"strogiy\", the shape Russians use for what someone is like right now. With the team is \"s nashey komandoy\", and that -oy ending is what \"s\", with, asks for."),
    (7, None, "'I need you to work excellently!' To want someone else to do something, Russian says \"chtoby\" plus a past-looking form: \"chtoby vy rabotali\". And \"mne nuzhno\" is literally 'to me it is needed'."),
    (8, None, "'The kitchen has run out of fresh arugula.' Literally 'finished itself': \"zakonchilas\" is what Russians say when something has run out. Because \"rukola\" is a 'she' word, it ends in -as to match."),
    (9, None, "'Lyova, quickly bring arugula from the storeroom!' Elena says \"prinesite\", the polite 'bring', even to her own staff. In \"so sklada\", from the storeroom, the \"so\" is \"s\", from, with an extra o before a tricky cluster of consonants."),
    (10, None, "'I am a sous-chef, not a courier!' There's no 'am' at all, just \"ya su-shef\". And \"a ne\" means 'and not', the usual way to say 'this, not that'."),
    (11, None, "'I decide myself who will go there!' Elena says \"sama\", myself, as a woman; a man would say \"sam\". The word \"tuda\", to there, is for movement, the partner of \"syuda\", to here."),
    (12, None, "'Fine, Chef, I will bring this greenery.' Lyova's \"prinesu\" means 'I will bring', a promise about later. And \"zelen\", greens, comes from \"zelyonyy\", green."),
]
