ID = 'hidamari-ryokan-s01e02-scene-08'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = '一つの部屋に二つの予約  (Two Names, One Room)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'takashi': '隆', 'mio': '美央', 'kenji': '健二'}

INTRO = "On Wednesday evening as dusk settles over Osaka, Takashi steps out of his office holding both the tablet and Kenji's paper ledger, his face pale. Mio and Kenji look up immediately. Listen first."

STORY = [
    ('takashi', '健二さん……美央さん……今夜、六号室が空いていると言ってください。', 'Kenji... Mio... please tell me room six is free tonight.'),
    ('mio', 'いいえ、隆さん。六号室には一時間前に南から来たご夫婦が入りました。', 'No, Takashi. The couple from the south checked into room six an hour ago.'),
    ('kenji', '一番から七番まで鍵は全部出ているし、八号室はペンキが乾いていない。', 'Every key from one to seven is out, and room eight still has wet paint.'),
    ('takashi', 'ああ、大失敗です！昨日、眼鏡なしでタブレットに電話予約を入れてしまいました！', 'Oh, disaster! Yesterday I entered a phone booking on the tablet without my glasses!'),
    ('mio', '待ってください。タブレットの画面と紙の帳面を一緒に見ましょう。', "Hold on. Let's look at the tablet screen and the paper ledger side by side."),
    ('kenji', '当ててやろうか。空いていない部屋を誰かに約束したんだな？', 'Let me guess. You promised somebody a room that is not free?'),
    ('mio', '隆さん！七号室はもう埋まっているのに、七号室にもう一人予約が入っています！', 'Takashi! Room seven is already occupied, and a second guest is booked into room seven!'),
    ('takashi', 'しかもその方は、今夜八時にここへ着きます。あと四十分です！', "And he arrives here at eight o'clock this evening—in forty minutes!"),
    ('kenji', 'だからあのタブレットは罠だと言ったんだ。', 'Told you that tablet is a trap.'),
    ('takashi', '外は雨ですし、この通りのホテルはどこも満室です！どうしましょう？', 'It is raining outside and every hotel on this street is full! What shall we do?'),
    ('mio', '待ってください！階段の上の三階には何があるんですか？', 'Wait a moment! What is up on the third floor above the stairs?'),
    ('kenji', '日当たりのいい古い屋根裏の書斎だ……急いでついて来い！', 'The sunny old attic study... follow me, quickly!'),
]

OPENER = "Sold-out rooms, pouring rain, and a forty-minute countdown close Episode 2. Let's walk through six lines."

WALK = [
    (0, None, ["'Kenji... Mio... please tell me room six is free tonight.' When asking about an available room, seat, or time slot, Japanese uses ", (None, '空いている'), ", meaning 'open' or 'unoccupied'."]),
    (3, None, ["'Oh, disaster! Yesterday I entered a phone booking on the tablet without my glasses!' Notice ", (None, '昨日'), " for 'yesterday' and ", (None, '大失敗'), ", literally a 'big failure' or blunder."]),
    (4, None, ["'Hold on. Let's look at the tablet screen and the paper ledger side by side.' Doing an action together uses ", (None, '一緒に'), ", 'together', followed by ", (None, '見ましょう'), ", 'let's look'."]),
    (7, None, ["'And that guest arrives on the eight o'clock evening train—in forty minutes!' Putting ", (None, 'あと'), " before a time span means 'remaining' — so ", (None, 'あと四十分'), " is 'forty minutes left'."]),
    (9, None, ["'It is raining outside and every hotel on this street is full! What shall we do?' Every traveller in Osaka learns ", (None, '満室'), ", literally 'full rooms' for 'no vacancy', and ", (None, 'どうしましょう'), " for 'what shall we do?'."]),
    (10, None, ["'Wait a moment! What is up on the third floor above the stairs?' Counting building floors adds a counter that softens slightly in ", (None, '三階'), ", meaning 'the third floor'."]),
]

TRANSITION = "Now let's replay the whole double-booking cliffhanger without pauses."

OUTRO = "Two guests booked into Room 7, rain falling over Osaka, and forty minutes until the eight o'clock train! Episode 2 is complete—join us in Episode 3 to see if the third-floor attic can save the night."

CLOSING = ('takashi', 'また明日！')
