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
    (0, '遅いわよ。', "'You are late.' \"Osoi\" covers both slow and late, and assertive \"wa yo\" adds sharp impatience as she glares at the door."),
    (0, '約束の時間が過ぎてる。', "'The appointment time has passed.' \"Yakusoku\" means promise or appointment, \"jikan\" is time, and \"sugiteru\" comes from \"sugiru\", to pass beyond."),
    (1, '申し訳ございません。', "'I am deeply sorry.' Literally \"moushiwake\" means an excuse or explanation, so saying none exists—\"gozaimasen\"—declares 'my mistake is inexcusable'."),
    (1, 'お待たせしすぎたのかもしれません。', "'Perhaps I kept you waiting too long.' Here is Muranishi's signature line! Polite \"omatase shita\", kept you waiting, gets \"sugi\", too much, tucked inside—turning an ordinary late arrival into dramatic fate."),
    (2, None, "'Every meeting between people is a miracle.' \"Deai\" comes from \"deau\", to encounter by chance, naming a meaningful meeting in life, paired with \"subete\", all."),
    (3, None, "'If you cannot decide now, you will not decide in a lifetime.' \"Kimerareru\" is the 'can decide' version of \"kimeru\", and \"isshou\" spans one entire lifetime."),
    (6, None, "'To put it plainly, this is your last chance!' \"Hakkiri\" is an expressive sound-word meaning clearly or bluntly, leading straight into katakana English \"rasuto chansu\"."),
    (8, None, "'This is my mission!' \"Shimei\" means a calling or mission, and \"nan desu\" wraps it in earnest conviction."),
    (9, None, "'Just now!' Muranishi shouts English \"jasuto nau\" to mean 'right this very second!'—even though English speakers would say 'right now!'"),
    (10, '俺、買うよ。', "'I will buy it.' Swept up in the urgency, the buyer blurts plain dictionary-form \"kau\", to buy, plus decisive \"yo\"."),
    (11, '今しかありませんよ！', "'There is only right now!' Pairing \"shika\" after \"ima\", now, with negative \"arimasen\" creates a spotlight meaning 'nothing except right now!'"),
]

TRANSITION = "Now let's listen to Muranishi's legendary late-arrival pitch again."

OUTRO = (
    "Remember \"yakusoku no jikan\" for an appointment time, \"moushiwake gozaimasen\" when you need a sincere formal apology, "
    "and \"ima shika arimasen\" for 'there is only now!'. "
    "See you at the celebration next."
)

CLOSING = ('client_f', 'またね。')
