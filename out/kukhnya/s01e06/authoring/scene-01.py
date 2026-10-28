# Authoring module for kukhnya-s01e06-scene-01.
ID = 'kukhnya-s01e06-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 1
TITLE = 'Путь на тарелку  (The Journey to the Plate)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Kukhnya means The Kitchen. It's a Russian comedy about Claude Monet, a smart Moscow restaurant where the chef, Barinov, rules the kitchen and everyone else survives as best they can. This is from episode six. Before the evening rush, Max, the young cook, and Kostya, the bartender he shares a flat with, look out at the guests and talk about what they never see. You'll hear it in Russian first, and it's fine to miss words."
OPENER = "Now slowly. It's a calm scene, so the sentences are short and nearly all of them are worth keeping."
TRANSITION = 'Here it is again in one go. It should feel more familiar now.'
OUTRO = 'Keep "kazhdyy vecher", every evening, and "kazhdoe blyudo", every dish: one word for \'every\', with its ending changed to fit. See you next time.'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Макс, посмотри на гостей в зале.', 'Max, look at the guests in the dining room.', [], ''),
    ('max', 'Они заказывают наши фирменные блюда.', 'They are ordering our specialty dishes.', [(1, 'заказываете любимое блюдо')], ''),
    ('kostya', 'Люди приходят сюда каждый вечер.', 'People come here every evening.', [(1, 'Когда вы приходите в ресторан')], ''),
    ('max', 'Каждый выбирает своё любимое блюдо.', 'Everyone chooses their favorite dish.', [(1, 'любимое блюдо')], ''),
    ('kostya', 'Они не думают о пути еды.', "They do not think about the food's journey.", [(2, 'вы наверняка не задумываетесь, какой путь')], ''),
    ('max', 'Какое блюдо проходит длинный путь?', 'Which dish travels a long way?', [(2, 'путь оно проделывает')], ''),
    ('kostya', 'Каждое блюдо начинает путь на рынке.', 'Every dish begins its journey at the market.', [(3, 'чтобы оказаться у вас на тарелке')], ''),
    ('max', 'Потом повара готовят заказ на кухне.', 'Then the cooks prepare the order in the kitchen.', [], ''),
    ('kostya', 'Вся кухня работает ради одной тарелки.', 'The whole kitchen works for one plate.', [], ''),
    ('max', 'Повара очень спешат и нервничают.', 'The cooks rush very much and get nervous.', [], ''),
    ('kostya', 'А гости видят только вкусный результат.', 'And guests only see the delicious result.', [], ''),
    ('max', 'Для них это настоящий праздник вкуса.', 'For them this is a real celebration of taste.', [], ''),
    ('kostya', 'Скоро начнётся наш обычный рабочий вечер.', 'Soon our usual working evening will begin.', [], ''),
]
WALK = [
    (0, None, '\'Max, look at the guests in the dining room.\' "Posmotri" is the friendly \'look\', the one you\'d say to a mate. Russian looks \'on\' things, "na gostey", and the hall, "zal", becomes "v zale" when it\'s where something is.'),
    (1, None, '\'They are ordering our specialty dishes.\' "Firmennye" comes from "firma", a company, so "firmennoe blyudo" is the house\'s own dish. You\'ll see that phrase on Russian menus.'),
    (2, None, '\'People come here every evening.\' "Lyudi", people, has nothing to do with the word for one person, chelovek. And "kazhdyy vecher", every evening, needs no \'on\' or \'in\' in front of it.'),
    (3, None, '\'Everyone chooses their favorite dish.\' "Lyubimoe", favourite, grows from "lyubit", to love, so it\'s literally \'the loved dish\'. "Svoyo" means \'their own\' and always points back to whoever is doing the choosing.'),
    (4, None, '\'They do not think about the food\'s journey.\' "Eda", food, turns into "edy" to mean \'of food\', so "o puti edy" is \'about the journey of food\' with no word for \'of\' anywhere.'),
    (5, None, '\'Which dish travels a long way?\' "Kakoe", which, takes the same -oe ending as "blyudo". "Prokhodit" is \'goes through\', from pro-, through, and "khodit", to walk.'),
    (6, None, '\'Every dish begins its journey at the market.\' "Kazhdoe" ends in -oe here because "blyudo" does; a line earlier it was "kazhdyy vecher". And a market is something you\'re \'on\', not \'in\': "na rynke".'),
    (7, None, '\'Then the cooks prepare the order in the kitchen.\' One cook is "povar", several are "povara", with a stressed -a instead of the usual -y. The kitchen, like the market, takes "na": "na kukhne".'),
    (8, None, '\'The whole kitchen works for one plate.\' "Radi" means \'for the sake of\', and it changes what follows: "odna tarelka", one plate, becomes "radi odnoy tarelki".'),
    (9, None, '\'The cooks rush very much and get nervous.\' "Nervnichat", to be nervous, is built on "nerv", nerve, so it\'s a word you can almost guess. Both verbs end in the \'they\' ending, -at and -ayut.'),
    (10, None, '\'And guests only see the delicious result.\' "Vkusnyy", delicious, comes from "vkus", taste, which you\'ll hear again in the next line. "Rezultat" is just \'result\' said the Russian way.'),
    (11, None, '\'For them this is a real celebration of taste.\' "Dlya nikh" is \'for them\'; after a little word like "dlya", \'them\' picks up an extra n at the front. "Prazdnik" is also what Russians call a public holiday.'),
    (12, None, '\'Soon our usual working evening will begin.\' "Nachnyotsya", will begin, is a single verb with the future built in. "Rabochiy vecher", a working evening, takes "rabochiy" from "rabota", work.'),
]
