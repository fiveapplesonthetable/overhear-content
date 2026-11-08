# Authoring module for linden-courtyard-ja-s01e01-scene-05.
ID = 'linden-courtyard-ja-s01e01-scene-05'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = 'Not My Clothes!  (私の服じゃないわ！)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'evelyn': 'Evelyn', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '二階の四号室に上がった直後、部屋から慌ただしく呼び鈴が鳴りました。ハンナとグレアムが駆けつけると、開けられた青いスーツケースの前でイヴリンが目を丸くしています。まずは場面全体を英語で聴いてみましょう。'
OPENER = 'それでは驚きの一場面を、一行ずつゆっくり確認していきましょう。'
TRANSITION = 'ではもう一度、自然なスピードで最初から聴いてみましょう。'
OUTRO = '外見は瓜二つでも、中身は大きな紳士靴と木製のおもちゃの列車でした。明るいフロントへ降りて、持ち手の荷札を調べることになります。それではまた次回。'
CLOSING = ('hannah', 'Goodbye!')
STORY = [
    ('hannah', 'Miss Evelyn, is everything all right? You rang the bell!', 'ミス・イヴリン、大丈夫ですか？ベルを鳴らされましたね！'),
    ('evelyn', 'Look inside this suitcase, Hannah! This is not my bag!', 'このスーツケースの中を見てちょうだい、ハンナ！これは私の鞄じゃないわ！'),
    ('hannah', 'Wait, it is dark blue, just like yours!', '待って、濃紺の色をしていて、あなたの鞄とそっくりですよ！'),
    ('evelyn', 'The outside is identical, yes! But look inside!', '外側はまったく同じなのよ、ええ！でも中を見てごらんなさい！'),
    ('graham', "Two pairs of big brown men's shoes and gray sweaters.", '大きな茶色の紳士靴が二足と、灰色のセーターですね。'),
    ('hannah', 'And what is this wrapped in white paper? A little wooden train!', 'それに白い紙に包まれたこれは何でしょう？小さな木製の列車です！'),
    ('evelyn', 'I certainly do not wear size eleven shoes!', '私は間違いなくサイズ十一の靴なんて履きませんよ！'),
    ('graham', 'No wonder it was so heavy. Wood and leather!', '道理であんなに重かったわけだ。木と革ですからね！'),
    ('evelyn', 'Someone at the train station took my blue suitcase by mistake!', '駅の誰かが、間違えて私の青いスーツケースを持っていってしまったんだわ！'),
    ('hannah', "Please sit down, ma'am. Do not worry, we will check the tag right now.", 'どうぞお掛けください、お客さま。ご心配なく、今すぐ荷札を確認しますから。'),
    ('graham', 'There is a small paper card tied to the side handle.', '横の持ち手に、小さな紙のカードが結ばれていますよ。'),
    ('evelyn', 'Oh, let us bring it downstairs to the light!', 'まあ、下の階の明るいところへ持っていきましょう！'),
]
WALK = [
    (0, None, ["'ミス・イヴリン、大丈夫ですか？ベルを鳴らされましたね！' 相手に何か変わったことがないか気遣うときは", (None, 'is everything all right'), 'と声をかけます。']),
    (1, None, ["'このスーツケースの中を見てちょうだい、ハンナ！これは私の鞄じゃないわ！' 入れ物の内部をのぞき込むときは", (None, 'Look inside this suitcase'), 'と言い、続けて', (None, 'This is not my bag'), 'と否定します。']),
    (2, None, ["'待って、濃紺の色をしていて、あなたの鞄とそっくりですよ！' あなたの鞄と繰り返す代わりに所有代名詞を使って", (None, 'just like yours'), 'とすっきり比べられます。']),
    (3, None, ["'外側はまったく同じなのよ、ええ！でも中を見てごらんなさい！' 見分けがつかないほどそっくりなことを", (None, 'The outside is identical'), 'という一語で表しています。']),
    (4, None, ["'大きな茶色の紳士靴が二足と、灰色のセーターですね。' 左右揃った靴を数えるには組を表す語を使って", (None, 'Two pairs of'), 'と言い、不規則な複数所有格の', (None, "men's shoes"), 'をすぐ後ろに続けます。']),
    (5, None, ["'それに白い紙に包まれたこれは何でしょう？小さな木製の列車です！' 後ろから状態を説明する過去分詞の", (None, 'wrapped in white paper'), 'と、大きさの次に材質を置く', (None, 'little wooden train'), 'の語順に注目しましょう。']),
    (6, None, ["'私は間違いなくサイズ十一の靴なんて履きませんよ！' 英語では靴を履くときも服と同じ動詞を使って", (None, 'do not wear size eleven shoes'), 'と表現します。']),
    (7, None, ["'道理であんなに重かったわけだ。木と革ですからね！' 謎が解けて納得したときは決まり文句の", (None, 'No wonder it was so heavy'), 'がとても自然に響きます。']),
    (8, None, ["'駅の誰かが、間違えて私の青いスーツケースを持っていってしまったんだわ！' 悪意なくうっかり取り違えたことは文末に", (None, 'by mistake'), 'を添えるだけで的確に伝わります。']),
    (9, None, ["'どうぞお掛けください、お客さま。ご心配なく、今すぐ荷札を確認しますから。' 相手を落ち着かせる丁寧な", (None, 'Please sit down'), 'と安心させる優しい', (None, 'Do not worry'), 'は接客の心強い味方です。']),
    (10, None, ["'横の持ち手に、小さな紙のカードが結ばれていますよ。' 新しく見つけた物の存在を切り出す", (None, 'There is a small paper card'), 'に、結ばれた状態を示す', (None, 'tied to the side handle'), 'を続けています。']),
    (11, None, ["'まあ、下の階の明るいところへ持っていきましょう！' 一緒に行動しようと誘う丁寧な", (None, 'let us bring it downstairs'), 'では、階下を表す語の前に前置詞を置かないのがポイントです。']),
]
