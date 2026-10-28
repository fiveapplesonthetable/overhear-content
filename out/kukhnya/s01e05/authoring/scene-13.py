# Authoring module for kukhnya-s01e05-scene-13.
ID = 'kukhnya-s01e05-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 13
TITLE = 'Предупреждение от Вики  (A Warning from Vika)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Vika, who runs the Claude Monet dining room, has heard that Nastya has been crying all day. She finds Max at his station in the kitchen, in the middle of making soup, and gives him a warning. Listen to it in Russian first.'
OPENER = 'Now slowly. Vika is angry and precise, which makes her easy to follow.'
TRANSITION = 'Now see how much you catch.'
OUTRO = 'Vika\'s warning is made of pieces you can reuse: "bolshe nikogda", "v posledniy raz", "iz-za tebya". And Max\'s reply shows the classic way to survive it: say "ponyal" and go back to the soup.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('vika', 'Макс, иди сюда прямо сейчас!', 'Max, come here right now!', [(159, 'Иди сюда')], ''),
    ('max', 'Привет, Вика, что случилось?', 'Hi, Vika, what happened?', [(159, 'привет')], ''),
    ('vika', 'Слушай меня очень внимательно.', 'Listen to me very carefully.', [(160, 'слушай сюда внимательно')], ''),
    ('vika', 'Не трогай моих официанток больше никогда!', "Don't touch my waitresses ever again!", [(161, 'кого-то из моих официанток')], ''),
    ('vika', 'Или я приму очень строгие меры.', 'Or I will take very strict measures.', [(162, 'Тебе вот этот')], ''),
    ('max', 'Вика, почему ты так сильно злишься?', 'Vika, why are you so angry?', [(163, 'Вик, да что с тобой')], ''),
    ('vika', 'Бедная Настя плачет из-за тебя весь день.', 'Poor Nastya has been crying because of you all day.', [(164, 'Настя рыдает целый день')], ''),
    ('max', 'Но между нами абсолютно ничего не было!', 'But absolutely nothing happened between us!', [(165, 'ничего не было')], ''),
    ('vika', 'Я видела ваши странные разговоры у бара.', 'I saw your strange conversations by the bar.', [(167, 'я все видела')], ''),
    ('vika', 'Я предупредила тебя в последний раз.', 'I warned you for the last time.', [(169, 'Я тебя предупредила')], ''),
    ('max', 'Хорошо, я понял тебя, спасибо за совет.', 'Alright, I understood you, thanks for the advice.', [(168, 'мне все равно')], ''),
    ('max', 'Теперь мне нужно быстро посолить суп.', 'Now I need to quickly salt the soup.', [(173, 'осталось посолить')], ''),
    ('max', 'И не забыть добавить свежих сливок.', 'And not forget to add fresh cream.', [(174, 'добавить сливок')], ''),
]
WALK = [
    (0, None, '\'Max, come here right now!\' Russian has two words for \'here\': "zdes" for where you are, and "syuda" for where you\'re going. "Idi syuda", \'come here\', needs the second.'),
    (1, None, '\'Hi, Vika, what happened?\' "Chto sluchilos" is the question to ask when someone looks upset. It\'s related to "sluchay", \'an occurrence\'.'),
    (2, None, '\'Listen to me very carefully.\' "Slushay menya", \'listen to me\', takes "menya" directly, with no \'to\'. "Vnimatelno", \'carefully\', is the attention word again.'),
    (3, None, '\'Don\'t touch my waitresses ever again!\' "Ofitsiantka", \'waitress\', is "ofitsiant" plus -ka. \'Never again\' is "bolshe nikogda", literally \'more never\'.'),
    (4, None, '\'Or I will take very strict measures.\' "Primu mery" means \'I\'ll take measures\', from "prinyat", the same verb Nastya used for taking a decision. "Strogie", \'strict\', is plural to match "mery".'),
    (5, None, '\'Vika, why are you so angry?\' "Zlishsya" is from "zlitsya", \'to be cross\', another verb that always carries -sya. "Tak silno" is \'so strongly\'.'),
    (6, None, '\'Poor Nastya has been crying because of you all day.\' "Iz-za tebya", \'because of you\', points the finger at someone. "Plachet" is present tense, since she\'s still crying.'),
    (7, None, '\'But absolutely nothing happened between us!\' "Mezhdu nami", \'between us\', puts \'us\' in the form "nami". Max also stacks the negatives again: "nichego ne bylo".'),
    (8, None, '\'I saw your strange conversations by the bar.\' "Videla" ends in -la, so the one who saw is a woman. "U bara" is \'by the bar\', with "u", \'at\', taking -a.'),
    (9, None, '\'I warned you for the last time.\' "Predupredila", \'warned\', begins with "pred-", \'before\', since a warning comes before trouble. \'For the last time\' is "v posledniy raz".'),
    (10, None, '\'Alright, I understood you, thanks for the advice.\' "Spasibo za sovet", \'thanks for the advice\', said a little too politely. "Sovet" also means \'council\', as in Soviet.'),
    (11, None, '\'Now I need to quickly salt the soup.\' "Posolit", \'to salt\', has "sol", \'salt\', at its core. "Mne nuzhno" means \'I need to\', literally \'to me it\'s needed\'.'),
    (12, None, '\'And not forget to add fresh cream.\' "Slivki", \'cream\', only exists in the plural. "Svezhikh slivok" takes the \'of\' form, meaning \'some fresh cream\'.'),
]
