ID = 'the-naked-director-s01e01-scene-25'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 25
TITLE = '俺はトシだ  (I Am Toshi)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'toshi': 'トシ', 'mama': 'ママ', 'muranishi': '村西'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Drinking alone in Susukino, Sapporo's lively entertainment district, Muranishi witnesses a loud argument over twenty thousand yen. "
    "After the bar's Mama-san restores order, a young hustler named Toshi sits down beside Muranishi to thank him and pour a drink. "
    "Listen to their first meeting."
)

STORY = [
    ('toshi', '何を返すんだよ？二万？', 'Give back what? Twenty thousand yen?', [(567, '何を返すんだよ'), (569, '万')], 'Wrote 二万 in kanji.'),
    ('mama', '二人ともやめなさい！', 'Both of you, stop it right now!', [(572, 'やめなさい')], 'Wrote 二人 in kanji.'),
    ('mama', '次に騒ぎを起こしたら、トシちゃん、追い出すからね。', 'Cause a commotion next time, Toshi-chan, and I will throw you out.', [(586, '次に騒ぎ'), (586, 'トシちゃん'), (587, '追い出すからね')], 'Added を after 騒ぎ.'),
    ('toshi', '分かってるよ、ママ。', 'I know, I know, Mama.', [(588, '分かってるよ ママ')], ''),
    ('toshi', '悪かったって。ママ、今日も美しいね。', 'I said my bad. Mama, you look beautiful today too.', [(589, '悪かったって'), (589, '今日も美しいね')], ''),
    ('mama', 'あんたもね。はいはい。', 'You too, sure, sure.', [(590, 'あんたもね はいはい')], ''),
    ('toshi', '俺はトシだ。助かったよ。', 'I am Toshi. You really helped me out.', [(592, '俺はトシだ 助かったよ')], ''),
    ('toshi', 'まあ、一杯やってくれよ。', 'Come on, let me pour you a drink.', [(593, 'やってくれよ')], 'Added 一杯 to clarify pouring a drink.'),
    ('muranishi', 'いや、もう十分だ。', 'No, I have had plenty already.', [(595, 'もう十分だ')], 'Added いや for natural conversational flow.'),
    ('toshi', 'そんな冷たいこと言うなよ。', 'Do not say something so cold.', [(596, 'こと言うなよ')], 'Replaced slang つれねえ with standard A1 冷たい.'),
    ('toshi', 'さあ、グラスを持ってきて。', 'Come on, bring a glass over here.', [(596, 'さあ グラス'), (596, '持ってきて')], 'Added を after グラス.'),
    ('muranishi', 'じゃあ、少しだけいただくよ。', 'Well then, I will have just a little.', [], 'Polite acceptance closing the exchange.'),
]

OPENER = "Bar banter moves fast—from stern scolding to shameless flattery to pouring drinks. Let's unpack each expression."

WALK = [
    (0, None, "'Give back what? Twenty thousand yen?' \"Kaesu\" means to return something to its owner. Notice Japanese counts big sums in units of \"man\", ten thousand—so \"niman\" is two ten-thousands, twenty thousand!"),
    (1, None, "'Both of you, stop it right now!' \"Futari tomo\" addresses the pair together as 'both of you'. Attaching \"nasai\" to \"yameru\", to stop, gives Mama-san a firm motherly command."),
    (2, None, "'Cause a commotion next time, Toshi-chan, and I will throw you out.' \"Tsugi ni\" means next time, \"sawagi\" is a ruckus, and \"oidasu\" joins \"ou\", chase, with \"dasu\", put out—literally 'chase out the door'."),
    (4, 'ママ、今日も美しいね。', "'Mama, you look beautiful today too.' Turning on the charm, Toshi uses \"kyou mo\", today as well, and literary-sounding \"utsukushii\", beautiful."),
    (5, None, "'You too, sure, sure.' Not fooled by his flattery, Mama-san brushes him off with \"hai hai\"—saying \"hai\" twice in a row means 'yeah, yeah, whatever you say'."),
    (6, '助かったよ。', "'You really helped me out.' Literally \"tasukatta\" means 'I was saved!'—the everyday way Japanese speakers thank someone whenever a small favour rescues them from a tight spot."),
    (7, None, "'Come on, let me pour you a drink.' \"Ippai\" counts one cup or glass, and \"ippai yaru\" is relaxed after-work shorthand for having a drink together."),
    (8, None, "'No, I have had plenty already.' \"Mou juubun\" pairs \"mou\", already, with \"juubun\", enough or plenty—useful whenever someone tries to refill your glass or plate."),
    (9, None, "'Do not say something so cold.' Just as English calls an unfriendly refusal 'cold', Japanese uses \"tsumetai\", chilly to the touch, for a cold attitude."),
    (10, None, "'Come on, bring a glass over here.' Combining \"motte\", holding, with \"kite\", come, gives \"motte kite\"—'bring it here!'"),
]

TRANSITION = "Now let's listen to Toshi and Muranishi's bar meeting again."

OUTRO = (
    "Keep \"tasukatta\" handy for 'you saved me!', \"mou juubun\" when you have had enough, "
    "and \"motte kite\" to ask someone to bring something over. "
    "See you in scene twenty-six."
)

CLOSING = ('mama', 'またね。')
