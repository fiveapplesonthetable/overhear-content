ID = 'the-naked-director-s01e02-scene-05'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = '三十八号店の開店  (Thirty-Eighth Branch Opening)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kitamori': '北森', 'tayama': '田山', 'muranishi': '村西'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "Muranishi's chain grows at breakneck speed, reaching its thirty-eighth branch in Sapporo. "
    "Inside the new shop, Kitamori and freshly promoted manager Tayama welcome customers while Muranishi cheers Tayama on. "
    "Let's listen to the Japanese first without worrying about every word."
)

STORY = [
    ('kitamori', 'どうもありがとうございました。', 'Thank you very much.', [(86, 'どうも ありがとうございました')], ''),
    ('kitamori', '次のお二人様、どうぞ。', 'Next party of two, please come ahead.', [(87, '次のお二人様 どうぞ')], ''),
    ('tayama', 'どうも、いらっしゃいませ。', 'Hello, welcome to our store.', [(88, 'どうも いらっしゃいませ')], ''),
    ('tayama', 'この辺でいいですかね？', 'Are these alright around here?', [(89, 'この辺でいいですかね')], ''),
    ('muranishi', 'うん、いいんじゃないか？', 'Yeah, does that not look good?', [(90, 'うん いいんじゃないか')], ''),
    ('muranishi', '頼むよ、田山店長。', 'I am counting on you, Manager Tayama.', [(90, '頼むよ 田山店長')], ''),
    ('muranishi', 'たくさん売って利益あげてね。', 'Sell plenty and bring up the profits.', [(91, 'たくさん売って利益あげてね')], ''),
    ('tayama', '頑張ります！', 'I will do my very best!', [(93, '頑張ります')], ''),
    ('tayama', '今、オープン記念で新作が割引になってます。', 'Right now, new releases are discounted for our grand opening.', [(96, '今 オープン記念で 新作が'), (96, '割引になってます')], 'Removed percentage symbol for clean kanji/kana text.'),
    ('tayama', 'よかったらどうぞ。', 'Please take a look if you like.', [(98, 'よかったら どうぞ')], ''),
    ('tayama', 'すぐ入れますから！', 'You can get right in!', [(99, 'すぐ入れますから')], ''),
]

OPENER = "This short scene is packed with real-world Japanese shop greetings and workplace encouragement. Let's hear each piece up close."

WALK = [
    (0, None, "'Thank you very much.' Shop staff use past-tense \"arigatou gozaimashita\" as a customer finishes paying and steps away, thanking them for the completed visit."),
    (1, None, "'Next party of two, please come ahead.' \"Futari\" counts two people using native Japanese numbers, wrapped in polite \"o\" and \"sama\"—the exact greeting you hear at restaurants and shops."),
    (2, None, "'Hello, welcome to our store.' \"Irasshaimase\" is the unmistakable call that greets you the instant you step into any Japanese shop, café, or market."),
    (3, None, "'Are these alright around here?' \"Kono hen\" means around this spot, handy for pointing at an approximate area on a shelf or a map."),
    (5, None, "'I am counting on you, Manager Tayama.' Casual \"tanomu\" means 'I ask of you' or 'counting on you'. Placing job title \"tenchou\", store manager, right after the surname works just like 'Manager Tayama'."),
    (6, None, "'Sell plenty and bring up the profits.' Linking \"utte\", sell and, from \"uru\", into \"rieki\", profit, shows how the \"te\" form chains two actions smoothly together."),
    (7, None, "'I will do my very best!' \"Ganbarimasu\" is Japan's favorite workplace pledge—promising steady effort rather than guaranteeing luck."),
    (8, None, "'Right now, new releases are discounted for our grand opening.' \"Kinen\" means commemoration or celebration, and \"waribiki\" literally splits off a fraction of the price: a discount."),
    (9, None, "'Please take a look if you like.' Starting with \"yokattara\", 'if it is good for you', takes all pressure off an offer before \"douzo\"."),
    (10, None, "'You can get right in!' \"Sugu\" means right away, and \"hairemasu\" turns \"hairu\", to enter, into 'can enter', ending with \"kara\" to give a friendly reason to step inside."),
]

TRANSITION = "Now let's hear the grand-opening scene again from start to finish."

OUTRO = (
    "Notice the difference between \"irasshaimase\" when a customer walks in and past-tense \"arigatou gozaimashita\" as they head out the door. "
    "See you next time."
)

CLOSING = ('tayama', 'またね！')
