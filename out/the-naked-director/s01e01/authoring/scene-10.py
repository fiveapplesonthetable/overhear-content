ID = 'the-naked-director-s01e01-scene-10'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 10
TITLE = '英語はお好きですか  (Do You Like English?)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'muranishi': '村西', 'resident': '主婦', 'ono': '小野'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Finally out in a residential neighborhood, Muranishi rings doorbells to sell English encyclopedias. "
    "With a stiff, nervous grin, he gets doors shut in his face one after another while Ono watches from across the street. "
    "Listen to how customers turn him down."
)

STORY = [
    ('muranishi', 'こんにちは。', 'Hello.', [(167, 'こんにちは')], ''),
    ('muranishi', '英語はお好きですか？', 'Do you like English?', [(168, '英語は お好きですか')], ''),
    ('resident', '結構です。', 'No, thank you.', [(169, '結構です')], ''),
    ('resident', '何？', 'What is it?', [(172, '何')], ''),
    ('muranishi', 'こんにちは。英語はお好きですか？', 'Hello. Do you like English?', [(178, 'こんにちは 英語は お好きですか')], ''),
    ('muranishi', 'これからの時代、英語が必要になってきます。', 'In the coming era, English is going to become necessary.', [(179, 'これからの時代 英語が必要になってきます')], ''),
    ('resident', '今は忙しいです。', 'I am busy right now.', [], 'Clean doorway brush-off keeping three-speaker limit.'),
    ('muranishi', '十年後には絶対必要ですよ。', 'Ten years from now, you will definitely need it.', [(181, '年後には')], 'Wrote 10 in kanji 十年後 and completed A1 sentence.'),
    ('ono', '正気か？お前。', 'Are you out of your mind?', [(183, '正気か お前')], ''),
    ('ono', '笑顔が怪しすぎだよ。', 'Your smile is way too suspicious.', [(184, '笑顔 怪しすぎだよ')], 'Added が for clear beginner structure.'),
    ('ono', '全然だめだ。', 'No good at all.', [(185, '全然')], 'Written だめ in hiragana plus だ.'),
    ('muranishi', 'すいません。', 'I am sorry.', [(186, 'すいません')], ''),
]

OPENER = "From polite doorway brush-offs to Ono's blunt feedback, every phrase here is pure everyday Japanese. Let's break them down."

WALK = [
    (0, None, "'Hello.' Written with final \"wa\" spelled like \"ha\", \"konnichiwa\" is the standard daytime greeting at any front door or shop."),
    (1, None, "'Do you like English?' \"Eigo\" means the English language. Putting respectful \"o\" in front of \"suki\", liked or fond of, turns 'do you like' into polite customer-service speech."),
    (2, None, "'No, thank you.' Watch out for \"kekkou desu\"! Although \"kekkou\" can mean 'fine' or 'splendid', when someone offers to sell or pour you something, \"kekkou desu\" means 'I am fine without it—no thank you'."),
    (5, None, "'In the coming era, English is going to become necessary.' \"Korekara\" literally means 'from here on', so \"korekara no jidai\" is 'the coming age'. At the end, \"natte kimasu\" adds the feeling of a change steadily coming toward us."),
    (6, None, "'I am busy right now.' \"Ima\" means now, and \"isogashii\" means busy—a handy two-word shield whenever you cannot talk."),
    (7, None, "'Ten years from now, you will definitely need it.' \"Juunen\" counts ten years, and \"go\" means after, giving 'ten years later'. \"Zettai\" adds 'definitely, no matter what'."),
    (9, None, "'Your smile is way too suspicious.' \"Egao\" combines \"e\", smiling, with \"kao\", face. Clipping \"ayashii\", shady or suspicious, into \"ayashisugi\" attaches \"sugi\", 'too much'."),
    (10, None, "'No good at all.' Pairing \"zenzen\", not at all, with \"dame\", no good, delivers a total thumbs-down: completely hopeless."),
    (11, None, "'I am sorry.' In real conversation, formal \"sumimasen\" very often relaxes into \"suimasen\" by dropping the middle 'm' sound—both mean 'sorry' or 'excuse me'."),
]

TRANSITION = "Now let's listen to Muranishi's disastrous sales calls again."

OUTRO = (
    "Remember \"eigo wa osuki desu ka\" to ask politely if someone likes English, "
    "\"kekkou desu\" for a firm 'no, thank you', and \"suimasen\" for an everyday apology. "
    "Next, Ono reveals what actually works."
)

CLOSING = ('muranishi', 'また会いましょう。')
