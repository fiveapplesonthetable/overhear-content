# Authoring module for kukhnya-s03e01-scene-12.
ID = 'kukhnya-s03e01-scene-12'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 12
TITLE = "Заговор официантов  (The Waiters' Conspiracy)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = 'Determined to get rid of the molecular menu, Chef Barinov secretly gathers the waiters and offers them ten thousand rubles each if no guest orders a molecular dish all week.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'That ends our twelfth scene. Watch how quickly the waiters tell every curious diner that the new molecular menu is pure chemistry from an inexperienced cook. See you next time!'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('barinov', 'Я вас не особо люблю.', 'I am not particularly fond of you.', [(223, 'Я вас не особо люблю')], ''),
    ('barinov', 'И знаю, что это взаимно.', 'And I know that it is mutual.', [(223, 'и знаю, что это взаимно')], ''),
    ('barinov', 'Если до конца недели никто не закажет...', 'If until the end of the week nobody orders...', [(224, 'если до конца недели'), (225, 'закажет')], 'adapted'),
    ('barinov', 'Договорились?', 'Do we have a deal?', [(227, 'Договорились')], ''),
    ('nastya', 'Да, шеф. Я всё сделаю, шеф.', 'Yes, Chef. I will do everything, Chef.', [(227, 'Да, шеф'), (230, 'Я все сделаю, шеф')], 'adapted'),
    ('nastya', 'Виктор Петрович, я думаю, это нечестно.', 'Viktor Petrovich, I think this is unfair.', [(228, 'Виктор Петрович, я думаю, это нечестно')], ''),
    ('barinov', 'Я уберу из меню молочного ягнёнка.', 'I will remove the milk-fed lamb from the menu.', [(229, 'Я уберу из меню молочного ягненка')], ''),
    ('guest', 'Скажите, а что это за молекулярная кухня?', 'Tell me, what is this molecular cuisine?', [(231, 'Скажите, а что это за молекулярная кухня')], ''),
    ('nastya', 'Вы знаете, я бы вам не советовал.', 'You know, I would not advise you to get it.', [(232, 'Вы знаете, я бы вам не советовал')], ''),
    ('nastya', 'Сплошная химия, и очень дорого.', 'Pure chemicals, and very expensive.', [(233, 'сплошная химия, во-вторых, очень дорого')], 'adapted'),
    ('nastya', 'Я бы не советовала вам это заказывать.', 'I would not advise you to order this.', [(237, 'Я бы не советовала вам это заказывать')], ''),
    ('nastya', 'Повар новый, неопытный.', 'The cook is new and inexperienced.', [(238, 'Повар новый, неопытный')], ''),
]
WALK = [
    (0, None, '\'I am not particularly fond of you.\' Barinov tells the guest that he is not particularly fond of the guest without dressing it up. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (1, None, "'And I know that it is mutual.' Adding that he knows that it is mutual fills in the missing piece for the guest."),
    (2, None, '\'If until the end of the week nobody orders...\' Adding that if until the end of the week nobody orders fills in the missing piece for the guest. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
    (3, None, '\'Do we have a deal?\' By checking whether they have a deal, Barinov presses the guest for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (4, None, "'Yes, Chef. I will do everything, Chef.' Since she will do everything, Nastya does not waste words on excuses."),
    (5, None, '\'Viktor Petrovich, I think this is unfair.\' Realizing that she thinks this is unfair changes how Nastya handles the situation. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (6, None, "'I will remove the milk-fed lamb from the menu.' Saying that he will remove the milk fed lamb from the menu is how Barinov sets the tone with the guest."),
    (7, None, "'Tell me, what is this molecular cuisine?' When the guest asks if tell him what is this molecular cuisine, Barinov has to answer fast."),
    (8, None, '\'You know, I would not advise you to get it.\' Explaining that she would not advise Barinov to get it lays the cards on the table for Barinov. Even in the middle of the drama, she keeps the polite plural "you" that workplace Russian expects.'),
    (9, None, "'Pure chemicals, and very expensive.' With the truth and menu in play, Nastya keeps this short reply brisk and direct."),
    (10, None, "'I would not advise you to order this.' Claiming that she would not advise Barinov to order this sounds confident, even if Barinov has doubts."),
    (11, None, "'The cook is new and inexperienced.' Pointing out that the cook is new and inexperienced gives Barinov a sobering reality check."),
]
