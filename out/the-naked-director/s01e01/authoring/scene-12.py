ID = 'the-naked-director-s01e01-scene-12'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 12
TITLE = 'すごい家ですね  (What an Amazing House)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'muranishi': '村西', 'okusama': '中井の妻', 'nakai': '中井'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Putting Ono's advice into action right away, Muranishi stops outside the grandest house in the neighborhood. "
    "He showers the lady of the house with compliments and English loanwords—until her intimidating husband Nakai steps out and orders him inside. "
    "Listen to how flattery opens the gate."
)

STORY = [
    ('muranishi', 'すごい家ですね。', 'What an amazing house.', [(214, 'すごい家ですね')], ''),
    ('okusama', '何よ？', 'What do you want?', [(217, '何よ')], ''),
    ('muranishi', 'あまりにビューティフォーだったので驚いてしまいました。', 'You were so beautiful that I was completely startled.', [(218, 'あまりに ビューティフォーだったので'), (219, '驚いてしまいました')], ''),
    ('okusama', 'お上手ね。でもセールスなら結構ですから。', 'Smooth talker. But if it is sales, no thank you.', [(220, 'お上手ね でもセールスなら結構ですから')], ''),
    ('muranishi', 'いやあ、それは残念ですね。', 'Oh my, that is a shame.', [(221, 'いやあ それは残念ですね')], ''),
    ('muranishi', 'スペシャルな商品なんですが。', 'Even though it is a very special product.', [(224, 'スペシャルな商品なんですが')], ''),
    ('okusama', 'どんな商品なの？', 'What kind of product is it?', [(225, 'どんな商品なの')], ''),
    ('muranishi', '少しだけお話を聞いていただけますか？', 'Could you listen to me for just a little moment?', [(226, '少しだけ お話 聞いていただけますか')], 'Added を after お話 for clarity.'),
    ('nakai', 'どうしたの？俺にも聞かせてくれよ。', 'What is going on? Let me hear it too.', [(227, 'どうしたの'), (229, '俺にも')], 'Standardised 聞かしてくれよ to 聞かせてくれよ.'),
    ('nakai', '早く入れよ！', 'Hurry up and get inside!', [(232, '早く入れよ')], ''),
    ('nakai', 'どんな特別な商品なんだよ？', 'Just what kind of special product is this?', [(236, 'どんな特別な商品なんだよ')], ''),
    ('muranishi', '英会話教材です。', 'It is an English conversation course.', [(237, '英会話教材です')], ''),
]

OPENER = "Notice how Muranishi mixes humble requests with playful katakana English, while Nakai barks gruff commands. Let's walk through it."

WALK = [
    (0, None, [
        '"\'What an amazing house.\' Looking at the first part, the word for amazing is " Here, the word ',
        (None, "すごい。"),
        ", ",
        (None, "家。"),
        " is house, and ",
        (None, "ですね。"),
        " invites agreement as he stares up at the gate."
    ]),
    (2, None, [
        '"\'You were so beautiful that I was completely startled.\' Following Ono\'s tip, Muranishi drops English \'beautiful\' as " They are saying ',
        (None, "ビューティフォー。"),
        "! At the end, ",
        (None, "驚いてしまいました。"),
        " adds a suffix onto the verb for surprise, showing the reaction slipped out unintentionally."
    ]),
    (3, 'お上手ね。', [
        '"\'Smooth talker.\' Literally, the word for skillful is " They are saying ',
        (None, "お上手。"),
        "—and when someone replies ",
        (None, "お上手ね。"),
        " to a compliment, it playfully means 'oh, you flatterer!'"
    ]),
    (4, None, [
        '"\'Oh my, that is a shame.\' In this situation, the word for a pity is " The phrase contains ',
        (None, "残念。"),
        ", which means regrettable. Saying ",
        (None, "それは残念ですね。"),
        " sounds sympathetic rather than pushy when someone turns you down."
    ]),
    (5, None, [
        '"\'Even though it is a very special product.\' As a salesman, the word for product is " Notice how ',
        (None, "商品。"),
        ", meaning commercial product. Leaving ",
        (None, "ですが。"),
        ", 'it is, however...', dangling at the end tempts her curiosity without finishing the sentence."
    ]),
    (6, None, [
        '"\'What kind of product is it?\' Here, the word for \'what kind of\' is " In this line, ',
        (None, "どんな。"),
        ", right before ",
        (None, "商品。"),
        ", and feminine ",
        (None, "なの。"),
        " turns the question warm and curious—she took the bait!"
    ]),
    (7, None, [
        '"\'Could you listen to me for just a little moment?\' Built from " Notice how ',
        (None, "少し。"),
        ", a little, plus ",
        (None, "だけ。"),
        ", only, this phrase softens his request before polite ",
        (None, "聞いていただけますか。"),
        ", 'could I humbly receive your listening?'"
    ]),
    (8, 'どうしたの？', [
        '"\'What is going on?\' Even a tough boss asks his wife " Watch for ',
        (None, "どうした。"),
        ", what happened, softened with rising ",
        (None, "の。"),
        " to ask 'what is the matter?'"
    ]),
    (9, None, [
        '"\'Hurry up and get inside!\' In his barking command, the word for quickly is " We can hear ',
        (None, "早く。"),
        ", and ",
        (None, "入れよ。"),
        " turns the verb to enter into an order nobody dares refuse."
    ]),
    (11, None, [
        '"\'It is an English conversation course.\' The word for this is " Here, the word ',
        (None, "英会話。"),
        ", which fuses the word for English with conversation, and ",
        (None, "教材。"),
        " means study materials."
    ]),
]

TRANSITION = "Now let's listen to the whole encounter at Nakai's gate again."

OUTRO = (
    "You heard the sympathetic phrase for 'that is a shame', the question word for 'what kind of', "
    "and the phrase to ask what is going on—all while Muranishi realizes he just walked into a lion's den. "
    "See you inside the mansion next."
)

CLOSING = ('okusama', 'さようなら。')
