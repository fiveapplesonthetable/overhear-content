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
    (0, None, '\'Hello! How are things, bartender?\' The guest says "ty" to the bartender, casual and friendly, since he has been drinking here. "Barmen" is "barman" in Russian letters. And "how your affairs" is the usual opening.'),
    (1, None, '\'Hello! How are you feeling today?\' Kostya answers politely, with "vy". Russian says "how yourself you feel", with a separate little word for "yourself". It\'s the same idea as the -sya ending.'),
    (2, None, '\'Ugh, today I feel worse than yesterday.\' This is the "than" word, which is used when the comparison is not a plain noun. "Worse" is a short, irregular form. The guest groans. He had too much last night.'),
    (3, None, '\'Did you happen to find my phone?\' "By chance" is built from the root of "happen". It\'s a polite way to ask. The guest hopes Kostya has seen it, and he looks around the bar as he says so.'),
    (4, None, '\'Yes, I found it near the counter.\' The counter of a bar is a word related to "stand". Kostya is helpful, as always. "Near" and "of the counter" give the position, the ending on "counter" doing the "of".'),
    (5, None, '\'Huge thanks for the help, friend!\' "Huge thank-you" is the usual Russian for "thanks a lot". "For help" is two small words. The guest is relieved, because losing a phone is no joke.'),
    (6, None, '\'Tell me honestly, did my girlfriend not call?\' The term for "girl" also means "girlfriend", so context decides. "Say honestly" is two short words. The guest asks nervously, because he has been waiting for a call.'),
    (7, None, '\'No, no one has called here yet.\' Notice how the little word that means "while" and "bye for now" also means "yet" here. "Nobody not rang" is a double negative. Kostya says it kindly.'),
    (8, None, '\'She has not returned from Saratov yet.\' "Saratov" is a city on a big river, and "from" shows in the ending. "Still not returned" ends in -las, since the woman is the one who has not returned. The guest has an explanation ready.'),
    (9, None, '\'Yesterday you spoke about her for a long time.\' "For a long time" is one word. And "about her" gets an extra "n" at the start of "her", as Russian does after small words. Kostya reminds him of yesterday\'s confession.'),
    (10, None, '\'Yes, my memory is slowly returning to me.\' The -sya on "returns" gives "returns itself". The guest is piecing last night together slowly. His memory comes back the way a tide does.'),
    (11, None, '\'Here is a drink for you on the house.\' Russian says "at the expense of the establishment". What Russian calls expense equals the score and the bill. Kostya treats the poor man to a drink.'),
    (12, None, '\'Thank you for your kindness, buddy!\' The word for "buddy" is "friend" with a big, warm ending, something like "old pal". "Kindness" comes from the Russian for "kind". The guest says it with real feeling.'),
]
