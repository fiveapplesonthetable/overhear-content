ID = 'hidamari-ryokan-s01e04-scene-01'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = '朝六時四十五分  (Six Forty-Five)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kenji': '健二', 'mio': '美央'}

INTRO = 'It is six forty-five in the morning at the Hidamari Inn in Osaka. While the guests still sleep upstairs, Kenji draws a quick street map on paper for Mio. Listen to the whole scene first.'

STORY = [
    ('mio', 'おはようございます、健二さん！上のシャワーはもう本当に冷たいんですか？', 'Good morning, Kenji! Are the showers upstairs really cold already?'),
    ('kenji', '川の水みたいに冷たいよ。この壊れた真鍮バルブをコートのポケットに入れな。', 'As cold as river water. Put this broken brass valve in your coat pocket.'),
    ('mio', '入れました。さあ、金物屋への行き方を教えてください。', 'Got it. Now please tell me how to get to the hardware shop.'),
    ('kenji', 'うちの門を出たら左へ曲がって、石の橋までまっすぐ歩くんだ。', 'Step out our gate, turn left, and walk straight to the stone bridge.'),
    ('mio', '門を左ですね、橋までまっすぐ。川を渡るんですか？', 'Left at the gate, straight to the bridge. Do I cross the river?'),
    ('kenji', 'ああ、橋を渡ったら、右手にある緑の薬局を通り過ぎる。', 'Yeah, once you cross the bridge, pass the green pharmacy on your right.'),
    ('mio', '橋を渡って、右に緑の薬局ですね。そのあとは？', 'Cross the bridge, green pharmacy on the right. And after that?'),
    ('kenji', '小さな広場へ左に曲がる。青い木のドアを探すんだ。', 'Turn left into the small square. Look for a blue wooden door.'),
    ('mio', 'お店の外に大きな看板はありますか？', 'Is there a big sign outside the shop?'),
    ('kenji', 'ドアの上に、金色の鍵の絵があるだけだ。店員にこのバルブを見せな。', 'Only a painted golden key above the door. Show this valve to the clerk.'),
    ('mio', '二十ミリ、真鍮、ボイラーのバルブ……走りながらずっと唱えます！', 'Twenty millimetres, brass, boiler valve... I will repeat it the whole way!'),
    ('kenji', '急いで走れよ、美央。四号室は七時十五分に起きるぞ！', 'Run fast, Mio. Room four wakes up at seven fifteen!'),
]

OPENER = "Asking and giving street directions across town is one of the best A1 survival skills. Let's walk through six lines."

WALK = [
    (1, None, ["'As cold as river water. Put this broken brass valve in your coat pocket.' Comparing temperatures is vivid with ", (None, '川の水みたいに'), ", literally 'just like river water'."]),
    (2, None, ["'Got it. Now please tell me how to get to the hardware shop.' Adding 'way' onto 'go' builds ", (None, '行き方'), ", the essential travel word for 'directions' or 'how to get there'."]),
    (3, None, ["'Step out our gate, turn left, and walk straight to the stone bridge.' Every direction-giver uses ", (None, 'まっすぐ'), ", meaning 'straight ahead', right up to ", (None, '石の橋'), ", 'the stone bridge'."]),
    (4, None, ["'Left at the gate, straight to the bridge. Do I cross the river?' Moving from one bank to the other uses ", (None, '川を渡る'), ", meaning 'to cross the river'."]),
    (5, None, ["'Yeah, once you cross the bridge, pass the green pharmacy on your right.' Notice ", (None, '薬局'), ", literally 'medicine bureau' for 'pharmacy', preceded by ", (None, '緑'), " for 'green'."]),
    (8, None, ["'Is there a big sign outside the shop?' Small shop fronts are easy to spot when you ask for ", (None, '大きな看板'), ", 'a big signboard'."]),
]

TRANSITION = "Now let's listen to Kenji's dawn street directions again."

OUTRO = 'Left outside the gate, across the stone bridge, past the green pharmacy, and left into the square—Mio is on the run. See you next time.'

CLOSING = ('mio', 'またね！')
