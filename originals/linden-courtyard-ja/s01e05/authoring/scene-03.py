# Authoring module for linden-courtyard-ja-s01e05-scene-03.
ID = 'linden-courtyard-ja-s01e05-scene-03'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 5
SCENE = 3
TITLE = 'Friday Lemon Cake  (金曜日のレモンケーキ)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'evelyn': 'Evelyn', 'caleb': 'Caleb', 'tessa': 'Tessa'}
INTRO = 'カフェの一角で、イヴリンは兄弟が金曜日のピアノのレッスンの後にいつも食べていたものを思い出します。その話を聞いたテッサの頭に、ぱっと素敵な考えがひらめきました。英語の会話をまず一通り聴いてみましょう。'
OPENER = '懐かしい思い出がどんな英語で語られるのか、順番に見ていきましょう。'
TRANSITION = 'では、カフェでの会話全体をもう一度ふつうの速さで聴いてみてください。'
OUTRO = '黄色いレモンが六つ、まるで今日を待っていたかのようにかごに並んでいました。次は中庭で、正午に向けた小さなテーブルの準備が始まります。それでは、ひとまずさようなら。'
CLOSING = ('tessa', 'Bye for now!')
STORY = [
    ('tessa', 'So, Caleb, you are really staying in the courtyard to greet Owen at noon?', 'それでケイレブ、本当に中庭に残って正午にオーウェンさんを迎えるのね？'),
    ('caleb', 'Yes, Tessa. Even if he turns around and walks straight back out the gate.', 'ええ、テッサさん。たとえ兄が向きを変えて、そのまま門から出て行ったとしても。'),
    ('evelyn', 'Owen will not walk out. He always acted tough for five seconds, then softened.', 'オーウェンは出て行ったりしないわ。あの子はいつも五秒だけ強がって、すぐに柔らかくなったもの。'),
    ('caleb', 'You still remember that after all these years?', '何年も経つのに、まだそんなことを覚えていらっしゃるんですか？'),
    ('evelyn', 'Of course! Every Friday when he missed a piano note, he frowned at the wall.', 'もちろんよ！毎週金曜日、ピアノの音を外すたびに、あの子は壁をにらんでいたわ。'),
    ('tessa', 'How did you get him smiling again, Miss Evelyn?', 'どうやってまた笑顔にさせたんですか、イヴリンさん？'),
    ('evelyn', 'His grandfather sliced warm lemon cake with powdered sugar on top!', 'おじいさまが、粉砂糖をのせた温かいレモンケーキを切り分けてくださったのよ！'),
    ('caleb', 'Oh! Yellow lemon glaze! We fought over the corner piece every single Friday!', 'ああ！黄色いレモンのアイシング！毎週金曜日、角の一切れを取り合っていました！'),
    ('tessa', 'Hold everything! What time is it right now? Nine thirty-five!', 'ちょっと待って！今何時？九時三十五分！'),
    ('caleb', 'Tessa, please do not do extra work because of us.', 'テッサさん、僕たちのために余計な仕事をしないでください。'),
    ('tessa', 'Six yellow lemons are sitting in my basket right now. This kitchen was waiting for today!', 'ちょうど今、黄色いレモンが六つかごに入っているの。このキッチンは今日を待っていたのよ！'),
    ('evelyn', 'Bake plenty of corner pieces, my dear!', '角の一切れをたくさん焼いてあげてね！'),
]
WALK = [
    (0, None, ["'それでケイレブ、本当に中庭に残って正午にオーウェンさんを迎えるのね？' 平叙文に", (None, 'really'), 'を入れて上がり調子で言うと、念を押す確認の質問になります。迎えることはトゥ不定詞で', (None, 'to greet Owen at noon'), 'と目的を添えます。']),
    (1, None, ["'ええ、テッサさん。たとえ兄が向きを変えて、そのまま門から出て行ったとしても。' 最悪の場合を覚悟する譲歩が", (None, 'Even if'), 'というのがこの言い方です。続く', (None, 'walks straight back out the gate'), 'では、ストレート、バック、アウトと副詞を重ねて動きを細かく描いています。']),
    (2, None, ["'オーウェンは出て行ったりしないわ。あの子はいつも五秒だけ強がって、すぐに柔らかくなったもの。' 強いふりをすることを", (None, 'acted tough'), 'と言います。アクトは「演じる」で、本心とは違う態度を示します。', (None, 'softened'), 'は形容詞ソフトに語尾エンをつけて動詞にしたものです。']),
    (3, None, ["'何年も経つのに、まだそんなことを覚えていらっしゃるんですか？' 長い年月を経てもなお、という驚きを", (None, 'after all these years'), 'で表します。スティルを動詞の前に置くと「今でもまだ」という意味が加わります。']),
    (4, None, ["'もちろんよ！毎週金曜日、ピアノの音を外すたびに、あの子は壁をにらんでいたわ。' 音を外すことを動詞", (None, 'missed a piano note'), 'で表します。ミスは「逃す、外す」が基本の意味です。眉をひそめる動作は', (None, 'frowned at the wall'), 'と、前置詞アットで向けた先を示します。']),
    (5, None, ["'どうやってまた笑顔にさせたんですか、イヴリンさん？' 使役のゲットを使い、人と動詞のイング形を続けると", (None, 'get him smiling again'), 'となり、ある状態にさせて動き出させる感じが出ます。']),
    (6, None, ["'おじいさまが、粉砂糖をのせた温かいレモンケーキを切り分けてくださったのよ！' 薄く切り分ける動作は", (None, 'sliced'), 'で、名詞スライスと同じ語です。粉砂糖は', (None, 'powdered sugar'), 'で、パウダーに語尾をつけた形容詞が使われています。']),
    (7, None, ["'ああ！黄色いレモンのアイシング！毎週金曜日、角の一切れを取り合っていました！' ケーキの表面にかける糖衣を", (None, 'glaze'), 'と言います。取り合いは', (None, 'fought over the corner piece'), 'で、争う対象を前置詞オーバーで表します。']),
    (8, None, ["'ちょっと待って！今何時？九時三十五分！' 何かをひらめいて周りを止めるときの決まり文句が", (None, 'Hold everything'), 'という決まり文句です。時刻は', (None, 'Nine thirty-five'), 'のように、時と分の数字を並べるだけで言えます。']),
    (9, None, ["'テッサさん、僕たちのために余計な仕事をしないでください。' 丁寧な否定の依頼は", (None, 'please do not do extra work'), 'です。理由を示す', (None, 'because of us'), 'は、ビコーズにオブを加えて名詞を続ける形です。']),
    (10, None, ["'ちょうど今、黄色いレモンが六つかごに入っているの。このキッチンは今日を待っていたのよ！' 物が置かれている状態を動詞シットの進行形で", (None, 'are sitting in my basket'), 'と表します。キッチンを人のように扱った', (None, 'This kitchen was waiting for today'), 'は、遊び心のある擬人化です。']),
    (11, None, ["'角の一切れをたくさん焼いてあげてね！' 量が十分にあることを", (None, 'plenty of'), 'で表します。最後の', (None, 'my dear'), 'は、年配の人が親しみを込めて相手を呼ぶ優しい言い方です。']),
]
