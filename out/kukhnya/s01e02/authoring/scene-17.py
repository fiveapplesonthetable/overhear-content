# Authoring module for kukhnya-s01e02-scene-17.
ID = 'kukhnya-s01e02-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 17
TITLE = 'Один нормальный день  (One Normal Day)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'sasha': 'Саша', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = 'The crises keep coming, and Vika finally sits down in the dining room, worn out. Sasha, the waitress, offers her a coffee and listens as Vika complains that nothing ever goes right at Claude Monet. Here is their talk in Russian first.'
OPENER = "Now let's look at the complaints."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Vika asks for nothing more than one quiet day, which is not much to ask. If you take away only "ya uverena", "I\'m sure", you\'ll find it useful.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('sasha', 'Виктория Сергеевна, вам принести чашку кофе?', 'Viktoriya Sergeyevna, should I bring you a cup of coffee?', [], ''),
    ('vika', 'Господи, как же меня всё достало!', 'Lord, how sick of everything I am!', [(205, 'меня все достало')], ''),
    ('sasha', 'В ресторане опять возникли новые проблемы?', 'Have new problems arisen in the restaurant again?', [], ''),
    ('vika', 'Конечно, в баре пропал дорогой коньяк.', 'Of course, expensive cognac went missing in the bar.', [], ''),
    ('sasha', 'Бармен Костя сейчас ищет эту бутылку.', 'Bartender Kostya is looking for that bottle now.', [], ''),
    ('vika', 'Ну почему всё всегда идёт не так?', 'Well why does everything always go wrong?', [(206, 'Ну почему все всегда')], ''),
    ('sasha', 'Наша работа всегда очень нервная.', 'Our work is always very stressful.', [], ''),
    ('vika', 'Шеф кричит, повара спорят, бардак везде!', 'The chef shouts, cooks argue, mess everywhere!', [], ''),
    ('sasha', 'Вам нужно немного отдохнуть и успокоиться.', 'You need to rest a bit and calm down.', [], ''),
    ('vika', 'Неужели нельзя, чтобы день прошёл нормально?', 'Can a day really not pass normally?', [(207, 'прошел нормально')], ''),
    ('sasha', 'Я уверена, скоро всё наладится.', 'I am sure everything will work out soon.', [], ''),
    ('vika', 'Хочу хотя бы один спокойный день!', 'I want at least one calm day!', [(208, 'Один день')], ''),
    ('sasha', 'Мы все очень хотим этого, поверьте.', 'We all want this very much, believe me.', [], ''),
]
WALK = [
    (0, None, '\'Viktoriya Sergeyevna, should I bring you a cup of coffee?\' "Vam prinesti", "to you to bring", is how Russians offer something. "Chashka" becomes "chashku", and "kofe" never changes.'),
    (1, None, '\'Lord, how sick of everything I am!\' The first word is "Gospodi", an exclamation like "oh Lord". The second half is "everything reached me", a stock way to say you\'ve had enough.'),
    (2, None, '\'Have new problems arisen in the restaurant again?\' "Voznikli" is "arose", and "opyat\'" is "again". "Novyye problemy" are both plural.'),
    (3, None, '\'Of course, expensive cognac went missing in the bar.\' "Disappeared" is "propal", with the -l of a masculine word, because "cognac" is masculine. It\'s the same verb as "disappear to" in the last scene.'),
    (4, None, '\'Bartender Kostya is looking for that bottle now.\' "Ishchet", is looking for, is the same verb as "ishchi" from the knife scene. "Etu butylku" ends in -u as the thing being sought.'),
    (5, None, '\'Well, why does everything always go wrong?\' "Idyot ne tak" is "goes not so". Russians say "idti", to go, about events as well as people.'),
    (6, None, '\'Our work is always very stressful.\' "Stressful" comes from "nerves". It ends in -aya to match the feminine word "work".'),
    (7, None, '\'The chef shouts, cooks argue, mess everywhere!\' "Bardak" is slang for a mess, a stronger word than "besporyadok". No "and" between the items, just commas.'),
    (8, None, '\'You need to rest a bit and calm down.\' "Vam nuzhno", "to you necessary", is the Russian "you need". "Otdokhnut\'" is "to rest", and "uspokoit\'sya", to calm down, ends in "-sya".'),
    (9, None, '\'Can a day really not pass normally?\' "Neuzheli" is "can it really be?". "Nel\'zya, chtoby" is "is it impossible that", and "proshyol", passed, is the past form that goes after "chtoby".'),
    (10, None, '\'I am sure everything will work out soon.\' A woman says "uverena", a man says "uveren". "Will work out" has the same root as "ladno", fine, so it means "will get into harmony".'),
    (11, None, '\'I want at least one calm day!\' "Khochu" already says "I want", so Vika drops the "ya". "Khotya by", at least, is two small words.'),
    (12, None, '\'We all want this very much, believe me.\' "Pover\'te", believe me, is the polite command from "verit\'", to believe. "My vse" is "we all".'),
]
