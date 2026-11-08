# Authoring module for linden-courtyard-ja-s01e01-scene-08.
ID = 'linden-courtyard-ja-s01e01-scene-08'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = 'Left on the Step  (石段に置かれた鞄)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '夜の九時、静まり返った宿の門のベルが突然鳴りました。ハンナとグレアムが一緒に外へ出てみると、中庭には誰の姿もなく、石段の上に濃紺のスーツケースがぽつんと置かれています。まずは第一話の締めくくりを英語で聴いてみましょう。'
OPENER = 'それでは夜のミステリーが動き出す会話を、一行ずつ見ていきましょう。'
TRANSITION = 'ではもう一度、緊迫感のあるやり取りを最初から聴いてみましょう。'
OUTRO = 'イヴリンの本物のスーツケースは無事に戻りましたが、差出人不明の封筒には金曜日まで自分の青い鞄を預かってほしいと書かれていました。ハンナの二日目も退屈する暇はなさそうです。それでは良い夜をお過ごしください。'
CLOSING = ('graham', 'Have a good night!')
STORY = [
    ('hannah', 'Did you hear that, Graham? Someone just rang the gate bell!', '今の聞こえましたか、グレアム？たった今、誰かが門のベルを鳴らしました！'),
    ('graham', "At nine o'clock? Stay here, let us open the door together.", '九時にかい？ここにいて、一緒にドアを開けよう。'),
    ('hannah', 'Hello? Good evening! Nobody is standing in the courtyard!', 'もしもし？こんばんは！中庭には誰も立っていませんよ！'),
    ('graham', 'Wait. Look down on the stone step.', '待って。足元の石段の上を見てごらん。'),
    ('hannah', "Another dark blue suitcase! Is this Miss Evelyn's bag?", 'もう一つの濃紺のスーツケース！これってミス・イヴリンの鞄ですか？'),
    ('graham', 'Check the zipper... yes, her initials are right here!', 'ファスナーを調べてみよう…ああ、まさにここに彼女のイニシャルがあるぞ！'),
    ('hannah', 'Why did the person run away without taking his own suitcase back?', 'どうしてその人は、自分のスーツケースを持ち帰らずに逃げてしまったのでしょう？'),
    ('graham', 'Look, there is a folded white envelope taped to the handle.', '見て、持ち手に折りたたまれた白い封筒がテープで貼られているよ。'),
    ('hannah', "Let me read it: 'Sorry for the mistake. Please keep my blue bag until Friday.'", '読ませて。「間違えてすみません。金曜日まで私の青い鞄を預かっておいてください」ですって。'),
    ('graham', 'Until Friday? No name, no signature!', '金曜日までだって？名前もなければ、署名もないぞ！'),
    ('hannah', 'Why leave your own shoes and wooden train with strangers until Friday?', 'どうして見ず知らずの他人に、金曜日まで自分の靴や木製の列車を預けたままにするのでしょう？'),
    ('graham', 'Welcome to the Linden Courtyard Inn, Hannah. Your second day will not be boring.', 'リンデン中庭インへようこそ、ハンナ。君の二日目も退屈にはなりそうにないね。'),
]
WALK = [
    (0, None, ["'今の聞こえましたか、グレアム？たった今、誰かが門のベルを鳴らしました！' 物音が耳に入ったかを過去の疑問文で", (None, 'Did you hear that'), 'と尋ね、直前の出来事を', (None, 'just rang the gate bell'), 'と驚いて伝えます。']),
    (1, None, ["'九時にかい？ここにいて、一緒にドアを開けよう。' ぴったりの時刻を表す", (None, "At nine o'clock"), 'と、相手を誘う落ち着いた表現の', (None, 'let us open the door together'), 'に注目しましょう。']),
    (2, None, ["'もしもし？こんばんは！中庭には誰も立っていませんよ！' 夜に出会ったときの挨拶は", (None, 'Good evening'), 'を使い、誰もいない様子を進行形で', (None, 'Nobody is standing'), 'と描写します。']),
    (3, None, ["'待って。足元の石段の上を見てごらん。' 視線を下に向けるときは動詞に副詞を添えて", (None, 'Look down on the stone step'), 'と具体的に場所を示します。']),
    (4, None, ["'もう一つの濃紺のスーツケース！これってミス・イヴリンの鞄ですか？' 追加のもう一つを表す", (None, 'Another dark blue suitcase'), 'と、人名の所有格を使った', (None, "Miss Evelyn's bag"), 'の組み合わせです。']),
    (5, None, ["'ファスナーを調べてみよう…ああ、まさにここに彼女のイニシャルがあるぞ！' 米国英語では鞄の留め具を", (None, 'Check the zipper'), 'と呼び、頭文字が複数なので', (None, 'her initials are right here'), 'と複数形で受けます。']),
    (6, None, ["'どうしてその人は、自分のスーツケースを持ち帰らずに逃げてしまったのでしょう？' 何々せずにという表現は前置詞の後ろに動名詞を置いて", (None, 'without taking his own suitcase back'), 'と組み立てます。']),
    (7, None, ["'見て、持ち手に折りたたまれた白い封筒がテープで貼られているよ。' 折られた状態を表す", (None, 'a folded white envelope'), 'に、貼り付けられた状態を説明する', (None, 'taped to the handle'), 'が後ろから続きます。']),
    (8, None, ["'読ませて。「間違えてすみません。金曜日まで私の青い鞄を預かっておいてください」ですって。' お詫びの定番表現", (None, 'Sorry for the mistake'), 'に続けて、期限の終わりを示す前置詞で', (None, 'until Friday'), 'と頼んでいます。']),
    (9, None, ["'金曜日までだって？名前もなければ、署名もないぞ！' 名詞の前に否定語を直接置いた", (None, 'No name, no signature'), 'は、驚きや戸惑いを歯切れよく伝える形です。']),
    (10, None, ["'どうして見ず知らずの他人に、金曜日まで自分の靴や木製の列車を預けたままにするのでしょう？' 理由を不思議がるときは疑問詞のすぐ後ろに動詞の原形を置いて", (None, 'Why leave your own shoes'), 'と問いかけられます。']),
    (11, None, ["'リンデン中庭インへようこそ、ハンナ。君の二日目も退屈にはなりそうにないね。' 未来の予測を否定形で表す", (None, 'will not be boring'), 'で、これからの展開への期待をユーモラスに語っています。']),
]
