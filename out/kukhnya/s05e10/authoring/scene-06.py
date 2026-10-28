# Authoring module for kukhnya-s05e10-scene-06.
ID = 'kukhnya-s05e10-scene-06'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 10
SCENE = 6
TITLE = 'Нагиев в люксе  (Nagiyev in the Suite)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'inspector': 'Инспектор', 'mikhail': 'Михаил', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.10'
SOURCE_FILE = 'sources/kukhnya/s05/e10.ru.srt'
INTRO = 'Inside the luxury suite, drunk Nagiyev has been hiding out and drinking with the bellboy. When the commission walks in, Nagiyev happily offers to give them a tour of the soft sofas while Mikhail desperately tries to hustle the inspectors out the door.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That brings the chaotic suite visit to a close. Listen for how Mikhail apologizes for disturbing the guest and tries to cover for Nagiyev's behavior. See you next time!"
CLOSING = ('mikhail', 'Пока!')
STORY = [
    ('mikhail', 'Извините, что мы вас побеспокоили.', 'Excuse us for disturbing you.', [(93, 'Извините, что мы вас побеспокоили')], 'adapted'),
    ('mikhail', 'Комиссия в отеле. Мы сейчас уходим.', 'The commission is in the hotel. We are leaving right now.', [(94, 'Комиссия в отеле. Мы сейчас уходим')], 'adapted'),
    ('nagiyev', 'О, комиссия! Так я вам сейчас всё покажу.', 'Oh, the commission! Well I will show you everything right now.', [(95, 'О, комиссия'), (96, 'Так я вам сейчас все покажу')], 'adapted'),
    ('nagiyev', 'Вот диванчики мягкие.', 'Here the little sofas are soft.', [(97, 'Вот диванчики')], 'adapted'),
    ('nagiyev', 'Ой, только он пустой.', 'Oh, only it is empty.', [(99, 'Ой, только он пустой')], 'adapted'),
    ('mikhail', 'Да, пойдёмте.', 'Yes, let us go.', [(100, 'Да, пойдемте')], 'adapted'),
    ('nagiyev', 'Пойдём. Ну, куда вы уходите?', 'Let us go. Well, where are you going?', [(101, 'Пойдем. Ну, куда вы уходите')], 'adapted'),
    ('nagiyev', 'Подождите! Ой, извините.', 'Wait! Oh, excuse me.', [(102, 'Подождите'), (103, 'Ой, извините')], 'adapted'),
    ('inspector', 'Что здесь происходит?', 'What is going on here?', [(94, 'Комиссия в отеле')], 'adapted'),
    ('mikhail', 'У них на родине сухой закон.', 'In their homeland there is prohibition.', [(104, 'сухой закон')], 'adapted'),
    ('mikhail', 'Сейчас всё будет хорошо.', 'Right now everything will be fine.', [(105, 'Сейчас все, все будет хорошо')], 'adapted'),
    ('inspector', 'Идёмте дальше.', 'Let us move on.', [(100, 'пойдемте')], 'adapted'),
]
WALK = [
    (0, None, '\'Excuse us for disturbing you.\' Mikhail directly directs this polite apology while facing Nagiyev using "izvinite" ("excuse me") — the respectful form of "excuse me" or "sorry" used when stepping in or apologizing.'),
    (1, None, '\'The commission is in the hotel. We are leaving right now.\' Emphasizing the commission right here, Mikhail lands on "komissiya" ("commission") as the key everyday word here.'),
    (2, None, "'Oh, the commission! Well I will show you everything right now.' Nagiyev fires back warmly in this moment, shifting the mood of the conversation in a single beat."),
    (3, None, "'Here the little sofas are soft.' Nagiyev opens up decisively with a nod, steering the talk right where he wants it."),
    (4, None, '\'Oh, only it is empty.\' Nagiyev counters readily on the spot and lands on "pustoy" ("empty-handed") as the key everyday word here.'),
    (5, None, "'Yes, let us go.' Speaking briskly before Nagiyev, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
    (6, None, "'Let us go. Well, where are you going?' Nagiyev asks deadpan what Mikhail is actually getting at here."),
    (7, None, '\'Wait! Oh, excuse me.\' Nagiyev plainly sends this polite apology in the exchange using "izvinite" ("excuse me") — the respectful form of "excuse me" or "sorry" used when stepping in or apologizing.'),
    (8, None, '\'What is going on here?\' Holding firm readily right here, the inspector puts the question word "chto" right at the start so Mikhail hears the focus immediately.'),
    (9, None, "'In their homeland there is prohibition.' Mikhail replies wryly on the spot, testing the inspector's reaction in the middle of the exchange."),
    (10, None, '\'Right now everything will be fine.\' Mikhail reacts evenly before the inspector and uses "khorosho" ("good, fine") to carry the main weight of the thought.'),
    (11, None, "'Let us move on.' Following up warmly before Mikhail, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
]
