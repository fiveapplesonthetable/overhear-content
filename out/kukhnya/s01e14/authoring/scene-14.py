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
INTRO = 'In the kitchen, a customer has found something odd in his dessert, and he demands to see the chef. Kostya brings the news to a very reluctant Lyova. Listen to the two of them in Russian first.'
OPENER = 'Now slowly, piece by piece.'
TRANSITION = 'And the conversation again, from the top.'
OUTRO = "Lyova has no choice but to go out and face the customer. Keep 'tuda', the going-there word, in your pocket. Talk soon."
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
    (0, None, "'I am not needed by anyone.' Literally 'to nobody not needed': nikomu and ne together, a double negative Russian requires. 'Nuzhen', needed, is the man's form; a woman would say nuzhna."),
    (1, None, "'Lyova, a customer found a SIM card in the dessert.' After 'v' for location, desert becomes deserte. And the card is sim-kartu, with a 'u', because it's the thing found."),
    (2, None, "'A SIM card? In the dessert?' Lyova repeats Kostya's words exactly, still sim-kartu with that 'u', as if the verb 'found' were still there. Echoing like this is the natural Russian way to say 'you what?'."),
    (3, None, "'Yes, he demands the chef.' 'Trebuet' is stronger than 'asks', closer to 'insists on'. 'Shef-povar' becomes shef-povara: for a person who is wanted, Russian uses the same 'a' ending as 'of'."),
    (4, None, "'Go to him, Lyova.' K nemu, to him. After a little word like 'k', 'him' gains an 'n' at the front, so it's nemu, not emu."),
    (5, None, "'I will not go there.' Russian has tam for being there and tuda for going there. With 'I will go', it has to be tuda."),
    (6, None, "'What do you mean, you will not go?' Kostya pounces with 'chto znachit', 'what does it mean', the everyday way to challenge what someone just said. 'Ne poydyosh' is 'you won't go', from 'poyti', 'to set off'."),
    (7, None, "'You are the chef today.' No 'are' appears. Just 'you today chef', and it sounds like a verdict."),
    (8, None, "'Go and figure this out.' 'Razbirat' means 'to take apart, to sort through'. With 'sya' and 's etim', 'with this', it becomes 'deal with it', and razbirays is the order form."),
    (9, None, "'But I am not the chef.' Careful with the first word: no sounds like English 'no', but in Russian it means 'but'. The Russian 'no' is net."),
    (10, None, "'Lyova, you need to figure it out.' Tebe nado, literally 'to you it's necessary'. Swap tebe for mne and you get 'I need to'."),
    (11, None, "'I am afraid to go there.' 'Boyus' is 'I'm afraid', and 'to go' follows in its basic form, idti. It's tuda again, the going-there word from a moment ago."),
    (12, None, "'Come on, go.' 'Davay' comes from the verb 'to give', and it's the all-purpose 'come on'. Russians put it in front of an order to push someone along."),
]
