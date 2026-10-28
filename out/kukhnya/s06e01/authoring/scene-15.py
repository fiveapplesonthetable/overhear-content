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
    (0, None, '\'Did you not expect it, Vitya?\' Checking whether Barinov not expect it is how the guest puts Barinov on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (1, None, "'You are not even here!' Insisting that the guest is not even here shows Barinov is not backing down."),
    (2, None, "'In your head I am still alive.' Saying that in Barinov's head he is still alive is how the guest sets the tone with Barinov."),
    (3, None, "'Vitya, go see a doctor.' Even though Barinov should go see a doctor, the guest keeps a steady face in front of Barinov."),
    (4, None, "'Surely you would be glad about that.' Adding that surely the guest would be glad fills in the missing piece for the guest."),
    (5, None, '\'In your troubles you always blame someone else.\' Around the plan and room, the guest sets a calm, everyday tone with Barinov. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (6, None, '\'The marriage fell apart—the mother-in-law is to blame.\' Since the marriage fell apart the mother in law is to blame, the guest does not waste words on excuses. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (7, None, "'Nobody loves you or appreciates you.' Mentioning that nobody loves Barinov or appreciates Barinov moves the talk in a new direction."),
    (8, None, '\'Everyone irritates someone as good as you.\' Around the room and kitchen, the guest sets a calm, everyday tone with Barinov. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (9, None, '\'What do you know about me?\' Here wondering what the guest knows about him shows Barinov looking for the real truth. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (10, None, "'Everything you just heard, you said to yourself.' Explaining that everything Barinov just heard Barinov said to themselves lays the cards on the table for Barinov."),
    (11, None, '\'And the conclusions are yours to draw too.\' The guest mentions that the conclusions are Barinov\'s to draw so Barinov sees what is at stake. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
]
