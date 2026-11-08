# Authoring module for linden-courtyard-ja-s01e01-scene-06.
ID = 'linden-courtyard-ja-s01e01-scene-06'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = 'The Luggage Tag  (スーツケースの荷札)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'arthur': 'Arthur'}
INTRO = 'フロントの明るい照明の下で、アーサーが眼鏡をかけてスーツケースの荷札を読み取ります。ハンナはすぐさま駅の遺失物取扱所に電話をかけますが、手がかりはほんのわずかです。まずは場面全体を聴いてみましょう。'
OPENER = 'それでは一行ずつ、電話や確認の表現を確かめていきましょう。'
TRANSITION = 'ではもう一度、場面全体のやり取りを通して聴いてみましょう。'
OUTRO = '駅にはまだ届け出がありませんでしたが、カフェコーナーからテッサが何か良い思いつきがある様子で手を振っています。それではまたすぐに。'
CLOSING = ('arthur', 'See you soon!')
STORY = [
    ('arthur', 'Dear me, what a mix-up! Let me look at the tag with my glasses.', 'やれやれ、なんという取り違えだ！眼鏡をかけて荷札を見てみよう。'),
    ('evelyn', 'Is there a name or a phone number on it?', 'そこに名前か電話番号は書いてありますか？'),
    ('arthur', 'No phone number, unfortunately. Only two initials and an old street name.', '残念ながら電話番号はありませんね。頭文字が二つと、古い通りの名前だけです。'),
    ('hannah', 'Wait, that street is right here in our neighborhood, five minutes away!', '待って、その通りならすぐこの近所で、五分離れたところですよ！'),
    ('evelyn', 'How strange! We rode the same morning train to the same district.', 'なんて不思議！同じ朝の列車に乗って、同じ地区まで来たなんて。'),
    ('arthur', 'Hannah, call the station lost and found office right away.', 'ハンナ、ただちに駅の遺失物取扱所に電話してくれ。'),
    ('hannah', 'I am dialing now... Hello? Did anyone report a swapped blue suitcase?', '今かけています…もしもし？入れ替わった青いスーツケースの届け出はありましたか？'),
    ('evelyn', 'Tell them mine has a red ribbon inside the top pocket!', '私の鞄には一番上のポケットの中に赤いリボンが入っているとお伝えして！'),
    ('hannah', 'Not yet? Please take our guesthouse number and address. Thank you!', 'まだですか？当館の電話番号と住所を控えてください。ありがとうございます！'),
    ('arthur', "They have nothing yet, ma'am, I am terribly sorry.", 'まだ何の連絡もないそうです、お客さま、誠に申し訳ございません。'),
    ('evelyn', 'It is not your fault. Still, I only have the coat on my back!', 'あなたのせいではありませんよ。とはいえ、着の身着のままこのコート一枚きりだわ！'),
    ('hannah', 'Wait one moment, Tessa in the cafe just waved to me with an idea!', 'ちょっと待ってください、カフェにいるテッサが何か思いついて私に手を振りました！'),
]
WALK = [
    (0, None, ["'やれやれ、なんという取り違えだ！眼鏡をかけて荷札を見てみよう。' 困った手違いに驚く感嘆表現の", (None, 'what a mix-up'), 'と、自分から行動を申し出る', (None, 'Let me look at the tag'), 'を使っています。']),
    (1, None, ["'そこに名前か電話番号は書いてありますか？' 何かが書かれて存在しているかを尋ねるときは疑問形の", (None, 'Is there a name or a phone number'), 'で切り出します。']),
    (2, None, ["'残念ながら電話番号はありませんね。頭文字が二つと、古い通りの名前だけです。' 期待に添えない返事を和らげるには", (None, 'unfortunately'), 'を添えるととても丁寧な響きになります。']),
    (3, None, ["'待って、その通りならすぐこの近所で、五分離れたところですよ！' 距離がどれくらい離れているかを言うときは時間の後ろに", (None, 'five minutes away'), 'を置くだけで簡単に表せます。']),
    (4, None, ["'なんて不思議！同じ朝の列車に乗って、同じ地区まで来たなんて。' 英語で同じと言うときは必ず定冠詞を伴って", (None, 'the same morning train'), 'のように表現します。']),
    (5, None, ["'ハンナ、ただちに駅の遺失物取扱所に電話してくれ。' 忘れ物や落とし物の窓口は決まった組み合わせで", (None, 'lost and found office'), 'と呼び、文末の', (None, 'right away'), 'で急ぎを伝えます。']),
    (6, None, ["'今かけています…もしもし？入れ替わった青いスーツケースの届け出はありましたか？' 今まさに番号を押している最中なので進行形の", (None, 'I am dialing now'), 'と言い、入れ替わった鞄を', (None, 'a swapped blue suitcase'), 'と説明します。']),
    (7, None, ["'私の鞄には一番上のポケットの中に赤いリボンが入っているとお伝えして！' 電話の向こうの係員たちへ伝えてほしいときは", (None, 'Tell them mine has'), 'と簡潔につなぎます。']),
    (8, None, ["'まだですか？当館の電話番号と住所を控えてください。ありがとうございます！' 現時点でまだ届いていないことを確認する短い", (None, 'Not yet'), 'と、番号を控えてもらう', (None, 'Please take our guesthouse number'), 'は電話応対の定番です。']),
    (9, None, ["'まだ何の連絡もないそうです、お客さま、誠に申し訳ございません。' 心から申し訳ない気持ちや同情を伝えるときは", (None, 'I am terribly sorry'), 'と副詞で気持ちを強めます。']),
    (10, None, ["'あなたのせいではありませんよ。とはいえ、着の身着のままこのコート一枚きりだわ！' 相手を気遣う優しい", (None, 'It is not your fault'), 'に続けて、着ている服しかない状態を', (None, 'the coat on my back'), 'と表現しています。']),
    (11, None, ["'ちょっと待ってください、カフェにいるテッサが何か思いついて私に手を振りました！' たった今起きた動作を伝える", (None, 'just waved to me'), 'では、合図を送る相手の前に前置詞を添えます。']),
]
