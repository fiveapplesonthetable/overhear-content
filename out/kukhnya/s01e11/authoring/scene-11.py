# Authoring module for kukhnya-s01e11-scene-11.
ID = 'kukhnya-s01e11-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 11
TITLE = "Гость Насти  (Nastya's Guest)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'sasha': 'Саша', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "Vika has a puzzle: a man at table five has come in as Nastya's guest, but he is not eating. She asks Sasha, the waitress, to explain. Over to the Russian."
OPENER = 'Right, back to the start, one line at a time.'
TRANSITION = 'And now the full version again.'
OUTRO = 'The man is writing in a notebook, and Vika has sent for Nastya. Another possible critic has arrived. Rest well, and see you soon.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Саша, подойди сюда на секунду.', 'Sasha, come over here for a second.', [], ''),
    ('sasha', 'Что случилось, Виктория Сергеевна?', 'What happened, Viktoria Sergeyevna?', [], ''),
    ('vika', 'Кто сидит за пятым столиком?', 'Who is sitting at the fifth table?', [], ''),
    ('sasha', 'Там сидит довольно странный мужчина.', 'A rather strange man is sitting there.', [], ''),
    ('vika', 'Почему он ничего не заказывает?', 'Why is he not ordering anything?', [], ''),
    ('sasha', 'Я не знаю, это гость Насти.', "I do not know, this is Nastya's guest.", [(159, 'Я не знаю')], ''),
    ('vika', 'Она уже подошла к нему?', 'Did she already approach him?', [], ''),
    ('sasha', 'Да, она только что дала меню.', 'Yes, she just gave him the menu.', [], ''),
    ('vika', 'Он внимательно изучает наш зал?', 'Is he carefully studying our hall?', [], ''),
    ('sasha', 'Он постоянно пишет в свой блокнот.', 'He is constantly writing in his notebook.', [], ''),
    ('vika', 'Это очень похоже на проверку.', 'This looks very much like an inspection.', [], ''),
    ('sasha', 'Мне позвать Настю к вам?', 'Should I call Nastya to you?', [], ''),
    ('vika', 'Да, позови её прямо сейчас.', 'Yes, call her right now.', [], ''),
]
WALK = [
    (0, None, ["'Sasha, come over here for a second.' We will analyze this line: ", ('vika', 'подойди'), ' means come up, based on the verb to go on foot. And ', ('vika', 'сюда'), ' is to here. Vika uses the informal you with the waitress and keeps it short.']),
    (1, None, ["'What happened, Viktoria Sergeyevna?' Sasha uses the first name and patronymic because she is talking to her boss. We hear ", ('sasha', 'Что'), ('sasha', 'случилось'), ' asks what happened.']),
    (2, None, ["'Who is sitting at the fifth table?' Russians sit behind a table, which gives us ", ('vika', 'за'), ('vika', 'пятым'), ('vika', 'столиком'), '. The number is ', ('vika', 'пятым'), ', matching a familiar pattern.']),
    (3, None, ["'A rather strange man is sitting there.' A trap word: ", ('sasha', 'мужчина'), ' ends like a feminine noun, yet ', ('sasha', 'странный'), ' before it is masculine. Here we have ', ('sasha', 'Там'), ('sasha', 'сидит'), ' puts the verb first, bringing someone new into view.']),
    (4, None, ["'Why is he not ordering anything?' We can examine the sentence: ", ('vika', 'ничего'), ('vika', 'не'), ('vika', 'заказывает'), ' keeps both negatives. The verb to order comes from the noun order.']),
    (5, None, ["'I do not know, this is Nastya's guest.' In ", ('sasha', 'гость'), ('sasha', 'Насти'), ', the ending on the name shows possession. Sasha hands the problem to her colleague.']),
    (6, None, ["'Did she already approach him?' The verb ", ('vika', 'подошла'), ' has a feminine ending. In ', ('vika', 'к'), ('vika', 'нему'), ', the pronoun picks up an extra letter after the preposition.']),
    (7, None, ["'Yes, she just gave him the menu.' Let us look at the speech: ", ('sasha', 'только'), ('sasha', 'что'), ' means just now. ', ('sasha', 'дала'), ' takes a feminine ending, while ', ('sasha', 'меню'), ' never changes its form.']),
    (8, None, ["'Is he carefully studying our hall?' The verb ", ('vika', 'изучает'), ' is the school word. ', ('vika', 'внимательно'), ' means carefully or attentively. Vika thinks the man is watching the room.']),
    (9, None, ["'He is constantly writing in his notebook.' We will inspect the dialogue: ", ('sasha', 'в'), ('sasha', 'свой'), ('sasha', 'блокнот'), ' points into his own notebook. ', ('sasha', 'постоянно'), ' means constantly, from the same family as regular guests.']),
    (10, None, ["'This looks very much like an inspection.' Let us look at the words: ", ('vika', 'похоже'), ('vika', 'на'), ' means similar to, matching a familiar pattern. The term ', ('vika', 'проверку'), ' grows from the verb to check.']),
    (11, None, ["'Should I call Nastya to you?' Russian asks ", ('sasha', 'Мне'), ('sasha', 'позвать'), ', using the infinitive. ', ('sasha', 'к'), ('sasha', 'вам'), ' is polite, and ', ('sasha', 'Настю'), ' changes its ending as she is the one called.']),
    (12, None, ["'Yes, call her right now.' The command ", ('vika', 'позови'), ' is for summoning someone. The expression ', ('vika', 'прямо'), ('vika', 'сейчас'), ' means right now. Vika ends the scene with an order.']),
]
