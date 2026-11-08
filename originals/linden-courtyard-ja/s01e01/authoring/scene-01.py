# Authoring module for linden-courtyard-ja-s01e01-scene-01.
ID = 'linden-courtyard-ja-s01e01-scene-01'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Lift the Handle  (ハンドルを持ち上げて)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'ポートランドの小さな宿、リンデン中庭インでの最初の朝です。新しく受付に入ったハンナが少し早めに到着すると、フロントの奥ではベテラン係のグレアムが熱いお茶を淹れています。まずは一語一句を気にせず、英語の会話全体の雰囲気を聴いてみましょう。'
OPENER = 'それでは今の会話を、一行ずつゆっくり振り返っていきましょう。'
TRANSITION = 'ではもう一度、今度は自然なスピードで場面全体を聴いてみましょう。'
OUTRO = 'ハンナは無事に中へ入り、八本の真鍮の鍵が並ぶフロントで最初の朝が始まりました。聞き取れない言葉があっても大丈夫、これから何度も出てきますよ。それではまた次回お会いしましょう。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Good morning! Excuse me, is the door locked?', 'おはようございます！すみません、ドアに鍵がかかっていますか？'),
    ('graham', 'Good morning. No, lift the handle first, then push.', 'おはよう。いや、まずハンドルを持ち上げて、それから押すんだよ。'),
    ('hannah', 'Oh, it opens! Thank you. I am Hannah, the new receptionist.', 'あっ、開きました！ありがとうございます。新しく来た受付のハンナです。'),
    ('graham', 'I am Graham. You are ten minutes early.', '私はグレアムだ。十分早い到着だね。'),
    ('hannah', 'I always walk fast on my first day. Where is the computer?', '初日はいつも速足で歩いてしまうんです。パソコンはどこにありますか？'),
    ('graham', 'In the drawer. Here we use this big paper book and a pencil.', '引き出しの中だよ。ここではこの大きな紙の台帳と鉛筆を使うんだ。'),
    ('hannah', 'A paper book? Really?', '紙の台帳ですか？本当に？'),
    ('graham', 'Paper still works when the power goes out.', '紙なら、停電になっても使えるからね。'),
    ('hannah', 'Fair enough! And these are the keys?', 'なるほど、もっともですね！それで、これらがお部屋の鍵ですか？'),
    ('graham', 'Yes, eight rooms, eight brass keys. Room four\'s guest arrives today.', 'ああ、八つの客室に八本の真鍮の鍵だ。四号室のお客さまは今日到着するよ。'),
    ('hannah', 'Great. Tell me everything I need to know.', 'わかりました。私が知っておくべきことを全部教えてください。'),
    ('graham', 'Rule one: drink hot tea first, then answer the bell.', 'ルールその一、まず熱いお茶を飲んで、それからベルに出ること。'),
]
WALK = [
    (0, None, ["'おはようございます！すみません、ドアに鍵がかかっていますか？' 朝のあいさつには", (None, 'Good morning'), 'を使い、質問するときは動詞の', (None, 'is'), 'を主語の前に出します。']),
    (1, None, ["'おはよう。いや、まずハンドルを持ち上げて、それから押すんだよ。' 手順を伝える命令文は主語を置かずに", (None, 'lift'), 'を置き、それから次に', (None, 'push'), 'と動詞の原形をそのまま並べます。']),
    (2, None, ["'あっ、開きました！ありがとうございます。新しく来た受付のハンナです。' 日本語では主語を省きますが、英語ではドアを指す代名詞を立てて", (None, 'it opens'), 'と必ず主語を添えます。']),
    (3, None, ["'私はグレアムだ。十分早い到着だね。' 予定より早く着いたことは動詞ではなく状態を表す形で", (None, 'You are ten minutes early'), 'とすっきり表現します。']),
    (4, None, ["'初日はいつも速足で歩いてしまうんです。パソコンはどこにありますか？' カレンダーの特定の日付や初日には", (None, 'on my first day'), 'という前置詞を選びます。']),
    (5, None, ["'引き出しの中だよ。ここではこの大きな紙の台帳と鉛筆を使うんだ。' 大きさと材質を名詞の前に並べて", (None, 'big paper book'), 'と前置詞なしでつなげます。']),
    (6, None, ["'紙の台帳ですか？本当に？' 相手の言葉に驚いて聞き返すときは", (None, 'Really'), 'と語尾を上げるだけで自然な相づちになります。']),
    (7, None, ["'紙なら、停電になっても使えるからね。' 「停電になる」や「電気が消える」ことは", (None, 'when the power goes out'), 'と表現します。']),
    (8, None, ["'なるほど、もっともですね！それで、これらがお部屋の鍵ですか？' 相手の理由に納得したときは", (None, 'Fair enough'), 'と返すと会話が気持ちよく弾みます。']),
    (9, None, ["'ああ、八つの客室に八本の真鍮の鍵だ。四号室のお客さまは今日到着するよ。' すでに決まっている今日の予定は現在形の", (None, 'arrives today'), 'で表すこともあります。']),
    (10, None, ["'わかりました。私が知っておくべきことを全部教えてください。' すべてを表す代名詞の", (None, 'everything'), 'のすぐ後ろに', (None, 'I need to know'), 'を直接つなげて説明します。']),
    (11, None, ["'ルールその一、まず熱いお茶を飲んで、それからベルに出ること。' 英語では電話だけでなくフロントの呼び鈴に出るときも", (None, 'answer the bell'), 'という動詞を使います。']),
]
