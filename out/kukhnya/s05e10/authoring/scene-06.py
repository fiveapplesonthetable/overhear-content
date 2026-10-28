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
    (0, None, "'Excuse us for disturbing you.' Mikhail proceeds calmly in their talk, to clear the air between them once and for all."),
    (1, None, '\'The commission is in the hotel. We are leaving right now.\' Mikhail picks one key word in reply: "komissiya" means "commission", and it carries the main weight of what Mikhail is saying.'),
    (2, None, '\'Oh, the commission! Well I will show you everything right now.\' Nagiyev centers one clear term on cue: "komissiya" means "commission", and it carries the main weight of what Nagiyev is saying.'),
    (3, None, "'Here the little sofas are soft.' Nagiyev cuts in decisively to settle things, leaving no doubt about where he stands."),
    (4, None, '\'Oh, only it is empty.\' Nagiyev highlights one direct piece at once: "pustoy" means "empty-handed", and it carries the main weight of what Nagiyev is saying.'),
    (5, None, "'Yes, let us go.' Mikhail drops this line plainly here: spoken Russian trims this down to just 2 words, dropping the extra helper words that English has to spell out."),
    (6, None, "'Let us go. Well, where are you going?' Nagiyev asks deadpan in front of the inspector without any preamble."),
    (7, None, '\'Wait! Oh, excuse me.\' Nagiyev spotlights one sharp touch in earnest: "podozhdite" means "wait" (from "podozhdat"), giving the line its exact edge.'),
    (8, None, '\'What is going on here?\' The inspector directs this update on cue: putting the question word "chto" right at the front of the line lets Mikhail hear the point of the question on the very first beat.'),
    (9, None, "'In their homeland there is prohibition.' Mikhail speaks wryly without a pause, bringing things back to earth after the buildup."),
    (10, None, '\'Right now everything will be fine.\' Mikhail stresses one concrete touch with the inspector: "khorosho" means "good, fine", and it carries the main weight of what Mikhail is saying.'),
    (11, None, "'Let us move on.' The inspector shares the reply plainly here: spoken Russian trims this down to just 2 words, dropping the extra helper words that English has to spell out."),
]
