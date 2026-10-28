# Authoring module for domashniy-arest-s01e08-scene-10.
ID = 'domashniy-arest-s01e08-scene-10'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 10
TITLE = 'Тяжёлое утро в баре  (A Rough Morning at the Bar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barman': 'Бармен', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "Welcome back to Domashniy Arest! After a long, despairing night of drinking following the slanderous attacks on his family honor, mayoral candidate Ivan Samsonov wakes up with a terrible hangover on a table in a dingy neighbourhood bar. The unsympathetic bartender wants to close up and orders Ivan to clear out. Let's listen to the scene in Russian first."
OPENER = "Now let's examine Ivan's painful morning confrontation in the bar line by line. The bartender tries to wake up the hungover mayoral candidate and push him out into the street."
TRANSITION = "Now let's listen to the rough morning conversation in the bar once more in Russian."
OUTRO = 'Broke, hungover, and exhausted, Ivan stumbles out into the daylight just hours before the fateful debate. See you next time!'
CLOSING = ('barman', 'Пока!')
STORY = [
    ('barman', 'Доброе утро! Просыпайся, соня.', 'Good morning! Wake up, sleepyhead.', [(143, 'Доброе утро')], ''),
    ('samson', 'Где я? Который сейчас час?', 'Where am I? What time is it now?', [], ''),
    ('barman', 'Уже утро. Наш бар закрывается.', 'It is already morning. Our bar is closing.', [], ''),
    ('samson', 'Дай мне ещё один стакан.', 'Give me one more glass.', [], ''),
    ('barman', 'Хватит с тебя. Ты пьян.', 'That is enough for you. You are drunk.', [], ''),
    ('samson', 'У меня ужасно болит голова.', 'My head aches terribly.', [], ''),
    ('barman', 'Ты пил всю ночь напролёт.', 'You drank all night long.', [], ''),
    ('samson', 'Я должен всё забыть.', 'I must forget everything.', [], ''),
    ('barman', 'Твои деньги совсем закончились.', 'Your money has completely run out.', [], ''),
    ('samson', 'Налей в долг! Я заплачу.', 'Pour on credit! I will pay.', [], ''),
    ('barman', 'Никаких долгов. Ты не мог заплатить.', 'No debts. You could not pay.', [(144, 'Ты не мог')], ''),
    ('samson', 'Мне нужно на выборы!', 'I need to go to the election!', [], ''),
    ('barman', 'Вставай на ноги и вали отсюда!', 'Get on your feet and get lost!', [(145, 'Вали')], ''),
    ('samson', 'Ухожу, ухожу. Мне очень плохо.', 'I am leaving, leaving. I feel very bad.', [], ''),
]
WALK = [
    (0, None, "'Good morning! Wake up, sleepyhead.' The bartender sarcastically greets the slumped customer."),
    (1, None, "'Where am I? What time is it now?' Ivan groggily lifts his head off the sticky table."),
    (2, None, "'It is already morning. Our bar is closing.' The bartender informs him that closing time has arrived."),
    (3, None, "'Give me one more glass.' Ivan desperately asks for another drink to numb his hangover."),
    (4, None, "'That is enough for you. You are drunk.' The bartender cuts him off bluntly: Ivan has had more than enough."),
    (5, None, "'My head aches terribly.' Literally, 'at me terribly aches the head' — the hangover is hitting Ivan with full force."),
    (6, None, "'You drank all night long.' That colorful expression at the end means straight through the night without stopping."),
    (7, None, "'I must forget everything.' Ivan expresses his desire to blot out the painful slander."),
    (8, None, "'Your money has completely run out.' His pockets are completely empty after the all-night binge."),
    (9, None, "'Pour on credit! I will pay.' Desperate for hair of the dog, Ivan begs the barman to put one more glass on his tab."),
    (10, None, "'No debts. You could not pay.' The bartender refuses to extend any further credit."),
    (11, None, "'I need to go to the election!' Ivan suddenly remembers his mayoral campaign responsibilities."),
    (12, None, "'Get on your feet and get lost!' The abrupt colloquial command tells Ivan to leave immediately."),
    (13, None, "'I am leaving, leaving. I feel very bad.' Ivan stumbles unsteadily toward the exit."),
]
