# Authoring module for linden-courtyard-ja-s01e02-scene-02.
ID = 'linden-courtyard-ja-s01e02-scene-02'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = 'No Milk in the Fridge  (冷蔵庫に牛乳がない！)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = '朝食開始まであと二十分というとき、カフェコーナーからテッサの悲鳴に近い声が響きました。乳製品を届ける配達バンが町の外でパンクしてしまい、冷蔵庫はほぼ空っぽです。まずは大慌ての場面を英語で聴いてみましょう。'
OPENER = 'それでは緊迫したキッチンのやり取りを、一行ずつ見ていきましょう。'
TRANSITION = 'ではもう一度、スピード感あふれる会話を通して聴いてみましょう。'
OUTRO = '現金五十ドルを受け取ったハンナは、角のマーケットへ向かって風のように飛び出していきました。果たして十分以内に戻ってこられるでしょうか。それではまた後で。'
CLOSING = ('hannah', 'See you later!')
STORY = [
    ('tessa', 'Oh no! Arthur, Hannah, we have a kitchen emergency!', '大変！アーサー、ハンナ、キッチンの緊急事態よ！'),
    ('arthur', 'Please do not say the word emergency before my morning coffee!', '朝のコーヒーを飲む前に、緊急事態という言葉を口にしないでくれよ！'),
    ('tessa', 'The dairy van has a flat tire outside town. Look in the fridge!', '乳製品の配達バンが町の外でパンクしたの。冷蔵庫の中を見て！'),
    ('hannah', 'One tiny splash of milk, two eggs, and no butter at all!', '牛乳がほんのひとしずくと、卵が二つ、それにバターはまったくありません！'),
    ('arthur', 'Eight hungry guests will come down the stairs at seven thirty!', 'お腹を空かせた八人のお客さまが、七時半には階段を降りてくるぞ！'),
    ('tessa', 'My bread dough is ready in the oven, at least.', '少なくとも、私のパン生地はオーブンの中で準備ができているわ。'),
    ('hannah', 'Give me a bag and some cash! The corner market opens at seven.', '袋と現金を少しください！角のマーケットが七時に開きます。'),
    ('arthur', 'Can you run there and back in ten minutes?', '十分以内にそこまで走って往復できるかい？'),
    ('hannah', 'Watch me! Tell me exactly what to buy.', '見ていてください！何を買えばいいか正確に教えて。'),
    ('tessa', 'Three bottles of milk, twenty eggs, butter, cheese, and red apples!', '牛乳を三本、卵を二十個、バター、チーズ、それに赤いりんごよ！'),
    ('arthur', 'Here is fifty from the cash box. Bring back the receipt!', 'ほら、現金箱から五十ドルだ。レシートを持ち帰ってきてくれよ！'),
    ('hannah', 'Hold the fort, I am already out the door!', '留守を頼みます、もうドアを飛び出していますから！'),
]
WALK = [
    (0, None, ["'大変！アーサー、ハンナ、キッチンの緊急事態よ！' 困った出来事が起きたときの第一声", (None, 'Oh no'), 'に続けて、急なピンチを', (None, 'a kitchen emergency'), 'と伝えています。']),
    (1, None, ["'朝のコーヒーを飲む前に、緊急事態という言葉を口にしないでくれよ！' 丁寧ながらも切実な否定の依頼を", (None, 'Please do not say the word'), 'とユーモアたっぷりに返しています。']),
    (2, None, ["'乳製品の配達バンが町の外でパンクしたの。冷蔵庫の中を見て！' タイヤの空気が抜けてパンクした状態を", (None, 'has a flat tire'), 'と言い、郊外を冠詞なしで', (None, 'outside town'), 'と簡潔に表します。']),
    (3, None, ["'牛乳がほんのひとしずくと、卵が二つ、それにバターはまったくありません！' 容器の底にわずかに残った液体を", (None, 'One tiny splash of milk'), 'と表し、完全なゼロを', (None, 'no butter at all'), 'と力強く強めます。']),
    (4, None, ["'お腹を空かせた八人のお客さまが、七時半には階段を降りてくるぞ！' まもなく起きる事態を予測して", (None, 'will come down the stairs'), 'と言い、到着時刻を', (None, 'at seven thirty'), 'と後ろに添えます。']),
    (5, None, ["'少なくとも、私のパン生地はオーブンの中で準備ができているわ。' 大変な状況の中でせめてもの救いを挙げるときは文末に", (None, 'at least'), 'を添えると自然です。']),
    (6, None, ["'袋と現金を少しください！角のマーケットが七時に開きます。' 数えられる袋には冠詞を付け、数えられない現金には量を和らげる語を付けて", (None, 'a bag and some cash'), 'と頼み、開店時刻を', (None, 'opens at seven'), 'と現在形で言います。']),
    (7, None, ["'十分以内にそこまで走って往復できるかい？' 行って戻ってくる往復の動きを簡潔に", (None, 'run there and back'), 'と言い、制限時間を', (None, 'in ten minutes'), 'という形で表します。']),
    (8, None, ["'見ていてください！何を買えばいいか正確に教えて。' 任せておいてと頼もしく答える", (None, 'Watch me'), 'に続けて、買うべき品物を', (None, 'exactly what to buy'), 'と手短に尋ねます。']),
    (9, None, ["'牛乳を三本、卵を二十個、バター、チーズ、それに赤いりんごよ！' 数えられない牛乳は容器の単位を使って", (None, 'Three bottles of milk'), 'と数え、数えられる卵やりんごはそのまま複数形にします。']),
    (10, None, ["'ほら、現金箱から五十ドルだ。レシートを持ち帰ってきてくれよ！' お金を手渡すときの", (None, 'Here is fifty'), 'と、忘れずに持ち帰るよう頼む', (None, 'Bring back the receipt'), 'の組み合わせです。']),
    (11, None, ["'留守を頼みます、もうドアを飛び出していますから！' 出かける際に現場を任せる楽しい決まり文句の", (None, 'Hold the fort'), 'と、すでに駆け出している勢いの', (None, 'already out the door'), 'で締めくくります。']),
]
