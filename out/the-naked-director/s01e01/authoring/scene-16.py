ID = 'the-naked-director-s01e01-scene-16'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 16
TITLE = 'お待たせしすぎたのかもしれません  (Perhaps I Kept You Waiting Too Long)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'client_f': '女性客', 'muranishi': '村西', 'customer': '客'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Arriving late to a home appointment, Muranishi faces an annoyed client checking the clock. "
    "Instead of shrinking back, he delivers the line that becomes his lifelong trademark—turning his lateness into destiny and urging the room to decide right this instant. "
    "Listen to Muranishi at full power."
)

STORY = [
    ('client_f', '遅いわよ。約束の時間が過ぎてる。', 'You are late. The appointment time has passed.', [(389, '遅いわよ 約束の時間 過ぎてる')], 'Added が after 約束の時間 for clarity.'),
    ('muranishi', '申し訳ございません。お待たせしすぎたのかもしれません。', 'I am deeply sorry. Perhaps I kept you waiting too long.', [(390, '申し訳ございません お待たせしすぎたのかもしれません')], ''),
    ('muranishi', '人との出会いはすべてミラクルです。', 'Every meeting between people is a miracle.', [(393, '人との出会いは'), (393, 'すべてミラクル')], 'Shortened middle phrase and added です.'),
    ('muranishi', '今決められないなら一生決められません。', 'If you cannot decide now, you will not decide in a lifetime.', [(398, '今 決められない'), (399, '一生')], 'Condensed two-cue parallel into crisp A1 sentence.'),
    ('muranishi', '皆様は毎日お忙しい日々を過ごしております。', 'All of you spend busy days every single day.', [(400, 'お忙しい日々を')], 'Simplified honorific verb to 過ごしております.'),
    ('muranishi', 'ストレートに言います！', 'I will say it straight!', [(406, 'ストレートに言います')], ''),
    ('muranishi', 'はっきり言ってラストチャンスです！', 'To put it plainly, this is your last chance!', [(409, 'はっきり言って ラストチャンスです')], ''),
    ('muranishi', '大勢の方がわたくしを待っているからです。', 'Because many other people are waiting for me.', [(415, '大勢の方が'), (416, '待っているからです')], ''),
    ('muranishi', 'これはわたくしの使命なんです！', 'This is my mission!', [(420, 'これは わたくしの使命なんです')], ''),
    ('muranishi', 'ジャストナウ！', 'Just now!', [(423, 'ジャストナウ')], ''),
    ('customer', '俺、買うよ。今か！', 'I will buy it. Right now, huh!', [(424, '俺 買うよ 今か')], ''),
    ('muranishi', 'ご購入ありがとうございます。今しかありませんよ！', 'Thank you for your purchase. There is only right now!', [(425, 'ご購入 ありがとうございます'), (426, '今しかありませんよ')], ''),
]

OPENER = "Muranishi turns an ordinary sales visit into high theatre, culminating in his most famous catchphrase. Let's hear how each line lands."

WALK = [
    (0, '遅いわよ。', [
        "'You are late.'  Starting off with ",
        ("client_f", "遅い"), ". This word covers both slow and late, and assertive ",
        ("client_f", "わよ"), " adds sharp impatience as she glares at the door."
    ]),
    (0, '約束の時間が過ぎてる。', [
        "'The appointment time has passed.'  The speaker uses ",
        ("client_f", "約束"), " this word means promise or appointment, ",
        ("client_f", "時間"), " is time, and ",
        ("client_f", "過ぎてる"), " comes from the verb for to pass beyond."
    ]),
    (1, '申し訳ございません。', [
        '"\'I am deeply sorry.\' Literally, " We can hear ',
        ("muranishi", "申し訳"), " this word means an excuse or explanation, so saying none exists—",
        ("muranishi", "ございません"), "—declares 'my mistake is inexcusable'."
    ]),
    (1, 'お待たせしすぎたのかもしれません。', [
        '"\'Perhaps I kept you waiting too long.\' Here is Muranishi\'s signature line! Polite " We can hear ',
        ("muranishi", "お待たせ"), ", keeping you waiting, gets ",
        ("muranishi", "しすぎた"), ". This word means too much, tucked inside—turning an ordinary late arrival into dramatic fate."
    ]),
    (2, None, [
        "'Every meeting between people is a miracle.'  The character says ",
        ("muranishi", "出会い"), " comes from the verb for to encounter by chance, naming a meaningful meeting in life, paired with ",
        ("muranishi", "すべて"), ", all."
    ]),
    (3, None, [
        "'If you cannot decide now, you will not decide in a lifetime.'  We can hear ",
        ("muranishi", "決められない"), " this word is the 'cannot decide' version of the verb for to decide, and ",
        ("muranishi", "一生"), " spans one entire lifetime."
    ]),
    (6, None, [
        "'To put it plainly, this is your last chance!'  The phrase contains ",
        ("muranishi", "はっきり"), " is an expressive sound-word meaning clearly or bluntly, leading straight into katakana English ",
        ("muranishi", "ラストチャンス"), "."
    ]),
    (8, None, [
        "'This is my mission!'  It features ",
        ("muranishi", "使命"), " this word means a calling or mission, and ",
        ("muranishi", "なんです"), " wraps it in earnest conviction."
    ]),
    (9, None, [
        '"\'Just now!\' Muranishi shouts English " Pay attention to ',
        ("muranishi", "ジャストナウ！"), " to mean 'right this very second!'—even though English speakers would say 'right now!'"
    ]),
    (10, '俺、買うよ。', [
        '"\'I will buy it.\' Swept up in the urgency, the buyer blurts plain dictionary-form " The word ',
        ("customer", "買う"), ". This word means to buy, plus decisive ",
        ("customer", "よ")
    ]),
    (11, '今しかありませんよ！', [
        '"\'There is only right now!\' Pairing " Listen for ',
        ("muranishi", "しか"), " after ",
        ("muranishi", "今"), ", now, with negative ",
        ("muranishi", "ありません"), " creates a spotlight meaning 'nothing except right now!'"
    ]),
]

TRANSITION = "Now let's listen to Muranishi's legendary late-arrival pitch again."

OUTRO = (
    "Remember the phrase for an appointment time, the expression when you need a sincere formal apology, "
    "and the expression for 'there is only now!'. "
    "See you at the celebration next."
)

CLOSING = ('client_f', 'またね。')
