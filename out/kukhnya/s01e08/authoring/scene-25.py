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
OUTRO = "Vika's best moment is \"poroda sushi\", breed sushi, before she corrects it to Shih Tzu. That kind of slip happens to everyone in a new language. See you next time."
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
    (0, None, "'Vika, look at me. What is this?' To look at someone is \"posmotri na menya\", with \"na\", at, before the person. Then \"eto chto takoe\" is a blunt 'what is this?', the question you ask when you already suspect the answer."),
    (1, None, "'Chef, this is my new little dog!' Vika's \"sobachka\" is \"sobaka\", dog, with the -chka ending that makes it small and sweet. Russians use these endings constantly with animals."),
    (2, None, "'I bought her this morning.' The word \"utrom\", in the morning, is \"utro\" with -om, and it needs no 'in'. Vika says \"kupila\", with the -a of a woman speaking."),
    (3, None, "'Why do you need a dog of the same breed?' Barinov's \"zachem tebe\" is literally 'what for to you', the short way to ask why someone needs something. Then \"takoy zhe\" means 'the same', and \"porody\" is \"poroda\", breed, in its 'of' form."),
    (4, None, "'I just really liked your Dyson.' The dog's real name is Tyson, and Vika's \"Dayson\" is the slip. Liking runs backwards in Russian: \"mne ponravilsya\", literally 'to me he was pleasing'."),
    (5, None, "'I could not resist and bought a puppy.' Saying \"ne uderzhalas\" means 'couldn't hold myself back', from \"derzhat\", to hold. Her \"pyosik\" is \"pyos\", dog, with the small, affectionate -ik."),
    (6, None, "'But they are completely identical!' You can hear \"odin\", one, at the root of \"odinakovye\", identical. The \"zhe\" after \"no\", but, adds the feeling of 'but surely'."),
    (7, None, "'Sorry, I still mix them up.' Literally 'up to these times', \"do sikh por\" means 'still' or 'to this day'. And \"putayu\", I mix up, goes back to \"putat\", to confuse."),
    (8, None, "'It seems this one is yours, and this one is mine.' Starting with \"kazhetsya\", it seems, is how Russians soften a guess. Then \"vot eto vasha, a vot eta moya\" points at each dog in turn, with the polite \"vasha\" for her boss."),
    (9, None, "'Vika, what is your dog's name?' Russian asks \"kak zovut\", literally 'how do they call', so the dog is the one being called: \"tvoego psa\". And \"pyos\" drops its o to become \"psa\"."),
    (10, None, "'Mine? His name is Maxik!' The answer \"ego zovut\", his name is, follows the same 'they call him' pattern. The name \"Maksik\" is Max with a cuddly -ik, so she has named the dog after her colleague."),
    (11, None, "'And what breed is this dog?' Russian says the breed is \"u etoy sobaki\", 'at this dog', which is how you say something has a thing. After \"u\" the dog takes its 'of' endings."),
    (12, None, "'Breed sushi... Oh, Shih Tzu!' The little \"oy\" is the Russian 'oops'. And \"shitsu\" and sushi sound close enough that the mix-up is easy."),
    (13, None, "'Just like your dog. I will go!' Literally 'as also', \"kak i\" means 'just like'. Saying \"ya poydu\", I'll go, is a common way to excuse yourself and leave."),
]
