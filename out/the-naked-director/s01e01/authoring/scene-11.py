ID = 'the-naked-director-s01e01-scene-11'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 11
TITLE = 'セールストークのコツ  (The Trick to Sales Talk)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'ono': '小野', 'muranishi': '村西'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Sitting down after those failed doorbell calls, Ono suddenly praises Muranishi for supporting his wife, two children, and mother all by himself. "
    "The moment Muranishi brightens up, Ono grins—he was demonstrating the secret of sales talk. "
    "Listen to Ono's lesson."
)

STORY = [
    ('ono', 'まあ、でもお前は頑張ってるよ。', 'Well, still, you are working really hard.', [(187, 'でも お前は頑張ってるよ')], ''),
    ('ono', '嫁さんと子供二人とおふくろさんを食べさせてるんだろ？', 'You are feeding your wife, two kids, and your mum, right?', [(190, '嫁さんと子供'), (190, 'おふくろさん')], 'Wrote 二人 in kanji and trimmed たった１人で for length.'),
    ('ono', '立派だよ、本当に。根性もあるしな。', 'That is admirable, truly. And you have grit too.', [(191, '立派だよ 本当に'), (192, '根性もあるしな')], ''),
    ('muranishi', 'ありがとうございます。', 'Thank you very much.', [(193, 'ありがとうございます')], ''),
    ('ono', '一瞬やる気になったろ？', 'For a second there, you felt motivated, right?', [(195, '一瞬 やる気になったろ')], ''),
    ('ono', 'これがセールストークの基本だ。', 'This is the foundation of sales talk.', [(196, 'これがセールストークの基本だ')], ''),
    ('ono', '褒めて相手を口説くんだよ。', 'You praise the other person and win them over.', [(198, '褒めて'), (198, '相手を')], 'Moved 相手を before the action for smooth A1 word order.'),
    ('ono', '褒めて、褒めて、心を開かせろ。', 'Praise them, praise them, and make them open their heart.', [(202, '褒めて 褒めて'), (203, '心を開かせろ')], ''),
    ('ono', 'なるべく丁寧な言葉でな。', 'Using as formal language as possible, mind you.', [(207, 'なるべく丁寧な言葉でな')], ''),
    ('ono', '英語の教材を売ってるんだから英語を使え。', 'You are selling English materials, so use English.', [(209, '英語の教材'), (209, '英語使え')], 'Added を markers for clear A1 structure.'),
    ('muranishi', 'お恥ずかしながら、私、イングリッシュは苦手で。', 'Embarrassing as it is, English is my weak point.', [(211, 'お恥ずかしながら 私 イングリッシュは苦手で')], ''),
    ('ono', '難しく考えるな。何でもいいから単語を言えばいいんだよ。', 'Do not overthink it. Just say any single words at all.', [(212, '難しく考え'), (213, '何でもいいから 単語を言えばいいんだよ')], 'Standardised 考えんな to 考えるな.'),
]

OPENER = "Ono gives Muranishi a masterclass in human psychology—and gives us a treasure chest of everyday expressions."

WALK = [
    (0, None, [
        '"\'Well, still, you are working really hard.\' The word for this is " Listen for ',
        (None, "頑張ってる。"),
        ", which comes from the word meaning to hang in there and give your best effort—one of the warmest things a colleague can tell you."
    ]),
    (1, None, [
        '"\'You are feeding your wife, two kids, and your mum, right?\' The casual word for a man\'s wife is " In this line, ',
        (None, "嫁さん。"),
        ", ",
        (None, "二人。"),
        " counts two people, and affectionate ",
        (None, "おふくろさん。"),
        " means one's mother. ",
        (None, "食べさせてる。"),
        " turns the word for eat into 'feeding and supporting'."
    ]),
    (2, '立派だよ、本当に。', [
        '"\'That is admirable, truly.\' In this sentence, the word for admirable is " The speaker uses ',
        (None, "立派。"),
        ", which praises someone as splendid, worthy of respect, or standing tall, reinforced by ",
        (None, "本当に。"),
        ", truly."
    ]),
    (4, None, [
        '"\'For a second there, you felt motivated, right?\' The word for motivation, " Notice how ',
        (None, "やる気。"),
        ", glues the word for doing onto the word for spirit—literally 'doing-spirit', the everyday word for motivation!"
    ]),
    (5, None, [
        '"\'This is the foundation of sales talk.\' The word for foundation here is " Starting off with ',
        (None, "基本。"),
        ", which means the basics or foundation of any craft, sport, or skill."
    ]),
    (6, None, [
        '"\'You praise the other person and win them over.\' The word for the other person is " Starting off with ',
        (None, "相手。"),
        ", meaning the person across from you—your listener, partner, or customer—and ",
        (None, "褒めて。"),
        " links the word for praise into ",
        (None, "口説く。"),
        ", to woo or persuade."
    ]),
    (7, None, [
        '"\'Praise them, praise them, and make them open their heart.\' The word for heart or mind is " Watch for ',
        (None, "心。"),
        ", and ",
        (None, "開かせろ。"),
        " turns the word for open into a command meaning 'make them open up!'"
    ]),
    (8, None, [
        '"\'Using as formal language as possible, mind you.\' Looking closely, the word for \'as much as possible\' is " Hear how ',
        (None, "なるべく。"),
        ", paired with ",
        (None, "丁寧な言葉。"),
        ", formal words."
    ]),
    (10, None, [
        '"\'Embarrassing as it is, English is my weak point.\' Funny irony: Muranishi calls English " It features ',
        (None, "イングリッシュ。"),
        " while admitting it is ",
        (None, "苦手。"),
        ", the word for something you are bad at or uncomfortable with."
    ]),
    (11, '難しく考えるな。', [
        '"\'Do not overthink it.\' Changing the word for difficult to " Pay attention to ',
        (None, "難しく。"),
        " before ",
        (None, "考えるな。"),
        ", do not think, literally says 'do not think difficultly'—'do not overcomplicate it!'"
    ]),
    (11, '何でもいいから単語を言えばいいんだよ。', [
        '"\'Just say any single words at all.\' The word for \'anything is fine\' is " Hear how ',
        (None, "何でもいい。"),
        ", and ",
        (None, "単語。"),
        " means individual vocabulary words rather than full sentences."
    ]),
]

TRANSITION = "Now let's hear Ono's whole sales-talk secret again."

OUTRO = (
    "Hold on to the word for motivation, the word to say you are not good at something, "
    "and the phrase to use whenever anything will do. "
    "Let's see Muranishi test this advice at a giant mansion next."
)

CLOSING = ('ono', 'また明日。')
