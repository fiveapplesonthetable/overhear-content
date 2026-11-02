ID = 'the-naked-director-s01e01-scene-05'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = '明日から教えてやる  (I Will Teach You Starting Tomorrow)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'muranishi': '村西', 'ono': '小野'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Following his boss's orders, Muranishi approaches Ono, the company's star salesman. "
    "Instead of talking about encyclopedias, Ono tests Muranishi on Alfred Hitchcock, pop music, and singing in the street. "
    "Listen to how this strange audition unfolds."
)

STORY = [
    ('muranishi', 'あの、小野さんから営業のことを学べって。', 'Um, I was told to learn about sales from you, Ono-san.', [(84, '小野さんから 営業のことを学べって')], ''),
    ('ono', 'ヒッチコックが死んだよ。', 'Hitchcock died.', [(85, 'ヒッチコックが死んだよ')], ''),
    ('muranishi', '無愛想ですね。', 'That is rather blunt, is it not?', [(86, '無愛想ですね')], ''),
    ('ono', '正気か？お前。', 'Are you out of your mind?', [(87, '正気か お前')], ''),
    ('muranishi', 'サイコは傑作ですよ。', 'Psycho is a masterpiece.', [(89, '傑作ですよ')], 'Combined title and praise from cue 89.'),
    ('ono', 'お前、音楽は何を聴くんだよ？', 'What kind of music do you listen to?', [(91, '音楽は何')], 'Added object marker を for A1 clarity.'),
    ('muranishi', '最近は洋楽です。', 'Lately, Western music.', [(92, '最近は洋楽')], 'Completed sentence with polite です.'),
    ('ono', '日本人ならこれだろ。歌えよ。', 'If you are Japanese, it has to be this. Sing!', [(94, '日本人なら これだろ'), (97, '歌えよ')], ''),
    ('muranishi', '僕らは自由だね。', 'We are free, are we not?', [(95, '自由だね')], 'Written 僕ら in standard kana.'),
    ('ono', 'よし、合格だ。明日から教えてやるよ。', 'All right, you pass. I will teach you starting tomorrow.', [(102, 'よし 合格だ 明日から教えてやるよ')], ''),
    ('muranishi', 'よろしくお願いします。', 'Thank you, I look forward to working with you.', [(103, 'よろしくお願いします')], ''),
    ('ono', 'じゃあ、さようなら。', 'Well then, goodbye.', [(104, 'じゃあ')], 'Standardised song-echo さよなら to standard さようなら.'),
]

OPENER = "Ono speaks in rapid, confident plain speech while Muranishi stays respectful. Let's walk through the highlights."

WALK = [
    (0, None, [
        '"\'Um, I was told to learn about sales from you, Ono-san.\' Opening with " We can hear ',
        (None, "あの"), " buys a polite beat before making a request. ",
        (None, "営業"), " this word means sales work, and ending on the casual quoting particle ",
        (None, "って"), " acts like 'they told me to...'."
    ]),
    (1, None, [
        "'Hitchcock died.'  The word ",
        (None, "死んだ"), " this word is the plain past of the verb to die, and ",
        (None, "よ"), " flags it as fresh news the listener has not heard yet."
    ]),
    (2, None, [
        '"\'That is rather blunt, is it not?\' Muranishi mistakes the remark for coldness and says " Focus on ',
        (None, "無愛想"), ", unfriendly or curt, softened with ",
        (None, "ですね")
    ]),
    (3, None, [
        '"\'Are you out of your mind?\' Ono\'s favourite catchphrase hinges on " Hear how ',
        (None, "正気"), ", sanity or right mind. Adding the sharp ",
        (None, "か"), " fires back 'are you sane?' whenever someone says something outrageous."
    ]),
    (5, None, [
        "'What kind of music do you listen to?'  In this sentence, ",
        (None, "音楽"), " this word means music, ",
        (None, "何"), " asks what, and ",
        (None, "聴く"), " covers both listening and asking."
    ]),
    (6, None, [
        "'Lately, Western music.'  Check out ",
        (None, "最近"), " this word means lately or recently. ",
        (None, "洋楽"), " pairs the character for Western with the one for music—contrasting neatly with the word for Japanese music."
    ]),
    (7, '日本人ならこれだろ。', [
        '"\'If you are Japanese, it has to be this.\' Adding the character for person to the word for Japan builds " They are saying ',
        (None, "日本人"), ", a Japanese person, and ",
        (None, "なら"), " this word means 'if it is the case that'."
    ]),
    (8, None, [
        '"\'We are free, are we not?\' Singing along, Muranishi uses " They are saying ',
        (None, "僕ら"), ", casual 'we', and ",
        (None, "自由"), ", freedom—a word that echoes through the whole episode."
    ]),
    (9, 'よし、合格だ。', [
        "'All right, you pass.'  Here, the word ",
        (None, "よし"), " is an upbeat 'all right!', and ",
        (None, "合格"), " this word is the word for passing an exam or audition."
    ]),
    (9, '明日から教えてやるよ。', [
        "'I will teach you starting tomorrow.'  The word ",
        (None, "明日"), " is tomorrow, followed by ",
        (None, "から"), ", from. ",
        (None, "教えてやる"), " attaches the tough, big-brother ending to the verb to teach, showing Ono sees himself as the boss of this pair."
    ]),
    (10, None, [
        '"\'Thank you, I look forward to working with you.\' Built around " Watch for ',
        (None, "よろしく"), ", favourably, ",
        (None, "よろしくお願いします"), " this word is the set greeting you use whenever a new partnership, job, or lesson begins."
    ]),
]

TRANSITION = "Now let's listen to Ono's impromptu audition once more."

OUTRO = (
    "You just heard words for lately and free, phrases for starting tomorrow, "
    "and the indispensable partnership greeting to look forward to working together. "
    "Until next time."
)

CLOSING = ('muranishi', 'また明日。')
