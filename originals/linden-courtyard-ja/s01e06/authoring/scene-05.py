# Authoring module for linden-courtyard-ja-s01e06-scene-05.
ID = 'linden-courtyard-ja-s01e06-scene-05'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 6
SCENE = 5
TITLE = 'Page Two, Clause Fourteen  (二枚目の紙、第十四条)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'arthur': 'Arthur', 'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = 'フロントで頭を抱えるアーサーの横で、ケイレブが通知書の裏にクリップで留められた二枚目の紙に気づきます。そこにはポートランド旧市街法の第十四条が書かれていました。まずは英語の会話をそのまま聴いてみましょう。'
OPENER = 'では、この思いがけない逃げ道の話を一文ずつ読み解いていきます。'
TRANSITION = '最後にもう一度、ふつうの速さで場面全体を通して聴いてください。'
OUTRO = '宿はこれから十年守られることになり、アーサーの眼鏡は嬉しさのあまり鼻から落ちてしまいました。次の第六場面では、この決定をみんなで祝います。'
CLOSING = ('hannah', 'Take care!')
STORY = [
    ('arthur', "Look at page one, Caleb: 'commercial office conversion next month.' We are finished!", '一枚目を見てくれ、ケイレブ。「来月、商業用オフィスに転用」だと。もうおしまいだ！'),
    ('caleb', 'Wait a moment, sir. Did you read page two clipped underneath?', 'ちょっと待ってください。下にクリップで留めてある二枚目は読みましたか？'),
    ('arthur', 'Only small gray numbers! My heart stopped at page one!', '灰色の小さな数字ばかりだったよ！一枚目で心臓が止まったんだ！'),
    ('hannah', 'Look where Caleb is pointing with his pencil, Arthur!', 'ケイレブが鉛筆で指しているところを見て、アーサー！'),
    ('caleb', 'Clause fourteen of the Portland Old Quarter Act, and my brother outside just nodded!', 'ポートランド旧市街法の第十四条です。外にいる兄も今うなずきました！'),
    ('arthur', 'In plain words, please! What does Clause fourteen say?', 'わかりやすい言葉で頼むよ！第十四条には何と書いてあるんだ？'),
    ('caleb', 'No courtyard building over eighty years old may become private offices if the first floor serves neighbors daily.', '築八十年を超える中庭付きの建物は、一階が毎日近所の人々の役に立っている場合、個人のオフィスにしてはならない。'),
    ('hannah', "'Serves neighbors daily'... like a public morning cafe?!", '「毎日近所の人々の役に立つ」…朝の誰でも入れるカフェみたいに？！'),
    ('caleb', 'Exactly! Right now your four tables only serve overnight hotel guests.', 'その通り！今はあなた方の四つのテーブルは宿泊客にしか使われていません。'),
    ('arthur', 'Wait, if we open our courtyard gate every morning for neighborhood coffee and bread...', '待てよ、毎朝中庭の門を開けて、近所の人にコーヒーとパンを出したら…'),
    ('caleb', 'Then your guesthouse lease is protected for another ten years by city law!', 'そうすれば、この宿の賃貸契約は市の法律でさらに十年守られます！'),
    ('hannah', 'Arthur! Your glasses just fell off your nose for a happy reason!', 'アーサー！嬉しい理由で、眼鏡が鼻から落ちたわよ！'),
]
WALK = [
    (0, None, ["'一枚目を見てくれ、ケイレブ。「来月、商業用オフィスに転用」だと。もうおしまいだ！' 絶望を表す決まり文句が", (None, 'We are finished'), 'です。形容詞の“終わった”を人に使うと「もう望みがない」という意味になります。']),
    (1, None, ["'ちょっと待ってください。下にクリップで留めてある二枚目は読みましたか？' 紙の位置を説明する", (None, 'clipped underneath'), 'は、過去分詞が後ろから名詞を修飾し、さらに副詞が場所を補っている形です。']),
    (2, None, ["'灰色の小さな数字ばかりだったよ！一枚目で心臓が止まったんだ！' 大げさな比喩の", (None, 'My heart stopped at page one'), 'は日本語の「心臓が止まるかと思った」に近く、ショックの大きさを伝えます。']),
    (3, None, ["'ケイレブが鉛筆で指しているところを見て、アーサー！' 視線を誘導する", (None, 'Look where Caleb is pointing'), 'では、“見る”の直後に場所を表す節がそのまま続きます。前置詞を挟まない点に注目しましょう。']),
    (4, None, ["'ポートランド旧市街法の第十四条です。外にいる兄も今うなずきました！' 法律の条項を読み上げる", (None, 'Clause fourteen'), 'は、条項名の後ろに数字を置くのが英語の順番です。続く', (None, 'just nodded'), 'の“ちょうど”は、たった今起きたことを強調します。']),
    (5, None, ["'わかりやすい言葉で頼むよ！第十四条には何と書いてあるんだ？' 専門用語を避けてほしいときの", (None, 'In plain words, please'), 'は、飾り気のない平易な表現を求める便利な依頼の言い方です。']),
    (6, None, ["'築八十年を超える中庭付きの建物は、一階が毎日近所の人々の役に立っている場合、個人のオフィスにしてはならない。' 年齢を表す", (None, 'over eighty years old'), 'は建物にも使えます。また', (None, 'first floor'), 'はアメリカ英語では地上階のことで、イギリス英語の二階とは異なるので注意しましょう。']),
    (7, None, ["'「毎日近所の人々の役に立つ」…朝の誰でも入れるカフェみたいに？！' 例えを示す", (None, 'like a public morning cafe'), 'では、“のような”の意味の前置詞が名詞句を導いています。“公共の”は「一般に開かれた」という意味です。']),
    (8, None, ["'その通り！今はあなた方の四つのテーブルは宿泊客にしか使われていません。' 強い同意の", (None, 'Exactly'), 'という返事に続いて、', (None, 'overnight hotel guests'), 'という表現が出てきます。“一晩の”という形容詞が客の種類を限定しています。']),
    (9, None, ["'待てよ、毎朝中庭の門を開けて、近所の人にコーヒーとパンを出したら…' 条件を切り出す", (None, 'if we open our courtyard gate every morning'), 'は、未来のことでも条件節では現在形を使うという英語の規則どおりの文です。']),
    (10, None, ["'そうすれば、この宿の賃貸契約は市の法律でさらに十年守られます！' 受け身の", (None, 'is protected for another ten years'), 'では、“もう一つの”が期間に付くと「さらに十年」という延長の意味になります。']),
    (11, None, ["'アーサー！嬉しい理由で、眼鏡が鼻から落ちたわよ！' 物が外れて落ちる様子を表す", (None, 'fell off your nose'), 'は、動詞に“離れて”の副詞を組み合わせた句動詞です。“眼鏡”は英語では常に複数形です。']),
]
