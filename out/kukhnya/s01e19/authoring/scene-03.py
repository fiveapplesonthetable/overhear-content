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
INTRO = "Later that morning Max is back at the flat, and this time it's Kostya asking the questions. Russian first, as always; the gist is plenty."
OPENER = "Let's go through Kostya's questions one at a time."
TRANSITION = 'And now straight through, the way the two friends said it.'
OUTRO = "Kostya has lost his job and Max has lost his night at Vika's, and you heard both in plain Russian. See you next time!"
CLOSING = ('kostya', 'Давай, пока!')
STORY = [
    ('kostya', 'Что ты здесь делаешь?', 'What are you doing here?', [(29, 'Что ты здесь делаешь? Что не на работе?')], ''),
    ('kostya', 'Что не на работе?', "Why aren't you at work?", [(29, 'Что ты здесь делаешь? Что не на работе?')], ''),
    ('max', 'Опять допрос.', 'Another interrogation.', [(31, 'Опять допрос. Вы что, сговорились что ли?')], ''),
    ('max', 'Вы сговорились что ли?', 'Did you plan this or something?', [(31, 'Опять допрос. Вы что, сговорились что ли?')], ''),
    ('max', 'Я сегодня во вторую смену.', 'I am on the second shift today.', [(32, 'Я сегодня в вторую смену.')], ''),
    ('kostya', 'Отлично. Я с тобой поеду.', 'Great. I will go with you.', [(33, 'Отлично. Я с тобой поеду.')], ''),
    ('max', 'Может ты забыл,', 'Maybe you forgot,', [(34, 'Костян, может ты забыл, но у тебя вроде это.')], ''),
    ('kostya', 'Да, я помню.', 'Yeah, I remember.', [(35, 'Да, да, я помню, меня уволили. Мне надо забрать кое-что.')], ''),
    ('kostya', 'Меня уволили.', 'I got fired.', [(35, 'Да, да, я помню, меня уволили. Мне надо забрать кое-что.')], ''),
    ('kostya', 'А что ты у Вики не остался?', "Why didn't you stay at Vika's?", [(36, 'А что ты у Викини остался?')], ''),
    ('max', 'Она меня не пустила.', "She wouldn't let me in.", [(36, 'А что ты у Викини остался? Она меня не пустила.')], ''),
    ('max', 'Она все усложнять начала.', 'She started making everything complicated.', [(39, 'Она все усложнять начала.')], ''),
]
WALK = [
    (0, None, "'What are you doing here?' \"Delaesh\", 'you're doing', ends in -esh because these two are on \"ty\" terms. \"Zdes'\" is 'here', the spot you're in."),
    (1, None, "'Why aren't you at work?' \"Chto\" here means 'why', a casual shortcut you'll hear a lot. \"Na rabote\" is 'at work': after \"na, rabota\" becomes \"rabote\"."),
    (2, None, "'Another interrogation.' \"Opyat'\" means 'again', with a sigh built in. \"Dopros\" is the very word Max threw at Vika last night, and now he's on the receiving end."),
    (3, None, "'Did you plan this or something?' Vy here is plural: Max means Kostya and Vika together. \"Sgovorilis'\" is 'you agreed between yourselves', and \"chto\" li on the end means 'or what?'."),
    (4, None, "'I'm on the second shift today.' \"Vo vtoruyu smenu\" is literally 'into the second shift'. \"V\" becomes \"vo\" here because \"vtoruyu\" starts with two consonants."),
    (5, None, "'Great. I'll go with you.' \"Poedu\" is 'I'll go' by car or bus; on foot it would be \"poydu\". \"S toboy\", 'with you', is the friendly 'you' after \"s\"."),
    (6, None, "'Maybe you forgot,' \"Mozhet\", 'maybe', softens what Max is about to say. \"Zabyl\", 'forgot', is the form for a man, since he's talking to Kostya."),
    (7, None, "'Yeah, I remember.' \"Ya pomnyu\" is 'I remember', and Kostya says it before Max has to finish. \"Pomnyu\" ends in -yu, a usual ending for 'I'."),
    (8, None, "'I got fired.' \"Menya uvolili\" is literally 'me they fired', the standard way to say you lost your job. Swap in \"ego\" and it's 'he got fired'."),
    (9, None, "'Why didn't you stay at Vika's?' \"U Viki\" means 'at Vika's place': after \"u\", Vika becomes \"Viki\". The same \"u\" gives \"u mamy\", 'at Mum's'."),
    (10, None, "'She wouldn't let me in.' \"Ne pustila\", 'didn't let in', ends in -a because Vika is the one who refused. \"Pustite\", 'let me in', is what you'd shout at a locked door."),
    (11, None, "'She started making everything complicated.' \"Uslozhnyat'\", 'to complicate', is built on \"slozhny\", 'complicated'. Putting it before \"nachala\", 'started', sounds very conversational."),
]
