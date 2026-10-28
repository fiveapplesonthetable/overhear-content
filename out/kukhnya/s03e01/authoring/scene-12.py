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
    (0, None, "'I am not particularly fond of you.' Barinov responds steadily across the room, letting the remark speak for itself."),
    (1, None, '\'And I know that it is mutual.\' Barinov answers naturally around Nastya and centers the remark on "vzaimno" ("likewise, mutually") without any extra fuss.'),
    (2, None, '\'If until the end of the week nobody orders...\' Discussing the ending before Nastya, Barinov pairs the negative word with "ne" ("not"), since Russian naturally doubles its negatives for emphasis.'),
    (3, None, '\'Do we have a deal?\' Barinov casually speaks this word of agreement for Nastya using "dogovorilis" ("deal") — literally "we have talked it through to an agreement", used just like "deal!" or "settled!".'),
    (4, None, '\'Yes, Chef. I will do everything, Chef.\' Nastya speaks frankly during the talk and lands on "sdelayu" ("I\'ll do", built on "sdelat") to keep the statement grounded.'),
    (5, None, '\'Viktor Petrovich, I think this is unfair.\' Nastya proceeds decisively before Barinov and lands on "nechestno" ("unfair, not fair") as the key everyday word here.'),
    (6, None, "'I will remove the milk-fed lamb from the menu.' Barinov replies earnestly on the spot, refusing to let the moment slip past."),
    (7, None, '\'Tell me, what is this molecular cuisine?\' Noting how molecular things are to Nastya, the guest brings in "molekulyarnaya" ("molecular", from "molekulyarnyy") as the key Russian word here.'),
    (8, None, "'You know, I would not advise you to get it.' Nastya counters dryly without a pause, letting the remark speak for itself."),
    (9, None, "'Pure chemicals, and very expensive.' Nastya fires back promptly hearing the guest, testing the guest's reaction in the middle of the exchange."),
    (10, None, '\'I would not advise you to order this.\' Nastya responds pointedly before the guest and centers the thought on "sovetovala" ("to advise, recommend", from "sovetovat") without wasting a word.'),
    (11, None, '\'The cook is new and inexperienced.\' Making clear how inexperienced things are on the spot, Nastya links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
]
