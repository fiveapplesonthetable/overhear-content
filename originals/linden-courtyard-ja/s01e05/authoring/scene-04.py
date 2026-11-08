# Authoring module for linden-courtyard-ja-s01e05-scene-04.
ID = 'linden-courtyard-ja-s01e05-scene-04'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 5
SCENE = 4
TITLE = 'Two Chairs Under the Tree  (木の下の二脚の椅子)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '中庭では、ハンナとテッサとグレアムが木の下に静かなテーブル席をしつらえ、吊るしたランタンの具合も確かめています。正午まで、あとわずかです。では最初に、英語で場面全体を聴いてみましょう。'
OPENER = '準備に追われる三人の会話を、一文ずつじっくり味わってみましょう。'
TRANSITION = 'それでは仕上げに、中庭の場面をもう一度通して聴いてみましょう。'
OUTRO = 'テーブルも椅子もランタンも整い、レモンケーキは網の上で冷めつつあります。あとは屋根裏で落ち着かないケイレブに声をかけるだけです。またすぐにお会いしましょう。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Let us put the small wooden table right here under the tree, away from the door.', '小さな木のテーブルを、ちょうどここ、木の下の扉から離れたところに置きましょう。'),
    ('graham', 'Good spot. Two solid chairs, facing the garden herbs instead of the lobby window.', 'いい場所だ。丈夫な椅子を二脚、ロビーの窓ではなく庭のハーブのほうに向けて置こう。'),
    ('tessa', 'Here is a clean white cloth and two blue teacups.', 'はい、清潔な白いクロスと青いティーカップを二つどうぞ。'),
    ('hannah', 'Graham, are you hanging those paper lanterns for noon?', 'グレアム、正午のためにその紙ちょうちんを吊るしているんですか？'),
    ('graham', 'The wire needed straightening anyway. Nothing sentimental about good maintenance.', 'どのみち針金をまっすぐにする必要があったんだ。きちんとした手入れに感傷なんてないさ。'),
    ('tessa', 'Oh, listen to Mister Maintenance! Yesterday you fixed the boiler, today you fix two brothers!', 'あら、ミスター・メンテナンスの言うことを聞いて！昨日はボイラーを直して、今日は兄弟二人を直すのね！'),
    ('graham', 'I fix pipes and chairs. People have to fix their own words.', '俺が直すのはパイプと椅子だ。人は自分の言葉を自分で直さなきゃならない。'),
    ('hannah', 'What time does your watch say now, Graham?', 'グレアム、あなたの時計では今何時？'),
    ('graham', 'Eleven twenty. Cake ready, Tessa?', '十一時二十分。ケーキはできたかい、テッサ？'),
    ('tessa', 'Cooling on the rack right now, golden crust and sweet lemon sugar!', 'ちょうど今、網の上で冷ましているところよ。黄金色の皮に甘いレモンシュガー！'),
    ('hannah', 'Look upstairs at the attic window: Caleb has changed his shirt three times!', '屋根裏の窓を見上げて。ケイレブがシャツを三回も着替えたわ！'),
    ('tessa', 'Go talk to him, Hannah, before he wears out the wooden floor!', '話しに行ってあげて、ハンナ。木の床がすり減ってしまう前に！'),
]
WALK = [
    (0, None, ["'小さな木のテーブルを、ちょうどここ、木の下の扉から離れたところに置きましょう。' 提案のレットアスは", (None, 'Let us put'), 'と省略せずに言うと少し改まった響きになります。場所を正確に示す', (None, 'right here'), 'のライトは「まさに」という強調です。']),
    (1, None, ["'いい場所だ。丈夫な椅子を二脚、ロビーの窓ではなく庭のハーブのほうに向けて置こう。' 動詞フェイスのイング形", (None, 'facing the garden herbs'), 'で椅子の向きを描写します。二つを比べて一方を選ぶときは', (None, 'instead of'), 'という表現を使います。']),
    (2, None, ["'はい、清潔な白いクロスと青いティーカップを二つどうぞ。' 物を差し出すときの決まり文句が", (None, 'Here is'), 'です。テーブル掛けの布は', (None, 'a clean white cloth'), 'と言い、形容詞は大きさや状態、色の順に並べるのが自然です。']),
    (3, None, ["'グレアム、正午のためにその紙ちょうちんを吊るしているんですか？' 進行形の疑問文", (None, 'are you hanging'), 'で、目の前の作業について尋ねています。', (None, 'those paper lanterns'), 'では、紙製のちょうちんを表しています。']),
    (4, None, ["'どのみち針金をまっすぐにする必要があったんだ。きちんとした手入れに感傷なんてないさ。' ニードのあとに動詞のイング形を続けると、「〜される必要がある」という受け身の意味になります。", (None, 'needed straightening'), 'がその例です。照れ隠しの', (None, 'anyway'), 'も効いています。']),
    (5, None, ["'あら、ミスター・メンテナンスの言うことを聞いて！昨日はボイラーを直して、今日は兄弟二人を直すのね！' からかいのあだ名", (None, 'Mister Maintenance'), 'は、敬称ミスターに職務名をつけた冗談です。', (None, 'today you fix two brothers'), 'では、動詞フィックスを人に使う言葉遊びが楽しめます。']),
    (6, None, ["'俺が直すのはパイプと椅子だ。人は自分の言葉を自分で直さなきゃならない。' 義務を表す", (None, 'have to'), 'は、外からの事情による必要を伝えます。オウンを所有格に添えた', (None, 'their own words'), 'は、他人任せにできないことを強調します。']),
    (7, None, ["'グレアム、あなたの時計では今何時？' 英語では時計や看板が「言う」と表現し、", (None, 'What time does your watch say'), 'と尋ねます。セイが「表示している」という意味で使われる、日本語にはない発想です。']),
    (8, None, ["'十一時二十分。ケーキはできたかい、テッサ？' 時刻は", (None, 'Eleven twenty'), 'と数字を二つ並べるだけです。続く', (None, 'Cake ready'), 'は、イズやザを省いた会話らしい短縮の疑問文です。']),
    (9, None, ["'ちょうど今、網の上で冷ましているところよ。黄金色の皮に甘いレモンシュガー！' 主語とビー動詞を省いて", (None, 'Cooling on the rack'), 'と答えています。焼き上がったケーキを置く金網がラックです。焼き色の表面は', (None, 'golden crust'), 'と言うのが定番です。']),
    (10, None, ["'屋根裏の窓を見上げて。ケイレブがシャツを三回も着替えたわ！' 上の階を見るよう促す", (None, 'Look upstairs'), 'は、副詞アップステアーズで方向を示します。', (None, 'has changed his shirt three times'), 'は現在完了で、今までの回数を数える用法です。']),
    (11, None, ["'話しに行ってあげて、ハンナ。木の床がすり減ってしまう前に！' 会話ではゴーのあとにトゥを省き", (None, 'Go talk to him'), 'と動詞を直接並べることがよくあります。使いすぎて傷めることを表す句動詞', (None, 'wears out'), 'で、落ち着きなく歩き回る様子をおどけて描いています。']),
]
