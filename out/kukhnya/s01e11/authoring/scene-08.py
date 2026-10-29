# Authoring module for kukhnya-s01e11-scene-08.
ID = 'kukhnya-s01e11-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 8
TITLE = 'Потерянный телефон  (The Lost Phone)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = 'At the bar, a customer arrives who has been there before. He is hungover, looking for his phone, and Kostya is the person he asks. The Russian comes first.'
OPENER = "We'll take it a bit at a time."
TRANSITION = 'And again, the whole conversation.'
OUTRO = 'The phone is found, and the customer has a drink on the house. Kostya has a kind heart, and he is about to be rewarded for it. On to the next.'
CLOSING = ('guest', 'Пока!')
STORY = [
    ('guest', 'Привет! Как твои дела, бармен?', 'Hello! How are things, bartender?', [(100, 'Здрасте.')], ''),
    ('kostya', 'Здравствуйте! Как вы себя сегодня чувствуете?', 'Hello! How are you feeling today?', [(101, 'Как себя чувствуете?')], ''),
    ('guest', 'Эх, сегодня мне хуже, чем вчера.', 'Ugh, today I feel worse than yesterday.', [(101, 'Эх, хуже, чем вчера.')], ''),
    ('guest', 'Ты случайно не находил мой телефон?', 'Did you happen to find my phone?', [(102, 'Ты мой телефон не находил?')], ''),
    ('kostya', 'Да, я нашёл его возле стойки.', 'Yes, I found it near the counter.', [(103, 'Находил.')], ''),
    ('guest', 'Огромное спасибо за помощь, друг!', 'Huge thanks for the help, friend!', [(103, 'О, спасибо.')], ''),
    ('guest', 'Скажи честно, моя девушка не звонила?', 'Tell me honestly, did my girlfriend not call?', [(104, 'Она не звонила?')], ''),
    ('kostya', 'Нет, сюда пока никто не звонил.', 'No, no one has called here yet.', [(104, 'Нет.')], ''),
    ('guest', 'Она ещё не вернулась из Саратова.', 'She has not returned from Saratov yet.', [(105, 'Наверное, еще не вернулась из Саратова.')], ''),
    ('kostya', 'Вы вчера долго говорили про неё.', 'Yesterday you spoke about her for a long time.', [(107, 'Ну, вы же мне вчера рассказывали.')], ''),
    ('guest', 'Да, память медленно возвращается ко мне.', 'Yes, my memory is slowly returning to me.', [(108, 'Да.')], ''),
    ('kostya', 'Вот вам напиток за счёт заведения.', 'Here is a drink for you on the house.', [(110, 'За счет заведения.')], ''),
    ('guest', 'Спасибо тебе за доброту, дружище!', 'Thank you for your kindness, buddy!', [(111, 'Спасибо тебе, дружище.')], ''),
]
WALK = [
    (0, None, '\'Hello! How are things, bartender?\' The guest says "ty" to the bartender: "kak tvoi dela", "how your affairs". "Barmen" is "barman" in Russian letters. He has been drinking here before.'),
    (1, None, '\'Hello! How are you feeling today?\' Kostya answers politely, with "vy". Russian says "kak vy sebya chuvstvuete", "how you yourself feel", where "sebya" is "yourself".'),
    (2, None, '\'Ugh, today I feel worse than yesterday.\' "Khuzhe, chem vchera" is "worse than yesterday", with "chem" for "than". "Khuzhe" is an irregular form of "plokho", "bad". "Mne khuzhe" is "to me worse".'),
    (3, None, '\'Did you happen to find my phone?\' Asking with "ne", "didn\'t you by chance find", makes the question softer, not negative. "Sluchayno", "by chance", is built on "sluchay", "a case" or "an occasion".'),
    (4, None, '\'Yes, I found it near the counter.\' "Stoyka", "counter", is related to "stoyat", "to stand". "Vozle stoyki" is "near the counter". "Nashyol" is "I found".'),
    (5, None, '\'Huge thanks for the help, friend!\' "Ogromnoe spasibo", "huge thanks", is the usual "thanks a lot". "Za pomoshch" is "for the help", and "drug" is "friend".'),
    (6, None, '\'Tell me honestly, did my girlfriend not call?\' "Devushka" is "girl" and also "girlfriend", so context decides. "Skazhi chestno" is "tell honestly". "Ne zvonila" is "didn\'t call".'),
    (7, None, '\'No, no one has called here yet.\' "Poka" is the word for "bye", and it also means "for now" or "yet". "Nikto ne zvonil" is "nobody not called", with both negatives. "Syuda" is "to here".'),
    (8, None, '\'She has not returned from Saratov yet.\' "Saratov" is a city on the "Volga", and "from Saratov" is "iz Saratova". "Eshchyo ne vernulas", "not yet returned", ends in -las for a woman.'),
    (9, None, '\'Yesterday you spoke about her for a long time.\' "Dolgo", "for a long time", is one word. "Pro neyo" is "about her", where "eyo" picks up an n- after "pro".'),
    (10, None, '\'Yes, my memory is slowly returning to me.\' "Vozvrashchaetsya" is "returns", with -sya, "returns itself". "Pamyat" is "memory", and "ko mne" is "to me".'),
    (11, None, '\'Here is a drink for you on the house.\' "Za schyot zavedeniya" is "at the expense of the establishment". "Schyot" also means "bill" and "score". "Vot vam napitok" is "here for you a drink".'),
    (12, None, '\'Thank you for your kindness, buddy!\' "Drugishche" is "drug", "friend", with a big warm ending: "old pal". "Dobrota", "kindness", comes from "dobry", "kind".'),
]
