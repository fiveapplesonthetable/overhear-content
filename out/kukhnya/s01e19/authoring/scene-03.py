# Authoring module for kukhnya-s01e19-scene-03.
ID = 'kukhnya-s01e19-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 3
TITLE = 'Снова допрос  (Interrogation again)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "Max and Kostya talk in the morning. Max is surprised to see Kostya still at the apartment instead of at work. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around Interrogation again line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Kostya explains that he was fired, and they both complain about their recent relationship struggles. Next time you watch the episode, listen for the Russian expressions for 'here' and 'to do' — you will catch every word right away. See you next time!"
CLOSING = ('kostya', 'До свидания.')
STORY = [
    ('max', 'Что ты здесь делаешь?', 'What are you doing here?', [(29, 'Что ты здесь делаешь? Что не на работе?')], ''),
    ('max', 'Что не на работе?', "Why aren't you at work?", [(29, 'Что ты здесь делаешь? Что не на работе?')], ''),
    ('kostya', 'Опять допрос.', 'Another interrogation.', [(31, 'Опять допрос. Вы что, сговорились что ли?')], ''),
    ('kostya', 'Вы сговорились что ли?', 'Did you plan this or something?', [(31, 'Опять допрос. Вы что, сговорились что ли?')], ''),
    ('max', 'Я сегодня во вторую смену.', 'I am on the second shift today.', [(32, 'Я сегодня в вторую смену.')], ''),
    ('kostya', 'Отлично. Я с тобой поеду.', 'Great. I will go with you.', [(33, 'Отлично. Я с тобой поеду.')], ''),
    ('max', 'Может ты забыл,', 'Maybe you forgot,', [(34, 'Костян, может ты забыл, но у тебя вроде это.')], ''),
    ('kostya', 'Да, я помню.', 'Yeah, I remember.', [(35, 'Да, да, я помню, меня уволили. Мне надо забрать кое-что.')], ''),
    ('kostya', 'Меня уволили.', 'I got fired.', [(35, 'Да, да, я помню, меня уволили. Мне надо забрать кое-что.')], ''),
    ('max', 'А что ты не у Вики остался?', "Why didn't you stay at Vika's?", [(36, 'А что ты у Викини остался? Она меня не пустила.')], ''),
    ('max', 'Она меня не пустила.', "She wouldn't let me in.", [(36, 'А что ты у Викини остался? Она меня не пустила.')], ''),
    ('kostya', 'Она все усложнять начала.', 'She started making everything complicated.', [(39, 'Она все усложнять начала.')], ''),
]
WALK = [
    (0, None, "'What are you doing here?' Max is confused to find his friend lingering at the apartment in the morning."),
    (1, None, "'Why aren't you at work?' Max bluntly asks why his friend is not at his shift at the restaurant."),
    (2, None, "'Another interrogation.' Kostya deflects the question by complaining about being interrogated, mirroring Max's earlier argument with Vika."),
    (3, None, "'Did you plan this or something?' Kostya gets defensive and accuses his friends of conspiring against him."),
    (4, None, "'I am on the second shift today.' Max explains his own presence at home by noting his later work schedule."),
    (5, None, "'Great. I will go with you.' Kostya eagerly seizes the chance to catch a ride to work later with his roommate."),
    (6, None, "'Maybe you forgot,' Max gently reminds his friend of the unfortunate situation from the previous day."),
    (7, None, "'Yeah, I remember.' Kostya sighs, acknowledging his painful reality."),
    (8, None, "'I got fired.' Kostya states his predicament plainly, noting that he was let go from his job."),
    (9, None, "'Why didn't you stay at Vika's?' Max uses the informal everyday 'you' here with 'remained', as friends and close colleagues do."),
    (10, None, "'She wouldn't let me in.' Max admits that she refused to let him stay over, highlighting the tension between them."),
    (11, None, "'She started making everything complicated.' Kostya complains that her reaction is making a simple situation overly complex."),
]
