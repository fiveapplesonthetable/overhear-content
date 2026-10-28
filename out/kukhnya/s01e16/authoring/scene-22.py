# Authoring module for kukhnya-s01e16-scene-22.
ID = 'kukhnya-s01e16-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 22
TITLE = 'Мой долг  (My duty)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'The inspector comes back to the kitchen for Fedya. Barinov makes one last try, but the inspector has made up his mind, and he even apologises for it.'
OPENER = "Now we'll take it apart."
TRANSITION = 'Now all of it together again, from the top.'
OUTRO = "Fedya is led away, and the kitchen is a cook short. Remember that 'dolg' means both 'duty' and 'debt': a duty is something you owe. See you next time!"
CLOSING = ('fedya', 'До свидания!')
STORY = [
    ('inspector', 'Собирайтесь.', 'Pack your things.', [(285, 'Собирайтесь.')], ''),
    ('fedya', 'Куда?', 'Where to?', [], ''),
    ('inspector', 'Домой, в Молдову.', 'Home, to Moldova.', [], ''),
    ('barinov', 'Неужели ничего нельзя сделать?', 'Is there really nothing to be done?', [], ''),
    ('inspector', 'Извините, это мой долг.', "I'm sorry, it's my duty.", [(286, 'Извините, это мой долг.')], ''),
    ('fedya', 'Шеф, мне очень жаль.', "Chef, I'm really sorry.", [], ''),
    ('barinov', 'Ты ни в чём не виноват.', "It's not your fault at all.", [], ''),
    ('fedya', 'Я ещё вернусь.', "I'll be back.", [], ''),
]
WALK = [
    (0, None, "'Pack your things.' 'Sobiraytes' is literally 'gather yourselves': '-sya' means 'oneself' and '-te' makes it polite. It also means 'get ready to go'."),
    (1, None, "'Where to?' Russian has two words for 'where': 'gde' for a place and 'kuda' for a direction. Fedya asks 'kuda', 'where to'."),
    (2, None, "'Home, to Moldova.' 'Domoy' already means 'to home', so it needs no preposition. 'V Moldovu', 'to Moldova', has the '-u' ending for movement into a place."),
    (3, None, "'Is there really nothing to be done?' 'Neuzheli' means 'can it really be', a word of disbelief. 'Nichego nelzya sdelat', 'nothing can be done', is a stock phrase."),
    (4, None, "'I'm sorry, it's my duty.' 'Izvinite' is the polite 'excuse me' or 'I'm sorry'. 'Dolg' means 'duty', and the same word means 'debt'."),
    (5, None, "'Chef, I'm really sorry.' 'Mne zhal' is literally 'to me it is a pity', so the feeling happens to you. 'Ochen' means 'very'."),
    (6, None, "'It's not your fault at all.' 'Ni v chyom ne vinovat' is literally 'not guilty in anything'. Russian stacks 'ni' and 'ne' in one sentence, and that's correct."),
    (7, None, "'I'll be back.' 'Vernus' means 'I will return', from 'vernutsya', 'to come back'. 'Eshchyo', 'yet' or 'still', adds 'you haven't seen the last of me'."),
]
