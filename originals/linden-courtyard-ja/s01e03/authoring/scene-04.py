# Authoring module for linden-courtyard-ja-s01e03-scene-04.
ID = 'linden-courtyard-ja-s01e03-scene-04'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = 'In from the Rain  (雨の中から)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb', 'tessa': 'Tessa'}
INTRO = '物静かな建築家のケイレブが、夜の雨にコートをぐっしょり濡らしてフロントに入ってきました。テッサが乾いたタオルと温かいスープを差し出し、ハンナは予約の手違いを正直に打ち明けようとします。英語の響きに耳を傾けながら、場面全体を聴いてみましょう。'
OPENER = 'それでは、雨の夜のフロントでの会話を、一行ずつ見ていきましょう。'
TRANSITION = '今度は、出迎えの場面全体を自然な速さで通して聴いてみましょう。'
OUTRO = 'ハンナの誠実な説明に、ケイレブはまず屋根裏部屋を見てみたいと答えました。次の場面では、三人で屋根裏へ上がり、ケイレブの反応を見届けます。'
CLOSING = ('caleb', 'See you soon!')
STORY = [
    ('hannah', 'Good evening! Come inside out of the rain, sir.', 'こんばんは！雨に濡れますから、どうぞ中へお入りください。'),
    ('caleb', 'Good evening. Sorry for dripping water on your clean floor.', 'こんばんは。きれいな床に水を垂らしてしまってすみません。'),
    ('hannah', 'Do not worry at all! You must be Caleb.', 'どうぞお気になさらず！ケイレブ様ですね。'),
    ('caleb', 'Yes, Caleb. I booked room seven by phone yesterday.', 'はい、ケイレブです。昨日、電話で七号室を予約しました。'),
    ('tessa', 'Here is a dry towel for your coat and a cup of hot soup, sir.', 'コート用の乾いたタオルと、温かいスープをどうぞ。'),
    ('caleb', 'Hot soup? After that cold walk in the rain, that sounds wonderful.', '温かいスープですか？あの冷たい雨の中を歩いた後だと、本当にありがたいです。'),
    ('hannah', 'Sir, before we go upstairs, I owe you an honest apology.', 'お客様、上の階へご案内する前に、正直にお詫びしなければならないことがあります。'),
    ('caleb', 'Oh? Is there a problem with my booking?', 'おや？私の予約に何か問題でも？'),
    ('hannah', 'We accidentally booked two guests into room seven tonight.', '手違いで、今夜の七号室に二人のお客さんを予約してしまったのです。'),
    ('caleb', 'Ah... in this rain? Every hotel near the station looked full.', 'ああ…この雨の中で？駅の近くのホテルはどこも満室のようでしたが。'),
    ('hannah', 'Please do not worry! We prepared our quiet third floor attic study just for you.', 'どうかご心配なく！静かな三階の屋根裏の書斎を、お客様のためだけにご用意しました。'),
    ('caleb', 'An attic study? May I see it first?', '屋根裏の書斎ですか？先に見せていただけますか？'),
]
WALK = [
    (0, None, ["'こんばんは！雨に濡れますから、どうぞ中へお入りください。' 夕方以降の挨拶", (None, 'Good evening'), 'という挨拶に続けて、', (None, 'Come inside out of the rain'), 'と言います。前置詞を二つ重ねて、雨の外へ出て中に入るという動きを描いています。']),
    (1, None, ["'こんばんは。きれいな床に水を垂らしてしまってすみません。' 謝る理由は前置詞の後に動名詞を続けて", (None, 'Sorry for dripping water'), 'と表します。しずくがぽたぽた落ちる様子を一語で表す動詞です。']),
    (2, None, ["'どうぞお気になさらず！ケイレブ様ですね。' 相手を安心させる", (None, 'Do not worry at all'), 'と、確信をもって推量する', (None, 'You must be Caleb'), 'がセットになっています。この助動詞はここでは義務ではなく推量を表します。']),
    (3, None, ["'はい、ケイレブです。昨日、電話で七号室を予約しました。' 予約するという動詞の過去形", (None, 'I booked room seven'), 'に、手段を表す', (None, 'by phone'), 'を冠詞なしで添えています。']),
    (4, None, ["'コート用の乾いたタオルと、温かいスープをどうぞ。' 差し出しながら言う", (None, 'Here is a dry towel'), 'という差し出しの後に、', (None, 'a cup of hot soup'), 'と容器を表す名詞を使って量を数えています。']),
    (5, None, ["'温かいスープですか？あの冷たい雨の中を歩いた後だと、本当にありがたいです。' 時間の前後を表す", (None, 'After that cold walk in the rain'), 'に続けて、聞こえ方の印象を伝える', (None, 'that sounds wonderful'), 'で喜びを表しています。']),
    (6, None, ["'お客様、上の階へご案内する前に、正直にお詫びしなければならないことがあります。' 借りがあるという動詞を使った", (None, 'I owe you an honest apology'), 'は、謝罪が当然の義務だという誠実な響きを持つ言い方です。']),
    (7, None, ["'おや？私の予約に何か問題でも？' 存在を尋ねる疑問文", (None, 'Is there a problem'), 'という問いの後に、', (None, 'with my booking'), 'と前置詞で対象を示すのが英語の自然な形です。']),
    (8, None, ["'手違いで、今夜の七号室に二人のお客さんを予約してしまったのです。' うっかりやってしまったことを表す副詞", (None, 'accidentally'), 'を動詞の前に置き、', (None, 'booked two guests into room seven'), 'では前置詞が対象となる部屋を示しています。']),
    (9, None, ["'ああ…この雨の中で？駅の近くのホテルはどこも満室のようでしたが。' 一つ一つすべてを表す", (None, 'Every hotel near the station'), 'は単数扱いで、', (None, 'looked full'), 'では見えるという動詞の後に形容詞が続いています。']),
    (10, None, ["'どうかご心配なく！静かな三階の屋根裏の書斎を、お客様のためだけにご用意しました。' 準備を整えたことを", (None, 'We prepared'), 'という過去形で伝え、', (None, 'just for you'), 'で特別な心配りを強調しています。']),
    (11, None, ["'屋根裏の書斎ですか？先に見せていただけますか？' 許可を丁寧に求める", (None, 'May I see it first'), 'の助動詞は、改まった場面やホテルの接客でよく使われる、控えめで上品な響きを持っています。']),
]
