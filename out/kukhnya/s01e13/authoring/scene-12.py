# Authoring module for kukhnya-s01e13-scene-12.
ID = 'kukhnya-s01e13-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 12
TITLE = 'Признание  (The Confession)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Nastya knows she should confess to breaking the mirror, but she can't bring herself to do it. Kostya offers to take the blame instead. Their talk comes first, in Russian."
OPENER = 'Again, and listen to who is being brave.'
TRANSITION = 'And the whole exchange again.'
OUTRO = "Kostya is ready to take the blame, and Nastya won't let him. Which of them says 'I broke it' first? Speak soon."
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('nastya', 'Шеф опять с ней ругается.', 'The boss is arguing with her again.', [(164, 'Шеф опять с ней рукается.')], ''),
    ('kostya', 'Да ладно, Настя, всё образуется.', 'Come on, Nastya, everything will work out.', [(165, 'Да ладно, Нась, все образуется.')], ''),
    ('nastya', 'Сегодня у нас тоже ничего не получится?', "Things won't work out for us today either?", [(166, 'сегодня у нас тоже ничего не получится?')], ''),
    ('kostya', 'Нет, Настя, ну ты просто обещала.', 'No, Nastya, you simply promised.', [(168, 'Да нет, Нась, ну ты просто обещала.')], ''),
    ('kostya', 'Хочешь, я пойду к шефу?', 'Do you want me to go to the boss?', [(169, 'хочешь, я пойду к шефу')], ''),
    ('kostya', 'Я скажу, что это я сломал зеркало.', 'I will say that I broke the mirror.', [(169, 'и скажу, что это я сломал его зеркало?')], ''),
    ('nastya', 'Не надо, он тебя уволит.', 'Do not do it, he will fire you.', [(170, 'Не надо, он тебя уволит.')], ''),
    ('kostya', 'Я сказал, значит, я пойду.', 'I said it, which means I will go.', [(172, 'Я сказал, значит, я пойду.')], ''),
    ('nastya', 'Костик, подожди, не ходи.', 'Kostik, wait, do not go.', [(173, 'Костик, подожди, не ходи.')], ''),
    ('kostya', 'Шеф, это я сломал ваше зеркало.', 'Boss, it was me who broke your mirror.', [(164, 'шеф')], ''),
    ('nastya', 'Нет, не верьте ему.', 'No, do not believe him.', [(168, 'нет')], ''),
    ('nastya', 'Это я сломала ваше зеркало.', 'I broke your mirror.', [(169, 'это')], ''),
    ('nastya', 'Он просто хочет меня прикрыть.', 'He just wants to cover for me.', [(168, 'просто')], ''),
]
WALK = [
    (0, None, ["'The boss is arguing with her again.' The word ", ('nastya', 'ругается'), ' means quarrelling loudly, or even swearing, and the reflexive ending is part of the action word. Also, ', ('nastya', 'с'), ('nastya', 'ней'), " means 'with her'."]),
    (1, None, ["'Come on, Nastya, everything will work out.' We will consider this line: ", ('kostya', 'Да'), ('kostya', 'ладно'), " is a cheerful 'come on, it's fine'. And ", ('kostya', 'образуется'), " means 'will take shape' and is used for 'it will sort itself out'."]),
    (2, None, ["'Things won't work out for us today either?' We can focus on this line: ", ('nastya', 'получится'), " is 'will turn out', and with nothing, it means 'nothing will work'. Also, ", ('nastya', 'тоже'), " is 'also'."]),
    (3, None, ["'No, Nastya, you simply promised.' The word ", ('kostya', 'обещала'), " carries a woman's ending. Kostya's pleading word is used in the way Russians often say 'well'."]),
    (4, None, ["'Do you want me to go to the boss?' We can examine the sentence: ", ('kostya', 'Хочешь'), ', ', ('kostya', 'я'), ('kostya', 'пойду'), " says 'want, I will go', leaving out 'that'. Also, ", ('kostya', 'к'), ('kostya', 'шефу'), " is 'to the boss'."]),
    (5, None, ["'I will say that I broke the mirror.' We can examine the sentence: ", ('kostya', 'это'), ('kostya', 'Я'), ('kostya', 'сломал'), " is the handy shape for owning up. The word takes a man's ending since Kostya is speaking."]),
    (6, None, ["'Do not do it, he will fire you.' The expression ", ('nastya', 'Не'), ('nastya', 'надо'), " keeps coming up for 'do not', and it is softer than a shouted order. Nastya begs rather than commands."]),
    (7, None, ["'I said it, which means I will go.' The word ", ('kostya', 'значит'), " means 'so' or 'therefore', and Kostya's logic is that he said he would, so he must."]),
    (8, None, ["'Kostik, wait, do not go.' After 'not', Russians say ", ('nastya', 'не'), ('nastya', 'ходи'), ", rather than the term they would use for a plain 'go'. And ", ('nastya', 'подожди'), ' is an order for a friend.']),
    (9, None, ["'Boss, it was me who broke your mirror.' We can consider the sentence: ", ('kostya', 'ваше'), " carries a polite 'your', with a neuter ending because the mirror is neuter. We hear ", ('kostya', 'это'), ('kostya', 'я'), ('kostya', 'сломал'), ' is used as before, now said to the boss.']),
    (10, None, ["'No, do not believe him.' You believe 'to' someone in Russian, so 'him' is ", ('nastya', 'ему'), '. The order ', ('nastya', 'не'), ('nastya', 'верьте'), ' is the polite form.']),
    (11, None, ["'I broke your mirror.' Nastya's sentence differs from Kostya's by one ending. The word ", ('nastya', 'сломала'), " has a woman's ending, because the person who broke it is a woman."]),
    (12, None, ["'He just wants to cover for me.' The word ", ('nastya', 'прикрыть'), " means 'to cover', in the sense of protecting. Also, ", ('nastya', 'меня'), " is 'me', and ", ('nastya', 'просто'), " means 'simply'."]),
]
