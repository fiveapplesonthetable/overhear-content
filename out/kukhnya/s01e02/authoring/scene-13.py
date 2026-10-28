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
    (0, None, '\'Kostya, have you already fixed our register?\' Vika says "Kostya" because she thinks it\'s him. "Pochinil", fixed, is the past for a man, and "nashu kassu", our till, ends in -u as the thing fixed.'),
    (1, None, '\'No, I am still working on this register.\' "Rabotayu nad" is "I work over", since "nad" means "above". After "nad", "kassa" becomes "kassoy".'),
    (2, None, '\'What are you even doing behind our bar counter?\' "Za" is "behind", and after it "barnaya stoyka" becomes "barnoy stoykoy". "Voobshche" sharpens the question.'),
    (3, None, '\'I am simply calmly adjusting this complex system.\' "Spokoyno", calmly, comes from "pokoy", peace, the root of "spokoynoy nochi", good night. "Nastraivayu" is "I\'m tuning", as you\'d tune a radio.'),
    (4, None, '\'Leave here quickly, out of the bar!\' "Von" is a rude "out!", and "iz bara" is "out of the bar". Vika piles them up, with "otsyuda", from here, as well.'),
    (5, None, '\'Woman, wait, I am a repair technician.\' Calling someone "zhenshchina", woman, is common but blunt. "Master po remontu", "master in repair", is a repairman, and "podozhdite" is the polite "wait".'),
    (6, None, '\'I said to get out of here immediately!\' "Skazala" ends in -a for Vika. "Nemedlenno", immediately, is "ne", not, plus "medlenno", slowly.'),
    (7, None, '\'Why are you shouting so loudly at me?\' "Zachem" is "what for", a sharper "why". "Krichite na menya" is "shout on me", with the same "na" as "smotri na", look at.'),
    (8, None, '\'Outsiders are strictly forbidden to be here.\' "Postoronniy", outsider, comes from "storona", side, so it means people from the side. "Strogo zapreshcheno", strictly forbidden, is what you see on signs.'),
    (9, None, '\'Fine, calm down, I am already leaving here.\' "Uspokoytes\'", calm down, has the same "pokoy" as "spokoyno". "Ladno" is the Russian "OK, fine".'),
    (10, None, '\'Waiter, quickly find bartender Kostya for me!\' "Naydi", find, is a friendly command. "Barmen Kostya" becomes "barmena Kostyu" because he\'s the one being found.'),
    (11, None, '\'I want to know who let this person in.\' "Khochu znat\'" is "I want to know". "Pustil" is "let in", and "etot chelovek" becomes "etogo cheloveka" as the one let in.'),
]
