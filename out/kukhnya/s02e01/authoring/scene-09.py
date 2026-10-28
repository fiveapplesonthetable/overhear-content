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
TRANSITION = "Now listen to the phone call between Max and Kostya again. Now let's listen to the whole conversation again from start to finish."
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
    (0, None, "'Hello, Kostya, can you hear me?' Max turns a statement into a question purely through rising intonation on the word meaning 'hello?', followed by 'hear'."),
    (1, None, "'Yes, Max, what happened to you?' Kostya uses the classic Russian possession phrasing — literally 'at you' rather than a verb meaning 'to have' around the word meaning 'happened'."),
    (2, None, "'I have a big problem right now.' Max uses the classic Russian possession phrasing — literally 'at me' rather than a verb meaning 'to have', combining 'now' with 'large' and 'problem'."),
    (3, None, "'Did you already talk with Vika?' Kostya knows Max was trying to apologize to Victoria."),
    (4, None, "'I wanted to talk with her seriously.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (5, None, "'But she just turned around and left!' Both past-tense verbs describe Victoria's quick exit."),
    (6, None, "'Well then come back to the kitchen.' Kostya leads with the direct command form meaning 'return', pairing it with 'back' and 'kitchen'."),
    (7, None, "'That is the thing, I cannot!' This conversational phrase highlights the main problem."),
    (8, None, "'Why can you not come?' Kostya does not understand why Max is still outside."),
    (9, None, "'Because I lost a small key.' Here Max anchors the line on the word meaning 'because' and builds the thought around 'lost' and 'short'."),
    (10, None, "'What key did you lose?' The phrasing opens with 'more' before bringing in 'key' and 'lost' to make the point clear."),
    (11, None, "'Kostya, come out to the street to me urgently!' Max leads with the direct command form meaning 'go out', pairing it with 'urgent' and 'street'."),
    (12, None, "'Fine, wait there, I will come right now.' Kostya agrees to come and help him out."),
]
