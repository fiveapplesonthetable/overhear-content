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
    (0, None, '\'But this is a secret vote, after all.\' Even though this is a secret vote after all, Fedya keeps a steady face in front of Senya. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (1, None, "'Go on out of here, call the next person in.' Here going on out of here call the next person sets up the next turn in their exchange."),
    (2, None, "'Good afternoon, I have a question.' Having a question is how Senya lays out the situation for Fedya."),
    (3, None, '\'Can the independent observer not watch?\' Checking whether the independent observer not watch cuts straight through the tension between Senya and Fedya. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (4, None, "'No, one cannot do that at all.' Adding that one cannot do that at all fills in the missing piece for Fedya. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (5, None, "'Understood, and what if like this?' Questioning whether understood and what if like this is how Senya tests Fedya's story."),
    (6, None, '\'Great, now you have voted fairly.\' Since great now Fedya has voted fairly, Timur does not waste words on excuses. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (7, None, "'Let us sum up the results of our fair contest.' Realizing that they should sum up the results of their fair contest changes how Timur handles the situation."),
    (8, None, "'Today Arseny won the election!' Declaring that today won the election brings Timur's temper right to the surface."),
    (9, None, '\'How did he suddenly win like that?\' Here wondering how he suddenly win like shows Fedya looking for the real truth. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (10, None, '\'Does anyone have any objections right now?\' By asking whether anyone have any objections right now, Timur presses Fedya for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (11, None, "'You can take the ballots for salad.' Timur mentions that Fedya can take the ballots for salad so Fedya sees what is at stake."),
]
