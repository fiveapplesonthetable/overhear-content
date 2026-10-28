# Authoring module for domashniy-arest-s01e04-scene-29.
ID = 'domashniy-arest-s01e04-scene-29'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 4
SCENE = 29
TITLE = 'Ночная гонка  (Night Race)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.04'
SOURCE_FILE = 'sources/domashniy-arest/s01/e04.ru.dual.srt'
INTRO = "Out on the night streets of Sineozersk. Last time, Ilona brought Arkady a pillow, a blanket, and vodka, told him she had deleted the video of Samson, and joined Arkady's campaign to turn Samson into a people's hero. Meanwhile, Samson and Nina are speeding through town in the test-drive car to return it before ten o'clock. Let's listen in Russian first."
OPENER = "Let's take the scene line by line. Samson is flying down the night street, and Nina holds on tight."
TRANSITION = "Now let's listen to the whole ride once more, start to finish."
OUTRO = "So the people's candidate delivers the test-drive car before ten o'clock — right through the dealership window. See you next time!"
CLOSING = ('nina', 'Пока!')
STORY = [
    ('nina', 'Самсон, ты едешь очень быстро!', "Samson, you're driving very fast!", [(1117, 'Самсон, ты едешь очень быстро')], ''),
    ('nina', 'У меня уже голова кружится.', 'My head is spinning already.', [(1118, 'У меня')], "slang 'эти, вертолеты' -> 'уже голова кружится'"),
    ('samson', 'Нам надо сдать машину до десяти часов.', "We have to return the car before ten o'clock.", [(1119, 'до'), (1119, 'часов')], "garbled 'Дмитрий, можно задать парад до 10 часов' -> 'Нам надо сдать машину до десяти часов'"),
    ('samson', 'Я, между прочим, народный кандидат!', "I am, for your information, the people's candidate!", [(1120, 'Я, между прочим, народный кандидат')], ''),
    ('samson', 'Народный кандидат не опаздывает, понятно?', "The people's candidate isn't late, got it?", [(1121, 'Народный кандидат'), (1121, 'понятно')], "'я не опаздываю' -> 'не опаздывает'"),
    ('samson', 'И мне сейчас нельзя ехать медленно.', "And I mustn't drive slowly right now.", [(1122, 'сейчас')], "simplifies cue 1122 'Тем более, если сейчас поеду медленнее'"),
    ('samson', 'Иначе все поймут, что за рулём пьяный!', 'Otherwise everyone will realise the driver is drunk!', [(1123, 'все поймут, что за рулем пьяный')], "'Иначе' replaces 'то'"),
    ('nina', 'Правда. Давай быстрее, Самсон!', 'True. Go faster, Samson!', [], "new: clean A1 for cue 1124 'Резонно. Гони, Самсон!'"),
    ('samson', 'Тихо, тихо! Вижу полицию!', 'Quiet, quiet! I see the police!', [(1125, 'Тихо, тихо'), (1125, 'вижу')], "'полицию' added"),
    ('samson', 'Сейчас мы от них уедем.', "Now we'll get away from them.", [(1126, 'сейчас')], "slang 'оторвемся' -> 'от них уедем'"),
    ('samson', 'Я этот город отлично знаю!', 'I know this town really well!', [], "new: clean A1 for garbled cue 1127 'это горозная как свои пять пальцев'"),
    ('nina', 'Самсон, я тебя так люблю!', 'Samson, I love you so much!', [(1129, 'я тебя так люблю')], "mistranscribed 'самсун' -> 'Самсон'"),
    ('samson', 'И я тебя люблю! Смотри!', 'And I love you too! Look!', [(1131, 'Смотри')], "replaces garbled cue 1130 'А я знаю, что как могу'"),
    ('samson', 'Летим! Хоп!', "We're flying! Hop!", [(1134, 'Хоп')], "garbled 'Адраксион / Пупочек' -> 'Летим!'"),
]
WALK = [
    (0, None, "'Samson, you're driving very fast!' Russian has a special word for going by vehicle rather than on foot, and this is its 'you' form. Nina has had a few glasses of sparkling wine at dinner."),
    (1, None, "'My head is spinning already.' Literally, 'at me already the head is turning round'. Samson has his eye on the clock."),
    (2, None, "'We have to return the car before ten o'clock.' The dealership manager lent him the luxury car only until ten in the evening. After the little word 'before', both 'ten' and 'hours' take the 'of' form. And Samson is proud of his new title."),
    (3, None, "'I am, for your information, the people's candidate!' The two words in the middle mean 'by the way' or 'for your information'. He adds a rule."),
    (4, None, "'The people's candidate isn't late, got it?' In Russian, 'to be late' is a single action word, not an describing word. And then comes Samson's logic."),
    (5, None, "'And I mustn't drive slowly right now.' Literally, 'to me right now it is forbidden to drive slowly'. Why not?"),
    (6, None, "'Otherwise everyone will realise the driver is drunk!' Literally, 'that behind the steering wheel is a drunk man'. Tipsy Nina finds this argument completely convincing."),
    (7, None, "'True. Go faster, Samson!' The word for 'faster' is the 'more' form of 'fast'. Suddenly Samson spots flashing lights ahead."),
    (8, None, "'Quiet, quiet! I see the police!' The word for 'police' changes its '-ya' ending to '-yu' as the direct object. Samson isn't worried."),
    (9, None, "'Now we'll get away from them.' Adding the prefix 'u-' to the word for driving means 'to drive away'. He turns into the dark courtyards behind the Society of the Blind."),
    (10, None, "'I know this town really well!' In the show he says he knows the town like his own five fingers. Nina is thrilled by the ride."),
    (11, None, "'Samson, I love you so much!' After all their quarrels, this evening out has made her happy again. Samson grins."),
    (12, None, "'And I love you too! Look!' Right ahead of them is a loading ramp in front of the glass wall of the car dealership."),
    (13, None, "'We're flying! Hop!' The car launches off the ramp and crashes straight through the showroom window, landing inside right on time at ten o'clock."),
]
