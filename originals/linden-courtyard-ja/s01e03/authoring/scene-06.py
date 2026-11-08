# Authoring module for linden-courtyard-ja-s01e03-scene-06.
ID = 'linden-courtyard-ja-s01e03-scene-06'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 3
SCENE = 6
TITLE = 'A Five-Star Sigh of Relief  (五つ星の安堵のため息)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '一階の受付では、アーサーが二重予約の解決を喜んでいます。ところが、ハンナがカウンターの上に小さな革の手帳が置き忘れられているのに気づきます。英語で場面全体を通して聴いてみてください。'
OPENER = 'ここからは、受付での会話を一行ずつ確かめていきましょう。'
TRANSITION = 'では、手帳をめぐる驚きの会話を、通しでもう一度味わってみましょう。'
OUTRO = 'ケイレブの手帳から、彼が旅行ガイドの書き手かもしれないという疑いが浮かびました。そこへ大きな金属音が響きます。第七場面では、手帳を返しに屋根裏へ向かいます。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('arthur', 'Well? Did he shout? Did he ask for his money back?', 'で？怒鳴られた？お金を返せと言われた？'),
    ('hannah', 'Neither! He loved the quiet roof beams and thanked us.', 'どちらでもないわ！静かな屋根の梁を気に入って、お礼まで言ってくれたの。'),
    ('arthur', 'Hannah, you have a gift for hospitality! My blood pressure is saved!', 'ハンナ、君にはおもてなしの才能があるよ！これで僕の血圧も救われた！'),
    ('tessa', 'He even finished every drop of vegetable soup before going up.', '上に行く前に、野菜スープも一滴残さず飲み干してくれたのよ。'),
    ('hannah', 'Wait, whose small brown leather notebook is this on the counter?', '待って、カウンターの上のこの小さな茶色い革の手帳は誰のもの？'),
    ('tessa', 'Caleb set it down when he took the dry towel from me!', 'ケイレブさんが、私から乾いたタオルを受け取るときに置いたのよ！'),
    ('arthur', 'Do not snoop, of course... wait, it fell open to the middle page!', 'もちろん、のぞき見は禁物だぞ…待て、真ん中のページがぱっと開いてしまった！'),
    ('hannah', 'Why are there neat pencil drawings of three guesthouses on our street?', 'どうしてうちの通りにある三軒の宿の、きれいな鉛筆画が描いてあるの？'),
    ('tessa', "Look at the words beside ours: 'Courtyard width, street noise, quiet score: nine out of ten!'", 'うちの絵の横の言葉を見て。「中庭の幅、通りの騒音、静けさの評価：十点中九点！」'),
    ('arthur', 'Nine out of ten?! Nobody measures courtyards unless...', '十点中九点だって？！中庭の寸法を測る人なんて、普通はいないぞ、もし…'),
    ('tessa', 'Unless he writes for the annual Portland Travel Guide!', 'もし毎年出るポートランド旅行ガイドの記者でもなければね！'),
    ('hannah', 'Quick, close it! Let us take it upstairs... wait, what is that loud clanking sound?', '早く閉じて！上へ持っていきましょう…待って、あの大きなガチャガチャいう音は何？'),
]
WALK = [
    (0, None, ["'で？怒鳴られた？お金を返せと言われた？' 返金を求める決まった言い方", (None, 'ask for his money back'), 'では、副詞が最後に来て「元の持ち主に戻す」という意味を添えています。']),
    (1, None, ["'どちらでもないわ！静かな屋根の梁を気に入って、お礼まで言ってくれたの。' 二択の質問に一語で答える", (None, 'Neither'), 'は、両方を同時に打ち消す便利な返事です。']),
    (2, None, ["'ハンナ、君にはおもてなしの才能があるよ！これで僕の血圧も救われた！' 生まれつきの才能を表すには", (None, 'a gift for hospitality'), 'のように、贈り物を意味する単語と前置詞を組み合わせます。']),
    (3, None, ["'上に行く前に、野菜スープも一滴残さず飲み干してくれたのよ。' 全部平らげたことを強調する", (None, 'every drop of'), 'は、液体を一滴ずつ数えるような細かさで「すべて」を表します。']),
    (4, None, ["'待って、カウンターの上のこの小さな茶色い革の手帳は誰のもの？' 持ち主を尋ねる疑問詞", (None, 'whose'), 'の後には名詞が続きます。形容詞が大きさ、色、素材の順に並んでいる点にも注目しましょう。']),
    (5, None, ["'ケイレブさんが、私から乾いたタオルを受け取るときに置いたのよ！' 物をそっと下ろす動作の", (None, 'set it down'), 'では、代名詞が動詞と副詞の間に挟まれる語順になります。']),
    (6, None, ["'もちろん、のぞき見は禁物だぞ…待て、真ん中のページがぱっと開いてしまった！' 他人の物をこっそり探る行為を", (None, 'snoop'), 'と言います。また本が勝手に開く様子は「落ちて開く」という発想で表しています。']),
    (7, None, ["'どうしてうちの通りにある三軒の宿の、きれいな鉛筆画が描いてあるの？' 存在を尋ねる", (None, 'Why are there'), 'は、存在を表す文の語順をひっくり返して疑問文にした形です。']),
    (8, None, ["'うちの絵の横の言葉を見て。「中庭の幅、通りの騒音、静けさの評価：十点中九点！」' 点数を伝える", (None, 'nine out of ten'), 'は、全体の中からいくつかを取り出すという感覚で、評価や割合によく使います。']),
    (9, None, ["'十点中九点だって？！中庭の寸法を測る人なんて、普通はいないぞ、もし…' 誰もしないことを言うには", (None, 'Nobody measures'), 'のように、否定の主語に肯定の動詞を合わせます。日本語のように動詞を打ち消す必要はありません。']),
    (10, None, ["'もし毎年出るポートランド旅行ガイドの記者でもなければね！' 前の人の言葉を受けて文を完成させる", (None, 'Unless he writes for'), 'は、「もし〜でない限り」という条件を表す接続詞で始まっています。']),
    (11, None, ["'早く閉じて！上へ持っていきましょう…待って、あの大きなガチャガチャいう音は何？' 金属同士がぶつかる響きを表す擬音語", (None, 'clanking'), 'は、そのまま形容詞のように名詞の前に置かれています。']),
]
