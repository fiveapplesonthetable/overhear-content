# Authoring module for kukhnya-s03e01-scene-03.
ID = 'kukhnya-s03e01-scene-03'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 3
TITLE = 'Штраф за разговор  (A Fine for Talking)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya': 'Настя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = 'In the dining room near the bar, art director Vika Goncharova hands Max a hefty fine for his mistake, and when he tries to ask her out after work, she raises the penalty even higher.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that ends our scene by the bar. Listen out for Vika doubling Max's fine when he refuses to drop the subject of a cafe date. Until next time!"
CLOSING = ('vika', 'Хорошего дня!')
STORY = [
    ('vika', 'Лавров, штраф три тысячи.', 'Lavrov, a fine of three thousand.', [(34, 'Лавров'), (35, 'Штраф три тысячи')], 'adapted'),
    ('max', 'Три тысячи?', 'Three thousand?', [(35, 'Три тысячи')], ''),
    ('vika', 'Так, давай убирай.', 'Right, go on and clean up.', [(37, 'Так, давай убирай')], ''),
    ('max', 'Мы с тобой в кафешку сходим?', 'Shall you and I go to a little cafe?', [(38, 'мы с тобой в кафешку сходим')], 'adapted'),
    ('vika', 'То, что я взяла тебя, ничего не значит.', 'The fact that I hired you means nothing.', [(39, 'То, что я взяла тебя на работу, ничего не значит')], 'adapted'),
    ('vika', 'У нас деловые отношения.', 'We have a business relationship.', [(40, 'деловые отношения')], 'adapted'),
    ('vika', 'Понятно?', 'Understood?', [(41, 'Понятно')], ''),
    ('max', 'Понятно. Но после смены сходим?', 'Understood. But shall we go after the shift?', [(41, 'Понятно'), (38, 'после смены')], 'adapted'),
    ('vika', 'Штраф пять тысяч.', 'A fine of five thousand.', [(43, 'Штраф пять тысяч')], ''),
    ('nastya', 'Кажется, пинается.', 'I think it is kicking.', [(44, 'Кажется, пинается')], ''),
    ('max', 'У него сейчас рост восемь сантиметров.', 'He is only eight centimeters tall right now.', [(45, 'У него сейчас рост восемь сантиметров')], ''),
    ('max', 'Как он может пинаться?', 'How can he be kicking?', [(46, 'он может пинаться')], 'adapted'),
]
WALK = [
    (0, None, "'Lavrov, a fine of three thousand.' Vika steps in firmly on the spot, letting the remark speak for itself."),
    (1, None, '\'Three thousand?\' Turning to the thousands before Vika, Max chooses "tysyachi" ("thousands", from the root "tysyacha") so Vika hears the exact meaning.'),
    (2, None, '\'Right, go on and clean up.\' Cutting in smoothly in front of Max, Vika starts with "davay" ("come on, let\'s") to invite Max right into the action.'),
    (3, None, "'Shall you and I go to a little cafe?' Max prompts firmly to see how Vika will answer on the spot."),
    (4, None, '\'The fact that I hired you means nothing.\' Vika pushes back briskly in the exchange and brings in "znachit" ("then, so") to make the meaning unmistakable.'),
    (5, None, '\'We have a business relationship.\' Touching on the relations in this beat, Vika reaches for "u nas" ("by us, at our place") to talk about what they share.'),
    (6, None, '\'Understood?\' Vika evenly drops this acknowledgment right on cue using "ponyatno" ("understood") — a single word meaning "clear, got it", showing the point has landed.'),
    (7, None, '\'Understood. But shall we go after the shift?\' Max naturally offers this acknowledgment toward Vika using "ponyatno" ("understood") — a single word meaning "clear, got it", showing the point has landed.'),
    (8, None, "'A fine of five thousand.' Bringing up the thousand during the talk, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (9, None, "'I think it is kicking.' Nastya pushes back wryly without any doubt, to clear the air between them once and for all."),
    (10, None, '\'He is only eight centimeters tall right now.\' Addressing the centimeters beside Nastya, Max brings in "santimetrov" ("centimeters", from "santimetr") as the key Russian word here.'),
    (11, None, '\'How can he be kicking?\' Holding firm briskly during the talk, the "-sya" ending on "pinatsya" ("to kick") marks an action that unfolds mutually or turns back on the speaker.'),
]
