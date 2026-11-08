# Authoring module for linden-courtyard-ja-s01e06-scene-08.
ID = 'linden-courtyard-ja-s01e06-scene-08'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 6
SCENE = 8
TITLE = 'Room Nine  (九号室)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = 'カフェ用の予備の椅子を地下室に取りに行ったグレアムは、古いれんが壁の奥から鍵のかかった木箱を見つけます。箱には九号室と刻まれていて、なんと九本目の真鍮の鍵まで付いていました。英語の会話に耳を傾けましょう。'
OPENER = 'では、謎めいたこの発見の場面を順番に読み進めていきます。'
TRANSITION = 'それでは、ハラハラする場面全体をもう一度通しで聴いてみましょう。'
OUTRO = '八部屋しかないはずの宿に、九号室の秘密が隠されていました。懐中電灯を手に、ハンナの二週目が今まさに始まります。'
CLOSING = ('graham', 'Until tomorrow!')
STORY = [
    ('hannah', 'Did you find the three folding chairs behind the boiler room, Graham?', 'ボイラー室の裏で、折りたたみ椅子を三脚見つけた、グレアム？'),
    ('graham', 'Found the chairs, and behind an old brick wall, I found this.', '椅子は見つけたよ。それと、古いれんが壁の奥でこれを見つけたんだ。'),
    ('arthur', 'A small cedar chest? I have never seen that box in fifteen years!', '小さな杉の箱？この十五年、あんな箱は一度も見たことがないぞ！'),
    ('hannah', 'Brush the dust off the brass plate on top... wait, read that number!', '上の真鍮の板のほこりを払って…待って、その番号を読んで！'),
    ('arthur', "Let me pull my glasses down from my forehead... 'Room Nine'?!", '額の眼鏡を下ろさせてくれ…「九号室」だって？！'),
    ('hannah', 'Graham, look at the wooden key board behind us: one, two, three, four, five, six, seven, eight!', 'グレアム、後ろの木の鍵掛けを見て。一、二、三、四、五、六、七、八！'),
    ('arthur', 'This guesthouse has only ever had eight rooms! Where on earth is Room Nine?!', 'この宿には昔から八部屋しかないんだ！九号室なんて一体どこにあるんだ？！'),
    ('graham', 'Listen when I tilt the box. Something metal just slid inside.', '箱を傾けたときの音を聞いてくれ。今、中で金属の何かが滑ったぞ。'),
    ('hannah', 'There is a tiny keyhole on the front latch, and look taped underneath: an old brass key!', '前の留め金に小さな鍵穴があるわ。それに下にテープで貼ってあるのは、古い真鍮の鍵よ！'),
    ('arthur', 'A ninth brass key?! Do we open it tonight or wait until morning?!', '九本目の真鍮の鍵だって？！今夜開けるか、朝まで待つか？！'),
    ('graham', 'Look at the folded blueprint sticking out of the hinge. There is a hidden door drawn on this floor!', '蝶番からはみ出している折りたたまれた設計図を見てくれ。この階に隠し扉が描いてある！'),
    ('hannah', 'Grab the flashlight, both of you. My second week starts right now!', '二人とも懐中電灯を持って。私の二週目は今から始まるのよ！'),
]
WALK = [
    (0, None, ["'ボイラー室の裏で、折りたたみ椅子を三脚見つけた、グレアム？' 椅子の種類を表す", (None, 'folding chairs'), 'では、動詞に進行形の語尾を付けた形が用途を示す形容詞として働いています。']),
    (1, None, ["'椅子は見つけたよ。それと、古いれんが壁の奥でこれを見つけたんだ。' 会話らしく主語を省いた", (None, 'Found the chairs'), 'という省略の後に続き、', (None, 'behind an old brick wall'), 'では素材の名詞がそのまま形容詞のように使われています。']),
    (2, None, ["'小さな杉の箱？この十五年、あんな箱は一度も見たことがないぞ！' 経験の否定を表す", (None, 'I have never seen that box in fifteen years'), 'は現在完了です。期間を表す前置詞が“中に”になる点に注目しましょう。']),
    (3, None, ["'上の真鍮の板のほこりを払って…待って、その番号を読んで！' 表面の汚れを払い落とす", (None, 'Brush the dust off'), 'では、“ブラシ”が動詞として使われ、“離れて”の語で取り除く動きを示します。']),
    (4, None, ["'額の眼鏡を下ろさせてくれ…「九号室」だって？！' 許可を求める決まり文句の", (None, 'Let me pull my glasses down'), 'は、「〜させて」の使役動詞の後に動詞の原形が続く形です。']),
    (5, None, ["'グレアム、後ろの木の鍵掛けを見て。一、二、三、四、五、六、七、八！' 鍵を掛けておく板を指す", (None, 'the wooden key board'), 'は、名詞を二つ並べて一つの物を表す複合名詞です。“木の”は素材を表す形容詞です。']),
    (6, None, ["'この宿には昔から八部屋しかないんだ！九号室なんて一体どこにあるんだ？！' 強調の", (None, 'has only ever had eight rooms'), 'は「今までに一度も」の副詞で範囲を強めています。驚きの', (None, 'Where on earth'), 'も覚えておきましょう。']),
    (7, None, ["'箱を傾けたときの音を聞いてくれ。今、中で金属の何かが滑ったぞ。' 物を斜めにする動作の", (None, 'when I tilt the box'), 'という時を表す節に続いて、', (None, 'Something metal'), 'では形容詞的な名詞が後ろから修飾しています。']),
    (8, None, ["'前の留め金に小さな鍵穴があるわ。それに下にテープで貼ってあるのは、古い真鍮の鍵よ！' とても小さいことを表す", (None, 'a tiny keyhole'), 'の形容詞は“小さい”より強い響きです。続く', (None, 'taped underneath'), 'では名詞がそのまま動詞として使われています。']),
    (9, None, ["'九本目の真鍮の鍵だって？！今夜開けるか、朝まで待つか？！' 選択を迫る", (None, 'Do we open it tonight or wait until morning'), 'は、接続詞で二つの行動を並べた疑問文です。期限を表す前置詞の使い方にも注目しましょう。']),
    (10, None, ["'蝶番からはみ出している折りたたまれた設計図を見てくれ。この階に隠し扉が描いてある！' 突き出ている様子の", (None, 'sticking out of the hinge'), 'は句動詞の進行形です。受け身の', (None, 'a hidden door drawn on this floor'), 'では、過去分詞が名詞を後ろから説明しています。']),
    (11, None, ["'二人とも懐中電灯を持って。私の二週目は今から始まるのよ！' 素早くつかむ動作の", (None, 'Grab the flashlight'), 'は、ただ取るより勢いのある動詞です。続く', (None, 'starts right now'), 'の“ちょうど”は時間をぴったり強調しています。']),
]
