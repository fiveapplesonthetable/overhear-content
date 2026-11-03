# Authoring module for kukhnya-s01e08-scene-25.
ID = 'kukhnya-s01e08-scene-25'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 25
TITLE = 'Две собаки  (Two Dogs)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Chef Barinov has his Shih Tzu, Tyson, back. Then Vika, the art director, turns up with a second Shih Tzu that looks exactly like him, and Barinov wants an explanation. Here it is in Russian first."
OPENER = "Let's go through the interrogation. Every answer Vika gives makes things worse."
TRANSITION = "Now the whole exchange once more."
OUTRO = "Vika's best slip is calling the dog's breed 'sushi' before quickly correcting herself to Shih Tzu — the sort of mix-up anyone can make under pressure. See you next time."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('barinov', 'Вика, посмотри на меня. Это что такое?', 'Vika, look at me. What is this?', [(296, 'Вика, это чё?')], ''),
    ('vika', 'Шеф, это моя новая собачка!', 'Chef, this is my new little dog!', [(297, 'Это моя собачка!')], ''),
    ('vika', 'Я её сегодня утром купила.', 'I bought her this morning.', [(298, 'Я её сегодня купила!')], ''),
    ('barinov', 'Зачем тебе собака такой же породы?', 'Why do you need a dog of the same breed?', [], ''),
    ('vika', 'Мне просто очень понравился ваш Дайсон.', 'I just really liked your Dyson.', [(299, 'Мне просто так понравился Ваш Дайсон!')], ''),
    ('vika', 'Я не удержалась и купила пёсика.', 'I could not resist and bought a puppy.', [(300, 'купил себе такого же пёсика!')], ''),
    ('barinov', 'Но они же совершенно одинаковые!', 'But they are completely identical!', [], ''),
    ('vika', 'Извините, я их до сих пор путаю.', 'Sorry, I still mix them up.', [(302, 'Я их до сих пор путаю!')], ''),
    ('vika', 'Кажется, вот это ваша, а вот эта моя.', 'It seems this one is yours, and this one is mine.', [(301, 'вот это ваша, а вот это моя!')], ''),
    ('barinov', 'Вика, а как зовут твоего пса?', "Vika, what is your dog's name?", [(304, 'А твоего зовут как?')], ''),
    ('vika', 'Моего? Его зовут Максик!', 'Mine? His name is Maxik!', [(306, 'Максик?')], ''),
    ('barinov', 'А какая порода у этой собаки?', 'And what breed is this dog?', [(307, 'А порода?')], ''),
    ('vika', 'Порода суши... Ой, шицу!', 'Breed sushi... Oh, Shih Tzu!', [(308, 'Суши. Ой, шицу.')], ''),
    ('vika', 'Как и ваша собака. Я пойду!', 'Just like your dog. I will go!', [(309, 'Как и ваша.'), (310, 'Ну, я пойду.')], ''),
]
WALK = [
    (0, None, ["'Vika, look at me. What is this?' To demand attention from someone, say ", ('barinov', 'посмотри'), ' to ask them to look at you.']),
    (1, None, ["'Chef, this is my new little dog!' Notice how she refers to her pet as a ", ('vika', 'собачка'), ', making the word for dog sound small and cute.']),
    (2, None, ["'I bought her this morning.' The phrase for this morning includes the word ", ('vika', 'утром'), ' to indicate the time of day.']),
    (3, None, ["'Why do you need a dog of the same breed?' You can question a person's reasons with ", ('barinov', 'Зачем'), ' when asking why they need something.']),
    (4, None, ["'I just really liked your Dyson.' Telling someone that a thing was pleasing requires ", ('vika', 'понравился'), ' to express that you liked it.']),
    (5, None, ["'I could not resist and bought a puppy.' When you simply cannot hold yourself back, say ", ('vika', 'удержалась'), ' to describe being unable to resist.']),
    (6, None, ["'But they are completely identical!' He points out their identical appearance using ", ('barinov', 'одинаковые'), ' to say they look completely the same.']),
    (7, None, ["'Sorry, I still mix them up.' If you want to admit confusing things, try ", ('vika', 'путаю'), ' for mixing up one thing with another.']),
    (8, None, ["'It seems this one is yours, and this one is mine.' Softening a guess often begins with ", ('vika', 'Кажется'), ', meaning it seems or appears so.']),
    (9, None, ["'Vika, what is your dog's name?' We inquire about a pet's name via ", ('barinov', 'зовут'), ', literally meaning how they call them.']),
    (10, None, ["'Mine? His name is Maxik!' She gives the name by starting with ", ('vika', 'Его'), ' to mean his or him.']),
    (11, None, ["'And what breed is this dog?' Barinov asks about the exact breed using ", ('barinov', 'порода'), ' to question what kind of dog it is.']),
    (12, None, ["'Breed sushi... Oh, Shih Tzu!' A small slip of the tongue brings a quick ", ('vika', 'Ой'), ', which is a common oops sound.']),
    (13, None, ["'Just like your dog. I will go!' Announcing that you are leaving is done with ", ('vika', 'пойду'), ' to state that you will go.']),
]
