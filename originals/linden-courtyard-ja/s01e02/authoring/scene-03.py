# Authoring module for linden-courtyard-ja-s01e02-scene-03.
ID = 'linden-courtyard-ja-s01e02-scene-03'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = 'Counting the Change  (お釣りを数えて)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'arthur': 'Arthur', 'tessa': 'Tessa'}
INTRO = 'わずか九分で、ハンナが買い物袋を両手に抱えて息を切らしながら戻ってきました。お釣りも一セントの狂いもなく完璧でしたが、買ってきたバターの包み紙を見たテッサが声を上げます。まずは英語で聴いてみましょう。'
OPENER = 'それではお釣りの確認とキッチンの機転を、一行ずつ見ていきましょう。'
TRANSITION = 'ではもう一度、場面全体を自然なテンポで聴いてみましょう。'
OUTRO = 'うっかり買ってきた海塩バターが、とっさの機転で絶品のスクランブルエッグへと生まれ変わることになりました。それではまた後ほど。'
CLOSING = ('tessa', 'Bye for now!')
STORY = [
    ('hannah', 'Nine minutes! Here are the milk, the eggs, and the apples!', '九分です！はい、牛乳と、卵と、りんごですよ！'),
    ('tessa', 'You are a hero, Hannah! Give me the milk first for the coffee machine.', 'あなたは救世主よ、ハンナ！コーヒーマシン用にまず牛乳をちょうだい。'),
    ('arthur', 'Impressive speed! Did the shopkeeper give you a receipt?', '見事なスピードだ！お店の人はレシートをくれたかい？'),
    ('hannah', 'Right here! Everything cost thirty-eight, so here is twelve in change.', 'すぐここに！全部で三十八ドルでしたから、十二ドルのお釣りです。'),
    ('arthur', 'Ten, eleven, twelve. Exact to the last coin, thank you!', '十、十一、十二。最後の硬貨一枚までぴったりだ、ありがとう！'),
    ('tessa', 'Wait a second, Hannah... which pack of butter did you grab?', 'ちょっと待って、ハンナ…どのパックのバターを手に取ったの？'),
    ('hannah', 'The gold wrapper on the top shelf. Why?', '一番上の棚にあった金色の包み紙のものです。どうしてですか？'),
    ('tessa', 'That is extra salty sea butter! My sweet jam rolls need plain butter!', 'それ、特別に塩気が強い海塩バターよ！私の甘いジャムロールには無塩バターが必要なの！'),
    ('hannah', 'Oh no! All the wrappers looked the same when I was running!', 'そんな！走っていたから、包み紙が全部同じに見えてしまって！'),
    ('arthur', 'Can we serve salty butter with sweet strawberry jam?', '甘いいちごジャムに、塩気の強いバターを添えて出せるかな？'),
    ('tessa', 'Wait, salty butter is terrible for jam, but amazing for scrambled eggs!', '待って、塩バターはジャムには最悪だけど、スクランブルエッグには最高だわ！'),
    ('hannah', 'Phew! Quick thinking saves breakfast again.', 'ふうっ！とっさの機転がまたしても朝食を救いましたね。'),
]
WALK = [
    (0, None, ["'九分です！はい、牛乳と、卵と、りんごですよ！' 差し出す品物が複数並んでいるので動詞も複数形にして", (None, 'Here are the milk, the eggs'), 'と勢いよく渡しています。']),
    (1, None, ["'あなたは救世主よ、ハンナ！コーヒーマシン用にまず牛乳をちょうだい。' ピンチを救ってくれた相手に最大級の感謝を伝える", (None, 'You are a hero'), 'はとても明るく温かい褒め言葉です。']),
    (2, None, ["'見事なスピードだ！お店の人はレシートをくれたかい？' 素早い働きぶりを称える", (None, 'Impressive speed'), 'に続けて、過去の疑問文', (None, 'Did the shopkeeper give you'), 'で確認します。']),
    (3, None, ["'すぐここに！全部で三十八ドルでしたから、十二ドルのお釣りです。' 費用がかかったという動詞は過去形も同じ形のままで", (None, 'Everything cost thirty-eight'), 'と言い、お釣りの金額を', (None, 'twelve in change'), 'と後ろに添えます。']),
    (4, None, ["'十、十一、十二。最後の硬貨一枚までぴったりだ、ありがとう！' 一枚の狂いもなく正確であることを", (None, 'Exact to the last coin'), 'と気持ちよく確かめています。']),
    (5, None, ["'ちょっと待って、ハンナ…どのパックのバターを手に取ったの？' 一瞬待ってと呼び止める", (None, 'Wait a second'), 'に続けて、選択肢の中から尋ねる', (None, 'which pack of butter'), 'という疑問詞を使います。']),
    (6, None, ["'一番上の棚にあった金色の包み紙のものです。どうしてですか？' 棚の最上段を指すときは接触の前置詞を使って", (None, 'on the top shelf'), 'と簡潔に場所を示します。']),
    (7, None, ["'それ、特別に塩気が強い海塩バターよ！私の甘いジャムロールには無塩バターが必要なの！' 形容詞の前にさらに強める語を置いた", (None, 'extra salty'), 'と、味付けのないシンプルな', (None, 'plain butter'), 'の鮮やかな対比です。']),
    (8, None, ["'そんな！走っていたから、包み紙が全部同じに見えてしまって！' すべて同じに見えたという", (None, 'looked the same'), 'に、当時の動作の背景を表す過去進行形', (None, 'when I was running'), 'を添えています。']),
    (9, None, ["'甘いいちごジャムに、塩気の強いバターを添えて出せるかな？' 料理を何と組み合わせて提供するかを相談するときは", (None, 'serve salty butter with'), 'と表現します。']),
    (10, None, ["'待って、塩バターはジャムには最悪だけど、スクランブルエッグには最高だわ！' 相性の悪さと良さを鮮やかに対比させて", (None, 'terrible for jam'), 'である一方で', (None, 'amazing for scrambled eggs'), 'とひらめきます。']),
    (11, None, ["'ふうっ！とっさの機転がまたしても朝食を救いましたね。' ほっと息をつく間投詞の", (None, 'Phew'), 'に続けて、素早い判断力を表す', (None, 'Quick thinking'), 'を主語に立てています。']),
]
