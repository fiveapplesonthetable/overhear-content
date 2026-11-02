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
    (0, None, "'Um, I was told to learn about sales from you, Ono-san.' Opening with \"ano\" buys a polite beat before making a request. \"Eigyou\" means sales work, and ending on casual quoting \"tte\" acts like 'they told me to...'."),
    (1, None, "'Hitchcock died.' \"Shinda\" is the plain past of \"shinu\", to die, and \"yo\" flags it as fresh news the listener has not heard yet."),
    (2, None, "'That is rather blunt, is it not?' Muranishi mistakes the remark for coldness and says \"buaisou\", unfriendly or curt, softened with \"desu ne\"."),
    (3, None, "'Are you out of your mind?' Ono's favourite catchphrase hinges on \"shouki\", sanity or right mind. Adding sharp \"ka\" fires back 'are you sane?' whenever someone says something outrageous."),
    (5, None, "'What kind of music do you listen to?' \"Ongaku\" means music, \"nani\" asks what, and \"kiku\" covers both listening and asking."),
    (6, None, "'Lately, Western music.' \"Saikin\" means lately or recently. \"Yougaku\" pairs \"you\", Western, with \"gaku\", music—contrasting neatly with \"hougaku\", Japanese music."),
    (7, '日本人ならこれだろ。', "'If you are Japanese, it has to be this.' Adding \"jin\", person, to \"Nihon\" builds \"Nihonjin\", a Japanese person, and \"nara\" means 'if it is the case that'."),
    (8, None, "'We are free, are we not?' Singing along, Muranishi uses \"bokura\", casual 'we', and \"jiyuu\", freedom—a word that echoes through the whole episode."),
    (9, 'よし、合格だ。', "'All right, you pass.' \"Yoshi\" is an upbeat 'all right!', and \"goukaku\" is the word for passing an exam or audition."),
    (9, '明日から教えてやるよ。', "'I will teach you starting tomorrow.' \"Ashita\" is tomorrow, followed by \"kara\", from. \"Oshiete yaru\" attaches tough, big-brother \"yaru\" to \"oshieru\", to teach, showing Ono sees himself as the boss of this pair."),
    (10, None, "'Thank you, I look forward to working with you.' Built around \"yoroshiku\", favourably, \"yoroshiku onegai shimasu\" is the set greeting you use whenever a new partnership, job, or lesson begins."),
]

TRANSITION = "Now let's listen to Ono's impromptu audition once more."

OUTRO = (
    "You just heard \"saikin\" for lately, \"jiyuu\" for free, \"ashita kara\" for starting tomorrow, "
    "and the indispensable partnership greeting \"yoroshiku onegai shimasu\". "
    "Until next time."
)

CLOSING = ('muranishi', 'また明日。')
