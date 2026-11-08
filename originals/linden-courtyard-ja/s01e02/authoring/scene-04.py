# Authoring module for linden-courtyard-ja-s01e02-scene-04.
ID = 'linden-courtyard-ja-s01e02-scene-04'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 2
SCENE = 4
TITLE = 'Herbs from the Courtyard  (中庭のハーブ)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'graham': 'Graham', 'tessa': 'Tessa', 'hannah': 'Hannah'}
INTRO = 'キッチンの騒ぎを聞きつけて、中庭からグレアムが摘みたての緑のハーブを持って入ってきました。時刻は七時二十九分、いよいよ八人のお客さまが階段を降りてきます。まずは活気ある準備の場面を聴いてみましょう。'
OPENER = 'それでは朝食直前のチームワークを、一行ずつ見ていきましょう。'
TRANSITION = 'ではもう一度、場面全体の心地よいリズムを聴いてみましょう。'
OUTRO = '焼きたてのパンにフランス風のスクランブルエッグ、そして摘みたてのハーブが揃い、二日目の朝食が始まりました。それではまたすぐに。'
CLOSING = ('graham', 'See you soon!')
STORY = [
    ('graham', 'I heard shouting about butter from all the way out in the courtyard.', 'ずっと外の中庭にいたのに、バターがどうとか叫ぶ声が聞こえたぞ。'),
    ('tessa', 'Hannah bought sea salt butter, so today we are making French style eggs!', 'ハンナが海塩バターを買ってきたから、今日はフランス風の卵料理を作っているのよ！'),
    ('graham', 'Good. Put these fresh green herbs on top before you serve them.', 'そいつはいい。お出しする前に、この新鮮な緑のハーブを上に載せなさい。'),
    ('hannah', 'Did you grow those herbs yourself, Graham?', 'そのハーブは、グレアムがご自分で育てたのですか？'),
    ('graham', 'Somebody has to take care of the courtyard plants.', '誰かが中庭の植物の世話をしなきゃならないからね。'),
    ('tessa', 'Smell that! Warm bread, hot eggs, and fresh herbs.', 'この香りを嗅いでみて！温かいパンに、熱々の卵、それに新鮮なハーブよ。'),
    ('hannah', 'Where do the small spoons and napkins go?', '小さなスプーンとナプキンはどこに置けばいいですか？'),
    ('tessa', 'Put one napkin and one small spoon beside every blue cup.', 'どの青いカップの横にも、ナプキンを一枚と小さなスプーンを一本置いてね。'),
    ('graham', 'Seven twenty-nine on my watch. Guests are coming down the stairs.', '私の腕時計で七時二十九分だ。お客さまが階段を降りてくるよ。'),
    ('hannah', 'Four tables, eight chairs, everything in place!', 'テーブルが四つ、椅子が八脚、すべて所定の位置に整いました！'),
    ('tessa', 'Pour the hot water into the teapot, Hannah, here they come!', 'ティーポットに熱いお湯を注いで、ハンナ、さあお客さまがいらっしゃったわよ！'),
    ('graham', 'Not bad for day two, rookie.', '二日目にしては悪くないね、新人さん。'),
]
WALK = [
    (0, None, ["'ずっと外の中庭にいたのに、バターがどうとか叫ぶ声が聞こえたぞ。' 叫ぶ声を聞いたことを", (None, 'I heard shouting'), 'と言い、はるばる離れた場所からという距離感を', (None, 'all the way out'), 'で強調しています。']),
    (1, None, ["'ハンナが海塩バターを買ってきたから、今日はフランス風の卵料理を作っているのよ！' 今まさにキッチンで調理している最中なので現在進行形の", (None, 'we are making French style eggs'), 'と生き生きと伝えます。']),
    (2, None, ["'そいつはいい。お出しする前に、この新鮮な緑のハーブを上に載せなさい。' 料理の仕上げに一番上へ添えることを", (None, 'Put these fresh green herbs on top'), 'と具体的に指示します。']),
    (3, None, ["'そのハーブは、グレアムがご自分で育てたのですか？' 他の誰でもなく本人の手でということを強調するため、文末に再帰代名詞を添えて", (None, 'grow those herbs yourself'), 'と尋ねています。']),
    (4, None, ["'誰かが中庭の植物の世話をしなきゃならないからね。' 照れ隠しに一般化して", (None, 'Somebody has to'), 'と切り出し、手入れすることを', (None, 'take care of'), 'という熟語で表します。']),
    (5, None, ["'この香りを嗅いでみて！温かいパンに、熱々の卵、それに新鮮なハーブよ。' 目の前に広がる素晴らしい香りに注意を向ける短い命令表現が", (None, 'Smell that'), 'という生き生きとした一言です。']),
    (6, None, ["'小さなスプーンとナプキンはどこに置けばいいですか？' 食器や道具の本来の置き場所を尋ねるときは行くという動詞を使って", (None, 'Where do the small spoons and napkins go'), 'と言うのがとても自然です。']),
    (7, None, ["'どの青いカップの横にも、ナプキンを一枚と小さなスプーンを一本置いてね。' すぐ隣の位置を示す前置詞と単数名詞を組み合わせて", (None, 'beside every blue cup'), 'と丁寧に案内します。']),
    (8, None, ["'私の腕時計で七時二十九分だ。お客さまが階段を降りてくるよ。' 時計の表示時刻は数字をそのまま並べて", (None, 'Seven twenty-nine on my watch'), 'と読み上げます。']),
    (9, None, ["'テーブルが四つ、椅子が八脚、すべて所定の位置に整いました！' すべての準備があるべき場所にぴたりと整った状態を", (None, 'everything in place'), 'と簡潔に表します。']),
    (10, None, ["'ティーポットに熱いお湯を注いで、ハンナ、さあお客さまがいらっしゃったわよ！' 外から容器の中へと注ぎ入れる動きを", (None, 'Pour the hot water into the teapot'), 'と表し、到着を', (None, 'here they come'), 'と明るく告げます。']),
    (11, None, ["'二日目にしては悪くないね、新人さん。' 控えめながらもしっかり相手を認める褒め言葉の", (None, 'Not bad for day two'), 'は英語らしい温かい表現です。']),
]
