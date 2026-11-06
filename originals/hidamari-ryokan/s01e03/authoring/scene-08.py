ID = 'hidamari-ryokan-s01e03-scene-08'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 3
SCENE = 8
TITLE = '氷のように冷たいお湯  (Ice-Cold Pipes)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kenji': '健二', 'mio': '美央', 'takashi': '隆'}

INTRO = 'Down at the front desk, Mio and Takashi wait anxiously by the cellar stairs until Kenji climbs up wiping his hands on a rag and shaking his head. Listen first.'

STORY = [
    ('takashi', '健二さん、ただの小さな空気の泡だと言ってください！お願いです！', 'Kenji, please tell me it was only a tiny air bubble! Please!'),
    ('kenji', '悪い知らせだ。古いボイラーの真鍮の圧力バルブがついに壊れた。', 'Bad news. The brass pressure valve on the old boiler finally gave out.'),
    ('mio', 'えっ、じゃあ今夜は暖房も、洗面所のお湯も出ないんですか？', 'Wait, does that mean no heating tonight and no hot water at the taps either?'),
    ('kenji', 'レンガの壁が熱を保つから、部屋は朝まで暖かいままだよ、美央。', 'The brick walls hold heat, so the rooms will stay warm until morning, Mio.'),
    ('takashi', 'ああ、よかった！それで、明日の朝のシャワーやお湯はどうなりますか？', "Thank goodness! And what about tomorrow morning's showers and hot water?"),
    ('kenji', '明日の朝七時には、蛇口からもシャワーからも氷みたいに冷たい水しか出ない。', 'At seven tomorrow morning, only ice-cold water will come out of the taps and showers.'),
    ('takashi', '氷みたいに冷たいシャワー！？三階に『大阪旅行ガイド』の調査員がいるのに！？', 'Ice-cold showers?! With the Osaka Travel Guide inspector on the third floor?!'),
    ('mio', '道具箱の中に、予備の真鍮バルブはありませんか？', 'Is there no spare brass valve inside your toolbox?'),
    ('kenji', '最後の一個を冬に使ったんだ。橋の向こうの古い金物屋にしか、このサイズはない。', 'I used the last one in winter. Only the old hardware shop past the bridge carries this size.'),
    ('mio', 'その金物屋は、朝何時に開きますか？', 'What time in the morning does that hardware shop open?'),
    ('kenji', '七時ちょうどだ。朝ごはんの三十分前だな。', 'Seven sharp. Thirty minutes before breakfast.'),
    ('mio', '目覚ましをセットしてください、健二さん。明日の朝、冷たいシャワーに勝ちますよ！', 'Set your alarm, Kenji. Tomorrow morning we beat the cold showers!'),
]

OPENER = "Trouble with the boiler in the cellar brings time questions, cold water, and dawn plans. Let's walk through six lines."

WALK = [
    (1, None, ["'Bad news. The brass pressure valve on the old boiler finally gave out.' Kenji breaks it plainly with ", (None, '悪い知らせ'), ", meaning 'bad news', and ", (None, '壊れた'), " for 'broke down'."]),
    (5, None, ["'At seven tomorrow morning, only ice-cold water will come out of the taps and showers.' Notice ", (None, '氷みたいに冷たい水'), ", literally 'water cold like ice'."]),
    (7, None, ["'Is there no spare brass valve inside your toolbox?' Keep ", (None, '道具箱'), ", literally 'tool box', alongside ", (None, '予備'), " for a 'spare' or backup part."]),
    (8, None, ["'I used the last one in winter. Only the old hardware shop past the bridge carries this size.' Across ", (None, '橋の向こう'), ", 'beyond the bridge', sits ", (None, '金物屋'), ", literally 'metal-things shop' for 'hardware store'."]),
    (9, None, ["'What time in the morning does that hardware shop open?' Asking opening hours anywhere uses ", (None, '何時に開きますか'), ", meaning 'at what time does it open?'."]),
    (11, None, ["'Set your alarm, Kenji. Tomorrow morning we beat the cold showers!' Mio rallies him with ", (None, '明日の朝'), ", 'tomorrow morning', and ", (None, '勝ちます'), ", meaning 'we will win'."]),
]

TRANSITION = "Now let's hear the Episode 3 cellar cliffhanger again."

OUTRO = 'A suspected guide inspector on the third floor, a cracked boiler valve in the cellar, and a 7:00 AM dash across the bridge! Episode 3 is complete—see you in Episode 4.'

CLOSING = ('kenji', 'また明日！')
