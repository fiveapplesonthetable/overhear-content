# Authoring module for linden-courtyard-ja-s01e04-scene-08.
ID = 'linden-courtyard-ja-s01e04-scene-08'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 4
SCENE = 8
TITLE = 'The Boy on the Stairs  (階段の男の子)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'evelyn': 'Evelyn', 'hannah': 'Hannah', 'caleb': 'Caleb'}
INTRO = '中庭でイヴリンが、リンデン通りの静かな弟の思い出を語ります。階段に座って音に耳を傾けていたあの男の子。ちょうどそこへケイレブが姿を現します。感動の再会の場面を、英語で聴いてみましょう。'
OPENER = 'それでは、思い出と現在が重なっていく瞬間を一行ずつ見ていきます。'
TRANSITION = 'では、この場面全体をもう一度、自然な英語で味わってください。'
OUTRO = '階段の上の小さなケイレブと、金曜日のピアノの先生。青いスーツケースの持ち主もついに名乗り出ました。次回は、すべての真実が語られます。さようなら。'
CLOSING = ('caleb', 'Goodbye!')
STORY = [
    ('hannah', 'Tell me more about the two boys on Linden Street, Miss Evelyn!', 'リンデン通りのふたりの男の子のこと、もっと聞かせてください、ミス・イヴリン！'),
    ('evelyn', 'The older brother was bold and loud, always rushing through his music scales.', 'お兄さんは大胆でにぎやかで、いつも音階を急いで弾き飛ばしていたわ。'),
    ('hannah', 'And the younger brother with the wooden train?', 'じゃあ、木の汽車を持っていた弟さんは？'),
    ('evelyn', 'Quiet as a mouse! He sat on the third stair listening to every single note.', 'ネズミみたいにおとなしい子だったわ！三段目の階段に座って、ひとつひとつの音に耳を傾けていたの。'),
    ('hannah', 'Listening to the sound of the room... wait a second!', '部屋の響きに耳を傾けて…ちょっと待って！'),
    ('evelyn', 'Whenever I finished playing, he asked why the piano sounded warmer when it rained.', '私が弾き終わるたびに、あの子は雨が降るとどうしてピアノの音が温かくなるのか聞いてきたのよ。'),
    ('caleb', 'Because wet wooden shutters soften the echo from the stone street...', '濡れた木の雨戸が、石畳の通りからの反響を和らげるからですよ…'),
    ('hannah', 'Caleb! Were you standing right there?!', 'ケイレブさん！ずっとそこに立っていたんですか？！'),
    ('evelyn', 'Good heavens... look at your eyes! Little Caleb from the third stair?!', 'まあ、なんてこと…その目！三段目の階段の、小さなケイレブなの？！'),
    ('caleb', "Miss Evelyn?! My brother's Friday piano teacher?!", 'ミス・イヴリン？！兄の金曜日のピアノの先生？！'),
    ('hannah', 'Wait, then Monday night on our step... the second blue suitcase...', '待って、じゃあ月曜日の夜、うちの玄関先で…ふたつ目の青いスーツケースは…'),
    ('caleb', 'Yes, Hannah. That blue suitcase is mine, and I owe you both the whole truth.', 'そうです、ハンナ。あの青いスーツケースは私のものです。おふたりには、本当のことを全部お話ししなければなりません。'),
]
WALK = [
    (0, None, ["'リンデン通りのふたりの男の子のこと、もっと聞かせてください、ミス・イヴリン！' 話の続きをせがむ決まり文句が", (None, 'Tell me more about'), 'です。後ろに話題となる名詞を続けるだけで使えます。']),
    (1, None, ["'お兄さんは大胆でにぎやかで、いつも音階を急いで弾き飛ばしていたわ。' 形容詞を対にした", (None, 'bold and loud'), 'で人柄を描き、句動詞の', (None, 'rushing through'), 'で、丁寧さに欠ける弾き方を表しています。']),
    (2, None, ["'じゃあ、木の汽車を持っていた弟さんは？' 文頭の接続詞で話題を移す", (None, 'And the younger brother'), 'は、動詞を省いた短い問いかけです。前置詞を使った', (None, 'with the wooden train'), 'が、その子の目印になっています。']),
    (3, None, ["'ネズミみたいにおとなしい子だったわ！三段目の階段に座って、ひとつひとつの音に耳を傾けていたの。' たとえの決まり文句", (None, 'Quiet as a mouse'), 'は、とてもおとなしいことを表します。強調の', (None, 'every single note'), 'も覚えておきたい表現です。']),
    (4, None, ["'部屋の響きに耳を傾けて…ちょっと待って！' 何かに気づいて話を止める", (None, 'wait a second'), 'は、実際の一秒ではなく、ほんの少しという意味の口語表現です。ハンナの頭の中で何かがつながりました。']),
    (5, None, ["'私が弾き終わるたびに、あの子は雨が降るとどうしてピアノの音が温かくなるのか聞いてきたのよ。' 接続詞の", (None, 'Whenever I finished playing'), 'は、毎回くり返されたことを表します。比較級の', (None, 'sounded warmer'), 'は、感覚を表す動詞と形容詞の組み合わせです。']),
    (6, None, ["'濡れた木の雨戸が、石畳の通りからの反響を和らげるからですよ…' 理由を答える", (None, 'Because'), 'で始め、動詞の', (None, 'soften the echo'), 'で音の仕組みを説明しています。形容詞に語尾をつけて動詞にする作り方にも注目しましょう。']),
    (7, None, ["'ケイレブさん！ずっとそこに立っていたんですか？！' 過去進行形の", (None, 'Were you standing right there'), 'は、その時点で続いていた動作を尋ねます。副詞の強調で、まさにその場所という驚きが伝わります。']),
    (8, None, ["'まあ、なんてこと…その目！三段目の階段の、小さなケイレブなの？！' 少し古風な驚きの言葉", (None, 'Good heavens'), 'は、年配の人が使うと上品に響きます。名前の前に形容詞をつけた', (None, 'Little Caleb'), 'は、子どものころの呼び方です。']),
    (9, None, ["'ミス・イヴリン？！兄の金曜日のピアノの先生？！' 所有格、曜日、楽器と、名詞の前に修飾を重ねた", (None, "My brother's Friday piano teacher"), 'は、日本語と同じく修飾語を前に積み上げる珍しい例です。']),
    (10, None, ["'待って、じゃあ月曜日の夜、うちの玄関先で…ふたつ目の青いスーツケースは…' 時と場所を並べた", (None, 'Monday night on our step'), 'や、序数を使った', (None, 'the second blue suitcase'), 'で、ハンナは記憶を順番にたどっています。']),
    (11, None, ["'そうです、ハンナ。あの青いスーツケースは私のものです。おふたりには、本当のことを全部お話ししなければなりません。' 名詞を伴わない所有代名詞の", (None, 'mine'), 'で持ち主だと名乗り、動詞の', (None, 'I owe you both the whole truth'), 'で、借りを返すように真実を打ち明ける決意を示しています。']),
]
