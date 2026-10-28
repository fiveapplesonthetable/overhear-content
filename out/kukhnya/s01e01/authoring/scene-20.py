# Authoring module for kukhnya-s01e01-scene-20.
ID = 'kukhnya-s01e01-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 20
TITLE = 'Шанс для новичка  (A Chance for the Newcomer)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = 'Max has been given a first job: peeling stickers off bananas. He tries to pitch his chicken in cream sauce to the chef, who laughs at him, and then, unexpectedly, gives him a test: a dessert for an important guest. Here it is in Russian first.'
OPENER = "Let's go back over the pitch."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'So Max has his chance, and a dessert to make for Eleonora Andreyevna, who is a regular at the restaurant. You can now say "I can cook" and "I have an idea".'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Шеф, у меня есть отличная идея.', 'Chef, I have an excellent idea.', [(218, 'есть идея')], ''),
    ('max', 'Я могу приготовить своё фирменное блюдо.', 'I can prepare my signature dish.', [(219, 'Мое фирменное блюдо')], ''),
    ('max', 'Это нежная курица в сливочном соусе.', 'It is tender chicken in cream sauce.', [(219, 'Курица в сливочном соусе')], ''),
    ('barinov', 'Великолепная идея от неизвестного человека.', 'A magnificent idea from an unknown person.', [(221, 'Супер идея')], ''),
    ('barinov', 'Ты пришёл на мою кухню случайно.', 'You came to my kitchen by accident.', [(222, 'попавший случайно')], ''),
    ('barinov', 'Лучше чисти бананы дальше!', 'Better keep peeling bananas!', [(225, 'Тащи еще пять ящиков бананов')], ''),
    ('max', 'Зачем вообще снимать эти наклейки?', 'Why peel off these stickers at all?', [(228, 'Нафига вообще отклеивать эти этикетки')], ''),
    ('barinov', 'Для идеального порядка во вселенной.', 'For ideal order in the universe.', [(229, 'Для баланса вселенной')], ''),
    ('max', 'Но я умею готовить прекрасные десерты.', 'But I know how to prepare wonderful desserts.', [(232, 'умеет офигенно готовить')], ''),
    ('barinov', 'Хорошо, я дам тебе один шанс.', 'All right, I will give you one chance.', [(233, 'Хорошо. Я дам тебе шанс')], ''),
    ('barinov', 'К нам пришёл наш постоянный гость.', 'Our regular guest has arrived.', [(234, 'У нас есть постоянный клиент')], ''),
    ('barinov', 'Ты приготовишь десерт для Элеоноры Андреевны.', 'You will prepare dessert for Eleonora Andreyevna.', [(235, 'Приготовишь для него десерт'), (237, 'Элеонора Андреевна')], ''),
    ('barinov', 'Если десерт понравится, ты останешься здесь.', 'If the dessert is liked, you will stay here.', [(238, 'Вот если ты сможешь угодить')], ''),
    ('max', 'Договорились, шеф! Я сделаю лучший десерт.', 'Agreed, chef! I will make the best dessert.', [(240, 'Окей'), (241, 'Ну, держитесь')], ''),
]
WALK = [
    (0, None, '\'Chef, I have an excellent idea.\' "U menya yest\'" is "at me there is", the full form of "I have". Earlier it was just "u menya dela", with "yest\'" left out.'),
    (1, None, '\'I can prepare my signature dish.\' "Mogu" is "I can". "Firmennoye" comes from "firma", company, so a "firmennoye blyudo" is the house\'s own dish.'),
    (2, None, '\'It is tender chicken in cream sauce.\' "Nezhnaya" is "tender", and "kuritsa" is "chicken". "Slivochnyy" comes from "slivki", cream, and "v souse" is "in the sauce".'),
    (3, None, '\'A magnificent idea from an unknown person.\' "Velikolepnaya" has "velikiy", great, inside it. "Neizvestnogo" is "ne" plus "izvestnyy", known, so "unknown". Praise this big from Barinov is a joke at Max\'s expense.'),
    (4, None, '\'You came to my kitchen by accident.\' "Sluchayno" comes from "sluchay", chance, which is also in "chto sluchilos\'", "what happened". "Na moyu kukhnyu" is "to my kitchen".'),
    (5, None, '\'Better keep peeling bananas!\' "Luchshe" is "better", used as "you\'d better". "Chisti" is the command "peel", from "chistyy", clean. "Dal\'she" is "further", meaning "keep going".'),
    (6, None, '\'Why peel off these stickers at all?\' "Zachem" is "what for". "Snimat\'" is "to take off", the everyday partner of "snimu" from the stove. "Nakleyki" are stickers, from "kleit\'", to glue.'),
    (7, None, '\'For ideal order in the universe.\' "Poryadok" is "order", the word from "keep order on your table". "Vo vselennoy" is "in the universe": "v" becomes "vo" before a heavy cluster like "vs", just to make it sayable.'),
    (8, None, '\'But I know how to prepare wonderful desserts.\' "No" is the plain "but", different from "a". "Prekrasnyye deserty" is plural, so the describing word ends in "-ye".'),
    (9, None, '\'All right, I will give you one chance.\' "Dam" is "I will give", irregular and short. "Tebe" is "to you", the friendly form.'),
    (10, None, '\'Our regular guest has arrived.\' "Postoyannyy" means "regular", and its partner "postoyanno" means "constantly". "K nam prishyol" is "has come to us".'),
    (11, None, '\'You will prepare dessert for Eleonora Andreyevna.\' Names change after "dlya", even the father\'s name: "Eleonora" becomes "Eleonory", and "Andreyevna" becomes "Andreyevny".'),
    (12, None, '\'If the dessert is liked, you will stay here.\' "Ponravitsya" is "will please", the future of "nravit\'sya". "Ostanyosh\'sya" is "you will stay", the "self" ending included.'),
    (13, None, '\'Agreed, chef! I will make the best dessert.\' "Dogovorilis\'!" is the everyday "deal!", the finished partner of "dogovarivalis\'" from the morning after. "Luchshiy" already means "best", with no need for "very".'),
]
