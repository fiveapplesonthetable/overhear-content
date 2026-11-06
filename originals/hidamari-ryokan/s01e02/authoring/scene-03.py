ID = 'hidamari-ryokan-s01e02-scene-03'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = 'おつりの計算  (Counting the Change)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'takashi': '隆', 'yuka': '由香'}

INTRO = 'Nine minutes later, Mio bursts back through the courtyard gate carrying two full bags of groceries for Yuka and Takashi. Listen to the scene first.'

STORY = [
    ('mio', '九分でした！牛乳と卵とりんご、買って来ましたよ！', 'Nine minutes! I bought the milk, the eggs, and the apples!'),
    ('yuka', '美央ちゃん、救世主だね！コーヒーマシンのためにまず牛乳をちょうだい。', 'Mio, you are a lifesaver! Hand me the milk first for the coffee machine.'),
    ('takashi', '見事な速さです！お店の人から領収書をもらいましたか？', 'Impressive speed! Did you get a receipt from the shopkeeper?'),
    ('mio', 'はい、ここです！全部で三千八百円だったので、おつりは千二百円です。', 'Right here! Everything cost three thousand eight hundred yen, so the change is twelve hundred yen.'),
    ('takashi', '千円、百円、二百円。一円も狂いなくぴったりです。ありがとう！', 'One thousand, one hundred, two hundred yen. Exact to the very last yen—thank you!'),
    ('yuka', 'ちょっと待って、美央ちゃん……どのバターを取って来たの？', 'Wait a second, Mio... which butter did you grab?'),
    ('mio', '一番上の棚にあった金色の包みですけど。どうして？', 'The gold wrapper on the top shelf. Why?'),
    ('yuka', 'これ、塩が強い有塩バターだよ！甘いジャムパンには無塩バターがいるの！', 'This is salty salted butter! My sweet jam rolls need unsalted butter!'),
    ('mio', 'ええっ！走っていたから、包みが全部同じに見えました！', 'Oh no! Because I was running, all the wrappers looked identical!'),
    ('takashi', '甘い苺ジャムに、しょっぱいバターを出しても大丈夫でしょうか？', 'Can we really serve salty butter alongside sweet strawberry jam?'),
    ('yuka', '待って……塩バターはジャムには向かないけど、スクランブルエッグには最高だよ！', 'Hold on—salted butter is bad for jam, yet amazing for scrambled eggs!'),
    ('mio', 'よかった！機転のおかげで朝ごはんが助かりましたね。', 'What a relief! Quick thinking saved breakfast again.'),
]

OPENER = "Prices in yen, exact change, and sweet versus salty flavours drive this scene. Let's hear six lines again."

WALK = [
    (1, None, ["'Mio, you are a lifesaver! Hand me the milk first for the coffee machine.' Between close friends or casual colleagues, ", (None, 'ちょうだい'), " is the warm everyday way to say 'please give me'."]),
    (3, None, ["'Right here! Everything cost three thousand eight hundred yen, so the change is twelve hundred yen.' Shopping sums start with ", (None, '全部で'), ", meaning 'in total', while ", (None, 'おつり'), " is the essential shop word for 'change'."]),
    (4, None, ["'One thousand, one hundred, two hundred yen. Exact to the very last yen—thank you!' When numbers, sizes, or timing match without a gap, Japanese uses ", (None, 'ぴったり'), " for 'exact' or 'just right'."]),
    (7, None, ["'This is salty salted butter! My sweet jam rolls need unsalted butter!' Taste contrasts are crystal clear here: ", (None, '塩'), " means 'salt', while ", (None, '甘い'), " means 'sweet'."]),
    (9, None, ["'Can we really serve salty butter alongside sweet strawberry jam?' In spoken Japanese, salty food is described as ", (None, 'しょっぱい'), ', paired here with ', (None, '苺ジャム'), " for 'strawberry jam'."]),
    (11, None, ["'What a relief! Quick thinking saved breakfast again.' Exhale with ", (None, 'よかった'), " — literally 'it was good' — whenever something turns out well after a scare."]),
]

TRANSITION = "Now let's replay the whole grocery return from start to finish."

OUTRO = 'A gold packet of salted butter nearly caused a jam disaster until Yuka turned it into rich scrambled eggs. See you next time in the café corner.'

CLOSING = ('yuka', 'またね！')
