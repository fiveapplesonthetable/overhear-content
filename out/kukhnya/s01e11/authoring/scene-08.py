# Authoring module for kukhnya-s01e11-scene-08.
ID = 'kukhnya-s01e11-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 8
TITLE = "Потерянный телефон  (The Lost Phone)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "guest": "anja"}
LABELS = {"guest": "Гость"}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "At the Claude Monet bar counter, an exhausted and hungover visitor approaches bartender Kostya. Relieved to recover the mobile phone he left behind the night before, he unburdens his romantic sorrows to the sympathetic bartender. Let's listen to their friendly bar exchange in Russian."
OPENER = "Now let's examine how Kostya assists the forgetful guest at the bar line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Comforted by the bartender's hospitality, the customer rests at the bar before facing the rest of his day. Next time you watch the episode, listen for the Russian expressions for 'bartender' and 'to come back' — you will catch every word right away. See you next time!"
CLOSING = ("guest", "Пока!")
STORY = [
    ('guest', 'Привет! Как твои дела, бармен?', 'Hello! How are things, bartender?', [(100, 'Здрасте.')], ''),
    ('guest', 'Здравствуйте! Как вы себя сегодня чувствуете?', 'Hello! How are you feeling today?', [(101, 'Как себя чувствуете?')], ''),
    ('guest', 'Эх, сегодня мне хуже, чем вчера.', 'Ugh, today I feel worse than yesterday.', [(101, 'Эх, хуже, чем вчера.')], ''),
    ('guest', 'Ты случайно не находил мой телефон?', 'Did you happen to find my phone?', [(102, 'Ты мой телефон не находил?')], ''),
    ('guest', 'Да, я нашёл его возле стойки.', 'Yes, I found it near the counter.', [(103, 'Находил.')], ''),
    ('guest', 'Огромное спасибо за помощь, друг!', 'Huge thanks for the help, friend!', [(103, 'О, спасибо.')], ''),
    ('guest', 'Скажи честно, моя девушка не звонила?', 'Tell me honestly, did my girlfriend not call?', [(104, 'Она не звонила?')], ''),
    ('guest', 'Нет, сюда пока никто не звонил.', 'No, no one has called here yet.', [(104, 'Нет.')], ''),
    ('guest', 'Она ещё не вернулась из Саратова.', 'She has not returned from Saratov yet.', [(105, 'Наверное, еще не вернулась из Саратова.')], ''),
    ('guest', 'Вы вчера долго говорили про неё.', 'Yesterday you spoke about her for a long time.', [(107, 'Ну, вы же мне вчера рассказывали.')], ''),
    ('guest', 'Да, память медленно возвращается ко мне.', 'Yes, my memory is slowly returning to me.', [(108, 'Да.')], ''),
    ('guest', 'Вот вам напиток за счёт заведения.', 'Here is a drink for you on the house.', [(110, 'За счет заведения.')], ''),
    ('guest', 'Спасибо тебе за доброту, дружище!', 'Thank you for your kindness, buddy!', [(111, 'Спасибо тебе, дружище.')], ''),
]
WALK = [
    (0, None, "'Hello! How are things, bartender?' The tired customer greets Kostya at the counter."),
    (1, None, "'Hello! How are you feeling today?' Here Kostya anchors the line on the word meaning 'hello' and builds the thought around 'how' and 'today'."),
    (2, None, "'Ugh, today I feel worse than yesterday.' Russian omits the present-tense verb 'to be' here, linking 'ugh' directly with 'today', combining 'ugh' with 'today' and 'worse'."),
    (3, None, "'Did you happen to find my phone?' , combining 'by chance' with 'found' and 'phone'."),
    (4, None, "'Yes, I found it near the counter.' Kostya uses the action verb meaning 'found' to focus on the single completed result, pairing it with 'counter'."),
    (5, None, "'Huge thanks for the help, friend!' Russian omits the present-tense verb 'to be' here, linking 'huge' directly with 'thanks', combining 'huge' with 'thanks' and 'help'."),
    (6, None, "'Tell me honestly, did my girlfriend not call?' , combining 'tell' with 'honestly' and 'girlfriend'."),
    (7, None, "'No, no one has called here yet.' Kostya expresses this naturally by combining the word for 'here' with 'yet' and 'called'."),
    (8, None, "'She has not returned from Saratov yet.' the guest puts the word for 'yet' together with 'returned' in a crisp, natural spoken turn of phrase."),
    (9, None, "'Yesterday you spoke about her for a long time.' Kostya recalls their conversation of the previous night."),
    (10, None, "'Yes, my memory is slowly returning to me.' The phrasing opens with 'memory' before bringing in 'slowly' and 'returns' to make the point clear."),
    (11, None, "'Here is a drink for you on the house.' Russian omits the present-tense verb 'to be' here, linking 'drink' directly with 'expense', combining 'drink' with 'expense' and 'establishment'."),
    (12, None, "'Thank you for your kindness, buddy!' Russian omits the present-tense verb 'to be' here, linking 'thank you' directly with 'kindness', combining 'thank you' with 'kindness' and 'buddy'."),
]
