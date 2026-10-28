# Authoring module for kukhnya-s02e01-scene-21.
ID = 'kukhnya-s02e01-scene-21'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 1
SCENE = 21
TITLE = 'Короткий разговор  (Brief Exchange)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.01'
SOURCE_FILE = 'sources/kukhnya/s02/e01.ru.dual.srt'
INTRO = "Max's dangerous stunt goes horribly wrong when he accidentally slips. He finds himself actually hanging and cries out for help. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max calls out to Vika in the hallway before discussing the plan. Next time you watch the episode, listen for the Russian expressions for 'to want' and 'to know' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Я хочу, чтобы ты знала.', 'I want you to know.', [], ''),
    ('max', 'Я люблю тебя.', 'I love you.', [], ''),
    ('vika', 'Прекрати.', 'Stop it.', [], ''),
    ('vika', 'Ты хочешь вешаться?', 'Do you want to hang yourself?', [], ''),
    ('vika', 'Мне все равно.', "I don't care.", [], ''),
    ('max', 'Постой.', 'Wait.', [], ''),
    ('max', 'Я не шучу.', 'I am not joking.', [], ''),
    ('max', 'Помоги!', 'Help!', [], ''),
    ('kostya', 'Что вы наделали, Виктория?', 'What have you done, Victoria?', [(264, 'Вик')], ''),
    ('kostya', 'Вы убили его.', 'You killed him.', [], ''),
    ('vika', 'Костя, помоги ему!', 'Kostya, help him!', [], ''),
    ('kostya', 'Ты реально повесился?', 'Did you really hang yourself?', [], ''),
]
WALK = [
    (0, None, "'I want you to know.' Standing on the crate, Max tells Vika he wants her to know one thing."),
    (1, None, "'I love you.' He declares openly that he loves her. Then Vika responds."),
    (2, None, "'Stop it.' Vika sharply tells him to cut out the act."),
    (3, None, "'Do you want to hang yourself?' She asks sarcastically if he really plans to hang himself."),
    (4, None, "'I don't care.' She adds coldly that she does not care either way."),
    (5, None, "'Wait.' Max calls out for her to wait before she leaves."),
    (6, None, "'I am not joking.' As the crate shifts under him, he insists he is not joking."),
    (7, None, "'Help!' Slipping for real, Max gasps for help."),
    (8, None, "'What have you done, Victoria?' Kostya rushes in on cue and asks Victoria what she has done."),
    (9, None, "'You killed him.' Still acting out the script, Kostya accuses her of killing Max. Then Vika responds."),
    (10, None, "'Kostya, help him!' Realizing Max is actually strangling, Vika yells at Kostya to save him."),
    (11, None, "'Did you really hang yourself?' Kostya stares in shock as he realizes Max's stunt went wrong for real."),
]
