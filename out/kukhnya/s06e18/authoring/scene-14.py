# Authoring module for kukhnya-s06e18-scene-14.
ID = 'kukhnya-s06e18-scene-14'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 18
SCENE = 14
TITLE = 'Тайное голосование  (The Secret Ballot)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'senya': 'Сеня', 'timur': 'Тимур'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.18'
SOURCE_FILE = 'sources/kukhnya/s06/e18.ru.srt'
INTRO = 'In the storage room, Timur presides over the kitchen vote while standing right inside the voting booth. After accepting a discreet cash bribe, Timur looks the other way and announces that Senya has won the election seven to three.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Senya's celebration as elected kitchen chief lasts only seconds before his discounted fish takes its revenge. See you next time!"
CLOSING = ('senya', 'Увидимся!')
STORY = [
    ('fedya', 'Но это же тайное голосование.', 'But this is a secret vote, after all.', [(237, 'голосование'), (238, 'тайное')], 'adapted'),
    ('timur', 'Иди отсюда, позови сюда следующего.', 'Go on out of here, call the next person in.', [(238, 'иди отсюда'), (239, 'Позови следующего')], 'adapted'),
    ('senya', 'Добрый день, у меня вопрос.', 'Good afternoon, I have a question.', [(241, 'Добрый день'), (242, 'Так у меня вопрос')], 'adapted'),
    ('senya', 'Независимый наблюдатель может не наблюдать?', 'Can the independent observer not watch?', [(242, 'Наблюдатель может не наблюдать')], 'adapted'),
    ('timur', 'Нет, так делать совсем нельзя.', 'No, one cannot do that at all.', [(243, 'Нет')], 'adapted'),
    ('senya', 'Понятно, а если вот так?', 'Understood, and what if like this?', [(243, 'Понятно. А если так')], 'adapted'),
    ('timur', 'Отлично, теперь ты честно проголосовал.', 'Great, now you have voted fairly.', [(245, 'Проголосовал')], 'adapted'),
    ('timur', 'Подводим итоги нашей честной борьбы.', 'Let us sum up the results of our fair contest.', [(246, 'честной борьбе')], 'adapted'),
    ('timur', 'Сегодня в выборах победил Арсений!', 'Today Arseny won the election!', [(247, 'победил Арсений')], 'adapted'),
    ('fedya', 'Как это он вдруг победил?', 'How did he suddenly win like that?', [(247, 'победил')], 'adapted'),
    ('timur', 'У кого-нибудь есть сейчас возражения?', 'Does anyone have any objections right now?', [(248, 'возражений нет')], 'adapted'),
    ('timur', 'Можете забирать бюллетени на салат.', 'You can take the ballots for salad.', [(248, 'можете забирать бюллетени на салат')], 'adapted'),
]
WALK = [
    (0, None, '\'But this is a secret vote, after all.\' Fedya frames that reply with warmth: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (1, None, "'Go on out of here, call the next person in.' Timur answers wryly toward Senya, bringing things back to earth after the buildup."),
    (2, None, '\'Good afternoon, I have a question.\' Senya picks one key choice for Fedya: "dobryy" means "good", and it carries the main weight of what Senya is saying.'),
    (3, None, "'Can the independent observer not watch?' Senya phrases the remark frankly here: Russian keeps the exact word order of a normal statement here, turning it into a question for Timur purely through rising pitch at the end."),
    (4, None, "'No, one cannot do that at all.' Timur speaks up evenly with a sigh, testing Fedya's reaction in the middle of the exchange."),
    (5, None, '\'Understood, and what if like this?\' Senya leans on this vivid piece in reply: "ponyatno" means "clear", and it carries the main weight of what Senya is saying.'),
    (6, None, '\'Great, now you have voted fairly.\' Timur gives that answer plainly here: the single Russian word "otlichno" ("great, excellent") sets up the whole statement without needing a separate word for "it is".'),
    (7, None, "'Let us sum up the results of our fair contest.' Timur steps in decisively without holding back, refusing to let the moment slip past."),
    (8, None, '\'Today Arseny won the election!\' Timur emphasizes one colorful element at once: "vyborakh" means "election" (from "vybory"), giving the line its exact edge.'),
    (9, None, '\'How did he suddenly win like that?\' Fedya gives the comeback frankly here: putting the question word "kak" right at the front of the line lets Timur hear the point of the question on the very first beat.'),
    (10, None, "'Does anyone have any objections right now?' Timur questions promptly where this conversation is heading next."),
    (11, None, '\'You can take the ballots for salad.\' Timur focuses on this sharp piece in reply: "byulleteni" means "ballots" (from "byulleten"), giving the line its exact edge.'),
]
