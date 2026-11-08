ID = 'hidamari-ryokan-s01e02-scene-05'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = 'ネクタイにジュース  (Juice on the Tie)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'takashi': '隆', 'kazuko': '和子', 'mio': '美央'}

INTRO = 'Breakfast is underway in the sunlit café corner. Kazuko sits by the window while Takashi insists on helping Mio pour drinks like a luxury hotel manager. Listen first.'

STORY = [
    ('mio', '改めておはようございます、和子さん！コーヒーと紅茶、どちらになさいますか？', 'Good morning again, Kazuko! Would you prefer coffee or black tea?'),
    ('kazuko', '砂糖なしの紅茶をお願いします。それと温かいパンを一切れ。', 'Black tea without sugar, please, and one slice of warm bread.'),
    ('takashi', '新鮮なオレンジジュースは、私がお注ぎしますよ！', 'Allow me to pour the fresh orange juice for you!'),
    ('kazuko', 'まあ、ご親切にありがとう。コップ半分だけお願いします。', 'Oh, how kind of you. Just half a glass, please.'),
    ('takashi', '当館では五つ星のサービスが当たり前……おっと！', 'At our inn, five-star service comes naturally... whoops!'),
    ('mio', '気をつけてください、隆さん、ピッチャーの注ぎ口が広いです！', 'Be careful, Takashi, the pitcher spout is wide!'),
    ('takashi', '大変だ！テーブルには一滴もこぼれていませんが……全部私のネクタイに！', 'Oh dear! Not a single drop spilled on the table, yet all of it is on my tie!'),
    ('kazuko', '心配しないで！冷たい炭酸水なら、オレンジジュースがすぐ落ちますよ。', 'Do not worry! Cold sparkling water takes orange juice right out.'),
    ('mio', '隆さん、きれいな布と冷たい水をお持ちしました。', 'Takashi, I brought a clean cloth and cold water.'),
    ('takashi', '失礼いたします、和子さん。堂々と事務室へ引き上げます！', 'Excuse me, Kazuko. I shall retreat to my office with dignity!'),
    ('kazuko', 'スクランブルエッグがとてもおいしいわ、美央さん。由香さんによろしく伝えてね。', 'The scrambled eggs are delicious, Mio. Tell Yuka my compliments!'),
    ('mio', 'はい、伝えます！どうぞごゆっくりお過ごしください。', 'I certainly will! Please enjoy a relaxing morning.'),
]

OPENER = "Ordering drinks at a café table and polite restaurant service fill this scene. Let's look at six highlights."

WALK = [
    (0, None, ["'Good morning again, Kazuko! Would you prefer coffee or black tea?' Green tea is usually 'tea' by default, while ", (None, '紅茶'), " literally means 'crimson tea' — regular black tea — and ", (None, 'どちら'), " asks 'which of the two?'."]),
    (1, None, ["'Black tea without sugar, please, and one slice of warm bread.' You can customise any café order by placing ", (None, 'なし'), ", meaning 'without', right after ", (None, '砂糖'), " for 'sugar'."]),
    (3, None, ["'Oh, how kind of you. Just half a glass, please.' Asking for half a portion is simple with ", (None, 'コップ半分'), ", joining 'glass' with ", (None, '半分'), ", literally 'half part'."]),
    (5, None, ["'Be careful, Takashi, the pitcher spout is wide!' Whenever someone is about to trip or spill something, ", (None, '気をつけてください'), " is the go-to warning meaning 'please be careful'."]),
    (6, None, ["'Oh dear! Not a single drop spilled on the table, yet all of it is on my tie!' Borrowed from English 'necktie', ", (None, 'ネクタイ'), ' takes the brunt of the orange juice.']),
    (9, None, ["'Excuse me, Kazuko. I shall retreat to my office with dignity!' Stepping away politely from a guest uses ", (None, '失礼いたします'), ", the extra-courteous cousin of 'excuse me'."]),
]

TRANSITION = "Now let's listen to the whole breakfast spill scene again."

OUTRO = "Kazuko praised the eggs while Takashi's silk tie drank the orange juice. Next time, the front-desk phone rings with news about the blue suitcase."

CLOSING = ('kazuko', 'さようなら！')
