# Authoring module for linden-courtyard-ja-s01e06-scene-03.
ID = 'linden-courtyard-ja-s01e06-scene-03'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = 'Thirty Days on Paper  (紙の上の三十日)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'フロントの奥で、アーサーは売却の通知を前に嘆いています。グレアムとハンナは、細かい条項まで読む前にあきらめてはいけないと彼を励まし、ハンナには一つ名案がひらめきます。それでは英語で場面を聴いてみてください。'
OPENER = '落ち込むアーサーと、それを支える仲間たちの言葉を順番に見ていきましょう。'
TRANSITION = 'では、フロントでのやり取りをもう一度、自然な速さで聴いてみましょう。'
OUTRO = '中庭には、古い建物にくわしい建築家がちょうど座っています。そこへテッサがテーブルから戻ってきました。続きは次の場面で。それではまた。'
CLOSING = ('graham', 'Bye for now!')
STORY = [
    ('arthur', 'Fifteen years of polishing brass keys and straightening ties... gone in thirty days!', '十五年間、真鍮の鍵を磨き、ネクタイを整えてきたのに…たった三十日で消えてしまうなんて！'),
    ('graham', 'Stop burying us before we read the whole document, Arthur.', '書類を全部読む前から、俺たちを葬るのはやめてくれ、アーサー。'),
    ('hannah', 'Yes! Earlier I noticed a second page clipped behind the cover letter.', 'そうよ！さっき、送り状の裏に二枚目がクリップで留めてあるのに気づいたの。'),
    ('arthur', 'Legal paragraphs give me a headache even with two pairs of glasses!', '法律の文章は、眼鏡を二つかけても頭が痛くなるんですよ！'),
    ('graham', 'This house survived eighty winters and one broken boiler valve yesterday.', 'この家は八十回の冬を越えてきたし、昨日はボイラーの弁が壊れても持ちこたえたんだ。'),
    ('hannah', 'Wait, who is sitting ten meters away in our courtyard right now?', '待って、今まさに十メートル先の中庭に座っているのは誰？'),
    ('arthur', 'Two brothers eating lemon cake?', 'レモンケーキを食べている兄弟二人ですか？'),
    ('hannah', 'An architect who works with historic courtyard buildings all over Portland!', 'ポートランド中の歴史ある中庭つきの建物を手がけている建築家よ！'),
    ('graham', 'Smart thinking, Hannah. Caleb reads city building rules every single week.', '冴えてるな、ハンナ。ケイレブは毎週欠かさず市の建築規則を読んでいるからな。'),
    ('arthur', 'Oh, I could never bother a paying guest with our landlord troubles!', 'ああ、お金を払っているお客さまに、うちの家主とのもめごとでご迷惑はかけられません！'),
    ('hannah', 'After we guarded his blue suitcase all week? He will want to help!', '一週間ずっと彼の青いスーツケースを預かってあげたのに？きっと力を貸したいと思うわよ！'),
    ('graham', 'Wait, Tessa is taking the cake out to their table right now.', '待って、ちょうど今、テッサが彼らのテーブルにケーキを運んでいるところだ。'),
]
WALK = [
    (0, None, ["'十五年間、真鍮の鍵を磨き、ネクタイを整えてきたのに…たった三十日で消えてしまうなんて！' 動詞に語尾を付けた形を前置詞の後ろに並べた", (None, 'polishing brass keys and straightening ties'), 'で、長年の仕事を名詞のように扱っています。積み重ねてきた日々が目に浮かぶ表現です。']),
    (1, None, ["'書類を全部読む前から、俺たちを葬るのはやめてくれ、アーサー。' 動詞の後ろに語尾付きの形を続けた", (None, 'Stop burying us'), 'は、「している行為をやめる」という意味です。不定詞を続けると「立ち止まって…する」と意味が変わるので注意しましょう。']),
    (2, None, ["'そうよ！さっき、送り状の裏に二枚目がクリップで留めてあるのに気づいたの。' 名詞を後ろから説明する過去分詞を使った", (None, 'a second page clipped behind the cover letter'), 'では、分詞以下が紙の状態を詳しく描写します。関係代名詞を使わずに短くまとめられる便利な形です。']),
    (3, None, ["'法律の文章は、眼鏡を二つかけても頭が痛くなるんですよ！' 体の不調を「与える」と表す", (None, 'give me a headache'), 'は、英語らしい発想です。主語に原因を置き、動詞の後ろに人と症状を並べます。']),
    (4, None, ["'この家は八十回の冬を越えてきたし、昨日はボイラーの弁が壊れても持ちこたえたんだ。' 困難を乗り越えて生き延びる動詞を使った", (None, 'This house survived eighty winters'), 'では、前置詞なしで乗り越えた対象を直接目的語にします。建物を人のように語る温かい言い方です。']),
    (5, None, ["'待って、今まさに十メートル先の中庭に座っているのは誰？' 距離を前に置いて位置を示す", (None, 'ten meters away'), 'では、副詞が「離れて」を表し、その前に距離を置きます。すぐ近くにいるのに気づかないのか、とヒントを出す言い方です。']),
    (6, None, ["'レモンケーキを食べている兄弟二人ですか？' 名詞を後ろから説明する", (None, 'Two brothers eating lemon cake'), 'は、動詞に語尾を付けた形が名詞を修飾しています。アーサーはまだ、ハンナの意図に気づいていません。']),
    (7, None, ["'ポートランド中の歴史ある中庭つきの建物を手がけている建築家よ！' 地域全体に広がることを表す", (None, 'all over Portland'), 'は、場所の前に置いて「…中で」という意味になります。日本語の「中」と同じように、範囲の広さを強調します。']),
    (8, None, ["'冴えてるな、ハンナ。ケイレブは毎週欠かさず市の建築規則を読んでいるからな。' 強調語をはさんだ", (None, 'every single week'), 'では、「一つ一つの」を意味する形容詞が加わって、一度も抜かさないという気持ちが強まります。']),
    (9, None, ["'ああ、お金を払っているお客さまに、うちの家主とのもめごとでご迷惑はかけられません！' 人の手をわずらわせる動詞を使った", (None, 'I could never bother a paying guest'), 'では、過去形の助動詞が控えめな気持ちを表します。客を表す名詞の前の語は「料金を払っている」という意味です。']),
    (10, None, ["'一週間ずっと彼の青いスーツケースを預かってあげたのに？きっと力を貸したいと思うわよ！' 未来の気持ちを確信をもって言う", (None, 'He will want to help'), 'では、助動詞が予測を、次の動詞が願望を表します。二つを重ねて「きっと…したくなる」という意味になります。']),
    (11, None, ["'待って、ちょうど今、テッサが彼らのテーブルにケーキを運んでいるところだ。' 相手に注意を促す現在進行形で", (None, 'Tessa is taking the cake out'), 'と状況を描写しています。']),
]
