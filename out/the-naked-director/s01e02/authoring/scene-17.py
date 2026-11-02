ID = 'the-naked-director-s01e02-scene-17'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 17
TITLE = 'すずらん三十万部  (Suzuran Sells Three Hundred Thousand)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'customer': '客', 'tayama': '田山', 'ikezawa': '池沢'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "At Hokudai Kanda's bookstore counter, eager customers crowd around manager Tayama asking for the new edition titled Suzuran at fifteen thousand yen a copy. "
    "Meanwhile in his quiet garden, Poseidon boss Ikezawa hears that Suzuran has already sold three hundred thousand copies. "
    "Just soak in the shop-counter rhythm first."
)

STORY = [
    ('customer', '「すずらん」ください。', 'Suzuran, please.', [(433, 'すずらん ください')], ''),
    ('tayama', '一万五千円です。', 'That is fifteen thousand yen.', [(434, '円です')], 'Spelled 1万5,000円 in kanji as 一万五千円.'),
    ('tayama', 'ありがとうございました。', 'Thank you very much.', [(435, 'ありがとうございました')], ''),
    ('customer', '僕も「すずらん」。', 'Suzuran for me too.', [(436, '僕も すずらん')], ''),
    ('customer', '「すずらん」お願いします。', 'Suzuran, please.', [(437, 'すずらん お願いします')], ''),
    ('tayama', 'ありがとうございます。', 'Thank you very much.', [(439, 'ありがとうございます')], ''),
    ('ikezawa', '派手にいったもんだな。', 'He really went big with this.', [(443, '派手にいったもんだな')], ''),
    ('ikezawa', 'すでに三十万部ほど売り上げてるのか。', 'He has already sold around three hundred thousand copies, huh.', [(444, 'すでに'), (444, '万部ほど 売り上げてる')], 'Spelled 30万部 in kanji and adapted report ending to Ikezawa musing aloud within the three-role limit.'),
    ('ikezawa', '自由をはき違えたかな。', 'Maybe he misunderstood what freedom means.', [(446, '自由を はき違えたかな')], ''),
    ('ikezawa', '分かった、今行くから。', 'Got it, I am coming right now.', [(448, '分かった 今 行くから')], 'Trimmed trailing laugh.'),
    ('ikezawa', '思いどおりにはいかないもんだ。', 'Things never go the way you expect.', [(449, '思いどおりには いかないもんだ')], 'Trimmed opening filler.'),
]

OPENER = "You just heard a textbook Japanese shop transaction followed by Ikezawa's dry reflection. Let's look closer at each line."

WALK = [
    (0, None, "'Suzuran, please.' Naming an item and adding \"kudasai\" is the simplest way in Japanese to ask for something over a counter, whether a book, a ticket, or a cup of coffee."),
    (1, None, "'That is fifteen thousand yen.' Counting in units of \"man\"—ten thousand—makes fifteen thousand \"ichiman gosen\", one ten-thousand plus five thousand, followed by \"en\" for yen."),
    (2, None, "'Thank you very much.' Shop staff say \"arigatou gozaimashita\" with \"mashita\" at the end once a sale wraps up, thanking you for a transaction that is now complete."),
    (3, None, "'Suzuran for me too.' \"Boku\" is a warm, polite-casual word for 'I' used mostly by men and boys. Adding \"mo\", too or also, turns \"boku mo\" into an easy 'me too!'."),
    (4, None, "'Suzuran, please.' Alongside \"kudasai\", \"onegaishimasu\" is the other counter classic for ordering—slightly softer, literally entrusting your request to the clerk."),
    (5, None, "'Thank you very much.' Compare \"arigatou gozaimasu\" here with \"gozaimashita\" a moment ago: while cash is still changing hands, the clerk stays in the present form."),
    (6, None, "'He really went big with this.' \"Hade ni\" means flashily or on a grand scale, from \"hade\", flashy. Ending on \"itta mon da na\" voices rueful admiration at how far Muranishi pushed things."),
    (7, None, "'He has already sold around three hundred thousand copies, huh.' \"Sudeni\" means already, while \"sanjuuman-bu\" pairs thirty \"man\"—three hundred thousand—with \"bu\", the counter for printed copies, plus \"hodo\" for 'approximately'."),
    (9, None, "'Got it, I am coming right now.' \"Wakatta\" is casual 'got it' or 'understood', and \"ima iku kara\"—literally 'because I am going now'—is how Japanese speakers call back 'coming right now!' whereas English says 'I am coming'."),
    (10, None, "'Things never go the way you expect.' \"Omoidoori\" welds \"omoi\", thought or wish, to \"doori\", just as, while \"ikanai mon da\" sighs that life rarely goes according to plan."),
]

TRANSITION = "Now let's listen to the whole bookstore and garden scene again without pauses."

OUTRO = (
    "With \"kudasai\", \"onegaishimasu\", and \"boku mo\", you can already step up to any counter in Japan, "
    "and counting by \"man\" unlocks big yen prices right away. "
    "See you again."
)

CLOSING = ('tayama', 'また会いましょう。')
