# Authoring module for kukhnya-s01e13-scene-18.
ID = 'kukhnya-s01e13-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 18
TITLE = 'Тайны персонала  (Staff Secrets)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Vika goes back into Max's room, flustered after bumping into Nastya. She is sure that her secret is out, and Max thinks she is overreacting. Listen to their talk in Russian before we go through it."
OPENER = 'Line by line, at a calmer pace.'
TRANSITION = 'Now it all again, from the top.'
OUTRO = 'Max and Vika agree on one thing: she should leave first. Whether the staff are fooled is another matter. Back soon.'
CLOSING = ('vika', 'Увидимся на кухне ресторана, Макс.')
STORY = [
    ('max', 'Почему ты вернулась такая злая?', 'Why did you come back so angry?', [(253, 'А че мы такие злые?')], ''),
    ('vika', 'Настя только что видела меня здесь!', 'Nastya just saw me in here!', [], ''),
    ('max', 'Она просто живёт в этой квартире.', 'She simply lives in this apartment.', [], ''),
    ('vika', 'Ты пригласил сюда весь наш ресторан?', 'Did you invite our whole restaurant here?', [(253, 'А ты бы еще весь персонал к тебе пригласил')], ''),
    ('max', 'По-моему, ты сильно преувеличиваешь сейчас.', 'In my opinion, you are exaggerating greatly now.', [(254, 'По-моему, ты преувеличиваешь')], ''),
    ('vika', 'Моя репутация в ресторане будет разрушена.', 'My reputation at the restaurant will be ruined.', [], ''),
    ('max', 'Настя добрая девушка и умеет молчать.', 'Nastya is a kind girl and knows how to keep quiet.', [], ''),
    ('vika', 'Официанты всегда обсуждают личную жизнь начальства.', "Waiters always discuss the management's personal life.", [], ''),
    ('max', 'Никто не станет обсуждать тебя, успокойся.', 'No one will discuss you, calm down.', [], ''),
    ('vika', 'Я больше никогда не приду сюда.', 'I will never come here again.', [], ''),
    ('max', 'Пожалуй, тебе уже пора на работу.', 'Perhaps it is already time for you to go to work.', [(254, 'пожалуй, тебе пора')], ''),
    ('vika', 'Мы должны выйти из дома раздельно.', 'We must leave the building separately.', [], ''),
    ('max', 'Я согласен, иди первой, Вика.', 'I agree, you go first, Vika.', [], ''),
]
WALK = [
    (0, None, ["'Why did you come back so angry?' Now let's inspect this line: ", ('max', 'вернулась'), " means came back: the woman's ending plus a short self ending. ", ('max', 'такая'), ('max', 'злая'), ' is so angry, and both end to match a woman.']),
    (1, None, ["'Nastya just saw me in here!' We will look at the speech: ", ('vika', 'только'), ('vika', 'что'), ' means just now, and not only what. ', ('vika', 'видела'), " has the woman's ending for Nastya."]),
    (2, None, ["'She simply lives in this apartment.' After in, apartment loses its final vowel and picks up a different ending, so it becomes ", ('max', 'квартире'), '.']),
    (3, None, ["'Did you invite our whole restaurant here?' We will look at this line: ", ('vika', 'весь'), ('vika', 'наш'), ('vika', 'ресторан'), ' is all our restaurant, and all matches the masculine restaurant. Invited, ', ('vika', 'пригласил'), ', ends with a masculine sound for Max.']),
    (4, None, ["'In my opinion, you are exaggerating greatly now.' We can analyze the speech: ", ('max', 'По'), '-', ('max', 'моему'), ' is in my opinion, built like in Russian. ', ('max', 'преувеличиваешь'), ' grows from great.']),
    (5, None, ["'My reputation at the restaurant will be ruined.' Ruined, ", ('vika', 'разрушена'), ', carries a feminine ending as reputation is feminine. ', ('vika', 'будет'), ('vika', 'разрушена'), ' reads will be destroyed.']),
    (6, None, ["'Nastya is a kind girl and knows how to keep quiet.' Let us break down the dialogue: ", ('max', 'умеет'), ' means knows how, so it is about a skill. ', ('max', 'молчать'), ' is to be silent. Max is soothing.']),
    (7, None, ["'Waiters always discuss the management's personal life.' Waiters, ", ('vika', 'Официанты'), ', is in the plural. ', ('vika', 'начальства'), ' is the management as a body, and the ending shows of.']),
    (8, None, ["'No one will discuss you, calm down.' We will inspect this line: ", ('max', 'Никто'), ('max', 'не'), ('max', 'станет'), ('max', 'обсуждать'), ' word-for-word means nobody will not start to discuss, frequent Russian for will not. The calming order, ', ('max', 'успокойся'), ', has a self ending.']),
    (9, None, ["'I will never come here again.' It translates as more never not. The triple negative is correct Russian. ", ('vika', 'приду'), ' is the on-foot kind of come.']),
    (10, None, ["'Perhaps it is already time for you to go to work.' Now we can focus on this line: ", ('max', 'Пожалуй'), ' means perhaps or I suppose, and it softens a suggestion. ', ('max', 'тебе'), ('max', 'пора'), ' says to you time.']),
    (11, None, ["'We must leave the building separately.' Let's consider the dialogue: ", ('vika', 'раздельно'), ' comes from the verb to divide. Out of the house is ', ('vika', 'из'), ('vika', 'дома'), ', with an ending after house.']),
    (12, None, ["'I agree, you go first, Vika.' Let's look at the phrase: ", ('max', 'согласен'), " has a man's bare ending. ", ('max', 'первой'), ' has the ending of a woman, since Vika goes first.']),
]
