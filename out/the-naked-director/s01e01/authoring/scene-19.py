ID = 'the-naked-director-s01e01-scene-19'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 19
TITLE = '金庫が空っぽだ  (The Safe Is Empty)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'police': '警察官', 'muranishi': '村西', 'kacho': '課長'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Just one morning after celebrating his number-one trophy, Muranishi arrives at Bianca International to find police officers outside the building. "
    "Inside, his section chief points to the open metal safe: Ono has vanished with every yen of the company's money. "
    "Listen to everything come crashing down."
)

STORY = [
    ('police', '英語の百科事典の会社だってさ。', 'They say it is an English encyclopedia company.', [(461, '英語の百科事典の会社だってさ')], ''),
    ('police', '最近はやってるみたいだな。', 'Looks like that business is popular lately.', [(462, '最近はやってるみたいだな')], ''),
    ('police', 'ああ、そうみたいだな。', 'Yeah, sure seems that way.', [(463, 'ああ')], 'Expanded short nod for natural A1 exchange.'),
    ('muranishi', '課長、何かあったんですか？', 'Chief, did something happen?', [(465, '何かあったんですか')], 'Added 課長 vocative.'),
    ('kacho', '大ありだよ。', 'Something huge happened.', [(466, '大ありだよ')], ''),
    ('kacho', '会社の売上金が全部金庫から消えたんだよ。', 'All the company sales money disappeared from the safe.', [(467, '会社の売上金が全部 金庫から消え')], 'Standardised 消えちまった to 消えた.'),
    ('muranishi', 'えっ、全部ですか？', 'What, all of it?', [(468, 'えっ')], 'Added 全部ですか for beginner comprehension.'),
    ('kacho', 'ほら、空っぽだよ。', 'Look, it is completely empty.', [(469, 'ほら 空っぽだよ')], ''),
    ('muranishi', '小野さんはどこですか？', 'Where is Ono-san?', [], 'Bridging question connecting the empty safe to Ono’s disappearance.'),
    ('kacho', 'どこにもいないよ。会社は終わりだ。', 'He is nowhere to be found. The company is finished.', [], 'Bridging answer explaining why Bianca International collapses.'),
    ('muranishi', 'そんな、信じられません。', 'No way, I cannot believe it.', [], 'Echoes 信じられない in polite office speech.'),
    ('muranishi', '今日はもう帰ります。', 'I am going home early today.', [], 'Bridges to Muranishi walking out in shock toward home.'),
]

OPENER = "In twelve short lines, Muranishi goes from top salesman to unemployed. Let's look closely at the words that tell the story."

WALK = [
    (0, None, "'They say it is an English encyclopedia company.' Native Japanese calls an encyclopedia \"hyakka jiten\", literally a 'hundred-subjects word-book'. Ending with \"datte sa\" passes along gossip—'so I hear'."),
    (1, None, "'Looks like that business is popular lately.' \"Hayatteru\" comes from \"hayaru\", to be trendy or booming, and \"mitai\" adds 'it seems like'."),
    (3, None, "'Chief, did something happen?' Walk into any noisy crowd or office commotion and ask \"nanika atta n desu ka\", built from \"nanika\", something, plus \"atta\", happened."),
    (4, None, "'Something huge happened.' When someone asks if anything is wrong, \"ooari\", literally 'big-exists!', answers 'you bet there is—big time!'"),
    (5, None, "'All the company sales money disappeared from the safe.' \"Kaisha\" is company, \"zenbu\" means all of it, \"kinko\" is a locked safe, and \"kieta\" comes from \"kieru\", to vanish."),
    (7, None, "'Look, it is completely empty.' \"Karappo\" has a lively, hollow bounce to its sound and means completely empty—empty safe, empty box, or empty stomach."),
    (8, None, "'Where is Ono-san?' Put anyone's name before \"doko\", where, and polite \"desu ka\" to ask where they are."),
    (9, 'どこにもいないよ。', "'He is nowhere to be found.' Pairing \"doko ni mo\" with negative \"inai\" sweeps every place clean: 'not anywhere at all'."),
    (9, '会社は終わりだ。', "'The company is finished.' \"Owari\" turns \"owaru\", to end, into 'the end'—heard at closing time and when a venture goes under."),
    (11, None, "'I am going home early today.' \"Kaerimasu\" is the polite everyday word for heading home—leading straight into Muranishi's early return to his house."),
]

TRANSITION = "Now let's listen to the office safe scene again."

OUTRO = (
    "Hold on to \"nanika atta n desu ka\" to ask if something happened, \"zenbu\" for 'all of it', "
    "and \"karappo\" when something is completely empty. "
    "See you in the next scene."
)

CLOSING = ('muranishi', 'さようなら。')
