# Authoring module for kukhnya-s01e14-scene-01.
ID = 'kukhnya-s01e14-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 1
TITLE = 'Утренние игры  (Morning Games)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = "Welcome to Kukhnya, a comedy about the kitchen of Claude Monet, a smart Moscow restaurant. In this episode, the head chef turns up drunk before an important dinner, and a very nervous Lyova has to take charge. We start earlier, in Vika's flat, where Max wakes up in a playful mood and Vika has a busy day ahead. Here's the scene in Russian; you don't need to catch everything."
OPENER = 'Now the same morning, slowly.'
TRANSITION = 'And the whole morning once more.'
OUTRO = "Max goes off to make the coffee, Vika gets ready for work, and the day that's about to get very loud starts quietly. Keep 'poka ne', 'until', in your pocket. Bye for now."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Вика, ты уже проснулась сегодня?', 'Vika, are you awake already today?', [], ''),
    ('vika', 'Да, я уже давно не сплю.', 'Yes, I have not been sleeping for a long time.', [], ''),
    ('max', 'Почему ты так рано встала?', 'Why did you get up so early?', [], ''),
    ('vika', 'У меня сегодня очень много дел.', 'I have a lot of things today.', [], ''),
    ('max', 'А как же наш вкусный завтрак?', 'And what about our tasty breakfast?', [], ''),
    ('vika', 'Ты можешь приготовить его сам.', 'You can prepare it yourself.', [], ''),
    ('max', 'Сейчас я человек-паук!', 'Now I am Spider-Man!', [(1, 'человек-паук')], 'adapted: cleaned up the crude joke'),
    ('vika', 'Очень смешно, но мне надо идти.', 'Very funny, but I need to go.', [], ''),
    ('max', 'Сейчас я тебя!', 'I am going to get you!', [(2, 'Сейчас я тебя.')], 'adapted: shortened'),
    ('vika', 'Макс, прекрати это немедленно!', 'Max, stop this immediately!', [], ''),
    ('max', 'Хорошо, я иду варить нам кофе.', 'Alright, I am going to brew coffee for us.', [], ''),
    ('vika', 'Пока ты не сходишь в душ.', 'Not until you take a shower.', [(3, 'Пока ты не сходишь в душ.')], ''),
]
WALK = [
    (0, None, "'Vika, are you awake already today?' Russian asks 'have you woken up?', with the past form 'prosnulas'. The 'la' in the middle is there because the 'you' is Vika, a woman; asked of Max, it would be 'prosnulsya'."),
    (1, None, "'Yes, I have not been sleeping for a long time.' Literally, 'already long I don't sleep'. With 'davno', 'for a long time', Russian keeps the plain present 'ne splyu' where English needs 'have been'."),
    (2, None, "'Why did you get up so early?' 'Vstala', got up, is literally 'stood up'. It ends in 'a' because Max is asking Vika."),
    (3, None, "'I have a lot of things today.' 'U menya mnogo del' is the everyday 'I've got lots to do'. After 'mnogo', a lot, the noun goes into its 'of' form, so 'delo', a thing to do, becomes 'del'."),
    (4, None, "'And what about our tasty breakfast?' 'A kak zhe...?' is the handy 'and what about...?' when you feel let down. 'Zavtrak' is masculine, so 'nash vkusny' match it."),
    (5, None, "'You can prepare it yourself.' Breakfast is a 'he' in Russian, so 'it' comes out as 'ego', him. 'Sam', yourself, has no ending because it's Max who'll do the cooking."),
    (6, None, "'Now I am Spider-Man!' 'Chelovek-pauk' is literally 'man-spider', joined with a hyphen. There's no 'am': 'seychas ya chelovek-pauk', 'now I man-spider'."),
    (7, None, "'Very funny, but I need to go.' 'Smeshno' on its own is a full reply, 'that's funny'. 'Mne nado idti' is literally 'to me it's necessary to go', the standard way to say you have to leave."),
    (8, None, "'I am going to get you!' There's no verb at all: 'seychas ya tebya', 'now I you'. The action is obvious, so Russian simply leaves it out, the same playful threat as 'I'll get you!'."),
    (9, None, "'Max, stop this immediately!' 'Prekrati' is the order 'stop it!' to one person you call 'ty'. 'Nemedlenno' is 'ne' plus 'medlenno', 'slowly', so literally 'not slowly'."),
    (10, None, "'Alright, I am going to brew coffee for us.' Russians 'varit' coffee, the cooking-by-boiling verb you'd also use for soup, 'varit sup'. 'Idu varit' is 'I'm off to make', two verbs with no 'to' between them."),
    (11, None, "'Not until you take a shower.' 'Poka ... ne' together mean 'until', so literally 'while you don't go to the shower'. The 'ne' here isn't a real 'not'; it's simply part of the pattern."),
]
