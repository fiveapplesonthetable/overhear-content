# Authoring module for domashniy-arest-s01e01-scene-27.
ID = 'domashniy-arest-s01e01-scene-27'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 27
TITLE = 'Новый мэр  (The New Mayor)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "We stay in the shared kitchen, with the same bad vodka. Last time, Pasha announced on television that he is running for mayor, and Samson told Arkady that all officials are thieves and nobody cares. Suddenly Arkady looks at Samson in a new way. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's take it slowly. Arkady has just had an idea, and he is cross with himself for not having it sooner."
TRANSITION = 'Here is the whole scene one more time.'
OUTRO = 'To close the first episode, Nina complains on the phone that all the boys chased her at school and somehow she drew this lucky ticket, and a song asks how much money it takes to be happy. See you next time!'
CLOSING = ('samson', 'До встречи!')
STORY = [
    ('arkady', 'Как я сразу не догадался!', "Why didn't I think of it right away!", [(1026, 'я сразу не догадался')], "'Блин, как же' dropped"),
    ('arkady', 'Самсон, ты русский?', 'Samson, are you Russian?', [(1028, 'Самсон, ты русский')], ''),
    ('samson', 'Нет, эфиоп!', 'No, Ethiopian!', [(1029, 'Эфиоп')], "'Нет,' added to make the joke clear"),
    ('arkady', 'Не сидел?', 'Never been in prison?', [(1030, 'Не сидел')], ''),
    ('samson', 'Нет, слава богу.', 'No, thank God.', [], "new; plain form of cue 1032 'Бог миловал' (God spared me)"),
    ('arkady', 'Православный?', 'Orthodox?', [(1033, 'Православный')], ''),
    ('samson', 'Ну а какой?', 'Well, what else?', [(1034, 'Ну, а какой')], ''),
    ('arkady', 'Русский. Православный. Не сидел.', 'Russian. Orthodox. Never been in prison.', [(1035, 'Русский. Православный. Не сидел')], ''),
    ('samson', 'Ну да. Жена, двое детей.', 'Well, yes. A wife, two kids.', [(1036, 'Жена, двое детей')], "'Ну да.' added; in the show Arkady says the whole list, here Samson adds this part"),
    ('arkady', 'Работал на стройке. Служил?', 'Worked on a building site. Did you serve in the army?', [(1036, 'Работал на стройке'), (1037, 'Служил')], ''),
    ('samson', 'Служил, конечно.', 'Of course I served.', [], 'new: Samson is ex-army (characters.md)'),
    ('arkady', 'Вот оно! Самсон, ты будешь новым мэром.', "That's it! Samson, you're going to be the new mayor.", [(1038, 'Вот оно'), (1039, 'Самсон, ты будешь новым мэром')], ''),
    ('samson', 'Согласен.', 'Agreed.', [(1040, 'Согласен')], ''),
    ('arkady', 'Ты не понял меня. Я тебя сделаю новым мэром.', "You don't understand me. I'm going to make you the new mayor.", [(1041, 'Ты не понял меня'), (1042, 'Я тебя сделаю новым мэром')], ''),
    ('samson', 'Меня? Мэром?', 'Me? Mayor?', [], 'new: Samson finally takes it seriously'),
    ('arkady', 'Через два месяца выборы. Ты же хотел новый уровень.', "The election is in two months. You wanted a new level, didn't you?", [(1043, 'Через два месяца'), (1044, 'Ты же хотел новый уровень')], "'выбора' (transcription error) -> 'выборы'"),
    ('samson', 'Ну, хотел.', 'Well, I did.', [], 'new'),
    ('arkady', 'Я помогу тебе, а ты поможешь мне.', "I'll help you, and you'll help me.", [(1047, 'я помогу тебе'), (1048, 'а ты поможешь мне')], ''),
]
WALK = [
    (0, None, "'Why didn't I think of it right away!' Literally, 'how did I not guess at once'. The verb is past and masculine: no extra ending, because Arkady is a man. Then he starts asking strange questions."),
    (1, None, "'Samson, are you Russian?' A question in Russian is often just a statement with a rising voice. Samson answers with a joke."),
    (2, None, "'No, Ethiopian!' A big, blond, very Russian man, being sarcastic. Arkady ignores it and goes on down his list."),
    (3, None, "'Never been in prison?' Literally, 'didn't sit?' In everyday Russian, 'to sit' can mean 'to do time'. Samson is glad to say no."),
    (4, None, "'No, thank God.' Literally, 'glory to God'. Next question."),
    (5, None, "'Orthodox?' He means the Orthodox church, the main church in Russia. Samson finds the question silly."),
    (6, None, "'Well, what else?' Literally, 'and which one?', as if there could be no other answer. Arkady sums it up."),
    (7, None, "'Russian. Orthodox. Never been in prison.' Three ticks on an invisible form. Samson adds his family."),
    (8, None, "'Well, yes. A wife, two kids.' After the word for 'two', the word for 'children' takes a special form, one you hear a lot. Arkady continues."),
    (9, None, "'Worked on a building site. Did you serve in the army?' Again past verbs with no subject: the ending tells you it's a man. Samson is proud of this one."),
    (10, None, "'Of course I served.' He repeats the verb as his answer, which is a very Russian way to say yes. And Arkady has his candidate."),
    (11, None, "'That's it! Samson, you're going to be the new mayor.' After the verb 'to be', the job takes a special ending for roles: you'll be 'as mayor'. Samson thinks it's just drunken talk."),
    (12, None, "'Agreed.' Said like a man accepting another glass. Arkady insists."),
    (13, None, "'You don't understand me. I'm going to make you the new mayor.' Same special ending on the job: 'make you as the new mayor'. Now Samson listens."),
    (14, None, "'Me? Mayor?' Two short questions, and he can hardly believe it. Arkady explains the plan."),
    (15, None, "'The election is in two months. You wanted a new level, didn't you?' The little word in the middle of the second sentence works like 'after all', reminding Samson of his own words. Samson admits it."),
    (16, None, "'Well, I did.' Just the verb again, in the past. And Arkady offers the deal."),
    (17, None, "'I'll help you, and you'll help me.' Both verbs are about the future. Two forms of the same verb, one for 'I', one for 'you', a neat pair to remember."),
]
