# Authoring module for kukhnya-s01e05-scene-19.
ID = 'kukhnya-s01e05-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 19
TITLE = 'Хитрый план  (A Cunning Plan)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "At the Claude Monet bar, Kostya the bartender and Sasha the waitress compare notes. They've been staging a little game to make Max jealous, and Sasha has just told Max a story of her own. Kostya wants to make the fake plan look more real. Listen in Russian first."
OPENER = "Let's go slowly. They're plotting, so the lines come out quick and low."
TRANSITION = 'Now the whole plot again, without breaks.'
OUTRO = 'Listen for "slushay", a "mozhet" and "dogovorilis". Those three little words are how Russians float a plan to a friend and then seal it.'
CLOSING = ('sasha', 'Пока!')
STORY = [
    ('kostya', 'Саша, ну что, ты сказала Максу?', 'Sasha, well, did you tell Max?', [(278, 'ты сказала Максу')], ''),
    ('sasha', 'Да, я сказала, что забыла его.', "Yes, I said I'd forgotten him.", [(264, 'я тебя уже забыла'), (279, 'Сказала')], ''),
    ('kostya', 'И как он на это отреагировал?', 'And how did he react to that?', [(280, 'Ну и что он')], ''),
    ('sasha', 'Он очень сильно удивился и расстроился.', 'He was very surprised and upset.', [(281, 'Расплакался')], ''),
    ('kostya', 'Мне даже немного жалко его стало.', 'I even felt a little sorry for him.', [(282, 'Мне даже его жалко стало')], ''),
    ('sasha', 'Ты только никому не рассказывай правду.', 'Just do not tell anyone the truth.', [(286, 'не говорили, что мы')], ''),
    ('kostya', 'Конечно, никто ничего не узнает.', 'Of course, no one will find out anything.', [(287, 'Понятное дело')], ''),
    ('sasha', 'Спасибо, ты настоящий верный друг!', "Thank you, you're a true, loyal friend!", [], ''),
    ('kostya', 'Слушай, а может мы сходим куда-нибудь?', 'Listen, maybe we should go somewhere?', [(288, 'а может мы с тобой повстречаемся')], ''),
    ('sasha', 'Куда именно ты предлагаешь пойти?', 'Where exactly do you suggest going?', [], ''),
    ('kostya', 'Давай сходим в кино вместе.', 'Let us go to the movies together.', [(290, 'в кино, я не знаю, сходим')], ''),
    ('kostya', 'Это нужно для правдоподобности нашего плана.', 'This is needed for the believability of our plan.', [(289, 'Для правдоподобности')], ''),
    ('sasha', 'Отличная идея, пойдём сегодня вечером!', 'Great idea, let us go tonight!', [(291, 'ну давай')], ''),
    ('kostya', 'Договорились, тогда встретимся после работы.', 'Agreed, then let us meet after work.', [(291, 'Так точно никто не догадается')], ''),
]
WALK = [
    (0, None, '\'Sasha, well, did you tell Max?\' "Nu chto" is a casual \'so?\'. "Skazala" has -la because Sasha is a woman, and "Maksu", \'to Max\', takes the dative -u.'),
    (1, None, '\'Yes, I said I\'d forgotten him.\' "Skazala" and "zabyla" share the -la ending, because Sasha is talking about herself. "Chto" here means \'that\', the word that joins the two halves.'),
    (2, None, '\'And how did he react to that?\' "Otreagiroval" is the English \'react\' with a Russian prefix and ending. Russians react \'on\' something: "na eto", \'on that\'.'),
    (3, None, '\'He was very surprised and upset.\' "Udivilsya" and "rasstroilsya" both carry -sya, for \'got surprised\' and \'got upset\'. "Ochen silno", \'very strongly\', together just means \'really\'.'),
    (4, None, '\'I even felt a little sorry for him.\' "Mne zhalko ego stalo" is literally \'to me pity him became\'. The one who feels sorry is "mne", \'to me\', and the one pitied is "ego".'),
    (5, None, '\'Just do not tell anyone the truth.\' "Ne rasskazyvay" is \'don\'t tell\', and Nastya means it as a plea. "Pravda" becomes "pravdu" as the thing not told.'),
    (6, None, '\'Of course, no one will find out anything.\' "Nikto nichego ne uznaet" stacks three negatives, and Russian needs all of them. "Uznaet" is perfective, so it\'s future: \'will find out\'.'),
    (7, None, '\'Thank you, you\'re a true, loyal friend!\' "Nastoyashchiy" can be \'true\' or \'real\', and "vernyy" is \'loyal\' or \'faithful\'. Both have the masculine -iy, -yy to match "drug".'),
    (8, None, '\'Listen, maybe we should go somewhere?\' A "mozhet" is a casual \'or maybe\', used to suggest something. "Kuda-nibud" is \'somewhere\', and the -nibud means \'some place or other\'.'),
    (9, None, '\'Where exactly do you suggest going?\' "Kuda" is \'where to\', for movement. "Predlagaesh", \'you suggest\', leads straight into "poyti", \'to go\'.'),
    (10, None, '\'Let us go to the movies together.\' "Kino", \'cinema\', is borrowed and never changes its ending. "Davay skhodim" means \'let\'s go\', for a trip there and back.'),
    (11, None, '\'This is needed for the believability of our plan.\' "Pravdopodobnosti" joins "pravda", \'truth\', and "podobnyy", \'similar\', so literally \'truth-likeness\'. After "dlya", \'for\', it\'s in the genitive.'),
    (12, None, '\'Great idea, let us go tonight!\' "Segodnya vecherom" is \'today in the evening\', and the -om on "vecher" does the work of \'in\'. "Poydyom", \'let\'s go\', is a common way to say yes to a plan.'),
    (13, None, '\'Agreed, then let us meet after work.\' "Dogovorilis", \'agreed\', literally \'we\'ve talked it into an agreement\', closes the deal. After "posle", \'after\', "rabota" becomes "raboty".'),
]
