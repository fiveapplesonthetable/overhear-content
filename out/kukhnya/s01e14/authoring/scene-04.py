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
INTRO = "It's the day of an important dinner, and Chef Barinov is late. Nagiyev, the owner, rings him up in a panic. Here is the phone call."
OPENER = 'The phone call again, piece by piece.'
TRANSITION = 'Now the call from the start.'
OUTRO = "Barinov is nearly there, or so he says. Two phrases to keep from this call: 'traffic jams', and 'I am nearly there'. Catch you in the next scene."
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
    (0, None, ["'Vitya, where are you? The guests are already arriving.' Now let's analyze the speech: ", ('nagiyev', 'ты'), ('nagiyev', 'где'), " asks 'you where?', with no 'are'. ", ('nagiyev', 'собираются'), " means 'gather themselves', the usual action for guests turning up."]),
    (1, None, ["'Hello, Dima, I am driving in the car.' Now let's break down the phrase: ", ('barinov', 'Алло'), ' is only for the phone. People travel ', ('barinov', 'на'), ('barinov', 'машине'), ", reading as 'on the car'."]),
    (2, None, ["'Why are you so very late today?' Now let's examine this part: ", ('nagiyev', 'так'), ('nagiyev', 'сильно'), " reads as 'so strongly', using the everyday word for 'a lot' or 'badly'. ", ('nagiyev', 'опаздываешь'), ' is the action form for being late.']),
    (3, None, ["'There were terrible traffic jams on the road.' A ", ('barinov', 'пробки'), ' is a traffic jam, originally meaning corks on a corked-up road. ', ('barinov', 'Были'), ", meaning 'were', is plural to match it."]),
    (4, None, ["'Our important client is already waiting for you.' We will inspect the sentence: ", ('nagiyev', 'ждёт'), ('nagiyev', 'тебя'), " reads as 'waits you', omitting 'for' and changing the form of the person waited for."]),
    (5, None, ["'Tell them to drink wine.' This reads as 'say to them, so that they drank wine'. After ", ('barinov', 'чтобы'), ", meaning 'so that', the action takes the past form ", ('barinov', 'пили'), ', even though nobody has drunk anything yet.']),
    (6, None, ["'I already poured them the best cognac.' Let us inspect this line: ", ('nagiyev', 'им'), ", meaning 'to them', is all that is needed for 'for them'. ", ('nagiyev', 'налил'), ", meaning 'poured', is the masculine past form."]),
    (7, None, ["'That is excellent, let them rest for now.' Let us break down the words: ", ('barinov', 'пусть'), " is 'let', followed by the plain 'they' action ", ('barinov', 'отдыхают'), ", reading as 'let they rest'. ", ('barinov', 'Вот'), ('barinov', 'и'), ('barinov', 'отлично'), " is the standard phrase for 'well, that is great then'."]),
    (8, None, ["'You must be here in five minutes!' We can analyze the sentence: ", ('nagiyev', 'должен'), ", meaning 'must', has a masculine form. ", ('nagiyev', 'через'), ('nagiyev', 'пять'), ('nagiyev', 'минут'), " reads as 'through five minutes', which is how you say 'in five minutes'."]),
    (9, None, ["'Do not yell at me, I am almost there.' You shout onto someone, making it ", ('barinov', 'на'), ('barinov', 'меня'), '. ', ('barinov', 'подъезжаю'), " means 'I am driving up', using a prefix for getting close."]),
    (10, None, ["'I am waiting for you at the main entrance.' We can consider the dialogue: ", ('nagiyev', 'у'), ('nagiyev', 'главного'), ('nagiyev', 'входа'), " reads as 'at the main entrance', taking a special ending. You will hear 'at the entrance' in any building."]),
    (11, None, ["'Coming, coming, I am almost there already.' Now we can focus on the speech: ", ('barinov', 'Иду'), ', ', ('barinov', 'Иду'), " is the impatient 'coming, coming!' used even when in a car. ", ('barinov', 'на'), ('barinov', 'месте'), ", reading as 'in place', means 'there' or 'arrived'."]),
]
