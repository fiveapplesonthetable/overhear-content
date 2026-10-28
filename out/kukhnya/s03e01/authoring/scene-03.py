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
    (0, None, "'Lavrov, a fine of three thousand.' Vika speaks firmly during the talk, so Max knows she is not just making small talk."),
    (1, None, '\'Three thousand?\' Max sharpens one key term in earnest: "tysyachi" means "thousands" (from "tysyacha"), giving the line its exact edge.'),
    (2, None, '\'Right, go on and clean up.\' Vika puts that remark right away: starting with "davay" is the classic everyday Russian way to say "come on, let\'s do this" between people on close terms.'),
    (3, None, "'Shall you and I go to a little cafe?' Max prompts firmly if there is more going on behind the scenes."),
    (4, None, '\'The fact that I hired you means nothing.\' Vika anchors one clear expression on cue: "znachit" means "then, so", and it carries the main weight of what Vika is saying.'),
    (5, None, '\'We have a business relationship.\' Vika voices this point before Nastya: the phrase "u nas" literally means "by us" or "at our place", the standard Russian way to talk about what a group or couple shares.'),
    (6, None, "'Understood?' Vika questions skeptically before Max can change the subject."),
    (7, None, '\'Understood. But shall we go after the shift?\' Max leans on this key element right here: "ponyatno" means "clear", and it carries the main weight of what Max is saying.'),
    (8, None, "'A fine of five thousand.' Vika gives the remark on cue: spoken Russian trims this down to just 3 words, dropping the extra helper words that English has to spell out."),
    (9, None, "'I think it is kicking.' Nastya responds wryly in this moment, shifting the whole mood of the room in a single beat."),
    (10, None, '\'He is only eight centimeters tall right now.\' Max favors one pointed expression with Nastya: "santimetrov" means "centimeters" (from "santimetr"), giving the line its exact edge.'),
    (11, None, '\'How can he be kicking?\' Max makes the reaction with warmth: the "-sya" ending on "pinatsya" ("to kick") turns the action inward or makes it happen between people naturally.'),
]
