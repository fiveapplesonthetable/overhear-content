# Authoring module for kukhnya-s01e14-scene-04.
ID = 'kukhnya-s01e14-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 4
TITLE = 'Лицо ресторана  (Face of the Restaurant)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = "It's the day of an important dinner, and Chef Barinov is late. Nagiyev, the owner, rings him up in a panic. Here's the phone call in Russian."
OPENER = 'The phone call again, piece by piece.'
TRANSITION = 'Now the call from the start.'
OUTRO = "Barinov is nearly there, or so he says. Two words to keep from this call: 'probki', traffic jams, and 'podyezzhayu', I'm nearly there. Catch you in the next scene."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('nagiyev', 'Витя, ты где? Уже гости собираются.', 'Vitya, where are you? The guests are already arriving.', [(46, 'Алло, Витя, ты где? Уже гости собирается.')], ''),
    ('barinov', 'Алло, Дима, я еду на машине.', 'Hello, Dima, I am driving in the car.', [], ''),
    ('nagiyev', 'Почему ты так сильно опаздываешь сегодня?', 'Why are you so very late today?', [], ''),
    ('barinov', 'Были ужасные пробки на дороге.', 'There were terrible traffic jams on the road.', [], ''),
    ('nagiyev', 'Наш важный клиент уже ждёт тебя.', 'Our important client is already waiting for you.', [], ''),
    ('barinov', 'Скажи им, чтобы они пили вино.', 'Tell them to drink wine.', [], ''),
    ('nagiyev', 'Я уже налил им лучший коньяк.', 'I already poured them the best cognac.', [], ''),
    ('barinov', 'Вот и отлично, пусть отдыхают пока.', 'That is excellent, let them rest for now.', [], ''),
    ('nagiyev', 'Ты должен быть здесь через пять минут!', 'You must be here in five minutes!', [], ''),
    ('barinov', 'Не кричи на меня, я подъезжаю.', 'Do not yell at me, I am almost there.', [(47, 'Я подъезжаю.')], ''),
    ('nagiyev', 'Я жду тебя у главного входа.', 'I am waiting for you at the main entrance.', [], ''),
    ('barinov', 'Иду, иду, уже почти на месте.', 'Coming, coming, I am almost there already.', [], ''),
]
WALK = [
    (0, None, "'Vitya, where are you? The guests are already arriving.' 'Ty gde?' is 'you where?', with no 'are'. 'Sobirayutsya' is 'gather themselves', the usual verb for guests turning up."),
    (1, None, "'Hello, Dima, I am driving in the car.' 'Allo' is only for the phone. 'Dima' is the short form of Dmitry, and Russians travel 'na mashine', literally 'on the car'."),
    (2, None, "'Why are you so very late today?' 'Tak silno' is literally 'so strongly'; 'silno' is the everyday word for 'a lot' or 'badly'. 'Opazdyvaesh' is the 'you' form of 'opazdyvat', to be late."),
    (3, None, "'There were terrible traffic jams on the road.' 'Probka' is a cork, and also a traffic jam, a road corked up with cars. 'Byli', were, is plural to match 'probki'."),
    (4, None, "'Our important client is already waiting for you.' 'Zhdyot tebya', literally 'waits you': Russian 'wait' needs no word for 'for', the person waited for simply changes from 'ty' to 'tebya'."),
    (5, None, "'Tell them to drink wine.' Literally, 'say to them, so that they drank wine'. After 'chtoby', so that, the verb goes into the past form, 'pili', even though nobody has drunk anything yet."),
    (6, None, "'I already poured them the best cognac.' 'Im', to them, is the whole of 'for them' here, no extra word. 'Nalil', poured, is the man's past form; a woman would say 'nalila'."),
    (7, None, "'That is excellent, let them rest for now.' 'Pust' is 'let', and the verb after it is the plain 'they' form, 'pust otdykhayut', 'let they rest'. 'Vot i otlichno' is the stock 'well, that's great then'."),
    (8, None, "'You must be here in five minutes!' 'Dolzhen', must, has the man's form; for a woman it's 'dolzhna'. 'Cherez pyat minut' is literally 'through five minutes', which is how Russians say 'in five minutes'."),
    (9, None, "'Do not yell at me, I am almost there.' You shout 'na' someone, onto them: 'krichat na menya'. 'Podyezzhayu' is 'I'm driving up', with 'pod', under or near, as the prefix for getting close."),
    (10, None, "'I am waiting for you at the main entrance.' 'U', at, takes the 'of' form, so 'glavny vkhod' becomes 'glavnogo vkhoda'. You'll hear 'u vkhoda', at the entrance, in any building."),
    (11, None, "'Coming, coming, I am almost there already.' 'Idu, idu' is the impatient 'coming, coming!' Russians say it even when they're in a car. 'Na meste', literally 'in place', means 'there' or 'arrived'."),
]
