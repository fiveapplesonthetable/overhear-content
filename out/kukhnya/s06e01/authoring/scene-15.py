ID = 'kukhnya-s06e01-scene-15'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 15
TITLE = "Разговор с самим собой  (A Conversation with Himself)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "guest": "anja"}
LABELS = {"guest": "Гость"}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'

INTRO = 'Alone in the kitchen and his office, Barinov confronts the hallucination of Elizaveta Genrikhovna, who tells him bluntly that she is his own conscience speaking back to him.'

STORY = [
    ('guest', 'Не ожидал, Витя?', 'Did you not expect it, Vitya?', [(257, 'Не ожидал?')], 'adapted'),
    ('guest', 'Вас же нет!', 'You are not even here!', [(259, 'вас же нет')], 'adapted'),
    ('guest', 'В твоей голове я до сих пор жива.', 'In your head I am still alive.', [(260, 'в твоей голове я до сих пор жива')], 'exact'),
    ('guest', 'Витя, сходи к врачу.', 'Vitya, go see a doctor.', [(261, 'Витя, сходи к врачу')], 'exact'),
    ('guest', 'Наверняка вы бы этому обрадовались.', 'Surely you would be glad about that.', [(263, 'Наверняка вы бы этому обрадовались')], 'exact'),
    ('guest', 'В твоих бедах ты всегда обвиняешь другого.', 'In your troubles you always blame someone else.', [(265, 'В твоих бедах ты всегда обвиняешь кого-то другого')], 'adapted'),
    ('guest', 'Разрушился брак — виновата теща.', 'The marriage fell apart—the mother-in-law is to blame.', [(266, 'Разрушился брак'), (267, 'Виновата теща')], 'adapted'),
    ('guest', 'Тебя никто не любит и не ценит.', 'Nobody loves you or appreciates you.', [(270, 'Тебя никто не любит, не ценит')], 'adapted'),
    ('guest', 'Тебя все раздражают такого хорошего.', 'Everyone irritates someone as good as you.', [(271, 'Тебя все раздражают такого хорошего')], 'exact'),
    ('guest', 'Что вы обо мне знаете?', 'What do you know about me?', [(272, 'Что вы обо мне знаете?')], 'exact'),
    ('guest', 'Все, что ты сейчас услышал, ты сам себе сказал.', 'Everything you just heard, you said to yourself.', [(275, 'Все, что ты сейчас услышал, это ты сам себе сказал')], 'adapted'),
    ('guest', 'И выводы делать тоже тебе.', 'And the conclusions are yours to draw too.', [(276, 'И выводы делать тоже тебе')], 'exact'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Did you not expect it, Vitya?' the guest raises the pitch on 'expected' to turn the phrase into a direct spoken question. Chef Barinov answers right away."),
    (1, None, "'You are not even here!' Here the Russian phrasing highlights 'you' before landing on 'no'."),
    (2, None, "'In your head I am still alive.' the guest anchors the line on 'your', while 'alive' completes the thought."),
    (3, None, "'Vitya, go see a doctor.' The grammar packs 'go' and 'the doctor' into a tight, idiomatic kitchen exchange. Chef Barinov answers right away."),
    (4, None, "'Surely you would be glad about that.' The plural past ending '-li' on the verb for 'would be glad' covers a group or the polite 'you'."),
    (5, None, "'In your troubles you always blame someone else.' In Russian, the idea of 'your' flows naturally into 'other' without extra filler words."),
    (6, None, "'The marriage fell apart—the mother-in-law is to blame.' The meaning hinges on 'fell apart' working together with 'mother-in-law' in spoken Russian."),
    (7, None, "'Nobody loves you or appreciates you.' The negative particle sits right before the verb meaning 'loves' to negate the statement."),
    (8, None, "'Everyone irritates someone as good as you.' The grammar packs 'you' and 'good' into a tight, idiomatic kitchen exchange."),
    (9, None, "'What do you know about me?' Chef Barinov chooses the respectful plural 'you' alongside 'know' to keep a polite distance. the guest answers right away."),
    (10, None, "'Everything you just heard, you said to yourself.' Spoken Russian keeps this brisk, leaning on 'all' and finishing on 'said'."),
    (11, None, "'And the conclusions are yours to draw too.' The meaning hinges on 'and' working together with 'to you' in spoken Russian."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Taking those words to heart, Barinov decides to finish baking the family cookies himself and make peace with Eleonora. Until next time!'
CLOSING = ("guest", "Хорошего дня!")
