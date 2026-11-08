# Authoring module for linden-courtyard-ja-s01e04-scene-03.
ID = 'linden-courtyard-ja-s01e04-scene-03'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 4
SCENE = 3
TITLE = 'Hot Cinnamon Rolls  (焼きたてシナモンロール)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'tessa': 'Tessa', 'evelyn': 'Evelyn', 'arthur': 'Arthur'}
INTRO = '一階のカフェでは、早起きのイヴリンが冷たい蛇口のことを尋ねに降りてきます。テッサとアーサーは焼きたてのシナモンロールで、なんとか彼女を引き留めようとします。さっそく場面全体を英語で聴いてみましょう。'
OPENER = 'それではカフェの朝の会話を、順を追って詳しく見ていきましょう。'
TRANSITION = 'それでは、もう一度最初から自然なスピードで聴いてみてください。'
OUTRO = 'ハンナが門を駆け抜け、アーサーはほっと胸をなで下ろしました。次はいよいよ地下のボイラー室で、お湯を取り戻す作業が始まります。ではまた後で。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('evelyn', 'Good morning! Something smells like warm cinnamon all the way upstairs!', 'おはようございます！二階までずっと、温かいシナモンのような香りがしていますよ！'),
    ('tessa', 'Good morning, Miss Evelyn! My cinnamon rolls just came out of the oven.', 'おはようございます、イヴリンさん！シナモンロールがちょうどオーブンから出てきたところです。'),
    ('arthur', "Sit right down by the sunny window, ma'am! No rush to go upstairs yet!", '日当たりのいい窓辺にどうぞお座りください！まだ二階へ急いで戻る必要はありませんよ！'),
    ('evelyn', 'Actually, I only came down to ask why the bathroom tap felt so chilly.', '実はね、浴室の蛇口がどうしてあんなに冷たかったのか聞きに降りてきただけなの。'),
    ('arthur', 'Chilly? Ah, yes! Our neighborhood water pipes take a gentle morning stretch!', '冷たかった？ああ、そうでした！この界隈の水道管は朝にゆっくり伸びをするんですよ！'),
    ('tessa', 'Have a hot cup of tea and a cinnamon roll for ten minutes first!', 'まずは十分ほど、熱い紅茶とシナモンロールを召し上がってください！'),
    ('evelyn', 'Well, nobody wise says no to warm cinnamon bread at seven in the morning.', 'そうね、朝の七時に温かいシナモンパンを断る賢い人なんていないわね。'),
    ('arthur', 'Wonderful choice! Would you like honey or apple jam beside it?', '素晴らしいご選択です！横にはちみつかりんごジャムをお付けしましょうか？'),
    ('evelyn', 'Just a little butter, thank you. Why are you looking at your watch, sir?', 'バターを少しだけでいいわ、ありがとう。どうして腕時計ばかり見ていらっしゃるの？'),
    ('arthur', 'Me? Oh, I simply love being on time! Seven fourteen is a beautiful minute!', '私ですか？いえ、ただ時間を守るのが大好きでして！七時十四分は美しい一分ですから！'),
    ('tessa', 'Look through the courtyard window, Arthur. Someone just ran through the gate!', '中庭の窓から見て、アーサー。今誰かが門を駆け抜けていったわ！'),
    ('arthur', "Saved! Excuse me one moment, ma'am, enjoy your hot tea!", '助かった！ちょっと失礼します、どうぞ熱い紅茶をお楽しみください！'),
]
WALK = [
    (0, None, ["'おはようございます！二階までずっと、温かいシナモンのような香りがしていますよ！' 香りを伝えるときは", (None, 'Something smells like warm cinnamon'), 'と、「スメル」の後に「ライク」を続けます。前の場面にも出た', (None, 'all the way upstairs'), 'が距離の長さを強調しています。']),
    (1, None, ["'おはようございます、イヴリンさん！シナモンロールがちょうどオーブンから出てきたところです。' 焼き上がりを伝える", (None, 'just came out of the oven'), 'は、「〜の中から外へ」を表す二語の前置詞を使った決まった言い方です。']),
    (2, None, ["'日当たりのいい窓辺にどうぞお座りください！まだ二階へ急いで戻る必要はありませんよ！' 勧める気持ちを強める", (None, 'Sit right down'), 'の「ライト」は「すぐに」という強調です。', (None, 'No rush'), 'は相手を気遣う短い決まり文句です。']),
    (3, None, ["'実はね、浴室の蛇口がどうしてあんなに冷たかったのか聞きに降りてきただけなの。' 文頭の", (None, 'Actually'), 'は、相手の予想と違う本題を切り出す合図です。触った感じを表す', (None, 'felt so chilly'), 'では「フィール」の過去形が使われています。']),
    (4, None, ["'冷たかった？ああ、そうでした！この界隈の水道管は朝にゆっくり伸びをするんですよ！' 苦しい言い訳の", (None, 'take a gentle morning stretch'), 'は、「テイク」と名詞を組み合わせて動作を表す英語らしい形です。水道管を人のように描いておどけています。']),
    (5, None, ["'まずは十分ほど、熱い紅茶とシナモンロールを召し上がってください！' 飲食を勧めるときは「食べる」ではなく", (None, 'Have a hot cup of tea'), 'のように「ハヴ」を使うのが自然です。文末の', (None, 'for ten minutes first'), 'で時間稼ぎの本音がにじみます。']),
    (6, None, ["'そうね、朝の七時に温かいシナモンパンを断る賢い人なんていないわね。' 否定の主語を使った", (None, 'nobody wise says no'), 'は、「ノーボディ」が主語になるので動詞は肯定形のままです。日本語の「誰も〜ない」と構造が異なります。']),
    (7, None, ["'素晴らしいご選択です！横にはちみつかりんごジャムをお付けしましょうか？' 丁寧に好みを尋ねる", (None, 'Would you like honey or apple jam'), 'は、接客で最もよく使われる形です。', (None, 'beside it'), 'で添える位置を示します。']),
    (8, None, ["'バターを少しだけでいいわ、ありがとう。どうして腕時計ばかり見ていらっしゃるの？' 控えめに頼む", (None, 'Just a little butter'), 'の後で、進行形の', (None, 'Why are you looking at your watch'), 'と尋ねます。進行形が「さっきから何度も」という様子を表します。']),
    (9, None, ["'私ですか？いえ、ただ時間を守るのが大好きでして！七時十四分は美しい一分ですから！' 動名詞を目的語にした", (None, 'I simply love being on time'), 'では、「オン・タイム」が「時間ぴったりに」を意味します。「イン・タイム」の「間に合って」とは区別しましょう。']),
    (10, None, ["'中庭の窓から見て、アーサー。今誰かが門を駆け抜けていったわ！' 窓越しに見るときは", (None, 'Look through the courtyard window'), 'と、「通して」を表す前置詞を使います。', (None, 'ran through the gate'), 'でも同じ前置詞が通り抜ける動きを描きます。']),
    (11, None, ["'助かった！ちょっと失礼します、どうぞ熱い紅茶をお楽しみください！' 安堵の一言", (None, 'Saved'), 'は「救われた」という過去分詞だけで気持ちを表します。席を外すときの', (None, 'Excuse me one moment'), 'は丁寧で便利な決まり文句です。']),
]
