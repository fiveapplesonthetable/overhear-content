# Authoring module for kukhnya-s01e05-scene-01.
ID = 'kukhnya-s01e05-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Ссора из-за поцелуя  (A Quarrel Over a Kiss)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "This is Kukhnya, which means The Kitchen: a Russian comedy set in a smart Moscow restaurant called Claude Monet, where the chef shouts and everyone else tries to get through the shift. In this story, from episode five, the bartender Kostya has just heard that his best friend Max kissed Nastya, the waitress he likes. Max has to talk his way out of it. Listen to it in Russian first, and don't worry about catching every word."
OPENER = "Let's go back through it line by line. Kostya is too angry for long sentences, which makes him easy to follow."
TRANSITION = "Here's the whole quarrel again, without stopping."
OUTRO = 'Keep two lines from this one: "za chto", for when you\'re blamed and don\'t know why, and "ne imeet znacheniya", for waving something away. Kostya\'s last word is "poka", and you\'ll hear it once more as a goodbye.'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('max', 'Костя, привет. Почему ты сердишься?', 'Kostya, hi. Why are you angry?', [], ''),
    ('kostya', 'Отвали, или я сломаю тебе нос!', 'Back off, or I will break your nose!', [(6, 'Отвали, или я тебе нос сломаю')], ''),
    ('max', 'За что? Что я тебе сделал?', 'What for? What did I do to you?', [(7, 'За что')], ''),
    ('kostya', 'Ты вчера целовался с моей девушкой!', 'Yesterday you kissed my girl!', [(7, 'ты целовался с моей девушкой')], ''),
    ('max', 'Это было совершенно случайное недоразумение.', 'It was a completely accidental misunderstanding.', [(11, 'это вообще недоразумение было')], ''),
    ('kostya', 'Вы целовались прямо в ресторане!', 'You were kissing right in the restaurant!', [], ''),
    ('max', 'Я вчера весь день хотел спать.', 'I wanted to sleep all day yesterday.', [(12, 'Я вчера весь день'), (12, 'спать хотел')], ''),
    ('max', 'Кстати, технически она пока не твоя.', 'By the way, technically she is not yours yet.', [(13, 'Кстати, технически она пока не твоя')], ''),
    ('kostya', 'Для меня это не имеет значения.', 'For me that does not matter.', [], ''),
    ('max', 'Между мной и Настей ничего нет!', 'There is nothing between me and Nastya!', [(15, 'между нами ничего нет')], ''),
    ('kostya', 'Ты предал нашу дружбу, Макс.', 'You betrayed our friendship, Max.', [], ''),
    ('max', 'Я докажу, что она мне безразлична.', 'I will prove that she means nothing to me.', [], ''),
    ('kostya', 'Посмотрим, как ты это докажешь.', 'We will see how you prove it.', [], ''),
]
WALK = [
    (0, None, '\'Kostya, hi. Why are you angry?\' "Pochemu" is the everyday \'why\'. "Serdishsya" is the \'you\' form of the verb "serditsya", \'to be angry\', and the -sya on the end belongs to the verb, so it stays on in every form.'),
    (1, None, '\'Back off, or I will break your nose!\' "Otvali" is a rude \'get lost\', not something to say to your boss. Then Russian says \'I will break to-you the nose\': "tebe", \'to you\', does the work of \'your\'.'),
    (2, None, '\'What for? What did I do to you?\' "Za chto", two short words, is what you say when you\'re blamed and can\'t see why. The second question has the same "tebe" in the middle: "chto ya tebe sdelal".'),
    (3, None, '\'Yesterday you kissed my girl!\' In Russian you kiss \'with\' someone: "tselovalsya s moey devushkoy", and after "s" the words take the endings -oy. "Devushka" covers both \'young woman\' and \'girlfriend\'.'),
    (4, None, '\'It was a completely accidental misunderstanding.\' Max goes for long, official-sounding words. "Sluchaynoe" comes from "sluchay", \'a chance\' or \'an occasion\', and "nedorazumenie" is the standard word for a misunderstanding.'),
    (5, None, '\'You were kissing right in the restaurant!\' Now the \'you\' is "vy", Max and Nastya together, and the verb turns plural: "tselovalis". "Pryamo" means \'right\' or \'straight\', and "v restorane" takes -e because it says where.'),
    (6, None, '\'I wanted to sleep all day yesterday.\' "Ves den", \'the whole day\', needs no little word in front, just as in English. "Khotel" is the man\'s form of \'wanted\'; Nastya would say "khotela".'),
    (7, None, '\'By the way, technically she is not yours yet.\' "Kstati" is \'by the way\', perfect for slipping in an awkward point. "Poka" here means \'yet\' or \'for now\', and the same word is also an everyday \'bye\'.'),
    (8, None, '\'For me that does not matter.\' Word for word: \'for me this not has meaning\'. "Dlya menya" means \'for me\', and "ne imeet znacheniya" is a ready-made way to say something doesn\'t matter.'),
    (9, None, '\'There is nothing between me and Nastya!\' After "mezhdu", \'between\', both names take instrumental endings: "mezhdu mnoy i Nastey". "Nichego net" uses two negatives, and in Russian that\'s correct.'),
    (10, None, '\'You betrayed our friendship, Max.\' "Druzhba", \'friendship\', is built on "drug", \'friend\'. Here it\'s "druzhbu", with -u, because it\'s the thing being betrayed.'),
    (11, None, '\'I will prove that she means nothing to me.\' "Dokazhu" is \'I will prove\'. Then she is "bezrazlichna mne", \'indifferent to me\', with "bez", \'without\', stuck on the front.'),
    (12, None, '\'We will see how you prove it.\' "Posmotrim", \'we\'ll see\', is what you say when you don\'t believe a word. Max\'s "dokazhu" comes back as "dokazhesh", the form for \'you\'.'),
]
