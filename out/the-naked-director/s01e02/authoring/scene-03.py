ID = 'the-naked-director-s01e02-scene-03'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = '私の店にします  (Buying the Bookstore)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'muranishi': '村西', 'kitamori': '北森'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "Next, Muranishi walks into a quiet Sapporo bookstore run by Kitamori and tries to place his magazines on the shelves. "
    "When Kitamori refuses, Muranishi unzipping his leather bag turns a rejected pitch into an unexpected job offer. "
    "Listen to their exchange in Japanese first without worrying about every detail."
)

STORY = [
    ('muranishi', 'どうぞ。', 'Here you go.', [(38, 'どうぞ')], ''),
    ('muranishi', 'こちらのお店には置いてありませんね。', 'You do not carry these in your shop, do you?', [(41, 'こちらのお店には 置いてありませんね')], 'Trimmed opening phrase.'),
    ('kitamori', 'いや、別に興味はありません。', 'No, I am not particularly interested.', [(43, 'いや 別に興味は')], 'Completed unfinished sentence politely.'),
    ('muranishi', '隠さなくて結構ですよ。', 'There is no need to hide it.', [(44, '隠さなくて結構ですよ')], ''),
    ('kitamori', 'ちょっと待ってください！', 'Please wait a moment!', [(48, 'ちょっと待ってください')], ''),
    ('kitamori', 'うちではこういう本は置けません。', 'We cannot stock books like these in our shop.', [(49, 'うちでは こういう本は置けません')], 'Trimmed trailing particle.'),
    ('muranishi', 'そうですか。', 'Is that so?', [(50, 'そうですか')], ''),
    ('muranishi', 'では、私の店にするしかありませんね。', 'Then I have no choice but to make this my shop.', [(51, 'では 私の店にするしか ありませんね')], ''),
    ('muranishi', 'こちらを買い取らせていただきたいのですが。', 'I would like you to let me buy this place.', [(53, 'こちらを買い取らせて いただきたいのですが')], ''),
    ('kitamori', 'この店に、こんなに？', 'This much money, for this shop?', [(54, 'この店に… こんなに')], ''),
    ('muranishi', 'これは給料の前払いです。', 'This is an advance on your salary.', [(58, 'これは給料の前払いです')], ''),
    ('muranishi', 'どちらにしますか？', 'Which one do you choose?', [(61, 'どちらにしますか')], ''),
]

OPENER = "Both men speak with salesman-to-shopkeeper politeness even as Muranishi buys the store out from under Kitamori. Let's unpack how those polite turns work."

WALK = [
    (0, None, "'Here you go.' \"Douzo\" is your go-to word whenever you hand something over, motion someone through a door, or invite them to go ahead."),
    (1, None, "'You do not carry these in your shop, do you?' \"Kochira\" literally points 'this way', serving as a polite 'your' in \"kochira no omise\", your shop. \"Oite arimasen\" says nothing has been placed in stock."),
    (2, None, "'No, I am not particularly interested.' Pairing \"betsu ni\" with a negative ending softens a refusal into 'not really' or 'nothing special', while \"kyoumi\" means interest."),
    (3, None, "'There is no need to hide it.' Attach \"nakute kekkou desu\" to a negative stem like \"kakusa\", from \"kakusu\", to hide, to say 'you don't need to do that' politely."),
    (5, None, "'We cannot stock books like these in our shop.' \"Kou iu\" means 'this kind of' before \"hon\", books. Changing \"oku\", to place, into \"okemasen\" expresses 'cannot put on the shelves'."),
    (7, None, "'Then I have no choice but to make this my shop.' \"Shika\" paired with a negative like \"arimasen\" means 'nothing except', turning \"suru shika arimasen\" into 'have no choice but to do'."),
    (8, None, "'I would like you to let me buy this place.' \"Kaitoru\" means to buy out, and stretching it into \"kaitorasete itadakitai\" humbles the speaker to ask graceful permission—classic Japanese business polish."),
    (10, None, "'This is an advance on your salary.' \"Kyuuryou\" is a regular job's salary, and \"maebarai\" joins \"mae\", front or beforehand, with \"harai\", payment: paying up front."),
    (11, None, "'Which one do you choose?' When choosing between two paths, \"dochira ni shimasu ka\"—literally 'which way will you make it?'—works at a restaurant table and in life-changing deals alike."),
]

TRANSITION = "Now let's listen to the whole bookstore scene again."

OUTRO = (
    "From ordering lunch to closing a deal, \"dochira ni shimasu ka\" is a clean, polite way to ask someone which option they choose. "
    "See you next time."
)

CLOSING = ('kitamori', 'また会いましょう。')
