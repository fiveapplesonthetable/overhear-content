# Authoring module for linden-courtyard-ja-s01e02-scene-05.
ID = 'linden-courtyard-ja-s01e02-scene-05'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = 'Juice on the Tie  (ネクタイにジュースが！)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'arthur': 'Arthur', 'evelyn': 'Evelyn', 'hannah': 'Hannah'}
INTRO = '朝食のテーブルについたイヴリンが穏やかにお茶とパンを注文していると、オーナーのアーサーが張り切ってオレンジジュースのピッチャーを手に現れました。五つ星の接客を見せようとしたその瞬間、思わぬハプニングが起きます。まずは英語で聴いてみましょう。'
OPENER = 'それでは上品な注文と微笑ましい一幕を、一行ずつ見ていきましょう。'
TRANSITION = 'ではもう一度、場面全体を自然なスピードで聴いてみましょう。'
OUTRO = 'アーサーのネクタイはオレンジジュースまみれになりましたが、炭酸水の知恵と絶品のスクランブルエッグで朝食は大成功でした。それではお気をつけて。'
CLOSING = ('evelyn', 'Take care!')
STORY = [
    ('hannah', 'Good morning again, Miss Evelyn! Would you like coffee or black tea?', '改めておはようございます、ミス・イヴリン！コーヒーと紅茶のどちらがよろしいですか？'),
    ('evelyn', 'Black tea without sugar, please, and one slice of warm bread.', '砂糖なしの紅茶をお願いします、それに温かいパンを一切れ。'),
    ('arthur', "Allow me to pour the fresh orange juice, ma'am!", '新鮮なオレンジジュースは私にお注ぎさせてください、お客さま！'),
    ('evelyn', 'Oh, how kind of you, sir. Just half a glass.', 'まあ、なんてご親切なのでしょう。ほんのグラス半分だけいただきます。'),
    ('arthur', 'At our guesthouse, five-star service comes naturally... whoops!', '当ゲストハウスでは、五つ星のサービスが自然と身についたものとして…おっとっと！'),
    ('hannah', 'Careful, Arthur, the pitcher spout is wide!', '気をつけて、アーサー、そのピッチャーは注ぎ口が広いんです！'),
    ('arthur', 'Oh dear! Not a drop on the table, thank goodness... all of it is on my tie!', 'あら大変！テーブルの上には一滴もこぼれなかった、やれやれ…全部私のネクタイにかかっているぞ！'),
    ('evelyn', 'Do not worry! Cold sparkling water takes orange juice right out.', 'ご心配なく！冷たい炭酸水を使えばオレンジジュースはすぐに落ちますよ。'),
    ('hannah', 'Here is a clean cloth and cold water, Arthur.', 'はい、清潔な布巾と冷たいお水ですよ、アーサー。'),
    ('arthur', "Excuse me, ma'am, I shall retreat to my office with dignity!", '失礼いたします、お客さま、私は威厳を保って事務室へ退却いたします！'),
    ('evelyn', 'Your scrambled eggs are delicious, Hannah. Tell Tessa my compliments!', 'スクランブルエッグがとてもおいしいわ、ハンナ。テッサに私からのお褒めの言葉を伝えてちょうだい！'),
    ('hannah', 'I will! Enjoy your morning.', 'お伝えしますね！どうぞ素敵な朝をお過ごしください。'),
]
WALK = [
    (0, None, ["'改めておはようございます、ミス・イヴリン！コーヒーと紅茶のどちらがよろしいですか？' お客さまに飲み物を勧めるときは最も丁寧な", (None, 'Would you like coffee or black tea'), 'という表現を使います。']),
    (1, None, ["'砂糖なしの紅茶をお願いします、それに温かいパンを一切れ。' 抜きでと頼むときは", (None, 'without sugar'), 'と言い、数えられないパンは単位を添えて', (None, 'one slice of warm bread'), 'と注文します。']),
    (2, None, ["'新鮮なオレンジジュースは私にお注ぎさせてください、お客さま！' 礼儀正しく手助けを申し出る決まり文句に動作を続けて", (None, 'Allow me to pour'), 'と格調高く声をかけています。']),
    (3, None, ["'まあ、なんてご親切なのでしょう。ほんのグラス半分だけいただきます。' 相手の気遣いに感謝する上品な", (None, 'how kind of you'), 'と、控えめな量を伝える', (None, 'Just half a glass'), 'の語順に注目しましょう。']),
    (4, None, ["'当ゲストハウスでは、五つ星のサービスが自然と身についたものとして…おっとっと！' 名詞の前でハイフンを使って単数形にする", (None, 'five-star service'), 'と、手を滑らせた瞬間の掛け声', (None, 'whoops'), 'の組み合わせです。']),
    (5, None, ["'気をつけて、アーサー、そのピッチャーは注ぎ口が広いんです！' とっさに注意を促す一言の", (None, 'Careful'), 'に続けて、器の注ぎ口を', (None, 'the pitcher spout is wide'), 'と知らせています。']),
    (6, None, ["'あら大変！テーブルの上には一滴もこぼれなかった、やれやれ…全部私のネクタイにかかっているぞ！' わずかなしずくも落ちなかったという", (None, 'Not a drop on the table'), 'から一転して', (None, 'on my tie'), 'と落ちがつきます。']),
    (7, None, ["'ご心配なく！冷たい炭酸水を使えばオレンジジュースはすぐに落ちますよ。' 炭酸入りの水を表す", (None, 'Cold sparkling water'), 'が染みをきれいに抜き取ることを', (None, 'takes orange juice right out'), 'と表現します。']),
    (8, None, ["'はい、清潔な布巾と冷たいお水ですよ、アーサー。' 一枚の拭き布は数えられる名詞として", (None, 'a clean cloth'), 'と言い、数えられない水には冠詞を付けずに並べます。']),
    (9, None, ["'失礼いたします、お客さま、私は威厳を保って事務室へ退却いたします！' あえて古風で芝居がかった助動詞を使った", (None, 'I shall retreat to my office'), 'に続けて文末の', (None, 'with dignity'), 'が笑いを誘います。']),
    (10, None, ["'スクランブルエッグがとてもおいしいわ、ハンナ。テッサに私からのお褒めの言葉を伝えてちょうだい！' 料理を作った人へ感謝と賛辞を届けるときは複数形で", (None, 'Tell Tessa my compliments'), 'と言うのが素敵な大人の表現です。']),
    (11, None, ["'お伝えしますね！どうぞ素敵な朝をお過ごしください。' 頼まれたことを快く引き受ける短い", (None, 'I will'), 'と、食事の席でかける温かい挨拶', (None, 'Enjoy your morning'), 'の組み合わせです。']),
]
