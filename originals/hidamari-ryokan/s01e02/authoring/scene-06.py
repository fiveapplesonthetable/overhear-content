ID = 'hidamari-ryokan-s01e02-scene-06'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = '金曜日の電話  (The Friday Caller)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'kenji': '健二'}

INTRO = "After breakfast, the lobby settles down as Mio updates the paper ledger and Kenji oils the front hinge. Suddenly the desk telephone rings. Let's listen in."

STORY = [
    ('mio', 'はい、ひだまり旅館でございます！受付の美央です。', 'Hello, Hidamari Inn! This is Mio at reception.'),
    ('kenji', '誰からだい？週末の新しい予約か？', 'Who is calling? Another reservation for the weekend?'),
    ('mio', 'あ、もしもし！濃い青いスーツケースの件でお電話ですか？', 'Oh, hello! Are you calling about the dark-blue suitcase?'),
    ('kenji', '名前を聞くんだ！紙に書き留めろ！', 'Ask for his name! Write it down on paper!'),
    ('mio', 'はい、鞄は荷物室で大切に預かっています。お名前を伺えますか？', 'Yes, we are keeping your bag safely in our luggage room. May I ask your name?'),
    ('kenji', '相手は何て言っている？どうして眉をひそめているんだ？', 'What is he saying? Why are you frowning?'),
    ('mio', 'もしもし？「白い紙の包みは開けないでください。金曜の正午に行きます」と……', "Hello? He says, 'Please do not open the white paper parcel. I will come Friday at noon'..."),
    ('kenji', '電話を代われ、俺がちゃんと聞いてやる！', 'Hand me the phone, I will ask him properly!'),
    ('mio', 'あっ、遅かったです！「ありがとうございます」と言って切れました！', "Oh, too late! He said 'Thank you' and the line clicked off!"),
    ('kenji', '丁寧な声だったか？若いのか、年配なのか？', 'Was it a polite voice? Young or older?'),
    ('mio', '静かで丁寧な声で、三十五歳くらいです。怒ってはいなくて、緊張していました。', 'A quiet, polite voice, around thirty-five. He was not angry, just nervous.'),
    ('kenji', '木の汽車のことで緊張だと？一時間ごとに話が妙になるな。', 'Nervous over a wooden toy train? This story grows stranger every hour.'),
]

OPENER = "Business phone etiquette meets Kenji's rapid-fire questions. Let's examine six expressions."

WALK = [
    (0, None, ["'Hello, Hidamari Inn! This is Mio at reception.' Answering a business phone in Japanese uses ", (None, 'でございます'), ", the polished service way to say 'this is'."]),
    (1, None, ["'Who is calling? Another reservation for the weekend?' Look at ", (None, '週末'), ", literally 'week end' for 'weekend', paired with ", (None, '予約'), " for a 'booking'."]),
    (4, None, ["'Yes, we are keeping your bag safely in our luggage room. May I ask your name?' Adding the polite prefix turns 'name' into ", (None, 'お名前'), ', followed by ', (None, '伺えますか'), ' for humbly asking.']),
    (6, None, ["'Hello? He says, Please do not open the white paper parcel. I will come Friday at noon...' Asking someone NOT to do something uses ", (None, '開けないでください'), ", meaning 'please do not open', and ", (None, '正午'), " means 'noon'."]),
    (8, None, ["'Oh, too late! He said Thank you and the line clicked off!' Notice ", (None, '遅かった'), ", the past form of 'late', and ", (None, '切れました'), ' for a phone call disconnecting.']),
    (10, None, ["'A quiet, polite voice, around thirty-five. He was not angry, just nervous.' Here ", (None, '声'), " means 'voice', while ", (None, '緊張していました'), ' describes feeling tense or nervous.']),
]

TRANSITION = "Now let's hear the mystery phone call again from beginning to end."

OUTRO = 'Now they have a firm time—Friday at noon—and a polite caller protecting that white paper parcel. See you next time in the afternoon café.'

CLOSING = ('mio', 'またね！')
