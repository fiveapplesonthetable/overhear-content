ID = 'hidamari-ryokan-s01e02-scene-07'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 2
SCENE = 7
TITLE = '午後のコーヒー休憩  (How Regulars Order)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'yuka': '由香', 'mio': '美央', 'kenji': '健二'}

INTRO = 'In the quiet afternoon sunshine, Mio takes a ten-minute break in the café corner while Yuka wipes the counter and Kenji tightens a wobbly wooden chair leg. Listen first.'

STORY = [
    ('yuka', '座って、美央ちゃん！今朝は町じゅう走ったんだから、コーヒーを飲んで。', 'Sit down, Mio! You ran all across town this morning, so drink some coffee.'),
    ('mio', 'わあ、嬉しい！ミルクと砂糖を少しお願いします。', 'Gladly! With milk and a little sugar, please.'),
    ('kenji', 'その角の椅子は気をつけろ。十秒待って、今このネジを締めるから。', 'Watch out for that corner chair. Wait ten seconds while I tighten this screw.'),
    ('mio', 'もう直ったんですか？健二さんはどこへでもドライバーを持ち歩くんですね！', 'Fixed already? Kenji, you carry a screwdriver everywhere!'),
    ('kenji', '古い建物は毎週火曜日にネジが一本緩むんだ。さあ座りな。', 'Old buildings loosen one screw every Tuesday. Go on, sit.'),
    ('yuka', 'ほら、朝の騒ぎも謎の電話もちゃんと乗り切ったじゃない！', 'Look, you made it right through the morning rush and the mystery phone call!'),
    ('mio', '正直に言うと、前の灰色のオフィスよりここの方がずっと好きです。', 'Honestly, I like this place far better than my old grey office.'),
    ('yuka', '金曜日の正午が楽しみだね！鞄の男が入って来るのを一番前で見たいな！', 'Wait until Friday at noon—I want a front-row view when Suitcase Man walks in!'),
    ('kenji', 'お客さんをじろじろ見るんじゃない。鞄を渡して、余計なことは聞かないんだ。', 'Do not stare at guests. We hand over the bag and mind our own business.'),
    ('yuka', 'ちょっと聞いてよ！本当は健二さんが私たちの二倍気になっているくせに！', 'Listen to him! Kenji is actually twice as curious as we are!'),
    ('kenji', '俺は安全を確認しているだけだ。それが仕事だからな。', 'I am simply checking safety. That is my job.'),
    ('mio', 'はいはい、健二さん。秘密はちゃんと守りますよ！', 'Sure thing, Kenji. Your secret is safe with us!'),
]

OPENER = "Coffee breaks and friendly teasing reveal how Japanese compares two things. Let's walk through six lines."

WALK = [
    (1, None, ["'Gladly! With milk and a little sugar, please.' Ordering 'a little' of something is effortless with ", (None, '少し'), ', placed right after ', (None, 'ミルクと砂糖'), " for 'milk and sugar'."]),
    (3, None, ["'Fixed already? Kenji, you carry a screwdriver everywhere!' Watch out for a classic false friend: in Japanese, ", (None, 'ドライバー'), " borrowed from English 'driver' usually means a screwdriver, not just a car driver!"]),
    (4, None, ["'Old buildings loosen one screw every Tuesday. Go on, sit.' Putting 'every' in front of 'week' builds ", (None, '毎週'), ', followed here by ', (None, '火曜日'), ", literally 'Fire Day' for 'Tuesday'."]),
    (6, None, ["'Honestly, I like this place far better than my old grey office.' Comparing two choices uses ", (None, 'より'), " for 'than' and ", (None, 'ずっと好き'), " for 'like much better'."]),
    (9, None, ["'Listen to him! Kenji is actually twice as curious as we are!' Doubling a number is easy with ", (None, '二倍'), ", meaning 'two times' or 'twice as much'."]),
    (11, None, ["'Sure thing, Kenji. Your secret is safe with us!' Mio promises to guard his ", (None, '秘密'), ", the everyday word for a 'secret'."]),
]

TRANSITION = "Now let's listen to the afternoon break scene again."

OUTRO = 'Warm coffee, a tightened screw, and three colleagues who already sound like old teammates. One final scene left in Episode 2—and Takashi is about to turn pale. See you next time.'

CLOSING = ('yuka', 'またね！')
