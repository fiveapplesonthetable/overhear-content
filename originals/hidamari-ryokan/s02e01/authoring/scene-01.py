ID = 'hidamari-ryokan-s02e01-scene-01'
SHOW = 'hidamari-ryokan'
SEASON = 2
EPISODE = 1
SCENE = 1
TITLE = '九本目の鍵  (The Ninth Key)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'kenji': '健二', 'takashi': '隆'}

INTRO = "It is early Saturday morning at the Hidamari Inn in Osaka, just hours after Kenji carried a dusty cedar box stamped 'Room 9' up from the cellar. Mio and Takashi lean over the front desk as Kenji turns the tiny brass key. Listen to the scene first."

STORY = [
    ('takashi', '健二さん、小さい鍵をゆっくり回してください。胸がドキドキします！', 'Kenji, please turn the small key slowly. My heart is pounding!'),
    ('kenji', '落ち着いてよ、隆さん。地下室の古い真鍮の鍵は、絶対に壊れないよ。', 'Relax, Takashi. An old brass lock from the cellar never breaks.'),
    ('mio', 'カチッと鳴りました！健二さん、木のふたを開けてください！', 'It clicked! Kenji, please open the wooden lid!'),
    ('kenji', '中には……大きいドアの鍵が一本、青い図面、それからハガキだ。', "Inside there's... one big door key, a blue plan, and postcards."),
    ('takashi', 'その青い紙の一番上を読みたいです！私の眼鏡はどこですか？', 'I want to read the top of that blue paper! Where are my glasses?'),
    ('mio', 'まだおでこの上ですよ、隆さん。昨日の夜と同じ場所です。', 'Still on your forehead, Takashi. The same place as last night.'),
    ('takashi', 'あった！ほら、「一階、九号室、庭のサンルーム」！', "Found them! Look: 'Ground floor, Room Nine, garden sunroom'!"),
    ('mio', 'えっ、一階に庭のサンルームがあるんですか！？', "Wait, there's a garden sunroom on the ground floor?!"),
    ('kenji', '見ろ。裏の廊下の本棚の後ろに、矢印がある。', "Look. There's an arrow behind the bookcase in the back hallway."),
    ('takashi', 'あの重い木の本棚は、二十年ずっとあの壁の前にありますよ！', 'That heavy wooden bookcase has stood against that wall for twenty years!'),
    ('mio', 'じゃあ、古い本の後ろに九番目のドアがあるんですね！', "Then behind those old books, there's a ninth door!"),
    ('kenji', 'まずコーヒーを一口飲もう。それから本を動かすぞ。', 'First, one sip of coffee. Then we move the books.'),
]

OPENER = 'A cedar box, a brass key and a lost pair of glasses: six lines to walk through, full of small useful words.'

WALK = [
    (0, None, ["'Kenji, please turn the small key slowly. My heart is pounding!' Japanese hears a racing heart as ", (None, 'ドキドキします'), ', a sound word for the thump-thump, and ', (None, 'ゆっくり'), " means 'slowly', the perfect word for a nervous owner."]),
    (1, None, ["'Relax, Takashi. An old brass lock from the cellar never breaks.' Kenji's ", (None, '絶対に'), " means 'absolutely'. Put it before a 'not' ending and it becomes a firm 'never'."]),
    (2, None, ["'It clicked! Kenji, please open the wooden lid!' Mio hears the lock go ", (None, 'カチッと'), ', the Japanese sound of a click. The word for the lid of a box is ', (None, 'ふた'), '.']),
    (3, None, ["'Inside there's... one big door key, a blue plan, and postcards.' Counting one key uses ", (None, '一本'), '. Japanese counts long, thin things like keys, pens and bottles with this little counter.']),
    (5, None, ["'Still on your forehead, Takashi. The same place as last night.' Mio's ", (None, 'まだ'), " is the tiny word for 'still', and glasses still sitting on a forehead are the oldest joke at this inn."]),
    (10, None, ["'Then behind those old books, there's a ninth door!' Add ", (None, '九番目'), " to your number words: the ending turns nine into 'ninth'. And ", (None, '後ろ'), " is the everyday word for 'behind'."]),
]

TRANSITION = "Now let's hear the whole box opening again from start to finish."

OUTRO = "Inside the cedar box sits a heavy door key and a floor plan pointing straight behind the hallway bookcase. Don't worry if a word or two went past quickly; they return right away. See you next time."

CLOSING = ('mio', 'また明日！')
