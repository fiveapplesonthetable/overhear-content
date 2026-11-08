# Authoring module for linden-courtyard-ja-s01e02-scene-06.
ID = 'linden-courtyard-ja-s01e02-scene-06'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = 'The Friday Caller  (金曜日に来る電話の主)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '朝食のあと、フロントの電話が鳴りました。受話器を取ったハンナの声色が変わります。電話の相手は、あの濃紺のスーツケースの持ち主だったのです。まずは緊張感漂う電話の場面を英語で聴いてみましょう。'
OPENER = 'それでは電話応対と伝言のやり取りを、一行ずつ見ていきましょう。'
TRANSITION = 'ではもう一度、場面全体を自然なスピードで聴いてみましょう。'
OUTRO = '電話の男性は名前を名乗らないまま、白い紙の包みを開けないでほしいとだけ言い残して電話を切りました。金曜日の正午がますます気になります。それではまた後ほど。'
CLOSING = ('hannah', 'Bye for now!')
STORY = [
    ('hannah', 'Linden Courtyard Inn, good morning! Hannah speaking.', 'リンデン中庭インでございます、おはようございます！ハンナがお受けしております。'),
    ('graham', 'Who is it? Another booking for the weekend?', '誰からだい？週末の予約がもう一件入ったのかい？'),
    ('hannah', 'Wait, hello, sir! You are calling about the dark blue suitcase?', '待って、もしもし、お客さま！濃紺のスーツケースの件でお電話ですね？'),
    ('graham', 'Ask him his name! Write it down!', '彼に名前を聞くんだ！書き留めておけよ！'),
    ('hannah', 'Yes, sir, we locked your bag safely in our closet. What is your name, please?', 'はい、お客さま、お荷物は当館の収納室に安全に鍵をかけて保管しております。失礼ですが、お名前を伺えますか？'),
    ('graham', 'What is he saying? Why are you frowning?', '彼は何と言っているんだ？どうして眉をひそめているんだい？'),
    ('hannah', "Sir? He says, 'Please do not open the white paper package. I will come Friday at noon.'", 'お客さま？「どうか白い紙の包みは開けないでください。金曜日の正午に伺います」とおっしゃっています。'),
    ('graham', 'Give me the phone, let me ask him properly!', '電話を貸してごらん、私がきちんと聞いてみよう！'),
    ('hannah', "Too late! He said 'Thank you' and hung up!", '遅かったわ！「ありがとうございます」と言って電話を切ってしまいました！'),
    ('graham', 'Polite voice? Young or old?', '丁寧な声だったかい？若い人、それとも年配の人？'),
    ('hannah', 'Quiet, polite, maybe thirty-five. He sounded nervous, not angry.', '物静かで丁寧で、たぶん三十五歳くらいです。怒っているのではなく、緊張しているように聞こえました。'),
    ('graham', 'Nervous about a wooden toy train? This story gets stranger every hour.', '木製のおもちゃの列車のことで緊張だって？この話は一時間ごとに奇妙になっていくね。'),
]
WALK = [
    (0, None, ["'リンデン中庭インでございます、おはようございます！ハンナがお受けしております。' 職場の電話に出たときに自分の名前を名乗る決まり文句は", (None, 'Hannah speaking'), 'と分詞だけで簡潔に言えます。']),
    (1, None, ["'誰からだい？週末の予約がもう一件入ったのかい？' 電話や玄関の相手が誰なのかを尋ねるときは英語では中立の代名詞を使って", (None, 'Who is it'), 'と聞くのが決まりです。']),
    (2, None, ["'待って、もしもし、お客さま！濃紺のスーツケースの件でお電話ですね？' 用件を確かめるときは現在進行形に話題の前置詞を添えて", (None, 'You are calling about'), 'と聞き返します。']),
    (3, None, ["'彼に名前を聞くんだ！書き留めておけよ！' 相手に名前を尋ねる", (None, 'Ask him his name'), 'と、忘れないよう紙に書く', (None, 'Write it down'), 'の素早い指示です。']),
    (4, None, ["'はい、お客さま、お荷物は当館の収納室に安全に鍵をかけて保管しております。失礼ですが、お名前を伺えますか？' 電話口で丁寧にお名前を尋ねる基本表現が", (None, 'What is your name, please'), 'という優しい聞き方です。']),
    (5, None, ["'彼は何と言っているんだ？どうして眉をひそめているんだい？' 今まさに電話の向こうで話している内容を", (None, 'What is he saying'), 'と尋ね、表情を', (None, 'Why are you frowning'), 'と気にかけています。']),
    (6, None, ["'お客さま？「どうか白い紙の包みは開けないでください。金曜日の正午に伺います」とおっしゃっています。' 丁寧な禁止のお願い", (None, 'Please do not open'), 'に続けて、来訪時刻を', (None, 'Friday at noon'), 'と伝えています。']),
    (7, None, ["'電話を貸してごらん、私がきちんと聞いてみよう！' 受話器を替わるよう求める", (None, 'Give me the phone'), 'と、ちゃんとした手順で尋ねる', (None, 'let me ask him properly'), 'の組み合わせです。']),
    (8, None, ["'遅かったわ！「ありがとうございます」と言って電話を切ってしまいました！' 間に合わなかったときの一言", (None, 'Too late'), 'と、通話を終えて切る過去の表現', (None, 'hung up'), 'を覚えましょう。']),
    (9, None, ["'丁寧な声だったかい？若い人、それとも年配の人？' 会話の中で手短に特徴を尋ねるときは、余分な語を省いて", (None, 'Polite voice'), 'さらに続けて', (None, 'Young or old'), 'とテンポよく聞けます。']),
    (10, None, ["'物静かで丁寧で、たぶん三十五歳くらいです。怒っているのではなく、緊張しているように聞こえました。' 声の響きから受けた印象を述べるには動詞の後ろに形容詞を置いて", (None, 'He sounded nervous'), 'と自然に表します。']),
    (11, None, ["'木製のおもちゃの列車のことで緊張だって？この話は一時間ごとに奇妙になっていくね。' 状況がどんどん変化していく様子を比較級で", (None, 'gets stranger every hour'), 'と締めくくっています。']),
]
