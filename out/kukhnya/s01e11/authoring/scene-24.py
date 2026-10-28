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
    (0, None, "'Kostya, wait a second, listen to me please.' Nastya catches up with the despondent bartender."),
    (1, None, "'Forgive me for stupidly calling you a coward.' Nastya uses the action verb meaning 'to forgive' to focus on the single completed result, pairing it with 'stupidly' and 'to call'."),
    (2, None, "'You treated me very unfairly.' Kostya uses the action verb meaning 'to enter' to focus on the single completed result, pairing it with 'very' and 'unfairly'."),
    (3, None, "'I was very mistaken and deeply regret it.' Nastya expresses this naturally by combining the word for 'strongly' with 'to make a mistake' and 'very'."),
    (4, None, "'Kostya, you are fired, quickly pack your things!' Barinov shouts ruthlessly across the dining room."),
    (5, None, "'Chef, are you really driving me out of work?' Kostya turns a statement into a question purely through rising intonation on the word meaning 'boss', pairing it with 'to drive out' and 'work'."),
    (6, None, "'You caused a scandal with an important restaurant critic!' Chef Barinov uses the action verb meaning 'to arrange' to focus on the single completed result, pairing it with 'scandal' and 'important'."),
    (7, None, "'Chef, it is I who am to blame for everything!' Russian omits the present-tense verb 'to be' here, linking 'boss' directly with 'guilty', combining 'boss' with 'guilty'."),
    (8, None, "'I do not care, the bartender leaves right now.' Chef Barinov puts the word for 'equally' together with 'bartender' and 'to leave' in a crisp, natural spoken turn of phrase."),
    (9, None, "'All right, chef, I will take off the uniform immediately.' Here Kostya anchors the line on the word meaning 'well' and builds the thought around 'boss' and 'now'."),
    (10, None, "'We cannot lose the restaurant' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (11, None, "'Our restaurant will have huge problems now.' Chef Barinov expresses this naturally by combining the word for 'restaurant' with 'now' and 'to be'."),
    (12, None, "'We must fix everything before the article comes out.' Nastya puts the word for 'due' together with 'to fix' and 'exit' in a crisp, natural spoken turn of phrase."),
]
