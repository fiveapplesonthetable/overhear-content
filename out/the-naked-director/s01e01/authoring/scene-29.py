ID = 'the-naked-director-s01e01-scene-29'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 29
TITLE = 'もう後戻りできないぞ  (No Turning Back Now)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'muranishi': '村西', 'toshi': 'トシ'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Walking through Susukino at night, the protagonist spots magazines sealed in clear plastic wrap so browsers cannot peek inside without buying. "
    "When his new partner tells him they sell over a million copies every month, he drops all hesitation and marches straight toward a shop called Showtime. "
    "Listen to the finale of Episode One."
)

STORY = [
    ('muranishi', 'これは何だ？', 'What is this?', [(683, 'これは')], 'Added 何だ for a complete A1 question.'),
    ('toshi', 'ビニールに包まれた中身が見えない本だ。', 'It is a book wrapped in vinyl so you cannot see the contents.', [(684, 'ビニールに包まれた 中身が見えない')], 'Used clean A1 noun 本.'),
    ('toshi', '中身を隠して買わせる新しい本なんだよ。', 'It hides what is inside to make people buy it—a new kind of book.', [(686, '中身を隠して'), (687, '買わせる'), (688, '新しい')], ''),
    ('toshi', 'これを考えた人は頭が切れるよな。', 'Whoever thought this up is really sharp.', [(689, '考えた')], 'Used 人 and kanji 切れる for A1 clarity.'),
    ('muranishi', 'これ、月にどのぐらい売れてるんだ？', 'Roughly how many of these sell per month?', [(690, 'これ 月 どのぐらい売れて')], 'Added に after 月.'),
    ('toshi', '月に百万冊以上は売れてるらしい。', 'Over a million copies a month, apparently.', [(691, '月に'), (691, '売れてるらしい')], 'Wrote 百万冊以上 in kanji.'),
    ('muranishi', '百万冊！？', 'One million copies!?', [(692, '万冊')], 'Wrote 百万冊 in kanji.'),
    ('muranishi', 'トシ、これを仕入れることはできるか？', 'Toshi, can we stock these?', [(694, 'トシ'), (696, '仕入れること')], 'Added これを and は for clean A1 grammar.'),
    ('toshi', '急に呼び捨てかよ。', "He says 'Suddenly calling me by my bare first name, huh?'", [(695, '急に呼び捨てかよ')], ''),
    ('toshi', 'まあ、あのショータイムだ。もう後戻りできないぞ。', 'Well, over at Showtime there. There is no turning back anymore.', [(697, 'まあ'), (698, 'あの ショータイム'), (700, 'もう後戻りでき')], 'Standardised できねえぞ to できないぞ.'),
    ('muranishi', '分かってる。', 'I know.', [(701, '分かってる')], ''),
    ('muranishi', '行ってくる。', 'I am going in.', [(702, '行ってくる')], ''),
]

OPENER = "Episode One ends with big numbers, sudden familiarity, and the same two-word doorway phrase our protagonist used at home—now with a brand-new meaning."

WALK = [
    (1, None, [
        "'It is a book wrapped in vinyl so you cannot see the contents.'  It features ",
        (None, "中身"), " joins the word for inside with the word for body or substance—meaning the contents inside a package, bag, or book. ",
        (None, "見えない"), " this word means cannot be seen."
    ]),
    (2, None, [
        '"\'It hides what is inside to make people buy it—a new kind of book.\' Turning the verb to buy into " The phrase contains ',
        (None, "買わせる"), " expresses making or tempting customers to buy, followed by ",
        (None, "新しい"), ", new."
    ]),
    (3, None, [
        '"\'Whoever thought this up is really sharp.\' Just like English \'sharp\', " Pay attention to ',
        (None, "頭が切れる"), " literally says 'the head cuts cleanly'—praising a clever, quick-witted business mind!"
    ]),
    (4, None, [
        '"\'Roughly how many of these sell per month?\' Built from the word for which, plus the word for about, " The speaker uses ',
        (None, "どのぐらい"), " asks 'roughly how much?', handy for prices, distances, and sales totals alike."
    ]),
    (5, None, [
        '"\'Over a million copies a month, apparently.\' Bound books and magazines count with the counter for books. Since the word for ten thousand is used, one hundred ten-thousands—" In this line, ',
        (None, "百万"), "—equals one million, and ",
        (None, "らしい"), " adds 'so I hear'."
    ]),
    (7, None, [
        '"\'Toshi, can we stock these?\' Store owners use " The speaker uses ',
        (None, "仕入れる"), " for buying stock to resell, paired with ",
        (None, "ことはできるか"), ", 'is it possible to?'"
    ]),
    (8, None, [
        '"He says \'Suddenly calling me by my bare first name, huh?\' Big cultural moment: " The word ',
        (None, "呼び捨て"), " this word means dropping polite suffixes and calling someone by their bare name alone—showing he just shifted into boss-and-partner mode ",
        (None, "急に"), ", all of a sudden!"
    ]),
    (9, 'もう後戻りできないぞ。', [
        "'There is no turning back anymore.'  You can catch ",
        (None, "後戻り"), " combines the word for back with the word for returning—so ",
        (None, "もう後戻りできない"), " warns 'you cannot turn back now'."
    ]),
    (10, None, [
        '"\'I know.\' Calm, unhurried " Pay attention to ',
        (None, "分かってる"), " drops yesterday's defensive ending—now he means business."
    ]),
    (11, None, [
        '"\'I am going in.\' Earlier he used " Watch for ',
        (None, "行ってくる"), " with his kids at the front door; here, and this word is built from the verb to go and the verb to come back, those same words launch a whole new life."
    ]),
]

TRANSITION = "Now let's listen to the final scene of Episode One from beginning to end."

OUTRO = (
    "Congratulations on finishing all of Episode One! "
    "You learned the word for contents, the phrase for a sharp mind, the term for dropping polite titles, "
    "and saw the everyday doorway phrase come full circle. "
    "Until Episode Two—see you next time!"
)
CLOSING = ('muranishi', 'また会いましょう。')
