ID = 'hidamari-ryokan-s01e01-scene-03'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = '眼鏡はどこ？  (Where Are My Glasses?)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'takashi': '隆', 'mio': '美央', 'kenji': '健二'}

INTRO = 'Before the first guest arrives, inn owner Takashi hurries in from the courtyard looking flustered. Mio and Kenji watch as Takashi pats his pockets in a panic. Listen to the whole scene first.'

STORY = [
    ('takashi', '皆さん、おはようございます！ようこそ、美央さん。準備はいいですか？', 'Good morning, everyone! Welcome, Mio. Is everything ready?'),
    ('mio', 'おはようございます！はい、受付はきれいですし、鍵も揃っています。', 'Good morning! Yes, the desk is clean and the keys are ready.'),
    ('takashi', '今日来る四号室のお客さまは一週間泊まります。完璧にしましょう！', "Today's guest in room four is staying a whole week. Let's make everything perfect!"),
    ('kenji', '落ち着いてよ、隆さん。部屋はきれいだし、タオルも新しい。', 'Relax, Takashi. The room is clean and the towels are fresh.'),
    ('takashi', '予約帳を読みたいんですが、眼鏡が見つかりません！', 'I want to read the reservation book, yet I cannot find my glasses!'),
    ('mio', '上着のポケットに入っていませんか？', 'Are they in your jacket pocket?'),
    ('takashi', 'いいえ、ペンと古いレシートが三枚だけです！', 'No, only a pen and three old receipts!'),
    ('kenji', '受付の後ろの鏡を見てごらんよ、隆さん。', 'Take a look in the mirror behind the desk, Takashi.'),
    ('takashi', 'どうして鏡に眼鏡が……あ！頭の上にあります！', 'Why would my glasses be in the mirror... oh! They are on top of my head!'),
    ('mio', 'おでこの上にちゃんとありましたね。', 'Right there safe and sound on your forehead.'),
    ('takashi', '誰にも言わないでくださいね！さあ、ベルが鳴ったら明るい笑顔ですよ。', 'Please do not tell anyone! Now, smile brightly when the bell rings.'),
    ('kenji', 'ほら、ちょうど今、門の前にタクシーが来たぞ。', 'Look, a taxi just pulled up at the gate right now.'),
]

OPENER = "Takashi stays polite even in a panic over his missing reading glasses. Let's look closer at six useful expressions."

WALK = [
    (0, None, ["'Good morning, everyone! Welcome, Mio. Is everything ready?' Addressing a group politely starts with ", (None, '皆さん'), ", meaning 'everyone', while ", (None, '準備'), " is the word for 'preparation' or 'readiness'."]),
    (2, None, ["'Today's guest in room four is staying a whole week. Let's make everything perfect!' Notice how Takashi elevates 'guest' to ", (None, 'お客さま'), ', the respectful hospitality word you hear in every Japanese inn and shop.']),
    (4, None, ["'I want to read the reservation book, yet I cannot find my glasses!' Here ", (None, '眼鏡'), " literally combines 'eye' and 'mirror' to mean 'glasses', followed by ", (None, '見つかりません'), " for 'cannot be found'."]),
    (6, None, ["'No, only a pen and three old receipts!' Japanese counts flat thin things like paper receipts with a special counter inside ", (None, '三枚'), ", meaning 'three flat sheets', capped off by ", (None, 'だけ'), " for 'only'."]),
    (8, None, ["'Why would my glasses be in the mirror... oh! They are on top of my head!' Location words work like nouns in Japanese: ", (None, '頭'), " means 'head' and ", (None, '上'), " means 'top' or 'above'."]),
    (11, None, ["'Look, a taxi just pulled up at the gate right now.' Kenji gets their attention with ", (None, 'ほら'), ", a handy little word meaning 'look!' or 'see there!', as ", (None, 'タクシー'), ' arrives outside.']),
]

TRANSITION = "Now let's hear the whole glasses mix-up again from beginning to end."

OUTRO = 'Takashi found his glasses perched on his own forehead right as the taxi arrived at the gate. Relax and let the rhythm of the words sink in; see you next time.'

CLOSING = ('takashi', 'また会いましょう！')
