# Authoring module for linden-courtyard-ja-s01e02-scene-01.
ID = 'linden-courtyard-ja-s01e02-scene-01'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = 'The Red Ribbon  (赤いリボン)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = '火曜日の朝、イヴリンがフロントへ降りてくると、昨夜門の前に置かれていた本物の青いスーツケースが待っていました。大切なティーカップも無事でほっと一安心ですが、残された鞄の謎はさらに深まります。まずは場面全体を英語で聴いてみましょう。'
OPENER = 'それでは朝の再会のやり取りを、一行ずつゆっくり見ていきましょう。'
TRANSITION = 'ではもう一度、会話全体を自然なスピードで聴いてみましょう。'
OUTRO = '赤いリボンもティーカップも無事で、イヴリンは晴れやかな気持ちで朝食へ向かいます。その一方でキッチンでは、思いがけない朝の騒動が始まっていました。それではまたすぐに。'
CLOSING = ('evelyn', 'See you soon!')
STORY = [
    ('hannah', 'Good morning, Miss Evelyn! Look what arrived at our gate last night.', 'おはようございます、ミス・イヴリン！昨夜うちの門に届いたものを見てください。'),
    ('evelyn', 'My suitcase! Let me open the top pocket... yes, my red ribbon!', '私のスーツケースだわ！一番上のポケットを開けさせて…ええ、私の赤いリボンよ！'),
    ('graham', 'And your teacup inside? Is it still in one piece?', '中に入っていたティーカップはどうですか？まだ割れずに無事ですか？'),
    ('evelyn', 'Not a single crack! Who brought it back?', 'ひび一つないわ！どなたが持ってきてくださったの？'),
    ('hannah', 'We do not know. Someone left it on the step and rang the bell.', 'わからないんです。誰かが石段の上に置いて、ベルを鳴らしていきました。'),
    ('evelyn', 'And he did not ask for his own suitcase with the wooden train?', 'それでその人は、木製の列車が入った自分のスーツケースは求めなかったの？'),
    ('graham', 'He left a short note asking us to keep it until Friday.', '金曜日まで預かっておいてほしいと頼む、短い書き置きを残していきました。'),
    ('evelyn', 'How curious! The handwriting on that tag felt oddly familiar to me.', 'なんて不思議なのかしら！あの荷札の筆跡、なぜか妙に見覚えがあったのよ。'),
    ('hannah', 'Really? Do you know someone in Portland?', '本当ですか？ポートランドにお知り合いがいらっしゃるのですか？'),
    ('evelyn', 'Twenty-five years ago I taught piano near here, though memories fade.', '二十五年前にこの近くでピアノを教えていたの、もっとも記憶は薄れていくけれどね。'),
    ('graham', 'For now, his bag stays safe under lock and key.', '今のところは、彼の鞄もしっかり鍵をかけて安全に保管しておきます。'),
    ('evelyn', 'Wonderful! Now I am ready for a big breakfast.', '頼もしいわ！さあ、たっぷりの朝ごはんをいただく準備は万端よ。'),
]
WALK = [
    (0, None, ["'おはようございます、ミス・イヴリン！昨夜うちの門に届いたものを見てください。' 到着したものをそのまま目的語に組み込んで", (None, 'Look what arrived'), 'と言い、昨日の夜を冠詞なしで', (None, 'last night'), 'と文末に続けます。']),
    (1, None, ["'私のスーツケースだわ！一番上のポケットを開けさせて…ええ、私の赤いリボンよ！' 自分で確かめるときに自然な", (None, 'Let me open the top pocket'), 'で目印のリボンを見つけます。']),
    (2, None, ["'中に入っていたティーカップはどうですか？まだ割れずに無事ですか？' 瀬戸物が欠けたり割れたりせず一つの形のままであることを", (None, 'still in one piece'), 'という鮮やかな慣用句で表します。']),
    (3, None, ["'ひび一つないわ！どなたが持ってきてくださったの？' ただの一つもないと強調する", (None, 'Not a single crack'), 'に続けて、主語を尋ねる疑問文を', (None, 'Who brought it back'), 'とそのままの語順で作ります。']),
    (4, None, ["'わからないんです。誰かが石段の上に置いて、ベルを鳴らしていきました。' 過去の二つの動作を並べて", (None, 'left it on the step'), 'と言い、それから次に', (None, 'rang the bell'), 'と時系列通りに伝えます。']),
    (5, None, ["'それでその人は、木製の列車が入った自分のスーツケースは求めなかったの？' 何かを引き渡すよう頼む表現を過去の否定形にして", (None, 'did not ask for his own suitcase'), 'と不思議がっています。']),
    (6, None, ["'金曜日まで預かっておいてほしいと頼む、短い書き置きを残していきました。' 名詞の後ろから内容を説明する分詞を使って", (None, 'a short note asking us'), 'と滑らかにつなげています。']),
    (7, None, ["'なんて不思議なのかしら！あの荷札の筆跡、なぜか妙に見覚えがあったのよ。' どこか懐かしく見覚えがある感覚を、筆跡を主語にして", (None, 'felt oddly familiar to me'), 'と表現します。']),
    (8, None, ["'本当ですか？ポートランドにお知り合いがいらっしゃるのですか？' 誰か心当たりがあるかと温かく尋ねるときは疑問文でも肯定的な響きの", (None, 'Do you know someone in Portland'), 'と自然に言えます。']),
    (9, None, ["'二十五年前にこの近くでピアノを教えていたの、もっとも記憶は薄れていくけれどね。' 今から遡る年月には期間の後ろに置く", (None, 'Twenty-five years ago'), 'を使い、楽器の指導は冠詞なしで', (None, 'taught piano'), 'とすっきり言います。']),
    (10, None, ["'今のところは、彼の鞄もしっかり鍵をかけて安全に保管しておきます。' 当面の間を表す文頭の", (None, 'For now'), 'と、厳重な保管を表す慣用句の', (None, 'under lock and key'), 'がよく響きます。']),
    (11, None, ["'頼もしいわ！さあ、たっぷりの朝ごはんをいただく準備は万端よ。' お腹が空いて食事が楽しみな気持ちを", (None, 'I am ready for a big breakfast'), 'と明るく伝えています。']),
]
