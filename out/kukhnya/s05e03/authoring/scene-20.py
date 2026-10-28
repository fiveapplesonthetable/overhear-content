# Authoring module for kukhnya-s05e03-scene-20.
ID = 'kukhnya-s05e03-scene-20'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 3
SCENE = 20
TITLE = 'Спасение Дениса и новый Аркадий  (Saving Denis and the New Arkady)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'denis': 'Денис', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.03'
SOURCE_FILE = 'sources/kukhnya/s05/e03.ru.srt'
INTRO = 'In the closing scene of Episode 3, Kostya and Nastya smuggle Denis out of room 205 on a laundry cart just before Eleonora opens the door, and Katya tells her father why Eleonora decided to keep him on. Listen to the finale.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that brings Episode 3 to a close as Denis narrowly escapes Eleonora's trap, though his guilty secret still weighs on him. See you in Episode 4. See you next time!"
CLOSING = ('katya', 'Пока!')
STORY = [
    ('katya', 'Мама, пойдём скорее отсюда.', "Mom, let's get out of here quickly.", [(351, 'Мам, пойдем?')], 'adapted'),
    ('katya', 'Может быть, он сейчас в душе.', 'Maybe he is in the shower right now.', [(352, 'Может быть, он в душе')], 'verbatim'),
    ('denis', 'Отпусти его, они уже ушли!', 'Let him go, they have left already!', [(353, 'его, они ушли!')], 'adapted'),
    ('denis', 'Слабость может превратиться в большую тайну.', 'A weakness can turn into a big secret.', [(355, 'слабость'), (355, 'тайну')], 'adapted'),
    ('denis', 'Тайна может разрушить нам всю жизнь.', 'A secret can destroy our whole life.', [(356, 'разрушить нам жизнь')], 'adapted'),
    ('barinov', 'Поздравляю тебя с новосельем!', 'Congratulations on your housewarming!', [(357, 'С новосельем!')], 'adapted'),
    ('barinov', 'Они у меня долго не живут.', 'They do not live long with me.', [(359, 'Да, они у меня долго не живут')], 'verbatim'),
    ('denis', 'Кто-то хранит тайны ради своих близких.', 'Someone keeps secrets for the sake of loved ones.', [(360, 'Кто-то хранит тайны ради своих близких')], 'verbatim'),
    ('barinov', 'Твоя мама меня почему-то не увольняет.', 'For some reason your mom is not firing me.', [(361, 'меня не увольняет')], 'adapted'),
    ('barinov', 'Она обещала. Не знаешь почему?', 'She promised to. Do you know why?', [(362, 'Обещала. Не знаешь почему?')], 'verbatim'),
    ('katya', 'Да, папа, я это знаю.', 'Yes, Dad, I know why.', [(363, 'Знаю')], 'adapted'),
    ('katya', 'Потому что ты очень крутой шеф.', 'Because you are a really cool chef.', [(364, 'Ты крутой шеф')], 'adapted'),
    ('denis', 'Кто-то готов разлучить близких людей.', 'Someone is ready to separate close people.', [(366, 'Кто-то готов разлучить близких людей')], 'verbatim'),
    ('denis', 'А кто-то не может доверить тайну себе.', 'And someone cannot entrust a secret even to himself.', [(368, 'кто-то не может доверить тайну'), (368, 'себе')], 'adapted'),
]
WALK = [
    (0, None, "'Mom, let's get out of here quickly.' Adding that Mom let them get out of here quickly fills in the missing piece for Barinov."),
    (1, None, "'Maybe he is in the shower right now.' Katya tells Barinov that maybe he is in the shower right now without dressing it up."),
    (2, None, "'Let him go, they have left already!' Declaring that Barinov should let him go they have left already brings Denis's temper right to the surface."),
    (3, None, "'A weakness can turn into a big secret.' Mentioning that a weakness can turn into a big secret moves the talk in a new direction."),
    (4, None, "'A secret can destroy our whole life.' Denis reminds Barinov that a secret can destroy their whole life before the moment passes."),
    (5, None, "'Congratulations on your housewarming!' Over the plan and the fish, Barinov lets his real feelings show."),
    (6, None, '\'They do not live long with me.\' Explaining that they do not live long with him lays the cards on the table for Denis. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (7, None, "'Someone keeps secrets for the sake of loved ones.' Denis mentions that someone keeps secrets for the sake of loved ones so Barinov sees what is at stake."),
    (8, None, "'For some reason your mom is not firing me.' Claiming that for some reason Denis's is not firing him sounds confident, even if Denis has doubts."),
    (9, None, '\'She promised to. Do you know why?\' Over the room and the fish, Barinov presses Denis for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (10, None, '\'Yes, Dad, I know why.\' Katya explains that dad she knows, keeping her voice calm and direct. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (11, None, "'Because you are a really cool chef.' Realizing that because Barinov is a really cool changes how Katya handles the situation."),
    (12, None, "'Someone is ready to separate close people.' Noting that someone is ready to separate close people keeps Denis's side of the story simple and clear."),
    (13, None, "'And someone cannot entrust a secret even to himself.' Even though someone cannot entrust a secret even to himself, Denis keeps a steady face in front of Barinov."),
]
