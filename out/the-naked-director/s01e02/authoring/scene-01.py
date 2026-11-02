ID = 'the-naked-director-s01e02-scene-01'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = '五十万の融通  (Five Hundred Thousand Yen)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'tencho': '店長', 'muranishi': '村西', 'toshi': 'トシ'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "In episode two of The Naked Director, Toru Muranishi and Toshi scramble to raise startup cash in Sapporo. "
    "Inside a small loan office, Muranishi puts up the deed to his house and stamps his personal seal before stepping outside to compare totals with Toshi. "
    "Let's hear the Japanese dialogue first without worrying about catching every word."
)

STORY = [
    ('muranishi', 'はい、自宅の権利書です。', 'Here is the deed to my house.', [(2, 'はい 自宅の権利書')], 'Added polite copula です.'),
    ('tencho', 'うちで五十万融通しますよ。', 'Our shop can lend you five hundred thousand yen.', [(5, 'うちで50万 融通しますよ')], 'Written in kanji without spaces.'),
    ('muranishi', 'どうも。', 'Thanks.', [(6, 'どうも')], ''),
    ('tencho', '利子は十日で一割です。', 'Interest is ten percent every ten days.', [(7, '利子は10日で１割')], 'Trimmed trailing clause and added です.'),
    ('tencho', 'いろいろ契約のことが書いてあります。', 'Various contract details are written here.', [(8, 'いろいろ契約のこと')], 'Polite ending あります.'),
    ('muranishi', '構いません。はい、実印です。', 'I do not mind. Here is my registered seal.', [(9, '構いません　はい 実印')], 'Added です.'),
    ('tencho', 'じゃ、押させてもらいますよ。', 'Well then, let me stamp it.', [(11, 'じゃ 押させてもらいますよ')], ''),
    ('muranishi', 'よろしくお願いします。', 'Thank you for taking care of this.', [(12, 'よろしくお願いします')], ''),
    ('toshi', 'おい、どうだった？', 'Hey, how did it go?', [(13, 'おい どうだった')], ''),
    ('muranishi', '五十万だ。', 'Five hundred thousand.', [(14, '50万')], 'Written in kanji with plain だ.'),
    ('toshi', '俺は全部で百万だな。', 'I got one million in total.', [(15, '俺は全部で')], 'Shortened middle verb for A1 clarity.'),
    ('toshi', 'もういいんじゃないか？', 'Is that not enough now?', [(16, 'もういいんじゃ')], 'Standardized colloquial contraction.'),
]

OPENER = "Muranishi stays brisk and polite inside the loan office, then switches to plain talk outside with Toshi. Let's walk through the key lines."

WALK = [
    (0, None, "'Here is the deed to my house.' \"Jitaku\" means one's own home, a slightly more formal cousin of \"ie\", house. Linking it with \"no\" to \"kenrisho\", title deed, names the document without needing a separate word for 'my'."),
    (1, None, "'Our shop can lend you five hundred thousand yen.' \"Uchi\" literally means home or inside, and businesspeople use it warmly for 'our shop' or 'our company'. \"Gojuuman\" counts fifty units of \"man\", ten thousand."),
    (2, None, "'Thanks.' A quick \"doumo\" works like an all-purpose nod that can mean thanks, hello, or excuse me depending on the moment."),
    (3, None, "'Interest is ten percent every ten days.' \"Tooka\" is the special ten-day counter, while \"ichiwari\" means one tenth—ten percent—using Japanese's everyday \"wari\" system for tenths."),
    (5, '構いません。', "'I do not mind.' \"Kamaimasen\" is the polite negative of \"kamau\", to care or mind, handy whenever you want to say 'that's fine with me'."),
    (5, 'はい、実印です。', "'Here is my registered seal.' In Japan, major contracts are stamped with a \"jitsuin\", a personal seal officially registered at city hall rather than signed by pen."),
    (7, None, "'Thank you for taking care of this.' \"Yoroshiku onegai shimasu\" seals a deal or favor ahead of time, asking the other person to treat the matter kindly."),
    (8, None, "'Hey, how did it go?' \"Dou datta\" pairs \"dou\", how, with plain past \"datta\", was—the natural casual way to ask a friend how something went."),
    (10, None, "'I got one million in total.' Toshi calls himself \"ore\", a rough masculine 'I', and sums things up with \"zenbu de\", in all. \"Hyakuman\" is one hundred ten-thousands: one million."),
    (11, None, "'Is that not enough now?' \"Mou ii\" alone can mean 'already good' or 'enough already', and softened with \"n ja nai ka\" it nudges Muranishi to agree."),
]

TRANSITION = "Now let's hear the whole scene again from start to finish."

OUTRO = (
    "Notice how Japanese counts big sums in units of \"man\", ten thousand, so fifty ten-thousands gives five hundred thousand and a hundred ten-thousands makes a million. "
    "Until next time, take care."
)

CLOSING = ('muranishi', 'じゃあね。')
