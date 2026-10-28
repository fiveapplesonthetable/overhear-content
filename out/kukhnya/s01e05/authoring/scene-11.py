# Authoring module for kukhnya-s01e05-scene-11.
ID = 'kukhnya-s01e05-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 11
TITLE = 'План мести  (A Plan of Revenge)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "In the Claude Monet staff room, Nastya is still in tears over Max, and Sasha, her fellow waitress, has decided crying won't fix anything. She has a plan, and it involves Kostya, the bartender and Max's best friend. Just listen to how it sounds in Russian first."
OPENER = 'Slowly now. Sasha sounds like a general, and Nastya sounds unconvinced.'
TRANSITION = 'Back to the full version.'
OUTRO = '"Mne stanet legche", \'it will get lighter for me\', is the Russian way to say you\'ll feel better. It works just as well for a headache or a bad day as for a broken heart.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Макс поступил со мной очень плохо.', 'Max treated me very badly.', [], ''),
    ('sasha', 'Хватит плакать, Настя, вытри слёзы.', 'Stop crying, Nastya, wipe your tears.', [], ''),
    ('sasha', 'Тебе нужно просто ему отомстить.', 'You just need to get back at him.', [(145, 'Тебе нужно просто ему отомстить')], ''),
    ('nastya', 'Мне станет легче, если отомстить?', 'Will I feel better if I get revenge?', [(146, 'Будет легче')], ''),
    ('sasha', 'Конечно, тебе сразу станет легче.', 'Of course, you will immediately feel better.', [], ''),
    ('nastya', 'Но как я могу наказать его?', 'But how can I punish him?', [(150, 'наказание')], ''),
    ('sasha', 'Начни встречаться с его лучшим другом.', 'Start going out with his best friend.', [(151, 'с его другом')], ''),
    ('nastya', 'С его другом? С барменом Костей?', 'With his friend? With bartender Kostya?', [(152, 'С Костей?')], ''),
    ('sasha', 'Да, именно с Костей!', 'Yes, exactly with Kostya!', [(153, 'Да, с Костей')], ''),
    ('sasha', 'Так Максу будет ещё больнее.', 'That way Max will hurt even more.', [(153, 'Так ему будет еще хуже')], ''),
    ('nastya', 'Думаешь, это действительно хорошая идея?', "Do you think that's really a good idea?", [], ''),
    ('sasha', 'Поверь мне, это самый лучший вариант.', 'Trust me, this is the very best option.', [(157, 'И поверь, это лучший вариант')], ''),
    ('sasha', 'Действуй прямо сейчас, не теряй времени.', 'Act right now, do not lose time.', [(157, 'Действуй давай')], ''),
]
WALK = [
    (0, None, '\'Max treated me very badly.\' You heard this exact line when Nastya told Vika. "Ochen plokho", \'very badly\', is the easy part; "postupil so mnoy" is \'acted with me\'.'),
    (1, None, '\'Stop crying, Nastya, wipe your tears.\' "Khvatit", \'enough\', is followed straight away by "plakat", \'to cry\'. "Vytri", \'wipe\', is a command to one person.'),
    (2, None, '\'You just need to get back at him.\' "Tebe nuzhno", \'to you it\'s needed\', is how \'you need to\' works. "Otomstit" comes from "mest", \'revenge\', and the person you take it on goes into the \'to\' form: "emu".'),
    (3, None, '\'Will I feel better if I get revenge?\' Literally \'to me will become lighter\'. "Legche" is the comparative of "lyogkiy", which means both \'light\' and \'easy\'.'),
    (4, None, '\'Of course, you will immediately feel better.\' Sasha repeats the shape back with "tebe" in place of "mne". "Srazu" means \'at once\', and you\'ll hear it constantly.'),
    (5, None, '\'But how can I punish him?\' "Mogu", \'I can\', is a word you\'ll need every day. "Nakazat" is \'to punish\', while "nakazanie" names the punishment itself.'),
    (6, None, '\'Start going out with his best friend.\' "Vstrechatsya s", \'to date\', is the verb Max used earlier. After "s", the words change to "s ego luchshim drugom", but "ego", \'his\', never changes.'),
    (7, None, '\'With his friend? With bartender Kostya?\' Nastya repeats it in disbelief. After "s", "barmen" becomes "barmenom" and Kostya becomes "Kostey".'),
    (8, None, '\'Yes, exactly with Kostya!\' "Imenno", \'exactly\', points straight at the word after it. Sasha won\'t let her wriggle out of it.'),
    (9, None, '\'That way Max will hurt even more.\' "Maksu budet bolnee" is \'to Max it will be more painful\'. "Eshchyo" before a \'more\' word like this means \'even\'.'),
    (10, None, '\'Do you think that\'s really a good idea?\' "Deystvitelno" means \'really\' in the sense of \'actually, in fact\'. "Dumaesh" on its own is a doubtful \'you think?\'.'),
    (11, None, '\'Trust me, this is the very best option.\' "Pover mne" is \'believe to me\', with "mne" in the \'to\' form. "Variant" looks like \'variant\' but means \'option\'.'),
    (12, None, '\'Act right now, do not lose time.\' "Ne teryay", \'don\'t lose\', is "ne" plus a command. After it, "vremya" turns into "vremeni", as it did in Nastya\'s \'love knows no time\'.'),
]
