# Authoring module for linden-courtyard-ja-s01e05-scene-06.
ID = 'linden-courtyard-ja-s01e05-scene-06'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 5
SCENE = 6
TITLE = 'Ten Minutes to Twelve  (正午まであと十分)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '十一時五十分、フロントではアーサーがネクタイを整えて正午を待っています。そこへ郵便配達員が、赤い判の押された分厚い書留封筒を届けにきました。アーサーはひとまず封筒を脇に置くことにします。それでは英語で場面を聴いてみましょう。'
OPENER = 'では、そわそわしたフロントの会話を一行ずつ見ていきましょう。'
TRANSITION = 'それでは場面全体を、もう一度ふつうの速さで聴いてみましょう。'
OUTRO = '通りの先の教会の時計が正午の鐘を打ち始め、みんなの視線が鉄の門へと集まります。それではまた後で。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('arthur', 'How does my tie look today, Hannah? Zero orange juice in sight!', '今日のネクタイはどうかな、ハンナ？オレンジジュースの染みはどこにもないぞ！'),
    ('hannah', 'Sharp and spotless, Arthur! Even your glasses are on your nose instead of your forehead.', 'きりっとして染み一つありませんよ、アーサー！眼鏡までおでこじゃなくて鼻の上にあります。'),
    ('arthur', 'Progress! Today our courtyard hosts a family reunion. Quiet dignity from everyone!', '進歩だね！今日、我らが中庭は家族の再会の舞台となる。皆、静かな品位を保つように！'),
    ('tessa', 'Says the man peeking through the lace curtain every thirty seconds!', '三十秒ごとにレースのカーテンからのぞいている人の言うことですか！'),
    ('arthur', 'I am checking the weather, Tessa! Who left this thick envelope by the bell?', '天気を確かめているんだよ、テッサ！ベルのそばにこの分厚い封筒を置いたのは誰だい？'),
    ('hannah', 'The mailman just asked me to sign for it. It has a red property office stamp.', '郵便屋さんがさっき受け取りのサインを頼んできたんです。不動産事務所の赤い判が押してあります。'),
    ('arthur', "From the building landlord's lawyer? Strange, our rent is paid until next summer.", '建物の大家さんの弁護士から？妙だな、家賃は来年の夏まで払ってあるのに。'),
    ('tessa', 'Open it after twelve, boss! Look at the clock: five minutes to noon!', '開けるのは十二時を過ぎてからにしてください、ボス！時計を見て、正午まであと五分ですよ！'),
    ('arthur', 'Right you are. Paperwork can wait. Put it beside the book for now.', 'その通りだ。書類仕事は後回しにできる。ひとまず台帳の横に置いておいてくれ。'),
    ('hannah', "I placed the blue suitcase right beside Caleb's table under the tree.", '青いスーツケースは、木の下のケイレブのテーブルのすぐ横に置きました。'),
    ('tessa', 'And the teapot is hot! Everybody step back from the window!', 'それにティーポットも温まってます！みんな、窓から下がって！'),
    ('arthur', 'Listen... the church clock down the street is starting to chime twelve!', '聞いて……通りの先の教会の時計が、十二時の鐘を打ち始めたぞ！'),
]
WALK = [
    (0, None, ["'今日のネクタイはどうかな、ハンナ？オレンジジュースの染みはどこにもないぞ！' 見た目の感想を尋ねる定番の疑問文が", (None, 'How does my tie look'), 'です。動詞は「〜に見える」という意味で、主語が単数なので助動詞も三人称単数の形になります。']),
    (1, None, ["'きりっとして染み一つありませんよ、アーサー！眼鏡までおでこじゃなくて鼻の上にあります。' 身なりをほめる", (None, 'Sharp and spotless'), 'の最初の形容詞は、本来「鋭い」ですが服装については「洗練された」の意味になります。また', (None, 'instead of your forehead'), 'は二つを比べて一方を選ぶ言い方です。']),
    (2, None, ["'進歩だね！今日、我らが中庭は家族の再会の舞台となる。皆、静かな品位を保つように！' 動詞を含む", (None, 'hosts a family reunion'), 'は「主催する、場を提供する」という意味で、ここでは場所を主語にした格調高い言い回しになっています。']),
    (3, None, ["'三十秒ごとにレースのカーテンからのぞいている人の言うことですか！' 動詞を含む", (None, 'peeking through'), 'はこっそりのぞき見ることを表し、前置詞は向こう側へ通り抜ける視線を示します。冒頭の動詞一語で「よく言うよ」という皮肉を作っているのも面白いですね。']),
    (4, None, ["'天気を確かめているんだよ、テッサ！ベルのそばにこの分厚い封筒を置いたのは誰だい？' 進行形の", (None, 'I am checking the weather'), 'は、今まさにしている最中だと言い訳する口調です。疑問詞を主語にした問いでは、語順を入れ替えずにそのまま動詞を続けます。']),
    (5, None, ["'郵便屋さんがさっき受け取りのサインを頼んできたんです。不動産事務所の赤い判が押してあります。' 動詞と前置詞を組み合わせた", (None, 'sign for it'), 'は、荷物や郵便物を受け取った証として署名することを表す決まった言い方です。']),
    (6, None, ["'建物の大家さんの弁護士から？妙だな、家賃は来年の夏まで払ってあるのに。' 受け身の形を使った", (None, 'our rent is paid'), 'は、支払いが完了した状態を表します。期限を示す前置詞と組み合わせて「来年の夏まで」と範囲を区切っています。']),
    (7, None, ["'開けるのは十二時を過ぎてからにしてください、ボス！時計を見て、正午まであと五分ですよ！' 時刻の言い方", (None, 'five minutes to noon'), 'では、前置詞が「〜まで残り」という意味を持ち、分を先に言ってから基準の時刻を添えます。']),
    (8, None, ["'その通りだ。書類仕事は後回しにできる。ひとまず台帳の横に置いておいてくれ。' 少し古風な同意表現の", (None, 'Right you are'), 'は、語順を倒置して強調した言い方です。また', (None, 'Paperwork can wait'), 'は、物事を主語にして「後回しでいい」と伝える便利な表現です。']),
    (9, None, ["'青いスーツケースは、木の下のケイレブのテーブルのすぐ横に置きました。' 副詞と前置詞を重ねた", (None, 'right beside'), 'の最初の語は、ここでは「正しい」ではなく「ちょうど、すぐ」と位置を強める働きをしています。']),
    (10, None, ["'それにティーポットも温まってます！みんな、窓から下がって！' 命令文の", (None, 'step back from the window'), 'は、動詞と副詞で「後ろへ下がる」を表し、前置詞が離れる元の場所を示しています。']),
    (11, None, ["'聞いて……通りの先の教会の時計が、十二時の鐘を打ち始めたぞ！' 場所を表す", (None, 'down the street'), 'は、坂を下る意味ではなく「通りを少し行ったところ」を指します。動詞を使った', (None, 'chime twelve'), 'は、時計が鐘の音で時刻を告げることです。']),
]
