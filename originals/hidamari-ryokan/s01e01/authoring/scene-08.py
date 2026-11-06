ID = 'hidamari-ryokan-s01e01-scene-08'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = '石段の上の鞄  (Left on the Step)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'kenji': '健二'}

INTRO = 'It is nearly nine at night, and the courtyard lanterns glow softly as Mio wraps up her first shift with Kenji. Suddenly, the front gate bell rings once in the quiet night. Listen first.'

STORY = [
    ('mio', '健二さん、今の聞こえましたか？門のベルが鳴りました！', 'Kenji, did you hear that just now? The gate bell rang!'),
    ('kenji', '夜の九時に？ここにいて、一緒にドアを開けよう。', "At nine at night? Stay close, let's open the door together."),
    ('mio', 'すみません！こんばんは！……中庭には誰も立っていませんよ！', 'Hello? Good evening! ...Nobody is standing in the courtyard!'),
    ('kenji', '待てよ。足元の石段を見てごらん。', 'Hold on. Look down at the stone step.'),
    ('mio', 'もう一つの濃い青いスーツケース！これ、和子さんの鞄ですか？', "Another dark-blue suitcase! Is this Kazuko's bag?"),
    ('kenji', 'ファスナーを見よう……ああ、和子さんのイニシャルがここにある！', "Let's check the zipper... yes, Kazuko's initials are right here!"),
    ('mio', 'どうしてその人は、自分の鞄を受け取らずに逃げたんでしょう？', 'Why did that person run away without taking back their own bag?'),
    ('kenji', '見ろ、持ち手に白い封筒がテープで貼ってあるぞ。', 'Look, a white envelope is taped onto the handle.'),
    ('mio', '読みますね。「間違えてすみません。青い鞄を金曜日まで預かってください。」', "Let me read it: 'Sorry for the mistake. Please keep my blue bag until Friday.'"),
    ('kenji', '金曜日まで？名前も署名もないじゃないか！', 'Until Friday? There is no name and no signature!'),
    ('mio', 'どうして金曜まで、靴や木の汽車を知らない宿に預けるんでしょう？', 'Why leave your shoes and wooden train with strangers until Friday?'),
    ('kenji', 'ひだまり旅館へようこそ、美央。二日目も退屈しないぞ。', "Welcome to the Hidamari Inn, Mio. Your second day won't be boring either."),
]

OPENER = "Evening greetings, a mystery envelope, and a Friday deadline close Episode 1. Let's hear the key lines up close."

WALK = [
    (0, None, ["'Kenji, did you hear that just now? The gate bell rang!' Mio asks ", (None, '聞こえましたか'), ", meaning 'could you hear it?' — Japanese distinguishes hearing a sound naturally from actively listening."]),
    (2, None, ["'Hello? Good evening! ...Nobody is standing in the courtyard!' After dark, the standard greeting switches to ", (None, 'こんばんは'), " for 'good evening', while ", (None, '中庭'), " literally joins 'middle' and 'garden' for 'courtyard'."]),
    (7, None, ["'Look, a white envelope is taped onto the handle.' Listen for ", (None, '白い封筒'), ", meaning 'white envelope', attached to ", (None, '持ち手'), ", literally the 'holding hand' or 'handle'."]),
    (8, None, ["'Let me read it: Sorry for the mistake. Please keep my blue bag until Friday.' The mystery writer asks ", (None, '金曜日まで'), ", 'until Friday', using ", (None, '預かってください'), " for 'please keep safe in your care'."]),
    (9, None, ["'Until Friday? There is no name and no signature!' Pairing two missing things uses ", (None, 'も'), ' twice in a row — neither ', (None, '名前'), ', a name, nor ', (None, '署名'), ', a signature.']),
    (11, None, ["'Welcome to the Hidamari Inn, Mio. Your second day won't be boring either.' Kenji welcomes her with ", (None, 'ようこそ'), ", 'welcome', and ", (None, '二日目'), " means 'day two'."]),
]

TRANSITION = "Now let's listen to the whole late-night cliffhanger again."

OUTRO = "Kazuko's suitcase is back on the step, yet the stranger vanished into the Osaka night and asked them to guard his bag until Friday. Episode 1 is complete—see you next time for Episode 2!"

CLOSING = ('kenji', 'また明日！')
