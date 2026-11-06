ID = 'hidamari-ryokan-s01e02-scene-04'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 2
SCENE = 4
TITLE = '中庭のハーブ  (Herbs from the Courtyard)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kenji': '健二', 'yuka': '由香', 'mio': '美央'}

INTRO = 'In the kitchen, Yuka whisks the eggs while Kenji walks in holding fresh green herbs clipped from the courtyard pot and Mio sets the four tables. Listen first.'

STORY = [
    ('kenji', '中庭まで、バターがどうとかいう大声が聞こえたぞ。', 'I heard loud voices about butter all the way out in the courtyard.'),
    ('yuka', '美央ちゃんが塩バターを買って来たから、今日は洋風の卵料理だよ！', 'Mio bought salted butter, so today we are making Western-style eggs!'),
    ('kenji', 'いいじゃないか。出す前に、この新鮮な緑のハーブを上に乗せなよ。', 'Sounds good. Put these fresh green herbs on top before serving.'),
    ('mio', '健二さん、そのハーブは自分で育てたんですか？', 'Kenji, did you grow those herbs yourself?'),
    ('kenji', '誰かが中庭の鉢植えを世話しないといけないからな。', 'Somebody has to look after the potted plants in the courtyard.'),
    ('yuka', 'いい香り！温かいパンに、熱々の卵と新鮮なハーブだね。', 'What a lovely aroma! Warm bread, piping-hot eggs, and fresh herbs.'),
    ('mio', '小さいスプーンとナプキンはどこに置きますか？', 'Where should I place the small spoons and napkins?'),
    ('yuka', '青いカップの横に、ナプキンを一枚と小さいスプーンを一本ずつ置いて。', 'Put one napkin and one small spoon beside every blue cup.'),
    ('kenji', '時計は七時二十九分だ。お客さんたちが階段を下りて来るぞ。', 'My watch says seven twenty-nine. The guests are coming down the stairs.'),
    ('mio', 'テーブルが四つ、椅子が八脚、全部並びました！', 'Four tables, eight chairs, everything is lined up in place!'),
    ('yuka', '美央ちゃん、急須にお湯を注いで！みんな来たよ！', 'Mio, pour the hot water into the teapot! Here comes everyone!'),
    ('kenji', '二日目にしては悪くないな、新人。', 'Not bad at all for your second day, rookie.'),
]

OPENER = "Setting tables, counting spoons and chairs, and pouring hot tea bring practical everyday words. Let's listen closely."

WALK = [
    (2, None, ["'Sounds good. Put these fresh green herbs on top before serving.' Notice ", (None, '出す前に'), ", meaning 'before serving', built around ", (None, '前に'), " for 'before'."]),
    (3, None, ["'Kenji, did you grow those herbs yourself?' Doing something on your own uses ", (None, '自分で'), ", 'by oneself', paired with ", (None, '育てた'), ' from the word for raising plants or children.']),
    (5, None, ["'What a lovely aroma! Warm bread, piping-hot eggs, and fresh herbs.' Doubling 'hot' gives ", (None, '熱々'), ', a vivid sound-like word for food that is piping hot straight from the pan.']),
    (7, None, ["'Put one napkin and one small spoon beside every blue cup.' Adding ", (None, 'ずつ'), " after a quantity means 'one each', distributing items evenly across ", (None, '青いカップ'), ', the blue cups.']),
    (10, None, ["'Mio, pour the hot water into the teapot! Here comes everyone!' Japanese has separate words for cold water and hot water: ", (None, 'お湯'), ' always means hot water, poured here into ', (None, '急須'), ', a teapot.']),
    (11, None, ["'Not bad at all for your second day, rookie.' Kenji's gruff praise ends on ", (None, '新人'), ", literally 'new person', the standard workplace word for a newcomer."]),
]

TRANSITION = "Now let's hear the whole breakfast preparation scene again."

OUTRO = 'With sixty seconds to spare, all four tables are ready and fragrant with courtyard herbs. Next time, the morning guests sit down for breakfast.'

CLOSING = ('kenji', 'じゃあね！')
