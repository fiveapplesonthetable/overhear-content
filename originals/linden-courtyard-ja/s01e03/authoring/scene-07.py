# Authoring module for linden-courtyard-ja-s01e03-scene-07.
ID = 'linden-courtyard-ja-s01e03-scene-07'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 3
SCENE = 7
TITLE = 'Returning the Notebook  (手帳を返しに)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb'}
INTRO = 'ハンナは置き忘れられた革の手帳を返しに、ケイレブの屋根裏部屋を訪ねます。ところが会話の最中に暖房管がカタンと鳴り、ラジエーターがぬるくなり始めます。耳を澄ませて英語の音声を聴きましょう。'
OPENER = 'さて、屋根裏での二人の会話を、順番に読み解いていきましょう。'
TRANSITION = '細かい表現を押さえたら、場面をもう一度最初から聴き直してみてください。'
OUTRO = '手帳は無事に持ち主のもとへ戻りましたが、暖房の様子がどうもおかしいようです。次の第八場面では、地下室から戻ったグレアムが悪い知らせを持ってきます。'
CLOSING = ('caleb', 'Have a good night!')
STORY = [
    ('hannah', 'Excuse me, Caleb? Sorry to disturb you.', '失礼します、ケイレブさん？お邪魔してすみません。'),
    ('caleb', 'Oh, my leather notebook! Thank you! I was just looking for it.', 'ああ、私の革の手帳！ありがとう！ちょうど探していたところなんです。'),
    ('hannah', 'You left it by the soup cup on the front counter.', '受付のカウンターの、スープのカップのそばに置いてありましたよ。'),
    ('caleb', 'All my street notes from this week are in here. You saved me.', '今週の通りのメモが全部ここに入っているんです。助かりました。'),
    ('hannah', 'We are glad you find our courtyard peaceful for your... work.', 'うちの中庭が、お客様の…お仕事にとって静かだと感じていただけて嬉しいです。'),
    ('caleb', 'Very peaceful! Though did you hear a funny metal knock just now?', 'とても静かですよ！ところで、今さっき妙な金属のコツンという音が聞こえませんでしたか？'),
    ('hannah', 'Yes! It sounded like it came from the heating pipe in the corner.', 'ええ！隅の暖房管から聞こえたようでした。'),
    ('caleb', 'Feel the radiator. The top is warm, while the bottom is turning cool.', 'ラジエーターを触ってみてください。上は温かいのに、下は冷たくなってきています。'),
    ('hannah', 'Oh! Sometimes old pipes have a little air bubble at night.', 'あら！古い配管は、夜になると小さな空気の泡がたまることがあるんです。'),
    ('caleb', 'I have a warm blanket, so I am quite comfortable tonight.', '暖かい毛布がありますから、今夜は十分快適ですよ。'),
    ('hannah', 'Thank you for being so patient! Graham will check the basement right away.', '辛抱強く待ってくださってありがとうございます！グレアムがすぐに地下室を見に行きます。'),
    ('caleb', 'Good night, Hannah. See you at breakfast.', 'おやすみなさい、ハンナさん。また朝食で。'),
]
WALK = [
    (0, None, ["'失礼します、ケイレブさん？お邪魔してすみません。' 相手の作業を中断させるときのお詫び", (None, 'Sorry to disturb you'), 'は、主語と動詞を省いた丁寧で短い言い方です。']),
    (1, None, ["'ああ、私の革の手帳！ありがとう！ちょうど探していたところなんです。' 進行中の動作を表す", (None, 'I was just looking for it'), 'では、過去進行形に「ちょうど」の副詞を加えて、まさにその最中だったことを伝えています。']),
    (2, None, ["'受付のカウンターの、スープのカップのそばに置いてありましたよ。' 置き忘れを表す", (None, 'You left it'), 'の動詞は「去る」だけでなく「物を残していく」という意味でもよく使われます。']),
    (3, None, ["'今週の通りのメモが全部ここに入っているんです。助かりました。' 感謝を大げさに表す", (None, 'You saved me'), 'は、直訳すると「私を救ってくれた」ですが、日常のちょっとした手助けにも気軽に使えます。']),
    (4, None, ["'うちの中庭が、お客様の…お仕事にとって静かだと感じていただけて嬉しいです。' 感じ方を表す", (None, 'you find our courtyard peaceful'), 'では、見つけるという動詞の後に目的語と形容詞を並べて「〜を〜だと思う」という意味になります。']),
    (5, None, ["'とても静かですよ！ところで、今さっき妙な金属のコツンという音が聞こえませんでしたか？' 話題を変える接続の言葉", (None, 'Though'), 'は、文頭に置くと「ところで」や「でも」のように軽い切り替えの合図になります。']),
    (6, None, ["'ええ！隅の暖房管から聞こえたようでした。' 聞いた印象を伝える", (None, 'It sounded like'), 'は、音から受けた推測を表す表現で、後ろに文を続けることができます。']),
    (7, None, ["'ラジエーターを触ってみてください。上は温かいのに、下は冷たくなってきています。' 二つの様子を対比する接続詞", (None, 'while'), 'と、変化の途中を表す', (None, 'is turning cool'), 'の組み合わせに注目しましょう。']),
    (8, None, ["'あら！古い配管は、夜になると小さな空気の泡がたまることがあるんです。' 頻度を表す副詞", (None, 'Sometimes'), 'を文頭に置くことで、珍しくない現象だと相手を安心させる言い方になっています。']),
    (9, None, ["'暖かい毛布がありますから、今夜は十分快適ですよ。' 程度を表す", (None, 'quite comfortable'), 'では、副詞が「十分に」という意味で形容詞を強めています。']),
    (10, None, ["'辛抱強く待ってくださってありがとうございます！グレアムがすぐに地下室を見に行きます。' 即座の対応を約束する", (None, 'right away'), 'は、時間をおかずに取りかかることを表す、会話でとてもよく使う副詞句です。']),
    (11, None, ["'おやすみなさい、ハンナさん。また朝食で。' 次に会う場面を添える別れのあいさつ", (None, 'See you at breakfast'), 'は、前置詞の後に場面や時を入れて自由に言い換えられます。']),
]
