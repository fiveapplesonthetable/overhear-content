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
INTRO = 'Following the disastrous confrontation with the restaurant critic, Nastya rushes to apologize to Kostya for calling him a coward. Before they can reconcile, Chef Barinov storms into the dining hall and abruptly fires the young bartender.'
OPENER = "Let's witness Nastya's sincere apology and Barinov's ruthless dismissal of Kostya following the critic scandal."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Dismissed by an unforgiving Barinov, Kostya leaves the restaurant while Nastya searches for a way to save him. Next time you watch the episode, listen for the Russian expressions for 'bartender' and 'fast' — you will catch every word right away. See you next time!"
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
    (0, None, "'Kostya, wait a second, listen to me please.' Nastya begs her boyfriend to wait a second and listen to her. She desperately wants to talk."),
    (1, None, "'Forgive me for stupidly calling you a coward.' Nastya apologizes for foolishly calling him a coward earlier. She feels terrible about what she said."),
    (2, None, "'You treated me very unfairly.' Kostya tells her that she treated him very unfairly. He is deeply hurt by her words."),
    (3, None, "'I was very mistaken and deeply regret it.' Nastya admits she made a huge mistake and regrets it deeply. She knows she was completely wrong."),
    (4, None, "'Kostya, you are fired, quickly pack your things!' Barinov angrily fires the bartender on the spot and tells him to pack his things fast. He is furious."),
    (5, None, "'Chef, are you really driving me out of work?' Kostya is shocked and asks if the boss is really kicking him out. He cannot believe this is happening."),
    (6, None, "'You caused a scandal with an important restaurant critic!' Barinov yells about the massive scandal caused with the VIP guest. It is an unforgivable offense."),
    (7, None, "'Chef, it is I who am to blame for everything!' Nastya bravely steps in and claims all the blame for herself. She wants to save his job."),
    (8, None, "'I do not care, the bartender leaves right now.' Barinov coldly says he does not care and the guy leaves immediately. He has made up his mind."),
    (9, None, "'All right, chef, I will take off the uniform immediately.' Kostya accepts his fate and agrees to take off his uniform right away. He will not fight it."),
    (10, None, "'We cannot lose the restaurant' Nastya argues they cannot afford to lose their best employee. She is trying everything to change his mind."),
    (11, None, "'Our restaurant will have huge problems now.' Barinov points out the huge problems heading their way now. The business might not survive this."),
    (12, None, "'We must fix everything before the article comes out.' Nastya insists they must fix everything before the terrible article is published. They still have a chance."),
]
