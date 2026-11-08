# Authoring module for linden-courtyard-ja-s01e01-scene-02.
ID = 'linden-courtyard-ja-s01e01-scene-02'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = 'Warm Rolls and Two Rings  (温かいロールパンと二回のベル)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'tessa': 'Tessa', 'graham': 'Graham'}
INTRO = 'それから五分後、朝食コーナーの方から焼きたてのパンの甘い香りがロビーいっぱいに広がります。パン職人のテッサが温かいロールパンのかごを抱えて、ハンナに挨拶しに出てきました。まずは場面を通して聴いてみましょう。'
OPENER = 'それでは今のやり取りを、一つずつ丁寧に見ていきましょう。'
TRANSITION = 'ではもう一度、会話全体の自然な流れを聴いてみましょう。'
OUTRO = '焼きたてのロールパンを手に、ハンナはキッチンに頼もしい味方ができました。親しい呼び捨てと丁寧な接客の切り替えはこれからもたびたび登場しますよ。それではまた後ほど。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('tessa', 'Hello! You must be Hannah. I am Tessa from the kitchen.', 'こんにちは！あなたがハンナね。私はキッチンのテッサよ。'),
    ('hannah', 'Nice to meet you, Tessa. Something smells wonderful!', 'はじめまして、テッサ。何かすごくいい匂いがしますね！'),
    ('tessa', 'Fresh morning rolls! Take one while it is still warm.', '焼きたての朝のロールパンよ！まだ温かいうちに一つどうぞ。'),
    ('hannah', 'Thank you! Do we use first names here?', 'ありがとうございます！ここでは下の名前で呼び合うのですか？'),
    ('tessa', 'With me, always! Leave the stiff polite talk for the guests.', '私にはいつもそうして！堅苦しい丁寧語はお客さま用に取っておいてね。'),
    ('graham', 'Tessa talks to everyone on our street like old friends.', 'テッサはこの通りの誰とでも昔からの友人のように話すんだよ。'),
    ('tessa', 'Because good coffee and warm bread make people friendly!', 'だっておいしいコーヒーと温かいパンは人を親しみやすくさせるもの！'),
    ('hannah', 'What was that bell? Somebody rang twice!', '今のベルは何ですか？誰かが二回鳴らしましたよ！'),
    ('graham', 'Nobody is there. That is the buzzer from room four.', '誰もいないよ。あれは四号室からのブザーだ。'),
    ('tessa', 'Even when room four is empty, the old wire rings twice.', '四号室が空室のときでさえ、古い配線が二回鳴るのよ。'),
    ('hannah', 'So the house says hello on its own?', 'じゃあ、この建物が自分から挨拶してくれるんですね？'),
    ('tessa', 'Exactly! You already fit right in.', 'まさにその通り！もうすっかりここに馴染んでいるわね。'),
]
WALK = [
    (0, None, ["'こんにちは！あなたがハンナね。私はキッチンのテッサよ。' 初対面の相手を見てきっとそうに違いないと親しみを込めて推測するときは", (None, 'You must be'), 'と切り出します。']),
    (1, None, ["'はじめまして、テッサ。何かすごくいい匂いがしますね！' 匂いがするという感覚の動詞", (None, 'smells'), 'の後ろには副詞ではなく形容詞の', (None, 'wonderful'), 'をそのまま置きます。']),
    (2, None, ["'焼きたての朝のロールパンよ！まだ温かいうちに一つどうぞ。' 前に出たロールパンを言い直さずに", (None, 'Take one'), 'と代名詞で受け、続けて', (None, 'while it is still warm'), 'と添えています。']),
    (3, None, ["'ありがとうございます！ここでは下の名前で呼び合うのですか？' 一般動詞の疑問文は先頭に助動詞を置いて", (None, 'Do we use first names'), 'と語順を作ります。']),
    (4, None, ["'私にはいつもそうして！堅苦しい丁寧語はお客さま用に取っておいてね。' 何かを使わずに残しておくという意味で", (None, 'Leave the stiff polite talk'), 'と軽やかに伝えています。']),
    (5, None, ["'テッサはこの通りの誰とでも昔からの友人のように話すんだよ。' 主語が三人称単数の習慣なので", (None, 'talks to everyone'), 'と語尾に音の印が付き、さらに', (None, 'like old friends'), 'とたとえています。']),
    (6, None, ["'だっておいしいコーヒーと温かいパンは人を親しみやすくさせるもの！' ある状態に変える働きを表す", (None, 'make people friendly'), 'は英語らしい簡潔な表現です。']),
    (7, None, ["'今のベルは何ですか？誰かが二回鳴らしましたよ！' 英語で二回と言うときは数字を並べずに一語で", (None, 'rang twice'), 'と表現するのが自然です。']),
    (8, None, ["'誰もいないよ。あれは四号室からのブザーだ。' 否定語を主語にして", (None, 'Nobody is there'), 'と単数形の動詞でシンプルに言い切ります。']),
    (9, None, ["'四号室が空室のときでさえ、古い配線が二回鳴るのよ。' 予想外の状況を強めるときは", (None, 'Even when room four is empty'), 'と文頭から導きます。']),
    (10, None, ["'じゃあ、この建物が自分から挨拶してくれるんですね？' 誰の手も借りずひとりでにという意味で文末に", (None, 'on its own'), 'を添えています。']),
    (11, None, ["'まさにその通り！もうすっかりここに馴染んでいるわね。' 強く同意する相づちの", (None, 'Exactly'), 'に続けて、場にぴったり溶け込む', (None, 'fit right in'), 'で褒めています。']),
]
