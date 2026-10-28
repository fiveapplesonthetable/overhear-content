# Authoring module for kukhnya-s01e08-scene-08.
ID = 'kukhnya-s01e08-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 8
TITLE = "Собака Нагиева  (Nagiyev's Dog)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Meanwhile, at Claude Monet, Max the cook is in on his day off, and Vika the hostess is minding Tyson, the owner Nagiyev's dog. A hot dog and a broken socket are about to ruin everyone's afternoon. It's in Russian first."
OPENER = "Let's go back through the accident. It all happens fast, so the sentences are short."
TRANSITION = 'Now the whole disaster again, in one go.'
OUTRO = "Short emergency words come in handy: ostorozhno, 'careful', spokoyno, 'calm down', and bystreye, 'quick'. And note that sobaka, 'dog', is feminine even for a male dog, while pyos is the masculine word. See you next time."
CLOSING = ('max', 'До встречи!')
STORY = [
    ('vika', 'Макс, почему ты ходишь без формы?', 'Max, why are you walking without a uniform?', [(98, 'Что за внешний вид? Где форма')], ''),
    ('max', 'У меня сегодня законный выходной день!', 'Today is my legitimate day off!', [(99, 'У меня сегодня уходной')], ''),
    ('max', 'Мои единственные джинсы сейчас стираются.', 'My only jeans are in the wash right now.', [(99, 'А джинсы стираются')], ''),
    ('vika', 'Здесь ресторан, а не домашняя прачечная.', 'This is a restaurant, not a home laundromat.', [(100, 'У тебя что, здесь прачечная')], ''),
    ('max', 'И чья это маленькая злая собака?', 'And whose little angry dog is this?', [(104, 'Тайсон, фу')], ''),
    ('vika', 'Это Тайсон, любимая собака Нагиева.', "This is Tyson, Nagiyev's favorite dog.", [(109, 'Ты сдашь, чья эта собака')], ''),
    ('max', 'Осторожно, собака схватила мой хот-дог!', 'Careful, the dog grabbed my hot dog!', [(105, 'Капец сосиски')], ''),
    ('vika', 'Тайсон, фу, немедленно брось сосиску!', 'Tyson, drop it, drop the sausage immediately!', [(104, 'Тайсон, фу'), (106, 'Тайсон')], ''),
    ('max', 'Ой, кажется, собаку ударило током!', 'Oh, it seems the dog was hit by electric current!', [(105, 'Офигеть')], ''),
    ('vika', 'Боже мой, он лежит и не дышит!', 'My God, he is lying and not breathing!', [(110, 'Боже мой, что я скажу')], ''),
    ('max', 'Я же говорил, эта розетка сломана!', 'I told you, this socket is broken!', [(107, 'Это ты за ней не уследила')], ''),
    ('vika', 'Что я теперь скажу Дмитрию Владимировичу?', 'What will I say to Dmitry Vladimirovich now?', [(110, 'что я скажу Дмитрию Владимировну')], ''),
    ('max', 'Спокойно, давай положим собаку в пакет.', "Calm down, let's put the dog in a bag.", [(114, 'ты в пакет')], ''),
    ('vika', 'Быстрее бежим к ветеринару спасать пса!', "Quick, let's run to the vet to save the dog!", [(115, 'О, Господи')], ''),
]
WALK = [
    (0, None, "'Max, why are you walking without a uniform?' Vika uses khodish, from khodit, for going around in general or for what you wear, rather than one trip. After bez, 'without', forma becomes formy."),
    (1, None, "'Today is my legitimate day off!' Built on zakon, 'law', zakonnyy means a day off by right. Russians call a day off vykhodnoy, from vykhodit, 'to go out'."),
    (2, None, "'My only jeans are in the wash right now.' As in English, dzhinsy exists only in the plural. Adding -sya to stirat, 'to wash clothes', gives stirayutsya, 'are being washed'."),
    (3, None, "'This is a restaurant, not a home laundromat.' Here a ne, 'and not', sets up the contrast, X, a ne Y, as in Barinov's shef-povar, a ne akter. The word prachechnaya, 'laundry', comes from an old word for washing clothes."),
    (4, None, "'And whose little angry dog is this?' To match sobaka, 'dog', whose becomes chya. For the same reason malenkaya and zlaya end in -aya."),
    (5, None, "'This is Tyson, Nagiyev's favorite dog.' Russian puts the owner after the dog and adds -a to his surname: 'the dog of Nagiyev'. The word lyubimaya, 'favourite', comes from lyubit, 'to love'."),
    (6, None, "'Careful, the dog grabbed my hot dog!' Notice that skhvatila ends in -a because sobaka is feminine, even though Tyson is male. And ostorozhno, 'careful', is the warning you shout."),
    (7, None, "'Tyson, drop it, drop the sausage immediately!' Russians say fu to a dog doing something bad, like 'no!' or 'leave it!'. The command bros, 'drop', comes from brosit, 'to throw'."),
    (8, None, "'Oh, it seems the dog was hit by electric current!' There's no subject in sobaku udarilo tokom: literally 'it struck the dog with current'. The current takes -om, tokom, and the dog is the object, sobaku."),
    (9, None, "'My God, he is lying and not breathing!' Vika says on, 'he', because Tyson is male, even though sobaka is feminine. And ne dyshit, 'isn't breathing', comes from dyshat."),
    (10, None, "'I told you, this socket is broken!' In ya zhe govoril, 'I did tell you', zhe adds the 'didn't I say so'. The -a on slomana matches rozetka, 'socket'."),
    (11, None, "'What will I say to Dmitry Vladimirovich now?' After skazhu, 'I'll tell', both his first name and his patronymic change, to -yu and -u. Name and patronymic, 'son of Vladimir', is how the staff address their boss."),
    (12, None, "'Calm down, let's put the dog in a bag.' On its own, spokoyno, 'calmly', works as 'calm down'. Between friends, 'let's put' is davay plus the 'we' form: davay polozhim."),
    (13, None, "'Quick, let's run to the vet to save the dog!' Here bezhim, 'let's run', is the 'we' form used as a suggestion. For a male dog there's also pyos, and as the one being saved it becomes psa."),
]
