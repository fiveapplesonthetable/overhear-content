ID = 'hidamari-ryokan-s01e03-scene-07'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 3
SCENE = 7
TITLE = '手帳を返しに  (Returning the Notebook)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'haruto': '陽翔'}

INTRO = "Mio climbs back up to the attic door to return Haruto's leather notebook, trying to act completely natural while suspecting he inspects inns for a living. Listen first."

STORY = [
    ('mio', 'すみません、陽翔さん。夜分にお邪魔して申し訳ありません。', 'Excuse me, Haruto. Sorry to disturb you so late in the evening.'),
    ('haruto', 'あっ、私の革の手帳！ありがとうございます！ちょうど探していたんです。', 'Oh, my leather notebook! Thank you! I was looking for it right now.'),
    ('mio', '一階のカウンターの、スープのカップの横にありました。', 'It was beside the soup cup on the first-floor counter.'),
    ('haruto', '今週の通りの記録が全部入っているんです。助かりました。', 'All my street notes from this week are inside here. You saved me.'),
    ('mio', 'うちの中庭が、陽翔さんの……お仕事に静かでよかったです。', 'We are glad our courtyard is peaceful for your... work.'),
    ('haruto', '本当に静かですよ！……でも今、洗面所の方から変な金属の音がしませんでしたか？', 'Truly peaceful! ...Though did a strange metallic knock just come from the washroom?'),
    ('mio', 'はい！隅のお湯のパイプから聞こえたみたいです。', 'Yes! It sounded like it came from the hot-water pipe in the corner.'),
    ('haruto', '蛇口のパイプを触ってみてください。上は温かいのに、下がぬるくなっています。', 'Touch the tap pipe: the top is warm, yet the bottom is turning lukewarm.'),
    ('mio', 'あっ！古いパイプには、夜たまに空気が入ることがあるんです。', 'Oh! Sometimes a little air gets into old pipes at night.'),
    ('haruto', '暖かい毛布がありますし、今夜のお風呂はもう済ませたので大丈夫ですよ。', 'I have a warm blanket, and I already washed up tonight, so I am fine.'),
    ('mio', '優しいお言葉をありがとうございます！すぐ健二さんが地下室を見ますね。', 'Thank you for being so understanding! Kenji will check the basement right away.'),
    ('haruto', 'おやすみなさい、美央さん。また明日の朝ごはんの時に。', 'Good night, Mio. See you at breakfast tomorrow morning.'),
]

OPENER = "Polite evening phrases and checking the washbasin hot-water pipe shape this quiet two-person scene. Let's review six lines."

WALK = [
    (0, None, ["'Excuse me, Haruto. Sorry to disturb you so late in the evening.' Knocking on someone's door politely uses ", (None, 'お邪魔して'), ", from the phrase meaning 'intruding on your space'."]),
    (1, None, ["'Oh, my leather notebook! Thank you! I was looking for it right now.' Looking for a misplaced item uses ", (None, '探していた'), ", meaning 'was searching for'."]),
    (3, None, ["'All my street notes from this week are inside here. You saved me.' Thank someone who rescues you from a jam with ", (None, '助かりました'), ", literally 'I was saved' or 'that really helped'."]),
    (7, None, ["'Touch the tap pipe: the top is warm, yet the bottom is turning lukewarm.' Look at the water temperature words: ", (None, '蛇口'), " literally means 'snake mouth' for a water tap, and ", (None, 'ぬるく'), " comes from 'lukewarm'."]),
    (9, None, ["'I have a warm blanket, and I already washed up tonight, so I am fine.' Bedding adds ", (None, '毛布'), ", literally 'wool cloth' for 'blanket', alongside ", (None, 'お風呂'), " for 'bath'."]),
    (11, None, ["'Good night, Mio. See you at breakfast tomorrow morning.' End any evening politely with ", (None, 'おやすみなさい'), ", the standard Japanese 'good night'."]),
]

TRANSITION = "Now let's listen to the upstairs notebook scene again."

OUTRO = 'Haruto got his notebook back smoothly, yet that cooling hot-water pipe spells trouble below. One final scene in Episode 3—down by the cellar door! See you next time.'

CLOSING = ('haruto', 'また明日！')
