# Authoring module for kukhnya-s01e18-scene-10.
ID = 'kukhnya-s01e18-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 10
TITLE = 'Плохая рыба  (Bad Fish)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = "In the changing room, Senya is looking green. He ate some fish he had stashed away in the kitchen, and Fedya has come to check on him. Listen for how Fedya's cure gets stronger with every line."
OPENER = 'Back to the first worried question.'
TRANSITION = 'Now the whole sickbed chat, start to end.'
OUTRO = 'Senya\'s resolve to stop stealing food lasts exactly as long as his stomach ache. Keep "slyshish?", you hear?, apart from "slushat", to listen on purpose. See you next time!'
CLOSING = ('fedya', 'Удачи!')
STORY = [
    ('fedya', 'Сеня, у тебя всё хорошо?', 'Senya, are you all right?', [(229, 'У тебя все хорошо')], ''),
    ('senya', 'Нет, мне очень плохо.', 'No, I feel really bad.', [(230, 'Нет')], ''),
    ('fedya', 'Я же тебе говорил, не ешь эту рыбу.', 'I told you not to eat that fish.', [(230, 'Я тебе говорил, не ешь эту рыбу')], ''),
    ('fedya', 'Ты пил активированный уголь?', 'Did you take activated charcoal?', [(231, 'Ты уголь пил')], ''),
    ('senya', 'Да, я уже выпил две пачки.', 'Yes, I have already taken two packs.', [(231, 'две пачки')], ''),
    ('senya', 'Но мне это совсем не помогло.', 'But it did not help me at all.', [], ''),
    ('fedya', 'Я когда на флоте служил, медузу нечаянно съел.', 'When I served in the Navy, I accidentally ate a jellyfish.', [(233, 'я когда на флоте служил'), (233, 'медузу один раз нечаянно съел')], ''),
    ('fedya', 'Тогда боцман сразу налил мне крепкого.', 'Back then the boatswain immediately poured me a strong drink.', [(234, 'сразу не налил')], ''),
    ('fedya', 'Слышишь, что я говорю?', 'Do you hear what I am saying?', [(235, 'Слышишь, что говорю')], ''),
    ('fedya', 'Тебе надо выпить чего-нибудь крепкого.', 'You need to drink something strong.', [(235, 'чего-нибудь крепкого надо')], ''),
    ('senya', 'Хорошо, сейчас пойду поищу в баре.', 'Alright, I will go look for some at the bar now.', [(236, 'сейчас пойду поищу')], ''),
    ('senya', 'Если выживу, воровать продукты перестану!', 'If I survive, I will stop stealing food!', [(237, 'Если выживу, воровать перестану')], ''),
]
WALK = [
    (0, None, '\'Senya, are you all right?\' "U tebya vsyo khorosho?", literally \'at you all good?\', is the everyday way to ask if someone is okay.'),
    (1, None, '\'No, I feel really bad.\' How you feel goes to \'me\': "mne ochen plokho", \'to me very bad\'.'),
    (2, None, '\'I told you not to eat that fish.\' "Zhe" adds \'didn\'t I\'. In "ne yesh etu rybu", don\'t eat that fish, "ryba" becomes "rybu" as the thing eaten.'),
    (3, None, '\'Did you take activated charcoal?\' Russians drink their medicine: "pit", to drink, covers tablets too. "Ugol" is coal, and charcoal.'),
    (4, None, '\'Yes, I\'ve already taken two packs.\' "Vypil" means drank down, all of it. It\'s "dve", not "dva", because "pachka", pack, is feminine.'),
    (5, None, '\'But it didn\'t help me at all.\' Help goes \'to me\': "mne ne pomoglo". "Sovsem ne" is not at all.'),
    (6, None, '\'When I served in the navy, I accidentally ate a jellyfish.\' You serve \'on\' the fleet: "na flote". "Nechayanno" means by accident.'),
    (7, None, '\'Then the boatswain poured me something strong.\' "Botsman", boatswain, is an old sailors\' borrowing. "Nalil mne krepkogo" leaves out the drink itself: \'poured me some strong\'.'),
    (8, None, '\'Do you hear what I\'m saying?\' "Slyshish", you hear, is about catching sounds. On its own, "slyshish" is also a rough \'hey, listen\'.'),
    (9, None, '\'You need to drink something strong.\' "Tebe nado", \'to you it\'s needed\'. Tagging "-nibud" onto "chego" makes \'anything at all\'.'),
    (10, None, '\'All right, I\'ll go and look for some at the bar.\' "Poydu poishchu", \'I\'ll go, I\'ll look\', with no \'and\': very spoken Russian. "V bare", at the bar.'),
    (11, None, '\'If I survive, I\'ll stop stealing food!\' "Vorovat", to steal, comes from "vor", thief. "Produkty" means groceries, not products.'),
]
