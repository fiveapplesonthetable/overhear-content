# Authoring module for linden-courtyard-ja-s01e05-scene-01.
ID = 'linden-courtyard-ja-s01e05-scene-01'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Truth in the Courtyard  (中庭で明かされた真実)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'evelyn': 'Evelyn'}
INTRO = '金曜日の朝、宿の中庭でケイレブがイヴリンとハンナに打ち明けます。月曜日の列車でうっかりイヴリンのスーツケースを持ち帰ってしまったこと、そして門の前で兄の姿を見かけて慌ててしまったこと。まずは場面全体を英語で聴いてみましょう。'
OPENER = 'では、ケイレブの正直な告白を一行ずつ丁寧にたどっていきましょう。'
TRANSITION = 'それでは、もう一度この場面を自然な速さで通して聴いてみましょう。'
OUTRO = 'そっくりな青いスーツケースの謎がようやく解けました。残るのは、ケイレブと兄オーウェンの間にある古いわだかまりです。次はフロントでの場面に進みます。ではまたすぐに。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('evelyn', 'Let me look at you properly, Caleb! You grew taller than the piano!', 'よく顔を見せてちょうだい、ケイレブ！ピアノより背が高くなったのね！'),
    ('caleb', 'I cannot believe you are staying in the exact same guesthouse, Miss Evelyn.', 'まさか全く同じ宿に泊まっていらっしゃるなんて、信じられません、イヴリン先生。'),
    ('hannah', 'Wait, so we rode the same train on Monday, and you took her suitcase?', '待って、じゃあ月曜日に私たちは同じ列車に乗っていて、あなたが彼女のスーツケースを持っていったの？'),
    ('caleb', "By complete accident! At my cousin's apartment I opened it and saw sheet music and a red ribbon.", 'まったくの偶然なんです！いとこのアパートで開けてみたら、楽譜と赤いリボンが入っていました。'),
    ('evelyn', 'Why did you leave my bag on the step at night and run away?', 'どうして夜中に私の鞄を石段に置いて、走って逃げてしまったの？'),
    ('caleb', 'Because when I walked here on Monday evening, I saw my older brother walking down this street!', '月曜日の夕方ここへ歩いてきたとき、兄がこの通りを歩いているのを見かけたからです！'),
    ('hannah', 'Your older brother lives here in Portland?', 'お兄さんがここポートランドに住んでいるんですか？'),
    ('caleb', 'Yes. I panicked, rang your bell, and slipped the Friday note onto the handle.', 'はい。慌ててしまって、ベルを鳴らし、金曜日のメモを取っ手に差し込みました。'),
    ('evelyn', 'Wait, and Wednesday night you checked in here under your real name?', '待って、それで水曜日の夜には本名でここにチェックインしたの？'),
    ('caleb', 'I needed a quiet place nearby before Friday, and honestly forgot you still had my bag!', '金曜日の前に近くで静かな場所が必要だったんです。正直、僕の鞄をまだ預かってもらっていることを忘れていました！'),
    ('hannah', 'Until you called us on Tuesday asking us not to open the white package!', '火曜日に電話してきて、白い包みを開けないでくれと頼むまではね！'),
    ('caleb', 'Everything in that white paper belongs to my brother Owen, not me.', 'あの白い紙の中身は全部、兄のオーウェンのもので、僕のものではありません。'),
]
WALK = [
    (0, None, ["'よく顔を見せてちょうだい、ケイレブ！ピアノより背が高くなったのね！' 久しぶりの相手をじっくり眺めたいとき、副詞の", (None, 'properly'), 'を添えます。形容詞プロパーに語尾リーをつけた形で、きちんと手を抜かずにという響きです。続く比較の', (None, 'grew taller than the piano'), 'では、成長を表す動詞グローの過去形と比較級が組み合わさっています。']),
    (1, None, ["'まさか全く同じ宿に泊まっていらっしゃるなんて、信じられません、イヴリン先生。' 驚きを強める決まった言い回しが", (None, 'the exact same guesthouse'), 'です。セイムの前にイグザクトを入れると、日本語の「全く同じ」に近い強調になります。泊まっている最中なので', (None, 'you are staying'), 'と進行形を使う点にも注目しましょう。']),
    (2, None, ["'待って、じゃあ月曜日に私たちは同じ列車に乗っていて、あなたが彼女のスーツケースを持っていったの？' 乗り物に乗ることを表す動詞ライドの過去形を使って", (None, 'rode the same train'), 'と言います。曜日の前には前置詞オンを置き、', (None, 'on Monday'), 'とするのが英語の決まりです。']),
    (3, None, ["'まったくの偶然なんです！いとこのアパートで開けてみたら、楽譜と赤いリボンが入っていました。' わざとではないと強く訴えるときは", (None, 'By complete accident'), 'と言います。前置詞バイを使うのがポイントです。楽譜は', (None, 'sheet music'), 'で、ミュージックは数えられない名詞なので複数形にしません。']),
    (4, None, ["'どうして夜中に私の鞄を石段に置いて、走って逃げてしまったの？' 動詞と副詞が組み合わさった句動詞", (None, 'run away'), 'は、その場から慌てて離れる様子を表します。夜にはアットを使って', (None, 'at night'), 'と言い、冠詞はつけません。']),
    (5, None, ["'月曜日の夕方ここへ歩いてきたとき、兄がこの通りを歩いているのを見かけたからです！' 知覚動詞シーのあとに人と動詞のイング形を続けると、動作の途中を目撃したことになります。", (None, 'saw my older brother walking'), 'という形です。年上のきょうだいは', (None, 'older brother'), 'と言い、英語では兄と弟を一語で区別しません。']),
    (6, None, ["'お兄さんがここポートランドに住んでいるんですか？' 語順は平叙文のままで、文末の上がり調子だけで疑問を表しています。", (None, 'lives here in Portland'), 'のように、ヒアで大まかに示してから地名で詳しくする順番は英語らしい並べ方です。']),
    (7, None, ["'はい。慌ててしまって、ベルを鳴らし、金曜日のメモを取っ手に差し込みました。' 一瞬で頭が真っ白になることを動詞", (None, 'panicked'), 'で表します。過去形ではケイが入る綴りに注意しましょう。そっと滑り込ませる動作は', (None, 'slipped the Friday note onto the handle'), 'と、スリップとオントゥで描きます。']),
    (8, None, ["'待って、それで水曜日の夜には本名でここにチェックインしたの？' ホテルで受付を済ませることを句動詞", (None, 'checked in'), 'で表します。名前を名乗る場合は前置詞アンダーを使い、', (None, 'under your real name'), 'と言うのが自然です。']),
    (9, None, ["'金曜日の前に近くで静かな場所が必要だったんです。正直、僕の鞄をまだ預かってもらっていることを忘れていました！' 副詞の", (None, 'nearby'), 'は名詞の後ろに置けるのが特徴です。文の途中に挟んだ', (None, 'honestly'), 'は、話し手の本音であることを示す便利な一語です。']),
    (10, None, ["'火曜日に電話してきて、白い包みを開けないでくれと頼むまではね！' 接続詞の", (None, 'Until'), 'で文を始め、前の話に皮肉っぽく付け加えています。頼んだ内容は不定詞の否定で', (None, 'asking us not to open'), 'と表し、ノットはトゥの前に置きます。']),
    (11, None, ["'あの白い紙の中身は全部、兄のオーウェンのもので、僕のものではありません。' 所有を表す動詞句", (None, 'belongs to'), 'は、持ち主を前置詞トゥのあとに置きます。最後の', (None, 'not me'), 'は、文を繰り返さずに否定だけを短く添える口語的な言い方です。']),
]
