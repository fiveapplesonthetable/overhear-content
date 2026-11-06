ID = 'hidamari-ryokan-s01e06-scene-05'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 6
SCENE = 5
TITLE = '二枚目、第十四条  (Page Two, Clause Fourteen)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'takashi': '隆', 'haruto': '陽翔', 'mio': '美央'}

INTRO = 'At the front desk, Takashi hands the two-page notice to Haruto while Mio holds her breath beside the paper ledger. Haruto flips straight to the second sheet. Listen first.'

STORY = [
    ('takashi', '陽翔さん、一枚目を見てください。「来月より商業オフィスへ改装」……もう終わりです！', "Haruto, look at page one: 'conversion to commercial offices starting next month'... we are finished!"),
    ('haruto', 'ちょっと待ってください、隆さん。下に留めてある二枚目を読みましたか？', 'Wait a moment, Takashi. Did you read the second page clipped underneath?'),
    ('takashi', '小さな灰色の数字ばかりですよ！一枚目で心臓が止まってしまいました！', 'It is nothing except tiny grey numbers! My heart stopped at page one!'),
    ('mio', '隆さん、陽翔さんが鉛筆で指している場所を見てください！', 'Takashi, look at the spot Haruto is pointing to with his pencil!'),
    ('haruto', '『大阪旧市街保存条例』の第十四条です……窓の外で兄も今うなずきました！', 'Clause fourteen of the Osaka Old Quarter Preservation Bylaw... and my brother outside the window just nodded!'),
    ('takashi', 'わかりやすい言葉でお願いします！第十四条には何と書いてありますか？', 'In plain words, please! What is written in Clause fourteen?'),
    ('haruto', '築八十年以上の中庭建築は、一階が毎日近所の人々に開かれていれば、専用オフィスに変えられません。', 'No courtyard building over eighty years old can be turned into private offices if its first floor serves neighbours daily.'),
    ('mio', '「毎日近所の人々に開かれている」……地域の朝カフェみたいにですか！？', "'Open to neighbours every day'... like a neighbourhood morning café?!"),
    ('haruto', 'その通りです！今は四つのテーブルが宿泊のお客さま専用になっていますよね。', 'Exactly! Right now your four tables are only for overnight guests.'),
    ('takashi', '待ってください……毎朝、近所のコーヒーとパンのために中庭の門を開ければ……', 'Hold on... if we open our courtyard gate every morning for neighbourhood coffee and bread...'),
    ('haruto', '市の条例によって、旅館の賃貸契約はあと十年間しっかり守られます！', "Under city bylaw, your inn's lease is firmly protected for another ten years!"),
    ('mio', '隆さん！嬉しい理由で、鼻から眼鏡がずり落ちましたよ！', 'Takashi! Your glasses just slipped down your nose for a happy reason!'),
]

OPENER = "Page two turns panic into joy with everyday words for months, mornings, and ten more years. Let's review six lines."

WALK = [
    (0, None, ["'Haruto, look at page one: conversion to commercial offices starting next month... we are finished!' Pair 'this month' with ", (None, '来月'), ", literally 'coming month' for 'next month'."]),
    (5, None, ["'In plain words, please! What is written in Clause fourteen?' Whenever someone uses stiff technical language, ask for ", (None, 'わかりやすい言葉'), ", 'easy-to-understand words'."]),
    (6, None, ["'No courtyard building over eighty years old can be turned into private offices if its first floor serves neighbours daily.' Doing something every single day is ", (None, '毎日'), ', paired with ', (None, '以上'), " after a number to mean 'eighty years or more'."]),
    (9, None, ["'Hold on... if we open our courtyard gate every morning for neighbourhood coffee and bread...' Swap 'day' for 'morning' and you get ", (None, '毎朝'), ", 'every morning'."]),
    (10, None, ["'Under city bylaw, your inn's lease is firmly protected for another ten years!' Notice ", (None, 'あと十年間'), ", meaning 'for another ten years', and ", (None, '守られます'), " for 'is protected'."]),
    (11, None, ["'Takashi! Your glasses just slipped down your nose for a happy reason!' Good news shines through in ", (None, '嬉しい理由'), ", 'a happy reason'."]),
]

TRANSITION = "Now let's listen to the Clause 14 breakthrough again."

OUTRO = 'Page two saved the day: welcoming Osaka neighbours for morning bread and coffee protects the Hidamari Inn for ten full years! Next time, Takashi makes two big announcements.'

CLOSING = ('mio', 'またね！')
