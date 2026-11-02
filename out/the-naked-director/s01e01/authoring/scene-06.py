ID = 'the-naked-director-s01e01-scene-06'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = '鼻歌なんかやめろ  (Stop Humming at Breakfast)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kozue': 'こずえ', 'muranishi': '村西', 'mayumi': '真由美'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "The next morning at the Muranishi family table, Toru's mother Kozue sighs about the economy while Toru hums happily. "
    "His daughter Mayumi greets everyone, Kozue scolds his humming, and Toru brags that things are looking up at work. "
    "Listen to the family breakfast table first."
)

STORY = [
    ('kozue', '不景気だなあ。', 'Times sure are hard.', [(106, '不景気だなあ')], ''),
    ('mayumi', 'おはよう。', 'Good morning.', [(108, 'おはよう')], ''),
    ('kozue', 'おはよう。', 'Good morning.', [(110, 'おはよう')], ''),
    ('kozue', '鼻歌なんかやめろ。', 'Stop that humming.', [(112, '鼻歌なんかやめろ')], ''),
    ('muranishi', '何でだよ。', 'Why, what is wrong with that?', [(114, '何でだよ')], ''),
    ('kozue', '仕事はちゃんとやってるのか？', 'Are you doing your job properly?', [(116, '仕事は ちゃんとやって')], 'Normalized northern dialect ending んのげ to んのか / るのか.'),
    ('muranishi', 'もちろん。', 'Of course.', [(117, 'もちろん')], ''),
    ('muranishi', '営業トップの人と組むことになった。', 'It has been decided I will team up with the top sales person.', [(118, '営業トップの人と'), (118, '組むことになった')], ''),
    ('muranishi', '上司から期待されてるんだ。', 'My boss has high hopes for me.', [(119, '上司から期待されて')], 'Added る in されてるんだ for standard spoken clarity.'),
    ('kozue', '家族を満足させないとだめだぞ。', 'You have got to keep your family satisfied.', [(121, '家族'), (121, '満足させ')], 'Rendered northern dialect warning into clear standard Japanese.'),
    ('muranishi', '分かってるよ。', 'I know, I know.', [(123, '分かってるよ')], ''),
    ('kozue', 'ほんとに大丈夫か？', 'Is it really going to be okay?', [(125, 'どうすんだ')], 'Adapted Kozue’s worried sigh into a simple A1 check.'),
]

OPENER = "At home, polite endings disappear completely. Let's look at how family members talk over breakfast."

WALK = [
    (0, None, [
        '"\'Times sure are hard.\' Remember " We can hear ',
        (None, "不景気"), ", recession, from the office? Stretching out ",
        (None, "だなあ"), " turns it into a weary sigh to herself."
    ]),
    (1, None, [
        '"\'Good morning.\' Between family and close friends, " The word ',
        (None, "おはよう。"), " stands on its own without the polite ending you use at work."
    ]),
    (3, None, [
        "'Stop that humming.'  You will hear ",
        (None, "鼻歌"), " joins the word for nose with the word for song—literally a 'nose-song'! Sliding ",
        (None, "なんか"), " after it dismisses humming as silly, before the blunt ",
        (None, "やめろ"), ", quit it!"
    ]),
    (4, None, [
        "'Why, what is wrong with that?'  You can catch ",
        (None, "何で"), " is everyday spoken 'why', more casual than other question words, and ",
        (None, "だよ"), " pushes back with mild protest."
    ]),
    (5, None, [
        "'Are you doing your job properly?'  It features ",
        (None, "仕事"), " this word means work or job, and ",
        (None, "ちゃんと"), " this word is a wonderfully useful everyday word meaning properly, neatly, or seriously."
    ]),
    (6, None, [
        '"\'Of course.\' One crisp word, " The speaker uses ',
        (None, "もちろん。"), ", answers 'of course!' in both casual and polite conversations."
    ]),
    (7, None, [
        "'It has been decided I will team up with the top sales person.'  Hear how ",
        (None, "組む"), " this word means to pair up or join forces. Ending an action with ",
        (None, "ことになった"), " presents the arrangement as something decided for you, rather than your own boast."
    ]),
    (8, None, [
        "'My boss has high hopes for me.'  The character says ",
        (None, "上司"), " this word means superior or boss, and ",
        (None, "期待"), " this word means expectation or hope, here turned into 'being counted on'."
    ]),
    (9, None, [
        "'You have got to keep your family satisfied.'  Notice how ",
        (None, "満足"), " this word means satisfaction, and ",
        (None, "だめ"), " signals 'no good'—so ",
        (None, "ないとだめ"), " is how you say 'if you do not do this, it will not do'."
    ]),
    (10, None, [
        '"\'I know, I know.\' Built from the verb to understand, " In this line, ',
        (None, "分かってるよ"), " is how every scolded husband or teenager in Japan answers 'I already get it!'"
    ]),
]

TRANSITION = "Now let's listen to the whole breakfast conversation again."

OUTRO = (
    "The word for humming—literally a nose-song—is easy to picture and never forgotten, "
    "and phrases like 'of course' and 'I know' pop up constantly in family life. "
    "See you in the hallway next."
)

CLOSING = ('mayumi', 'またね。')
