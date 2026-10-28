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
    (0, None, '\'But this is a secret vote, after all.\' Returning to the voting on the spot, Fedya links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (1, None, "'Go on out of here, call the next person in.' Timur opens up wryly during the talk, before Fedya can change the subject."),
    (2, None, '\'Good afternoon, I have a question.\' Senya promptly extends this daytime greeting at the start of the beat using "dobryy den" ("good afternoon") — literally "good day", the standard Russian greeting from late morning through afternoon.'),
    (3, None, "'Can the independent observer not watch?' Addressing the independent observer on the spot, Senya keeps normal statement word order here, turning the line into a question for Timur purely through rising pitch."),
    (4, None, "'No, one cannot do that at all.' Timur speaks up evenly facing Senya, keeping the focus on what actually matters here."),
    (5, None, '\'Understood, and what if like this?\' Senya plainly sends this acknowledgment for Timur using "ponyatno" ("understood") — a single word meaning "clear, got it", showing the point has landed.'),
    (6, None, '\'Great, now you have voted fairly.\' Holding firm directly in front of Senya, Timur leans on "otlichno" ("great, excellent"), which carries the whole predicate in Russian without needing "it is".'),
    (7, None, "'Let us sum up the results of our fair contest.' Timur weighs in decisively with Senya, to clear the air between them once and for all."),
    (8, None, '\'Today Arseny won the election!\' Underscoring the election on the spot, Timur centers the thought on "vyborakh" ("election", from "vybory") without wasting a word.'),
    (9, None, '\'How did he suddenly win like that?\' Stepping in boldly to Timur, Fedya puts the question word "kak" right at the start so Timur hears the focus immediately.'),
    (10, None, "'Does anyone have any objections right now?' Timur questions promptly where this conversation is heading next."),
    (11, None, '\'You can take the ballots for salad.\' Highlighting the ballots beside Fedya, Timur leans on "byulleteni" ("ballots", a form of "byulleten") to give the remark its edge.'),
]
