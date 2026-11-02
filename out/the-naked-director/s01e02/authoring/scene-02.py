ID = 'the-naked-director-s01e02-scene-02'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = '全種類ください  (Ordering Every Kind)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'toshi': 'トシ', 'chu': 'チュウ', 'muranishi': '村西'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "With cash in hand, Muranishi and Toshi sit down at a Sapporo coffee shop to meet a magazine broker named Chu. "
    "After hearing about the biggest publisher in Japan, Muranishi surprises everyone at the table with the size of his order. "
    "Listen to the conversation in Japanese first, and don't worry about catching every word."
)

STORY = [
    ('chu', 'ああ、トシさん、どうも。', 'Oh, Toshi, hello there.', [(20, 'ああ トシさん どうも')], ''),
    ('toshi', 'カバン屋のチュウさんだ。', 'This is Chu, the bag dealer.', [(21, 'カバン屋のチュウさんだ')], ''),
    ('muranishi', 'どうも、村西です。', 'Hello, I am Muranishi.', [(24, 'どうも 村西です')], ''),
    ('chu', 'はい。どれでもあるよ。', 'Right. I have whatever you want.', [(25, 'はい'), (28, 'どれでもあるよ')], 'Combined brief greeting and stock line.'),
    ('chu', 'あとはポセイドンさんのシリーズだね。', 'And then there is the series from Poseidon.', [(30, 'ポセイドンさんの')], 'Simplified title reference.'),
    ('muranishi', 'ポセイドン？', 'Poseidon?', [(31, 'ポセイドン')], ''),
    ('chu', '業界じゃ最大手だよ。', 'They are the biggest player in the industry.', [(32, '最大手だよ')], 'Trimmed prefix for clean A1 vocabulary.'),
    ('muranishi', 'じゃあ、いただこうか。', 'Well then, I will take them.', [(33, 'じゃあ いただこうか')], ''),
    ('chu', 'どれがご入り用だい？', 'Which ones do you need?', [(34, 'ご入り用だい')], 'Shortened double question to one clean question.'),
    ('muranishi', '全種類です。', 'Every kind.', [(35, '全種類')], 'Added polite です.'),
    ('toshi', 'そんなたくさんいらないだろ？', 'You do not need that many, do you?', [(36, 'そんなたくさん')], 'Standardized colloquial negative.'),
    ('toshi', 'まさか、店でも構えるつもりか？', 'Wait, are you planning to open a shop or something?', [(37, 'まさか 店でも構えるつもりか')], ''),
]

OPENER = "Watch how Muranishi stays calm and polite even while making a bold move that catches Toshi off guard. Let's go through it line by line."

WALK = [
    (1, None, "'This is Chu, the bag dealer.' Adding \"ya\", shop or dealer, onto \"kaban\", bag, creates \"kabanya\"—just like \"honya\" for a bookstore or \"panya\" for a bakery."),
    (2, None, "'Hello, I am Muranishi.' Introducing yourself in Japanese can be as short as \"doumo\" plus your surname and \"desu\", with no need to say 'my name is'."),
    (3, 'どれでもあるよ。', "'I have whatever you want.' \"Dore\" asks 'which one' among three or more things, and adding \"demo\" turns it into 'whichever one' or 'any of them'."),
    (6, None, "'They are the biggest player in the industry.' \"Gyoukai\" means an industry or business world, and \"ja\" contracts \"de wa\", 'in'. \"Saidai\" means biggest, paired with \"te\", hand or major firm."),
    (7, None, "'Well then, I will take them.' \"Itadakou\" is the casual 'let's' or 'I think I will' form of humble \"itadaku\", to receive—what buyers warmly say when deciding on an item."),
    (8, None, "'Which ones do you need?' Chu dresses up \"iriyou\", need, with respectful \"go\" for his customer, then softens the question with old-school merchant \"dai\"."),
    (9, None, "'Every kind.' Putting \"zen\", all or whole, in front of \"shurui\", type or variety, packs 'every single kind' into one crisp compound."),
    (10, None, "'You do not need that many, do you?' \"Takusan\" means a lot, and \"iranai\" is the plain negative of \"iru\", to need—not to be confused with \"iru\", to be."),
    (11, None, "'Wait, are you planning to open a shop or something?' Opening with \"masaka\" expresses disbelief, like 'no way' or 'surely not', while \"tsumori\" names an intention or plan."),
]

TRANSITION = "Now let's listen to the whole coffee shop meeting again."

OUTRO = (
    "Keep an ear out for shop words built with \"ya\", and for \"tsumori\" whenever someone talks about what they plan to do. "
    "See you in the next scene."
)

CLOSING = ('toshi', 'じゃあね！')
