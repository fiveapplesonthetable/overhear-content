# Authoring module for kukhnya-s01e02-scene-13.
ID = 'kukhnya-s01e02-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 13
TITLE = 'Посторонний в баре  (An Outsider in the Bar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'master': 'Мастер', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "Back at the bar, Vika sees a man behind the counter fiddling with the cash register. From behind she takes him for Kostya, but it isn't: it's a stranger, and she is not pleased. Here's their argument in Russian first."
OPENER = "Let's go through the confusion."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Vika throws the repairman out and sends for the real Kostya. You\'ve learned how to say "get out of here" and "strictly forbidden".'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Костя, ты уже починил нашу кассу?', 'Kostya, have you already fixed our register?', [(179, 'ты сикибер починил')], ''),
    ('master', 'Нет, я ещё работаю над этой кассой.', 'No, I am still working on this register.', [(180, 'Нет но и работу надо')], ''),
    ('vika', 'Что ты вообще делаешь за нашей барной стойкой?', 'What are you even doing behind our bar counter?', [(181, 'Что здесь делаешь')], ''),
    ('master', 'Я просто спокойно настраиваю эту сложную систему.', 'I am simply calmly adjusting this complex system.', [(181, 'чиню')], ''),
    ('vika', 'Быстро уходи отсюда вон из бара!', 'Leave here quickly, out of the bar!', [(182, 'давай вон из бара')], ''),
    ('master', 'Женщина, подождите, я мастер по ремонту.', 'Woman, wait, I am a repair technician.', [(186, 'что ты завелась-то')], ''),
    ('vika', 'Я сказала немедленно выйти отсюда вон!', 'I said to get out of here immediately!', [(183, 'Вон я сказала')], ''),
    ('master', 'Зачем вы так громко кричите на меня?', 'Why are you shouting so loudly at me?', [(186, 'что ты завелась')], ''),
    ('vika', 'Посторонним людям строго запрещено находиться здесь.', 'Outsiders are strictly forbidden to be here.', [(185, 'Что стоишь Вон из бара')], ''),
    ('master', 'Ладно, успокойтесь, я уже ухожу отсюда.', 'Fine, calm down, I am already leaving here.', [(186, 'А ладно')], ''),
    ('vika', 'Официант, быстро найди мне бармена Костю!', 'Waiter, quickly find bartender Kostya for me!', [(184, 'Артем быстро зови Костю')], ''),
    ('vika', 'Я хочу знать, кто пустил этого человека.', 'I want to know who let this person in.', [(184, 'зови Костю')], ''),
]
WALK = [
    (0, None, '\'Kostya, have you already fixed our register?\' Vika uses Kostya\'s name because she thinks it\'s him. "Fixed" ends in -l, which is the past for a man.'),
    (1, None, '\'No, I am still working on this register.\' "Work on" uses a small word that literally means "above". The register takes the ending that this word calls for.'),
    (2, None, '\'What are you even doing behind our bar counter?\' The little word "behind" gives the counter an ending. And "even" sharpens a question.'),
    (3, None, '\'I am simply calmly adjusting this complex system.\' "Calmly" comes from "calm", the same as in "good night". "Adjust" is what you do when tuning something.'),
    (4, None, '\'Leave here quickly, out of the bar!\' "Out" appears twice, once as a rude "get out!" and once in "out of". Russians pile them up for emphasis.'),
    (5, None, '\'Woman, wait, I am a repair technician.\' Calling a woman "woman" to her face is blunt, and the repairman does it. "Master of repair" is the Russian for repair technician.'),
    (6, None, '\'I said to get out of here immediately!\' "Said" ends in -a for Vika. "Immediately" is "not slowly", with "not" in front of "slowly".'),
    (7, None, '\'Why are you shouting so loudly at me?\' The question is "what for". Russian says "shout at me" with the same small word as in "look at".'),
    (8, None, '\'Outsiders are strictly forbidden to be here.\' "Outsiders" comes from "side", so it\'s people from the side. "Forbidden" is what you see on signs.'),
    (9, None, '\'Fine, calm down, I am already leaving here.\' "Calm yourself" is the same family as "calmly". "Fine" is how Russians say "OK".'),
    (10, None, '\'Waiter, quickly find bartender Kostya for me!\' "Find" is a friendly command. Kostya\'s name changes its ending to "-u" because he is the one being found.'),
    (11, None, '\'I want to know who let this person in.\' "I want to know" is two words. "Pustil" is "let in", and "this person" takes object endings.'),
]
