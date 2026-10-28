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
    (0, None, '\'Viktoriya Sergeyevna, should I bring you a cup of coffee?\' "To you to bring" is how Russian offers something: "vam prinesti". "Coffee" never changes.'),
    (1, None, '\'Lord, how sick of everything I am!\' The first word is "Gospodi", an exclamation like "oh Lord". The second half is "everything reached me", a stock way to say you\'ve had enough.'),
    (2, None, '\'Have new problems arisen in the restaurant again?\' "Arisen" is a single word, and "again" is a small one. "New problems" is plural, so both words end in "-y".'),
    (3, None, '\'Of course, expensive cognac went missing in the bar.\' "Disappeared" is "propal", with the -l of a masculine word, because "cognac" is masculine. It\'s the same verb as "disappear to" in the last scene.'),
    (4, None, '\'Bartender Kostya is looking for that bottle now.\' "Looks for" is the family of "ishchi", the command from the knife scene. "That bottle" ends in -u as the thing being sought.'),
    (5, None, '\'Well, why does everything always go wrong?\' Literally "goes not so", using the everyday word for "go". Russians use it for events as well as people.'),
    (6, None, '\'Our work is always very stressful.\' "Stressful" comes from "nerves". It ends in -aya to match the feminine word "work".'),
    (7, None, '\'The chef shouts, cooks argue, mess everywhere!\' "Bardak" is slang for a mess, a stronger word than "besporyadok". No "and" between the items, just commas.'),
    (8, None, '\'You need to rest a bit and calm down.\' "To you necessary" is how Russian says "you need". "Calm down" has "-sya" on the end, and it\'s from the word for "calm".'),
    (9, None, '\'Can a day really not pass normally?\' "Neuzheli" is a question word meaning "really?". "Nel\'zya, chtoby" is "is it impossible that", and "passed" is the past of the verb for "pass".'),
    (10, None, '\'I am sure everything will work out soon.\' A woman says "uverena", a man says "uveren". "Will work out" has the same root as "ladno", fine, so it means "will get into harmony".'),
    (11, None, '\'I want at least one calm day!\' "I want" drops the "I", because "khochu" already says it. "At least" is two little words.'),
    (12, None, '\'We all want this very much, believe me.\' "Believe me" is a polite command. "We all" is two short words.'),
]
