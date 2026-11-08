# Authoring module for linden-courtyard-ja-s01e01-scene-04.
ID = 'linden-courtyard-ja-s01e01-scene-04'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'Room Four on the Second Floor  (二階の四号室)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = 'タクシーから降りてきたのは、穏やかな物腰の元ピアノ教師イヴリンです。長い列車の旅を終え、ずっしりと重い青いスーツケースを携えてフロントへやって来ました。まずは場面を通して英語を聴いてみましょう。'
OPENER = 'それでは今の丁寧な接客のやり取りを、一行ずつ見ていきましょう。'
TRANSITION = 'ではもう一度、自然な会話のテンポで聴いてみましょう。'
OUTRO = 'グレアムが重い青い鞄を運び、イヴリンは中庭を見下ろす二階の四号室へと向かいました。ところがこの青いスーツケースが、思わぬ騒動を巻き起こします。それではまた次回。'
CLOSING = ('evelyn', 'Take care!')
STORY = [
    ('hannah', "Welcome! Good morning, ma'am.", 'ようこそいらっしゃいませ！おはようございます、お客さま。'),
    ('evelyn', 'Good morning, my dear. I have a booking for Evelyn.', 'おはよう、お嬢さん。イヴリンの名前で予約しています。'),
    ('hannah', 'Yes, room four on the second floor! How was your train trip?', 'はい、二階の四号室ですね！列車の旅はいかがでしたか？'),
    ('evelyn', 'Quiet and pleasant, thank you, though this suitcase feels very heavy today.', '静かで快適でしたよ、ありがとう。ただ今日はこのスーツケースがずいぶん重く感じるけれど。'),
    ('graham', 'Allow me. Goodness, did you pack stones in here?', 'お持ちしましょう。おやまあ、この中に石でもお詰めになったのですか？'),
    ('evelyn', 'Only dresses, sheet music, and my favorite teacup!', 'ワンピースと楽譜と、私のお気に入りのティーカップだけですよ！'),
    ('hannah', 'Here is your key, number four. Breakfast is from seven thirty to ten.', 'こちらが四番の鍵でございます。ご朝食は七時半から十時までです。'),
    ('evelyn', 'Wonderful. Is the window facing the street or the courtyard?', '素敵ね。窓は通り側と中庭側のどちらに面していますか？'),
    ('hannah', 'The courtyard, right above the old tree. It is very quiet.', '中庭側で、古い木のちょうど真上です。とても静かですよ。'),
    ('evelyn', 'Just what I need. Where are the stairs?', 'まさに私が求めていた通りだわ。階段はどこかしら？'),
    ('graham', 'Right through this archway. I will carry the blue bag up for you.', 'このアーチ道を抜けたすぐ先です。青い鞄は私が上の階までお運びしますよ。'),
    ('evelyn', 'Thank you both very much.', 'お二人とも、本当にどうもありがとう。'),
]
WALK = [
    (0, None, ["'ようこそいらっしゃいませ！おはようございます、お客さま。' 女性のお客さまへ敬意を込めて呼びかけるときは文末に", (None, "Good morning, ma'am"), 'を添えるととても丁寧です。']),
    (1, None, ["'おはよう、お嬢さん。イヴリンの名前で予約しています。' ホテルに到着して予約があることを伝えるときはシンプルに", (None, 'I have a booking for Evelyn'), 'と自然に言えます。']),
    (2, None, ["'はい、二階の四号室ですね！列車の旅はいかがでしたか？' 建物の階数を表すには接触の前置詞を使って", (None, 'on the second floor'), 'と言い、旅の感想は', (None, 'How was your train trip'), 'と温かく尋ねます。']),
    (3, None, ["'静かで快適でしたよ、ありがとう。ただ今日はこのスーツケースがずいぶん重く感じるけれど。' 手に持った感触を述べるときは物を主語にして", (None, 'feels very heavy'), 'と形容詞を続けます。']),
    (4, None, ["'お持ちしましょう。おやまあ、この中に石でもお詰めになったのですか？' 手助けを申し出る上品な一言", (None, 'Allow me'), 'に続けて、過去の疑問文', (None, 'did you pack stones'), 'と冗談を添えています。']),
    (5, None, ["'ワンピースと楽譜と、私のお気に入りのティーカップだけですよ！' 音楽の譜面は数えられない名詞の組み合わせで", (None, 'sheet music'), 'と呼び、一番好きな物を', (None, 'my favorite teacup'), 'と紹介します。']),
    (6, None, ["'こちらが四番の鍵でございます。ご朝食は七時半から十時までです。' 鍵を手渡す定番表現の", (None, 'Here is your key'), 'に続けて、時間帯を', (None, 'from seven thirty to ten'), 'と案内します。']),
    (7, None, ["'素敵ね。窓は通り側と中庭側のどちらに面していますか？' 部屋や窓がどちらを向いているかを尋ねるときは", (None, 'facing the street or the courtyard'), 'という動詞の形がとても自然です。']),
    (8, None, ["'中庭側で、古い木のちょうど真上です。とても静かですよ。' 離れた上方の位置を示す前置詞に強調を添えて", (None, 'right above the old tree'), 'と情景を描いています。']),
    (9, None, ["'まさに私が求めていた通りだわ。階段はどこかしら？' 屋内階段は段がいくつも連なるため常に複数形で", (None, 'Where are the stairs'), 'と複数動詞で尋ねます。']),
    (10, None, ["'このアーチ道を抜けたすぐ先です。青い鞄は私が上の階までお運びしますよ。' 通路を抜ける動きを表す", (None, 'Right through this archway'), 'と、その場で申し出る', (None, 'I will carry the blue bag up'), 'に注目しましょう。']),
    (11, None, ["'お二人とも、本当にどうもありがとう。' 二人の相手にまとめてお礼を伝えるときは代名詞のすぐ後ろに添えて", (None, 'Thank you both very much'), 'と温かく締めくくります。']),
]
