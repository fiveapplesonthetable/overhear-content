ID = 'the-naked-director-s01e02-scene-20'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 20
TITLE = '検問所の絵本  (Picture Books at the Checkpoint)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kawada': '川田', 'toshi': 'トシ', 'police': '警察官'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "Out on the dark highway in Hokkaido, Toshi and Kawada roll right up to a nighttime police checkpoint. "
    "Toshi panics when an officer asks to inspect the cargo bed, but calm Kawada has prepared a clever surprise inside children's picture books. "
    "Listen to the polite checkpoint questions first."
)

STORY = [
    ('kawada', '検問ですよね、あれ。', 'That is a checkpoint, right?', [(524, '検問ですよね')], ''),
    ('toshi', 'まずいだろ、これ。どうするんだよ？', 'This is bad. What are we going to do?', [(526, 'まずいだろ')], 'Standardized どうすんだよ to どうするんだよ.'),
    ('police', 'こんばんは。エンジン止めてください。', 'Good evening. Please stop the engine.', [(530, 'こんばんは'), (530, 'エンジン止めてくださ')], 'Normalized elongated vowel ー.'),
    ('police', 'お酒、飲んでないですね？', 'You have not been drinking alcohol, right?', [(531, '飲んでないですね')], ''),
    ('police', '荷台を調べるんで、開けてもらえますか？', 'We are checking the cargo bed, so could you open it?', [(536, '開けてもらえますか')], ''),
    ('kawada', 'もっとちゃんと見てください、お巡りさん。', 'Please look more closely, officer.', [(549, '見てください')], ''),
    ('kawada', 'これ、絵本ですよね？', 'These are picture books, right?', [(554, '絵本ですよね')], ''),
    ('police', '確かに絵本だな。', 'They certainly are picture books.', [(555, '確かに絵本だな')], ''),
    ('police', 'なかなかかわいい絵本ですね。', 'They are pretty cute picture books.', [(558, 'かわいい絵本ですね')], ''),
    ('police', '異常なし。行っていいぞ。', 'Nothing unusual. You may go.', [(560, '異常なし'), (560, '行っていいぞ')], ''),
    ('kawada', 'それじゃ、行きましょうか。', 'Well then, shall we get going?', [(561, '行きましょうか')], ''),
    ('kawada', '万が一のために積んでおきました。', 'I loaded them aboard just in case.', [(564, '万が一のために積んでおきました')], ''),
]

OPENER = "Watch how the officer shifts from crisp traffic-stop politeness to a gruff wave-through, while Kawada never loses his cool. Let's hear the key lines."

WALK = [
    (0, None, "'That is a checkpoint, right?' Kawada names \"kenmon\", a roadside inspection point, and checks with \"desu yo ne\", 'is it not?'. Tacking \"are\", that over there, onto the very end mirrors natural spoken order when spotting something ahead."),
    (1, 'まずいだろ、これ。', "'This is bad.' On a dinner plate \"mazui\" means bad-tasting, but in a jam it means 'uh-oh, trouble'. \"Daro\" asks roughly for agreement—'this looks bad, right?'."),
    (2, None, "'Good evening. Please stop the engine.' After evening greeting \"konbanwa\", the officer pairs borrowed \"enjin\" with \"tomete kudasai\", please stop it. \"Tomeru\" handles stopping vehicles, machines, or water."),
    (3, None, "'You have not been drinking alcohol, right?' \"Osake\" covers all alcoholic drinks, dressed up with polite prefix \"o\". \"Nonde nai desu ne\" checks negatively—'not drinking, right?'—the standard traffic-stop question in Japan."),
    (4, None, "'We are checking the cargo bed, so could you open it?' \"Nidai\" is a truck's cargo bed, and \"shiraberu\" means inspect or check. Ending with \"akete moraemasu ka\", literally 'could we receive your opening it?', softens an order into a polite request."),
    (5, None, "'Please look more closely, officer.' \"Motto chanto\" combines \"motto\", more, with \"chanto\", properly or carefully. Friendly \"omawarisan\"—built from \"mawaru\", to patrol—is how everyday citizens address a beat officer."),
    (6, None, "'These are picture books, right?' Combining \"e\", picture, with \"hon\", book, gives \"ehon\", an illustrated children's book. Kawada repeats \"desu yo ne\" with calm confidence to nudge the officer's answer."),
    (7, None, "'They certainly are picture books.' Once the officer spots the cash tucked inside, \"tashika ni\" signals 'sure enough' or 'certainly'. Plain \"da na\" sounds like a man nodding to himself."),
    (9, None, "'Nothing unusual. You may go.' \"Ijou nashi\"—literally 'abnormality: none'—is classic crisp patrol shorthand for 'all clear'. Then \"itte ii zo\" pairs \"itte ii\", okay to go, with authoritative \"zo\"."),
    (10, None, "'Well then, shall we get going?' \"Ikimashou\" means 'let us go', built on \"iku\", go. Adding rising \"ka\" at the end turns 'let's go' into a considerate 'shall we get going?'."),
    (11, None, "'I loaded them aboard just in case.' \"Man ga ichi\" literally says 'one in ten thousand'—the idiomatic chunk for 'just in case'. Attaching \"okimashita\" to \"tsunde\", loading up, shows he did it ahead of time to prepare."),
]

TRANSITION = "Now let's hear the whole nighttime checkpoint exchange again from beginning to end."

OUTRO = (
    "From \"konbanwa\" and \"akete moraemasu ka\" to \"man ga ichi\", "
    "you heard how polite requests and advance preparation work in everyday Japanese. "
    "Until next time—goodbye."
)

CLOSING = ('kawada', 'さようなら。')
