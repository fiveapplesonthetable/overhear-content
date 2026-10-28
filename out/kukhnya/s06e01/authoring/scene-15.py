# Authoring module for kukhnya-s06e01-scene-15.
ID = 'kukhnya-s06e01-scene-15'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 15
TITLE = 'Разговор с самим собой  (A Conversation with Himself)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = 'Alone in the kitchen and his office, Barinov confronts the hallucination of Elizaveta Genrikhovna, who tells him bluntly that she is his own conscience speaking back to him.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Taking those words to heart, Barinov decides to finish baking the family cookies himself and make peace with Eleonora. Until next time!'
CLOSING = ('barinov', 'Хорошего дня!')
STORY = [
    ('guest', 'Не ожидал, Витя?', 'Did you not expect it, Vitya?', [(257, 'Не ожидал?')], 'adapted'),
    ('barinov', 'Вас же нет!', 'You are not even here!', [(259, 'вас же нет')], 'adapted'),
    ('guest', 'В твоей голове я до сих пор жива.', 'In your head I am still alive.', [(260, 'в твоей голове я до сих пор жива')], 'exact'),
    ('guest', 'Витя, сходи к врачу.', 'Vitya, go see a doctor.', [(261, 'Витя, сходи к врачу')], 'exact'),
    ('barinov', 'Наверняка вы бы этому обрадовались.', 'Surely you would be glad about that.', [(263, 'Наверняка вы бы этому обрадовались')], 'exact'),
    ('guest', 'В твоих бедах ты всегда обвиняешь другого.', 'In your troubles you always blame someone else.', [(265, 'В твоих бедах ты всегда обвиняешь кого-то другого')], 'adapted'),
    ('guest', 'Разрушился брак — виновата теща.', 'The marriage fell apart—the mother-in-law is to blame.', [(266, 'Разрушился брак'), (267, 'Виновата теща')], 'adapted'),
    ('guest', 'Тебя никто не любит и не ценит.', 'Nobody loves you or appreciates you.', [(270, 'Тебя никто не любит, не ценит')], 'adapted'),
    ('guest', 'Тебя все раздражают такого хорошего.', 'Everyone irritates someone as good as you.', [(271, 'Тебя все раздражают такого хорошего')], 'exact'),
    ('barinov', 'Что вы обо мне знаете?', 'What do you know about me?', [(272, 'Что вы обо мне знаете?')], 'exact'),
    ('guest', 'Все, что ты сейчас услышал, ты сам себе сказал.', 'Everything you just heard, you said to yourself.', [(275, 'Все, что ты сейчас услышал, это ты сам себе сказал')], 'adapted'),
    ('guest', 'И выводы делать тоже тебе.', 'And the conclusions are yours to draw too.', [(276, 'И выводы делать тоже тебе')], 'exact'),
]
WALK = [
    (0, None, "'Did you not expect it, Vitya?' The guest quizzes eagerly whether Barinov really thought this through."),
    (1, None, '\'You are not even here!\' Speaking evenly with the guest, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (2, None, '\'In your head I am still alive.\' Addressing the head with Barinov, the guest links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (3, None, "'Vitya, go see a doctor.' The guest steps in earnestly facing Barinov, making his position completely clear."),
    (4, None, '\'Surely you would be glad about that.\' Barinov opens up boldly at once and centers the thought on "obradovalis" ("would be glad", from "obradovatsya") without wasting a word.'),
    (5, None, "'In your troubles you always blame someone else.' The guest jumps in right away during the talk, keeping the focus on what actually matters here."),
    (6, None, "'The marriage fell apart—the mother-in-law is to blame.' The guest follows up right away without holding back, shifting the mood of the conversation in a single beat."),
    (7, None, '\'Nobody loves you or appreciates you.\' The guest answers dryly before Barinov and uses "lyubit" ("loves") to carry the main weight of the thought.'),
    (8, None, "'Everyone irritates someone as good as you.' The guest continues evenly with a shrug, bringing things back to earth after the buildup."),
    (9, None, "'What do you know about me?' Barinov presses calmly where this conversation is heading next."),
    (10, None, '\'Everything you just heard, you said to yourself.\' The guest responds frankly during the talk and chooses "uslyshal" ("heard", from the root "uslyshat") so Barinov hears the exact meaning.'),
    (11, None, "'And the conclusions are yours to draw too.' The guest cuts in bluntly around Barinov, testing Barinov's reaction in the middle of the exchange."),
]
