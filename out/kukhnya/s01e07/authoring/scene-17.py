# Authoring module for kukhnya-s01e07-scene-17.
ID = 'kukhnya-s01e07-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 17
TITLE = 'В гостях у Кости  (Visiting Kostya)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = 'Kostya, the bartender, has talked Nastya the waitress into coming to see his rented flat, and he has made an effort to tidy up. Then she spots something on the floor, and the mood changes. Listen to the visit in Russian.'
OPENER = "Slowly now. Kostya is proud of his home, and Nastya sees something he hasn't noticed."
TRANSITION = 'Now the visit at full speed, from the top.'
OUTRO = "Nastya's list of insults is long and worth hearing again: murderer, monster, cruel. Kostya's reply is simply that it's an ordinary trap. See you next time."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('kostya', 'Настя, добро пожаловать в мою квартиру.', 'Nastya, welcome to my apartment.', [], ''),
    ('nastya', 'У тебя здесь довольно уютно и чисто.', 'It is quite cozy and clean here with you.', [], ''),
    ('kostya', 'Ну, точнее, эта квартира съёмная.', 'Well, more precisely, this apartment is rented.', [(333, 'не моя съемная')], ''),
    ('kostya', 'Вот диван, стул, мягкая подушка.', 'Here is a couch, a chair, a soft pillow.', [(334, 'Диван, стул'), (335, 'Подушка')], ''),
    ('nastya', 'Костя, я всё это отлично вижу.', 'Kostya, I can see all this perfectly.', [(335, 'Кость, я вижу')], ''),
    ('kostya', 'Проходи скорее и садись на диван.', 'Come in quickly and sit on the couch.', [(336, 'Проходи, проходи. Садись')], ''),
    ('nastya', 'Ой, а что это там внизу?', 'Oh, and what is that down there?', [(337, 'Что это?')], ''),
    ('nastya', 'Боже мой, это же мёртвая мышь!', 'My God, that is a dead mouse!', [(338, 'Это…')], ''),
    ('nastya', 'Костя, ты самый настоящий жестокий убийца!', 'Kostya, you are a real cruel murderer!', [(338, 'Ты убийца')], ''),
    ('nastya', 'Ты погубил маленькую беззащитную мышь!', 'You destroyed a little defenseless mouse!', [(339, 'Убил маленькую ни в чем не повинную мышь')], ''),
    ('kostya', 'Настя, но это обычная мышеловка!', 'Nastya, but this is an ordinary mousetrap!', [], ''),
    ('nastya', 'Ты ещё сидишь и спокойно улыбаешься?!', 'You are still sitting and calmly smiling?!', [(340, 'Еще лыбится сидит')], ''),
    ('nastya', 'Ты поступил как настоящий монстр!', 'You acted like a real monster!', [(342, 'Ты вообще монстр')], ''),
]
WALK = [
    (0, None, '\'Nastya, welcome to my apartment.\' "Dobro pozhalovat\'", \'welcome\', is a set phrase, close to \'kindly come in\'. After it, v takes the object form: v moyu kvartiru.'),
    (1, None, '\'It is quite cozy and clean here with you.\' U tebya, \'at you\', means \'at your place\'. "Uyutno", \'cozy\', comes from uyut, comfort and homeliness.'),
    (2, None, '\'Well, more precisely, this apartment is rented.\' "Tochneye", \'more precisely\', is the comparative of tochno, a neat way to correct yourself. "S\'yomnaya", \'rented\', comes from snyat\', the verb Max used when he asked Nastya where to rent.'),
    (3, None, '\'Here is a couch, a chair, a soft pillow.\' After vot, \'here is\', a list of nouns needs no verb. "Myagkaya", \'soft\', ends in -aya because podushka is feminine.'),
    (4, None, '\'Kostya, I can see all this perfectly.\' "Vizhu", \'I see\', swaps the d of videt\' for zh. Russian needs no \'can\' here: ya vizhu is just \'I see\'.'),
    (5, None, '\'Come in quickly and sit on the couch.\' "Prokhodi", literally \'go through\', is what a host says at the door. "Sadis\'" na divan uses the object form after na, because she is moving onto it.'),
    (6, None, '\'Oh, and what is that down there?\' The little a softens the question, like \'and so\'. "Vnizu" means \'down below\', with no movement.'),
    (7, None, '\'My "God", that is a dead mouse!\' "Bozhe moy", \'my "God\'", uses an old calling form of "Bog", "God". "Mysh\'", mouse, is feminine, so \'dead\' is myortvaya.'),
    (8, None, '\'Kostya, you are a real cruel murderer!\' "Samyy nastoyashchiy", \'the most real\', works like \'an out-and-out\'. "Ubiytsa", \'murderer\', comes from ubit\', to kill, and ends in -a even for a man.'),
    (9, None, '\'You destroyed a little defenseless mouse!\' "Bezzashchitnaya", \'defenceless\', is bez, \'without\', plus zashchita, protection; as the object it becomes bezzashchitnuyu. "Pogubil" is a heavy word for ruining a life.'),
    (10, None, '\'Nastya, but this is an ordinary mousetrap!\' "Myshelovka" joins mysh\', mouse, and lovit\', to catch. "Obychnaya", \'ordinary\', comes from obychay, a custom.'),
    (11, None, '\'You are still sitting and calmly smiling?!\' "Yeshchyo" here is indignant, like \'on top of everything\'. "Ulybaesh\'sya" is the ty form; in the kitchen, Max used the polite ulybaetes\' with the chef.'),
    (12, None, '\'You acted like a real monster!\' "Postupil", \'acted\', describes how someone behaves, good or bad. "Kak", \'like\', brings in the comparison, and monstr is the English \'monster\'.'),
]
