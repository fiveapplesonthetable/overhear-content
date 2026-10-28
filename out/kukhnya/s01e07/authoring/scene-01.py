# Authoring module for kukhnya-s01e07-scene-01.
ID = 'kukhnya-s01e07-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 1
TITLE = 'Жизнь в столице  (Life in the Capital)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = "This is Kukhnya, which means The Kitchen, a Russian comedy set in Claude Monet, a smart Moscow restaurant where Chef Barinov shouts and the cooks try to keep their jobs. Episode seven opens with Max, a young cook from Voronezh who has been in Moscow for two weeks, chatting with Kostya, the bartender. Max is keeping quiet about where he actually sleeps. You'll hear it in Russian first, and it's fine to miss words."
OPENER = "Now slowly. It's a friendly chat, and the sentences are short enough to follow."
TRANSITION = "Let's hear the whole chat again, without stopping."
OUTRO = "Max says he doesn't pay a single kopeck, and Kostya doesn't believe him, which is how a secret gets started. You can already say how long you've lived somewhere and where you're from. See you next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Я живу в Москве уже две недели.', 'I have been living in Moscow for two weeks already.', [(1, 'Две недели, как я уехал из Воронежа')], ''),
    ('kostya', 'Ты уже привык к жизни в Москве?', 'Have you already gotten used to life in Moscow?', [], ''),
    ('max', 'Я приехал сюда из Воронежа за мечтой.', 'I came here from Voronezh for a dream.', [(1, 'я уехал из Воронежа')], ''),
    ('kostya', 'И теперь ты работаешь в лучшем ресторане.', 'And now you work in the best restaurant.', [(2, 'Я работаю в самом офигенном ресторане Москвы')], ''),
    ('max', 'Ресторан Клод Моне — самый известный в городе.', 'Claude Monet restaurant is the most famous in the city.', [(3, 'Клод Мане')], ''),
    ('kostya', 'Здесь очень строгие правила и дорогое меню.', 'Here there are very strict rules and an expensive menu.', [], ''),
    ('max', 'Но для меня это прекрасный опыт.', 'But for me this is wonderful experience.', [], ''),
    ('kostya', 'А где ты нашёл себе жильё?', 'And where did you find yourself housing?', [], ''),
    ('max', 'Я живу в самом центре города.', 'I live right in the center of the city.', [(3, 'я живу в самом центре Москвы')], ''),
    ('kostya', 'Квартиры в центре стоят огромных денег.', 'Apartments in the center cost huge money.', [], ''),
    ('max', 'А я не плачу ни одной копейки!', 'And I do not pay a single kopeck!', [(3, 'ни копейки за это не'), (4, 'плачу')], ''),
    ('kostya', 'Это звучит очень странно и подозрительно.', 'That sounds very strange and suspicious.', [], ''),
    ('max', 'У меня есть один секретный план.', 'I have one secret plan.', [], ''),
]
WALK = [
    (0, None, "'I have been living in Moscow for two weeks already.' Russian has no 'have been living': it just says 'I live in Moscow already two weeks', zhivu, plain present. Notice dve, the form of 'two' used with feminine words like nedelya, a week."),
    (1, None, '\'Have you already gotten used to life in Moscow?\' "Privyk", \'got used\', has no l at the end, which is unusual for a man\'s past. It takes k, \'towards\', so you get used \'to\' life: k zhizni.'),
    (2, None, '\'I came here from Voronezh for a dream.\' "Priekhal" means he came by transport, train or bus, not on foot. And za mechtoy, \'after a dream\', is the same pattern as going to the shop za khlebom, for bread.'),
    (3, None, "'And now you work in the best restaurant.' After v, 'in', the restaurant becomes restorane and 'best' becomes luchshem. Both endings mark the place where something happens."),
    (4, None, "'Claude Monet restaurant is the most famous in the city.' Put samyy, 'most', in front of a describing word and you have a superlative: samyy izvestnyy, the most famous. The dash in writing stands in for 'is', which Russian leaves out."),
    (5, None, '\'Here there are very strict rules and an expensive menu.\' "Menyu" is borrowed from French and never changes its ending. It counts as neuter, so \'expensive\' takes the neuter -oe: dorogoe menyu.'),
    (6, None, '\'But for me this is a wonderful experience.\' "Dlya menya", \'for me\', is worth keeping whole. "Opyt" is the everyday word for experience, as in work experience on a CV.'),
    (7, None, '\'And where did you find yourself housing?\' "Sebe", \'for yourself\', is often slipped in like this when you get something for your own use. "Zhilyo", housing, is related to zhit\', to live.'),
    (8, None, '\'I live right in the center of the city.\' "Samyy" shows up again, this time as samom, and here it means \'the very\'. V samom tsentre is literally \'in the very center\'.'),
    (9, None, "'Apartments in the center cost huge money.' Here stoyat means 'they cost', not 'they stand'. Money, dengi, only exists in the plural, and here it is in the 'of' form, deneg."),
    (10, None, '\'And I do not pay a single kopeck!\' "Ni odnoy kopeyki" is \'not even one kopeck\', and Russian keeps the ne of \'I don\'t pay\' as well. Two negatives in one sentence are normal here.'),
    (11, None, '\'That sounds very strange and suspicious.\' "Zvuchit", \'sounds\', is built on zvuk, a sound. Kostya isn\'t buying it.'),
    (12, None, '\'I have one secret plan.\' U menya est\', \'at me there is\', is the basic Russian \'I have\'. "Sekretnyy" is the English \'secret\' with a Russian adjective ending.'),
]
