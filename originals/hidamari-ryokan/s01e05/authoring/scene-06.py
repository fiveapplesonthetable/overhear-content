ID = 'hidamari-ryokan-s01e05-scene-06'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 5
SCENE = 6
TITLE = '正午の十分前  (Ten Minutes to Twelve)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'takashi': '隆', 'mio': '美央', 'yuka': '由香'}

INTRO = 'Inside at the front desk at eleven fifty, Takashi straightens a fresh blue tie while Mio and Yuka watch the clock—right as the postman leaves a thick registered envelope on the counter. Listen first.'

STORY = [
    ('takashi', '美央さん、今日のネクタイはどうですか？オレンジジュースは一滴もありませんよ！', "Mio, how does today's tie look? Not a single drop of orange juice in sight!"),
    ('mio', 'ばっちり清潔です、隆さん！眼鏡もおでこじゃなくてちゃんと鼻の上にありますよ。', 'Spotless and sharp, Takashi! Even your glasses are on your nose instead of your forehead.'),
    ('takashi', '進歩ですね！今日は中庭で家族の再会がありますから、皆さん静かな品格を保ちましょう！', 'Progress! Today our courtyard hosts a family reunion, so let us all keep quiet dignity!'),
    ('yuka', '三十秒ごとにレースのカーテンから覗いている人が言うセリフかな？', 'Says the man peeking through the lace curtain every thirty seconds!'),
    ('takashi', '天気を確かめているだけです、由香さん！ベルの横にあるこの分厚い封筒は何ですか？', 'I am merely checking the weather, Yuka! What is this thick envelope beside the bell?'),
    ('mio', 'たった今、郵便屋さんに受領のサインをしました。不動産管理室の赤い印鑑が押してあります。', 'I just signed for it from the postman. It bears a red stamp from the property office.'),
    ('takashi', '建物の大家さんの弁護士からですか？変ですね、家賃は来年の夏まで払ってありますよ。', "From the building landlord's lawyer? Strange, our rent is paid through next summer."),
    ('yuka', '隆さん、開けるのは十二時過ぎてからにして！時計を見て、正午まであと五分だよ！', 'Takashi, open it after twelve! Look at the clock: five minutes to noon!'),
    ('takashi', 'その通りですね。書類はあとにして、今は帳面の横に置いておきましょう。', "Quite right. Paperwork can wait—let's leave it beside the ledger for now."),
    ('mio', '青いスーツケースは、木の下の陽翔さんのテーブルのすぐ横に置きました。', "I placed the blue suitcase right beside Haruto's table under the tree."),
    ('yuka', '急須も熱々だよ！みんな、窓から少し離れて！', 'The teapot is piping hot too! Everyone, step back from the window!'),
    ('takashi', '聞いてください……通りの時計台の鐘が、正午を打ち始めました！', 'Listen... the clock tower bell down the street has started chiming noon!'),
]

OPENER = "Body parts, mail delivery, and the noon chimes build suspense inside the lobby. Let's walk through six lines."

WALK = [
    (1, None, ["'Spotless and sharp, Takashi! Even your glasses are on your nose instead of your forehead.' Face words appear side by side: ", (None, 'おでこ'), " means 'forehead' and ", (None, '鼻'), " means 'nose'."]),
    (4, None, ["'I am merely checking the weather, Yuka! What is this thick envelope beside the bell?' Everyday small talk relies on ", (None, '天気'), " for 'weather', while ", (None, '分厚い封筒'), " means 'a thick envelope'."]),
    (5, None, ["'I just signed for it from the postman. It bears a red stamp from the property office.' Official mail in Osaka carries ", (None, '赤い印鑑'), ', a red ink seal stamp, delivered by ', (None, '郵便屋さん'), ", 'the mail carrier'."]),
    (6, None, ["'From the building landlord's lawyer? Strange, our rent is paid through next summer.' Housing vocabulary pairs ", (None, '大家さん'), ", 'landlord', with ", (None, '家賃'), ", 'rent'."]),
    (7, None, ["'Takashi, open it after twelve! Look at the clock: five minutes to noon!' Notice ", (None, '正午まであと五分'), ", 'five minutes left until noon'."]),
    (11, None, ["'Listen... the clock tower bell down the street has started chiming noon!' Putting 'begin' onto 'strike' forms ", (None, '打ち始めました'), ' as ', (None, '時計台の鐘'), ", 'the clock tower bell', rings out."]),
]

TRANSITION = "Now let's replay the eleven-fifty lobby scene without pauses."

OUTRO = "That thick red-stamped envelope waits unopened beside the ledger as twelve chimes echo across Osaka! Let's step outside to the courtyard gate next time."

CLOSING = ('yuka', 'じゃあね！')
