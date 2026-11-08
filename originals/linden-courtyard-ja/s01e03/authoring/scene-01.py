# Authoring module for linden-courtyard-ja-s01e03-scene-01.
ID = 'linden-courtyard-ja-s01e03-scene-01'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = 'Thirty-Five Minutes  (三十五分)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'フロントでは、七号室に同じ夜の予約が二つ入っていたと分かり、アーサーがすっかり慌てています。そこへグレアムが、三階の屋根裏部屋の小さな銀の鍵を取り出しました。細かい単語は気にせず、まずは場面全体を英語で聴いてみましょう。'
OPENER = 'それでは、慌ただしいフロントでの会話を一行ずつ丁寧にたどっていきましょう。'
TRANSITION = '今度は会話をひと続きのまま、自然な速さで聴いてみましょう。'
OUTRO = '三人は客が着く前に屋根裏部屋を整えようと、三階への階段を駆け上がっていきました。ひと息ついたら、次の場面で屋根裏の様子をのぞいてみましょう。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('arthur', 'Thirty-five minutes! He will write a terrible one star review!', 'あと三十五分！あの人、ひどい星一つのレビューを書くに決まってる！'),
    ('hannah', 'Take a deep breath, Arthur. Nobody has written anything yet.', '深呼吸して、アーサー。まだ誰も何も書いていないわ。'),
    ('graham', 'Here is the small silver key for the third floor attic door.', 'これが三階の屋根裏部屋の扉の、小さな銀の鍵だよ。'),
    ('arthur', 'Does the attic even have a proper bed?', 'そもそも屋根裏にちゃんとしたベッドなんてあるんですか？'),
    ('graham', 'Yes, a good wooden bed, a clean desk, and the best view in the house.', 'あるとも。立派な木のベッドに、きれいな机、それに家じゅうで一番の眺めだ。'),
    ('hannah', 'Then why do we never rent it to guests?', 'じゃあ、どうして一度もお客さんに貸したことがないの？'),
    ('graham', 'Because the stairs are narrow and Arthur keeps old lamp boxes there.', '階段が狭いうえに、アーサーが古いランプの箱をあそこにしまっているからさ。'),
    ('arthur', 'Only three small boxes! Maybe four!', '小さな箱がたった三つですよ！四つかもしれませんけど！'),
    ('hannah', 'We can move four boxes in five minutes. Let us go look right now!', '箱四つなら五分で動かせるわ。今すぐ見に行きましょう！'),
    ('graham', 'Up the stairs, turn left at the landing, last door at the top.', '階段を上がって、踊り場で左に曲がって、一番上の突き当たりの扉だ。'),
    ('arthur', 'I will bring clean white sheets from the linen closet!', 'リネン用の戸棚から、洗いたての白いシーツを持っていきます！'),
    ('hannah', 'Come on, race you to the third floor!', 'さあ、三階まで競走よ！'),
]
WALK = [
    (0, None, ["'あと三十五分！あの人、ひどい星一つのレビューを書くに決まってる！' 名詞の前に置いて形容詞のように働く", (None, 'one star review'), 'では、星が一つなので複数形にせず、ハイフンでつなぐ書き方もよく見られます。']),
    (1, None, ["'深呼吸して、アーサー。まだ誰も何も書いていないわ。' 落ち着かせたい相手にかける決まり文句が", (None, 'Take a deep breath'), 'です。さらに否定文の最後に置く', (None, 'yet'), 'は、今の時点ではまだ起きていないという含みを添えます。']),
    (2, None, ["'これが三階の屋根裏部屋の扉の、小さな銀の鍵だよ。' 物を手渡しながら差し出すときは", (None, 'Here is'), 'で始めます。形容詞が小ささ、色の順に並んでいる点にも注目しましょう。']),
    (3, None, ["'そもそも屋根裏にちゃんとしたベッドなんてあるんですか？' 疑問文に入り込んだ", (None, 'even'), 'は驚きや疑いを表し、', (None, 'a proper bed'), 'は名ばかりではない本格的なものという意味になります。']),
    (4, None, ["'あるとも。立派な木のベッドに、きれいな机、それに家じゅうで一番の眺めだ。' 最上級の", (None, 'the best view'), 'の後は、範囲を表す場所の前に前置詞', (None, 'in the house'), 'を置くのが基本の形です。']),
    (5, None, ["'じゃあ、どうして一度もお客さんに貸したことがないの？' 頻度を表す", (None, 'never'), 'は一般動詞の直前に置き、', (None, 'rent it to guests'), 'のように貸す相手は前置詞で示します。']),
    (6, None, ["'階段が狭いうえに、アーサーが古いランプの箱をあそこにしまっているからさ。' 階段を指す", (None, 'the stairs are narrow'), 'では、段の集まりとして複数扱いになり、動詞も複数形を使います。また', (None, 'keeps'), 'は物を置いたままにしておく意味の動詞です。']),
    (7, None, ["'小さな箱がたった三つですよ！四つかもしれませんけど！' 数を少なく見せたいときは", (None, 'Only three small boxes'), 'と強調し、言い直しには', (None, 'Maybe four'), 'と短く付け足すのが口語らしい言い方です。']),
    (8, None, ["'箱四つなら五分で動かせるわ。今すぐ見に行きましょう！' 所要時間の前には前置詞を置いて", (None, 'in five minutes'), 'と表します。さらに', (None, 'right now'), 'は今という語を強めて急ぎの気持ちを伝えます。']),
    (9, None, ["'階段を上がって、踊り場で左に曲がって、一番上の突き当たりの扉だ。' 道案内でよく使う", (None, 'turn left at the landing'), 'では、曲がる地点を点として示す前置詞が使われています。日本語より短く命令形で並べるのが英語の道案内の特徴です。']),
    (10, None, ["'リネン用の戸棚から、洗いたての白いシーツを持っていきます！' 自分から申し出るときは", (None, 'I will bring'), 'と未来の意志を示し、', (None, 'the linen closet'), 'はシーツやタオルをしまう収納のことです。']),
    (11, None, ["'さあ、三階まで競走よ！' 相手を誘って駆け出すときのくだけた言い方が", (None, 'race you to the third floor'), 'です。本来は主語のある長い文ですが、会話では頭が省かれてこの短い形になります。']),
]
