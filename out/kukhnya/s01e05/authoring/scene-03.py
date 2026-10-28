# Authoring module for kukhnya-s01e05-scene-03.
ID = 'kukhnya-s01e05-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 3
TITLE = 'Операция «Треска»  (Operation Cod)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Over in the Claude Monet kitchen, Chef Barinov has a problem that has nothing to do with love: somebody thawed a pile of cod, and it all has to be sold today. He gathers the staff and pulls in Sasha, one of the waitresses, to help. Listen to it in Russian first.'
OPENER = 'Now slowly. Barinov gives orders, and orders are short, which suits us.'
TRANSITION = 'Once more from the top, at full speed.'
OUTRO = 'Some of this works in any job: "ponyatno" for \'understood\', and "chto nam teper delat" for \'what do we do now\'. As for the cod, Barinov means that fine.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Внимание, повара! Начнём наше собрание.', 'Attention, cooks! Let us begin our meeting.', [(38, 'начнем собрание')], ''),
    ('sasha', 'Шеф, что сегодня стряслось на кухне?', 'Chef, what happened in the kitchen today?', [], ''),
    ('barinov', 'Кто-то вчера разморозил пять килограммов трески.', 'Someone thawed five kilograms of cod yesterday.', [(39, 'разморозил пять килограммов трески')], ''),
    ('sasha', 'И что нам теперь делать?', 'And what are we to do now?', [], ''),
    ('barinov', 'Мы обязаны продать всю рыбу сегодня!', 'We must sell all the fish today!', [(40, 'мы должны ее сегодня продать')], ''),
    ('sasha', 'Гости заказывают только мясо и пасту.', 'Guests only order meat and pasta.', [], ''),
    ('barinov', 'Саша, подойди ко мне немедленно.', 'Sasha, come to me immediately.', [(42, 'Саша! Зайди сюда')], ''),
    ('sasha', 'Я слушаю вас внимательно, шеф.', 'I am listening to you carefully, chef.', [(43, 'Да, шеф')], ''),
    ('barinov', 'Передай официантам: сегодня активно предлагаем треску.', 'Tell the waiters: today we actively offer cod.', [(43, 'что сегодня продаем треску')], ''),
    ('sasha', 'Может быть, сделаем специальную скидку?', 'Maybe we will give a special discount?', [], ''),
    ('barinov', 'Да, скидка двадцать процентов на рыбу.', 'Yes, twenty percent discount on fish.', [(44, 'скидка 20%')], ''),
    ('sasha', 'Понятно, шеф, мы всё организуем.', 'Understood, chef, we will organize everything.', [(45, 'Понятно')], ''),
    ('barinov', 'Если рыба останется, я вас оштрафую!', 'If fish remains, I will fine you!', [], ''),
]
WALK = [
    (0, None, '\'Attention, cooks! Let us begin our meeting.\' "Vnimanie" works just like \'attention!\' in English. "Povar", \'cook\', makes its plural with a stressed -a, "povara", as a handful of common words do.'),
    (1, None, '\'Chef, what happened in the kitchen today?\' "Stryaslos" is a dramatic \'happened\', for something bad that has suddenly landed on you. Kitchens take "na", not "v": "na kukhne", \'in the kitchen\'.'),
    (2, None, '\'Someone thawed five kilograms of cod yesterday.\' "Kto-to" is "kto", \'who\', plus -to, making \'someone\'. "Razmorozil" has "moroz", \'frost\', inside, with "raz-" undoing it, and after "pyat" comes "kilogrammov treski", \'of kilograms of cod\'.'),
    (3, None, '\'And what are we to do now?\' Literally \'and what to-us now to do?\'. There\'s no \'should\' and no \'are\', just "nam", \'to us\', and the bare verb "delat".'),
    (4, None, '\'We must sell all the fish today!\' "Obyazany" is a strong \'must\', close to \'we are obliged\'. "Ryba", \'fish\', becomes "vsyu rybu" because it\'s what gets sold.'),
    (5, None, '\'Guests only order meat and pasta.\' Pasta becomes "pastu" as the thing ordered, while "myaso", \'meat\', stays as it is: words ending in -o don\'t change here.'),
    (6, None, '\'Sasha, come to me immediately.\' "Podoydi" is a command to one person, \'come over\'. Before "mne", the little "k", \'to\', gets an extra vowel and becomes "ko": "ko mne".'),
    (7, None, '\'I am listening to you carefully, chef.\' Sasha uses "vas", the polite \'you\', with her boss. "Vnimatelno", \'carefully\', is built on "vnimanie", the \'attention!\' that opened the scene.'),
    (8, None, '\'Tell the waiters: today we actively offer cod.\' "Peredai" is \'pass on\', for handing a message along. "Ofitsiantam" ends in -am, meaning \'to the waiters\'.'),
    (9, None, '\'Maybe we will give a special discount?\' "Mozhet byt" is literally \'may be\'. Sasha phrases her idea as a question, the safe way to suggest something to a boss.'),
    (10, None, '\'Yes, twenty percent discount on fish.\' "Dvadtsat", \'twenty\', is "dva", \'two\', glued to a shortened \'ten\'. After it, "protsent" takes the form "protsentov", as it does after five, six and so on.'),
    (11, None, '\'Understood, chef, we will organize everything.\' "Ponyatno", \'understood\', is the word to use with any boss. "Organizuem" looks like English, with -em for \'we\'.'),
    (12, None, '\'If fish remains, I will fine you!\' "Esli", \'if\', opens the threat. "Oshtrafuyu" hides "shtraf", \'a fine\', and "vas" here means the whole staff.'),
]
