# Authoring module for linden-courtyard-ja-s01e04-scene-01.
ID = 'linden-courtyard-ja-s01e04-scene-01'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = 'Six Forty-Five  (六時四十五分)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah'}
INTRO = '夜明け前のフロントで、グレアムが壊れた真鍮のバルブをハンナに手渡し、石の橋の向こうにある古い金物屋までの道順を丁寧に説明します。お客さまが目を覚ます七時十五分までが勝負です。まずは場面全体を英語で聴いてみましょう。'
OPENER = 'それでは道案内のやり取りを、一文ずつ順番にたどっていきましょう。'
TRANSITION = 'では、もう一度この朝の会話を自然な速さで通して聴いてみましょう。'
OUTRO = 'ハンナはコートのポケットにバルブを入れ、石の橋へ向かって駆け出しました。次は川の向こうの小さな広場で、彼女の電話に耳を傾けましょう。それではまたすぐに。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Good morning, Graham! Are the showers upstairs really cold already?', 'おはよう、グレアム！上のシャワー、本当にもう冷たくなっているの？'),
    ('graham', 'Cold as river water. Take this broken brass valve in your coat pocket.', '川の水みたいに冷たいよ。この壊れた真鍮のバルブをコートのポケットに入れていってくれ。'),
    ('hannah', 'Got it. Now tell me how to find the hardware shop.', 'わかった。じゃあ金物屋への行き方を教えて。'),
    ('graham', 'Turn left outside our gate and walk straight to the stone bridge.', 'うちの門を出たら左に曲がって、石の橋までまっすぐ歩くんだ。'),
    ('hannah', 'Left at the gate, straight to the bridge. Do I cross the river?', '門で左、橋までまっすぐね。川は渡るの？'),
    ('graham', 'Yes, cross the bridge, then pass the green pharmacy on your right.', 'ああ、橋を渡って、それから右手にある緑の薬局を通り過ぎるんだ。'),
    ('hannah', 'Bridge, then green pharmacy on the right. And after that?', '橋、それから右手に緑の薬局。そのあとは？'),
    ('graham', 'Turn left into the small square. Look for a blue wooden door.', '左に曲がって小さな広場に入る。青い木の扉を探してくれ。'),
    ('hannah', 'Does the shop have a big sign outside?', 'お店の外に大きな看板は出ているの？'),
    ('graham', 'Only a painted golden key above the door. Show the clerk this valve.', '扉の上に金色の鍵の絵が描いてあるだけだ。店員さんにこのバルブを見せてくれ。'),
    ('hannah', 'Twenty millimeters, brass, boiler valve. I will repeat it all the way!', '二十ミリ、真鍮、ボイラーのバルブ。道中ずっと繰り返して言うわ！'),
    ('graham', 'Run fast, Hannah. Room four wakes up at seven fifteen!', '急いで走ってくれ、ハンナ。四号室は七時十五分に起きるぞ！'),
]
WALK = [
    (0, None, ["'おはよう、グレアム！上のシャワー、本当にもう冷たくなっているの？' 文の最後に置かれた", (None, 'already'), 'は、予想より早く何かが起きたという驚きを表します。疑問文の末尾に来ると「もうそうなの？」という意外さがぐっと強まります。']),
    (1, None, ["'川の水みたいに冷たいよ。この壊れた真鍮のバルブをコートのポケットに入れていってくれ。' 冒頭の", (None, 'Cold as river water'), 'は、本来の比較の形から最初の語と主語を省いた口語的な言い方です。「まるで〜のように」という比喩を短く鮮やかに言えます。']),
    (2, None, ["'わかった。じゃあ金物屋への行き方を教えて。' 了解をすばやく伝える", (None, 'Got it'), 'は、理解したことを示す日常の決まり文句です。続けて疑問詞と不定詞を組み合わせた', (None, 'how to find'), 'で「行き方」を一言で尋ねています。']),
    (3, None, ["'うちの門を出たら左に曲がって、石の橋までまっすぐ歩くんだ。' 道案内の基本は命令形で、まず", (None, 'Turn left'), 'と方向を示し、次に', (None, 'walk straight to'), 'で目的地までの進み方を伝えます。命令形でも道案内では失礼になりません。']),
    (4, None, ["'門で左、橋までまっすぐね。川は渡るの？' 次の手順を確かめるときは現在形の疑問文で", (None, 'Do I cross the river'), 'と尋ねます。日本語の「渡るの？」と同じく、決まった手順を確認する自然な言い方です。']),
    (5, None, ["'ああ、橋を渡って、それから右手にある緑の薬局を通り過ぎるんだ。' 動詞の", (None, 'pass'), 'は、何かの横を進んでいくことを表します。位置を伝える', (None, 'on your right'), 'は前置詞に「オン」を使うのが決まりです。']),
    (6, None, ["'橋、それから右手に緑の薬局。そのあとは？' 復唱の後で続きを促す", (None, 'And after that'), 'は、短く上げ調子で言えば「次は？」という意味の立派な質問になります。']),
    (7, None, ["'左に曲がって小さな広場に入る。青い木の扉を探してくれ。' 中へ入っていく動きを表す前置詞を使った", (None, 'Turn left into the small square'), 'が自然です。また探し物には', (None, 'Look for'), 'を使います。形容詞は大きさや色、素材の順に並ぶ点にも注目しましょう。']),
    (8, None, ["'お店の外に大きな看板は出ているの？' 英語では店を主語にして「持っている」という動詞を使い、", (None, 'Does the shop have a big sign'), 'と尋ねます。日本語の「看板が出ている」とは発想が異なります。']),
    (9, None, ["'扉の上に金色の鍵の絵が描いてあるだけだ。店員さんにこのバルブを見せてくれ。' 過去分詞を形容詞として使う", (None, 'a painted golden key'), 'と、位置を示す', (None, 'above the door'), 'の組み合わせに注目です。「アバブ」は接触せずに上にあることを表します。']),
    (10, None, ["'二十ミリ、真鍮、ボイラーのバルブ。道中ずっと繰り返して言うわ！' 名詞を並べて覚える", (None, 'Twenty millimeters'), 'は単位が複数形になる点に注意しましょう。最後の', (None, 'all the way'), 'は、始めから終わりまで途切れずにという意味の慣用句です。']),
    (11, None, ["'急いで走ってくれ、ハンナ。四号室は七時十五分に起きるぞ！' 時刻は数を二つ並べるだけで言え、", (None, 'seven fifteen'), 'となります。また', (None, 'wakes up'), 'は部屋を主語にして、そこに泊まるお客さまを指す言い方です。']),
]
