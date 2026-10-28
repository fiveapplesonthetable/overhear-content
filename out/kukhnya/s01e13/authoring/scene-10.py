# Authoring module for kukhnya-s01e13-scene-10.
ID = 'kukhnya-s01e13-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 10
TITLE = 'Звонок из Милана  (A Call from Milan)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'angelina_h': 'Ангелина', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Max realises he's caused a mess, and he has an idea to fix it: a fake phone call. He rings the restaurant pretending to be an Italian and tells the hostess the trade show is cancelled. Russian first, as always."
OPENER = 'Again, and watch the little acting job.'
TRANSITION = 'Here it is, top to bottom.'
OUTRO = "Max's trick works, and Vika is on her way back. Can you hear him trying not to laugh? Catch you next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Бонжорно, синьоры.', 'Buongiorno, signori.', [], ''),
    ('angelina_h', 'Добрый день, ресторан Клод Моне.', 'Good afternoon, Claude Monet restaurant.', [], ''),
    ('max', 'Меня зовут Александр.', 'My name is Alexander.', [(130, 'Меня зовут Александр')], ''),
    ('max', 'Выставка отменяется.', 'The exhibition is cancelled.', [(132, 'выставка отменится')], ''),
    ('max', 'Передайте это Виктории.', 'Pass this on to Victoria.', [(133, 'Передайте')], ''),
    ('angelina_h', 'Хорошо, я передам.', 'All right, I will pass it on.', [], ''),
    ('max', 'Граци, синьора, чао-чао.', 'Grazie, signora, ciao-ciao.', [(134, 'Граци, сеньора'), (135, 'Чао-чао.')], ''),
    ('angelina_h', 'Да, алло. Виктория Сергеевна, здравствуйте.', 'Yes, hello. Victoria Sergeyevna, hello.', [(138, 'Да, алло. Виктория Сергеевна, здравствуйте')], ''),
    ('angelina_h', 'Звонил представитель выставки из Милана.', 'A representative of the exhibition from Milan called.', [(139, 'Звонил представитель выставки из Милана')], ''),
    ('angelina_h', 'Он сказал, что она отменяется.', 'He said that it is cancelled.', [(139, 'сказал, что она отменяется.')], ''),
    ('vika', 'А, правда? Я уже в Домодедово.', 'Oh, really? I am already in Domodedovo.', [(140, 'А, правда? А я уже в Домодедово')], ''),
    ('vika', 'Я чуть не улетела.', 'I almost flew away.', [(140, 'чуть не улетела.')], ''),
    ('vika', 'Спасибо, что предупредили.', 'Thank you for warning me.', [(141, 'Спасибо, что предупредили.')], ''),
]
WALK = [
    (0, None, "'Buongiorno, signori.' These are Italian words written in Russian letters, so Max's fake accent does the talking. It sounds like 'bonzhorno', not quite right, which is the joke."),
    (1, None, "'Good afternoon, Claude Monet restaurant.' 'Dobry den' is 'good day', and Russians use it for the afternoon, too. The name of the restaurant doesn't change, whatever the sentence."),
    (2, None, "'My name is Alexander.' Russian has no 'my name is': it says 'me they call Alexander'. The 'they' is not spoken."),
    (3, None, "'The exhibition is cancelled.' The event cancels itself, so the action takes 'sya'. That's the Russian form for trains and events that are called off."),
    (4, None, "'Pass this on to Victoria.' The order is the polite one, ending in 'ite'. The name takes an 'i' to say 'to'."),
    (5, None, "'All right, I will pass it on.' 'Peredam' is 'I will pass on'. It comes from the same word as Max's 'peredayte', but now it's the future."),
    (6, None, "'Grazie, signora, ciao-ciao.' More fake Italian. 'Chao' is how Russians write 'ciao', and they use it as a casual goodbye with friends."),
    (7, None, "'Yes, hello. Victoria Sergeyevna, hello.' 'Allo' is only for answering the phone. 'Zdravstvuyte' is the polite hello for people you don't know well."),
    (8, None, "'A representative of the exhibition from Milan called.' 'Zvonil' ends in 'l' for a man. 'Iz Milana' is 'from Milan', with 'a' on the city after 'from'."),
    (9, None, "'He said that it is cancelled.' 'Ona' is 'she', because 'vystavka' is feminine in Russian, so a trade show counts as a 'she'. 'Chto' here means 'that'."),
    (10, None, "'Oh, really? I am already in Domodedovo.' 'Pravda' means 'truth', and Russians say it to mean 'really?'. Vika is at one of Moscow's airports, and she says 'v' for 'in' with no change to the name."),
    (11, None, "'I almost flew away.' 'Almost' is made of 'barely' and 'not', which is a quirk of the phrase. 'Flew off' starts with 'u', the prefix for 'away'."),
    (12, None, "'Thank you for warning me.' 'Thanks that' is how you say thanks for something. The polite 'warned' is in the plural."),
]
