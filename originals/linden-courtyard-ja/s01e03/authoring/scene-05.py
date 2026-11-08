# Authoring module for linden-courtyard-ja-s01e03-scene-05.
ID = 'linden-courtyard-ja-s01e03-scene-05'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 3
SCENE = 5
TITLE = 'Half Price and Quiet Beams  (半額と静かな梁)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb', 'graham': 'Graham'}
INTRO = 'ハンナとグレアムに案内されて、ケイレブが屋根裏部屋へ上がってきます。古い樫の梁が並ぶ天井に建築家の目が輝き、半額の申し出にも満足そうです。まずは場面全体を英語で聴いてみましょう。'
OPENER = 'それでは、屋根裏でのやり取りを一文ずつ丁寧に見ていきます。'
TRANSITION = '表現を確認できたところで、もう一度自然な速さで通して聴いてください。'
OUTRO = 'ケイレブは静かな屋根裏と広い机がすっかり気に入り、二重予約の騒ぎもひとまず収まりました。次の第六場面では、一階の受付に戻ります。'
CLOSING = ('hannah', 'Good night!')
STORY = [
    ('hannah', 'Here we are, sir. Watch your head on this low wooden beam.', '着きましたよ。この低い木の梁に頭をぶつけないよう気をつけてくださいね。'),
    ('caleb', 'Oh... look at the proportions of this timber roof!', 'おお…この木造の屋根の比率を見てください！'),
    ('graham', 'Solid oak, eighty years old. Not a single leak.', '樫の無垢材で、築八十年です。雨漏りは一つもありません。'),
    ('hannah', 'Because of our mistake, tonight is half price, with breakfast included.', 'こちらの手違いですので、今夜は半額、朝食付きです。'),
    ('caleb', 'Listen for a second... you cannot hear a single car from the street.', 'ちょっと耳を澄ませてみて…通りの車の音が一台も聞こえません。'),
    ('hannah', 'Only the courtyard tree and the rain.', '聞こえるのは中庭の木と雨の音だけです。'),
    ('caleb', 'To tell you the truth, I hate noisy first floor rooms. I love this space!', '正直に言うと、騒がしい一階の部屋は大嫌いなんです。この空間、最高ですね！'),
    ('graham', 'Really? You do not mind the extra stairs?', '本当ですか？階段が多くても構いませんか？'),
    ('caleb', 'Not at all! And this wide desk under the window is ideal for my work.', '全然！それに窓の下のこの広い机は、私の仕事にぴったりです。'),
    ('hannah', 'What a relief! Here is your silver key, Caleb.', 'ほっとしました！こちらが銀色の鍵です、ケイレブさん。'),
    ('caleb', 'Thank you both for being honest instead of sending me back into the rain.', '雨の中へ追い返さずに、正直に話してくれたお二人に感謝します。'),
    ('graham', 'Sleep well, sir. Breakfast starts at seven thirty downstairs.', 'ゆっくりお休みください。朝食は下の階で七時半からです。'),
]
WALK = [
    (0, None, ["'着きましたよ。この低い木の梁に頭をぶつけないよう気をつけてくださいね。' 天井の低い場所で相手に注意を促す決まり文句が", (None, 'Watch your head'), 'です。直訳すると「頭を見て」ですが、日本語の「頭上注意」にあたる親切な一言です。']),
    (1, None, ["'おお…この木造の屋根の比率を見てください！' 建築家らしい言葉として", (None, 'proportions'), 'が出てきます。高さと幅の釣り合いを指すときは、このように複数形で使うのが普通です。']),
    (2, None, ["'樫の無垢材で、築八十年です。雨漏りは一つもありません。' 動詞を省いた短い言い方の", (None, 'Not a single leak'), 'は、単数の強調で「ただの一つも」という気持ちを込めた打ち消しになります。']),
    (3, None, ["'こちらの手違いですので、今夜は半額、朝食付きです。' ホテルの案内でよく見る", (None, 'with breakfast included'), 'は、名詞の後ろに過去分詞を置いて「含まれた状態で」と付け加える形です。']),
    (4, None, ["'ちょっと耳を澄ませてみて…通りの車の音が一台も聞こえません。' ここでの", (None, 'you cannot hear'), 'の主語は目の前の相手だけではなく、「誰であっても」という一般的な人を指す用法です。']),
    (5, None, ["'聞こえるのは中庭の木と雨の音だけです。' 文頭に置かれた", (None, 'Only'), 'が、前の文の続きを短く補っています。会話では動詞を繰り返さず、このように名詞だけで答えることがよくあります。']),
    (6, None, ["'正直に言うと、騒がしい一階の部屋は大嫌いなんです。この空間、最高ですね！' 本音を切り出す前置きの", (None, 'To tell you the truth'), 'は、日本語の「実を言うと」に近い便利な表現です。']),
    (7, None, ["'本当ですか？階段が多くても構いませんか？' 相手の気持ちを確かめる", (None, 'You do not mind'), 'は、語順は平叙文のまま上がり調子で読むことで、驚きを含んだ質問になっています。']),
    (8, None, ["'全然！それに窓の下のこの広い机は、私の仕事にぴったりです。' 強い否定の返事", (None, 'Not at all'), 'は、「気になりますか」という問いに対して「少しも」と答える定番の言い方です。']),
    (9, None, ["'ほっとしました！こちらが銀色の鍵です、ケイレブさん。' 安堵を表す感嘆文", (None, 'What a relief'), 'は、冠詞を伴って「なんという安心だろう」と気持ちをまるごと言い表します。']),
    (10, None, ["'雨の中へ追い返さずに、正直に話してくれたお二人に感謝します。' 二つの行動を比べる", (None, 'instead of'), 'の後ろには、動詞を「〜すること」の形にして続けます。']),
    (11, None, ["'ゆっくりお休みください。朝食は下の階で七時半からです。' 寝る前のあいさつ", (None, 'Sleep well'), 'は、動詞の命令形ですが、命令ではなく温かい願いを伝える言葉です。']),
]
