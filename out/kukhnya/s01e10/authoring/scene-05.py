# Authoring module for kukhnya-s01e10-scene-05.
ID = 'kukhnya-s01e10-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 5
TITLE = 'Неожиданное признание  (An Unexpected Confession)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = "At the Claude Monet bar counter, junior cook Max notices Chef Viktor Barinov sitting gloomily with a dark expression. When Max asks what went wrong, expecting another complaint about football or hangovers, Barinov abruptly shocks him by revealing a secret about Victoria's feelings. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine this startling revelation from Barinov line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Leaving Max in absolute disbelief and questioning everything about his future with Victoria, Chef Barinov watches his bewildered expression with grim amusement. Next time you watch the episode, listen for the Russian expressions for 'to be' and 'important' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Здравствуйте, шеф, как ваши дела сегодня?', 'Hello, chef, how are your affairs today?', [(21, 'Здрасте.')], ''),
    ('barinov', 'Макс, не задавай мне глупых вопросов.', 'Max, do not ask me foolish questions.', [], ''),
    ('max', 'Вы опять проиграли деньги на ставках?', 'Did you lose money on bets again?', [(22, 'Опять проигрался?')], ''),
    ('barinov', 'Я бы сейчас с удовольствием выпил водки.', 'I would gladly drink vodka right now.', [(23, 'Да я бы водки хлебнул.')], ''),
    ('max', 'Что ещё неприятного у вас случилось?', 'What else unpleasant has happened to you?', [(24, 'Что случилось?')], ''),
    ('barinov', 'Дело вовсе не в моих ставках.', 'The matter is not at all about my bets.', [], ''),
    ('max', 'А в чём тогда настоящая проблема?', 'Then what is the real problem?', [], ''),
    ('barinov', 'У меня есть для тебя важная новость.', 'I have important news for you.', [], ''),
    ('max', 'Какая новость, шеф, говорите скорее.', 'What news, chef, tell me quickly.', [], ''),
    ('barinov', 'Тётя Вика сказала, что любит тебя.', 'Aunt Vika said that she loves you.', [(25, 'А тетя Вика сказала, что любит тебя.')], ''),
    ('max', 'Что? Этого просто не может быть!', 'What? That simply cannot be!', [], ''),
    ('barinov', 'Она сама призналась мне в этом.', 'She herself confessed this to me.', [], ''),
    ('max', 'Шеф, вы точно не шутите сейчас?', 'Chef, are you definitely not joking right now?', [], ''),
]
WALK = [
    (0, None, "'Hello, chef, how are your affairs today?' Walking up to the bar counter, Max cheerfully greets Chef Barinov and asks how things are going."),
    (1, None, "'Max, do not ask me foolish questions.' Sitting with a dark scowl, Barinov grumbles at Max not to ask him foolish questions."),
    (2, None, "'Did you lose money on bets again?' Knowing his boss's habits, Max guesses that Viktor lost money betting on football again."),
    (3, None, "'I would gladly drink vodka right now.' Barinov expresses this naturally by combining the word for 'now' with 'pleasure' and 'drank'."),
    (4, None, "'What else unpleasant has happened to you?' When Barinov hints at worse trouble, Max asks what other unpleasant news has come up."),
    (5, None, "'The matter is not at all about my bets.' Russian leaves out the word for 'to be' here, linking 'matter' directly with 'at all', followed by 'bets'."),
    (6, None, "'Then what is the real problem?' Russian leaves out the word for 'to be' here, linking 'then' directly with 'real', followed by 'problem'."),
    (7, None, "'I have important news for you.' Barinov leans in and announces that he has an important piece of news specifically for Max."),
    (8, None, "'What news, chef, tell me quickly.' Intrigued and slightly nervous, Max urges the chef to tell him the news right away."),
    (9, None, "'Aunt Vika said that she loves you.' Calling Victoria 'Aunt Vika' in his gruff way, Barinov drops the bombshell that she is in love with Max."),
    (10, None, "'What? That simply cannot be!' Max is completely floored, blurting out that such a thing is simply impossible."),
    (11, None, "'She herself confessed this to me.' Barinov insists it is true, claiming that Vika confessed her feelings to him in person."),
    (12, None, "'Chef, are you definitely not joking right now?' Still reeling from shock, Max asks whether the chef is pulling a prank on him right now."),
]
