# Authoring module for linden-courtyard-ja-s01e03-scene-02.
ID = 'linden-courtyard-ja-s01e03-scene-02'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = 'The Sunny Attic  (日の当たる屋根裏部屋)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '三階まで上がったハンナ、グレアム、テッサの三人は、中庭を見下ろす静かな屋根裏部屋の扉を開けました。部屋を見回しながら、お客さんを迎えるのに足りないものを一つずつ数えていきます。耳を澄ませて、場面全体を英語で聴いてください。'
OPENER = 'では、屋根裏部屋での三人の会話を、順番に詳しく見ていきましょう。'
TRANSITION = 'それでは、屋根裏のやり取りを通しでもう一度聴いてみましょう。'
OUTRO = '足りないものの目星がつき、三人は古い段ボール箱を抱えて階段を下りていきます。次の場面では、いよいよ部屋の仕上げに取りかかります。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('hannah', 'Oh, look at this room! Big wooden beams and a window over the courtyard!', 'まあ、この部屋を見て！太い木の梁に、中庭を見下ろす窓まであるわ！'),
    ('tessa', 'Listen to the rain on the roof. It feels so cozy up here!', '屋根に当たる雨の音を聞いて。ここはすごく居心地がいいわね！'),
    ('graham', 'Dry, warm, and quiet. Now tell me what is missing.', '乾いていて、暖かくて、静かだ。さあ、何が足りないか言ってくれ。'),
    ('hannah', 'Okay: there is a bed, a table, and a chair, but no bedside lamp.', 'ええと、ベッドとテーブルと椅子はあるけど、枕元のランプがないわ。'),
    ('tessa', 'And no mirror on the wall, and the floor feels bare without a rug.', 'それに壁に鏡もないし、ラグがないと床が殺風景に感じるわ。'),
    ('graham', 'There is a brass reading lamp in my workshop downstairs.', '下の作業場に、真鍮の読書用ランプがあるよ。'),
    ('tessa', 'And I have two soft pillows and a woven blue rug in the closet!', 'それに私、戸棚にふかふかの枕を二つと、青い織物のラグを持ってるの！'),
    ('hannah', 'What about the small bathroom next door? Does the light work?', '隣の小さなお風呂場はどう？電気はつくの？'),
    ('graham', 'New bulb last week, clean soap, plenty of hot water.', '電球は先週新しくしたし、石けんも新品、お湯もたっぷり出る。'),
    ('tessa', 'Give us fifteen minutes and this attic will beat room seven!', '十五分ちょうだい。そうしたらこの屋根裏、七号室にも負けないわよ！'),
    ('hannah', 'Grab those cardboard boxes, Graham. Down the stairs we go!', 'その段ボール箱を持って、グレアム。さあ、階段を下りるわよ！'),
    ('graham', 'Careful on the turn, do not bump the wall!', '曲がり角に気をつけて、壁にぶつけるなよ！'),
]
WALK = [
    (0, None, ["'まあ、この部屋を見て！太い木の梁に、中庭を見下ろす窓まであるわ！' 驚いて注意を引くときは", (None, 'look at this room'), 'と言います。窓の位置は', (None, 'over the courtyard'), 'で表し、上から見下ろす位置関係が伝わります。']),
    (1, None, ["'屋根に当たる雨の音を聞いて。ここはすごく居心地がいいわね！' 耳を傾ける動作は", (None, 'Listen to the rain'), 'のように前置詞を伴います。また', (None, 'cozy'), 'は暖かくくつろげる空間を表す人気の形容詞です。']),
    (2, None, ["'乾いていて、暖かくて、静かだ。さあ、何が足りないか言ってくれ。' 文の中に組み込まれた疑問", (None, 'what is missing'), 'は、主語を尋ねる形なのでそのままの語順になります。']),
    (3, None, ["'ええと、ベッドとテーブルと椅子はあるけど、枕元のランプがないわ。' 存在を述べる", (None, 'there is a bed'), 'に対し、ないものは名詞の前に否定語を付けて', (None, 'no bedside lamp'), 'と簡潔に言えます。']),
    (4, None, ["'それに壁に鏡もないし、ラグがないと床が殺風景に感じるわ。' 見た目の印象を伝える", (None, 'the floor feels bare'), 'では、感じるという動詞の後に形容詞をそのまま続けます。さらに', (None, 'without a rug'), 'で条件を添えています。']),
    (5, None, ["'下の作業場に、真鍮の読書用ランプがあるよ。' 素材と用途を重ねた", (None, 'a brass reading lamp'), 'は、名詞を前から修飾する英語らしい形です。', (None, 'downstairs'), 'は一語で場所を表す副詞です。']),
    (6, None, ["'それに私、戸棚にふかふかの枕を二つと、青い織物のラグを持ってるの！' 柔らかさを表す", (None, 'two soft pillows'), 'に加えて、もう一つの品として', (None, 'a woven blue rug'), 'では作り方を表す過去分詞が形容詞として使われています。']),
    (7, None, ["'隣の小さなお風呂場はどう？電気はつくの？' 話題を切り替えて尋ねる", (None, 'What about'), 'の後には名詞を置きます。機械や設備が正常に動くかどうかは', (None, 'Does the light work'), 'のように動くという意味の動詞で聞きます。']),
    (8, None, ["'電球は先週新しくしたし、石けんも新品、お湯もたっぷり出る。' 動詞を省いた報告調で", (None, 'New bulb last week'), 'と並べています。量の多さは', (None, 'plenty of hot water'), 'という決まった言い方で表します。']),
    (9, None, ["'十五分ちょうだい。そうしたらこの屋根裏、七号室にも負けないわよ！' 命令文と接続詞を組み合わせると、そうすればという意味になります。", (None, 'will beat room seven'), 'の動詞は、試合だけでなく比べて上回る意味でも使われます。']),
    (10, None, ["'その段ボール箱を持って、グレアム。さあ、階段を下りるわよ！' さっとつかむ動作を表す", (None, 'Grab those cardboard boxes'), 'という命令に続いて、', (None, 'Down the stairs we go'), 'は方向を文頭に出した弾むような言い方です。']),
    (11, None, ["'曲がり角に気をつけて、壁にぶつけるなよ！' 注意を促す", (None, 'Careful on the turn'), 'は形容詞だけで始まる口語的な形です。うっかりぶつかる意味の', (None, 'do not bump the wall'), 'で、否定の命令文になっています。']),
]
