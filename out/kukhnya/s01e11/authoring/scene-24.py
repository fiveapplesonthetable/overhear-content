# Authoring module for kukhnya-s01e11-scene-24.
ID = 'kukhnya-s01e11-scene-24'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 24
TITLE = 'Трус и увольнение  (The Coward and the Firing)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = 'The chef has heard what Kostya did, and he is about to deal with it. Nastya apologises to Kostya first, in the kitchen corridor. Just listen, and see how much you pick up.'
OPENER = 'This time, with explanations.'
TRANSITION = 'Once more, at the pace of a real conversation.'
OUTRO = "Kostya is fired, and Nastya wants him back. The two of them have only a few hours before the critic's article comes out. Back soon."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Костя, подожди секунду, выслушай меня пожалуйста.', 'Kostya, wait a second, listen to me please.', [], ''),
    ('nastya', 'Прости, что я глупо назвала тебя трусом.', 'Forgive me for stupidly calling you a coward.', [(312, 'Прости, что назвала тебя трусом.')], ''),
    ('kostya', 'Ты поступила со мной очень несправедливо.', 'You treated me very unfairly.', [], ''),
    ('nastya', 'Я сильно ошиблась и очень сожалею об этом.', 'I was very mistaken and deeply regret it.', [], ''),
    ('barinov', 'Костя, ты уволен, быстро собирай свои вещи!', 'Kostya, you are fired, quickly pack your things!', [(313, 'Костя, ты уволец, собирай вещи.')], ''),
    ('kostya', 'Шеф, неужели вы выгоняете меня с работы?', 'Chef, are you really driving me out of work?', [], ''),
    ('barinov', 'Ты устроил скандал с важным ресторанным критиком!', 'You caused a scandal with an important restaurant critic!', [], ''),
    ('nastya', 'Шеф, это я во всём виновата!', 'Chef, it is I who am to blame for everything!', [], ''),
    ('barinov', 'Мне всё равно, бармен уходит прямо сейчас.', 'I do not care, the bartender leaves right now.', [], ''),
    ('kostya', 'Хорошо, шеф, я сейчас же сниму форму.', 'All right, chef, I will take off the uniform immediately.', [], ''),
    ('nastya', 'Мы не можем потерять лучшего бармена ресторана.', "We cannot lose the restaurant's best bartender.", [], ''),
    ('barinov', 'У нашего ресторана сейчас будут огромные проблемы.', 'Our restaurant will have huge problems now.', [(319, 'Я думаю, у нас большие проблемы.')], ''),
    ('nastya', 'Мы должны всё исправить до выхода статьи.', 'We must fix everything before the article comes out.', [], ''),
]
WALK = [
    (0, None, ["'Kostya, wait a second, listen to me please.' Now let's inspect the speech: ", ('nastya', 'выслушай'), ' has a prefix so Nastya asks him to listen to the end. ', ('nastya', 'подожди'), ' means wait. She uses familiar address with him, and she is gentle.']),
    (1, None, ["'Forgive me for stupidly calling you a coward.' After called, the coward changes its ending, becoming ", ('nastya', 'трусом'), '. ', ('nastya', 'Прости'), ' means forgive. Now it is her turn.']),
    (2, None, ["'You treated me very unfairly.' We will break down this part: ", ('kostya', 'несправедливо'), ' means not fairly, made from the term for justice. ', ('kostya', 'поступила'), ' means acted. Kostya is hurt.']),
    (3, None, ["'I was very mistaken and deeply regret it.' We will analyze the dialogue: ", ('nastya', 'ошиблась'), ' means was mistaken, and has the feminine ending. ', ('nastya', 'сожалею'), ' means I regret. Nastya apologises in full.']),
    (4, None, ["'Kostya, you are fired, quickly pack your things!' Now let's break down this part: ", ('barinov', 'уволен'), ' is fired. ', ('barinov', 'собирай'), ' means pack, but literally reads collect. ', ('barinov', 'свои'), ('barinov', 'вещи'), ' means your things. Barinov is blunt.']),
    (5, None, ["'Chef, are you really driving me out of work?' We can break down the phrase: ", ('kostya', 'выгоняете'), ' is drive out, with the prefix for out. ', ('kostya', 'с'), ('kostya', 'работы'), ' is from work. ', ('kostya', 'неужели'), ' is can it really be. Kostya cannot believe it.']),
    (6, None, ["'You caused a scandal with an important restaurant critic!' Now we can examine this line: ", ('barinov', 'устроил'), ('barinov', 'скандал'), ' means arranged a scandal, and is the idiom for made a scene. ', ('barinov', 'с'), ('barinov', 'важным'), ('barinov', 'ресторанным'), ('barinov', 'критиком'), ' means with an important restaurant critic. Barinov is stern.']),
    (7, None, ["'Chef, it is I who am to blame for everything!' We will examine this line: ", ('nastya', 'виновата'), ' means guilty, and is a short form with a feminine ending. ', ('nastya', 'во'), ('nastya', 'всём'), ' means in everything. Nastya takes the blame, and it is a brave thing to do.']),
    (8, None, ["'I do not care, the bartender leaves right now.' Now let's break down the phrase: ", ('barinov', 'Мне'), ('barinov', 'всё'), ('barinov', 'равно'), ' is the idiom Barinov used about the critic in the soup scene. ', ('barinov', 'бармен'), ' means bartender. ', ('barinov', 'прямо'), ('barinov', 'сейчас'), ' is right now.']),
    (9, None, ["'All right, chef, I will take off the uniform immediately.' We will analyze this line: ", ('kostya', 'форму'), ' is the uniform. ', ('kostya', 'сниму'), ' means I will take off. Kostya accepts, with dignity.']),
    (10, None, ["'We cannot lose the restaurant's best bartender.' Now let's look at the dialogue: ", ('nastya', 'потерять'), ' means to lose. ', ('nastya', 'лучшего'), ' means best, and grows from better. Nastya includes herself in the consequences.']),
    (11, None, ["'Our restaurant will have huge problems now.' Now we can examine the words: ", ('barinov', 'У'), ('barinov', 'нашего'), ('barinov', 'ресторана'), ('barinov', 'сейчас'), ('barinov', 'будут'), ' means at our restaurant will be, which is the pattern for will have. ', ('barinov', 'огромные'), ' is huge. Barinov knows what the article could say.']),
    (12, None, ["'We must fix everything before the article comes out.' Let's analyze the dialogue: ", ('nastya', 'до'), ('nastya', 'выхода'), ('nastya', 'статьи'), ' is before the exit of the article, where exit means a publication coming out. ', ('nastya', 'исправить'), ' is to fix. Nastya sets the deadline.']),
]
