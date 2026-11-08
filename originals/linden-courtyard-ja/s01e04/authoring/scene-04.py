# Authoring module for linden-courtyard-ja-s01e04-scene-04.
ID = 'linden-courtyard-ja-s01e04-scene-04'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 4
SCENE = 4
TITLE = 'Down in the Cellar  (地下室にて)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah'}
INTRO = '地下のボイラー室で、グレアムとハンナは古いバルブを外し、新しい真鍮のバルブを取り付けます。うまくいけば、宿じゅうにお湯が勢いよく戻ってくるはずです。それでは、場面全体を英語で聴いてみましょう。'
OPENER = 'では修理の手順を追いながら、一文ずつ表現を確認していきましょう。'
TRANSITION = '最後に、修理の場面全体をもう一度通して聴いてみましょう。'
OUTRO = '銅の管が温まり、お湯は三階へ向かって上っていきます。息の合った二人の朝の大仕事は、見事に成功しました。それではまたすぐにお会いしましょう。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Here are both brass valves, Graham! Catch my breath? Never!', '真鍮のバルブ、二つともあるわよ、グレアム！一息つく？とんでもない！'),
    ('graham', 'Hold this flashlight steady on the pipe joint right here.', 'この懐中電灯を、ここの管の継ぎ目にしっかり当てていてくれ。'),
    ('hannah', 'Got it! Did you turn off the main water tap already?', '了解！もう元栓は閉めたの？'),
    ('graham', 'Off and drained. Pass me the heavy wrench on your left.', '閉めて、水も抜いたよ。左にある重いレンチを取ってくれ。'),
    ('hannah', 'This big iron one? Here you go.', 'この大きな鉄のやつ？はい、どうぞ。'),
    ('graham', 'One turn, two turns... look how clean that new brass thread fits.', '一回転、二回転…見てくれ、新しい真鍮のねじ山がきれいにはまっていく。'),
    ('hannah', 'No drips at all! Can we light the boiler now?', '一滴も漏れてない！もうボイラーに火をつけてもいい？'),
    ('graham', 'Open the blue wheel slowly to the left, not too fast.', '青いハンドルをゆっくり左へ回してくれ、速すぎないようにな。'),
    ('hannah', 'Turning slowly... listen! Water is rushing in!', 'ゆっくり回してる…聞いて！水が勢いよく流れ込んでる！'),
    ('graham', 'And there goes the burner flame, steady blue, just how it should be.', 'そしてバーナーの炎がついた。安定した青色だ、まさにこうでなくちゃ。'),
    ('hannah', 'Touch the copper pipe! It is warming up already!', '銅の管を触ってみて！もう温まってきてるわ！'),
    ('graham', 'Three minutes to reach the third floor. Good run today, partner.', '三階に届くまで三分だ。今日はいい走りだったな、相棒。'),
]
WALK = [
    (0, None, ["'真鍮のバルブ、二つともあるわよ、グレアム！一息つく？とんでもない！' 物を差し出すときの", (None, 'Here are both brass valves'), 'は、複数なので「ヒア・アー」になります。', (None, 'Catch my breath'), 'は走った後に呼吸を落ち着かせることを表す慣用句です。']),
    (1, None, ["'この懐中電灯を、ここの管の継ぎ目にしっかり当てていてくれ。' 動かさずに保つよう頼む", (None, 'Hold this flashlight steady'), 'は、動詞と目的語に形容詞を続ける形です。', (None, 'right here'), 'の「ライト」は場所をぴたりと示す強調です。']),
    (2, None, ["'了解！もう元栓は閉めたの？' 機械や水道を止めるときは", (None, 'turn off'), 'を使います。家全体の水を止める', (None, 'main water tap'), 'は「主要な」を意味する形容詞がつきます。']),
    (3, None, ["'閉めて、水も抜いたよ。左にある重いレンチを取ってくれ。' 答えの", (None, 'Off and drained'), 'は、形容詞と過去分詞を並べた職人らしい簡潔な返事です。手渡しを頼む', (None, 'Pass me the heavy wrench'), 'は「人」の後に「物」を置く語順になります。']),
    (4, None, ["'この大きな鉄のやつ？はい、どうぞ。' 名詞の繰り返しを避ける", (None, 'This big iron one'), 'では「ワン」が工具の代わりをしています。手渡すときの', (None, 'Here you go'), 'も覚えておきたい定番の一言です。']),
    (5, None, ["'一回転、二回転…見てくれ、新しい真鍮のねじ山がきれいにはまっていく。' 回数を数える", (None, 'One turn, two turns'), 'では、二つ目から名詞が複数形になります。感嘆の', (None, 'look how clean'), 'は疑問詞の「ハウ」に形容詞を続けて驚きを表す形です。']),
    (6, None, ["'一滴も漏れてない！もうボイラーに火をつけてもいい？' 強い否定の", (None, 'No drips at all'), 'では、「アット・オール」が「まったく」と否定を強めます。', (None, 'light the boiler'), 'の「ライト」は動詞で「点火する」という意味です。']),
    (7, None, ["'青いハンドルをゆっくり左へ回してくれ、速すぎないようにな。' 副詞を添えた", (None, 'Open the blue wheel slowly'), 'で慎重さを促し、', (None, 'not too fast'), 'と念を押します。丸いハンドルを英語では「車輪」と呼ぶ点も面白いですね。']),
    (8, None, ["'ゆっくり回してる…聞いて！水が勢いよく流れ込んでる！' 進行形の", (None, 'Water is rushing in'), 'では、「ラッシュ」が急いで押し寄せる動きを、「イン」が中へ入る方向を表します。']),
    (9, None, ["'そしてバーナーの炎がついた。安定した青色だ、まさにこうでなくちゃ。' 目の前の出来事を示す", (None, 'there goes the burner flame'), 'は、主語と動詞が倒置された口語表現です。', (None, 'just how it should be'), 'は満足を表す言い回しです。']),
    (10, None, ["'銅の管を触ってみて！もう温まってきてるわ！' 命令形の", (None, 'Touch the copper pipe'), 'に続く喜びの声', (None, 'It is warming up already'), 'では進行形が少しずつ変化していく様子を表しています。']),
    (11, None, ["'三階に届くまで三分だ。今日はいい走りだったな、相棒。' 所要時間を示す", (None, 'Three minutes to reach the third floor'), 'は、不定詞が目的を表しています。最後の', (None, 'partner'), 'は、一緒に働く仲間への親しみを込めた呼びかけです。']),
]
