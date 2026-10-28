# Authoring module for kukhnya-s01e05-scene-20.
ID = 'kukhnya-s01e05-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 20
TITLE = 'Просьба о помощи  (A Request for Help)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "In the Claude Monet kitchen, the dinner rush has buried Max at the fish station. He has to ask Fedya, the fish cook he's been feuding with, for help, and Fedya isn't going to make it easy. Listen in Russian first."
OPENER = "Slowly now. Fedya pretends he can't hear, and that's how he gets Max to apologise again and again."
TRANSITION = "Here's the whole apology, start to finish."
OUTRO = 'Between them they\'ve given you "pomogi", \'help me\', "izvini", \'sorry\', and "uspokoysya", \'calm down\'. That\'s a decent kit for making up with a colleague.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Федя, пожалуйста, помоги мне с заказами.', 'Fedya, please help me with the orders.', [(292, 'Слушай, Федь, извини'), (294, 'Помоги с заказами')], ''),
    ('fedya', 'Что ты говоришь? Я плохо слышу.', "What are you saying? I can't hear well.", [(295, 'Что? Извини, говорю')], ''),
    ('max', 'Я говорю, что прошу прощения.', 'I am saying that I ask for forgiveness.', [(293, 'Я зря себя так вывел')], ''),
    ('fedya', 'Коллеги, можно потише на кухне, пожалуйста?', 'Colleagues, could you be quieter in the kitchen, please?', [(296, 'Коллеги! Можно потише чуть-чуть, пожалуйста')], ''),
    ('fedya', 'Макс хочет сказать нам что-то важное.', 'Max wants to tell us something important.', [(297, 'человек что-то важное сказать хочет')], ''),
    ('max', 'Федя, извини меня за всё.', 'Fedya, forgive me for everything.', [(298, 'Федя, извини')], ''),
    ('max', 'Ты отличный опытный повар, а я нет.', "You're an excellent, experienced cook, and I'm not.", [(299, 'Ты прекрасный повар, а я нет')], ''),
    ('max', 'Помоги мне быстро приготовить эти блюда.', 'Help me quickly prepare these dishes.', [(300, 'Помоги мне, пожалуйста, с заказами')], ''),
    ('fedya', 'Я всё очень хорошо услышал.', 'I heard everything very well.', [(301, 'Понятно')], ''),
    ('fedya', 'Но я тебе совсем не верю.', 'But I do not believe you at all.', [(302, 'Но не верю')], ''),
    ('fedya', 'В твоих словах нет настоящей искренности.', 'In your words there is no real sincerity.', [(303, 'Ну, искренности не хватает')], ''),
    ('fedya', 'Давай повтори всё ещё разок громче!', 'Come on, repeat everything once more louder!', [(304, 'Давай еще разок')], ''),
    ('max', 'Я больше не буду ничего повторять!', 'I will not repeat anything anymore!', [(305, 'Да пошел ты')], ''),
    ('fedya', 'Ладно, успокойся, я сейчас помогу.', 'Alright, calm down, I will help now.', [], ''),
]
WALK = [
    (0, None, '\'Fedya, please help me with the orders.\' "Pozhaluysta", \'please\', also means \'you\'re welcome\'. After "s", \'with\', the plural takes -ami: "s zakazami".'),
    (1, None, '\'What are you saying? I can\'t hear well.\' "Slyshu" is from "slyshat", \'to hear\', which is different from "slushat", \'to listen\'. "Plokho", \'badly\', is the opposite of "khorosho".'),
    (2, None, '\'I am saying that I ask for forgiveness.\' "Proshu proshcheniya", literally \'I ask for forgiveness\', is a more formal apology than "izvini". "Proshchenie" becomes "proshcheniya" after "proshu".'),
    (3, None, '\'Colleagues, could you be quieter in the kitchen, please?\' "Mozhno", \'may one\', is the all-purpose way to ask permission. "Potishe", with "po-", means \'a bit quieter\'.'),
    (4, None, '\'Max wants to tell us something important.\' "Chto-to vazhnoe" is \'something important\', and "vazhnoe" takes -oe to match "chto-to". Fedya says it loudly so the whole kitchen will listen.'),
    (5, None, '\'Fedya, forgive me for everything.\' "Izvini" is the "ty" command, for a friend or an equal; to a boss it would be "izvinite". "Za vsyo", \'for everything\', has "za", the word you apologise \'for\' with.'),
    (6, None, '\'You\'re an excellent, experienced cook, and I\'m not.\' "Opytnyy" comes from "opyt", \'experience\'. "A ya net", \'and I not\', gets by without any \'am\'.'),
    (7, None, '\'Help me quickly prepare these dishes.\' "Pomogi mne" is literally \'help to me\', and Russian always helps \'to\' someone. "Prigotovit", \'to prepare\', comes straight after with no \'to\' word.'),
    (8, None, '\'I heard everything very well.\' "Uslyshal" means \'I heard\' as in \'I caught it\', the one-off partner of "slyshat". It answers his own "plokho slyshu" from a moment ago.'),
    (9, None, '\'But I do not believe you at all.\' "Verit" takes the dative, so it\'s \'I believe to you\': "tebe ne veryu". "Sovsem ne" means \'not at all\'.'),
    (10, None, '\'In your words there is no real sincerity.\' "Net", \'there is no\', puts what\'s missing into the genitive, so it\'s "iskrennosti". "V tvoikh slovakh", \'in your words\', takes the -akh ending for a place.'),
    (11, None, '\'Come on, repeat everything once more louder!\' "Razok" is a cosy form of "raz", \'one time\'. "Gromche", \'louder\', is the comparative of "gromko".'),
    (12, None, '\'I will not repeat anything anymore!\' "Bolshe ne" means \'not anymore\'. "Ne budu povtoryat" is \'I won\'t be repeating\', with "budu", \'I will be\', in front.'),
    (13, None, '\'Alright, calm down, I will help now.\' "Ladno", \'okay then\', settles things. "Uspokoysya", \'calm down\', ends in -sya, so it\'s literally \'calm yourself\'.'),
]
