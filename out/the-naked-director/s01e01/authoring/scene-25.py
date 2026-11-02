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
    "Drinking alone in Susukino, Sapporo's lively entertainment district, the protagonist witnesses a loud argument over twenty thousand yen. "
    "After the bar's owner restores order, a young hustler sits down beside him to thank him and pour a drink. "
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
    (0, None, [
        "'Give back what? Twenty thousand yen?'  Check out ",
        (None, "返す"), " this word means to return something to its owner. Notice Japanese counts big sums in units of ",
        (None, "万"), ", ten thousand—so ",
        (None, "二万"), " is two ten-thousands, twenty thousand!"
    ]),
    (1, None, [
        "'Both of you, stop it right now!'  The speaker uses ",
        (None, "二人とも"), " addresses the pair together as 'both of you'. Attaching a firm ending to ",
        (None, "やめなさい"), " gives a motherly command."
    ]),
    (2, None, [
        "'Cause a commotion next time, Toshi-chan, and I will throw you out.'  We can hear ",
        (None, "次に"), " this word means next time, ",
        (None, "騒ぎ"), " this word is a ruckus, and ",
        (None, "追い出す"), " joins the verb for chase with the verb for put out—literally 'chase out the door'."
    ]),
    (4, 'ママ、今日も美しいね。', [
        '"\'Mama, you look beautiful today too.\' Turning on the charm, he uses " The phrase contains ',
        (None, "今日も"), ", today as well, and literary-sounding ",
        (None, "美しいね"), ", beautiful."
    ]),
    (5, None, [
        '"\'You too, sure, sure.\' Not fooled by his flattery, she brushes him off with " Watch for ',
        (None, "はいはい"), "—saying yes twice in a row this word means 'yeah, yeah, whatever you say'."
    ]),
    (6, '助かったよ。', [
        '"\'You really helped me out.\' Literally " You can catch ',
        (None, "助かったよ"), " this word means 'I was saved!'—the everyday way speakers thank someone whenever a small favour rescues them."
    ]),
    (7, None, [
        "'Come on, let me pour you a drink.'  It features ",
        (None, "一杯"), " counts one cup or glass, and pouring one is relaxed after-work shorthand for having a drink together."
    ]),
    (8, None, [
        "'No, I have had plenty already.'  The word ",
        (None, "もう十分だ"), " pairs ",
        (None, "もう"), ", already, with ",
        (None, "十分だ"), ", enough or plenty—useful whenever someone tries to refill your glass or plate."
    ]),
    (9, None, [
        '"\'Do not say something so cold.\' Just as English calls an unfriendly refusal \'cold\', Japanese uses " Starting off with ',
        (None, "冷たい"), ", chilly to the touch, for a cold attitude."
    ]),
    (10, None, [
        '"\'Come on, bring a glass over here.\' Combining the verb for holding with the verb for come gives " In this line, ',
        (None, "持ってきて"), "—'bring it here!'"
    ]),
]

TRANSITION = "Now let's listen to their bar meeting again."

OUTRO = (
    "Keep the phrase for 'you saved me!' handy, the expression for when you have had enough, "
    "and the command to ask someone to bring something over. "
    "See you in scene twenty-six."
)
CLOSING = ('mama', 'またね。')
