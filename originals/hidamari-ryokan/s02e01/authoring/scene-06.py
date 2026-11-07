ID = 'hidamari-ryokan-s02e01-scene-06'
SHOW = 'hidamari-ryokan'
SEASON = 2
EPISODE = 1
SCENE = 6
TITLE = '五月のハガキ  (Postcards from May)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'yuka': '由香', 'kazuko': '和子', 'kenji': '健二'}

INTRO = "Back at the four-table café corner while Mio answers the front-desk phone, Yuka pours fresh tea for Kazuko and Kenji as they spread the old postcards from the cedar box across the table. Let's listen in first."

STORY = [
    ('yuka', 'この白黒の写真を見て！中庭の木がまだ小さい。一階の窓までしかないよ！', 'Look at this black-and-white photo! The courtyard tree is still small. It only reaches the ground-floor windows!'),
    ('kenji', '和子さん、その青いハガキの裏を読んでください。', 'Kazuko, please read the back of that blue postcard.'),
    ('kazuko', '「三十年前の五月十日。毎週金曜日の六時、九号室でお茶とピアノ」', "'May tenth, thirty years ago. Tea and piano in Room Nine, every Friday at six.'"),
    ('yuka', '毎週金曜日の六時！通りのみんなが、お茶と音楽のためにここに来たんだ！', 'Every Friday at six! The whole street came here for tea and music!'),
    ('kenji', '次のカードも見て。「パン屋さんと先生に、隅の椅子を二つ取っておいてください」', "Look at the next card too: 'Please save two corner chairs for the baker and the teacher.'"),
    ('kazuko', '素敵ですね。三十年前から、この家は近所の人をつないでいたんですね。', 'How lovely. Even thirty years ago, this house was bringing neighbours together.'),
    ('yuka', 'それに、来週の金曜日は、月の最初の金曜日だよ！', 'And next Friday is the first Friday of the month!'),
    ('kenji', '待て。来週の金曜日の六時に、九号室をまた開けたいのか？', 'Wait. You want to reopen Room Nine next Friday at six?'),
    ('yuka', '六日でガラスを洗って、雨戸をぬって、レモンタルトを焼く！', 'Six days to wash the glass, paint the shutters and bake lemon tarts!'),
    ('kazuko', '健二さん、あの鳴らない鍵盤を直してくれたら、喜んで六時に弾きます。', "Kenji, if you fix that silent key, I'll gladly play at six."),
    ('kenji', 'いいですよ。美央と隆さんに、金曜日の計画を話しに行こう！', "Deal. Let's go tell Mio and Takashi our Friday plan!"),
    ('yuka', 'ハガキを持って行こう！この写真を見たら、隆さんは絶対「はい」って言うよ！', "Bring the postcard! Once Takashi sees this photo, he'll definitely say yes!"),
]

OPENER = "Old postcards tell the room's story, full of days and times. Let's walk through six lines."

WALK = [
    (0, None, ["'Look at this black-and-white photo! The courtyard tree is still small. It only reaches the ground-floor windows!' The word for a black-and-white photo is ", (None, '白黒'), ", 'white-black', the colours in the opposite order from English. And ", (None, 'までしかない'), " means 'only reaches as far as'."]),
    (1, None, ["'Kazuko, please read the back of that blue postcard.' The back of a card or a coin is its ", (None, '裏'), ', and the front of the card has its own opposite word.']),
    (3, None, ["'Every Friday at six! The whole street came here for tea and music!' Yuka repeats ", (None, '毎週'), ", 'every week'. That same first part, meaning 'every', also builds 'every day' and 'every month'."]),
    (4, None, ["'Look at the next card too: 'Please save two corner chairs for the baker and the teacher.'' The old card asks to ", (None, '取っておいてください'), ": 'take' plus 'put aside', the polite chunk for 'please save it for me'."]),
    (8, None, ["'Six days to wash the glass, paint the shutters and bake lemon tarts!' Yuka strings her six-day plan together with linking endings: wash, then ", (None, 'ぬって'), " for 'paint', then bake. One ending links them all, like 'and then'."]),
    (10, None, ["'Deal. Let's go tell Mio and Takashi our Friday plan!' Kenji's ", (None, '話しに行こう'), " means 'let's go to tell'. Join any action to 'go' this way to say 'go and do it', like 'go and eat'."]),
]

TRANSITION = "Now let's listen to the whole postcard scene again."

OUTRO = 'Thirty years ago Room 9 welcomed the street every Friday at six, and now Yuka, Kazuko and Kenji are ready to bring the tradition back. See you next time.'

CLOSING = ('yuka', 'またね！')
