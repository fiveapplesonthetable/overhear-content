# Authoring module for kukhnya-s01e16-scene-18.
ID = 'kukhnya-s01e16-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 18
TITLE = 'Метод дедукции  (Method of Deduction)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'inspector': 'Инспектор', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "Still searching the dining room for disguised employees, the migration inspector stops at the table of French pastry chef Louis. Like a seasoned detective, the inspector points out three telltale habits that prove Louis is actually a chef working at the restaurant rather than a guest. Let's listen to his clever deduction in Russian."
OPENER = "Let's examine how the inspector uses observation to uncover Louis's true profession."
TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "Now you know how to ask for documents, describe someone's profession, and explain workplace rules in Russian. Listen to what happens next when the inspector escorts Louis away. Next time you watch the episode, listen for the Russian expressions for 'may' and 'to have a look' — you will catch every word right away. See you next time!"
CLOSING = ('inspector', 'Покажите мне ваш французский паспорт.')
STORY = [
    ('inspector', 'Можно посмотреть на ваши документы?', 'May I look at your documents?', [(261, 'ваши документы?')], ''),
    ('louis', 'Я просто обычный гость ресторана.', 'I am just an ordinary guest of the restaurant.', [], ''),
    ('inspector', 'Нет, вы работаете здесь поваром.', 'No, you work here as a chef.', [(261, 'Вы же повар в этом ресторане')], ''),
    ('louis', 'Почему вы вдруг так решили?', 'Why did you suddenly decide so?', [], ''),
    ('inspector', 'Вы очень внимательно смотрите на блюдо.', 'You are looking at the dish very carefully.', [(262, 'только повар может так придирчиво рассматривать')], ''),
    ('inspector', 'Вам эта еда совсем не нравится.', 'You do not like this food at all.', [(263, 'ему оно не понравится')], ''),
    ('inspector', 'Потому что готовил её другой повар.', 'Because another chef cooked it.', [(264, 'готовил-то его кто-то другой')], ''),
    ('louis', 'Я просто люблю хорошую кухню.', 'I simply love good cuisine.', [], ''),
    ('inspector', 'Ещё вы постоянно трогаете свою голову.', 'Also you are constantly touching your head.', [(265, 'Вы все время трогаете голову')], ''),
    ('inspector', 'На работе вы всегда носите шапку.', 'At work you always wear a cap.', [], ''),
    ('inspector', 'И вы совсем не пьёте вино.', 'And you are not drinking the wine at all.', [(266, 'Вы не прикоснулись вообще')], ''),
    ('inspector', 'Потому что на работе нельзя пить.', 'Because at work one must not drink.', [(267, 'потому что на работе пить')], ''),
    ('louis', 'Да, вы сказали чистую правду.', 'Yes, you told the pure truth.', [], ''),
]
WALK = [
    (0, None, "'May I look at your documents?' A formal request used by an official during an inspection."),
    (2, None, "'No, you work here as a chef.' Russian uses the matching word ending for the profession after the verb to work."),
    (8, None, "'Also you are constantly touching your head.' A sharp observation pointing out a physical habit."),
    (11, None, "'Because at work one must not drink.' An explanation referencing workplace rules with an impersonal modal word. Now, let's listen to the inspector's deduction from start to finish. Now let's listen to the whole conversation again from start to finish."),
]
