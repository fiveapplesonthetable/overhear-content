ID = 'hidamari-ryokan-s01e01-scene-05'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = '私の服じゃない！  (Not My Clothes!)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kazuko': '和子', 'mio': '美央', 'kenji': '健二'}

INTRO = "Two minutes after heading upstairs, Room 4's buzzer rings at the desk—four times in a row instead of twice. Mio hurries up to find Kazuko and Kenji staring into the open suitcase. Listen first."

STORY = [
    ('mio', '和子さん、大丈夫ですか？ベルが鳴りましたが！', 'Kazuko, is everything alright? You rang the bell!'),
    ('kazuko', '美央さん、このスーツケースの中を見てください！私の鞄じゃありません！', 'Mio, please look inside this suitcase! It is not my bag!'),
    ('mio', 'えっ、でも外側は同じ濃い青ですよ！', 'Wait, yet the outside is the exact same dark blue!'),
    ('kazuko', '外側はそっくりです！でも中を見てください！', 'The outside looks identical! Still, look inside!'),
    ('kenji', '大きな茶色い紳士靴が二足と、灰色のセーターだな。', "Two pairs of big brown men's shoes and grey sweaters."),
    ('mio', '白い紙に包まれているのは何ですか？小さな木の汽車です！', 'And what is this wrapped in white paper? It is a small wooden train!'),
    ('kazuko', '私は二十八センチの靴なんて履きませんわ！', 'I certainly do not wear twenty-eight centimetre shoes!'),
    ('kenji', '通りで重かったわけだ。木と革だからね！', 'No wonder it was so heavy. Wood and leather!'),
    ('kazuko', '駅で誰かが間違えて私の青いスーツケースを持って行ったんです！', 'Someone at the station took my blue suitcase by mistake!'),
    ('mio', 'どうぞ座ってください、和子さん。今すぐ名札を確認しましょう。', "Please sit down, Kazuko. Let's check the luggage tag right away."),
    ('kenji', '横の持ち手に小さな紙の札が付いているぞ。', 'There is a small paper tag tied to the side handle.'),
    ('kazuko', 'まあ、下の明るい所へ持って行きましょう！', "Oh, let's bring it downstairs into the bright light!"),
]

OPENER = "The mystery begins in Room 4 with colours, materials, and Japanese shoe sizes. Let's examine the key lines."

WALK = [
    (0, None, ["'Kazuko, is everything alright? You rang the bell!' One word you will hear constantly in Japanese is ", (None, '大丈夫'), ", an all-purpose check meaning 'alright', 'safe', or 'okay'."]),
    (1, None, ["'Mio, please look inside this suitcase! It is not my bag!' Saying ", (None, '見てください'), ' makes a polite request to look, and ', (None, 'じゃありません'), " cleanly says 'is not'."]),
    (5, None, ["'And what is this wrapped in white paper? It is a small wooden train!' Notice the colours and materials: ", (None, '白い紙'), " means 'white paper', while ", (None, '木の汽車'), " links 'wood' to an old-fashioned train locomotive."]),
    (6, None, ["'I certainly do not wear twenty-eight centimetre shoes!' Japanese shoe sizes measure foot length directly in centimetres, so ", (None, '二十八センチ'), " is a large men's shoe, paired with ", (None, '履きません'), ' from the word for putting on footwear.']),
    (8, None, ["'Someone at the station took my blue suitcase by mistake!' Listen for ", (None, '駅'), ", meaning 'train station', and ", (None, '間違えて'), ", which means 'by mistake' or 'mixing things up'."]),
    (9, None, ["'Please sit down, Kazuko. Let's check the luggage tag right away.' Mio calms her guest with ", (None, '座ってください'), ", 'please sit down', and ", (None, '今すぐ'), " for 'right away'."]),
]

TRANSITION = "Now let's replay the whole Room 4 surprise from start to finish."

OUTRO = "Instead of dresses and sheet music, the blue suitcase holds twenty-eight centimetre brown shoes and a wooden train. Let's see what is written on that tag next time."

CLOSING = ('mio', 'また明日！')
