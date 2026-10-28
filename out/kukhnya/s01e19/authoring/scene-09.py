# Authoring module for kukhnya-s01e19-scene-09.
ID = 'kukhnya-s01e19-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 9
TITLE = 'Возвращение поваров  (Return of the Cooks)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "Barinov is on the phone in his office, trying to talk Fedya into coming back. Fedya is in no hurry to forgive him. You'll hear the Russian first; just follow the tug of war."
OPENER = 'Now the phone call, line by line.'
TRANSITION = "Here's the call again from hello to ten o'clock."
OUTRO = 'Fedya held out for a promotion and settled for a start time, and you caught the whole bargain. See you next time!'
CLOSING = ('barinov', 'Всё, до завтра!')
STORY = [
    ('barinov', 'Алло, Федя, привет!', 'Hello, Fedya, hi!', [(182, 'Алло, Федь, привет.')], ''),
    ('fedya', 'Здравствуйте, шеф, как ваши дела?', 'Hello, chef, how are you?', [(183, 'Как дела? Эктор Петрович, приветствую.')], ''),
    ('barinov', 'Федя, хватит ломать комедию.', 'Fedya, quit acting.', [(194, 'Биль, хватит ломать комедию.')], ''),
    ('barinov', 'Возвращайся назад, ты мне очень нужен.', 'Come back, I really need you.', [(195, 'Возвращайся, ты мне нужен.')], ''),
    ('fedya', 'Шеф, я не вернусь на кухню.', 'Chef, I will not return to the kitchen.', [(196, 'Шеф, знаете, скорее всего, нет.')], ''),
    ('barinov', 'Я знаю, что я был виноват.', 'I know that I was at fault.', [(198, 'Я знаю, я виноват.')], ''),
    ('barinov', 'Извини, но Сеня уже согласился вернуться.', 'Sorry, but Senya has already agreed to return.', [(199, 'Извини. Сеня с Лёвой уже согласились вернуться.')], ''),
    ('fedya', 'Неужели Сеня правда согласился?', 'Did Senya really agree?', [(200, 'Да ладно, и Сеня?')], ''),
    ('barinov', 'Сеня первый согласился на всё.', 'Senya was the first to agree to everything.', [(200, 'Сеня первый согласился.')], ''),
    ('fedya', 'Тогда сделайте меня новым су-шефом.', 'Then make me the new sous-chef.', [(202, 'Вы сделаете меня су-шефом.')], ''),
    ('barinov', 'Нет, никаких су-шефов, Федя.', 'No, no sous-chefs, Fedya.', [(203, 'Нет. Поднимите зарплату.'), (204, 'Нет.')], ''),
    ('fedya', 'Хорошо, тогда я приду завтра утром.', 'Fine, then I will come tomorrow morning.', [(205, 'Ну ладно. Тогда завтра в десять.')], ''),
    ('barinov', 'Жду тебя ровно в десять часов.', "I expect you at exactly ten o'clock.", [(205, 'Тогда завтра в десять.')], ''),
]
WALK = [
    (0, None, "'Hello, Fedya, hi!' \"Allo\" is only for answering the phone; in person you'd never say it. Barinov piles on \"privet\" to sound friendly."),
    (1, None, "'Hello, chef, how are you?' \"Zdravstvuyte\" is the formal hello, and its first \"v\" is silent: 'zdrastvuyte'. Fedya says \"vashi dela\" to his old boss, who calls him \"ty\"."),
    (2, None, "'Fedya, quit acting.' \"Lomat' komediyu\", literally 'to break a comedy', means putting on an act. \"Khvatit\", 'enough', plus a verb is how you tell someone to stop."),
    (3, None, "'Come back, I really need you.' \"Ty mne nuzhen\" is literally 'you are needed to me'. That's the usual way to say 'I need you' about a person."),
    (4, None, "'Chef, I will not return to the kitchen.' \"Na kukhnyu\", 'to the kitchen', is the going-there form; in the kitchen would be \"na kukhne\". \"Ne vernus'\" already means 'won't return', without any 'will'."),
    (5, None, "'I know that I was at fault.' \"Ya vinovat\" is 'it's my fault', literally 'I am guilty'. \"Chto\" here isn't 'what' but 'that', joining the two halves."),
    (6, None, "'Sorry, but Senya has already agreed to return.' \"Izvini\" is 'sorry' to one person you call \"ty\"; Fedya would hear \"izvinite\" from a stranger. \"Soglasilsya\", 'agreed', ends in -sya."),
    (7, None, "'Did Senya really agree?' \"Neuzheli\" is a one-word 'really?!', full of surprise. Adding \"pravda\" after it only doubles the disbelief."),
    (8, None, "'Senya was the first to agree to everything.' \"Pervy\", 'first', does the job of 'was the first to'. \"Na vsyo\" is 'to everything', so Senya didn't haggle at all."),
    (9, None, "'Then make me the new sous-chef.' \"Su-shef\" is French sous-chef, literally 'under-chef'. After \"sdelayte\", 'make', the new role gets -ym and -om: \"novym su-shefom\"."),
    (10, None, "'No, no sous-chefs, Fedya.' \"Nikakikh\", 'none at all', is a firm no. \"Su-shefov\" is 'of sous-chefs', the ending you hear after words like that."),
    (11, None, "'Fine, then I will come tomorrow morning.' \"Pridu\" is 'I'll come', on foot. \"Zavtra utrom\", 'tomorrow morning', is built the same way as \"segodnya utrom\"."),
    (12, None, "'I expect you at exactly ten o'clock.' After \"desyat', chas\" becomes \"chasov\"; in the first scene, after tri, it was chasa. \"Rovno\", 'exactly', also means 'flat, even'."),
]
