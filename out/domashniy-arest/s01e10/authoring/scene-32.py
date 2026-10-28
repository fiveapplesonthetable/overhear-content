# Authoring module for domashniy-arest-s01e10-scene-32.
ID = 'domashniy-arest-s01e10-scene-32'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 10
SCENE = 32
TITLE = 'Нам урезали зарплату  (Our Salaries Were Cut)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'colleague': 'Коллега', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.10'
SOURCE_FILE = 'sources/domashniy-arest/s01/e10.ru.dual.srt'
INTRO = "Returning to the university after her son's contest, Marina expects a peaceful day at the department. Instead, she is ambushed in the corridor by furious colleagues who reveal a shocking administrative scandal: to finance her municipal research grant, the dean slashed regular faculty salaries in half. Let's listen to this tense confrontation in Russian first; don't worry about catching every word."
OPENER = 'Let us examine this tense university hallway argument step by step to understand each line.'
TRANSITION = 'Now let us listen to the complete confrontation once more, noting the emotional accusations.'
OUTRO = 'Marina realizes her academic project has been weaponized against her colleagues, and heads off to confront management. Great job following this dramatic workplace dispute in Russian. See you next time!'
CLOSING = ('marina', 'Пока!')
STORY = [
    ('colleague', 'Марина, ты довольна своим проектом?', 'Marina, are you pleased with your project?', [], 'added opening challenge'),
    ('marina', 'Да, я закончила важную работу.', 'Yes, I finished important work.', [], 'added proud response'),
    ('colleague', 'Ну и делай свой проект дальше.', 'Fine, go work on your project further.', [(999, 'Ну и делай свой')], 'softened cue 999'),
    ('colleague', 'Нам из-за тебя зарплату урезали!', 'Our salaries were cut because of you!', [(1001, 'Нам из-за тебя зарплату'), (1002, 'урезали вдвое')], 'combined cues 1001-1002'),
    ('colleague', 'Урезали ровно в два раза.', 'They cut it exactly in half.', [(1002, 'урезали вдвое')], 'paraphrased cue 1002'),
    ('marina', 'Что? Почему из-за меня?', 'What? Why because of me?', [], 'added shocked question'),
    ('colleague', 'Все деньги ушли на твой проект.', 'All the money went to your project.', [], 'added budget explanation'),
    ('colleague', 'У Лены муж вообще инвалид.', "Lena's husband is actually disabled.", [(1004, 'У Ленки он вообще муж'), (1005, 'инвалид')], 'adapted cues 1004-1005'),
    ('colleague', 'Ему платят совсем маленькие копейки.', 'They pay him very tiny pennies.', [(1006, 'за нее копейки платят')], 'adapted cue 1006'),
    ('marina', 'Я совершенно ничего не знала!', 'I knew absolutely nothing!', [], 'added genuine protest'),
    ('colleague', 'Теперь все сотрудники будут страдать.', 'Now all employees will suffer.', [], 'added collective complaint'),
    ('marina', 'Я сейчас пойду к ректору.', 'I will go to the dean right now.', [], 'added decision to confront'),
    ('marina', 'Я разберусь с этой ситуацией.', 'I will sort out this situation.', [], 'added resolution statement'),
    ('colleague', 'Попробуй, если тебе поверят.', 'Try, if they believe you.', [], 'added parting skepticism'),
]
WALK = [
    (0, None, "'Marina, are you pleased with your project?' Cornering her in the university hallway, a fellow lecturer opens with a loaded question."),
    (1, None, "'Yes, I finished important work.' Still in a great mood after her son's contest, Marina doesn't sense the trap."),
    (2, None, "'Fine, go work on your project further.' Saying \"nu i\" like this is a bitter, dismissive \"well then, go right ahead\"."),
    (3, None, "'Our salaries were cut because of you!' Literally \"they trimmed the salary for us because of you\", dropping the ugly truth."),
    (4, None, "'They cut it exactly in half.' Where English says \"cut in half\", Russian says \"cut by two times\"."),
    (5, None, "'What? Why because of me?' Stunned, Marina has no idea how her historical research could hurt anyone's paycheck."),
    (6, None, "'All the money went to your project.' To fund her monastery film without a budget, Eduard simply raided the faculty payroll."),
    (7, None, "'Lena's husband is actually disabled.' Pointing to a coworker, he shows who is really paying the price for Eduard's favor."),
    (8, None, "'They pay him very tiny pennies.' In Russian, \"kopeks\" — the tiny coins that make up a ruble — means a pittance."),
    (9, None, "'I knew absolutely nothing!' Horrified, she swears she had no part in the dean's scheme."),
    (10, None, "'Now all employees will suffer.' The whole department is furious and blames her for their lost income."),
    (11, None, "'I will go to the dean right now.' Refusing to profit off her coworkers' backs, she marches straight toward Eduard's office."),
    (12, None, "'I will sort out this situation.' \"Razberus\" is a firm everyday word meaning \"I'll get to the bottom of this and fix it\"."),
    (13, None, "'Try, if they believe you.' Still bitter, the colleague doubts she will actually give up her funding."),
]
