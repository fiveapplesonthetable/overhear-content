# Authoring module for linden-courtyard-ja-s01e06-scene-02.
ID = 'linden-courtyard-ja-s01e06-scene-02'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 6
SCENE = 2
TITLE = 'The Wooden Train  (木の機関車)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'caleb': 'Caleb', 'owen': 'Owen', 'evelyn': 'Evelyn'}
INTRO = 'ケイレブが差し出した白い包みの中には、祖父が彫った木の機関車が入っていました。兄弟が昔の思い出に浸っていると、子どものころのピアノの先生イヴリンが近づいてきて声をかけます。ではさっそく英語の会話に耳を傾けてみましょう。'
OPENER = '思いがけない再会が二重に重なるこの場面を、一文ずつ確かめていきましょう。'
TRANSITION = '今度は場面全体を、登場人物の気持ちを想像しながら通しで聴いてみましょう。'
OUTRO = '木の機関車とピアノの先生が、兄弟を子どものころへ連れ戻してくれました。一方そのころ、フロントでは別の心配ごとが持ち上がっています。それではまた次の場面で。'
CLOSING = ('evelyn', 'See you later!')
STORY = [
    ('caleb', 'Before the movers cleared Linden Street, I saved this box from the attic shelf.', '引っ越し業者がリンデン通りの家を空にする前に、屋根裏の棚からこの箱を救い出しておいたんだ。'),
    ('owen', "Open the white paper... no! Grandfather's carved wooden train engine!", '白い紙を開けて…まさか！祖父が彫った木の機関車じゃないか！'),
    ('caleb', 'Look underneath the wheels. Your name and mine are still penciled there.', '車輪の下を見て。兄さんの名前と僕の名前が、まだ鉛筆で書いてあるよ。'),
    ('owen', 'I thought this was lost when we sold the house! Why keep it for me?', '家を売ったときになくなったと思ってた！どうして俺のために取っておいたんだ？'),
    ('caleb', 'Because a house is brick and timber, Owen, while family is what we keep.', '家はれんがと材木でできているけど、オーウェン、家族は僕たちが守っていくものだからさ。'),
    ('evelyn', 'And you two boys kept the best part of Number twelve right here.', 'そしてあなたたち二人は、十二番地のいちばん素敵なところを、ちゃんとここに持ってきたのね。'),
    ('owen', "Excuse me, ma'am... wait. That voice! Miss Evelyn, my piano teacher?!", '失礼ですが、奥さん…待ってください。その声！イヴリン先生、僕のピアノの先生ですか？！'),
    ('evelyn', 'Still waiting for you to play your F major scale slowly, Owen!', 'ヘ長調の音階をゆっくり弾いてくれるのを、まだ待っているのよ、オーウェン！'),
    ('owen', 'Am I dreaming?! Did you plan this whole reunion, Caleb?', '夢を見てるのか？！この再会、全部お前が計画したのか、ケイレブ？'),
    ('caleb', "Pure luck, and one swapped blue suitcase on Monday morning's train!", 'ただの偶然さ。それと、月曜の朝の列車で取り違えた青いスーツケースが一つ！'),
    ('evelyn', 'Life arranges better duets than we do, my dear boys.', '人生は、私たちよりずっと上手に二重奏を仕立ててくれるものよ、可愛い坊やたち。'),
    ('owen', 'Please sit with us, Miss Evelyn! Tell me I am not twenty-five years late for my lesson!', 'どうぞご一緒に座ってください、イヴリン先生！レッスンに二十五年遅刻したわけじゃないと言ってください！'),
]
WALK = [
    (0, None, ["'引っ越し業者がリンデン通りの家を空にする前に、屋根裏の棚からこの箱を救い出しておいたんだ。' 時を表す接続詞で始まる", (None, 'Before the movers cleared Linden Street'), 'に注目しましょう。ここでの動詞は「片付けて空にする」という意味で、業者を表す名詞は動詞に語尾を付けて作られています。']),
    (1, None, ["'白い紙を開けて…まさか！祖父が彫った木の機関車じゃないか！' 名詞の前に形容詞を三つ重ねた", (None, 'carved wooden train engine'), 'では、過去分詞が「彫られた」、次の語が「木製の」を表します。英語では状態、材質、種類の順に並べるのが自然です。']),
    (2, None, ["'車輪の下を見て。兄さんの名前と僕の名前が、まだ鉛筆で書いてあるよ。' 「真下に」を表す前置詞を使った", (None, 'Look underneath the wheels'), 'では、上に何かがかぶさっている下側という感じが出ます。単純な「下」よりも、隠れた場所を指す語です。']),
    (3, None, ["'家を売ったときになくなったと思ってた！どうして俺のために取っておいたんだ？' すでにそうなっていたと思い込んでいた内容を", (None, 'I thought this was lost'), 'と言っています。受け身の形で「失われた状態だった」と表すのが英語らしい言い方です。']),
    (4, None, ["'家はれんがと材木でできているけど、オーウェン、家族は僕たちが守っていくものだからさ。' 対比の接続詞を使った", (None, 'while family is what we keep'), 'では、関係代名詞が「…するもの」という名詞のかたまりを作ります。前半の家と後半の家族がくっきり対比されます。']),
    (5, None, ["'そしてあなたたち二人は、十二番地のいちばん素敵なところを、ちゃんとここに持ってきたのね。' 場所を強調する", (None, 'right here'), 'では、副詞が「まさに、ちょうど」という意味で後ろの語を強めます。右という意味ではないので注意しましょう。']),
    (6, None, ["'失礼ですが、奥さん…待ってください。その声！イヴリン先生、僕のピアノの先生ですか？！' 年上の女性への丁寧な呼びかけが", (None, "ma'am"), 'です。もとは長い敬称を縮めた形で、名前を知らない相手にも礼儀正しく話しかけられます。']),
    (7, None, ["'ヘ長調の音階をゆっくり弾いてくれるのを、まだ待っているのよ、オーウェン！' 冗談めかした出だしの", (None, 'Still waiting for you to play'), 'は、主語と助動詞が省かれた会話らしい形です。前置詞の後ろに相手と不定詞を続け、「あなたが…するのを待つ」となります。']),
    (8, None, ["'夢を見てるのか？！この再会、全部お前が計画したのか、ケイレブ？' 信じられない気持ちを表す", (None, 'Am I dreaming'), 'は、進行形の疑問文です。今この瞬間のことを尋ねるので、日本語の「見てるのか」と同じ感覚で使えます。']),
    (9, None, ["'ただの偶然さ。それと、月曜の朝の列車で取り違えた青いスーツケースが一つ！' 形容詞で強めた", (None, 'Pure luck'), 'では、もとは「混じりけのない」という意味の語が「まったくの」と運を強調します。計画ではないと笑って否定する言い方です。']),
    (10, None, ["'人生は、私たちよりずっと上手に二重奏を仕立ててくれるものよ、可愛い坊やたち。' ピアノの先生らしい比喩の", (None, 'Life arranges better duets'), 'に注目しましょう。この動詞は音楽で「編曲する」という意味もあり、出来事を「手配する」との掛け言葉になっています。']),
    (11, None, ["'どうぞご一緒に座ってください、イヴリン先生！レッスンに二十五年遅刻したわけじゃないと言ってください！' 遅れた長さを前に置く", (None, 'twenty-five years late'), 'では、期間を表す語句が形容詞の前に来て「どれだけ遅れたか」を示します。数をハイフンでつなぐ書き方も覚えておきましょう。']),
]
