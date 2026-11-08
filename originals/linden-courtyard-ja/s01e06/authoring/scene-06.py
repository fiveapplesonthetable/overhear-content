# Authoring module for linden-courtyard-ja-s01e06-scene-06.
ID = 'linden-courtyard-ja-s01e06-scene-06'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 6
SCENE = 6
TITLE = 'Permanent Keys  (ずっと使える鍵)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'arthur': 'Arthur', 'tessa': 'Tessa', 'hannah': 'Hannah'}
INTRO = 'ほっとして満面の笑みを浮かべたアーサーは、テッサの朝の中庭カフェにさっそく許可を出します。そしてハンナには、ある大切な申し出が待っていました。英語の音声に耳を傾けてください。'
OPENER = 'それでは、喜びにあふれたこの会話をじっくり見ていきましょう。'
TRANSITION = '続いて、会話全体を自然なスピードでもう一度聴いてみましょう。'
OUTRO = 'ハンナは正式なフロント責任者になり、名前は消えないインクで台帳に書かれます。次は金色のランタンが灯る夜の中庭へ向かいます。'
CLOSING = ('arthur', 'See you later!')
STORY = [
    ('arthur', 'Tessa, how many cinnamon rolls and lemon cakes can your oven bake each morning?', 'テッサ、君のオーブンで毎朝シナモンロールとレモンケーキをいくつ焼ける？'),
    ('tessa', 'Double what I make now! Are we really opening the courtyard cafe to our street?', '今の倍は焼けますよ！本当に中庭のカフェを通りのみんなに開くんですか？'),
    ('arthur', 'Starting tomorrow at eight! Four tables inside, three tables under the tree!', '明日の八時からだ！中に四卓、木の下に三卓だ！'),
    ('tessa', 'My dream cafe, right here in our own courtyard! Wait until I tell the whole street!', '夢のカフェが、私たちの中庭にできるなんて！通りのみんなに話したら驚くわ！'),
    ('arthur', 'And now, Hannah, today is Friday, the last day of your five day trial week.', 'さて、ハンナ。今日は金曜日、五日間の試用期間の最終日だね。'),
    ('hannah', 'Oh! With the suitcases, the boiler, and the letter, I completely forgot!', 'まあ！スーツケースにボイラーに手紙にで、すっかり忘れていました！'),
    ('arthur', 'On Monday you opened our tricky door; since then you saved rooms, pipes, breakfast, and our lease.', '月曜日に君はあの厄介なドアを開けた。それから部屋も、配管も、朝食も、賃貸契約も救ってくれた。'),
    ('tessa', 'If you do not hire her full time, Arthur, I am hiring her in my kitchen!', 'アーサー、彼女を正社員にしないなら、私が厨房で雇いますからね！'),
    ('arthur', 'Hands off, Tessa! Hannah, would you stay as our permanent front desk manager?', '手を出すな、テッサ！ハンナ、うちの正式なフロント責任者として残ってくれないか？'),
    ('hannah', 'Stay here with all of you? Yes, a hundred times yes!', '皆さんと一緒にここに残るんですか？はい、百回でもはいです！'),
    ('arthur', "Wonderful! Your name goes in Graham's big paper book in permanent ink!", '素晴らしい！君の名前をグレアムの大きな台帳に消えないインクで書こう！'),
    ('hannah', 'Best first week of my life!', '人生で最高の最初の一週間です！'),
]
WALK = [
    (0, None, ["'テッサ、君のオーブンで毎朝シナモンロールとレモンケーキをいくつ焼ける？' 数えられる物の数を尋ねる", (None, 'how many cinnamon rolls'), 'では、後ろの名詞が必ず複数形になります。量を聞く表現とは使い分けが必要です。']),
    (1, None, ["'今の倍は焼けますよ！本当に中庭のカフェを通りのみんなに開くんですか？' 量を比べる", (None, 'Double what I make now'), 'は、“二倍”の語の後ろに「〜するもの」を表す節が続く、簡潔で口語的な言い方です。']),
    (2, None, ["'明日の八時からだ！中に四卓、木の下に三卓だ！' 開始時点を示す", (None, 'Starting tomorrow at eight'), 'は、動詞の進行形を前置詞のように使って「〜から始めて」を表します。場所の', (None, 'under the tree'), 'も合わせて覚えましょう。']),
    (3, None, ["'夢のカフェが、私たちの中庭にできるなんて！通りのみんなに話したら驚くわ！' 名詞を重ねた", (None, 'My dream cafe'), 'では、前の名詞が形容詞のように働きます。“〜するまで待って”の', (None, 'Wait until I tell'), 'は「話したらきっと驚くぞ」という楽しみな気持ちを表す決まった言い回しです。']),
    (4, None, ["'さて、ハンナ。今日は金曜日、五日間の試用期間の最終日だね。' 期間を形容詞にした", (None, 'five day trial week'), 'では、数字と名詞を組み合わせて名詞の前に置くとき、“日”が複数形にならない点がポイントです。']),
    (5, None, ["'まあ！スーツケースにボイラーに手紙にで、すっかり忘れていました！' 理由をまとめる前置詞の", (None, 'With the suitcases, the boiler, and the letter'), 'は「〜があったせいで」の意味です。副詞の', (None, 'completely forgot'), 'で忘れ方の程度を強めています。']),
    (6, None, ["'月曜日に君はあの厄介なドアを開けた。それから部屋も、配管も、朝食も、賃貸契約も救ってくれた。' 扱いにくい物を表す", (None, 'tricky door'), 'の形容詞は「こつが必要な」という意味です。さらに', (None, 'since then'), 'は過去のある時点から今までの流れを示します。']),
    (7, None, ["'アーサー、彼女を正社員にしないなら、私が厨房で雇いますからね！' 雇用形態を表す", (None, 'full time'), 'は副詞的に使われています。反対の表現はパートタイムです。']),
    (8, None, ["'手を出すな、テッサ！ハンナ、うちの正式なフロント責任者として残ってくれないか？' 横取りを制する", (None, 'Hands off'), 'は短く強い命令です。丁寧な依頼の', (None, 'would you stay'), 'は、仮定の助動詞を使うことで控えめな響きになります。']),
    (9, None, ["'皆さんと一緒にここに残るんですか？はい、百回でもはいです！' 強い承諾を表す", (None, 'a hundred times yes'), 'は、数を誇張して喜びを伝える英語らしい言い回しです。']),
    (10, None, ["'素晴らしい！君の名前をグレアムの大きな台帳に消えないインクで書こう！' 書く道具を表す", (None, 'in permanent ink'), 'は、手段の“で”に英語では“中に”の前置詞を使う点が日本語と違います。']),
    (11, None, ["'人生で最高の最初の一週間です！' 最上級を使った感嘆の", (None, 'Best first week of my life'), 'では、会話なので冒頭の冠詞と主語と動詞が省略されています。']),
]
