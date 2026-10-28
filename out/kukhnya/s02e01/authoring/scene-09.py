# Authoring module for kukhnya-s02e01-scene-09.
ID = 'kukhnya-s02e01-scene-09'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 1
SCENE = 9
TITLE = 'Звонок другу  (Calling a Friend)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.01'
SOURCE_FILE = 'sources/kukhnya/s02/e01.ru.dual.srt'
INTRO = 'Stranded outside after Victoria walks away, Max pulls out his phone and calls his best friend Kostya at the bar. He confesses that his attempt to talk to Victoria failed and begs Kostya to come outside and rescue him.'
OPENER = 'Listen to Max calling Kostya for help after getting stuck outside.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Only a loyal friend like Kostya will drop his work at the bar to rescue Max from his latest blunder. Next time you watch the episode, listen for the Russian expressions for 'to hear' and 'to happen' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Алло, Костя, ты меня слышишь?', 'Hello, Kostya, can you hear me?', [(140, 'Алло, Костян')], ''),
    ('kostya', 'Да, Макс, что у тебя случилось?', 'Yes, Max, what happened to you?', [(140, 'Алло, Костян')], ''),
    ('max', 'У меня сейчас большая проблема.', 'I have a big problem right now.', [(140, 'Алло, Костян')], ''),
    ('kostya', 'Ты уже поговорил с Викой?', 'Did you already talk with Vika?', [(140, 'Костян')], ''),
    ('max', 'Я хотел с ней серьёзно поговорить.', 'I wanted to talk with her seriously.', [(140, 'Алло')], ''),
    ('max', 'Но она просто развернулась и ушла!', 'But she just turned around and left!', [(140, 'Костян')], ''),
    ('kostya', 'Ну и возвращайся обратно на кухню.', 'Well then come back to the kitchen.', [(140, 'Алло, Костян')], ''),
    ('max', 'В том-то и дело, что не могу!', 'That is the thing, I cannot!', [(140, 'Алло')], ''),
    ('kostya', 'Почему ты не можешь прийти?', 'Why can you not come?', [(140, 'Костян')], ''),
    ('max', 'Потому что я потерял маленький ключ.', 'Because I lost a small key.', [(140, 'Алло, Костян')], ''),
    ('kostya', 'Какой ещё ключ ты потерял?', 'What key did you lose?', [(140, 'Костян')], ''),
    ('max', 'Костя, срочно выходи ко мне на улицу!', 'Kostya, come out to the street to me urgently!', [(140, 'Алло, Костян')], ''),
    ('kostya', 'Ладно, жди там, сейчас приду.', 'Fine, wait there, I will come right now.', [(140, 'Костян')], ''),
]
WALK = [
    (0, None, "'Hello, Kostya, can you hear me?' Stuck outside, Max calls Kostya and checks if he can hear him."),
    (1, None, "'Yes, Max, what happened to you?' Kostya answers and asks what is going on."),
    (2, None, "'I have a big problem right now.' Max confesses that he has landed himself in serious trouble."),
    (3, None, "'Did you already talk with Vika?' Kostya knows Max was trying to apologize to Victoria."),
    (4, None, "'I wanted to talk with her seriously.' He explains that he wanted to have a serious talk with Vika."),
    (5, None, "'But she just turned around and left!' Instead of listening, Vika simply turned on her heel and walked away."),
    (6, None, "'Well then come back to the kitchen.' Not knowing about the handcuffs, Kostya tells him to just head back to the kitchen."),
    (7, None, "'That is the thing, I cannot!' This conversational phrase highlights the main problem."),
    (8, None, "'Why can you not come?' Kostya does not understand why Max is still outside."),
    (9, None, "'Because I lost a small key.' Max sheepishly admits why he is stuck: he lost the little key."),
    (10, None, "'What key did you lose?' Kostya is baffled and asks what key Max is talking about."),
    (11, None, "'Kostya, come out to the street to me urgently!' Max begs Kostya to hurry out to the street and rescue him."),
    (12, None, "'Fine, wait there, I will come right now.' Kostya agrees to come and help him out. Now listen to the phone call between Max and Kostya again."),
]
