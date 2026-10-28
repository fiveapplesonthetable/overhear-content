# Authoring module for kukhnya-s01e05-scene-02.
ID = 'kukhnya-s01e05-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 2
TITLE = 'Мечты о будущем  (Dreams of the Future)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Meanwhile, in the staff locker room at Claude Monet, the waitress Nastya is floating. She thinks yesterday's kiss with Max was the start of a love story, which is not what Max just told Kostya. Her friend Sasha, another waitress, is trying to keep up. Here it is in Russian."
OPENER = 'Now slowly. Nastya races ahead, and Sasha keeps asking questions to pull her back.'
TRANSITION = 'And now the chat in one piece.'
OUTRO = 'Sasha\'s little questions are worth stealing: "pravda", "neuzheli", a "ty uzhe". They keep any conversation going. Max, of course, has no idea about the children.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('sasha', 'Настя, у вас с Максом всё серьёзно?', 'Nastya, is everything serious between you and Max?', [], ''),
    ('nastya', 'Да, мы вчера даже поцеловались.', 'Yes, yesterday we even kissed.', [], ''),
    ('sasha', 'Правда? И как это произошло?', 'Really? And how did that happen?', [], ''),
    ('nastya', 'Это было невероятно романтично!', 'It was incredibly romantic!', [], ''),
    ('sasha', 'Неужели ты влюбилась в него?', 'Did you really fall in love with him?', [], ''),
    ('nastya', 'Он такой добрый и внимательный парень.', 'He is such a kind and attentive guy.', [], ''),
    ('sasha', 'Вы ведь знакомы всего одну неделю.', 'After all, you have only known each other one week.', [], ''),
    ('nastya', 'Настоящая любовь не знает времени.', 'True love knows no time.', [], ''),
    ('nastya', 'Представляешь, какие у нас будут красивые дети!', 'Imagine what beautiful children we will have!', [(22, 'Представляешь, какие у нас дети красивые будут')], ''),
    ('sasha', 'Ты уже думаешь о детях?!', 'Are you already thinking about children?!', [], ''),
    ('nastya', 'Конечно, мы создадим прекрасную семью.', 'Of course, we will create a wonderful family.', [], ''),
    ('sasha', 'А Макс знает о твоих планах?', 'And does Max know about your plans?', [], ''),
    ('nastya', 'Скоро мы обязательно всё обсудим.', 'Soon we will definitely discuss everything.', [], ''),
]
WALK = [
    (0, None, '\'Nastya, is everything serious between you and Max?\' Russian says \'at you with Max everything serious\', with no \'is\' at all. "U vas" is plural here, because Sasha means the two of them.'),
    (1, None, '\'Yes, yesterday we even kissed.\' The same kissing verb, but now it\'s "potselovalis", with "po-" in front. That makes it one kiss, done and finished, where Kostya\'s "tselovalis" sounded more like an ongoing activity.'),
    (2, None, '\'Really? And how did that happen?\' "Pravda" literally means \'truth\', and said with a rising voice it\'s \'really?\'. "Proizoshlo" ends in -o to agree with "eto", \'it\'.'),
    (3, None, '\'It was incredibly romantic!\' "Neveroyatno" is "ne", \'not\', in front of "veroyatno", \'probably\', so: improbably, unbelievably. "Romantichno" you can guess.'),
    (4, None, '\'Did you really fall in love with him?\' "Neuzheli" is a surprised \'can it really be?\'. In Russian you fall in love \'into\' someone: "vlyubilas v nego", and the -las tells you it\'s a woman who fell.'),
    (5, None, '\'He is such a kind and attentive guy.\' "Takoy" before a description means \'such a\'. "Dobryy" and "vnimatelnyy" both end in -yy, the usual ending when the adjective describes a man, here "paren", \'guy\'.'),
    (6, None, '\'After all, you have only known each other one week.\' "Ved", tucked in the middle, is \'after all\', a gentle \'come on\'. "Nedelya", \'week\', becomes "odnu nedelyu" when it says how long.'),
    (7, None, '\'True love knows no time.\' It sounds like a song lyric, and Nastya means it. After "ne znaet", \'doesn\'t know\', the word for \'time\' shifts from "vremya" to "vremeni".'),
    (8, None, '\'Imagine what beautiful children we will have!\' "Predstavlyaesh" is literally \'do you imagine?\', used like \'just imagine!\'. \'We will have\' is "u nas budut", \'at us will be\'.'),
    (9, None, '\'Are you already thinking about children?!\' "Uzhe", \'already\', carries all of Sasha\'s shock. After "o", \'about\', "deti", \'children\', turns into "detyakh".'),
    (10, None, '\'Of course, we will create a wonderful family.\' "Konechno" is spelled with a ch but said \'koneshno\'. "Semya", \'family\', becomes "semyu" because it\'s the thing they\'ll create.'),
    (11, None, '\'And does Max know about your plans?\' The one question Nastya has dodged. After "o", both words take plural endings: "o tvoikh planakh".'),
    (12, None, '\'Soon we will definitely discuss everything.\' "Obsudim" is \'we will discuss\', with the same -im as "sozdadim" in her last line. "Obyazatelno", \'definitely\', is a word Russians say all the time to promise something.'),
]
