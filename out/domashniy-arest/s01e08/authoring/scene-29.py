# Authoring module for domashniy-arest-s01e08-scene-29.
ID = 'domashniy-arest-s01e08-scene-29'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 29
TITLE = 'Бумаги в больнице  (Hospital Paperwork)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'doctor': 'Доктор', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "While Arkady learned that Lyosha's condition is treatable with medication, Marina went straight to the municipal hospital. In the corridor, the local surgeon hands her the legal consent form for the high-risk surgery. Listen to the Russian conversation first, and do not worry about catching every word."
OPENER = "Let's follow Marina's conversation with the surgeon line by line."
TRANSITION = "Now listen to Marina's hospital exchange again."
OUTRO = 'Unaware that Arkady has found the real diagnosis, Marina signs the hospital consent. Meanwhile, out on the town streets, Samsonov is nursing his wounded pride. See you next time!'
CLOSING = ('marina', 'Пока!')
STORY = [
    ('doctor', 'Приведёте ребёнка с утра.', 'You will bring the child in the morning.', [(592, 'Приведете ребенка с утра')], ''),
    ('doctor', 'Вот, прочтите и здесь распишитесь.', 'Here, read this and sign right here.', [(594, 'Вот, прочтите и здесь распишитесь')], ''),
    ('marina', 'Скажите, а эта операция очень опасная?', 'Tell me, is this operation very dangerous?', [(595, 'Скажите, а эта операция очень опасная')], ''),
    ('doctor', 'Здесь все операции сложные и опасные.', 'Here all operations are complex and dangerous.', [(597, 'Здесь все операции сложные, опасные')], ''),
    ('marina', 'А если мы не сделаем её?', 'And what if we do not do it?', [], 'clarifying question'),
    ('doctor', 'Тогда мальчик не сможет ходить.', 'Then the boy will not be able to walk.', [(599, 'не сможете ходить')], ''),
    ('marina', 'Я очень боюсь за ребёнка.', 'I am very afraid for the child.', [], "mother's fear"),
    ('doctor', 'Тогда что вы решили? Время идёт.', 'Then what have you decided? Time is passing.', [(603, 'Тогда что')], ''),
    ('marina', 'Я просто хочу услышать правду.', 'I just want to hear the truth.', [(604, 'Я просто хотела услышать')], ''),
    ('doctor', 'Если что-то случится, вы должны понимать.', 'If something happens, you must understand.', [(609, 'если, не дай бог, что-то случится')], ''),
    ('doctor', 'Вся ответственность лежит на вас.', 'All responsibility lies with you.', [], 'new clarifying A1 sentence'),
    ('marina', 'Хорошо. Я всё подпишу.', 'Fine. I will sign everything.', [], 'new closing A1 sentence'),
]
WALK = [
    (0, None, "'You will bring the child in the morning.' The surgeon gives direct instructions."),
    (1, None, "'Here, read this and sign right here.' This phrase means to place one's signature."),
    (2, None, "'Tell me, is this operation very dangerous?' Marina asks the question that terrifies her."),
    (3, None, "'Here all operations are complex and dangerous.' The doctor refuses to offer false comfort."),
    (4, None, "'And what if we don't do it?' Marina searches for alternatives."),
    (5, None, "'Then the boy will not be able to walk.' The future modal construction describes the consequence."),
    (6, None, "'I am very afraid for the child.' The verb takes the preposition meaning 'for'."),
    (7, 'Тогда что вы решили?', "'Then what have you decided?' The surgeon is impatient to finish the paperwork."),
    (7, 'Время идёт.', "'Time is passing.' Literally 'time is walking'."),
    (8, None, "'I just want to hear the truth.' Marina wants honest medical facts."),
    (9, None, "'If something happens, you must understand.' The conditional clause uses the future tense."),
    (10, None, "'All responsibility lies with you.' The hospital protects itself from legal liability."),
    (11, 'Хорошо.', "'Fine.' Marina surrenders to her desperation."),
    (11, 'Я всё подпишу.', "'I will sign everything.' With a heavy heart, she signs the forms."),
]
