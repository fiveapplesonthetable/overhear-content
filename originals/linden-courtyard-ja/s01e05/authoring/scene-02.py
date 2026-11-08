# Authoring module for linden-courtyard-ja-s01e05-scene-02.
ID = 'linden-courtyard-ja-s01e05-scene-02'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 5
SCENE = 2
TITLE = 'Three Years of Silence  (三年間の沈黙)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'フロントでは、グレアムがケイレブのために青いスーツケースの鍵を開けます。ケイレブは、兄オーウェンと三年間も口をきいていない理由をぽつりぽつりと語り始めます。それでは、まず英語の会話に耳を傾けてみてください。'
OPENER = '兄弟の間に何があったのか、言葉の一つひとつを確かめていきましょう。'
TRANSITION = 'ここでもう一度、フロントでのやり取りを最初から聴き直してみましょう。'
OUTRO = '署名のない絵葉書には、兄に会いたい気持ちと、断られる怖さが詰まっていました。次はカフェの一角で、イヴリンが懐かしい金曜日の思い出を語ります。ではまた後ほど。'
CLOSING = ('graham', 'See you later!')
STORY = [
    ('graham', 'So our mystery Friday caller was sleeping upstairs under my attic roof all along.', 'つまり、謎の金曜日の電話の主は、ずっと上の屋根裏部屋で寝ていたってわけか。'),
    ('caleb', 'Sorry for the trouble, Graham. Thank you for guarding this bag all week.', 'ご迷惑をおかけしました、グレアムさん。一週間この鞄を守ってくださってありがとうございます。'),
    ('hannah', 'Why could you not simply hand Owen the wooden train at his front door?', 'どうして玄関先でオーウェンさんに木の列車を手渡すだけにできなかったの？'),
    ('caleb', 'Three years ago, after our grandfather died, Owen and I argued bitterly over selling the old house.', '三年前、祖父が亡くなったあと、オーウェンと僕は古い家を売るかどうかで激しく言い争ったんです。'),
    ('graham', 'Family houses and old memories, those arguments cut deep.', '実家と古い思い出か。そういう口論は深い傷を残すものだ。'),
    ('caleb', 'We have not spoken since that day. Last week I sent him one short postcard.', 'あの日から一度も話していません。先週、短い絵葉書を一枚だけ送りました。'),
    ('hannah', 'Asking him to meet you here on Friday at noon?', '金曜日の正午にここで会おうって頼んだの？'),
    ('caleb', "Actually, I only wrote: 'Something from Grandfather is waiting at the Linden Courtyard Inn Friday at noon.'", '実は、こう書いただけなんです。「祖父からのものが、金曜日の正午にリンデン・コートヤード・インで待っている」と。'),
    ('graham', 'Aha! You feared that if you signed your name, stubborn big brother would stay home!', 'なるほど！名前を書いたら、頑固な兄貴が家から出てこないと思ったんだな！'),
    ('caleb', 'You know older brothers well, Graham.', '兄というものをよくご存じですね、グレアムさん。'),
    ('hannah', 'Wait, were you planning to let the clerk hand him the bag and watch from across the street?!', 'えっ、じゃあ受付の人に鞄を渡させて、通りの向こうから見守るつもりだったんですか！？'),
    ('caleb', 'That was my cowardly Monday plan... before I met all of you.', 'それが月曜日の臆病な計画でした…皆さんに出会う前の。'),
]
WALK = [
    (0, None, ["'つまり、謎の金曜日の電話の主は、ずっと上の屋根裏部屋で寝ていたってわけか。' 名詞を前に重ねて形容詞のように使うのが", (None, 'our mystery Friday caller'), 'です。コーラーは電話をかけてくる人のことです。最後の', (None, 'all along'), 'は、後から気づいた驚きを込める決まり文句です。']),
    (1, None, ["'ご迷惑をおかけしました、グレアムさん。一週間この鞄を守ってくださってありがとうございます。' 軽い謝罪の定番が", (None, 'Sorry for the trouble'), 'です。感謝の理由は前置詞フォーのあとに動詞のイング形で続け、', (None, 'Thank you for guarding this bag'), 'という形で表現します。']),
    (2, None, ["'どうして玄関先でオーウェンさんに木の列車を手渡すだけにできなかったの？' ハンドは名詞の「手」だけでなく動詞の「手渡す」にもなります。", (None, 'hand Owen the wooden train'), 'では、人、物の順に目的語を二つ並べています。家の正面玄関は', (None, 'front door'), 'と言うのが一般的です。']),
    (3, None, ["'三年前、祖父が亡くなったあと、オーウェンと僕は古い家を売るかどうかで激しく言い争ったんです。' 過去のある時点は数字のあとにアゴーを置いて", (None, 'Three years ago'), 'と表します。激しい口論は副詞を添えて', (None, 'argued bitterly over selling the old house'), 'と言い、争点は前置詞オーバーで示します。']),
    (4, None, ["'実家と古い思い出か。そういう口論は深い傷を残すものだ。' 刃物で切るイメージを借りた", (None, 'cut deep'), 'という表現です。ここでのディープは副詞として働き、心に深く切り込む痛みを伝えています。']),
    (5, None, ["'あの日から一度も話していません。先週、短い絵葉書を一枚だけ送りました。' 過去から今まで続く状態は現在完了で表し、起点はシンスで示します。", (None, 'We have not spoken since that day'), 'の形です。一方、先週の出来事は単純な過去形で', (None, 'Last week I sent him one short postcard'), 'と現在完了とは区別して言います。']),
    (6, None, ["'金曜日の正午にここで会おうって頼んだの？' 主語を省いて動詞のイング形から始め、相手の話を補う聞き方です。", (None, 'Asking him to meet you'), 'のように、頼む内容はトゥ不定詞で続けます。正午は前置詞アットを使い', (None, 'at noon'), 'と言うのが決まりです。']),
    (7, None, ["'実は、こう書いただけなんです。「祖父からのものが、金曜日の正午にリンデン・コートヤード・インで待っている」と。' 相手の思い込みを訂正するときの前置きが", (None, 'Actually'), 'です。物が主語でも', (None, 'is waiting at the Linden Courtyard Inn'), 'のように進行形が使えるのが英語の面白いところです。']),
    (8, None, ["'なるほど！名前を書いたら、頑固な兄貴が家から出てこないと思ったんだな！' 恐れていた内容を条件の形で示した", (None, 'if you signed your name'), 'では、仮定のため過去形が使われています。家にこもったままでいることは', (None, 'would stay home'), 'と言い、ホームの前に前置詞は不要です。']),
    (9, None, ["'兄というものをよくご存じですね、グレアムさん。' 人やものの性質を熟知していることを", (None, 'You know older brothers well'), 'と言います。複数形にすると、特定の誰かではなく兄全般を指す言い方になります。']),
    (10, None, ["'えっ、じゃあ受付の人に鞄を渡させて、通りの向こうから見守るつもりだったんですか！？' 過去の予定を尋ねる過去進行形が", (None, 'were you planning to'), 'です。道の反対側は', (None, 'from across the street'), 'と、前置詞フロムとアクロスを重ねて表します。']),
    (11, None, ["'それが月曜日の臆病な計画でした…皆さんに出会う前の。' 形容詞の", (None, 'cowardly'), 'は語尾がリーでも副詞ではない点に気をつけましょう。最後の', (None, 'before I met all of you'), 'では、オールオブユーが「皆さん全員」という温かい響きを添えています。']),
]
