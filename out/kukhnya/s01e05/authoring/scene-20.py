# Authoring module for kukhnya-s01e05-scene-20.
ID = 'kukhnya-s01e05-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 20
TITLE = 'Просьба о помощи  (A Request for Help)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "In the Claude Monet kitchen, the dinner rush has buried Max at the fish station. He has to ask Fedya, the fish cook he's been feuding with, for help, and Fedya isn't going to make it easy. Listen in Russian first."
OPENER = "Slowly now. Fedya pretends he can't hear, and that's how he gets Max to apologise again and again."
TRANSITION = "Here's the whole apology, start to finish."
OUTRO = "Between them they've given you the words for 'help me', 'sorry', and 'calm down'. That's a decent kit for making up with a colleague."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Федя, пожалуйста, помоги мне с заказами.', 'Fedya, please help me with the orders.', [(292, 'Слушай, Федь, извини'), (294, 'Помоги с заказами')], ""),
    ('fedya', 'Что ты говоришь? Я плохо слышу.', "What are you saying? I can't hear well.", [(295, 'Что? Извини, говорю')], ""),
    ('max', 'Я говорю, что прошу прощения.', 'I am saying that I ask for forgiveness.', [(293, 'Я зря себя так вывел')], ""),
    ('fedya', 'Коллеги, можно потише на кухне, пожалуйста?', 'Colleagues, could you be quieter in the kitchen, please?', [(296, 'Коллеги! Можно потише чуть-чуть, пожалуйста')], ""),
    ('fedya', 'Макс хочет сказать нам что-то важное.', 'Max wants to tell us something important.', [(297, 'человек что-то важное сказать хочет')], ""),
    ('max', 'Федя, извини меня за всё.', 'Fedya, forgive me for everything.', [(298, 'Федя, извини')], ""),
    ('max', 'Ты отличный опытный повар, а я нет.', "You're an excellent, experienced cook, and I'm not.", [(299, 'Ты прекрасный повар, а я нет')], ""),
    ('max', 'Помоги мне быстро приготовить эти блюда.', 'Help me quickly prepare these dishes.', [(300, 'Помоги мне, пожалуйста, с заказами')], ""),
    ('fedya', 'Я всё очень хорошо услышал.', 'I heard everything very well.', [(301, 'Понятно')], ""),
    ('fedya', 'Но я тебе совсем не верю.', 'But I do not believe you at all.', [(302, 'Но не верю')], ""),
    ('fedya', 'В твоих словах нет настоящей искренности.', 'In your words there is no real sincerity.', [(303, 'Ну, искренности не хватает')], ""),
    ('fedya', 'Давай повтори всё ещё разок громче!', 'Come on, repeat everything once more louder!', [(304, 'Давай еще разок')], ""),
    ('max', 'Я больше не буду ничего повторять!', 'I will not repeat anything anymore!', [(305, 'Да пошел ты')], ""),
    ('fedya', 'Ладно, успокойся, я сейчас помогу.', 'Alright, calm down, I will help now.', [], ""),
]
WALK = [
    (0, None, ["'Fedya, please help me with the orders.' , 'please', also translates to 'you're ", ('max', 'пожалуйста,'), " welcome'. After ", ('max', 'с'), ", 'with', the plural takes the instrumental ending: ", ('max', 'с'), ('max', 'заказами.')]),
    (1, None, ["'What are you saying? I can't hear well.' is from the verb 'to hear', ", ('fedya', 'слышу.'), " which is different from 'to listen'. ", ('fedya', 'плохо'), ", 'badly', is the opposite of 'good'."]),
    (2, None, ["'I am saying that I ask for forgiveness.' , literally 'I ask for forgiveness', ", ('max', 'прошу'), ('max', 'прощения.'), " is a more formal apology than 'sorry'. The word for 'forgiveness' changes form after ", ('max', 'прошу'), '.']),
    (3, None, ["'Colleagues, could you be quieter in the kitchen, please?' , 'may one', is the all-purpose ", ('fedya', 'можно'), " way to ask permission. ", ('fedya', 'потише'), ", with its prefix, means 'a bit quieter'."]),
    (4, None, ["'Max wants to tell us something important.' is 'something important', ", ('fedya', 'что-то'), ('fedya', 'важное.'), " and ", ('fedya', 'важное.'), ' takes a matching ending. Fedya says it loudly so the whole kitchen will listen.']),
    (5, None, ["'Fedya, forgive me for everything.' is the informal command, for a ", ('max', 'извини'), ' l command, for a friend or an equal; to a boss it would be formal. ', ('max', 'за'), ('max', 'всё.'), ", 'for everything', uses ", ('max', 'за'), " the word you apologise 'for' with."]),
    (6, None, ["'You're an excellent, experienced cook, and I'm not.' is built from the word for ", ('max', 'опытный'), " 'experience'. ", ('max', 'а'), ('max', 'я'), ('max', 'нет.'), ", 'and I not', gets by without any 'am'."]),
    (7, None, ["'Help me quickly prepare these dishes.' is literally 'help to me', and ", ('max', 'Помоги'), ('max', 'мне'), " Russian always helps 'to' someone. ", ('max', 'приготовить'), ", 'to prepare', comes straight after with no 'to' word."]),
    (8, None, ["'I heard everything very well.' means 'I heard' as in 'I ", ('fedya', 'услышал.'), " heard' as in 'I caught it', the one-off partner of 'to hear'. It answers his own 'hear badly' from a moment ago."]),
    (9, None, ["'But I do not believe you at all.' The verb for 'believe' takes the dative, so it's 'I believe to you': ", ('fedya', 'тебе'), ('fedya', 'совсем'), ('fedya', 'не'), ('fedya', 'верю.'), ('fedya', 'совсем'), ('fedya', 'не'), " translates to 'not at all'."]),
    (10, None, ["'In your words there is no real sincerity.' , 'there is no', puts what's ", ('fedya', 'нет'), " missing into the genitive case, so it's ", ('fedya', 'искренности.'), ('fedya', 'В'), ('fedya', 'твоих'), ('fedya', 'словах'), ", 'in your words', takes the ending for a place."]),
    (11, None, ["'Come on, repeat everything once more louder!' is a cosy form of the ", ('fedya', 'разок'), " word for 'one time'. ", ('fedya', 'громче!'), ", 'louder', is the comparative of 'loud'."]),
    (12, None, ["'I will not repeat anything anymore!' literally translates to 'not ", ('max', 'больше'), ('max', 'не'), " anymore'. ", ('max', 'не'), ('max', 'буду'), ('max', 'повторять!'), " is 'I won't be repeating', with ", ('max', 'буду'), ", 'I will be', in front."]),
    (13, None, ["'Alright, calm down, I will help now.' , 'okay then', settles ", ('fedya', 'Ладно,'), " things. ", ('fedya', 'успокойся,'), ", 'calm down', ends with the reflexive suffix, so it's literally 'calm yourself'."]),
]
