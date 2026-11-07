ID = 'hidamari-ryokan-s02e01-scene-07'
SHOW = 'hidamari-ryokan'
SEASON = 2
EPISODE = 1
SCENE = 7
TITLE = 'お金を数えて  (Count the Coins)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'takashi': '隆', 'mio': '美央', 'yuka': '由香'}

INTRO = 'At the front desk, Takashi is adding numbers on a notepad with a worried frown when Mio and Yuka show him the thirty-year-old courtyard postcard. Listen first.'

STORY = [
    ('takashi', 'この古い写真は大好きです。でも、新しいカフェの家具はとても高いですよ！', 'I really love this old photo. But new café furniture is very expensive!'),
    ('mio', '隆さん、高い新しい家具を買うなんて、誰が言いましたか？', 'Takashi, who said anything about buying expensive new furniture?'),
    ('yuka', '地下室に木のテーブルが四つあるし、上には白いテーブルクロスもあるよ。', 'There are four wooden tables in the cellar, and white tablecloths upstairs too.'),
    ('takashi', '椅子は？カップは？雨戸の緑のペンキや、温かい壁のランプは？', 'What about chairs? Cups? Green paint for the shutters, and warm wall lamps?'),
    ('mio', '私のリストを見てください。緑のペンキが二缶、カップが十二個、市場のレモンです。', 'Look at my list. Two cans of green paint, twelve cups, and lemons from the market.'),
    ('yuka', 'それに、陽翔さんと大輝さんが、テーブル運びを無料で手伝ってくれるって！', "And Haruto and Daiki say they'll help carry the tables for free!"),
    ('takashi', 'ちょっと待って……もう一度、数字を確認します。部屋全部で、これだけですか！？', 'Hold on... let me check the numbers again. Only this much for the whole room?!'),
    ('mio', '今週は、客室が全部満室です、隆さん。今日、現金で払えますよ。', 'Every guest room is full this week, Takashi. We can pay in cash today.'),
    ('takashi', 'それに、市は月末までにカフェが開くのを見たいんです！', 'And the city wants to see the café open by the end of the month!'),
    ('yuka', '隆さん、「はい」って言って！また眼鏡をなくす前に！', 'Say yes, Takashi! Before you lose your glasses again!'),
    ('takashi', 'わかりました、はい！九号室は、来週の金曜日の六時にオープンです！', 'All right, yes! Room Nine opens next Friday at six!'),
    ('mio', 'やった！サンルームの天井のランプを試しに行きましょう！', "Hooray! Let's go and test the ceiling lamp in the sunroom!"),
]

OPENER = "Money talk at the front desk: prices, counters and cash. Let's walk through six lines."

WALK = [
    (0, None, ["'I really love this old photo. But new café furniture is very expensive!' Takashi's worry word is ", (None, '高い'), ". It means 'tall' for trees, and 'expensive' for things like ", (None, '家具'), ', the word for furniture.']),
    (4, None, ["'Look at my list. Two cans of green paint, twelve cups, and lemons from the market.' Japanese counts with little helper words: ", (None, '二缶'), " is 'two cans', while ", (None, '十二個'), ' uses the all-purpose counter for small objects.']),
    (5, None, ["'And Haruto and Daiki say they'll help carry the tables for free!' The word for 'free of charge' is ", (None, '無料'), ", built from 'no' and 'fee'. You'll see it on signs all over the city."]),
    (6, None, ["'Hold on... let me check the numbers again. Only this much for the whole room?!' Shocked by the small total, Takashi asks ", (None, 'これだけ'), ", 'this' plus 'only': 'only this much?'"]),
    (7, None, ["'Every guest room is full this week, Takashi. We can pay in cash today.' Hotel signs say ", (None, '満室'), ", 'full rooms', meaning no vacancies. And ", (None, '現金'), ", literally 'present money', is cash."]),
    (9, None, ["'Say yes, Takashi! Before you lose your glasses again!' Yuka teases him with ", (None, 'なくす前に'), ": put 'before' after a plain action, and it means 'before you lose them'."]),
]

TRANSITION = "Now let's hear the whole budget talk again from beginning to end."

OUTRO = "With a practical budget and full guest rooms upstairs, Takashi gives the green light for Friday at six. One last scene for Episode 1, so let's listen."

CLOSING = ('takashi', 'また明日！')
