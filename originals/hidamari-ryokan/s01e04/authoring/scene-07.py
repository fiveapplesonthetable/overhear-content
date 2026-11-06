ID = 'hidamari-ryokan-s01e04-scene-07'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = '日差しの下の名札  (Sunlight on the Tag)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'kazuko': '和子', 'kenji': '健二'}

INTRO = "At midday, Kenji airs out the hallway storage room after last night's rain and sets the unclaimed blue suitcase by the desk right as Kazuko walks over to chat with Mio. Listen first."

STORY = [
    ('kenji', '荷物室を掃除する五分だけ、この青いスーツケースをここに置かせてくれ。', 'Let me set this blue suitcase here for five minutes while I sweep the luggage room.'),
    ('mio', '気をつけて扱ってくださいね、健二さん。明日の正午は金曜日ですから！', 'Handle it carefully, Kenji. Tomorrow at noon is Friday!'),
    ('kazuko', 'あら、それが月曜日の電車で入れ替わった双子のスーツケースですか？', "Oh, is that the twin suitcase swapped on Monday's train?"),
    ('mio', 'はい、和子さん。まだ持ち主の方を待っているんです。', 'Yes, Kazuko. It is still waiting for its owner.'),
    ('kazuko', '明るい日差しの中で、もう一度あの紙の名札を見てもいいかしら？', 'May I look at that paper tag once more here in the bright sunlight?'),
    ('kenji', 'どうぞ見てください、和子さん。月曜日の午後はロビーが暗かったですからね。', 'Please go right ahead, Kazuko. Monday afternoon the lobby was dim.'),
    ('kazuko', 'ちょっと待って……「けやき通り十二番地」、それに角に彫られた子供の頃のイニシャル！', "Wait a moment... 'Number twelve, Keyaki Lane', and childhood initials carved in the corner!"),
    ('mio', '和子さん、すごく驚いていますね！「けやき通り十二番地」をご存じなんですか？', 'Kazuko, you look amazed! Do you know Number twelve, Keyaki Lane?'),
    ('kazuko', '知っているどころか！六年間、毎週金曜日にあの木の階段を上ってピアノを教えました！', 'Know it? Every Friday for six years I climbed those wooden stairs to teach piano!'),
    ('kenji', '二十五年前にですか？その同じ家で？', 'Twenty-five years ago? In that exact same house?'),
    ('kazuko', '大工のおじいさんと孫の兄弟が二人で暮らしていて、お兄ちゃんはピアノ、弟は汽車が大好きだったの！', 'A master carpenter lived there with his two grandsons: the older boy played piano, and the younger brother loved trains!'),
    ('mio', '大工のおじいさん……そして鞄の中には小さな木の汽車！', 'A carpenter grandfather... and inside the bag, a small wooden train!'),
]

OPENER = "Bright noon sunlight on Keyaki Lane's address unlocks a twenty-five-year family memory. Let's walk through six lines."

WALK = [
    (2, None, ["'Oh, is that the twin suitcase swapped on Monday's train?' Identical pairs are described playfully with ", (None, '双子'), ", the Japanese word for 'twins', right after ", (None, '月曜日'), ", 'Monday'."]),
    (4, None, ["'May I look at that paper tag once more here in the bright sunlight?' Asking to do something one more time uses ", (None, 'もう一度'), ", 'once again', under ", (None, '明るい日差し'), ", 'bright sunlight'."]),
    (5, None, ["'Please go right ahead, Kazuko. Monday afternoon the lobby was dim.' Pair bright with its opposite ", (None, '暗かった'), ", meaning 'was dark', during ", (None, '午後'), ", 'the afternoon'."]),
    (7, None, ["'Kazuko, you look amazed! Do you know Number twelve, Keyaki Lane?' Asking a guest respectfully 'do you know?' uses ", (None, 'ご存じ'), ' instead of the everyday plain word.']),
    (8, None, ["'Know it? Every Friday for six years I climbed those wooden stairs to teach piano!' Counting years attaches a smooth suffix in ", (None, '六年間'), ", meaning 'for a span of six years'."]),
    (10, None, ["'A master carpenter lived there with his two grandsons: the older boy played piano, and the younger brother loved trains!' Japanese distinguishes older and younger brothers clearly: ", (None, 'お兄ちゃん'), " means 'older brother' and ", (None, '弟'), " means 'younger brother', living with ", (None, '大工'), ", a 'carpenter'."]),
]

TRANSITION = "Now let's listen to Kazuko's discovery at the front desk again."

OUTRO = "Daylight on a faded tag revealed two grandsons on Keyaki Lane and their carpenter grandfather's wooden train! One final scene left in Episode 4—see you in the courtyard next time."

CLOSING = ('kazuko', 'また会いましょう！')
