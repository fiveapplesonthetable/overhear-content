# Authoring module for kukhnya-s01e06-scene-15.
ID = 'kukhnya-s01e06-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 15
TITLE = 'Писатель Виктор Пелевин  (The Writer Viktor Pelevin)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Back at Claude Monet, Max has a plan to get Rodion a table: book it in the name of Viktor Pelevin, a famous writer whom nobody ever sees. Kostya thinks it's madness. It's in Russian first."
OPENER = "Let's go through the phone call and the argument after it. Max is sure of himself, and Kostya isn't."
TRANSITION = "Here's the booking and the argument in one go."
OUTRO = 'You can now book a table in Russian: "zabronirovat stolik", for whom, and the name. And if you need to worry out loud, a "esli" and "vdrug" both mean \'what if\'. See you next time.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Алло, ресторан, я хочу забронировать столик.', 'Hello, restaurant, I want to reserve a table.', [(201, 'Ресторан Клод Мане, я слушаю вас')], ''),
    ('kostya', 'Макс, для кого именно ты заказываешь стол?', 'Max, for whom exactly are you booking a table?', [(204, 'Макс, какой Пелевин?')], ''),
    ('max', 'Для известного русского писателя Виктора Пелевина.', 'For the famous Russian writer Viktor Pelevin.', [(202, 'для писателя Виктора Пелевина')], ''),
    ('kostya', 'Ты с ума сошёл, какой ещё Пелевин?', 'Are you out of your mind, what Pelevin?', [(204, 'Макс, какой Пелевин?')], ''),
    ('max', 'Администратор очень обрадовалась такому важному гостю.', 'The administrator was very thrilled with such an important guest.', [(203, 'Какая честь. Ждем вас')], ''),
    ('kostya', 'А если Виктория знает его в лицо?', 'And what if Victoria knows what he looks like?', [(205, 'Вдруг она знает, как он выглядит')], ''),
    ('max', 'Пелевин — загадочный писатель, никто его не видел.', 'Pelevin is a mysterious writer, nobody has seen him.', [(206, 'Ты знаешь, как выглядит Виктор Пелевин?')], ''),
    ('kostya', 'Вдруг в ресторане есть его преданные читатели?', 'What if there are his devoted readers in the restaurant?', [(205, 'как он выглядит, а?')], ''),
    ('max', 'Они видели только его имя на обложке.', 'They only saw his name on the cover.', [(206, 'Да ладно тебе')], ''),
    ('kostya', 'Как Родион сможет убедительно изобразить гения?', 'How will Rodion be able to convincingly portray a genius?', [(207, 'А я знаю')], ''),
    ('max', 'Он просто наденет тёмные очки.', 'He will simply put on dark glasses.', [(208, 'Вот так')], ''),
    ('kostya', 'Надеюсь, эта безумная авантюра сработает сегодня.', 'I hope this crazy gamble will work today.', [(208, 'Вот так')], ''),
]
WALK = [
    (0, None, '\'Hello, restaurant, I want to reserve a table.\' "Allo" is the hello you only say on the phone. "Stolik" is a \'little table\', which is what you book in a restaurant.'),
    (1, None, '\'Max, for whom exactly are you booking a table?\' "Dlya kogo", for whom, changes "kto" to "kogo" after "dlya". "Zakazyvaesh", you\'re ordering, is also how you order food in a restaurant.'),
    (2, None, '\'For the famous Russian writer Viktor Pelevin.\' After "dlya" every word changes: "izvestnogo", "russkogo", "pisatelya", "Viktora Pelevina". That pile of endings is what makes the sentence sound so official.'),
    (3, None, '\'Are you out of your mind, what Pelevin?\' "S uma soshyol", \'gone down off the mind\', is the idiom for \'gone mad\'. "Kakoy eshche" Pelevin, \'what other Pelevin\', means \'what are you on about?\'.'),
    (4, None, '\'The administrator was very thrilled with such an important guest.\' "Obradovalas", was delighted, ends in -as, so the administrator is a woman. "Takomu vazhnomu gostyu" is \'at such an important guest\', with -omu and -yu on each word.'),
    (5, None, '\'And what if Victoria knows what he looks like?\' "Znaet v litso", \'knows in the face\', means knows him by sight. Kostya is worried she\'d spot the fake at once.'),
    (6, None, '\'Pelevin is a mysterious writer, nobody has seen him.\' "Zagadochnyy", mysterious, is from "zagadka", a riddle. "Nikto ego ne videl" has two negatives, "nikto" and "ne", as Russian always does.'),
    (7, None, '\'What if there are his devoted readers in the restaurant?\' "Vdrug", suddenly, works as \'what if\' at the start of a worried question. "Chitateli", readers, are people who "chitat", read.'),
    (8, None, '\'They only saw his name on the cover.\' "Imya", name, doesn\'t change here because it\'s what they saw. "Na oblozhke", on the cover, turns "oblozhka" into -e for the place.'),
    (9, None, '\'How will Rodion be able to convincingly portray a genius?\' "Smozhet", will be able, is the future of "moch", can. "Geniya" is genius with -ya, because it\'s what he\'ll portray.'),
    (10, None, '\'He will simply put on dark glasses.\' "Ochki", glasses, only exists in the plural. "Nadenet", will put on, is the verb for clothes; for a hat or glasses you use it too.'),
    (11, None, '\'I hope this crazy gamble will work today.\' "Avantyura", a risky adventure, is a French loan with a bad reputation in Russian. "Bezumnaya", crazy, is literally \'without mind\': "bez" plus "um".'),
]
