# Authoring module for linden-courtyard-ja-s01e01-scene-07.
ID = 'linden-courtyard-ja-s01e01-scene-07'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 1
SCENE = 7
TITLE = 'Tea and a Warm Cardigan  (お茶と暖かいカーディガン)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'tessa': 'Tessa', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = 'カフェコーナーに案内されたイヴリンに、テッサは熱いミントティーと新品の柔らかいカーディガンを用意しました。グレアムも謎の青いスーツケースをしっかりと保管します。まずは心温まるやり取りを聴いてみましょう。'
OPENER = 'それでは一文ずつ、思いやりのこもった表現を見ていきましょう。'
TRANSITION = 'ではもう一度、穏やかな会話全体を自然な速さで聴いてみましょう。'
OUTRO = '温かいお茶とカーディガンのおかげで、イヴリンも笑顔を取り戻しました。ところがその夜遅く、静かな中庭の門で思いがけないベルが鳴り響きます。それではおやすみなさい。'
CLOSING = ('tessa', 'Good night!')
STORY = [
    ('tessa', "Here you are, ma'am: hot mint tea and honey.", 'さあどうぞ、お客さま。熱いミントティーとはちみつですよ。'),
    ('evelyn', 'Oh, thank you, Tessa. My hands were cold from the shock!', 'まあ、ありがとう、テッサ。驚きのあまり両手が冷たくなっていたのよ！'),
    ('tessa', 'And look, this soft wool cardigan is clean and never worn. Try it on.', 'それにご覧になって、この柔らかいウールのカーディガンは清潔でまだ一度も袖を通していないんです。羽織ってみてください。'),
    ('evelyn', 'Are you sure? It looks lovely and warm!', '本当にいいの？とても素敵で暖かそうだわ！'),
    ('graham', "It fits you very well, ma'am.", 'とてもよくお似合いですよ、お客さま。'),
    ('evelyn', 'You good people are saving my whole trip.', '親切なみなさんが、私の旅を丸ごと救ってくださっているわ。'),
    ('tessa', 'A traveler cannot sit upstairs sad on her first evening in Portland!', 'ポートランドでの最初の夜に、旅のお客さまを上の階で悲しく座らせてはおけませんもの！'),
    ('graham', 'I locked the other blue suitcase safely in our luggage closet.', 'もう片方の青いスーツケースは、荷物用の収納室に安全に鍵をかけてしまいました。'),
    ('evelyn', 'Thank you, Graham. That little wooden train inside looked old and precious.', 'ありがとう、グレアム。中にあったあの小さな木製の列車、古くて大切な品に見えたわ。'),
    ('tessa', 'Whoever owns it will surely look for it soon.', '持ち主がどなたであれ、きっとすぐに探し始めるはずですよ。'),
    ('evelyn', 'I think I will sleep well tonight after all.', 'おかげさまで、今夜はやっぱりぐっすり眠れそうだわ。'),
    ('graham', "Rest well, ma'am. Ring down if you need anything.", 'どうぞゆっくりお休みください、お客さま。何かご入用でしたらベルでお知らせくださいね。'),
]
WALK = [
    (0, None, ["'さあどうぞ、お客さま。熱いミントティーとはちみつですよ。' 飲み物や品物を目の前で差し出すときは", (None, 'Here you are'), 'と声をかけるのが最も自然で温かい表現です。']),
    (1, None, ["'まあ、ありがとう、テッサ。驚きのあまり両手が冷たくなっていたのよ！' 両手は複数形なので過去の動詞も複数に合わせて", (None, 'My hands were cold'), 'と言い、冷えた原因を', (None, 'from the shock'), 'と後ろに続けます。']),
    (2, None, ["'それにご覧になって、この柔らかいウールのカーディガンは清潔でまだ一度も袖を通していないんです。羽織ってみてください。' 未使用であることを過去分詞で", (None, 'never worn'), 'と言い、試着を勧めるときは代名詞を間に挟んで', (None, 'Try it on'), 'と温かく言います。']),
    (3, None, ["'本当にいいの？とても素敵で暖かそうだわ！' 相手の親切に遠慮しつつ確かめる", (None, 'Are you sure'), 'と、見た目の印象を述べる', (None, 'It looks lovely and warm'), 'の組み合わせです。']),
    (4, None, ["'とてもよくお似合いですよ、お客さま。' 服のサイズや雰囲気がぴったり合っていることを褒めるときは", (None, 'It fits you very well'), 'と自然に伝えます。']),
    (5, None, ["'親切なみなさんが、私の旅を丸ごと救ってくださっているわ。' 目の前の人たちへ感謝を込めて", (None, 'You good people'), 'と呼びかけ、旅全体を', (None, 'saving my whole trip'), 'と表しています。']),
    (6, None, ["'ポートランドでの最初の夜に、旅のお客さまを上の階で悲しく座らせてはおけませんもの！' 上の階でという副詞をそのまま動詞に続けて", (None, 'sit upstairs sad'), 'と情景を描いています。']),
    (7, None, ["'もう片方の青いスーツケースは、荷物用の収納室に安全に鍵をかけてしまいました。' 二つあるうちのもう一方を指すときは定冠詞を付けて", (None, 'the other blue suitcase'), 'とはっきり呼びます。']),
    (8, None, ["'ありがとう、グレアム。中にあったあの小さな木製の列車、古くて大切な品に見えたわ。' 思い出の詰まった品物を表すのに", (None, 'looked old and precious'), 'という形容詞がぴったりです。']),
    (9, None, ["'持ち主がどなたであれ、きっとすぐに探し始めるはずですよ。' まだ誰かわからない持ち主を主語に立てるときは", (None, 'Whoever owns it'), 'と言い、探す動作には', (None, 'look for it'), 'という形を使います。']),
    (10, None, ["'おかげさまで、今夜はやっぱりぐっすり眠れそうだわ。' 自分の見通しをやわらかく伝える", (None, 'I think I will sleep well'), 'の最後に、いろいろあったけれど結局はという', (None, 'after all'), 'を添えています。']),
    (11, None, ["'どうぞゆっくりお休みください、お客さま。何かご入用でしたらベルでお知らせくださいね。' 夜のお休みを気遣う上品な", (None, 'Rest well'), 'と、上の階からフロントを鳴らす', (None, 'Ring down'), 'で締めくくっています。']),
]
