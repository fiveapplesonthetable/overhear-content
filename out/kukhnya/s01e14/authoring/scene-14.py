# Authoring module for kukhnya-s01e14-scene-14.
ID = 'kukhnya-s01e14-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 14
TITLE = 'Сим-карта в десерте  (SIM Card in Dessert)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'In the kitchen, a customer has found something odd in his dessert, and he demands to see the chef. Kostya brings the news to a very reluctant Lyova. Their conversation comes first, in Russian.'
OPENER = 'One line at a time, once more.'
TRANSITION = 'And the conversation again, from the top.'
OUTRO = 'Lyova has no choice but to go out and face the customer. Kostya runs out of patience quickly. Talk soon.'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('lyova', 'Я никому не нужен.', 'I am not needed by anyone.', [(214, 'никому')], ''),
    ('kostya', 'Лёва, клиент нашёл сим-карту в десерте.', 'Lyova, a customer found a SIM card in the dessert.', [(216, 'клиент в своем десерте нашел сим-карту.')], 'adapted: Lyova for Lyuba, who is not in the scene'),
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
    (0, None, "'I am not needed by anyone.' Russian stacks up negatives, so it's 'to nobody not needed'. Lyova is a man, and so the short word for 'needed' has no ending."),
    (1, None, "'Lyova, a customer found a SIM card in the dessert.' Dessert borrows an 'e' ending after 'in', so it reads 'v deserte'. The SIM card is a loan word too, joined by a hyphen."),
    (2, None, "'A SIM card? In the dessert?' Lyova just echoes the two pieces back as questions. Russian doesn't need a verb to ask 'what?'."),
    (3, None, "'Yes, he demands the chef.' The verb 'trebuet' is stronger than 'asks', closer to 'insists'. After it, the chef goes into the 'of' form, 'shef-povara'."),
    (4, None, "'Go to him, Lyova.' When 'him' comes after a little word like 'to', it gets an extra 'n', so 'on' turns into 'nemu'. That 'n' is a small rule worth knowing."),
    (5, None, "'I will not go there.' Russian has two words for 'there': one for being there and one for going there. This one is the second, the going kind."),
    (6, None, "'What do you mean, you will not go?' It begins with the stock phrase 'what does it mean', and it works for any 'what do you mean'. Kostya is incredulous."),
    (7, None, "'You are the chef today.' No 'are' appears. Just 'you today chef', and it sounds like a verdict."),
    (8, None, "'Go and figure this out.' 'Razbirat'sya' literally means 'take yourself apart over it', which is Russian for 'sort it out'. A little 'i' joins the two orders."),
    (9, None, "'But I am not the chef.' It's a flat 'but I not chef'. The 'but' at the start is the one you use to object."),
    (10, None, "'Lyova, you need to figure it out.' Here the need is the person's: 'to you it is necessary'. It's the same pattern as 'I need' and 'he needs', with only the little word in front changing."),
    (11, None, "'I am afraid to go there.' 'Boyus'' is 'I fear'. The going-to 'there', 'tuda', is the same one he used earlier, and the action stays in its basic form."),
    (12, None, "'Come on, go.' 'Davay' is the all-purpose 'come on', literally 'give'. Russians put it in front of an order to make it friendlier."),
]
