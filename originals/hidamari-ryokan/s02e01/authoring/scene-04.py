ID = 'hidamari-ryokan-s02e01-scene-04'
SHOW = 'hidamari-ryokan'
SEASON = 2
EPISODE = 1
SCENE = 4
TITLE = '白い布の下  (Under the White Sheet)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'kazuko': '和子', 'kenji': '健二'}

INTRO = 'Hearing excited voices down the hall, Room 4 guest Kazuko walks over with her morning teacup just as Mio and Kenji reach the tall shape under the white cloth. Listen first.'

STORY = [
    ('kazuko', 'おはようございます！どうして皆さん、廊下の壁の中に立っているんですか？', 'Good morning! Why is everyone standing inside the hallway wall?'),
    ('mio', '和子さん、来てください！九号室を見つけました！', 'Kazuko, come and look! We found Room Nine!'),
    ('kazuko', 'まあ、素敵なアーチの窓！中に入ってもいいですか？', 'Goodness, what lovely arched windows! May I come inside?'),
    ('kenji', '足元のほこりに気をつけて、和子さん。この白い布を一緒にたたみましょう。', "Mind the dust at your feet, Kazuko. Let's fold this white sheet together."),
    ('mio', '一、二……わあ！黒くて、ぴかぴかの木です！', 'One, two... wow! Dark, shiny wood!'),
    ('kazuko', 'アップライトピアノ！本物のくるみの木のピアノです！', 'An upright piano! A real walnut piano!'),
    ('kenji', 'ふたに気をつけて。何十年も閉まっていましたから。', 'Careful with the lid. It has been closed for decades.'),
    ('kazuko', '美央さん、白い鍵盤を見て。きれいで、一本も欠けていません。', "Mio, look at the white keys. They're clean, and not one is missing."),
    ('mio', 'どうぞ、和子さん！この家のために、何か弾いてください！', 'Go ahead, Kazuko! Play something for the house!'),
    ('kazuko', '聞いて……少し低くて、とても温かい音。あら、真ん中のレが鳴りません！', 'Listen... a little low, and very warm. Oh, the middle re makes no sound!'),
    ('kenji', '一つだけ、頑固な鍵盤が歌わないんですね？', "So just one stubborn key won't sing?"),
    ('kazuko', '健二さん、古いピアノは一回しっかり直せば、全部の歌を思い出しますよ。', 'Kenji, fix an old piano properly once, and it remembers every song.'),
]

OPENER = "A piano wakes up after decades of silence. Let's walk through six lines."

WALK = [
    (2, None, ["'Goodness, what lovely arched windows! May I come inside?' To ask permission, Kazuko adds 'is it all right' to 'come in': ", (None, '入ってもいいですか'), ". Swap in any action, like 'may I sit?'"]),
    (3, None, ["'Mind the dust at your feet, Kazuko. Let's fold this white sheet together.' Kenji warns her about her ", (None, '足元'), ", literally 'foot-base', the space right at your feet. And ", (None, 'たたみましょう'), " means 'let's fold'."]),
    (4, None, ["'One, two... wow! Dark, shiny wood!' Polished wood is ", (None, 'ぴかぴか'), ', a sparkly sound word that Japanese uses for anything shiny and clean.']),
    (6, None, ["'Careful with the lid. It has been closed for decades.' Kenji's ", (None, '何十年も'), " means 'for decades', literally 'how-many tens of years, even'."]),
    (7, None, ["'Mio, look at the white keys. They're clean, and not one is missing.' The word for piano keys is ", (None, '鍵盤'), ", built from 'key' and 'board', and ", (None, '欠けていません'), " means 'nothing is missing'."]),
    (8, None, ["'Go ahead, Kazuko! Play something for the house!' Playing an instrument uses its own word in Japanese: ", (None, '弾いてください'), " is 'please play', only for pianos, guitars and other things you touch."]),
]

TRANSITION = "Now let's listen to the whole piano scene again."

OUTRO = 'Beneath the dust sheet stands a warm walnut piano with eighty-seven working keys and one silent middle note. See you in the next scene.'

CLOSING = ('kazuko', 'また会いましょう！')
