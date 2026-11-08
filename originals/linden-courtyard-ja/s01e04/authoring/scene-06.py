# Authoring module for linden-courtyard-ja-s01e04-scene-06.
ID = 'linden-courtyard-ja-s01e04-scene-06'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 4
SCENE = 6
TITLE = 'The Acoustic Architect  (音を設計する建築家)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '中庭の菩提樹の下で、ケイレブがノートのスケッチを広げます。そこに書かれていたのは、ホテルの星ではなく静けさの数字でした。ハンナとテッサが知る、ケイレブの本当の仕事とは何でしょうか。英語の会話に耳を傾けてみましょう。'
OPENER = 'では、謎がほどけていく会話を順番にたどってみましょう。'
TRANSITION = 'それでは場面をはじめから、ふつうの速さでもう一度どうぞ。'
OUTRO = 'ケイレブは音響建築家で、この界隈には家族にまつわる理由があって来たのでした。そして金曜日という言葉に、テッサははっとします。ではまた後で。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('caleb', 'Look closely at this page. It measures decibels and quietness, not hotel stars!', 'このページをよく見てください。測っているのはデシベルと静けさで、ホテルの星じゃありません！'),
    ('hannah', "Decibels? So 'nine out of ten' was not a review of my front desk?", 'デシベル？じゃあ『十点中九点』は、うちのフロントの評価じゃなかったんですか？'),
    ('caleb', 'Well, your front desk deserves ten! Honestly, though, I am an acoustic architect.', 'まあ、あなたのフロントなら十点に値しますよ！でも正直に言うと、私は音響建築家なんです。'),
    ('tessa', 'An acoustic architect! Do you design concert halls?', '音響建築家！コンサートホールを設計するんですか？'),
    ('caleb', 'Small libraries and courtyards, mostly. I measure how old stone walls block street noise.', '主に小さな図書館や中庭です。古い石の壁が通りの騒音をどう遮るかを測っているんです。'),
    ('hannah', 'That is why you listened for cars up in the attic last night!', 'だから昨夜、屋根裏で車の音に耳を澄ませていたんですね！'),
    ('caleb', 'Exactly. Outside on the avenue it is loud, yet inside this courtyard you hear leaves and birds.', 'そのとおり。外の大通りはうるさいのに、この中庭の中では木の葉や鳥の声が聞こえるでしょう。'),
    ('tessa', 'Wait until Arthur hears he panicked all night over decibels!', 'アーサーったら、デシベルのことで一晩中うろたえてたって知ったらどうなるかしら！'),
    ('caleb', 'Truthfully, I also chose this neighborhood for an old family reason.', '実を言うと、この界隈を選んだのには、昔の家族にまつわる理由もあるんです。'),
    ('hannah', 'Oh? Did your family live near here once?', 'あら？ご家族が昔この近くに住んでいたんですか？'),
    ('caleb', 'Two streets away, when I was small. Friday is... an important day for me.', '二本先の通りに、私が小さかったころ。金曜日は…私にとって大事な日なんです。'),
    ('tessa', 'Wait, did he just say Friday?!', '待って、今、金曜日って言った？！'),
]
WALK = [
    (0, None, ["'このページをよく見てください。測っているのはデシベルと静けさで、ホテルの星じゃありません！' 命令文の", (None, 'Look closely at this page'), 'では、副詞が動詞のすぐあとに来ています。さらに', (None, 'not hotel stars'), 'と否定を後ろに添えて、対比をはっきりさせています。']),
    (1, None, ["'デシベル？じゃあ『十点中九点』は、うちのフロントの評価じゃなかったんですか？' 文頭の", (None, 'So'), 'は、話の流れから結論を確かめるときの合図です。名詞の', (None, 'a review of my front desk'), 'では、前置詞が評価の対象を示しています。']),
    (2, None, ["'まあ、あなたのフロントなら十点に値しますよ！でも正直に言うと、私は音響建築家なんです。' 動詞", (None, 'deserves ten'), 'は、ふさわしいだけの価値があるという意味です。文末に置く', (None, 'though'), 'は、前の言葉に軽く反論を添える口語的な使い方です。']),
    (3, None, ["'音響建築家！コンサートホールを設計するんですか？' 母音で始まる形容詞の前では冠詞が変わり", (None, 'An acoustic architect'), 'となります。仕事の内容を聞くときは、現在形の', (None, 'Do you design concert halls'), 'で習慣的な行為を尋ねます。']),
    (4, None, ["'主に小さな図書館や中庭です。古い石の壁が通りの騒音をどう遮るかを測っているんです。' 文末に置いた", (None, 'mostly'), 'は答えの範囲をやわらかく限定します。後半の', (None, 'how old stone walls block street noise'), 'は、疑問詞で始まる名詞のかたまりです。']),
    (5, None, ["'だから昨夜、屋根裏で車の音に耳を澄ませていたんですね！' 理由に気づいたときの決まり文句が", (None, 'That is why'), 'です。さらに動詞句の', (None, 'listened for cars'), 'のように前置詞を変えると、何かが聞こえるのを待ち構えるという意味になります。']),
    (6, None, ["'そのとおり。外の大通りはうるさいのに、この中庭の中では木の葉や鳥の声が聞こえるでしょう。' 一語で強く同意する", (None, 'Exactly'), 'に続けて、接続詞の', (None, 'yet'), 'が、外のうるささと中の静けさを鮮やかに対比させています。']),
    (7, None, ["'アーサーったら、デシベルのことで一晩中うろたえてたって知ったらどうなるかしら！' 命令形の", (None, 'Wait until Arthur hears'), 'は、相手の反応が楽しみだという気持ちを表すおなじみの言い回しです。']),
    (8, None, ["'実を言うと、この界隈を選んだのには、昔の家族にまつわる理由もあるんです。' 打ち明け話の前置きとなる副詞", (None, 'Truthfully'), 'に続き、理由を表す前置詞を使った', (None, 'for an old family reason'), 'が選んだわけを説明しています。']),
    (9, None, ["'あら？ご家族が昔この近くに住んでいたんですか？' 短く興味を示す", (None, 'Oh?'), 'は、相手にもっと話してほしいと促す合図です。文末の', (None, 'once'), 'は、ここでは一度ではなく以前という意味です。']),
    (10, None, ["'二本先の通りに、私が小さかったころ。金曜日は…私にとって大事な日なんです。' 距離を表す", (None, 'Two streets away'), 'のように、数量のあとに副詞を置くと、どれだけ離れているかを示せます。続く', (None, 'when I was small'), 'は時を表す節です。']),
    (11, None, ["'待って、今、金曜日って言った？！' 副詞の", (None, 'just'), 'が過去形と一緒に使われ', (None, 'did he just say Friday'), 'と、ついさっきの発言に驚いている様子を伝えています。']),
]
