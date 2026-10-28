# Authoring module for kukhnya-s01e14-scene-14.
ID = 'kukhnya-s01e14-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 14
TITLE = "Сим-карта в десерте  (SIM Card in Dessert)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "kostya": "anja", "lyova": "angelina"}
LABELS = {"kostya": "Костя", "lyova": "Лёва"}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = "In the kitchen, Kostya tells Lyova about a problem with a customer's dessert. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around SIM Card in Dessert line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Kostya pushes Lyova to take responsibility for the kitchen. Next time you watch the episode, listen for the Russian expressions for 'necessary' and 'client' — you will catch every word right away. See you next time!"
CLOSING = ("kostya", "Пока!")
STORY = [
    ('lyova', 'Я никому не нужен.', 'I am not needed by anyone.', [(214, 'никому')], ''),
    ('kostya', 'Люба, клиент нашел сим-карту в десерте.', 'Lyuba, a customer found a SIM card in the dessert.', [(216, 'люба')], ''),
    ('lyova', 'Сим-карту? В десерте?', 'A SIM card? In the dessert?', [(216, 'сим')], ''),
    ('kostya', 'Да, он требует шеф-повара.', 'Yes, he demands the chef.', [(218, 'требует')], ''),
    ('kostya', 'Иди к нему, Лёва.', 'Go to him, Lyova.', [(218, 'иди')], ''),
    ('lyova', 'Я не пойду туда.', 'I will not go there.', [(219, 'пойду')], ''),
    ('kostya', 'Что значит, ты не пойдешь?', 'What do you mean, you will not go?', [(217, 'что')], ''),
    ('kostya', 'Ты сегодня шеф-повар.', 'You are the chef today.', [(220, 'сегодня')], ''),
    ('kostya', 'Иди и разбирайся с этим.', 'Go and figure this out.', [(218, 'иди')], ''),
    ('lyova', 'Но я не шеф-повар.', 'But I am not the chef.', [(218, 'шеф')], ''),
    ('kostya', 'Лёва, тебе надо разобраться.', 'Lyova, you need to figure it out.', [(230, 'лева')], ''),
    ('lyova', 'Я боюсь туда идти.', 'I am afraid to go there.', [], ''),
    ('kostya', 'Давай, иди.', 'Come on, go.', [(223, 'давай')], ''),
]
WALK = [
    (0, None, "'I am not needed by anyone.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'I' straight to 'is needed'."),
    (1, None, "'Lyuba, a customer found a SIM card in the dessert.' Here Kostya anchors the line on the word meaning 'client' and builds the thought around 'found' and 'SIM card'."),
    (2, None, "'A SIM card? In the dessert?' There is no question word here — in Russian, rising intonation on 'dessert' is enough to make it a question. And Kostya jumps in."),
    (3, None, "'Yes, he demands the chef.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (4, None, "'Go to him, Lyova.' Kostya uses a direct command command form of the verb meaning 'go'."),
    (5, None, "'I will not go there.' Lyova uses the action verb meaning 'go' to focus on the single completed result, pairing it with 'there'."),
    (6, None, "'What do you mean, you will not go?' The question word for 'what' comes right at the start, followed directly by 'will go'."),
    (7, None, "'You are the chef today.' Russian omits the present-tense verb 'to be' here, linking 'today' directly with 'head chef', combining 'today' with 'head chef'."),
    (8, None, "'Go and figure this out.' Kostya leads with the direct command form meaning 'go', followed by 'to understand well'."),
    (9, None, "'But I am not the chef.' Russian omits the present-tense verb 'to be', connecting 'but' directly with 'head chef'."),
    (10, None, "'Lyova, you need to figure it out.' Notice the self-directed ending on the verb for 'to deal with', which directs the action back onto the subject. Then Lyova responds."),
    (11, None, "'I am afraid to go there.' the self-directed ending on the verb for 'am afraid' turns the action back onto the subject. And Kostya jumps in."),
    (12, None, "'Come on, go.' Kostya leads with the direct command form meaning 'let's', followed by 'go'."),
]
