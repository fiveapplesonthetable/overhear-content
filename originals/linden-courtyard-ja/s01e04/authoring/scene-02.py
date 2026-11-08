# Authoring module for linden-courtyard-ja-s01e04-scene-02.
ID = 'linden-courtyard-ja-s01e04-scene-02'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = 'The Blue Door  (青い扉)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '川を渡ったハンナは、小さな広場からグレアムに電話をかけ、最後の曲がり角を確かめます。果たして金色の鍵の看板と、ぴったりの真鍮のバルブは見つかるのでしょうか。それでは、場面全体を英語で聴いてください。'
OPENER = 'では電話越しのやり取りを、一行ずつ丁寧に見ていきましょう。'
TRANSITION = '今度は場面の最初から最後まで、通してもう一度聴いてみましょう。'
OUTRO = '予備のバルブまで手に入れたハンナは、橋を駆け戻っていきます。一方、宿の一階では、テッサとアーサーがお客さまの足止め作戦を始めていました。ではまた後ほど。'
CLOSING = ('graham', 'Bye for now!')
STORY = [
    ('hannah', 'Graham, can you hear me? I just passed the green pharmacy!', 'グレアム、聞こえる？ちょうど緑の薬局を通り過ぎたところよ！'),
    ('graham', 'Loud and clear. Are you standing by the little stone fountain?', 'はっきり聞こえるよ。小さな石の噴水のそばに立っているかい？'),
    ('hannah', 'Yes! There are two small streets on the left. Which one do I take?', 'ええ！左側に小さな通りが二本あるの。どっちに行けばいい？'),
    ('graham', 'Take the second street, beside the flower stand, not the narrow alley.', '二本目の通りだ、花屋の屋台の横の。狭い路地じゃないぞ。'),
    ('hannah', 'Walking now... oh, I see the golden key sign and the blue door!', '今歩いてる…あ、金色の鍵の看板と青い扉が見えた！'),
    ('graham', 'Good! Is the shutter open?', 'よし！シャッターは開いているかい？'),
    ('hannah', 'The clerk is unlocking it right now! Stay on the phone one second.', '店員さんがちょうど今、鍵を開けてるところ！ちょっとだけ電話を切らずに待ってて。'),
    ('graham', 'Make sure the brass ring inside is twenty millimeters wide.', '中の真鍮の輪がちゃんと幅二十ミリあるか確かめてくれ。'),
    ('hannah', 'He matched it against the old one. He has two left on the shelf!', '古いのと照らし合わせてくれたわ。棚に二つ残ってるって！'),
    ('graham', 'Buy both! A spare valve saves next winter too.', '両方買ってくれ！予備のバルブがあれば来年の冬も助かる。'),
    ('hannah', 'Paid in cash! Keep your toolbox open, I am running back across the bridge!', '現金で払ったわ！工具箱を開けておいて、今橋を走って戻ってるから！'),
    ('graham', 'Hurry, I just heard footsteps on the second floor stairs!', '急いでくれ、今二階の階段で足音が聞こえたぞ！'),
]
WALK = [
    (0, None, ["'グレアム、聞こえる？ちょうど緑の薬局を通り過ぎたところよ！' 電話の第一声として定番の", (None, 'can you hear me'), 'に続けて言うハンナの報告', (None, 'I just passed'), 'では「ジャスト」が直前に起きたばかりの出来事を表します。']),
    (1, None, ["'はっきり聞こえるよ。小さな石の噴水のそばに立っているかい？' 無線の用語から来た", (None, 'Loud and clear'), 'は、音がよく届いていると答える決まり文句です。進行形の', (None, 'standing by'), 'で今の位置を尋ねています。']),
    (2, None, ["'ええ！左側に小さな通りが二本あるの。どっちに行けばいい？' 存在を伝える", (None, 'There are two small streets'), 'は複数なので動詞が「アー」になります。道を選ぶときは「テイク」を使って', (None, 'Which one do I take'), 'と尋ねるのが自然です。']),
    (3, None, ["'二本目の通りだ、花屋の屋台の横の。狭い路地じゃないぞ。' 序数を使った", (None, 'Take the second street'), 'で道を指定し、', (None, 'beside the flower stand'), 'と目印を添えます。否定の', (None, 'not the narrow alley'), 'で間違えやすい道を先回りして除いています。']),
    (4, None, ["'今歩いてる…あ、金色の鍵の看板と青い扉が見えた！' 現在分詞だけを使った", (None, 'Walking now'), 'は、主語と動詞を省いた電話らしい実況です。目に入った瞬間の', (None, 'I see the golden key sign'), 'は、「見える」に当たる動詞を現在形で使います。']),
    (5, None, ["'よし！シャッターは開いているかい？' 形容詞の「オープン」を使った", (None, 'Is the shutter open'), 'は状態を尋ねる言い方です。開ける動作ではなく、開いている状態を聞いている点に注目しましょう。']),
    (6, None, ["'店員さんがちょうど今、鍵を開けてるところ！ちょっとだけ電話を切らずに待ってて。' 逆の意味を作る接頭辞のついた", (None, 'unlocking it right now'), 'に続く頼みの表現', (None, 'Stay on the phone'), 'は通話をつないだままにしてと頼む表現です。']),
    (7, None, ["'中の真鍮の輪がちゃんと幅二十ミリあるか確かめてくれ。' 念押しの", (None, 'Make sure'), 'は、後ろに文を続けて「〜であることを確認して」と言います。寸法は', (None, 'twenty millimeters wide'), 'のように数値の後に形容詞を置きます。']),
    (8, None, ["'古いのと照らし合わせてくれたわ。棚に二つ残ってるって！' 比べて合わせる", (None, 'matched it against the old one'), 'では前置詞「アゲンスト」が並べて比べる感じを出します。また', (None, 'two left on the shelf'), 'の「レフト」は左ではなく「残っている」の意味です。']),
    (9, None, ["'両方買ってくれ！予備のバルブがあれば来年の冬も助かる。' 二つともという意味の", (None, 'Buy both'), 'の後の理由の文では', (None, 'A spare valve'), 'が主語となって「救う」という動詞を取ります。物を主語にする英語らしい発想です。']),
    (10, None, ["'現金で払ったわ！工具箱を開けておいて、今橋を走って戻ってるから！' 支払い方法を表す", (None, 'Paid in cash'), 'は前置詞「イン」を使います。', (None, 'Keep your toolbox open'), 'は動詞と目的語に形容詞を続けて、状態を保つよう頼む形です。']),
    (11, None, ["'急いでくれ、今二階の階段で足音が聞こえたぞ！' 短い命令の", (None, 'Hurry'), 'の後に知らせの一文', (None, 'I just heard footsteps'), 'と続けます。「ヒア」の過去形は「ハード」と発音し、綴りも不規則に変わります。']),
]
