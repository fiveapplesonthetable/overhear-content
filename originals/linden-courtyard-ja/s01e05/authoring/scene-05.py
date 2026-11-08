# Authoring module for linden-courtyard-ja-s01e05-scene-05.
ID = 'linden-courtyard-ja-s01e05-scene-05'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 5
SCENE = 5
TITLE = 'Simple Words First  (まずは簡単な言葉で)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = '正午まであと二十分。中庭のケイレブは、十九もの理由を並べた堅苦しいスピーチを何度も練習しています。見かねたハンナは、紙をしまって短く正直な三つの文だけにしようと提案します。まずは二人のやり取りを英語で聴いてみましょう。'
OPENER = 'それではハンナの温かいアドバイスを、一文ずつ味わっていきましょう。'
TRANSITION = 'では改めて、場面全体を自然な速さで聴いてみましょう。'
OUTRO = 'ケイレブは紙をポケットにしまい、三つの素直な文を胸に刻みました。正午の鐘まで、残りはあと十分です。それではお気をつけて。'
CLOSING = ('caleb', 'Take care!')
STORY = [
    ('hannah', 'Here, drink a sip of cool water, Caleb. What is on that paper?', 'はい、冷たいお水を一口どうぞ、ケイレブ。その紙には何が書いてあるの？'),
    ('caleb', 'A five minute speech explaining nineteen reasons why we were both wrong in April.', '四月に僕たちが二人とも間違っていた十九の理由を説明する、五分間のスピーチです。'),
    ('hannah', 'Nineteen reasons?! Are you welcoming your brother or reading a train schedule?', '十九の理由？！お兄さんを出迎えるの、それとも列車の時刻表を読み上げるの？'),
    ('caleb', 'When I get nervous, my sentences grow very long and formal!', '緊張すると、僕の文はすごく長くて堅苦しくなるんです！'),
    ('hannah', 'Fold that paper and put it in your pocket right now.', 'その紙を折りたたんで、今すぐポケットにしまいなさい。'),
    ('caleb', 'Without my notes, what do I say when he walks through that gate?', 'メモなしで、兄があの門を通って入ってきたら何て言えばいいんですか？'),
    ('hannah', "Start with three short sentences. First: 'Hello, Owen, thank you for coming.'", '短い文を三つから始めましょう。一つ目は「やあ、オーウェン、来てくれてありがとう」。'),
    ('caleb', "'Hello, Owen, thank you for coming.' Okay, I can remember that.", '「やあ、オーウェン、来てくれてありがとう」。よし、それなら覚えられます。'),
    ('hannah', "Second: 'I missed you these three years.'", '二つ目は「この三年間、会いたかった」。'),
    ('caleb', "'I missed you these three years.' Honest and clear. And third?", '「この三年間、会いたかった」。正直で分かりやすい。で、三つ目は？'),
    ('hannah', "'Sit down, there is hot tea and Friday lemon cake.'", '「座って。熱いお茶と金曜日のレモンケーキがあるよ」。'),
    ('caleb', 'Tea and lemon cake! Hannah, you should open a school for nervous brothers.', 'お茶とレモンケーキ！ハンナ、緊張した兄弟のための学校を開くべきですよ。'),
]
WALK = [
    (0, None, ["'はい、冷たいお水を一口どうぞ、ケイレブ。その紙には何が書いてあるの？' 相手に物を差し出すときの決まり文句が", (None, 'Here'), 'です。続く表現の', (None, 'a sip of cool water'), 'の名詞は、ほんの少しすする量を表し、数えられない水を数える単位として働いています。']),
    (1, None, ["'四月に僕たちが二人とも間違っていた十九の理由を説明する、五分間のスピーチです。' 名詞の前に置く数量表現では、複数形の語尾を付けずに", (None, 'five minute speech'), 'のように単数のまま形容詞として使うのが英語の約束です。']),
    (2, None, ["'十九の理由？！お兄さんを出迎えるの、それとも列車の時刻表を読み上げるの？' 二つの選択肢を並べてからかう疑問文です。", (None, 'train schedule'), 'は名詞を二つ重ねて一つの意味を作る複合名詞で、日本語の「列車時刻表」とよく似た作りです。']),
    (3, None, ["'緊張すると、僕の文はすごく長くて堅苦しくなるんです！' 状態の変化を表す動詞を使った", (None, 'get nervous'), 'は「緊張した状態になる」という意味です。さらに', (None, 'grow very long'), 'の動詞は、少しずつ大きくなっていく変化を表します。']),
    (4, None, ["'その紙を折りたたんで、今すぐポケットにしまいなさい。' 主語を省いて動詞の原形で始めると命令文になります。", (None, 'Fold that paper'), 'のように、親しい間柄では率直な指示もやさしく響きます。']),
    (5, None, ["'メモなしで、兄があの門を通って入ってきたら何て言えばいいんですか？' 時を表す接続詞の後では、未来のことでも現在形を使います。", (None, 'when he walks'), 'の部分が未来の助動詞を伴わないのはそのためです。']),
    (6, None, ["'短い文を三つから始めましょう。一つ目は「やあ、オーウェン、来てくれてありがとう」。' 動詞の後に前置詞を続けた", (None, 'Start with'), 'は、最初の一歩に何を使うかを示します。また', (None, 'thank you for coming'), 'では、前置詞の後の動詞が動名詞の形になっていますね。']),
    (7, None, ["'「やあ、オーウェン、来てくれてありがとう」。よし、それなら覚えられます。' 能力を表す助動詞を使った", (None, 'I can remember that'), 'は、目の前の課題に自信を取り戻した気持ちを短く伝えています。']),
    (8, None, ["'二つ目は「この三年間、会いたかった」。' 動詞を使った", (None, 'I missed you'), 'は「いなくて寂しく思う」という意味で、日本語の「会いたかった」に当たる、家族や友人への素直な気持ちの表現です。']),
    (9, None, ["'「この三年間、会いたかった」。正直で分かりやすい。で、三つ目は？' 形容詞を二つ並べた", (None, 'Honest and clear'), 'は、主語と動詞を省いた短い感想です。続く疑問は、接続詞と序数だけで次を尋ねる口語らしい言い方です。']),
    (10, None, ["'「座って。熱いお茶と金曜日のレモンケーキがあるよ」。' 存在を表す構文", (None, 'there is hot tea'), 'は、後に続く名詞の数に合わせて動詞の形を選びます。ここでは最初の名詞に合わせて単数形が使われています。']),
    (11, None, ["'お茶とレモンケーキ！ハンナ、緊張した兄弟のための学校を開くべきですよ。' 助動詞を使った", (None, 'you should open a school'), 'は、ここでは本気の忠告ではなく、相手への感謝を込めた冗談のほめ言葉として使われています。']),
]
