# Authoring module for dvorik-u-mosta-s01e05-scene-01.
ID = 'dvorik-u-mosta-s01e05-scene-01'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Правда во дворе  (Truth in the Courtyard)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'roman': 'Роман', 'kira': 'Кира', 'larisa': 'Лариса'}
INTRO = "Under the courtyard tree at the Bridge Courtyard Inn in St Petersburg, Roman sits down with Kira and Larisa Borisovna to explain Monday night's mystery from the very beginning. Listen first."
OPENER = "Let's walk through Roman's confession one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'All the puzzle pieces from Monday and Tuesday finally click together. Next time, Roman explains why he has not spoken to his brother Gleb in three years.'
CLOSING = ('kira', 'До скорого!')
STORY = [
    ('larisa', 'Дай я посмотрю на тебя, Рома! Ты вырос выше пианино!', 'Let me look at you, Roma! You grew taller than the piano!'),
    ('roman', 'Не могу поверить, что вы живёте в этом же гостевом доме, Лариса Борисовна.', 'I cannot believe that you are staying in this very same guesthouse, Larisa Borisovna.'),
    ('kira', 'Подождите — вы ехали на одном поезде в понедельник и взяли её чемодан?', 'Wait — you rode the same train on Monday and took her suitcase?'),
    ('roman', 'Совершенно случайно! Дома у брата жены я открыл его и увидел ноты и красную ленту.', "Completely by accident! At my cousin's flat I opened it and saw sheet music and a red ribbon."),
    ('larisa', 'А почему ты оставил мою сумку вечером на ступеньке и убежал?', 'And why did you leave my bag on the step in the evening and run away?'),
    ('roman', 'Потому что в понедельник вечером я увидел на этой улице моего старшего брата!', 'Because on Monday evening I saw my older brother on this street!'),
    ('kira', 'Ваш старший брат живёт здесь в Петербурге?', 'Does your older brother live here in St Petersburg?'),
    ('roman', 'Да, он живёт здесь уже пять лет. Я испугался, позвонил в звонок и приклеил записку.', 'Yes, he has been living here for five years now. I panicked, rang the bell, and taped on the note.'),
    ('larisa', 'Стойте — а в среду вечером ты заселился сюда под своим настоящим именем?', 'Hold on — and on Wednesday night you checked in here under your real name?'),
    ('roman', 'Мне было нужно тихое место рядом до пятницы, и, честно говоря, я слишком стеснялся попросить вернуть мой чемодан!', 'I needed a quiet place nearby before Friday, and honestly felt too shy to ask for my bag!'),
    ('kira', 'Даже после того, как во вторник вы позвонили нам насчёт белого свёртка!', 'Even after you called us on Tuesday about the white parcel!'),
    ('roman', 'Всё внутри этой белой бумаги принадлежит моему брату Глебу, а не мне.', 'Everything inside that white paper belongs to my brother Gleb, not to me.'),
]
WALK = [
    (0, None, ["'Let me look at you, Roma! You grew taller than the piano!' Having known him as a child, Larisa switches warmly to ", (None, 'ты вырос'), " — 'you grew up!'."]),
    (1, None, ["'I cannot believe that you are staying in this very same guesthouse, Larisa Borisovna.' Adding the little intensifier makes ", (None, 'в этом же'), " mean 'in this very same'."]),
    (2, None, "'Wait — you rode the same train on Monday and took her suitcase?' Kira keeps her polite 'you' with Roman as she traces Monday's chain of events."),
    (3, None, ["'Completely by accident! At my cousin's flat I opened it and saw sheet music and a red ribbon.' Pairing ", (None, 'Совершенно случайно!'), " gives you 'purely, completely by chance!'."]),
    (4, None, ["'And why did you leave my bag on the step in the evening and run away?' Adding the 'away' prefix onto running creates ", (None, 'убежал?'), " — 'ran away'."]),
    (5, None, ["'Because on Monday evening I saw my older brother on this street!' Notice ", (None, 'в понедельник вечером'), " stacking the day of the week right before 'in the evening'."]),
    (6, None, ["'Does your older brother live here in St Petersburg?' Notice how spoken intonation alone turns ", (None, 'живёт здесь'), ' into a clear yes-or-no question.']),
    (7, None, ["'Yes, he has been living here for five years now. I panicked, rang the bell, and taped on the note.' Ongoing life from past into present stays present in Russian: ", (None, 'живёт здесь уже пять лет.'), " literally says 'lives here already five years'."]),
    (8, None, ["'Hold on — and on Wednesday night you checked in here under your real name?' Genuine or real is ", (None, 'настоящим'), " — 'under his real name'."]),
    (9, None, ["'I needed a quiet place nearby until Friday, and I forgot my suitcase was still with you!' Past need uses neuter ", (None, 'Мне было нужно'), " matching neuter 'quiet place'."]),
    (10, None, ["'Even after you called us on Tuesday about the white parcel!' Something neatly wrapped up is ", (None, 'свёртка!'), ' — here in the genitive case.']),
    (11, None, ["'Everything inside that white paper belongs to my brother Gleb, not to me.' Ownership by right uses ", (None, 'принадлежит'), " — 'belongs to'."]),
]
