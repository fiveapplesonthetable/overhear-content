ID = 'hidamari-ryokan-s01e05-scene-02'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 5
SCENE = 2
TITLE = '三年間の沈黙  (Three Years of Silence)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'haruto': '陽翔', 'mio': '美央', 'kenji': '健二'}

INTRO = 'Inside at the front desk on Friday morning, three hours before noon, Kenji brings the dark-blue suitcase out of the luggage closet for Haruto and Mio. Listen first.'

STORY = [
    ('kenji', '金曜日の謎の電話の主が、ずっと上の屋根裏で寝ていたとはな。', 'To think our mystery Friday caller was sleeping upstairs in the attic all along.'),
    ('haruto', 'ご迷惑をおかけしました、健二さん。一週間も鞄を守ってくれてありがとうございます。', 'Sorry for the trouble, Kenji. Thank you for guarding this bag all week.'),
    ('mio', 'どうして大輝さんの家の玄関で、木の汽車を直接渡せなかったんですか？', 'Why could you not hand the wooden train directly to Daiki at his front door?'),
    ('haruto', '三年前、祖父が亡くなったあと、古い家を売るかどうかで大輝と激しく言い争ったんです。', 'Three years ago after our grandfather passed away, Daiki and I argued fiercely over selling the old house.'),
    ('kenji', '家族の家と昔の思い出か……そういう喧嘩は傷が深いからな。', 'A family house and old memories... arguments like that cut deep.'),
    ('haruto', 'あの日から一度も話していません。先週、短い絵葉書を一枚だけ送りました。', 'We have not spoken since that day. Last week I sent him one short postcard.'),
    ('mio', '金曜日の正午に、ここで会おうと書いたんですか？', 'Did you write asking him to meet you here Friday at noon?'),
    ('haruto', 'いいえ、「金曜日の正午、祖父の物がひだまり旅館で待っている」とだけ書きました。', "No, I only wrote, 'Friday at noon, something of Grandfather's is waiting at Hidamari Inn.'"),
    ('kenji', 'なるほど！自分の名前を書いたら、頑固な兄貴が来ないと思ったんだな！', 'Aha! You figured if you signed your own name, your stubborn big brother would stay home!'),
    ('haruto', 'お兄さんというものをよく分かっていらっしゃいますね、健二さん。', 'You understand older brothers very well, Kenji.'),
    ('mio', 'えっ、じゃあ受付の人に鞄を渡させて、通りの向こうから見守るつもりだったんですか！？', 'Wait—you were planning to let the clerk hand him the bag and watch from across the street?!'),
    ('haruto', '月曜日の時点ではそんな臆病な計画でした……皆さんに出会うまでは。', 'On Monday that was my cowardly plan... until I met all of you.'),
]

OPENER = "A short postcard, family history, and finding courage three hours before noon anchor this scene. Let's walk through six lines."

WALK = [
    (1, None, ["'Sorry for the trouble, Kenji. Thank you for guarding this bag all week.' Apologising politely for causing inconvenience uses the set phrase ", (None, 'ご迷惑をおかけしました'), '.']),
    (3, None, ["'Three years ago after our grandfather passed away, Daiki and I argued fiercely over selling the old house.' Talking modestly about your own grandfather uses ", (None, '祖父'), ', paired with ', (None, '三年前'), " for 'three years ago'."]),
    (4, None, ["'A family house and old memories... arguments like that cut deep.' Cherished memories have a warm everyday noun: ", (None, '思い出'), ", literally 'thoughts coming out', alongside ", (None, '喧嘩'), " for a 'quarrel'."]),
    (5, None, ["'We have not spoken since that day. Last week I sent him one short postcard.' Pointing to a past date uses ", (None, 'あの日から'), ", 'since that day', and ", (None, '絵葉書'), " for 'picture postcard'."]),
    (8, None, ["'Aha! You figured if you signed your own name, your stubborn big brother would stay home!' Casual men's speech often uses ", (None, '兄貴'), " for 'big brother', described here as ", (None, '頑固な'), ", 'stubborn'."]),
    (10, None, ["'Wait—you were planning to let the clerk hand him the bag and watch from across the street?!' Talking about an earlier plan uses ", (None, 'つもりだった'), ", meaning 'intended to'."]),
]

TRANSITION = "Now let's replay the front-desk conversation from start to finish."

OUTRO = 'Instead of hiding across the lane, Haruto has decided to face his brother in the courtyard at noon. See you next time in the café corner.'

CLOSING = ('kenji', 'じゃあね！')
