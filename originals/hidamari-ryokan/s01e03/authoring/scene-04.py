ID = 'hidamari-ryokan-s01e03-scene-04'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = '雨の中から  (In from the Rain)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'haruto': '陽翔', 'yuka': '由香'}

INTRO = 'Down in the lobby, soft-spoken traveller Haruto steps inside shaking rainwater off his umbrella. Mio greets him at the front desk while Yuka hurries out with a dry towel. Listen first.'

STORY = [
    ('mio', 'いらっしゃいませ！こんばんは。雨の中、どうぞ中へお入りください。', 'Welcome! Good evening. Please come inside out of the rain.'),
    ('haruto', 'こんばんは。きれいな床を濡らしてしまって、すみません。', 'Good evening. Sorry for getting your clean floor wet.'),
    ('mio', 'いいえ、お気になさらないでください！陽翔さまですね。', 'Not at all, please do not worry! You must be Haruto.'),
    ('haruto', 'はい、陽翔です。昨日、電話で七号室を予約しました。', 'Yes, I am Haruto. Yesterday I booked room seven by phone.'),
    ('yuka', 'コート用の乾いたタオルと、温かい野菜スープをどうぞ。', 'Here is a dry towel for your coat and a cup of hot vegetable soup.'),
    ('haruto', '温かいスープですか？あの冷たい雨の中を歩いた後だと、本当にありがたいです。', 'Hot soup? After that cold walk in the rain, that sounds wonderful.'),
    ('mio', 'あの、上へご案内する前に、正直にお詫びしたいことがあります。', 'Um, before showing you upstairs, I owe you an honest apology.'),
    ('haruto', 'えっ？私の予約に何か問題がありましたか？', 'Oh? Was there some problem with my reservation?'),
    ('mio', '手違いで、今夜の七号室に二人のお客さんを予約してしまったのです。', 'We accidentally booked two guests into room seven tonight.'),
    ('haruto', 'ああ……この雨の中でですか？駅の近くのホテルはどこも満室でしたよ。', 'Ah... in this rain? Every hotel near the station was completely full.'),
    ('mio', 'ご安心ください！三階の静かな屋根裏の書斎を、特別にご用意しました。', 'Please rest assured! We prepared our quiet third-floor attic study specially for you.'),
    ('haruto', '屋根裏の書斎ですか？まず見せていただけますか？', 'An attic study? May I take a look at it first?'),
]

OPENER = "Warm hospitality, soup on a rainy evening, and a sincere apology keep the mood calm. Let's review six key lines."

WALK = [
    (0, None, ["'Welcome! Good evening. Please come inside out of the rain.' Inviting a guest across the threshold uses ", (None, 'お入りください'), ", the welcoming polite way to say 'please come in'."]),
    (1, None, ["'Good evening. Sorry for getting your clean floor wet.' Notice how Haruto apologises thoughtfully with ", (None, 'すみません'), ' just for dripping rain on ', (None, 'きれいな床'), ", 'the clean floor'."]),
    (5, None, ["'Hot soup? After that cold walk in the rain, that sounds wonderful.' He describes the rain as ", (None, '冷たい'), ", 'cold to the touch', while ", (None, 'ありがたい'), " means 'grateful' or 'welcome'."]),
    (7, None, ["'Oh? Was there some problem with my reservation?' Keep ", (None, '何か問題'), ", meaning 'some problem', in your toolkit whenever checking on a hitch."]),
    (10, None, ["'Please rest assured! We prepared our quiet third-floor attic study specially for you.' Reassuring a worried guest starts with ", (None, 'ご安心ください'), ", literally 'please put your heart at peace'."]),
    (11, None, ["'An attic study? May I take a look at it first?' Asking permission very politely uses ", (None, '見せていただけますか'), ", meaning 'could you kindly let me see it?'."]),
]

TRANSITION = "Now let's hear Haruto's rainy arrival again all the way through."

OUTRO = 'A dry towel, hot vegetable soup, and honest words kept Haruto smiling. Next time, he climbs the stairs to give his verdict on the attic room.'

CLOSING = ('haruto', 'また会いましょう！')
