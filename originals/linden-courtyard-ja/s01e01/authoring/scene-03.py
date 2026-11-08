# Authoring module for linden-courtyard-ja-s01e01-scene-03.
ID = 'linden-courtyard-ja-s01e01-scene-03'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Where Are My Glasses?  (私の眼鏡はどこ？)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '朝食前のフロントに、宿のオーナーであるアーサーが慌ただしくやって来ました。今日から四号室に一週間滞在する大切なお客さまが気にかかり、老眼鏡を探して大騒ぎしています。まずは英語のやり取りを聴いてみましょう。'
OPENER = 'それでは今の場面を、一文ずつ落ち着いて確かめていきましょう。'
TRANSITION = 'ではもう一度、場面全体を通して聴いてみましょう。'
OUTRO = 'おでこに載せたままの眼鏡も無事に見つかり、門の前にはちょうどタクシーが到着しました。大切な四号室のお客さまをこれからお迎えします。それではまた後ほど。'
CLOSING = ('arthur', 'Bye for now!')
STORY = [
    ('arthur', 'Good morning, everyone! Welcome, Hannah. Is everything ready?', 'みんな、おはよう！ようこそ、ハンナ。準備はすべて整っているかい？'),
    ('hannah', 'Good morning! Yes, the desk is clean and the keys are ready.', 'おはようございます！はい、フロントは清潔ですし、鍵の準備もできています。'),
    ('arthur', "Today's guest in room four is staying all week. Everything must be perfect!", '今日の四号室のお客さまは一週間ずっと滞在される。すべて完璧でなくては！'),
    ('graham', 'Relax, Arthur. The room is clean and the towels are fresh.', '落ち着いて、アーサー。部屋はきれいだし、タオルも洗い立てだよ。'),
    ('arthur', 'I need to read the reservation book, but I cannot find my glasses!', '予約台帳を読む必要があるのに、私の眼鏡が見つからないんだ！'),
    ('hannah', 'Are they in your coat pocket?', 'コートのポケットの中に入っていませんか？'),
    ('arthur', 'No, only my pen and three old receipts!', 'いや、私のペンと古いレシートが三枚あるだけだ！'),
    ('graham', 'Look in the mirror behind the desk, boss.', 'フロントの後ろの鏡を見てごらんよ、ボス。'),
    ('arthur', 'Why would my glasses be in the... oh! They are on my head!', 'どうして私の眼鏡が鏡の中になんて…あっ！頭の上にあるじゃないか！'),
    ('hannah', 'Right there on your forehead, safe and sound.', 'まさにおでこの上に、無事におさまっていますよ。'),
    ('arthur', 'Do not tell anyone! Now, smile brightly when the bell rings.', '誰にも言わないでくれよ！さあ、ベルが鳴ったら明るく微笑んで。'),
    ('graham', 'Here comes a taxi at the gate right now.', 'ほら、たった今、門のところにタクシーが来たよ。'),
]
WALK = [
    (0, None, ["'みんな、おはよう！ようこそ、ハンナ。準備はすべて整っているかい？' すべてを表す語は英語では単数扱いになるため", (None, 'Is everything ready'), 'と単数の動詞で尋ねます。']),
    (1, None, ["'おはようございます！はい、フロントは清潔ですし、鍵の準備もできています。' 単数の机には", (None, 'the desk is clean'), 'と言い、複数の鍵には', (None, 'the keys are ready'), 'と動詞を使い分けます。']),
    (2, None, ["'今日の四号室のお客さまは一週間ずっと滞在される。すべて完璧でなくては！' 日付や時間にも所有の形を使って", (None, "Today's guest"), 'と自然に表現でき、確定した予定には', (None, 'is staying all week'), 'という進行形を使います。']),
    (3, None, ["'落ち着いて、アーサー。部屋はきれいだし、タオルも洗い立てだよ。' 焦っている相手をなだめるときは一言で", (None, 'Relax'), 'と声をかけ、清潔なタオルを', (None, 'the towels are fresh'), 'と安心させて伝えます。']),
    (4, None, ["'予約台帳を読む必要があるのに、私の眼鏡が見つからないんだ！' できないことを強く伝えるときは助動詞の否定形で", (None, 'I cannot find my glasses'), 'とはっきり言います。']),
    (5, None, ["'コートのポケットの中に入っていませんか？' 眼鏡はレンズが二枚一組で常に複数扱いのため、代名詞も複数形を使って", (None, 'Are they in your coat pocket'), 'と丁寧に尋ねます。']),
    (6, None, ["'いや、私のペンと古いレシートが三枚あるだけだ！' レシートという単語は綴りに黙字を含みますが、複数形で", (None, 'three old receipts'), 'と軽やかに発音します。']),
    (7, None, ["'フロントの後ろの鏡を見てごらんよ、ボス。' 鏡の中に映る自分の姿を見るときは前置詞に注意して", (None, 'Look in the mirror'), 'と表現します。']),
    (8, None, ["'どうして私の眼鏡が鏡の中になんて…あっ！頭の上にあるじゃないか！' 表面にぴたりと触れて載っている位置なので", (None, 'They are on my head'), 'と表現します。']),
    (9, None, ["'まさにおでこの上に、無事におさまっていますよ。' 場所を強調する", (None, 'Right there on your forehead'), 'に、無事を表す決まり文句の', (None, 'safe and sound'), 'を添えています。']),
    (10, None, ["'誰にも言わないでくれよ！さあ、ベルが鳴ったら明るく微笑んで。' 否定の命令文は先頭に", (None, 'Do not tell anyone'), 'を置き、未来の条件でも', (None, 'when the bell rings'), 'と現在形で結びます。']),
    (11, None, ["'ほら、たった今、門のところにタクシーが来たよ。' 目の前に何かがやって来たときは場所の語を先に出して", (None, 'Here comes a taxi'), 'と生き生きと伝えます。']),
]
