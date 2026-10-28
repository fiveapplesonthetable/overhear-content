# Authoring module for kukhnya-s01e17-scene-15.
ID = 'kukhnya-s01e17-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 15
TITLE = 'Билет в клуб  (A Ticket to the Club)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = 'Two scenes are cut together here. Barinov is sitting in the rival restaurant, reading the menu and finding it ridiculous. Back at Claude Monet, Vika asks Max about the kitchen and spots the ticket his friends gave him. Both scenes play in Russian first.'
OPENER = "Let's take both conversations slowly."
TRANSITION = 'Now both conversations again, from start to finish.'
OUTRO = 'Barinov sneers at the menu, and Vika finds a ticket with only one seat. Next time you open a menu, try "nu i chto tut u nas?", so, what have we got? See you next time!'
CLOSING = ('vika', 'Ну, до вечера. Пока!')
STORY = [
    ('barinov', 'Меню уже у нас, большое спасибо.', 'We already have the menu, thank you very much.', [(241, 'Меню есть, спасибо')], ''),
    ('barinov', 'Ну и что тут у нас?', 'So what do we have here?', [(244, 'Ну что тут у нас')], ''),
    ('barinov', 'Тут русская, французская и японская кухня.', 'Here is Russian, French, and Japanese cuisine.', [(245, 'Русская кухня, французская')], ''),
    ('barinov', 'Они называют это всей кухней мира.', 'They call this cuisine from all over the world.', [(247, 'Вся кухня мира')], ''),
    ('barinov', 'Тут есть пицца, суши и борщ.', 'They have pizza, sushi, and borscht here.', [(251, 'Пицца, суши')], ''),
    ('vika', 'Макс, как идут дела на кухне?', 'Max, how are things going in the kitchen?', [(254, 'Как дела')], ''),
    ('max', 'Всё хорошо, мы спокойно работаем.', 'Everything is fine, we are working calmly.', [(255, 'Вот, работаем')], ''),
    ('vika', 'Я придумала блюдо на праздничный ужин.', 'I thought of a dish for the holiday dinner.', [(256, 'приготовить на праздничный ужин')], ''),
    ('max', 'Это просто здорово, большое спасибо тебе.', 'That is simply great, thank you very much.', [(257, 'Здорово')], ''),
    ('vika', 'Подожди, а это что за билет?', 'Wait, what kind of ticket is this?', [(258, 'А это что')], ''),
    ('max', 'Настя и Костя подарили билет в клуб.', 'Nastya and Kostya gave me a ticket to the club.', [(259, 'подарили билет на сегодня в клуб')], ''),
    ('vika', 'Значит, там только один билет?', 'So there is only one ticket there?', [(260, 'Один')], ''),
    ('vika', 'Мне готовить сегодня ужин или нет?', 'Should I cook dinner tonight or not?', [(262, 'мне готовить ужин или нет')], ''),
    ('max', 'Вика, мои друзья меня точно поймут.', 'Vika, my friends will definitely understand me.', [(264, 'они меня поймут')], ''),
]
WALK = [
    (0, None, '\'We already have the menu, thank you very much.\' "Menyu uzhe u nas" is literally "menu already at us", meaning "we have the menu".'),
    (1, None, '\'So what have we got here?\' "Nu i chto tut u nas?" is the standard thing to say as you open a menu or a box.'),
    (2, None, '\'There\'s Russian, French and Japanese cuisine here.\' "Kukhnya" means both kitchen and cuisine. All three words before it end in "-aya" to match.'),
    (3, None, '\'They call this the cuisine of the whole world.\' "Nazyvayut" means "they call". "Vsya kukhnya mira", all the world\'s cuisine, is the restaurant\'s own boast.'),
    (4, None, '\'There\'s pizza, sushi and borscht here.\' "Est" means "there is". "Borshch" is the beet soup, sitting on one menu with pizza and sushi.'),
    (5, None, '\'Max, how are things in the kitchen?\' "Kak idut dela" is literally "how are matters walking". "Na kukhne": "kukhnya" becomes "kukhne" after "na".'),
    (6, None, '\'All good, we\'re working calmly.\' "Spokoyno" means calmly, without any trouble.'),
    (7, None, '\'I\'ve thought of a dish for the holiday dinner.\' "Pridumala", came up with, has the woman\'s "-a" ending. "Prazdnichnyy", festive, comes from "prazdnik", holiday.'),
    (8, None, '\'That\'s just great, thank you so much.\' "Zdorovo", great, is stressed at the start; stress the end and it\'s a slangy "hi".'),
    (9, None, '\'Wait, what\'s this ticket?\' "Chto za bilet" is "what sort of ticket". "Podozhdi" is the friendly "wait".'),
    (10, None, '\'Nastya and Kostya gave me a ticket to the club.\' "Podarili", gave as a present, comes from "podarok". "V klub" keeps "klub" as it is for a destination.'),
    (11, None, '\'So there\'s only one ticket?\' "Odin", one, is the whole point: one ticket, not two.'),
    (12, None, '\'Am I cooking dinner tonight or not?\' "Mne gotovit" is literally "to me to cook", the Russian way to ask "should I...?".'),
    (13, None, '\'Vika, my friends will definitely understand me.\' "Poymut", will understand, comes from "ponyat". "Menya" means "me".'),
]
