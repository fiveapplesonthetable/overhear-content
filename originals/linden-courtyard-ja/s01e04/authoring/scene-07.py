# Authoring module for linden-courtyard-ja-s01e04-scene-07.
ID = 'linden-courtyard-ja-s01e04-scene-07'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = 'Sunlight on the Tag  (名札に差す日の光)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = '荷物置き場の風通しをしようと、グレアムが青いスーツケースを運び出します。明るい日の光の下で荷札を見たイヴリンは、そこに書かれた古い住所に心当たりがある様子です。さあ、英語で聴いてみましょう。'
OPENER = 'それでは、記憶がよみがえっていく様子を一文ずつ追いかけましょう。'
TRANSITION = 'では全体をもう一度、通して聴いてみましょう。'
OUTRO = '大工とふたりの孫、そしてかばんの中の木の汽車。点と点がつながり始めました。この続きは中庭で。それでは、ひとまずさようなら。'
CLOSING = ('evelyn', 'Bye for now!')
STORY = [
    ('graham', 'Let me set this blue suitcase here for five minutes while I sweep the closet.', '物置を掃いているあいだ、この青いスーツケースを五分だけここに置かせてもらうよ。'),
    ('hannah', 'Careful with it, Graham. Friday at noon is tomorrow!', '気をつけて扱ってね、グレアム。金曜の正午って明日のことよ！'),
    ('evelyn', "Oh, is that the twin suitcase from Monday's train?", 'あら、それは月曜日の列車で一緒だった、そっくりのスーツケースですか？'),
    ('hannah', "Yes, ma'am, still waiting for its owner.", 'はい、奥さま。まだ持ち主を待っているんです。'),
    ('evelyn', 'May I look at the paper tag again here in the bright sunlight?', 'この明るい日差しの中で、もう一度紙の荷札を見てもいいかしら？'),
    ('graham', "Go right ahead, ma'am. Monday afternoon the lobby was dark.", 'どうぞどうぞ、奥さま。月曜日の午後はロビーが暗かったですからね。'),
    ('evelyn', 'Wait a moment... Number twelve, Linden Street, and two childhood initials written in the corner!', 'ちょっと待って…リンデン通り十二番地、それに角には子どもの頭文字がふたつ書かれているわ！'),
    ('hannah', 'Miss Evelyn, you look amazed! Do you know Number twelve, Linden Street?', 'ミス・イヴリン、ずいぶん驚いていらっしゃいますね！リンデン通り十二番地をご存じなんですか？'),
    ('evelyn', 'Know it? Every Friday for six years I climbed those wooden stairs to teach piano!', '知っているかですって？六年間、毎週金曜日にあの木の階段を上ってピアノを教えに行ったのよ！'),
    ('graham', 'Twenty-five years ago? In that same house?', '二十五年前ですか？その同じ家で？'),
    ('evelyn', 'A carpenter lived there with his two grandsons. The older boy played piano, and the little one loved trains!', 'あそこには大工さんがふたりの孫と住んでいたの。上の子はピアノを弾いて、下の子は汽車が大好きだったわ！'),
    ('hannah', 'A carpenter... and a little wooden toy train inside the bag!', '大工さん…それに、かばんの中の小さな木のおもちゃの汽車！'),
]
WALK = [
    (0, None, ["'物置を掃いているあいだ、この青いスーツケースを五分だけここに置かせてもらうよ。' 動詞の", (None, 'set this blue suitcase here'), 'は、そっと据えるという感じの置き方です。接続詞の', (None, 'while I sweep the closet'), 'で、同時に進む作業を表しています。']),
    (1, None, ["'気をつけて扱ってね、グレアム。金曜の正午って明日のことよ！' 形容詞だけで始める", (None, 'Careful with it'), 'は、命令文の動詞を省いた口語表現です。時刻を言うときは', (None, 'at noon'), 'のように前置詞を使います。']),
    (2, None, ["'あら、それは月曜日の列車で一緒だった、そっくりのスーツケースですか？' 名詞を形容詞のように使った", (None, 'the twin suitcase'), 'は、双子のように瓜二つという意味です。所有を表す', (None, "Monday's train"), 'は、曜日にも使える形です。']),
    (3, None, ["'はい、奥さま。まだ持ち主を待っているんです。' 年上の女性への丁寧な呼びかけ", (None, "ma'am"), 'は、もとの長い語を短くした形です。主語を省いた', (None, 'still waiting for its owner'), 'では、副詞が続いている状態を強調しています。']),
    (4, None, ["'この明るい日差しの中で、もう一度紙の荷札を見てもいいかしら？' 丁寧に許可を求める", (None, 'May I look at'), 'は、くだけた言い方よりも上品な響きがあります。光の中にいることを表す', (None, 'in the bright sunlight'), 'の前置詞にも注目しましょう。']),
    (5, None, ["'どうぞどうぞ、奥さま。月曜日の午後はロビーが暗かったですからね。' 快く許可する決まり文句が", (None, 'Go right ahead'), 'です。副詞が入ることで、遠慮はいらないという気持ちがいっそう強まります。']),
    (6, None, ["'ちょっと待って…リンデン通り十二番地、それに角には子どもの頭文字がふたつ書かれているわ！' 住所は英語では番号、通りの名の順に", (None, 'Number twelve, Linden Street'), 'と言います。過去分詞を後ろから添えた', (None, 'written in the corner'), 'は、名詞を説明する形です。']),
    (7, None, ["'ミス・イヴリン、ずいぶん驚いていらっしゃいますね！リンデン通り十二番地をご存じなんですか？' 動詞の", (None, 'you look amazed'), 'は、見た目の印象を伝える言い方で、後ろには形容詞が来ます。']),
    (8, None, ["'知っているかですって？六年間、毎週金曜日にあの木の階段を上ってピアノを教えに行ったのよ！' 相手の言葉を繰り返す", (None, 'Know it?'), 'は、当然だという驚きの返しです。続く', (None, 'Every Friday for six years'), 'で、頻度と期間を重ねています。']),
    (9, None, ["'二十五年前ですか？その同じ家で？' 過去の時点を表すときは、期間のあとに", (None, 'Twenty-five years ago'), 'のように副詞を置きます。日本語の「前」と同じく、数字のあとに続く点が覚えやすいでしょう。']),
    (10, None, ["'あそこには大工さんがふたりの孫と住んでいたの。上の子はピアノを弾いて、下の子は汽車が大好きだったわ！' 比較級を使った", (None, 'The older boy'), 'は兄弟の年長の方を指します。代名詞を使った', (None, 'the little one'), 'は、名詞のくり返しを避ける工夫です。']),
    (11, None, ["'大工さん…それに、かばんの中の小さな木のおもちゃの汽車！' 形容詞を重ねるときは、大きさ、素材、用途の順に並べて", (None, 'a little wooden toy train'), 'となります。この語順は英語らしさを身につける大切なポイントです。']),
]
