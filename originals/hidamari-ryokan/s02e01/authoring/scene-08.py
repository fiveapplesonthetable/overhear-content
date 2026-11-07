ID = 'hidamari-ryokan-s02e01-scene-08'
SHOW = 'hidamari-ryokan'
SEASON = 2
EPISODE = 1
SCENE = 8
TITLE = "スイッチにさわらないで  (Don't Touch That Switch)"
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kenji': '健二', 'takashi': '隆', 'mio': '美央'}

INTRO = 'Back at the doorway of Room 9, Kenji opens his leather tool bag to inspect the old brass wall switch, but an excited Takashi reaches past him beside Mio. Listen first.'

STORY = [
    ('kenji', '隆さん、その真鍮のスイッチにさわる前に、一分待ってよ。', 'Takashi, wait one minute before you touch that brass switch.'),
    ('takashi', 'どうしてですか？このガラスのランプ、覚えています。きれいに光りますよ！', 'Why? I remember this glass lamp. It glows so beautifully!'),
    ('mio', '隆さん、待ってください！健二さんがドライバーを出していますよ！', 'Takashi, wait! Kenji has his screwdriver out!'),
    ('takashi', '一回だけカチッと……パン！……あれっ？', 'Just one click... bang! ...Huh?'),
    ('mio', '今の大きい音は何ですか！？廊下からです！', 'What was that loud noise just now?! It came from the hallway!'),
    ('kenji', '古い電線のせいで、一階のヒューズが飛んだんだ。', 'The old wire blew the ground-floor fuse.'),
    ('takashi', 'ロビーのランプが消えました！キッチンのオーブンも壊しましたか！？', 'The lobby lamp went out! Did I break the kitchen oven too?!'),
    ('mio', 'あっ、暗いキッチンから由香さんが呼んでいます！', 'Uh-oh, Yuka is calling from the dark kitchen!'),
    ('kenji', '三十年前の布の電線だよ、隆さん。俺が中を見る前に、スイッチにさわるな。', "It's thirty-year-old cloth wire, Takashi. Never touch a switch before I look inside."),
    ('takashi', 'お昼の前に直せますか、健二さん？予備のヒューズがあると言ってください！', 'Can you fix it before lunch, Kenji? Please tell me you have spare fuses!'),
    ('kenji', 'キッチンは二分で直せる。でも九号室には、新しい銅の電線がいるな。', 'I can fix the kitchen in two minutes. But Room Nine needs new copper wire.'),
    ('mio', '隆さん、懐中電灯をしっかり持ってください。六日のカウントダウンが始まりました！', 'Takashi, hold the flashlight steady. Our six-day countdown has begun!'),
]

OPENER = "One impatient click, and the lights go out. Let's walk through six lines."

WALK = [
    (2, None, ["'Takashi, wait! Kenji has his screwdriver out!' In Japanese a ", (None, 'ドライバー'), " is a screwdriver, borrowed from English 'driver', not the person at the wheel."]),
    (5, None, ["'The old wire blew the ground-floor fuse.' The word for electric wire is ", (None, '電線'), ", 'electric line'. A blown fuse ", (None, '飛んだ'), ", literally 'flew', in Japanese."]),
    (6, None, ["'The lobby lamp went out! Did I break the kitchen oven too?!' When a light goes out, it ", (None, '消えました'), ", from the word for 'disappear'. The same word is used for a candle or a sound fading away."]),
    (8, None, ["'It's thirty-year-old cloth wire, Takashi. Never touch a switch before I look inside.' Kenji's ", (None, 'さわるな'), " is a blunt 'don't touch', a short command ending that only works with people you know well. It is how a gruff handyman talks to his own boss."]),
    (9, None, ["'Can you fix it before lunch, Kenji? Please tell me you have spare fuses!' Takashi begs for ", (None, '予備'), ", the word for 'spare' or 'backup', handy for spare keys and spare batteries too."]),
    (11, None, ["'Takashi, hold the flashlight steady. Our six-day countdown has begun!' The word for flashlight is ", (None, '懐中電灯'), ", literally a 'pocket electric lamp', from the days when people kept a light in their kimono."]),
]

TRANSITION = "Now let's replay the whole fuse scene from start to finish."

OUTRO = 'One impatient click from Takashi pops the ground-floor fuse and proves Room 9 needs fresh wiring before Friday! Episode 1 of Season 2 is complete. See you in Episode 2.'

CLOSING = ('kenji', 'じゃあ、またね！')
