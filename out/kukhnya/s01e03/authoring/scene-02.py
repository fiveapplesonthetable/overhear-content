# Authoring module for kukhnya-s01e03-scene-02.
ID = 'kukhnya-s01e03-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = 'Обед персонала  (Staff Lunch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ainura': 'Айнура', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = 'Staff lunch in the back room. Nastya, the waitress, turns down the meat cutlets, and Ainura, who cleans the kitchen, wants to know why. Nastya explains that she is a vegetarian, and Ainura has a story about hard times. Here is the talk in Russian first.'
OPENER = "Now let's go through the lunch table."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Nastya doesn\'t touch the cutlets, and Ainura has nothing to say to a cow\'s right to life. If you remember anything, take "potomu chto", "because".'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('ainura', 'Настя, почему ты не кушаешь мясо?', 'Nastya, why do you not eat meat?', [(83, 'А почему ты мясо не кушаешь, Тян')], ''),
    ('nastya', 'Потому что я строгая вегетарианка.', 'Because I am a strict vegetarian.', [(84, 'А я вегетарианка')], ''),
    ('ainura', 'Да ты что? А я думала, ты русская.', 'Really? And here I thought you were Russian.', [(85, 'Да ты что, вегетарианка'), (86, 'А это, думала, ты русская')], ''),
    ('nastya', 'Вегетарианцы — это люди, которые не едят мясо.', 'Vegetarians are people who do not eat meat.', [(87, 'Вегетарианцы – это люди, которые мясо не едят')], ''),
    ('ainura', 'Раньше я тоже была вегетарианкой.', 'I used to be a vegetarian too.', [(88, 'Раньше я тоже была вегетариантой')], ''),
    ('nastya', 'Правда? Когда вы не ели мясо?', 'Really? When did you not eat meat?', [], ''),
    ('ainura', 'В девяностые годы совсем не было денег.', 'In the nineties there was no money at all.', [(88, 'в 90-е годы'), (89, 'Денег не было')], ''),
    ('ainura', 'Я целый год ела только картошку.', 'I ate only potatoes for a whole year.', [(89, 'одну картошку ела')], ''),
    ('nastya', 'Я считаю недопустимым убивать животных.', 'I consider killing animals unacceptable.', [(91, 'считаю недопустимым убивать животных')], ''),
    ('ainura', 'Но сочные мясные котлеты такие вкусные!', 'But juicy meat cutlets are so tasty!', [(94, 'вот таких вот сочных')], ''),
    ('nastya', 'Каждая коровка имеет право на жизнь.', 'Every cow has the right to life.', [(92, 'была милая коровка')], ''),
    ('ainura', 'Ой, бай! Ты так красиво рассказываешь!', 'Oh my! You tell stories so beautifully!', [(96, 'Ой, бай! Ты так вкусно рассказываешь')], ''),
    ('nastya', 'Надеюсь, вы меня наконец поняли.', 'I hope you finally understood me.', [], ''),
]
WALK = [
    (0, None, '\'Nastya, why do you not eat meat?\' Ainura says "kushat\'", a soft, homely verb for eating, often used with children. The plain verb is "yest\'". Meat is "myaso".'),
    (1, None, '\'Because I am a strict vegetarian.\' "Potomu chto", because, answers "pochemu", why. In "vegetarianka" the -ka marks a woman; a man would be a "vegetarianets".'),
    (2, None, '\'Really? And here I thought you were Russian.\' "Da ty chto?" is a very Russian "you don\'t say!", word for word "yes, you what?". "Dumala", thought, ends in -la because Ainura is a woman.'),
    (3, None, '\'Vegetarians are people who do not eat meat.\' "Lyudi", people, is the plural of "chelovek", a person. "Kotoryye" is "who", and "ne yedyat" is "do not eat", from the irregular verb "yest\'".'),
    (4, None, '\'I used to be a vegetarian too.\' "Ran\'she", earlier, gives you "used to". After "byla", was, the word changes to "vegetariankoy", the ending Russian uses for "as a".'),
    (5, None, '\'Really? When did you not eat meat?\' Nastya says "vy" to the older Ainura, while Ainura calls her "ty". "Kogda" is "when", and "yeli", ate, has the -li of "vy".'),
    (6, None, '\'In the nineties there was no money at all.\' "V devyanostyye gody" is "in the ninetieth years", how Russians name a decade. "Ne bylo deneg" is "there was not of money": "den\'gi" becomes "deneg" after "ne bylo".'),
    (7, None, '\'I ate only potatoes for a whole year.\' "Tselyy god" is "a whole year". Russian keeps "kartoshka", potato, in the singular for potatoes as food, so it\'s "kartoshku" here.'),
    (8, None, '\'I consider killing animals unacceptable.\' "Zhivotnoye", animal, grows from "zhivoy", alive. "Nedopustimym" is "ne" plus "dopustimyy", permissible, and it takes -ym after "schitayu", I consider.'),
    (9, None, '\'But juicy meat cutlets are so tasty!\' "Sochnyye", juicy, grows out of "sok", juice, and "myasnyye" is "meaty", from "myaso". "Takiye vkusnyye" is "such tasty", plural to match "kotlety".'),
    (10, None, '\'Every cow has the right to life.\' A cow is "korova", and "korovka" makes her small and dear. "Imeyet pravo na zhizn\'" is "has a right to life"; this bookish "imet\'" replaces the usual "u menya yest\'".'),
    (11, None, '\'Oh my! You tell stories so beautifully!\' "Oy, bay!" is a cry of surprise from Ainura\'s homeland. "Krasivo", beautifully, comes from "krasivyy", and "rasskazyvayesh\'" is "you tell".'),
    (12, None, '\'I hope you finally understood me.\' Nastya speaks to the older Ainura as "vy", and "ponyali", understood, has the -li that goes with it. "Nadeyus\'", I hope, is one word, and its -s\' is the short -sya that comes after a vowel.'),
]
